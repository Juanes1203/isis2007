# CampusFlow — Esquema de base de datos

PostgreSQL 16. Migraciones con Alembic. Este documento refleja el estado en `head`.
Si cambia el esquema, cambia primero la migración y después este archivo.

Siete tablas: `users`, `courses`, `enrollments`, `deliverables`, `documents`, `chunks`,
`reminders`. No hay más. Si una conversación necesita una octava tabla, eso es una decisión
de producto, no un detalle de implementación.

## 0. Extensiones y convenciones

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";   -- gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS "vector";     -- pgvector
CREATE EXTENSION IF NOT EXISTS "pg_trgm";    -- búsqueda léxica auxiliar
```

Convenciones duras:

- Claves primarias `uuid` con `gen_random_uuid()`. Nada de enteros autoincrementales expuestos.
- Nombres de tabla en plural, en minúscula, `snake_case`.
- **Todo instante es `timestamptz` y se guarda en UTC.** Ver ADR-04 en `architecture.md`.
  Nunca `timestamp` a secas: una columna naive es exactamente el bug que ya nos costó
  mostrar como vencida una entrega que vence hoy a las 23:59 en Bogotá.
- `created_at` y `updated_at` en toda tabla, con `DEFAULT now()`.
- Borrado en cascada solo donde la fila hija no tiene sentido sin el padre.

## 1. users

```sql
CREATE TABLE users (
    id            uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
    email         citext      NOT NULL UNIQUE,
    full_name     text        NOT NULL,
    password_hash text        NOT NULL,
    timezone      text        NOT NULL DEFAULT 'America/Bogota',
    is_active     boolean     NOT NULL DEFAULT true,
    created_at    timestamptz NOT NULL DEFAULT now(),
    updated_at    timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT users_email_len CHECK (char_length(email) BETWEEN 5 AND 254)
);
```

`password_hash` guarda bcrypt, nunca la contraseña. La columna no se selecciona en ningún
schema Pydantic de salida.

## 2. courses

```sql
CREATE TABLE courses (
    id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
    code       text        NOT NULL,
    name       text        NOT NULL,
    term       text        NOT NULL,                       -- '2026-20'
    timezone   text        NOT NULL DEFAULT 'America/Bogota',
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT courses_code_term_uniq UNIQUE (code, term)
);
```

`timezone` es la zona en la que el profesor piensa las fechas. `due_at` se guarda en UTC;
para mostrar "vence hoy" se convierte con esta zona, no con la del servidor.

## 3. enrollments

```sql
CREATE TYPE enrollment_role AS ENUM ('student', 'monitor', 'professor');

CREATE TABLE enrollments (
    id         uuid            PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id    uuid            NOT NULL REFERENCES users(id)   ON DELETE CASCADE,
    course_id  uuid            NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    role       enrollment_role NOT NULL DEFAULT 'student',
    created_at timestamptz     NOT NULL DEFAULT now(),
    CONSTRAINT enrollments_uniq UNIQUE (user_id, course_id)
);

CREATE INDEX enrollments_user_idx   ON enrollments (user_id);
CREATE INDEX enrollments_course_idx ON enrollments (course_id);
```

Esta tabla es la frontera de autorización de todo el sistema: si no hay fila aquí,
el usuario no ve el curso, ni sus documentos, ni sus entregas.

## 4. deliverables

```sql
CREATE TABLE deliverables (
    id              uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id       uuid        NOT NULL REFERENCES courses(id)   ON DELETE CASCADE,
    created_by      uuid            NULL REFERENCES users(id)     ON DELETE SET NULL,
    source_doc_id   uuid            NULL REFERENCES documents(id) ON DELETE SET NULL,
    title           text        NOT NULL,
    description     text            NULL,
    due_at          timestamptz NOT NULL,        -- SIEMPRE UTC
    weight_pct      numeric(5,2)    NULL,
    estimated_hours numeric(5,2)    NULL,
    created_at      timestamptz NOT NULL DEFAULT now(),
    updated_at      timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT deliverables_hours_nonneg  CHECK (estimated_hours IS NULL OR estimated_hours >= 0),
    CONSTRAINT deliverables_weight_range  CHECK (weight_pct IS NULL OR (weight_pct >= 0 AND weight_pct <= 100)),
    CONSTRAINT deliverables_title_nonempty CHECK (char_length(btrim(title)) > 0)
);

-- La agenda ordena por due_at dentro de los cursos del usuario: este índice es el que importa.
CREATE INDEX deliverables_course_due_idx ON deliverables (course_id, due_at);
CREATE INDEX deliverables_due_idx        ON deliverables (due_at);
```

Nota de UTC: `due_at` es un instante, no una fecha de pared. Una entrega "hoy a las 23:59"
en Bogotá se guarda como el día siguiente a las `04:59Z`. Cualquier comparación con
`datetime.utcnow()` (naive) o con `date.today()` está mal por construcción.

## 5. documents

```sql
CREATE TYPE document_status AS ENUM ('pending', 'processing', 'ready', 'failed');

CREATE TABLE documents (
    id            uuid            PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id     uuid            NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    uploaded_by   uuid                NULL REFERENCES users(id)   ON DELETE SET NULL,
    filename      text            NOT NULL,
    content_hash  char(64)        NOT NULL,          -- sha256 del archivo
    kind          text            NOT NULL DEFAULT 'syllabus',
    page_count    integer             NULL,
    status        document_status NOT NULL DEFAULT 'pending',
    error_reason  text                NULL,
    created_at    timestamptz     NOT NULL DEFAULT now(),
    updated_at    timestamptz     NOT NULL DEFAULT now(),
    CONSTRAINT documents_hash_per_course UNIQUE (course_id, content_hash)
);

CREATE INDEX documents_course_status_idx ON documents (course_id, status);
```

`content_hash` evita que 200 estudiantes suban el mismo syllabus 200 veces (Q-01 del brief).

## 6. chunks

```sql
CREATE TABLE chunks (
    id          uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id uuid        NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    course_id   uuid        NOT NULL REFERENCES courses(id)   ON DELETE CASCADE,
    ordinal     integer     NOT NULL,
    content     text        NOT NULL,
    token_count integer     NOT NULL,
    page_from   integer         NULL,
    page_to     integer         NULL,
    embedding   vector(1536)    NULL,
    created_at  timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT chunks_ordinal_uniq UNIQUE (document_id, ordinal),
    CONSTRAINT chunks_tokens_pos   CHECK (token_count > 0)
);

-- Filtro por curso antes de la búsqueda vectorial: sin esto el retrieval cruza cursos.
CREATE INDEX chunks_course_idx ON chunks (course_id);

-- Índice vectorial para distancia coseno (pgvector).
CREATE INDEX chunks_embedding_hnsw
    ON chunks USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

-- Mitad léxica del retrieval híbrido.
CREATE INDEX chunks_content_fts
    ON chunks USING gin (to_tsvector('spanish', content));
```

`course_id` está desnormalizado a propósito: permite filtrar por permisos sin `JOIN`
en la consulta vectorial, que es el camino caliente (RNF-04).

## 7. reminders

Modelada en v0, no implementada (RF-26, RF-27).

```sql
CREATE TYPE reminder_channel AS ENUM ('email', 'inapp');

CREATE TABLE reminders (
    id              uuid             PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         uuid             NOT NULL REFERENCES users(id)        ON DELETE CASCADE,
    deliverable_id  uuid             NOT NULL REFERENCES deliverables(id) ON DELETE CASCADE,
    channel         reminder_channel NOT NULL DEFAULT 'inapp',
    offset_minutes  integer          NOT NULL DEFAULT 1440,   -- 24 h antes
    scheduled_at    timestamptz      NOT NULL,                -- due_at - offset, en UTC
    sent_at         timestamptz          NULL,
    created_at      timestamptz      NOT NULL DEFAULT now(),
    CONSTRAINT reminders_uniq          UNIQUE (user_id, deliverable_id, offset_minutes),
    CONSTRAINT reminders_offset_pos    CHECK (offset_minutes > 0)
);

-- El worker futuro barre por scheduled_at con sent_at nulo.
CREATE INDEX reminders_pending_idx
    ON reminders (scheduled_at)
    WHERE sent_at IS NULL;
```

## 8. Índices que importan y por qué

| Índice | Consulta que acelera | Requisito |
|---|---|---|
| `deliverables_course_due_idx` | agenda unificada ordenada por vencimiento | RNF-01 |
| `enrollments_user_idx` | resolver los cursos del usuario en cada request | RNF-08 |
| `chunks_embedding_hnsw` | top-k por similitud coseno | RNF-04 |
| `chunks_course_idx` | acotar el retrieval al curso del usuario | RNF-09 |
| `chunks_content_fts` | mitad léxica del retrieval híbrido | RF-22 |
| `reminders_pending_idx` | barrido de recordatorios pendientes | RF-26 |
| `documents_hash_per_course` | evitar reingesta del mismo PDF | Q-01 |
