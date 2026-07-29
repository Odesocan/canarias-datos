"""
Extractor del indicador de esfuerzo público: gasto/presupuesto en educación
sobre el PIB regional.

No se recalcula: se toma del output ya armonizado del área de Presupuestos
(uno de sus 13 conceptos de política social), filtrando concepto == 'educacion'.
Ver Cuaderno_metodologico_educacion.docx §8.5.
"""

from datetime import datetime
from typing import Dict, List

import pandas as pd

from config.settings import PRESUPUESTOS_OUTPUTS
from config.comunidades import por_nombre
from config.indicadores import por_key
from utils.logger import setup_logger

logger = setup_logger()


def _ultimo_archivo() -> "pd.Path":
    """Localiza el CSV largo más reciente presupuestos_pib_integrado_*_long.csv."""
    candidatos = sorted(PRESUPUESTOS_OUTPUTS.glob("presupuestos_pib_integrado_*_long.csv"))
    if not candidatos:
        raise FileNotFoundError(
            f"No se encontró presupuestos_pib_integrado_*_long.csv en {PRESUPUESTOS_OUTPUTS}"
        )
    return candidatos[-1]


def extraer_gasto_pib() -> List[Dict]:
    ind = por_key("gasto_edu_pib")
    ahora = datetime.now().isoformat(timespec="seconds")

    archivo = _ultimo_archivo()
    logger.info("Presupuestos: leyendo %s", archivo.name)
    df = pd.read_csv(archivo)
    edu = df[df["concepto"] == "educacion"].copy()
    logger.info("  concepto=educacion: %d filas (%d CCAA, %s-%s)",
                len(edu), edu["ccaa"].nunique(),
                edu["anio"].min(), edu["anio"].max())

    salida, sin_map = [], set()
    for _, row in edu.iterrows():
        terr = por_nombre(str(row["ccaa"]))
        if terr is None:
            sin_map.add(row["ccaa"])
            continue
        salida.append({
            "indicador": ind["key"],
            "bloque": ind["bloque"],
            "fuente": f"Presupuestos · {archivo.name}",
            "dataset": ind["dataset"],
            "ccaa": terr["nombre"],
            "ccaa_id": terr["ccaa_id"],
            "nuts2": terr["nuts2"],
            "anio": int(row["anio"]),
            "sexo": "total",
            "valor": round(float(row["pct_pib_regional"]), 4),
            "unidad": ind["unidad"],
            # respeta la bandera de origen del área de Presupuestos
            "origen": str(row.get("origen_pib", "real")),
            "extraido_en": ahora,
            "url_fuente": str(archivo),
        })
    if sin_map:
        logger.warning("  CCAA sin mapear en Presupuestos: %s", sorted(sin_map))
    logger.info("  gasto_edu_pib: %d filas normalizadas", len(salida))
    return salida
