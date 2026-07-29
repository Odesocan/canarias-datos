"""
Estado de los indicadores MEFP sin fuente automatizable.

ACTUALIZACIÓN (simulacro 2026-07-21): EDUCAbase resultó ser PC-Axis (Jaxi) con
descarga directa `csv_bd` — NO requiere scraping. Idoneidad, graduación en ESO y
escolarización 0-2 ya se extraen en extract/educabase.py.

Queda un único indicador pendiente: `gasto_por_alumno` por CCAA. No existe como
tabla EDUCAbase csv_bd (las series de gasto son nacionales por tipo de
administración). Es un indicador de síntesis (publicación 'Cifras de la
Educación' / Sistema Estatal de Indicadores) o derivable en la etapa de
transformación (gasto público por CCAA ÷ alumnado por CCAA).

Este módulo NO inventa datos: reporta el/los pendientes con su motivo para que
el informe QA lo refleje con transparencia.
"""

from typing import Dict, List

from config.indicadores import PENDIENTES
from utils.logger import setup_logger

logger = setup_logger()


def estado_pendientes() -> List[Dict]:
    """Devuelve la ficha de estado de cada indicador MEFP pendiente."""
    fichas = []
    for ind in PENDIENTES:
        logger.warning("MEFP pendiente · %s — sin API pública (%s)",
                       ind["key"], ind.get("fuente_url", "EDUCAbase"))
        fichas.append({
            "indicador": ind["key"],
            "bloque": ind["bloque"],
            "fuente": ind["fuente"],
            "dataset": ind["dataset"],
            "estado": "pendiente",
            "motivo": ind.get("motivo",
                              "Sin fuente automatizable a día de hoy; requiere descarga manual"),
            "fuente_url": ind.get("fuente_url"),
            "desagrega_sexo": ind["desagrega_sexo"],
        })
    return fichas


def extraer() -> List[Dict]:
    """Interfaz homóloga a los demás extractores: aún no produce filas de datos."""
    logger.info("MEFP: 0 filas (4 indicadores pendientes de fuente automatizable)")
    return []
