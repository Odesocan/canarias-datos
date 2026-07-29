"""Logger compartido de la etapa de carga (reutiliza el del pipeline)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "1_extraccion"))
from utils.logger import setup_logger  # noqa: E402

logger = setup_logger("educacion_carga")
