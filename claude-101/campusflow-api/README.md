# campusflow-api

API del curso "Claude 101" para el caso CampusFlow: agenda unificada de
entregas académicas.

## Stack

Python 3.12, FastAPI, SQLAlchemy 2.x, Pydantic v2, pytest. SQLite por
defecto (cero configuración); PostgreSQL 16 + pgvector cuando el curso
llegue al bloque de RAG.

## Instalar

    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env

## Poblar datos de ejemplo

    python seed.py

## Correr

    uvicorn app.main:app --reload

Documentación interactiva en http://localhost:8000/docs

## Tests

    pytest -q

## Endpoints

- GET /health
- GET /courses
- GET /courses/{course_id}
- GET /courses/{course_id}/agenda
- GET /courses/{course_id}/workload (pendiente, ver CLAUDE.md)

## Estado conocido

Hay un bug intencional en el cálculo de días restantes y una feature sin
terminar. Ambos están documentados en CLAUDE.md y en el material del
curso (Parte VII).
