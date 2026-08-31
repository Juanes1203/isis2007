# CampusFlow — Estándares de código

Aplican a todo el repo `campusflow-api`, escriba el código una persona o un agente.
No hay dos varas: el PR se juzga por lo que dice este archivo.

## 1. Estilo

- Python 3.12. Formateo con `black` (line length 100). Lint con `ruff` (reglas
  `E,F,I,N,UP,B,SIM,ASYNC`). CI falla si `ruff check` o `black --check` fallan.
- **Type hints obligatorios** en toda función y método, incluido el retorno.
  `mypy --strict` sobre `app/services/` y `app/db/`. Sin `Any` salvo en frontera con librerías
  sin tipos, y ahí con `# type: ignore[...]` específico y comentado.
- **Pydantic v2 para todo I/O.** Entrada de la API, salida de la API y payloads de
  proveedores externos. Nada de `dict` crudo cruzando una frontera.
- Sin comentarios que repitan el código. Los comentarios explican **por qué**, no qué.
- Docstrings solo en funciones públicas de `services/`, en una línea.
- Nada de `print`. Logging estructurado con `structlog`.
- Prohibido `datetime.utcnow()`. Se usa `datetime.now(timezone.utc)`. Ver ADR-04.

## 2. Estructura de carpetas

```
app/
  main.py              # crea la app, monta routers, health
  config.py            # Settings de Pydantic, lee env. Único lugar que toca os.environ
  api/
    deps.py            # dependencias: sesión de DB, usuario actual, verificación de curso
    routes_auth.py
    routes_courses.py
    routes_documents.py
    routes_agenda.py
    schemas/           # modelos Pydantic de request y response
  services/
    deadlines.py       # days_left, agenda, workload
    ingestion.py       # PDF, chunking, embeddings, propuestas
    rag.py             # retrieval híbrido, prompt, validación de citas
  db/
    models.py          # modelos SQLAlchemy 2.x
    repositories/      # acceso a datos, uno por agregado
    session.py
migrations/            # Alembic
tests/
  unit/                # services puros, sin base de datos
  integration/         # con Postgres real vía testcontainers
  conftest.py
```

`api` importa `services`; `services` importa `db`. Nunca al revés.
Un `import` de FastAPI dentro de `services/` es rechazo automático del PR.

## 3. Convenciones de nombres

- Módulos y funciones `snake_case`. Clases `PascalCase`. Constantes `UPPER_SNAKE`.
- Schemas Pydantic: `DeliverableCreate`, `DeliverableRead`, `DeliverableUpdate`.
- Modelos SQLAlchemy en singular: `class Deliverable`. Tablas en plural: `deliverables`.
- Funciones que hacen I/O son `async` y su nombre dice qué traen: `fetch_agenda_for_user`.
- Booleanos con prefijo: `is_active`, `has_text_layer`, `should_retry`.
- Tests: `test_<unidad>_<condición>_<resultado_esperado>`.
  Ejemplo: `test_days_left_due_today_2359_returns_zero`.

## 4. Errores y códigos HTTP

- Los `services/` lanzan excepciones de dominio (`CourseNotFound`, `NotEnrolled`,
  `DocumentHasNoText`). No conocen HTTP.
- `api/` traduce dominio a HTTP en un `exception_handler` central. Un `raise HTTPException`
  dentro de un servicio es rechazo de PR.
- Tabla de traducción:

| Situación | Código |
|---|---|
| Payload inválido (Pydantic) | 422 |
| Sin JWT o JWT vencido | 401 |
| Autenticado pero sin inscripción en el curso | 403 |
| Recurso inexistente **al que sí tendrías acceso** | 404 |
| Conflicto de unicidad (correo, documento repetido) | 409 |
| PDF sin capa de texto | 422 |
| Error del proveedor de embeddings o del modelo | 503 |

- Un recurso ajeno responde 403, no 404. No enumeramos cursos ajenos por diferencia de códigos.
- El cuerpo de error siempre `{"error": {"code": "...", "message": "..."}}`.
  El `message` es para humanos y no filtra nombres de tabla, SQL ni stack traces.

## 5. Tests

- `pytest` + `pytest-asyncio`. Integración con Postgres real (`testcontainers`), no SQLite:
  pgvector y `timestamptz` no se simulan.
- **Siempre se testea:** toda función de `services/`, todo endpoint en su camino feliz y en
  su camino de autorización (403), y **todo borde de fecha**: mismo día, 23:59, ya vencida,
  cambio de zona horaria, lista vacía.
- Un bug corregido entra con el test que lo reproduce. Sin test, no es un fix: es una opinión.
- Cobertura mínima 80% global y **90% en `app/services/`**. CI falla por debajo.
- Prohibido testear implementación: nada de assert sobre llamadas internas privadas.
- El tiempo se congela con `freezegun` o se inyecta un `clock`. Nunca `datetime.now()` real
  dentro de un test de fechas.

## 6. Git

- Ramas: `feat/agenda-workload`, `fix/days-left-utc`, `chore/bump-ruff`, `docs/adr-05`.
  Nunca commits directos a `main`.
- Commits convencionales: `tipo(scope): descripción en imperativo`.
  Ejemplos: `fix(deadlines): calcular days_left en UTC`, `feat(api): agregar GET workload`,
  `test(deadlines): cubrir bordes de vencimiento`.
- Un commit, un cambio lógico. Formateo y lógica no viajan juntos.
- **PR de máximo 400 líneas de diff** sin contar migraciones autogeneradas ni lockfiles.
  Un PR más grande se parte. Un PR que nadie puede revisar en 20 minutos no se revisa: se aprueba.
- Todo PR describe: qué cambia, por qué, cómo se probó, y qué NO cubre.
- Squash merge. `main` siempre verde.

## 7. Reglas para código generado por IA

El código generado por un agente entra por el mismo PR, con el mismo estándar, y con
revisión humana. Que lo haya escrito Claude no es una atenuante: es un detalle de implementación.

**Lo que se revisa SIEMPRE, línea por línea:**

- Cualquier consulta a base de datos: parámetros, índices usados, N+1.
- Cualquier manejo de fechas, zonas horarias o duraciones.
- Cualquier verificación de autorización o de pertenencia a un curso.
- Cualquier borde: lista vacía, valor nulo, división, `timedelta` negativo.
- Los tests que vinieron con el código: ¿fallan si rompo la función a propósito?

**Lo que NUNCA se acepta, aunque funcione:**

- **SQL construido por concatenación o f-strings.** Siempre parámetros o SQLAlchemy.
  Una sola ocurrencia bloquea el merge.
- **Secretos en el código.** Ni de ejemplo, ni en un test, ni en un comentario.
  Todo por `config.Settings` desde variables de entorno.
- **Dependencias nuevas sin justificar.** Agregar algo a `pyproject.toml` exige una línea
  en el PR: qué problema resuelve y por qué no se resuelve con la librería estándar.
- **Tests que solo prueban el happy path.** Si el PR agrega lógica de fechas y no trae el
  caso de "vence hoy a las 23:59", el PR está incompleto.
- **Lógica duplicada.** Si la función ya existe en `services/`, el agente no escribe otra copia
  en `api/`. Ya nos pasó con `days_left` y costó un bug en producción de clase.
- **`try/except Exception: pass`** o cualquier excepción tragada en silencio.
- Código muerto, imports sin usar, funciones "por si acaso" que nadie llama.

**Antes de abrir el PR con código de un agente, el humano responde tres preguntas por escrito:**
¿entiendo cada línea?, ¿qué caso rompe esto?, ¿qué haría yo distinto y por qué acepté esto?
Si no puede responderlas, el código no está listo, aunque los tests pasen.
