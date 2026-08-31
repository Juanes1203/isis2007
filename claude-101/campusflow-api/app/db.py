"""Configuración de la base de datos: engine, sesión y Base declarativa.

Por defecto usa SQLite para que el curso arranque en minutos sin instalar
nada más. Cuando lleguemos al bloque de RAG, cambia DATABASE_URL en .env
a una URL de PostgreSQL 16 + pgvector: el resto del código no cambia.
"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./campusflow.db")

# check_same_thread solo aplica a SQLite; se ignora si DATABASE_URL apunta a Postgres.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Clase base declarativa para todos los modelos de CampusFlow."""


def get_db():
    """Dependencia de FastAPI: entrega una sesión y la cierra al terminar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
