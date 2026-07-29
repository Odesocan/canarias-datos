"""
Exportador de datos procesados a CSV.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict

import pandas as pd

from config.settings import PROCESSED_DIR
from utils.logger import setup_logger

logger = setup_logger("csv_exporter")


class CSVExporter:
    """
    Exporta el DataFrame procesado a CSV.
    Genera un archivo completo con todos los campos.
    """

    def export(
        self,
        df: pd.DataFrame,
        output_dir: Path = None,
    ) -> Dict[str, Path]:
        """
        Exporta el DataFrame a CSV.

        Args:
            df: DataFrame procesado.
            output_dir: Directorio de salida.

        Returns:
            Dict con nombre → ruta del archivo generado.
        """
        if output_dir is None:
            output_dir = Path.home() / "Desktop"

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        paths = {}

        # Dataset completo
        filename = f"alquiler_historico_ccaa_{timestamp}.csv"
        filepath = output_dir / filename
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        paths["completo"] = filepath
        logger.info(
            f"CSV exportado: {filepath} ({len(df)} filas)"
        )

        # Copia en PROCESSED_DIR para que --stage load pueda encontrarlo
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        processed_path = PROCESSED_DIR / filename
        df.to_csv(processed_path, index=False, encoding="utf-8-sig")
        paths["processed"] = processed_path
        logger.info(f"Copia procesada: {processed_path}")

        return paths
