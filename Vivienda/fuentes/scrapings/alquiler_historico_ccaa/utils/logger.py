"""
Logging estructurado para el pipeline ETL.
Genera logs tanto en consola como en archivo con rotación.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

from config.settings import LOGS_DIR


def setup_logger(
    name: str = "historico_etl",
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Configura y retorna un logger con salida a consola y archivo.

    Args:
        name: Nombre del logger.
        level: Nivel mínimo de logging.

    Returns:
        Logger configurado.
    """
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Evitar duplicación de handlers si se llama varias veces
    if logger.handlers:
        return logger

    # Formato detallado para archivo
    file_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s.%(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Formato conciso para consola
    console_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%H:%M:%S",
    )

    # Handler de archivo con timestamp en nombre
    timestamp = datetime.now().strftime("%Y%m%d")
    file_handler = logging.FileHandler(
        LOGS_DIR / f"etl_{timestamp}.log",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Handler de consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
