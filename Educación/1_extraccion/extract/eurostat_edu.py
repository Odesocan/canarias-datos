"""
Extractor de los indicadores de población basados en la EPA, vía Eurostat.

Cubre 5 de los 10 indicadores del dashboard (Cuaderno §4):
  abandono_temprano, nivel_superior_25_34, nivel_bajo_25_64,
  formacion_adultos_25_64, neet_15_29
todos desagregados por CCAA (NUTS-2) y sexo.
"""

from datetime import datetime
from typing import Dict, List

from config.comunidades import por_nuts2
from config.indicadores import SEXO_MAP
from config.settings import EUROSTAT_BASE, YEAR_START
from extract.eurostat_client import fetch_dataset
from utils.logger import setup_logger

logger = setup_logger()


def extraer_indicador(ind: Dict) -> List[Dict]:
    """Descarga y normaliza un indicador Eurostat al esquema canónico."""
    ahora = datetime.now().isoformat(timespec="seconds")
    filas = fetch_dataset(ind["dataset"], ind["filtros"])

    # URL de referencia (los geos reales son la lista de CCAA españolas del cliente)
    url_fuente = (f"{EUROSTAT_BASE}{ind['dataset']}?format=JSON&lang=EN"
                  f"&sinceTimePeriod={YEAR_START}&geo=ES...ES70")
    salida = []
    descartadas = 0
    for f in filas:
        terr = por_nuts2(f.get("geo", ""))
        sexo = SEXO_MAP.get(f.get("sex", "T"), "total")
        if terr is None or f.get("valor") is None:
            descartadas += 1
            continue
        salida.append({
            "indicador": ind["key"],
            "bloque": ind["bloque"],
            "fuente": f"Eurostat · {ind['dataset']}",
            "dataset": ind["dataset"],
            "ccaa": terr["nombre"],
            "ccaa_id": terr["ccaa_id"],
            "nuts2": terr["nuts2"],
            "anio": int(f["time"]),
            "sexo": sexo,
            "valor": round(float(f["valor"]), 4),
            "unidad": ind["unidad"],
            "origen": "real",
            "extraido_en": ahora,
            "url_fuente": url_fuente,
        })
    logger.info("  %s: %d filas normalizadas (%d descartadas)",
                ind["key"], len(salida), descartadas)
    return salida
