"""ccaa/lar/transform.py — Asignación de concepto local.

La Rioja cambió la clasificación funcional en 2017: los BOLR 2015-2016 usan el
esquema ANTIGUO (grupo 4.1=Sanidad, 4.2=Educación, 3.1=Protección social,
5.3.1/7.1=Agrario, 4.5=Cultura, 4.3=Vivienda, 1.*=Dirección), incompatible con
el nuevo (2017+, donde 3.1=Sanidad). Con un único mapping, los códigos nuevos
mis-asignaban ~403 M€ de sanidad de 2016 a soberania (el prefijo de código gana
al keyword). Por eso ≤2016 usa `correspondencias_legacy.yml`. FIX 2026-07-02.
"""
import os

from .._common.transform_helpers import asignar_concepto_local

_LEGACY = os.path.join(os.path.dirname(__file__), "correspondencias_legacy.yml")


def transform(rows, anio):
    """Asigna 'concepto'; ≤2016 = esquema funcional antiguo (mapping legacy)."""
    if anio <= 2016:
        return asignar_concepto_local(rows, mapping_path=_LEGACY)
    return asignar_concepto_local(rows, mapping_path=__file__)
