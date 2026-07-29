"""
Limpieza y transformación de datos crudos del histórico de alquiler por CCAA.
Convierte datos crudos (strings en formato español) a formato tidy numérico.
"""

import re
from typing import Any, Dict, List, Optional

import pandas as pd

from utils.logger import setup_logger

logger = setup_logger("cleaner")


# ── Mapeo de meses en español ─────────────────────────────────────────────

MESES_ES = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}


class HistoricoCleaner:
    """
    Limpia y transforma datos crudos del scraping de histórico.

    Transformaciones:
    1. Split "Marzo 2026" → mes=3, periodo=2026, mes_nombre="Marzo"
    2. Parse "12,5 €/m²" → 12.5 (float)
    3. Parse "1,2%" → 1.2, "-" → None, "n.d." → None
    4. Deduplicación por (comunidad, mes, periodo)
    5. Validación de rangos
    """

    def clean(self, records: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Pipeline completo de limpieza.

        Args:
            records: Lista de diccionarios crudos del scraper.

        Returns:
            DataFrame limpio en formato tidy.
        """
        if not records:
            logger.warning("No hay registros para limpiar")
            return pd.DataFrame()

        df = pd.DataFrame(records)
        initial = len(df)
        logger.info(f"Limpiando {initial} registros crudos")

        df = self._split_mes_periodo(df)
        df = self._parse_precio_m2(df)
        df = self._parse_variaciones(df)
        df = self._remove_invalid(df)
        df = self._remove_duplicates(df)
        df = self._validate_ranges(df)
        df = self._select_columns(df)

        logger.info(
            f"Limpieza completada: {len(df)} registros válidos "
            f"(de {initial} crudos, {initial - len(df)} descartados)"
        )

        return df

    def _split_mes_periodo(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Divide 'Marzo 2026' en mes (3), periodo (2026), mes_nombre ('Marzo').
        """
        def parse_mes_raw(text: str):
            if not text or not isinstance(text, str):
                return None, None, None

            parts = text.strip().split()
            if len(parts) < 2:
                return None, None, None

            mes_nombre = parts[0].strip()
            mes_num = MESES_ES.get(mes_nombre.lower())

            try:
                periodo = int(parts[1])
            except (ValueError, IndexError):
                return None, None, None

            return mes_nombre, mes_num, periodo

        parsed = df["mes_raw"].apply(parse_mes_raw)
        df["mes_nombre"] = parsed.apply(lambda x: x[0])
        df["mes"] = parsed.apply(lambda x: x[1])
        df["periodo"] = parsed.apply(lambda x: x[2])

        # Eliminar columna cruda
        df = df.drop(columns=["mes_raw"], errors="ignore")

        return df

    def _parse_precio_m2(self, df: pd.DataFrame) -> pd.DataFrame:
        """Parsea '12,5 €/m²' → 12.5 en formato float."""
        df["precio_m2"] = df["precio_m2_raw"].apply(self._parse_spanish_decimal)
        df = df.drop(columns=["precio_m2_raw"], errors="ignore")
        return df

    def _parse_variaciones(self, df: pd.DataFrame) -> pd.DataFrame:
        """Parsea columnas de variación: '1,2%' → 1.2, '-' → None."""
        for col in ["variacion_mensual", "variacion_trimestral", "variacion_anual"]:
            raw_col = f"{col}_raw"
            if raw_col in df.columns:
                df[col] = df[raw_col].apply(self._parse_percentage)
                df = df.drop(columns=[raw_col], errors="ignore")
            else:
                df[col] = None
        return df

    def _remove_invalid(self, df: pd.DataFrame) -> pd.DataFrame:
        """Elimina filas sin mes o periodo válido."""
        before = len(df)
        df = df.dropna(subset=["mes", "periodo"])
        df["mes"] = df["mes"].astype(int)
        df["periodo"] = df["periodo"].astype(int)
        removed = before - len(df)
        if removed > 0:
            logger.info(f"  {removed} filas sin mes/periodo válido eliminadas")
        return df

    def _remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Deduplica por (comunidad, mes, periodo), quedándose con el último."""
        before = len(df)
        df = df.drop_duplicates(
            subset=["comunidad", "mes", "periodo"],
            keep="last",
        )
        removed = before - len(df)
        if removed > 0:
            logger.info(f"  {removed} duplicados eliminados")
        return df

    def _validate_ranges(self, df: pd.DataFrame) -> pd.DataFrame:
        """Valida rangos razonables de precio y periodo."""
        before = len(df)

        # Precio m² entre 2 y 60 euros (rango nacional: desde zonas rurales
        # hasta Madrid/País Vasco donde puede superar los 20 €/m²)
        if "precio_m2" in df.columns:
            df.loc[
                (df["precio_m2"].notna()) &
                ((df["precio_m2"] < 2) | (df["precio_m2"] > 60)),
                "precio_m2"
            ] = None

        # Periodo entre 2005 y 2030
        df = df[
            (df["periodo"] >= 2005) & (df["periodo"] <= 2030)
        ]

        # Mes entre 1 y 12
        df = df[
            (df["mes"] >= 1) & (df["mes"] <= 12)
        ]

        removed = before - len(df)
        if removed > 0:
            logger.info(f"  {removed} filas fuera de rango eliminadas")

        return df

    def _select_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Selecciona y ordena las columnas finales."""
        columns = [
            "comunidad", "codigo_ccaa",
            "mes", "periodo", "mes_nombre",
            "precio_m2",
            "variacion_mensual", "variacion_trimestral", "variacion_anual",
            "fecha_extraccion",
        ]
        # Solo incluir columnas que existen
        existing = [c for c in columns if c in df.columns]
        return df[existing].reset_index(drop=True)

    @staticmethod
    def _parse_spanish_decimal(text: Any) -> Optional[float]:
        """
        Parsea un número en formato español a float.
        Maneja: "12,5", "1.234,56", "12,5 €/m²", "-", "n.d."
        """
        if text is None:
            return None

        s = str(text).strip()

        # Valores nulos conocidos
        if s in ("-", "--", "n.d.", "nd", "s.d.", "sd", "", "N/A", "n/a"):
            return None

        # Eliminar símbolos no numéricos (€, /m², espacios, etc.)
        cleaned = re.sub(r"[^\d,.\-]", "", s)

        if not cleaned or cleaned == "-":
            return None

        # Formato español: punto = miles, coma = decimal
        if "," in cleaned and "." in cleaned:
            cleaned = cleaned.replace(".", "").replace(",", ".")
        elif "," in cleaned:
            cleaned = cleaned.replace(",", ".")

        try:
            return float(cleaned)
        except ValueError:
            return None

    @staticmethod
    def _parse_percentage(text: Any) -> Optional[float]:
        """
        Parsea un porcentaje en formato español a float.
        Maneja: "1,2%", "-0,5%", "1.2%", "-", "n.d."
        """
        if text is None:
            return None

        s = str(text).strip()

        if s in ("-", "--", "n.d.", "nd", "s.d.", "sd", "", "N/A", "n/a"):
            return None

        # Eliminar el símbolo de porcentaje y espacios
        cleaned = re.sub(r"[^\d,.\-]", "", s)

        if not cleaned or cleaned == "-":
            return None

        # Coma decimal → punto
        cleaned = cleaned.replace(",", ".")

        try:
            return float(cleaned)
        except ValueError:
            return None
