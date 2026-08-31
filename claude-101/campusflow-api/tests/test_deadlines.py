"""Tests de app/services/deadlines.py.

INCOMPLETO A PROPÓSITO (ver Parte VII del curso): solo cubre el camino
feliz. Antes de confiar en este módulo hacen falta al menos:
  - entrega que vence HOY a las 23:59 (el bug conocido)
  - entrega ya vencida (varios días atrás)
  - entrega en una zona horaria distinta a la del servidor
  - agenda vacía (lista de entregas = [])
  - orden estable cuando dos entregas empatan en días restantes
"""
from datetime import datetime, timedelta

from app.services.deadlines import calcular_dias_restantes, estado_entrega


def test_entrega_lejana_en_el_futuro():
    """Camino feliz: una entrega en unos diez días se ve como 'proxima'."""
    fecha_entrega = datetime.now() + timedelta(days=10, hours=1)

    dias = calcular_dias_restantes(fecha_entrega)
    estado = estado_entrega(fecha_entrega)

    assert dias == 10
    assert estado == "proxima"
