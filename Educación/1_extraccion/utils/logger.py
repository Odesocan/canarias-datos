"""
Logging estructurado del pipeline de extracción de Educación.
Salida simultánea a consola (concisa) y a fichero con timestamp (detallada).
Mismo patrón que el resto de áreas de Canarias en Datos.
"""

import logging
import sys
from datetime import datetime

from config.settings import LOGS_DIR


def setup_logger(name: str = "educacion_extraccion",
                 level: int = logging.INFO) -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if logger.handlers:
        return logger

    file_fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s.%(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S",
    )

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fh = logging.FileHandler(LOGS_DIR / f"extraccion_{ts}.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(file_fmt)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(console_fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
