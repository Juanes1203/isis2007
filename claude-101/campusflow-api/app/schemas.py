"""Esquemas Pydantic v2 para entrada/salida de la API."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DeliverableOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    due_at: datetime
    estimated_hours: float
    days_left: int
    status: str  # "vencida" | "proxima" -- ver el bug conocido en Parte VII


class CourseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    code: str


class WorkloadOut(BaseModel):
    """Respuesta de GET /courses/{course_id}/workload (feature pendiente)."""

    course_id: int
    week_start: datetime
    week_end: datetime
    deliverable_count: int
    estimated_hours: float
