# -*- coding: utf-8 -*-
"""
FASE 2 · SUB-FASE A — LIMPIEZA
Canarias en Datos · Sección Empleo · ODESOCAN

Depura y HOMOGENEÍZA los artefactos de extracción (1_extraccion/salida) sin
consolidar todavía. Cubre las tres tareas pedidas:

  1. Valores perdidos → se CUANTIFICAN y MARCAN (flag_missing); NO se imputan
     (la imputación/proyección es 3_modelado, §7.6). Se documenta su origen
     (submuestras EPA de Ceuta/Melilla, celdas suprimidas por 'Secreto').
  2. Outliers → se detectan con regla robusta (mediana ± K·IQR por grupo) y con
     rangos imposibles por tipo de variable, y se MARCAN (flag_outlier /
     flag_rango); NO se eliminan (los extremos reales son informativos).
  3. Homogeneización de nombres y formatos → territorio canónico, genero
     estandarizado, categorías extraídas con vocabulario controlado (parsers.py)
     y periodo unificado (anyo, trimestre, t_index).

Salida: intermedio/<slug>_limpio.parquet  +  intermedio/reporte_limpieza.csv
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

import config as cfg
import parsers

# tipo de variable por tabla → rango imposible aplicable
TIPO_VARIABLE = {
    "epa_tasa_paro": "tasa", "epa_tasa_actividad": "tasa", "epa_tasa_empleo": "tasa",
    "epa_tiempo_busqueda": "tasa", "epa_tipo_contrato": "mixto", "epa_tipo_jornada": "mixto",
    "etcl_tiempo_trabajo": "horas", "eaes_ganancia_ccaa": "salario",
}
RANGOS = {"tasa": cfg.RANGO_TASA, "horas": cfg.RANGO_HORAS, "salario": cfg.RANGO_SALARIO}
SLUGS_INE = list(TIPO_VARIABLE.keys())
CAT_COLS = ["grupo_edad", "tiempo_busqueda", "tipo_contrato", "tipo_jornada",
            "jornada", "sector", "medida", "estadistico"]


def _homogeneiza_genero(df: pd.DataFrame) -> pd.Series:
    """Género estandarizado: {Ambos géneros, Hombres, Mujeres}; 'Total' si no hay género."""
    s = df["genero"].where(df["genero"].notna(), cfg.GENERO_SIN_DESGLOSE)
    return s.replace({None: cfg.GENERO_SIN_DESGLOSE})


def _flag_outliers(df: pd.DataFrame, grupo_cols: list[str]) -> pd.Series:
    """Regla robusta mediana ± K·IQR dentro de cada grupo (indicador·genero·categoría)."""
    if df.empty:
        return pd.Series([], dtype=bool)
    g = df.groupby(grupo_cols, dropna=False)["valor"]
    q1 = g.transform(lambda x: x.quantile(0.25))
    q3 = g.transform(lambda x: x.quantile(0.75))
    iqr = q3 - q1
    lo = q1 - cfg.OUTLIER_IQR_K * iqr
    hi = q3 + cfg.OUTLIER_IQR_K * iqr
    return (df["valor"] < lo) | (df["valor"] > hi)


def limpia_tabla_ine(slug: str, df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = df[df["anyo"] >= cfg.ANYO_DESDE].copy()

    # --- homogeneización de nombres/formatos ---
    dims = df["serie_nombre"].map(lambda n: parsers.categoria_por_slug(slug, n)).tolist()
    dims_df = pd.DataFrame(dims, index=df.index)
    for c in dims_df.columns:
        df[c] = dims_df[c]
    per = df.apply(lambda r: parsers.homogeneiza_periodo(r["anyo"], r["periodo"], r["periodicidad"]),
                   axis=1).tolist()
    per_df = pd.DataFrame(per, index=df.index)
    for c in ["trimestre", "t_index"]:
        df[c] = per_df[c]
    df["genero"] = _homogeneiza_genero(df)

    # --- valores perdidos (marcar, no imputar) ---
    df["flag_missing"] = df["valor"].isna() | df.get("secreto", False).fillna(False)
    df["flag_submuestra"] = df["territorio"].isin(["Ceuta", "Melilla"])  # EPA: muestra pequeña

    # --- outliers: rango imposible + regla robusta ---
    tipo = TIPO_VARIABLE[slug]
    if tipo in RANGOS:
        lo, hi = RANGOS[tipo]
        df["flag_rango"] = df["valor"].notna() & ((df["valor"] < lo) | (df["valor"] > hi))
    else:  # 'mixto' (abs + %): aplica [0,100] sólo a las filas en porcentaje
        pct = df["unidad"].eq("Porcentaje")
        df["flag_rango"] = pct & df["valor"].notna() & ((df["valor"] < 0) | (df["valor"] > 100))
    # el outlier es una anomalía TEMPORAL dentro de la serie de cada territorio
    # (por eso se incluye 'territorio': evita marcar CCAA grandes por su tamaño)
    grupo = ["territorio", "genero"] + [c for c in CAT_COLS if c in df.columns]
    if "unidad" in df.columns:
        grupo = grupo + ["unidad"]
    df["flag_outlier"] = _flag_outliers(df, grupo)

    reporte = {
        "slug": slug, "filas": len(df),
        "missing": int(df["flag_missing"].sum()),
        "missing_fuera_ceuta_melilla": int((df["flag_missing"] & ~df["flag_submuestra"]).sum()),
        "outliers": int(df["flag_outlier"].sum()),
        "fuera_de_rango": int(df["flag_rango"].sum()),
        "submuestra_cm": int(df["flag_submuestra"].sum()),
        "territorios": df["territorio"].nunique(),
    }
    return df, reporte


def limpia_alquiler(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = df[df["anyo"] >= cfg.ANYO_DESDE].copy()
    df["genero"] = cfg.GENERO_SIN_DESGLOSE
    df["trimestre"] = np.nan
    df["t_index"] = df["anyo"].astype(float)
    df["flag_missing"] = df["precio_m2_medio_anual"].isna()
    df["flag_parcial_anyo"] = df["n_meses"] < 12   # año con <12 meses observados
    df["flag_rango"] = df["precio_m2_medio_anual"].notna() & (df["precio_m2_medio_anual"] <= 0)
    df["flag_outlier"] = _flag_outliers(df.rename(columns={"precio_m2_medio_anual": "valor"}),
                                        ["territorio"])
    reporte = {
        "slug": "alquiler_ccaa_anual", "filas": len(df),
        "missing": int(df["flag_missing"].sum()),
        "anyos_parciales": int(df["flag_parcial_anyo"].sum()),
        "fuera_de_rango": int(df["flag_rango"].sum()),
        "territorios": df["territorio"].nunique(),
    }
    return df, reporte


def ejecutar() -> pd.DataFrame:
    cfg.INTERMEDIO_DIR.mkdir(parents=True, exist_ok=True)
    reportes = []
    print("── FASE A · LIMPIEZA ──")
    for slug in SLUGS_INE:
        df = pd.read_parquet(cfg.EXTRACCION_DIR / f"{slug}.parquet")
        limpio, rep = limpia_tabla_ine(slug, df)
        limpio.to_parquet(cfg.INTERMEDIO_DIR / f"{slug}_limpio.parquet", index=False)
        reportes.append(rep)
        print(f"  {slug:22} filas={rep['filas']:>6} · missing={rep['missing']:>4} "
              f"(fuera C/M={rep['missing_fuera_ceuta_melilla']}) · outliers={rep['outliers']:>4} "
              f"· fuera_rango={rep['fuera_de_rango']}")

    alq = pd.read_parquet(cfg.EXTRACCION_DIR / "alquiler_ccaa_anual.parquet")
    alq_limpio, rep = limpia_alquiler(alq)
    alq_limpio.to_parquet(cfg.INTERMEDIO_DIR / "alquiler_ccaa_anual_limpio.parquet", index=False)
    reportes.append(rep)
    print(f"  {'alquiler_ccaa_anual':22} filas={rep['filas']:>6} · missing={rep['missing']} "
          f"· años_parciales={rep['anyos_parciales']}")

    rep_df = pd.DataFrame(reportes)
    rep_df.to_csv(cfg.INTERMEDIO_DIR / "reporte_limpieza.csv", index=False, encoding="utf-8")
    with (cfg.INTERMEDIO_DIR / "reporte_limpieza.json").open("w", encoding="utf-8") as fh:
        json.dump(reportes, fh, ensure_ascii=False, indent=2)
    print(f"✓ Intermedios y reporte en: {cfg.INTERMEDIO_DIR}")
    return rep_df


if __name__ == "__main__":
    ejecutar()
