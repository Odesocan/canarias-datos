"""
Diccionario de las 17 comunidades autónomas de España + Ceuta y Melilla.
Cada entrada incluye su slug de Idealista, código INE y población de referencia.

Funciones de búsqueda flexible para resolver variantes de nombre
que aparecen en diferentes fuentes (Idealista, INE, uso coloquial).
"""

import unicodedata
from typing import Dict, List, Optional


# ── Utilidades de normalización ────────────────────────────────────────────


def _generar_slug(nombre: str) -> str:
    """
    Genera un slug URL a partir del nombre de la comunidad.
    Elimina acentos, convierte a minúsculas, reemplaza espacios por guiones.
    """
    normalized = unicodedata.normalize("NFD", nombre)
    ascii_text = "".join(
        c for c in normalized if unicodedata.category(c) != "Mn"
    )
    return ascii_text.lower().replace(" ", "-")


def _c(
    nombre: str,
    slug: str,
    codigo_ine: str = "",
    poblacion: int = 0,
    aliases: list = None,
    nombre_busqueda: str = None,
) -> Dict:
    """Crea una entrada de comunidad autónoma de forma concisa.

    nombre_busqueda: nombre desambiguado para usar en búsquedas de Google
        (ej. "Comunidad de Madrid" en lugar de "Madrid" para no obtener
        resultados de la ciudad de Madrid). Por defecto usa `nombre`.
    """
    return {
        "nombre": nombre,
        "slug_idealista": slug,
        "codigo_ine": codigo_ine,
        "poblacion_2024": poblacion,
        "aliases": aliases or [],
        "nombre_busqueda": nombre_busqueda or nombre,
    }


# ── Lista de comunidades autónomas ─────────────────────────────────────────

COMUNIDADES_AUTONOMAS: List[Dict] = [
    _c("Andalucía",            "andalucia",           "01", 8_582_000,
       aliases=["Andalucia"]),
    _c("Aragón",               "aragon",              "02", 1_345_000,
       aliases=["Aragon"]),
    _c("Asturias",             "asturias",            "03", 1_011_000,
       aliases=["Principado de Asturias"]),
    _c("Baleares",             "baleares",            "04", 1_210_000,
       aliases=["Illes Balears", "Islas Baleares", "Baleares"]),
    _c("Canarias",             "canarias",            "05", 2_221_000,
       aliases=["Islas Canarias"]),
    _c("Cantabria",            "cantabria",           "06",   585_000),
    _c("Castilla-La Mancha",   "castilla-la-mancha",  "08", 2_082_000,
       aliases=["Castilla La Mancha"]),
    _c("Castilla y León",      "castilla-y-leon",     "07", 2_383_000,
       aliases=["Castilla y Leon", "CyL"]),
    _c("Cataluña",             "cataluna",            "09", 7_898_000,
       aliases=["Catalunya", "Catalonia", "Cataluna"]),
    _c("Comunidad Valenciana", "comunidad-valenciana","10", 5_057_000,
       aliases=["Valencia", "País Valenciano", "Pais Valenciano"]),
    _c("Extremadura",          "extremadura",         "11", 1_056_000),
    _c("Galicia",              "galicia",             "12", 2_695_000),
    _c("La Rioja",             "la-rioja",            "26",   322_000,
       aliases=["Rioja"]),
    _c("Madrid",               "madrid-comunidad",    "13", 6_771_000,
       aliases=["Comunidad de Madrid", "madrid"],
       nombre_busqueda="Comunidad de Madrid"),
    _c("Murcia",               "murcia-region",       "14", 1_529_000,
       aliases=["Región de Murcia", "Region de Murcia", "murcia"],
       nombre_busqueda="Región de Murcia"),
    _c("Navarra",              "navarra",             "15",   661_000,
       aliases=["Comunidad Foral de Navarra"]),
    _c("País Vasco",           "euskadi",             "16", 2_204_000,
       aliases=["Pais Vasco", "Euskadi", "Euskal Herria", "pais-vasco"],
       nombre_busqueda="Euskadi"),
    _c("Ceuta",                "ceuta",               "18",    84_000),
    _c("Melilla",              "melilla",             "19",    86_000),
]


# ── Índices de búsqueda ────────────────────────────────────────────────────


def _build_indices():
    por_slug = {}
    por_nombre_lower = {}
    por_alias = {}

    for c in COMUNIDADES_AUTONOMAS:
        slug = c["slug_idealista"]
        por_slug[slug] = c
        por_nombre_lower[c["nombre"].lower()] = c

        for alias in c.get("aliases", []):
            por_alias[alias.lower()] = c
            por_alias[_generar_slug(alias)] = c

        base_slug = _generar_slug(c["nombre"])
        if base_slug != slug:
            por_alias[base_slug] = c

    return por_slug, por_nombre_lower, por_alias


_IDX_SLUG, _IDX_NOMBRE, _IDX_ALIAS = _build_indices()


# ── Funciones de búsqueda ─────────────────────────────────────────────────


def buscar_comunidad(query: str) -> Optional[Dict]:
    """
    Busca una comunidad por nombre, slug o alias. Búsqueda flexible.
    Acepta: "Euskadi", "pais-vasco", "País Vasco", "cataluna", etc.
    """
    q = query.strip()
    q_lower = q.lower()
    q_slug = _generar_slug(q)

    if q_slug in _IDX_SLUG:
        return _IDX_SLUG[q_slug]
    if q_lower in _IDX_NOMBRE:
        return _IDX_NOMBRE[q_lower]
    if q_lower in _IDX_ALIAS:
        return _IDX_ALIAS[q_lower]
    if q_slug in _IDX_ALIAS:
        return _IDX_ALIAS[q_slug]

    # Búsqueda parcial (substring)
    for nombre, c in _IDX_NOMBRE.items():
        if q_lower in nombre or nombre in q_lower:
            return c

    return None


def normalizar_nombre(texto: str) -> Optional[str]:
    """Dado cualquier variante de nombre, devuelve el nombre oficial."""
    c = buscar_comunidad(texto)
    return c["nombre"] if c else None


def get_slugs() -> List[str]:
    """Devuelve la lista de todos los slugs de Idealista."""
    return [c["slug_idealista"] for c in COMUNIDADES_AUTONOMAS]


def build_historico_url(comunidad: Dict) -> str:
    """
    Construye la URL de referencia de la página de histórico de alquiler.

    Ejemplo:
        https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/
        alquiler/extremadura/report/
    """
    slug = comunidad["slug_idealista"]
    return (
        f"https://www.idealista.com/sala-de-prensa/"
        f"informes-precio-vivienda/alquiler/{slug}/report/"
    )
