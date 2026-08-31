# CLAUDE.md — campusflow-api

Este es el repo de práctica del curso "Claude 101: De Prompting a
Product Engineering". Implementa un fragmento del backend de
CampusFlow, un asistente académico para estudiantes de pregrado.

## Stack (no cambiar sin discutirlo)

Python 3.12, FastAPI, SQLAlchemy 2.x, Pydantic v2, pytest. Persistencia:
SQLite en desarrollo (DATABASE_URL en .env), PostgreSQL 16 + pgvector
cuando se trabaje en RAG. Sin frontend: API-first.

## Comandos

- pytest -q — corre los tests. Deben pasar en verde antes de cualquier commit.
- uvicorn app.main:app --reload — levanta el servidor en localhost:8000.
- python seed.py — puebla datos de ejemplo (idempotente, se puede correr varias veces).

## Estándares

- Comentarios y nombres de dominio en español; nombres de código (variables,
  funciones internas) en inglés cuando el equipo ya los usa así.
- Type hints en toda función nueva. Pydantic v2 (model_config, no class Config).
- Un test por cada caso borde que agregues, no solo el camino feliz.

## Qué NO tocar sin preguntar

- El esquema de app/models.py (hay seeds y tests que dependen de los nombres
  de columna).
- La URL de conexión por defecto en app/db.py: debe seguir siendo SQLite
  para que el curso arranque sin instalar Postgres.

## Conocido y pendiente

- app/services/deadlines.py tiene un bug de manejo de fechas (naive vs.
  UTC) duplicado en app/api/routes.py. No lo arregles sin leerte la
  Parte VII del material del curso.
- GET /courses/{course_id}/workload está sin implementar (ver TODO en
  app/api/routes.py).

## Política de código generado por IA

Todo lo que Claude escriba en este repo se revisa como si lo hubiera
escrito una persona junior: se lee el diff completo, se corren los tests,
y no se hace merge de nada que el autor humano no pueda explicar en voz alta.
