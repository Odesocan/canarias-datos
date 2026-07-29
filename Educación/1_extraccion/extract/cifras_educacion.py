"""
Extractor de gasto_por_alumno desde "Las cifras de la educación en España" (MEFP).

El gasto público por alumno por CCAA NO existe como tabla EDUCAbase csv_bd, pero
sí en el anuario "Las cifras de la educación en España", cuaderno financiero
**B4 · El gasto en educación**, hoja **B4.6 · "Gasto público por alumno en
enseñanza no universitaria"** (fuente: Estadística del Gasto Público en
Educación · presupuesto liquidado).

Particularidades resueltas:
  · Cada edición cubre 1-2 años de referencia; se iteran varias ediciones y se
    deduplica por (CCAA, año) quedándose con el valor de la edición MÁS RECIENTE
    (dato revisado).
  · La maquetación de B4.6 varía (1 o 2 años, columnas separadoras): el parser
    localiza dinámicamente la fila de medidas ("...público y concertado" vs
    "...público") y la fila de años, y extrae el bloque de **centros públicos**.
  · Los nombres de CCAA usan formas con paréntesis ('Asturias (Principado de)'),
    resueltas por config.comunidades.por_nombre.

Se extrae la medida "Gasto público por alumno público" (centros públicos), que
es la que declara el cuaderno metodológico. Unidad: euros. Sin desglose por sexo.
"""

import io
import re
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup

from config.settings import (HTTP_TIMEOUT, HTTP_RETRIES, HTTP_BACKOFF,
                             USER_AGENT, YEAR_START)
from config.comunidades import por_nombre
from utils.logger import setup_logger

logger = setup_logger()

WEB = "https://www.educacionfpydeportes.gob.es"
EDICION_URL = (WEB + "/servicios-al-ciudadano/estadisticas/indicadores/"
               "cifras-educacion-espana/{ed}.html")

# Ediciones a barrer, de MÁS RECIENTE a más antigua (cada una aporta 1-2 años).
# Cubren de sobra 2015-2023; la deduplicación prioriza la edición más reciente.
EDICIONES = [
    "2023-2024", "2022-2023", "2021-2022", "2020-2021", "2019-2020",
    "2018-2019", "2017-2018", "2016-2017", "2015-2016",
]


def _get(url: str) -> bytes:
    last = None
    for intento in range(1, HTTP_RETRIES + 1):
        try:
            r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=HTTP_TIMEOUT)
            if r.status_code == 200 and r.content:
                return r.content
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            last = repr(e)
        if intento < HTTP_RETRIES:
            time.sleep(HTTP_BACKOFF * intento)
    raise RuntimeError(f"No se pudo descargar {url}: {last}")


def _url_cuaderno_b4(ed: str) -> Optional[str]:
    """Localiza en la página de la edición el enlace al cuaderno B4 (gasto)."""
    html = _get(EDICION_URL.format(ed=ed)).decode("utf-8", "replace")
    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all("a", href=True):
        href = a["href"]
        fn = href.split("/")[-1]
        if fn.lower().endswith(".xlsx") and re.match(r"b4[-.]", fn, re.IGNORECASE):  # b4.xlsx / B4-xlsx.xlsx
            return WEB + href if href.startswith("/") else href
    return None


def _parse_b46(contenido: bytes) -> List[Tuple[str, int, float]]:
    """Extrae (territorio, año, valor) del bloque 'centros públicos' de B4.6."""
    xl = pd.ExcelFile(io.BytesIO(contenido))
    hoja = next((s for s in xl.sheet_names
                 if xl.parse(s, header=None, nrows=6).astype(str)
                 .apply(lambda c: c.str.contains("por alumno", case=False)).any().any()), None)
    if hoja is None:
        return []
    df = xl.parse(hoja, header=None)

    # Fila de medidas = la que contiene 'concertado' (distingue los dos bloques)
    fila_med = next((i for i in range(min(8, len(df)))
                     if df.iloc[i].astype(str).str.contains("concertado", case=False).any()), None)
    if fila_med is None:
        return []
    # Etiqueta de medida por columna (forward-fill a lo ancho)
    medidas = df.iloc[fila_med].astype("object").where(df.iloc[fila_med].notna()).ffill()

    # Fila de años = primera fila tras las medidas con celdas de 4 dígitos
    fila_anio = None
    for i in range(fila_med + 1, min(fila_med + 4, len(df))):
        if df.iloc[i].astype(str).str.fullmatch(r"\d{4}(\.0)?").any():
            fila_anio = i
            break
    if fila_anio is None:
        return []

    # Columnas del bloque 'público' (centros públicos): medida con 'público' y sin 'concertado'
    cols_publico = {}
    for col in range(1, df.shape[1]):
        etiqueta = str(medidas.get(col, ""))
        celda = str(df.iat[fila_anio, col])
        m = re.fullmatch(r"(\d{4})(\.0)?", celda)
        if not m:
            continue
        if "público" in etiqueta.lower() and "concertado" not in etiqueta.lower():
            cols_publico[col] = int(m.group(1))

    filas, sin_map = [], set()
    for i in range(fila_anio + 1, len(df)):
        nombre = df.iat[i, 0]
        if not isinstance(nombre, str) or not nombre.strip() or nombre.strip().startswith("("):
            continue
        terr = por_nombre(nombre)
        if terr is None:
            sin_map.add(nombre.strip())
            continue
        for col, anio in cols_publico.items():
            val = pd.to_numeric(str(df.iat[i, col]).replace(".", "").replace(",", "."),
                                errors="coerce") if isinstance(df.iat[i, col], str) \
                  else pd.to_numeric(df.iat[i, col], errors="coerce")
            if pd.notna(val):
                filas.append((terr["nombre"], anio, float(val)))
    if sin_map:
        logger.info("  Cifras: %d etiquetas de territorio no mapeadas (p. ej. Ceuta/Melilla "
                    "combinadas): %s", len(sin_map), sorted(sin_map))
    return filas


def extraer() -> List[Dict]:
    """Ensambla la serie de gasto por alumno (centros públicos) por CCAA y año."""
    ahora = datetime.now().isoformat(timespec="seconds")
    vistos: Dict[Tuple[str, int], Dict] = {}   # (ccaa, anio) -> fila (prioriza edición reciente)

    for ed in EDICIONES:                        # de más reciente a más antigua
        try:
            url = _url_cuaderno_b4(ed)
            if not url:
                logger.warning("Cifras %s: no se encontró el cuaderno B4", ed)
                continue
            filas = _parse_b46(_get(url))
            nuevos = 0
            for nombre, anio, valor in filas:
                terr = por_nombre(nombre)
                clave = (terr["ccaa_id"], anio)
                if clave in vistos:             # ya lo tenemos de una edición más reciente
                    continue
                vistos[clave] = {
                    "indicador": "gasto_por_alumno", "bloque": "D",
                    "fuente": f"MEFP · Cifras de la Educación {ed} · B4.6",
                    "dataset": f"cifras_educacion/{ed}/b4.xlsx#B4.6",
                    "ccaa": terr["nombre"], "ccaa_id": terr["ccaa_id"], "nuts2": terr["nuts2"],
                    "anio": anio, "sexo": "total", "valor": round(valor, 2),
                    "unidad": "EUR", "origen": "real", "extraido_en": ahora,
                    "url_fuente": url,
                }
                nuevos += 1
            logger.info("Cifras %s: %d años·CCAA nuevos (%d filas en B4.6)", ed, nuevos, len(filas))
        except Exception as e:  # noqa: BLE001
            logger.warning("Cifras %s: fallo (%s)", ed, e)

    salida = [f for f in vistos.values() if f["anio"] >= YEAR_START]
    salida.sort(key=lambda r: (r["ccaa_id"], r["anio"]))
    logger.info("  gasto_por_alumno: %d filas (%d-%d) desde Cifras de la Educación",
                len(salida),
                min((f["anio"] for f in salida), default=0),
                max((f["anio"] for f in salida), default=0))
    return salida
