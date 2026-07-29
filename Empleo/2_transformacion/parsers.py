# -*- coding: utf-8 -*-
"""
Homogeneización de nombres y formatos (parte de la fase A · limpieza).

Las series del INE llegan como texto libre y con la posición de cada dimensión
cambiante entre tablas. Aquí se extrae la CATEGORÍA de cada serie con vocabulario
controlado (una lista cerrada de etiquetas por tabla), lo que es robusto frente
al orden y a las variantes ortográficas de territorio/genero.

También se homogeneíza el periodo a un formato común (anyo, trimestre, periodo,
periodicidad) para poder unir después fuentes trimestrales y anuales.
"""
from __future__ import annotations

import re
import unicodedata


def _norm(s: str) -> str:
    if s is None:
        return ""
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def _match(nombre: str, vocab: list[str], por_defecto: str | None = None) -> str | None:
    """Devuelve la primera etiqueta de `vocab` cuya forma normalizada aparezca
    en `nombre`. El orden de `vocab` importa: colocar primero las etiquetas más
    específicas (p. ej. 'Industria, construcción y servicios' antes que 'Industria')."""
    n = _norm(nombre)
    for etiqueta in vocab:
        if _norm(etiqueta) in n:
            return etiqueta
    return por_defecto


# --------------------------------------------------------------------------- #
# Vocabularios controlados por tabla (slug de extracción)
# --------------------------------------------------------------------------- #
VOCAB_EDAD = ["Menores de 25 años", "De 25 a 54 años", "De 55 y más años", "Total"]

VOCAB_TIEMPO_BUSQUEDA = [
    "Ya ha encontrado empleo", "Menos de 1 mes", "De 1 mes a menos de 3 meses",
    "De 3 meses a menos de 6 meses", "De 6 meses a menos de 1 año",
    "De 1 año a menos de 2 años", "2 años o más", "Total",
]
# categorías que componen el Paro de Larga Duración (≥ 1 año)
PLD_CATEGORIAS = ["De 1 año a menos de 2 años", "2 años o más"]

# el orden evita que 'Total' capture 'De duración indefinida: Total' o 'Temporal: Total'
VOCAB_TIPO_CONTRATO = ["De duración indefinida", "Temporal", "Total"]

VOCAB_TIPO_JORNADA = ["Jornada a tiempo completo", "Jornada a tiempo parcial", "Total"]

VOCAB_ETCL_JORNADA = ["Ambas jornadas", "Jornada a tiempo completo", "Jornada a tiempo parcial"]
VOCAB_ETCL_SECTOR = ["Industria, construcción y servicios", "Industria", "Construcción", "Servicios"]
VOCAB_ETCL_MEDIDA = ["Horas pactadas", "Horas pagadas", "Horas efectivas",
                     "Horas no trabajadas", "Horas extras"]

VOCAB_EAES_ESTAD = ["Percentil 10", "Cuartil inferior", "Mediana", "Cuartil superior",
                    "Percentil 90", "Media"]


def categoria_por_slug(slug: str, nombre: str) -> dict:
    """Devuelve un dict de dimensiones categóricas homogeneizadas para una serie."""
    if slug in ("epa_tasa_paro", "epa_tasa_actividad", "epa_tasa_empleo"):
        return {"grupo_edad": _match(nombre, VOCAB_EDAD, "Total")}
    if slug == "epa_tiempo_busqueda":
        return {"tiempo_busqueda": _match(nombre, VOCAB_TIEMPO_BUSQUEDA)}
    if slug == "epa_tipo_contrato":
        return {"tipo_contrato": _match(nombre, VOCAB_TIPO_CONTRATO)}
    if slug == "epa_tipo_jornada":
        return {"tipo_jornada": _match(nombre, VOCAB_TIPO_JORNADA)}
    if slug == "etcl_tiempo_trabajo":
        return {
            "jornada": _match(nombre, VOCAB_ETCL_JORNADA),
            "sector": _match(nombre, VOCAB_ETCL_SECTOR),
            "medida": _match(nombre, VOCAB_ETCL_MEDIDA),
        }
    if slug == "eaes_ganancia_ccaa":
        return {"estadistico": _match(nombre, VOCAB_EAES_ESTAD)}
    return {}


# --------------------------------------------------------------------------- #
# Periodo homogéneo
# --------------------------------------------------------------------------- #
def homogeneiza_periodo(anyo, periodo, periodicidad) -> dict:
    """Unifica el periodo a (anyo, trimestre, periodo_norm, t_index).

    - Trimestral: 'YYYYTn' → trimestre n, t_index = anyo + (n-1)/4
    - Anual:      'YYYY'    → trimestre None, t_index = anyo
    """
    anyo = int(anyo) if anyo is not None else None
    trimestre = None
    periodo_norm = str(periodo) if periodo is not None else (str(anyo) if anyo else None)
    if periodo_norm:
        m = re.search(r"T([1-4])", periodo_norm)
        if m:
            trimestre = int(m.group(1))
    t_index = None
    if anyo is not None:
        t_index = anyo + (trimestre - 1) / 4 if trimestre else float(anyo)
    return {"anyo": anyo, "trimestre": trimestre, "periodo": periodo_norm,
            "periodicidad": periodicidad, "t_index": t_index}
