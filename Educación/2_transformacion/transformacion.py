"""
Etapa 2 · Transformación / normalización · pipeline Educación · Canarias en Datos.

Consolida el consolidado largo de extracción (educacion_raw_long.csv) en las dos
tablas finales del dashboard, siguiendo la convención del resto de áreas
(ced_<tematica>_global / ced_<tematica>_gen):

  · ced_educacion_global : clave (ccaa, periodo) · los 10 indicadores (genero total)
  · ced_educacion_gen    : clave (ccaa, periodo, genero) · los 8 indicadores con
                           desagregación por sexo (genero ∈ total/hombres/mujeres)

Decisiones (Cuaderno §5, §8):
  · Marco territorial = 17 CCAA oficiales (se excluyen España/nacional y las
    ciudades autónomas Ceuta/Melilla, que quedan en el raw).
  · Nombres de salida alineados con el resto del proyecto (join geográfico D3).
  · Ventana activa: periodo >= 2015.
  · Transformación = datos observados (origen='real'); las proyecciones (p. ej.
    gasto_edu_pib 2025-2026 de Presupuestos) se dejan para la etapa de modelado.
  · Formato de salida homólogo: CSV separado por ';', decimal con coma, 'NA'.

Uso:
    python transformacion.py            # genera las tablas
    python transformacion.py --qa       # y ejecuta el análisis QA
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent                  # 2_transformacion
EDUCACION_DIR = BASE_DIR.parent
EXTRACCION_DIR = EDUCACION_DIR / "1_extraccion"
sys.path.insert(0, str(EXTRACCION_DIR))

from config.comunidades import TERRITORIOS, nombre_salida     # noqa: E402
from config.indicadores import INDICADORES                    # noqa: E402
from utils.logger import setup_logger                         # noqa: E402

logger = setup_logger("educacion_transformacion")

RAW_LONG = EXTRACCION_DIR / "data" / "raw" / "educacion_raw_long.csv"
OUT_DIR = BASE_DIR / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

YEAR_START = 2015
GASTO_PIB_MIN_PLAUSIBLE = 1.5   # gasto_edu_pib < 1.5 %PIB = hueco de clasificación (Presupuestos)
CCAA17_IDS = [t["ccaa_id"] for t in TERRITORIOS if t["tipo"] == "ccaa"]

# Orden canónico de indicadores (por bloque, según el cuaderno §4)
ORDEN_IND = [i["key"] for i in INDICADORES]
IND_SEXO = [i["key"] for i in INDICADORES if i["desagrega_sexo"]]      # 8 indicadores
GENEROS = ["total", "hombres", "mujeres"]


def _exportar(df: pd.DataFrame, nombre: str) -> None:
    """Exporta a CSV (;, decimal coma, NA) y XLSX, como el resto de áreas."""
    csv_path = OUT_DIR / f"{nombre}.csv"
    df.to_csv(csv_path, sep=";", decimal=",", na_rep="NA", index=False, encoding="utf-8")
    try:
        df.to_excel(OUT_DIR / f"{nombre}.xlsx", index=False)
    except Exception as e:  # noqa: BLE001
        logger.warning("No se pudo exportar %s.xlsx: %s", nombre, e)
    logger.info("  -> %s (%d filas, %d cols)", csv_path.name, len(df), df.shape[1])


def transformar() -> dict:
    logger.info("=" * 64)
    logger.info("TRANSFORMACIÓN · Educación · desde %s", RAW_LONG.name)
    logger.info("=" * 64)

    df = pd.read_csv(RAW_LONG, dtype={"ccaa_id": str})
    n0 = len(df)

    # ── Limpieza de calidad: gasto_edu_pib implausible (< 1.5 %PIB) ──────────
    # Son huecos de clasificación de la fuente Presupuestos (p. ej. Baleares
    # 2018-2021 ≈ 0,003 %PIB), no ceros reales. Se enmascaran a NA para que no
    # contaminen ni el modelado (denominador MAPE ≈ 0) ni el dashboard.
    implausible = (df["indicador"] == "gasto_edu_pib") & (df["valor"] < GASTO_PIB_MIN_PLAUSIBLE)
    n_mask = int(implausible.sum())
    if n_mask:
        df.loc[implausible, "valor"] = pd.NA
        logger.warning("Enmascaradas %d celdas gasto_edu_pib < %.1f %%PIB (fuente Presupuestos)",
                       n_mask, GASTO_PIB_MIN_PLAUSIBLE)

    # ── Filtros de marco (territorio · origen · ventana) ────────────────────
    df = df[df["ccaa_id"].isin(CCAA17_IDS)]              # 17 CCAA oficiales
    df = df[df["origen"] == "real"]                      # datos observados
    df = df[df["anio"] >= YEAR_START]                    # ventana activa
    logger.info("Filtrado: %d -> %d filas (17 CCAA · real · >=%d)", n0, len(df), YEAR_START)

    # Nombre de salida alineado con el proyecto + renombrado de ejes
    df["ccaa"] = [nombre_salida(cid, nom) for cid, nom in zip(df["ccaa_id"], df["ccaa"])]
    df = df.rename(columns={"anio": "periodo", "sexo": "genero"})

    # ── ced_educacion_gen (8 indicadores × 3 géneros) ───────────────────────
    gen = df[df["indicador"].isin(IND_SEXO)]
    gen_wide = (gen.pivot_table(index=["ccaa", "periodo", "genero"],
                                columns="indicador", values="valor", aggfunc="first")
                   .reset_index())
    gen_wide["origen"] = "real"
    cols_gen = ["ccaa", "periodo", "genero", "origen"] + [c for c in IND_SEXO if c in gen_wide]
    gen_wide = gen_wide[cols_gen].sort_values(["ccaa", "periodo", "genero"])

    # ── ced_educacion_global (10 indicadores, genero total) ─────────────────
    glob = df[df["genero"] == "total"]
    glob_wide = (glob.pivot_table(index=["ccaa", "periodo"],
                                  columns="indicador", values="valor", aggfunc="first")
                     .reset_index())
    glob_wide["origen"] = "real"
    cols_glob = ["ccaa", "periodo", "origen"] + [c for c in ORDEN_IND if c in glob_wide]
    glob_wide = glob_wide[cols_glob].sort_values(["ccaa", "periodo"])

    # ── Consolidado largo, armonizado (analítico / trazable) ────────────────
    long_out = (df[["ccaa", "ccaa_id", "nuts2", "periodo", "genero", "indicador",
                    "valor", "unidad", "origen", "fuente", "url_fuente"]]
                .sort_values(["indicador", "ccaa", "periodo", "genero"]))

    _exportar(glob_wide, "ced_educacion_global")
    _exportar(gen_wide, "ced_educacion_gen")
    long_out.to_csv(OUT_DIR / "ced_educacion_long.csv", sep=";", decimal=",",
                    na_rep="NA", index=False, encoding="utf-8")
    logger.info("  -> ced_educacion_long.csv (%d filas)", len(long_out))

    per = sorted(glob_wide["periodo"].unique())
    logger.info("-" * 64)
    logger.info("Global: %d filas · %d CCAA · %d-%d · %d indicadores",
                len(glob_wide), glob_wide["ccaa"].nunique(), per[0], per[-1],
                len([c for c in ORDEN_IND if c in glob_wide]))
    logger.info("Gen   : %d filas · %d CCAA · géneros %s · %d indicadores",
                len(gen_wide), gen_wide["ccaa"].nunique(),
                sorted(gen_wide["genero"].unique()),
                len([c for c in IND_SEXO if c in gen_wide]))
    return {"global": glob_wide, "gen": gen_wide, "long": long_out}


def main():
    p = argparse.ArgumentParser(description="Transformación · pipeline Educación")
    p.add_argument("--qa", action="store_true", help="Ejecutar el QA tras transformar")
    args = p.parse_args()
    transformar()
    if args.qa:
        logger.info("Lanzando análisis QA de transformación...")
        import qa_transformacion
        qa_transformacion.run()


if __name__ == "__main__":
    main()
