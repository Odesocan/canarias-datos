"""
Validación de calidad de los datos transformados.
Genera informes de cobertura, completitud y rangos.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import pandas as pd

from config.settings import PROCESSED_DIR
from utils.logger import setup_logger

logger = setup_logger("validator")


class HistoricoValidator:
    """
    Valida la calidad de los datos históricos transformados.

    Checks:
    - Cobertura: cuántas comunidades tienen datos
    - Completitud: % de valores no nulos por campo
    - Rangos: precio_m2, periodos, variaciones
    - Profundidad temporal: rango de años cubierto
    """

    def validate(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Ejecuta todas las validaciones y genera informe.

        Returns:
            Diccionario con resultados de validación.
        """
        if df.empty:
            logger.warning("DataFrame vacío — no hay datos para validar")
            return {"status": "empty", "registros": 0}

        report = {
            "timestamp": datetime.now().isoformat(),
            "registros_totales": len(df),
            "cobertura": self._check_cobertura(df),
            "completitud": self._check_completitud(df),
            "rangos": self._check_rangos(df),
            "temporal": self._check_temporal(df),
        }

        # Resumen
        n_comunidades = report["cobertura"]["comunidades_con_datos"]
        report["status"] = "ok" if n_comunidades >= 5 else "warning"

        logger.info(
            f"Validación: {len(df)} registros | "
            f"{n_comunidades} comunidades | "
            f"status={report['status']}"
        )

        # Guardar informe
        self._save_report(report)

        return report

    def _check_cobertura(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analiza cobertura por comunidad autónoma."""
        comunidades = df["comunidad"].nunique()

        por_comunidad = (
            df.groupby("comunidad")
            .size()
            .sort_values(ascending=False)
            .to_dict()
        )

        return {
            "comunidades_con_datos": comunidades,
            "registros_por_comunidad": por_comunidad,
        }

    def _check_completitud(self, df: pd.DataFrame) -> Dict[str, float]:
        """Calcula % de valores no nulos por campo."""
        total = len(df)
        completitud = {}
        for col in df.columns:
            non_null = df[col].notna().sum()
            completitud[col] = round(non_null / total * 100, 1)
        return completitud

    def _check_rangos(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Verifica rangos de valores numéricos."""
        rangos = {}

        if "precio_m2" in df.columns:
            precio = df["precio_m2"].dropna()
            if not precio.empty:
                rangos["precio_m2"] = {
                    "min": round(float(precio.min()), 2),
                    "max": round(float(precio.max()), 2),
                    "media": round(float(precio.mean()), 2),
                    "mediana": round(float(precio.median()), 2),
                }

        for col in ["variacion_mensual", "variacion_trimestral", "variacion_anual"]:
            if col in df.columns:
                vals = df[col].dropna()
                if not vals.empty:
                    rangos[col] = {
                        "min": round(float(vals.min()), 2),
                        "max": round(float(vals.max()), 2),
                        "media": round(float(vals.mean()), 2),
                    }

        return rangos

    def _check_temporal(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analiza cobertura temporal."""
        if "periodo" not in df.columns:
            return {}

        return {
            "anio_min": int(df["periodo"].min()),
            "anio_max": int(df["periodo"].max()),
            "anios_cubiertos": int(df["periodo"].nunique()),
            "registros_por_anio": (
                df.groupby("periodo")
                .size()
                .sort_index()
                .to_dict()
            ),
        }

    def _save_report(self, report: Dict[str, Any]) -> None:
        """Guarda el informe de validación en JSON."""
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = PROCESSED_DIR / f"quality_report_{timestamp}.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)

        logger.info(f"Informe de calidad: {path}")
