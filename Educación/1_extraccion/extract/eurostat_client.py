"""
Cliente HTTP de la API de difusión de Eurostat (JSON-stat 2.0).

Descarga un dataset filtrado a los territorios españoles (NUTS-2 = CCAA) desde
YEAR_START, con reintentos y backoff. Devuelve las filas ya decodificadas.
"""

import time
from typing import Dict, List

import requests

from config.settings import (EUROSTAT_BASE, HTTP_TIMEOUT, HTTP_RETRIES,
                             HTTP_BACKOFF, USER_AGENT, YEAR_START)
from config.comunidades import NUTS2_ALL
from utils.jsonstat import a_filas
from utils.logger import setup_logger

logger = setup_logger()


def fetch_dataset(dataset: str, filtros: Dict[str, List[str]]) -> List[Dict]:
    """
    Descarga `dataset` con los `filtros` dados (dict dim -> lista de códigos),
    restringido a todos los geos españoles y a time >= YEAR_START.

    Devuelve la lista de filas tidy (una por celda no vacía).
    """
    params = [("format", "JSON"), ("lang", "EN"),
              ("sinceTimePeriod", str(YEAR_START))]
    for geo in NUTS2_ALL:
        params.append(("geo", geo))
    for dim, codigos in filtros.items():
        for c in codigos:
            params.append((dim, c))

    url = EUROSTAT_BASE + dataset
    last_err = None
    for intento in range(1, HTTP_RETRIES + 1):
        try:
            resp = requests.get(url, params=params,
                                headers={"User-Agent": USER_AGENT},
                                timeout=HTTP_TIMEOUT)
            if resp.status_code == 200:
                filas = a_filas(resp.json())
                logger.info("Eurostat %s: %d celdas descargadas", dataset, len(filas))
                return filas
            if resp.status_code == 416:  # rango/filtros sin datos: no es un error
                logger.warning("Eurostat %s: HTTP 416 (sin datos para los filtros) -> []", dataset)
                return []
            logger.warning("Eurostat %s: HTTP %d (intento %d/%d)",
                           dataset, resp.status_code, intento, HTTP_RETRIES)
            last_err = f"HTTP {resp.status_code}: {resp.text[:200]}"
        except (requests.RequestException, ValueError) as e:
            last_err = repr(e)
            logger.warning("Eurostat %s: error %s (intento %d/%d)",
                           dataset, last_err, intento, HTTP_RETRIES)
        if intento < HTTP_RETRIES:
            time.sleep(HTTP_BACKOFF * intento)

    raise RuntimeError(f"No se pudo descargar {dataset}: {last_err}")
