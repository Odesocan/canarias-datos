"""ccaa/ext/transform.py — Asignación de concepto local."""
from .._common.transform_helpers import asignar_concepto_local


def transform(rows, anio):
    """Asigna 'concepto' usando ext/correspondencias.yml."""
    return asignar_concepto_local(rows, mapping_path=__file__)
