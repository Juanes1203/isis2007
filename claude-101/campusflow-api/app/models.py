"""Modelos SQLAlchemy 2.x para CampusFlow."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Course(Base):
    """Una materia del semestre."""

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    code: Mapped[str] = mapped_column(String(20), unique=True)

    deliverables: Mapped[list["Deliverable"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )


class Deliverable(Base):
    """Una entrega (tarea, parcial, proyecto) con fecha límite."""

    __tablename__ = "deliverables"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    title: Mapped[str] = mapped_column(String(200))
    # Se guarda "en UTC" por convención del equipo, pero la columna no
    # fuerza tzinfo: SQLite (y otros backends) pueden devolver un datetime
    # naive al leer. Ver app/services/deadlines.py para el bug real.
    due_at: Mapped[datetime]
    estimated_hours: Mapped[float] = mapped_column(default=2.0)

    course: Mapped["Course"] = relationship(back_populates="deliverables")
