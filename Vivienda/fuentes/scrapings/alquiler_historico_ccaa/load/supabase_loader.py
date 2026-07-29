"""
Cargador de datos a Supabase (PostgreSQL).
Implementa upsert por clave compuesta (comunidad, mes, periodo).
"""

from typing import Dict, List, Any, Optional

import pandas as pd

from config.supabase_config import (
    SUPABASE_URL,
    SUPABASE_KEY,
    TABLE_NAME,
    BATCH_SIZE,
    UPSERT_ON_CONFLICT,
    CREATE_TABLE_SQL,
)
from utils.logger import setup_logger

logger = setup_logger("supabase_loader")


class SupabaseLoader:
    """
    Carga datos procesados a Supabase.

    Características:
    - Upsert: actualiza si ya existe (por comunidad + mes + periodo)
    - Carga por lotes (batches) para evitar timeouts
    - Logging detallado de cada operación
    - Creación automática de tabla si no existe
    """

    def __init__(
        self,
        url: Optional[str] = None,
        key: Optional[str] = None,
    ):
        self.url = url or SUPABASE_URL
        self.key = key or SUPABASE_KEY
        self.client = None

    def connect(self) -> None:
        """Establece conexión con Supabase."""
        if not self.url or not self.key:
            raise ValueError(
                "Credenciales de Supabase no configuradas. "
                "Definir SUPABASE_URL y SUPABASE_KEY en .env"
            )
        try:
            from supabase import create_client

            self.client = create_client(self.url, self.key)
            logger.info(f"Conectado a Supabase: {self.url[:40]}...")
        except ImportError:
            logger.error(
                "supabase-py no instalado. Ejecutar: pip install supabase"
            )
            raise
        except Exception as e:
            logger.error(f"Error conectando a Supabase: {e}")
            raise

    def print_create_table_sql(self) -> None:
        """
        Muestra el SQL para crear la tabla.
        Requiere ejecución manual desde el SQL Editor de Supabase Dashboard.
        """
        logger.info(
            "Para crear la tabla, ejecutar el siguiente SQL en el "
            "SQL Editor de Supabase Dashboard:"
        )
        logger.info(CREATE_TABLE_SQL)

    def load(self, df: pd.DataFrame) -> Dict[str, int]:
        """
        Carga DataFrame a Supabase con upsert.

        Args:
            df: DataFrame procesado para cargar.

        Returns:
            Dict con estadísticas de carga.
        """
        if self.client is None:
            self.connect()

        records = self._df_to_records(df)
        total = len(records)
        loaded = 0
        errors = 0

        logger.info(f"Cargando {total} registros a Supabase ({TABLE_NAME})")

        # Cargar por lotes
        for i in range(0, total, BATCH_SIZE):
            batch = records[i : i + BATCH_SIZE]
            batch_num = (i // BATCH_SIZE) + 1
            total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE

            try:
                response = (
                    self.client.table(TABLE_NAME)
                    .upsert(batch, on_conflict=UPSERT_ON_CONFLICT)
                    .execute()
                )

                batch_loaded = len(batch)
                loaded += batch_loaded
                logger.debug(
                    f"  Batch {batch_num}/{total_batches}: "
                    f"{batch_loaded} registros cargados"
                )

            except Exception as e:
                errors += len(batch)
                logger.error(
                    f"  Error en batch {batch_num}/{total_batches}: {e}"
                )

        stats = {
            "total": total,
            "cargados": loaded,
            "errores": errors,
            "tasa_exito": round(loaded / max(total, 1) * 100, 1),
        }

        logger.info(
            f"Carga completada: {loaded}/{total} registros "
            f"({stats['tasa_exito']}% éxito)"
        )

        return stats

    def _df_to_records(self, df: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Convierte DataFrame a lista de diccionarios para Supabase.
        Maneja NaN y tipos incompatibles.
        """
        # Reemplazar NaN con None para JSON
        df_clean = df.where(df.notna(), None)

        records = df_clean.to_dict(orient="records")

        # Campos que deben ser enteros en PostgreSQL (SMALLINT)
        int_fields = {"mes", "periodo"}

        for record in records:
            for key, value in record.items():
                if isinstance(value, float) and (value != value):  # NaN check
                    record[key] = None
                elif hasattr(value, "item"):  # numpy types
                    record[key] = value.item()
                elif key in int_fields and isinstance(value, float):
                    record[key] = int(value)

        return records

    def get_existing_keys(self) -> set:
        """
        Obtiene las claves compuestas ya existentes en Supabase.
        Útil para scraping incremental.

        Returns:
            Set de tuplas (comunidad, mes, periodo).
        """
        if self.client is None:
            self.connect()

        try:
            response = (
                self.client.table(TABLE_NAME)
                .select("comunidad,mes,periodo")
                .execute()
            )
            return {
                (r["comunidad"], r["mes"], r["periodo"])
                for r in response.data
            }
        except Exception as e:
            logger.error(f"Error obteniendo claves existentes: {e}")
            return set()
