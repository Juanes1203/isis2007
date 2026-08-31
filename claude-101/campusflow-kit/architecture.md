# CampusFlow — Arquitectura v0

Repo: `campusflow-api` · Stack cerrado: Python 3.12, FastAPI, PostgreSQL 16 + pgvector,
SQLAlchemy 2.x, Pydantic v2, Alembic, pytest. API-first, sin frontend. Auth JWT.

Este documento describe cómo está construido v0 y **por qué**. Las decisiones están en
formato ADR corto. Un ADR no se edita: si cambia la decisión, se escribe uno nuevo que lo supera.

## 1. Visión general

Un solo servicio FastAPI, una sola base de datos Postgres. Sin colas, sin microservicios,
sin vector store aparte. La ingesta de documentos corre en un `BackgroundTask` del mismo
proceso: es suficiente para v0 y es honesto sobre sus límites (ver sección 6).

Tres capas, sin excepciones:

- `api/` — routers, validación de entrada/salida con Pydantic v2, códigos HTTP. Sin lógica.
- `services/` — reglas de negocio. Sin FastAPI, sin `Request`, sin `HTTPException`.
- `db/` — modelos SQLAlchemy y repositorios. Sin lógica de negocio.

Regla: `api` importa `services`, `services` importa `db`. Nunca al revés. Nunca saltando capa.

## 2. Componentes

```
                  +---------------------+
  Cliente HTTP    |   FastAPI (app/)    |
  (curl, Postman) |                     |
        |         |  api/routes_*.py    |
        +-------->|  deps.py (JWT)      |
                  +----------+----------+
                             |
             +---------------+----------------+
             |               |                |
             v               v                v
      +-------------+ +-------------+ +----------------+
      | services/   | | services/   | | services/      |
      | deadlines   | | ingestion   | | rag            |
      | (agenda,    | | (PDF, chunk,| | (retrieval,    |
      |  days_left) | |  embeddings)| |  prompt, cita) |
      +------+------+ +------+------+ +--------+-------+
             |               |                 |
             +-------+-------+--------+--------+
                     |                |
                     v                v
             +---------------+ +--------------------+
             |  db/ (SQLA 2) | | clientes externos  |
             |  repositorios | | - embeddings API   |
             +-------+-------+ | - Anthropic API    |
                     |         +--------------------+
                     v
        +------------------------------+
        | PostgreSQL 16 + pgvector     |
        | 7 tablas + índice HNSW       |
        +------------------------------+
```

## 3. Decisiones de arquitectura (ADRs)

### ADR-01 — FastAPI como framework HTTP
**Estado:** aceptado (2026-07-30).
**Contexto:** necesitamos una API con validación fuerte, tipos, documentación automática
y buen soporte de async para llamar APIs externas (embeddings, modelo).
**Decisión:** FastAPI sobre Django REST o Flask.
**Razones:** integración nativa con Pydantic v2, que ya usamos como contrato de I/O; OpenAPI
generado sin trabajo extra, lo que hace el repo legible para un agente; async de primera clase
para las llamadas a proveedores externos; superficie pequeña, apropiada para un curso.
**Consecuencias:** no hay admin ni ORM incluido, así que traemos SQLAlchemy 2.x y Alembic a mano.
La disciplina de capas queda en nosotros, no en el framework.

### ADR-02 — pgvector dentro de Postgres, no un vector store aparte
**Estado:** aceptado (2026-08-02).
**Contexto:** necesitamos búsqueda por similitud sobre los chunks de los documentos del curso.
Alternativas evaluadas: Qdrant, Pinecone, Chroma.
**Decisión:** extensión `pgvector` en la misma base de datos Postgres.
**Razones:** el corpus de v0 es pequeño (decenas de miles de chunks, no millones); mantener
una sola base evita un segundo sistema que operar, respaldar y sincronizar; el filtro por
permisos (`course_id` del usuario inscrito) es un `JOIN` normal, no una réplica de metadatos
en dos sistemas; transacciones: documento, chunks y embeddings se escriben o se caen juntos.
**Consecuencias:** si el corpus crece a millones de vectores o necesitamos filtros complejos
a gran escala, pgvector deja de ser suficiente y se escribe un ADR que supere este.
Aceptamos ese techo a cambio de simplicidad operativa hoy.

### ADR-03 — API-first, sin frontend en v0
**Estado:** aceptado (2026-08-02).
**Contexto:** el alcance del curso son 3 horas y el objetivo es enseñar ingeniería de producto
con agentes, no CSS.
**Decisión:** entregamos una API HTTP documentada con OpenAPI. El cliente es `curl`, Postman
o los tests. Sin React, sin plantillas, sin app móvil.
**Razones:** los criterios de aceptación se verifican con requests, no con clics; el contrato
queda explícito y testeable; un frontend duplicaría el esfuerzo sin aportar aprendizaje nuevo.
**Consecuencias:** no hay demo "bonita". Toda la evidencia de que el producto funciona vive en
los tests y en el OpenAPI. Cualquier UI futura consume esta API sin cambiarla.

### ADR-04 — Todo instante se guarda en UTC
**Estado:** aceptado (2026-08-05).
**Contexto:** un bug real en `days_left` mostraba como vencida una entrega que vence hoy a las
23:59 hora de Bogotá. Causa: mezcla de `datetime` naive con instantes aware en UTC y uso de
`.days` sobre un `timedelta` negativo, que trunca hacia abajo.
**Decisión:** todas las columnas de tiempo son `timestamptz` y se persisten en UTC.
En Python solo circulan `datetime` **aware**; se prohíbe `datetime.utcnow()` y se usa
`datetime.now(timezone.utc)`. La conversión a `America/Bogota` ocurre únicamente al serializar.
La zona horaria del curso vive en `courses.timezone` y es dato, no supuesto.
**Razones:** una sola representación interna elimina la clase completa de bugs de comparación.
**Consecuencias:** hay que normalizar en la frontera (parsers de PDF, entrada de la API) y
el cálculo de "días restantes" debe hacerse sobre días calendario en la zona del curso,
no dividiendo un `timedelta`. La función vive en **un solo lugar**: `services/deadlines.py`.
Hoy está duplicada en `api/routes.py`; eliminar esa copia es deuda declarada.

## 4. Flujo de ingesta de documentos

1. `POST /courses/{course_id}/documents` recibe el PDF. Se valida tipo, tamaño (máx. 20 MB)
   y que el usuario esté inscrito. Se guarda la fila en `documents` con `status='pending'` y
   se responde 202 con el `document_id`.
2. Un `BackgroundTask` extrae el texto por página con `pypdf`. Si no hay capa de texto,
   `status='failed'` con motivo `no_text_layer`.
3. Chunking por ventana de ~800 tokens con solape de 100, respetando límites de párrafo.
   Cada chunk guarda `page_from` y `page_to` para poder citar.
4. Los chunks se envían en lotes de 64 al proveedor de embeddings (1536 dimensiones).
   Se escriben en `chunks` con su vector.
5. Un paso de extracción estructurada pide al modelo las entregas con fecha del documento
   y devuelve propuestas con `title`, `due_at`, `estimated_hours` y el chunk de origen.
   **Las propuestas no se guardan en `deliverables`**: esperan confirmación del usuario.
6. `status='ready'`. El usuario revisa en `GET /documents/{id}/proposals` y confirma.

## 5. Flujo de consulta con RAG

1. `POST /courses/{course_id}/ask` valida inscripción del usuario. Sin inscripción, 403.
2. La pregunta se convierte a embedding con el mismo modelo de la ingesta. Mezclar modelos
   de embedding entre ingesta y consulta es un error silencioso: los vectores no son comparables.
3. Retrieval híbrido: top-20 por distancia coseno en pgvector, filtrado por `course_id`,
   más top-20 por búsqueda léxica `tsvector`. Se fusionan y se recorta a top-8.
4. Los 8 chunks se arman como contexto con su documento y su página.
5. Se llama al modelo con instrucción explícita: responder solo con el contexto dado y citar.
   Si la similitud máxima está por debajo del umbral, no se llama al modelo: se responde
   "no está en los documentos del curso".
6. La respuesta se valida: cada `chunk_id` citado debe existir en el contexto enviado.
   Una cita que no existe invalida la respuesta completa.

## 6. Límites conocidos

- La ingesta corre en el mismo proceso web. Dos PDFs grandes simultáneos degradan la latencia
  de toda la API. Aceptado en v0; la solución es una cola, y no está en alcance.
- Sin reranker. El retrieval es denso + léxico y se corta en top-8. Un reranker mejoraría la
  precisión pero agrega un proveedor más.
- No hay caché de embeddings de preguntas repetidas. Camilo va a pagar dos veces la misma pregunta.
- Sin OCR: los syllabus escaneados fallan por diseño.
- El índice HNSW se construye una vez; con inserciones masivas hay que reindexar a mano.
- No hay multi-tenant: una instancia, una universidad, una zona horaria por curso.
- `days_left` está duplicada en `services/deadlines.py` y `api/routes.py`. Es deuda conocida,
  está en el backlog y es la causa directa del bug de ADR-04.
