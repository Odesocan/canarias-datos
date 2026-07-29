"""
Catálogo territorial canónico: 17 CCAA + 2 ciudades autónomas + nacional.

Enlaza el nombre canónico con el código INE (2 dígitos) y el código NUTS-2 de
Eurostat, además de la población de referencia. Es el equivalente Python del
R/ccaa_dictionary.R del resto de pipelines.
"""

import unicodedata
from typing import Dict, List, Optional


def _norm(txt: str) -> str:
    """Minúsculas sin acentos ni espacios extremos, para búsqueda flexible."""
    n = unicodedata.normalize("NFD", txt or "")
    n = "".join(c for c in n if unicodedata.category(c) != "Mn")
    return n.lower().strip()


def _t(nombre, ine, nuts2, poblacion, tipo, aliases=None):
    return {
        "nombre": nombre,
        "ccaa_id": ine,
        "nuts2": nuts2,
        "poblacion_2024": poblacion,
        "tipo": tipo,               # ccaa | ciudad_autonoma | nacional
        "aliases": aliases or [],
    }


# tipo: 'ccaa' (17 oficiales), 'ciudad_autonoma' (Ceuta/Melilla), 'nacional' (España)
TERRITORIOS: List[Dict] = [
    _t("España",                    "00", "ES",   48_085_000, "nacional",
       aliases=["Total Nacional", "Nacional", "Total", "European Union", "Spain"]),
    _t("Andalucía",                 "01", "ES61",  8_584_000, "ccaa"),
    _t("Aragón",                    "02", "ES24",  1_351_000, "ccaa"),
    _t("Principado de Asturias",    "03", "ES12",  1_006_000, "ccaa",
       aliases=["Asturias", "Asturias, Principado de"]),
    _t("Illes Balears",             "04", "ES53",  1_209_000, "ccaa",
       aliases=["Baleares", "Islas Baleares", "Balearic Islands", "Balears, Illes", "Balears"]),
    _t("Canarias",                  "05", "ES70",  2_213_000, "ccaa",
       aliases=["Canary Islands"]),
    _t("Cantabria",                 "06", "ES13",    588_000, "ccaa"),
    _t("Castilla y León",           "07", "ES41",  2_383_000, "ccaa",
       aliases=["Cast. y León", "Castilla-León"]),
    _t("Castilla-La Mancha",        "08", "ES42",  2_085_000, "ccaa",
       aliases=["Cast.-La Mancha", "Castilla - La Mancha", "Castilla La Mancha"]),
    _t("Cataluña",                  "09", "ES51",  7_901_000, "ccaa",
       aliases=["Catalunya", "Catalonia"]),
    _t("Comunitat Valenciana",      "10", "ES52",  5_216_000, "ccaa",
       aliases=["Comunidad Valenciana", "C. Valenciana", "Valencia"]),
    _t("Extremadura",               "11", "ES43",  1_054_000, "ccaa"),
    _t("Galicia",                   "12", "ES11",  2_705_000, "ccaa"),
    _t("Comunidad de Madrid",       "13", "ES30",  6_871_000, "ccaa",
       aliases=["Madrid", "C. de Madrid", "Madrid, Comunidad de"]),
    _t("Región de Murcia",          "14", "ES62",  1_567_000, "ccaa",
       aliases=["Murcia", "Murcia, Región de"]),
    _t("Comunidad Foral de Navarra","15", "ES22",    668_000, "ccaa",
       aliases=["Navarra", "Navarra, Comunidad Foral de"]),
    _t("País Vasco",                "16", "ES21",  2_224_000, "ccaa",
       aliases=["Euskadi", "Basque Country", "País Vasco/Euskadi"]),
    _t("La Rioja",                  "17", "ES23",    322_000, "ccaa",
       aliases=["Rioja", "Rioja, La"]),
    _t("Ciudad de Ceuta",           "18", "ES63",     83_000, "ciudad_autonoma",
       aliases=["Ceuta"]),
    _t("Ciudad de Melilla",         "19", "ES64",     85_000, "ciudad_autonoma",
       aliases=["Melilla"]),
]

# Índices de búsqueda -----------------------------------------------------------
BY_NUTS2: Dict[str, Dict] = {t["nuts2"]: t for t in TERRITORIOS}
BY_INE: Dict[str, Dict] = {t["ccaa_id"]: t for t in TERRITORIOS}

# nombre normalizado (canónico + aliases) -> territorio
_BY_NAME: Dict[str, Dict] = {}
for _terr in TERRITORIOS:
    _BY_NAME[_norm(_terr["nombre"])] = _terr
    for _al in _terr["aliases"]:
        _BY_NAME[_norm(_al)] = _terr

# Los 17 códigos NUTS-2 de las CCAA oficiales (sin nacional ni ciudades)
NUTS2_CCAA = [t["nuts2"] for t in TERRITORIOS if t["tipo"] == "ccaa"]
# Todos los geos a solicitar a Eurostat (incluye nacional y ciudades autónomas)
NUTS2_ALL = [t["nuts2"] for t in TERRITORIOS]
CCAA_OFICIALES = [t["nombre"] for t in TERRITORIOS if t["tipo"] == "ccaa"]


def por_nuts2(codigo: str) -> Optional[Dict]:
    return BY_NUTS2.get(codigo)


import re as _re
_TRAILING_PAREN = _re.compile(r"\s*\([^)]*\)\s*$")   # nota al pie " (2)" o forma " (Principado de)"


# Nombres de salida alineados con las tablas del resto del proyecto (join geográfico
# del hub D3 por nombre). Vivienda/Salud Mental usan estas variantes; las demás
# coinciden con el nombre canónico.
_NOMBRE_SALIDA = {"04": "Islas Baleares", "10": "Comunidad Valenciana"}


def nombre_salida(ccaa_id: str, nombre_canonico: str) -> str:
    return _NOMBRE_SALIDA.get(ccaa_id, nombre_canonico)


def por_nombre(nombre: str) -> Optional[Dict]:
    """Resuelve un nombre libre (INE, Eurostat, MEFP, coloquial) al territorio canónico.

    Tolera marcadores de nota al pie ('Navarra, Comunidad Foral de (2)') y las
    formas con paréntesis de los Excel del MEFP ('Asturias (Principado de)').
    """
    if not nombre:
        return None
    t = _BY_NAME.get(_norm(nombre))
    if t is None:
        t = _BY_NAME.get(_norm(_TRAILING_PAREN.sub("", nombre)))
    return t
