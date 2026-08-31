"""Puebla la base de datos con datos de ejemplo para la demo del curso.

Uso: python seed.py
"""
from datetime import datetime, timedelta, timezone

from app.db import Base, SessionLocal, engine
from app.models import Course, Deliverable

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Limpia datos previos para que el script sea idempotente.
db.query(Deliverable).delete()
db.query(Course).delete()
db.commit()

curso = Course(name="Ingeniería de Software", code="ISIS3710")
db.add(curso)
db.commit()
db.refresh(curso)

ahora_utc = datetime.now(timezone.utc)

entregas = [
    Deliverable(
        course_id=curso.id,
        title="Quiz 1 - Fundamentos",
        due_at=ahora_utc - timedelta(days=3),  # ya vencida
        estimated_hours=1.0,
    ),
    Deliverable(
        course_id=curso.id,
        title="Entrega 2 - API REST",
        # vence HOY a las 23:59: la que dispara el bug conocido (Parte VII)
        due_at=ahora_utc.replace(hour=23, minute=59, second=0, microsecond=0),
        estimated_hours=6.0,
    ),
    Deliverable(
        course_id=curso.id,
        title="Proyecto final - Propuesta",
        due_at=ahora_utc + timedelta(days=10),
        estimated_hours=8.0,
    ),
]
db.add_all(entregas)
db.commit()

# Leemos el codigo antes de cerrar la sesion: despues del close()
# los objetos quedan desasociados y SQLAlchemy no puede recargar atributos.
codigo = curso.code
db.close()

print(f"Listo: curso '{codigo}' con {len(entregas)} entregas.")
