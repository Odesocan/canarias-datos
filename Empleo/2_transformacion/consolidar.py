# -*- coding: utf-8 -*-
"""
FASE 2 · SUB-FASE B (2/2) — CONSOLIDACIÓN / JOIN
Canarias en Datos · Sección Empleo · ODESOCAN

Une todos los indicadores en un dataset longitudinal único (§8: ced_empleo).
Produce dos representaciones del MISMO contenido:

  · ced_empleo.csv            → LARGO/tidy, frecuencia nativa (trimestral EPA/ETCL,
                                anual EAES/alquiler). Fuente de verdad, sin pérdida
                                de información: 1 fila por observación, la columna
                                `indicador` contiene todas las variables.
  · ced_empleo_anual_ancho.csv→ ANCHO anual (1 fila por territorio·genero·año, 1
                                columna por indicador). Cómodo para Power BI y para
                                comparar CCAA (§7.1 "agregados anuales homogéneos").

Por qué el LARGO es el canónico: los indicadores tienen frecuencias y
desagregaciones distintas (unos por genero, otros no; unos trimestrales, otros
anuales). Forzar todo a una sola matriz ancha nativa generaría celdas vacías;
el largo lo evita y el ancho anual se deriva de él sin ambigüedad.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

import config as cfg
import indicadores as ind

# nombre corto de cada indicador para las columnas del formato ancho
SLUG_INDICADOR = {
    1: "tasa_paro", 2: "tasa_actividad", 3: "tasa_empleo", 4: "horas_servicios",
    6: "tasa_paro_juvenil", 7: "paro_larga_duracion", 8: "temporalidad",
    9: "parcialidad", 10: "brecha_salarial", 11: "pct_alquiler_salario",
}
# indicadores territoriales (sin desglose de género) → en el ancho van en 'Ambos géneros'
IND_SIN_GENERO = {4, 10}


def _anualiza(long_df: pd.DataFrame) -> pd.DataFrame:
    """Media anual de los indicadores trimestrales; los anuales se mantienen."""
    trimestral = long_df[long_df["periodicidad"] == "trimestral"].copy()
    anual = long_df[long_df["periodicidad"] != "trimestral"].copy()

    agg = (trimestral.groupby(["indicador_id", "indicador", "unidad", "territorio_cod",
                               "territorio", "genero", "anyo"], dropna=False)
           .agg(valor=("valor", "mean"),
                n_trim=("valor", "count"),
                flag_outlier=("flag_outlier", "any"),
                flag_missing=("flag_missing", "any"))
           .reset_index())
    agg["periodicidad"] = "anual (media de trimestres)"
    anual["n_trim"] = np.nan
    cols = ["indicador_id", "indicador", "unidad", "territorio_cod", "territorio",
            "genero", "anyo", "valor", "n_trim", "periodicidad", "flag_outlier", "flag_missing"]
    return pd.concat([agg[cols], anual.reindex(columns=cols)], ignore_index=True)


def _ancho_anual(anual_long: pd.DataFrame) -> pd.DataFrame:
    d = anual_long.copy()
    # los indicadores sin genero (horas, brecha) se colocan en la fila 'Ambos géneros'
    d.loc[d["indicador_id"].isin(IND_SIN_GENERO), "genero"] = cfg.GENERO_AMBOS
    d["col"] = d["indicador_id"].map(SLUG_INDICADOR)
    ancho = d.pivot_table(index=["territorio_cod", "territorio", "genero", "anyo"],
                          columns="col", values="valor", aggfunc="first").reset_index()
    # ordenar columnas de indicadores por nº de indicador
    orden = [SLUG_INDICADOR[k] for k in sorted(SLUG_INDICADOR) if SLUG_INDICADOR[k] in ancho.columns]
    ancho = ancho[["territorio_cod", "territorio", "genero", "anyo"] + orden]
    return ancho.sort_values(["territorio", "genero", "anyo"]).reset_index(drop=True)


def ejecutar() -> dict:
    cfg.SALIDA_DIR.mkdir(parents=True, exist_ok=True)
    print("── FASE B · CONSOLIDACIÓN (join) ──")

    long_df = ind.calcular_todos()
    long_df = long_df.sort_values(["indicador_id", "territorio", "genero", "anyo", "trimestre"]) \
                     .reset_index(drop=True)
    long_df.to_csv(cfg.SALIDA_DIR / "ced_empleo.csv", index=False, encoding="utf-8")
    long_df.to_parquet(cfg.SALIDA_DIR / "ced_empleo.parquet", index=False)

    anual_long = _anualiza(long_df)
    ancho = _ancho_anual(anual_long)
    ancho.to_csv(cfg.SALIDA_DIR / "ced_empleo_anual_ancho.csv", index=False, encoding="utf-8")
    ancho.to_parquet(cfg.SALIDA_DIR / "ced_empleo_anual_ancho.parquet", index=False)

    # manifiesto
    man = {
        "seccion": "Empleo", "fase": "2_transformacion",
        "filas_largo": len(long_df),
        "indicadores": sorted(long_df["indicador_id"].unique().tolist()),
        "n_indicadores": long_df["indicador_id"].nunique(),
        "territorios": sorted(long_df["territorio"].dropna().unique().tolist()),
        "anyo_min": int(long_df["anyo"].min()), "anyo_max": int(long_df["anyo"].max()),
        "filas_ancho_anual": len(ancho),
        "indicador_5_afiliacion": "PENDIENTE (ficheros Seguridad Social no cargados)",
        "supuesto_indicador_11": {
            "superficie_ref_m2": cfg.SUPERFICIE_REF_M2, "pagas_anyo": cfg.PAGAS_ANYO,
            "formula": "(precio_m2 * m2_ref) / (ganancia_media_anual / pagas) * 100",
        },
    }
    with (cfg.SALIDA_DIR / "manifiesto_transformacion.json").open("w", encoding="utf-8") as fh:
        json.dump(man, fh, ensure_ascii=False, indent=2)

    print(f"  ced_empleo.csv (largo):        {len(long_df):>6} filas · "
          f"{long_df['indicador_id'].nunique()} indicadores · {man['anyo_min']}–{man['anyo_max']}")
    print(f"  ced_empleo_anual_ancho.csv:    {len(ancho):>6} filas · "
          f"{len([c for c in ancho.columns if c in SLUG_INDICADOR.values()])} columnas-indicador")
    print(f"✓ Salida en: {cfg.SALIDA_DIR}")
    return {"long": long_df, "ancho": ancho, "manifiesto": man}


if __name__ == "__main__":
    ejecutar()
