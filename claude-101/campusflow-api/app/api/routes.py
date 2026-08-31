"""Endpoints HTTP de CampusFlow."""
from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Course, Deliverable
from app.schemas import CourseOut, DeliverableOut, WorkloadOut

router = APIRouter()


@router.get("/courses", response_model=list[CourseOut])
def listar_cursos(db: Session = Depends(get_db)) -> list[Course]:
    """Lista todas las materias registradas."""
    return db.query(Course).all()


@router.get("/courses/{course_id}", response_model=CourseOut)
def obtener_curso(course_id: int, db: Session = Depends(get_db)) -> Course:
    """Detalle de una materia."""
    curso = db.get(Course, course_id)
    if curso is None:
        raise HTTPException(status_code=404, detail="curso no encontrado")
    return curso


@router.get("/courses/{course_id}/agenda", response_model=list[DeliverableOut])
def obtener_agenda(course_id: int, db: Session = Depends(get_db)) -> list[DeliverableOut]:
    """Agenda de entregas de una materia, de la más urgente a la menos urgente."""
    entregas = db.query(Deliverable).filter(Deliverable.course_id == course_id).all()

    # BUG DUPLICADO A PROPÓSITO: esta cuenta de días restantes está copiada
    # de app/services/deadlines.py en lugar de importarla de ahí. Si alguien
    # arregla calcular_dias_restantes() en services/deadlines.py, esta copia
    # sigue rota. Ver Parte VII del material del curso antes de tocar esto.
    def _dias_restantes(fecha_entrega: datetime) -> int:
        ahora = datetime.now()
        delta = fecha_entrega - ahora
        return delta.days

    resultado = []
    for entrega in entregas:
        dias = _dias_restantes(entrega.due_at)
        estado = "vencida" if dias <= 0 else "proxima"
        resultado.append(
            DeliverableOut(
                id=entrega.id,
                title=entrega.title,
                due_at=entrega.due_at,
                estimated_hours=entrega.estimated_hours,
                days_left=dias,
                status=estado,
            )
        )

    # BUG: hereda el mismo problema de granularidad de días que ordenar_agenda()
    # en services/deadlines.py -- dos entregas del mismo día empatan en 0.
    resultado.sort(key=lambda d: d.days_left)
    return resultado


@router.get("/courses/{course_id}/workload", response_model=WorkloadOut)
def obtener_workload(course_id: int, db: Session = Depends(get_db)) -> WorkloadOut:
    """Carga académica de la semana para una materia.

    TODO(feature pendiente -- ver Parte VII del material del curso):
    implementar según la especificación. Debe devolver el número de
    entregas y las horas estimadas para la semana en curso.
    """
    raise HTTPException(status_code=501, detail="workload no implementado todavía")
