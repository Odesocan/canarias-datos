# -*- coding: utf-8 -*-
"""
Normalización territorial y utilidades de parseo para la extracción de Empleo.

- Diccionario canónico de CCAA con códigos INE (§7.2 del cuaderno).
- Detección de territorio y genero a partir del nombre de la serie del INE
  (las series vienen como texto libre y la posición de cada dimensión varía
  entre tablas, por lo que se hace por coincidencia de subcadena distintiva).
- Parseo de periodo (trimestre/mes/año) del punto de datos de la API.
- Parseo numérico con locale español (para futuros ficheros SEPE/TGSS, §7.5).

Nota: el diccionario de ISLAS de Canarias se construirá cuando se incorpore la
fuente ISTAC (única con desglose insular garantizado). Aquí se cubre el nivel
Total Nacional + 17 CCAA + Ceuta/Melilla.
"""
from __future__ import annotations

import unicodedata
from datetime import datetime, timezone


# --------------------------------------------------------------------------- #
# Diccionario canónico de CCAA (código INE, nombre canónico, variantes)
# --------------------------------------------------------------------------- #
# Las variantes son subcadenas DISTINTIVAS ya normalizadas (minúsculas, sin
# acentos) que aparecen en los nombres de serie del INE.
CANON_CCAA: list[tuple[str, str, tuple[str, ...]]] = [
    ("00", "Total Nacional", ("total nacional",)),
    ("01", "Andalucía", ("andalucia",)),
    ("02", "Aragón", ("aragon",)),
    ("03", "Principado de Asturias", ("asturias",)),
    ("04", "Illes Balears", ("balears", "baleares")),
    ("05", "Canarias", ("canarias",)),
    ("06", "Cantabria", ("cantabria",)),
    ("07", "Castilla y León", ("castilla y leon", "castilla - leon", "castilla-leon")),
    ("08", "Castilla-La Mancha", ("castilla - la mancha", "castilla-la mancha", "castilla la mancha")),
    ("09", "Cataluña", ("cataluna", "catalunya")),
    ("10", "Comunitat Valenciana", ("valenciana",)),
    ("11", "Extremadura", ("extremadura",)),
    ("12", "Galicia", ("galicia",)),
    ("13", "Comunidad de Madrid", ("madrid",)),
    ("14", "Región de Murcia", ("murcia",)),
    ("15", "Comunidad Foral de Navarra", ("navarra",)),
    ("16", "País Vasco", ("pais vasco", "euskadi")),
    ("17", "La Rioja", ("rioja",)),
    ("18", "Ceuta", ("ceuta",)),
    ("19", "Melilla", ("melilla",)),
]


def normaliza_texto(texto: str) -> str:
    """Minúsculas y sin acentos, para comparaciones robustas."""
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def detecta_territorio(nombre_serie: str) -> tuple[str | None, str | None]:
    """Devuelve (codigo_ine, nombre_canonico) del territorio de la serie.

    Prioriza 'Total Nacional' y usa subcadenas distintivas para no confundir
    Castilla y León con Castilla-La Mancha, ni La Rioja con otras CCAA.
    """
    norm = normaliza_texto(nombre_serie)
    # 'total nacional' primero (contiene 'nacional')
    for codigo, canonico, variantes in CANON_CCAA:
        if any(v in norm for v in variantes):
            return codigo, canonico
    return None, None


def detecta_genero(nombre_serie: str) -> str | None:
    """Devuelve 'Ambos géneros' | 'Hombres' | 'Mujeres' | None."""
    norm = normaliza_texto(nombre_serie)
    if "ambos sexos" in norm:
        return "Ambos géneros"
    if "mujeres" in norm:
        return "Mujeres"
    if "hombres" in norm:
        return "Hombres"
    return None


# --------------------------------------------------------------------------- #
# Periodo
# --------------------------------------------------------------------------- #
_PERIODICIDAD = {1: "anual", 3: "trimestral", 6: "semestral", 12: "mensual"}


def parse_periodo(punto: dict) -> dict:
    """Extrae año, periodo legible y periodicidad de un punto de datos de la API."""
    anyo = punto.get("Anyo")
    periodo_obj = punto.get("Periodo") or {}
    fk = periodo_obj.get("FK_Periodicidad")
    periodicidad = _PERIODICIDAD.get(fk, "desconocida")
    nombre_periodo = punto.get("NombrePeriodo")  # p. ej. '2026T1' o '2024'
    # marca temporal (la API da epoch en milisegundos)
    fecha_ms = punto.get("Fecha")
    fecha_iso = None
    if fecha_ms:
        fecha_iso = datetime.fromtimestamp(fecha_ms / 1000, tz=timezone.utc).date().isoformat()
    return {
        "anyo": anyo,
        "periodo": nombre_periodo,
        "periodicidad": periodicidad,
        "num_periodo": periodo_obj.get("Valor"),
        "fecha": fecha_iso,
    }


# --------------------------------------------------------------------------- #
# Parseo numérico locale español (para ficheros SEPE/TGSS futuros, §7.5)
# --------------------------------------------------------------------------- #
def parse_numero_es(valor) -> float | None:
    """Convierte '1.234,56' (locale español) a float. Robusto ante None/vacíos."""
    if valor is None:
        return None
    if isinstance(valor, (int, float)):
        return float(valor)
    s = str(valor).strip()
    if s in ("", "-", "..", "…", "N/A", "n/a"):
        return None
    s = s.replace(".", "").replace("\xa0", "").replace(" ", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None
