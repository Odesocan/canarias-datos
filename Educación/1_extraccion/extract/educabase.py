"""
Extractor de EDUCAbase (MEFP) — cliente PC-Axis / Jaxi.

HALLAZGO DEL SIMULACRO (2026-07-21): EDUCAbase NO exige scraping con navegador.
Corre sobre la plataforma PC-Axis (Jaxi) del INE — la misma de INEbase — y cada
tabla expone descargas directas de fichero en varios formatos:

    https://estadisticas.educacion.gob.es/EducaJaxiPx/files/_px/es/{fmt}/{path}/{file}.{ext}?nocab=1

El formato `csv_bd` ("base de datos") viene ya en formato largo/tidy (una fila por
combinación de dimensiones + valor), separado por tabuladores y codificado en
ISO-8859-15. Por eso este extractor usa `requests` (robusto, reproducible, sin
anti-bot), en lugar de nodriver/Playwright como en Idealista/Booking.

Cada tabla se declara en TABLAS con su path, fichero y el mapeo de sus columnas
de dimensión a los campos canónicos del proyecto (ccaa, sexo, curso→año).
"""

from datetime import datetime
from typing import Dict, List, Optional

import requests

from config.settings import HTTP_TIMEOUT, HTTP_RETRIES, HTTP_BACKOFF, USER_AGENT, YEAR_START
from config.comunidades import por_nombre
from utils.logger import setup_logger
import time

logger = setup_logger()

JAXI_FILES = "https://estadisticas.educacion.gob.es/EducaJaxiPx/files/_px/es/"

# Mapeo de la columna "Sexo" de EDUCAbase a la etiqueta canónica
SEXO_MAP = {
    "AMBOS SEXOS": "total", "TOTAL": "total",
    "HOMBRES": "hombres", "MUJERES": "mujeres",
    "VARONES": "hombres", "MUJER": "mujeres", "HOMBRE": "hombres",
}

# Registro de tablas EDUCAbase por indicador del dashboard.
# `path` y `file` se obtienen del diálogo de exportación (dlgExport.htm).
# `col_*` indican qué columna del csv_bd corresponde a cada dimensión.
TABLAS = {
    "idoneidad_15": {
        "path": "no-universitaria/alumnado/matriculado/series-new/gen-idoneidad/l0",
        "file": "idoneidad_05",              # 05 = edad de 15 años
        "col_sexo": "Sexo",
        "col_ccaa": "Comunidad autónoma",
        "col_curso": "periodo",
        "unidad": "%",
    },
    "escolarizacion_0_2": {
        "path": "no-universitaria/alumnado/matriculado/series-new/gen-escolar/l0",
        "file": "escolar_05",                # 05 = tasa neta de 0 a 2 años
        "col_sexo": "Sexo",
        "col_ccaa": "Comunidad autónoma",
        "col_curso": "periodo",
        "unidad": "%",
    },
    "graduacion_eso": {
        "path": "no-universitaria/alumnado/resultados/series-hasta-2023-2024-rd/alumnado/l0",
        "file": "series_1_03",               # Tasa bruta que finaliza ESO (Graduado en ESO)
        "col_sexo": "Sexo",
        "col_ccaa": "Comunidad autónoma",
        "col_curso": "periodo",
        "unidad": "%",
    },
    # gasto_por_alumno NO tiene tabla EDUCAbase csv_bd por CCAA (las series de gasto
    # son nacionales por tipo de administración). Es un indicador de síntesis: se
    # obtiene de "Cifras de la Educación" o se deriva (gasto CCAA / alumnado CCAA)
    # en la etapa de transformación. Ver config/indicadores.py.
}


def _url_csv_bd(path: str, file: str) -> str:
    return f"{JAXI_FILES}csv_bd/{path}/{file}.csv_bd?nocab=1"


def descargar_csv_bd(path: str, file: str) -> str:
    """Descarga el csv_bd de una tabla EDUCAbase (con reintentos). Devuelve texto."""
    url = _url_csv_bd(path, file)
    last = None
    for intento in range(1, HTTP_RETRIES + 1):
        try:
            r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=HTTP_TIMEOUT)
            if r.status_code == 200 and r.content:
                # El servidor declara ISO-8859-15 pero envía UTF-8 con BOM.
                # Decodificamos por contenido, no por la cabecera (que miente):
                # utf-8-sig (quita BOM) y, si falla, latin-1 como red de seguridad.
                try:
                    texto = r.content.decode("utf-8-sig")
                except UnicodeDecodeError:
                    texto = r.content.decode("ISO-8859-15", "replace")
                logger.info("EDUCAbase %s/%s: %d bytes", path.split('/')[-1], file, len(r.content))
                return texto
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            last = repr(e)
        logger.warning("EDUCAbase %s: %s (intento %d/%d)", file, last, intento, HTTP_RETRIES)
        if intento < HTTP_RETRIES:
            time.sleep(HTTP_BACKOFF * intento)
    raise RuntimeError(f"No se pudo descargar {url}: {last}")


def _parse_num(txt: str) -> Optional[float]:
    """Parsea número en locale español; None para celdas ausentes (.., -, vacío)."""
    t = (txt or "").strip()
    if t in ("", "..", ".", "-", "n.d.", "s.e."):
        return None
    try:
        return float(t.replace(".", "").replace(",", "."))
    except ValueError:
        return None


def _curso_a_anio(curso: str) -> Optional[int]:
    """'2024-25' -> 2024 (año natural de inicio del curso; Cuaderno §5.3)."""
    c = (curso or "").strip()
    for sep in ("-", "/"):
        if sep in c:
            ini = c.split(sep)[0].strip()
            if ini.isdigit():
                return int(ini[:4])
    return int(c[:4]) if c[:4].isdigit() else None


def parse_csv_bd(texto: str, spec: Dict) -> List[Dict]:
    """
    Parsea el csv_bd (tab-separado) a filas {sexo, ccaa, anio, valor} canónicas.
    La última columna es el valor; el resto son dimensiones nombradas en la cabecera.
    """
    lineas = [l for l in texto.splitlines() if l.strip()]
    if not lineas:
        return []
    # Cabecera (quitar BOM si lo hubiera)
    cab = [c.strip().lstrip("﻿") for c in lineas[0].split("\t")]
    idx = {name: i for i, name in enumerate(cab)}
    i_sexo = idx.get(spec["col_sexo"])
    i_ccaa = idx.get(spec["col_ccaa"])
    i_curso = idx.get(spec["col_curso"])
    i_val = len(cab) - 1  # el valor es la última columna

    filas, sin_map = [], set()
    for ln in lineas[1:]:
        celdas = ln.split("\t")
        if len(celdas) <= i_val:
            continue
        terr = por_nombre(celdas[i_ccaa]) if i_ccaa is not None else None
        if terr is None:
            sin_map.add(celdas[i_ccaa] if i_ccaa is not None else "?")
            continue
        anio = _curso_a_anio(celdas[i_curso]) if i_curso is not None else None
        sexo = SEXO_MAP.get(celdas[i_sexo].strip().upper(), "total") if i_sexo is not None else "total"
        valor = _parse_num(celdas[i_val])
        if anio is None:
            continue
        filas.append({
            "ccaa": terr["nombre"], "ccaa_id": terr["ccaa_id"], "nuts2": terr["nuts2"],
            "anio": anio, "sexo": sexo, "valor": valor,
        })
    if sin_map:
        logger.info("  EDUCAbase: %d etiquetas de CCAA no mapeadas (revisar): %s",
                    len(sin_map), sorted(sin_map)[:8])
    return filas


def extraer(indicador_key: str, bloque: str) -> List[Dict]:
    """Extrae un indicador MEFP declarado en TABLAS al esquema canónico completo."""
    spec = TABLAS.get(indicador_key)
    if spec is None:
        raise KeyError(f"{indicador_key} no está declarado en educabase.TABLAS")
    ahora = datetime.now().isoformat(timespec="seconds")
    texto = descargar_csv_bd(spec["path"], spec["file"])
    base = parse_csv_bd(texto, spec)
    url_fuente = _url_csv_bd(spec["path"], spec["file"])
    salida = []
    n_prev = 0
    for f in base:
        if f["anio"] < YEAR_START:          # ventana del proyecto (coherente con Eurostat/Cifras)
            n_prev += 1
            continue
        salida.append({
            "indicador": indicador_key, "bloque": bloque,
            "fuente": "MEFP · EDUCAbase (PC-Axis)", "dataset": f"{spec['file']}.px",
            "ccaa": f["ccaa"], "ccaa_id": f["ccaa_id"], "nuts2": f["nuts2"],
            "anio": f["anio"], "sexo": f["sexo"],
            "valor": round(f["valor"], 4) if f["valor"] is not None else None,
            "unidad": spec["unidad"], "origen": "real", "extraido_en": ahora,
            "url_fuente": url_fuente,
        })
    logger.info("  %s: %d filas normalizadas desde EDUCAbase (%d filas < %d descartadas)",
                indicador_key, len(salida), n_prev, YEAR_START)
    return salida
