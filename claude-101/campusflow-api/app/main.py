"""Punto de entrada de la aplicación FastAPI."""
from fastapi import FastAPI

from app.api.routes import router
from app.db import Base, engine

# Crea las tablas si no existen (suficiente para el curso; en producción se usaría Alembic).
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CampusFlow API", version="0.1.0")
app.include_router(router)


@app.get("/health")
def health() -> dict[str, str]:
    """Chequeo simple de que el servicio está vivo."""
    return {"status": "ok"}
