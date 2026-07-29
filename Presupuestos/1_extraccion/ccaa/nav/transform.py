"""ccaa/nav/transform.py — Asignación de concepto local."""
from .._common.transform_helpers import asignar_concepto_local


def transform(rows, anio):
    """Asigna 'concepto' usando nav/correspondencias.yml."""
    return asignar_concepto_local(rows, mapping_path=__file__)
