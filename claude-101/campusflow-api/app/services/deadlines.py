"""Lógica de negocio sobre fechas límite de entregas.

BUG INTENCIONAL (ver Parte VII del curso): calcular_dias_restantes mezcla
datetime.now() naive con fechas guardadas "en UTC" y usa .days sobre un
timedelta que puede ser negativo. No lo arregles sin leer esa sección.
"""
from __future__ import annotations

from datetime import datetime

from app.models import Deliverable


def calcular_dias_restantes(fecha_entrega: datetime) -> int:
    """Días que faltan para una entrega. Negativo si ya venció."""
    ahora = datetime.now()  # naive, hora local del servidor
    delta = fecha_entrega - ahora  # fecha_entrega se asume UTC pero llega naive
    return delta.days


def estado_entrega(fecha_entrega: datetime) -> str:
    """Clasifica una entrega según cuánto falta."""
    dias = calcular_dias_restantes(fecha_entrega)
    if dias <= 0:
        return "vencida"
    return "proxima"


def ordenar_agenda(entregas: list[Deliverable]) -> list[Deliverable]:
    """Ordena entregas de la más urgente a la menos urgente."""
    return sorted(entregas, key=lambda e: calcular_dias_restantes(e.due_at))
