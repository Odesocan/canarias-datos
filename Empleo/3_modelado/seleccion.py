# -*- coding: utf-8 -*-
"""
Métricas de error y selección de modelo (con parsimonia) — fase 3 · Empleo.

A partir de las predicciones de validación cruzada (una fila por serie·fold·
modelo con observado y predicho) calcula MAE, MAPE, RMSE y NMAE por (serie,
modelo) y elige, POR SERIE, el modelo que minimiza el error aplicando la regla
de parsimonia: si varios modelos empatan (dentro de la tolerancia), gana el más
simple.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import config as cfg


# --------------------------------------------------------------------------- #
# Métricas por (serie, modelo)
# --------------------------------------------------------------------------- #
def metricas_cv(cv_long: pd.DataFrame) -> pd.DataFrame:
    """cv_long: columnas [unique_id, modelo, y, yhat]. Devuelve métricas por serie·modelo."""
    df = cv_long.dropna(subset=["y", "yhat"]).copy()
    df["ae"] = (df["y"] - df["yhat"]).abs()
    df["se"] = (df["y"] - df["yhat"]) ** 2
    # MAPE robusto: excluye puntos con |y| ≈ 0
    mask = df["y"].abs() > cfg.MAPE_EPS
    df["ape"] = np.where(mask, (df["y"] - df["yhat"]).abs() / df["y"].abs() * 100, np.nan)

    g = df.groupby(["unique_id", "modelo"])
    met = g.agg(
        n_folds=("ae", "size"),
        mae=("ae", "mean"),
        rmse=("se", lambda s: float(np.sqrt(np.mean(s)))),
        mape=("ape", "mean"),
        escala=("y", lambda s: float(np.mean(np.abs(s)))),
    ).reset_index()
    met["nmae"] = np.where(met["escala"] > 0, met["mae"] / met["escala"], np.nan)
    met["complejidad"] = met["modelo"].map(lambda m: cfg.ALGORITMOS.get(m, {}).get("complejidad", 99))
    return met


# --------------------------------------------------------------------------- #
# Selección por serie con parsimonia
# --------------------------------------------------------------------------- #
def _elige_por_serie(sub: pd.DataFrame) -> pd.Series:
    """sub: métricas de todos los modelos de UNA serie. Devuelve la fila elegida.

    Precisión primaria = MAPE (o NMAE si el MAPE no es evaluable). Se define el
    conjunto "equivalente al mejor" como los modelos dentro de la tolerancia en la
    métrica primaria — esto SIEMPRE incluye al mejor, nunca queda vacío. Entre los
    equivalentes gana el más simple (parsimonia); se desempata por MAE y métrica.
    """
    val = sub.dropna(subset=["mae"]).copy()
    if val.empty:
        return pd.Series({"modelo": None, "aplicó_parsimonia": False, "metrica_seleccion": "ninguna"})
    # criterio de precisión primario = MAPE; si no hay MAPE válido en la serie, NMAE
    metrica = "mape" if val["mape"].notna().any() else "nmae"
    cand = val.dropna(subset=[metrica])
    if cand.empty:                      # ni MAPE ni NMAE → usa MAE
        metrica, cand = "mae", val
    mejor = cand.loc[cand[metrica].idxmin()]

    # equivalentes = dentro de la tolerancia en la métrica primaria (incluye al mejor)
    tol = 1 + cfg.PARSIMONIA_TOL_REL
    equiv = cand[cand[metrica] <= mejor[metrica] * tol]
    # entre los equivalentes → el más simple; desempate por MAE y luego métrica
    elegido = equiv.sort_values(["complejidad", "mae", metrica]).iloc[0]

    return pd.Series({
        "modelo": elegido["modelo"],
        "mape": elegido["mape"], "mae": elegido["mae"],
        "rmse": elegido["rmse"], "nmae": elegido["nmae"],
        "modelo_mas_preciso": mejor["modelo"],
        "aplicó_parsimonia": bool(elegido["modelo"] != mejor["modelo"]),
        "metrica_seleccion": metrica,
    })


def seleccion_por_serie(met: pd.DataFrame) -> pd.DataFrame:
    """Para cada unique_id elige el modelo (más preciso / más parsimonioso)."""
    filas = []
    for uid, sub in met.groupby("unique_id"):
        r = _elige_por_serie(sub)
        r["unique_id"] = uid
        filas.append(r)
    return pd.DataFrame(filas)


# --------------------------------------------------------------------------- #
# Selección global (convención del proyecto: un algoritmo de referencia)
# --------------------------------------------------------------------------- #
def seleccion_global(met: pd.DataFrame, sel_series: pd.DataFrame,
                     meta: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Devuelve (tabla_global, tabla_por_indicador) al estilo
    seleccion_algoritmo_proyeccion_{global,variables}.csv del proyecto."""
    # unir el indicador de cada serie
    m = met.merge(meta[["unique_id", "indicador_id", "indicador"]], on="unique_id", how="left")

    por_indicador = (m.groupby(["indicador_id", "indicador", "modelo"])
                     .agg(n_series=("unique_id", "nunique"),
                          mae_medio=("mae", "mean"),
                          mape_medio=("mape", "mean"),
                          nmae_medio=("nmae", "mean"))
                     .reset_index()
                     .sort_values(["indicador_id", "nmae_medio"]))

    n_series_total = m["unique_id"].nunique()
    ganadas = sel_series["modelo"].value_counts().rename("n_series_ganadas")
    glob = (m.groupby("modelo")
            .agg(series_evaluadas=("unique_id", "nunique"),
                 mae_medio=("mae", "mean"),
                 mape_medio=("mape", "mean"),
                 nmae_medio=("nmae", "mean"))
            .reset_index())
    glob = glob.merge(ganadas, left_on="modelo", right_index=True, how="left")
    glob["n_series_ganadas"] = glob["n_series_ganadas"].fillna(0).astype(int)
    glob["cobertura"] = glob["series_evaluadas"] / n_series_total
    glob["error_global"] = glob["nmae_medio"]
    glob["complejidad"] = glob["modelo"].map(lambda x: cfg.ALGORITMOS.get(x, {}).get("complejidad", 99))
    glob = glob.sort_values("error_global").reset_index(drop=True)
    return glob, por_indicador
