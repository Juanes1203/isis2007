# campusflow-api

API de CampusFlow: una sola agenda de entregas construida a partir de los documentos reales
del curso, con preguntas en lenguaje natural respondidas con cita al documento.

Servicio HTTP en FastAPI sobre PostgreSQL 16 + pgvector. **API-first: no hay frontend.**
El alcance de v0 está en `product-brief.md`; el contrato, en `requirements.md`.

## Requisitos

- Python 3.12
- Docker y Docker Compose
- `uv` (o `pip` con un virtualenv)
- Una API key de un proveedor de embeddings y una de Anthropic

## Levantar el entorno

1. Base de datos con pgvector:

```bash
docker run -d --name campusflow-db \
  -e POSTGRES_USER=campusflow \
  -e POSTGRES_PASSWORD=changeme \
  -e POSTGRES_DB=campusflow \
  -p 5432:5432 \
  -v campusflow_pgdata:/var/lib/postgresql/data \
  pgvector/pgvector:pg16
```

O, equivalente, con el compose del repo:

```bash
docker compose up -d db
```

2. Verificar que la extensión está disponible:

```bash
docker exec -it campusflow-db psql -U campusflow -d campusflow \
  -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

3. Dependencias y variables de entorno:

```bash
uv sync
cp .env.example .env
```

Variables que hay que llenar en `.env` (nombres, no valores; ningún valor real va al repo):

| Variable | Para qué |
|---|---|
| `DATABASE_URL` | cadena de conexión a Postgres |
| `JWT_SECRET` | firma de los tokens HS256 |
| `JWT_EXPIRE_MINUTES` | vigencia del token, por defecto 1440 |
| `EMBEDDINGS_PROVIDER` | proveedor de embeddings |
| `EMBEDDINGS_MODEL` | modelo de embeddings, 1536 dimensiones |
| `EMBEDDINGS_API_KEY` | credencial del proveedor de embeddings |
| `ANTHROPIC_API_KEY` | credencial para la generación de respuestas |
| `ANTHROPIC_MODEL` | modelo usado en `/ask` |
| `MAX_UPLOAD_MB` | tamaño máximo de PDF, por defecto 20 |
| `LOG_LEVEL` | nivel de logging |

4. Migraciones:

```bash
uv run alembic upgrade head
```

Para crear una migración nueva tras cambiar `app/db/models.py`:

```bash
uv run alembic revision --autogenerate -m "add workload fields"
uv run alembic upgrade head
```

Revisa siempre la migración generada antes de aplicarla. Alembic no adivina renombres.

5. Correr la API:

```bash
uv run uvicorn app.main:app --reload --port 8000
```

OpenAPI en `http://localhost:8000/docs`. Health en `http://localhost:8000/health`.

## Tests

```bash
uv run pytest                      # todo
uv run pytest tests/unit -q        # solo unitarios, sin Docker
uv run pytest -k days_left -vv     # un caso
uv run pytest --cov=app --cov-report=term-missing
```

Los tests de integración levantan un Postgres con `testcontainers`: necesitan Docker corriendo.
Cobertura mínima: 80% global, 90% en `app/services/`.

## Estructura del repo

```
app/            código de la aplicación (api / services / db)
migrations/     revisiones de Alembic
tests/          unit e integration
docs/           ADRs y notas de diseño
pyproject.toml  dependencias, ruff, black, mypy, pytest
compose.yaml    Postgres + pgvector para desarrollo
```

## Cómo contribuir

1. Rama desde `main`: `feat/...`, `fix/...`, `chore/...`, `docs/...`.
2. Lee `coding-standards.md` antes del primer commit. Aplica también al código generado por IA.
3. Antes de abrir el PR: `uv run ruff check . && uv run black --check . && uv run pytest`.
4. PR de máximo 400 líneas de diff. Describe qué cambia, por qué, cómo se probó y qué no cubre.
5. Un bug se corrige con el test que lo reproduce en el mismo PR.
6. Los cambios de arquitectura entran como un ADR nuevo en `docs/`, no editando uno existente.

## Estado conocido

- `days_left` está duplicada en `app/services/deadlines.py` y `app/api/routes.py`, y mezcla
  `datetime` naive con instantes en UTC: una entrega que vence hoy a las 23:59 aparece vencida
  y desordena la agenda. Es el bug abierto número uno.
- `GET /courses/{course_id}/workload` está especificado (RF-20, US-05) y no implementado.
- Los tests de `days_left` solo cubren el happy path.
