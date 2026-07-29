# -*- coding: utf-8 -*-
"""
FASE 3 · MODELADO / PROYECCIÓN
Canarias en Datos · Sección Empleo · ODESOCAN

Proyecta los indicadores del consolidado (2_transformacion/ced_empleo) hasta el
final de 2026 mediante una COMPETICIÓN de algoritmos de series temporales
(AutoARIMA, AutoETS, AutoTheta + líneas base Naive/SeasonalNaive/Drift/…),
evaluados con validación cruzada temporal rolling-origin (1 paso adelante) y
seleccionados POR SERIE minimizando MAPE y MAE, con regla de PARSIMONIA
(ante empate técnico gana el modelo más simple).

Réplica en Python del patrón multi-algoritmo de las demás secciones (modelado.R).

Salidas:
  ced_empleo.csv / .parquet                      → real + proyeccion (bandera origen)
  seleccion_algoritmo_proyeccion_global.csv      → ranking de algoritmos
  seleccion_algoritmo_proyeccion_variables.csv   → error por indicador·algoritmo
  seleccion_algoritmo_proyeccion_series.csv      → modelo elegido por serie
  manifiesto_modelado.json
"""
from __future__ import annotations

import json
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

from statsforecast import StatsForecast
from statsforecast.models import (AutoARIMA, AutoETS, AutoTheta, HistoricAverage,
                                  Naive, RandomWalkWithDrift, SeasonalNaive, WindowAverage)

import config as cfg
import seleccion as sel

MODELOS_COLS = list(cfg.ALGORITMOS.keys())
CACHE_DIR = cfg.BASE_DIR / ".cache_cv"


def _modelos(season_length: int):
    win = min(season_length * 2, 8) if season_length > 1 else 3
    return [
        AutoARIMA(season_length=season_length),
        AutoETS(season_length=season_length),
        AutoTheta(season_length=season_length),
        SeasonalNaive(season_length=season_length),
        RandomWalkWithDrift(),
        WindowAverage(window_size=win),
        Naive(),
        HistoricAverage(),
    ]


def _ds(anyo, trimestre):
    mes = int((trimestre - 1) * 3 + 1) if pd.notna(trimestre) else 1
    return pd.Timestamp(year=int(anyo), month=mes, day=1)


def _desde_ds(ds, periodicidad):
    ds = pd.Timestamp(ds)
    if periodicidad == "trimestral":
        trim = (ds.month - 1) // 3 + 1
        return {"anyo": ds.year, "trimestre": trim, "periodo": f"{ds.year}T{trim}",
                "t_index": ds.year + (trim - 1) / 4}
    return {"anyo": ds.year, "trimestre": np.nan, "periodo": str(ds.year),
            "t_index": float(ds.year)}


def _prepara(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Construye el frame de statsforecast (unique_id, ds, y) + una tabla meta."""
    df = df.copy()
    df["unique_id"] = (df["indicador_id"].astype(str) + "|" + df["territorio"]
                       + "|" + df["genero"])
    df["ds"] = [_ds(a, t) for a, t in zip(df["anyo"], df["trimestre"])]
    sf_df = df[["unique_id", "ds", "valor"]].rename(columns={"valor": "y"}).dropna(subset=["y"])
    sf_df = sf_df.sort_values(["unique_id", "ds"]).reset_index(drop=True)
    meta = (df.sort_values("ds").groupby("unique_id")
            .agg(indicador_id=("indicador_id", "first"), indicador=("indicador", "first"),
                 unidad=("unidad", "first"), territorio_cod=("territorio_cod", "first"),
                 territorio=("territorio", "first"), genero=("genero", "first"),
                 fuente=("fuente", "first"), periodicidad=("periodicidad", "first"))
            .reset_index())
    return sf_df, meta


def _cv_largo(cv: pd.DataFrame) -> pd.DataFrame:
    presentes = [m for m in MODELOS_COLS if m in cv.columns]
    largo = cv.melt(id_vars=["unique_id", "ds", "y"], value_vars=presentes,
                    var_name="modelo", value_name="yhat")
    return largo


def _cv_y_forecast(sf_df, season_length, cv_folds, freq, h, tag, recompute):
    """Ejecuta (o recupera de caché) la CV y el forecast — la parte cara."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cv_path = CACHE_DIR / f"cv_{tag}.parquet"
    fc_path = CACHE_DIR / f"fc_{tag}.parquet"
    if not recompute and cv_path.exists() and (h <= 0 or fc_path.exists()):
        cv = pd.read_parquet(cv_path)
        fc = pd.read_parquet(fc_path) if (h > 0 and fc_path.exists()) else pd.DataFrame()
    else:
        sf = StatsForecast(models=_modelos(season_length), freq=freq, n_jobs=1)
        cv = sf.cross_validation(df=sf_df, h=1, step_size=1, n_windows=cv_folds)
        cv.to_parquet(cv_path, index=False)
        fc = pd.DataFrame()
        if h > 0:
            fc = sf.forecast(df=sf_df, h=h)
            fc.to_parquet(fc_path, index=False)
    if cfg.INCLUIR_PROPHET:
        cv, fc = _merge_prophet(sf_df, cv, fc, freq, h, tag, recompute)
    return cv, fc


def _merge_prophet(sf_df, cv, fc, freq, h, tag, recompute):
    """Añade la columna 'Prophet' a la CV y al forecast (cacheada aparte)."""
    import prophet_model as pm
    pcv_path = CACHE_DIR / f"prophet_cv_{tag}.parquet"
    pfc_path = CACHE_DIR / f"prophet_fc_{tag}.parquet"
    estacional = (freq == "QS")  # la estacionalidad anual sólo es estimable con datos infra-anuales
    if not recompute and pcv_path.exists() and (h <= 0 or pfc_path.exists()):
        pcv = pd.read_parquet(pcv_path)
        pfc = pd.read_parquet(pfc_path) if (h > 0 and pfc_path.exists()) else pd.DataFrame()
    else:
        print(f"    · Prophet [{tag}]: ajustando por serie·fold (lento, se cachea)…", flush=True)
        pcv = pm.prophet_cv(sf_df, cv, freq, estacional)
        pcv.to_parquet(pcv_path, index=False)
        pfc = pm.prophet_forecast(sf_df, h, freq, estacional) if h > 0 else pd.DataFrame()
        if h > 0:
            pfc.to_parquet(pfc_path, index=False)
    cv = cv.drop(columns=[c for c in ["Prophet"] if c in cv.columns])
    cv = cv.merge(pcv, on=["unique_id", "ds"], how="left")
    if h > 0 and not fc.empty and not pfc.empty:
        fc = fc.drop(columns=[c for c in ["Prophet"] if c in fc.columns])
        fc = fc.merge(pfc, on=["unique_id", "ds"], how="left")
    return cv, fc


def _procesa_grupo(sf_df, meta, season_length, cv_folds, min_puntos, freq, h, tag, recompute):
    """CV + selección + forecast para un grupo de frecuencia homogénea."""
    # sólo series con longitud suficiente para CV
    n = sf_df.groupby("unique_id")["y"].size()
    validas = n[n >= min_puntos + cv_folds].index
    sf_df = sf_df[sf_df["unique_id"].isin(validas)].reset_index(drop=True)
    if sf_df.empty:
        return None

    cv, fc = _cv_y_forecast(sf_df, season_length, cv_folds, freq, h, tag, recompute)
    met = sel.metricas_cv(_cv_largo(cv))
    sel_series = sel.seleccion_por_serie(met)
    return {"met": met, "sel_series": sel_series, "forecast": fc, "meta": meta,
            "sf_df": sf_df, "h": h}


def _construye_proyecciones(res, meta) -> pd.DataFrame:
    """Genera las filas de proyección (origen='proyeccion') con el modelo elegido por serie."""
    fc, sel_series = res["forecast"], res["sel_series"]
    if fc is None or fc.empty:
        return pd.DataFrame()
    elegido = sel_series.set_index("unique_id")["modelo"].to_dict()
    info = sel_series.set_index("unique_id")[["mape", "mae", "aplicó_parsimonia"]].to_dict("index")
    meta_i = meta.set_index("unique_id")

    filas = []
    for _, r in fc.iterrows():
        uid = r["unique_id"]
        modelo = elegido.get(uid)
        if uid not in meta_i.index:
            continue
        m = meta_i.loc[uid]
        valor = r[modelo] if (modelo and modelo in r.index) else np.nan
        per = _desde_ds(r["ds"], m["periodicidad"])
        filas.append({
            "indicador_id": m["indicador_id"], "indicador": m["indicador"], "unidad": m["unidad"],
            "territorio_cod": m["territorio_cod"], "territorio": m["territorio"], "genero": m["genero"],
            **per, "periodicidad": m["periodicidad"], "valor": round(float(valor), 3) if pd.notna(valor) else np.nan,
            "origen": "proyeccion", "fuente": m["fuente"], "flag_missing": pd.isna(valor),
            "flag_outlier": False, "algoritmo": modelo,
            "modelo_mape": info.get(uid, {}).get("mape"), "modelo_mae": info.get(uid, {}).get("mae"),
            "aplico_parsimonia": info.get(uid, {}).get("aplicó_parsimonia", False),
        })
    return pd.DataFrame(filas)


def ejecutar(recompute: bool = False) -> dict:
    cfg.SALIDA_DIR.mkdir(parents=True, exist_ok=True)
    print("── FASE 3 · MODELADO ──")
    ced = pd.read_parquet(cfg.CONSOLIDADO)

    resultados, metricas_all, sel_all, proyecciones = [], [], [], []
    for periodicidad, season, folds, minp, freq in [
        ("trimestral", 4, cfg.CV_FOLDS_TRIMESTRAL, cfg.MIN_PUNTOS_TRIMESTRAL, "QS"),
        ("anual", 1, cfg.CV_FOLDS_ANUAL, cfg.MIN_PUNTOS_ANUAL, "YS"),
    ]:
        sub = ced[ced["periodicidad"] == periodicidad]
        if sub.empty:
            continue
        sf_df, meta = _prepara(sub)
        max_ds = sf_df["ds"].max()
        if periodicidad == "trimestral":
            h = (cfg.HORIZONTE_ANYO * 4 + 4) - (max_ds.year * 4 + ((max_ds.month - 1) // 3 + 1))
        else:
            h = cfg.HORIZONTE_ANYO - max_ds.year
        print(f"  [{periodicidad}] series={sf_df['unique_id'].nunique()} · "
              f"último={max_ds.date()} · horizonte h={h}")
        res = _procesa_grupo(sf_df, meta, season, folds, minp, freq, max(h, 0),
                             tag=periodicidad, recompute=recompute)
        if res is None:
            continue
        res["periodicidad"] = periodicidad
        resultados.append(res)
        metricas_all.append(res["met"].merge(meta[["unique_id", "indicador_id", "indicador"]],
                                              on="unique_id", how="left"))
        sel_all.append(res["sel_series"].assign(periodicidad=periodicidad))
        proyecciones.append(_construye_proyecciones(res, meta))

    met_total = pd.concat(metricas_all, ignore_index=True)
    sel_total = pd.concat(sel_all, ignore_index=True)
    proy = pd.concat([p for p in proyecciones if not p.empty], ignore_index=True) \
        if any(not p.empty for p in proyecciones) else pd.DataFrame()

    # selección global (convención del proyecto)
    meta_join = met_total[["unique_id", "indicador_id", "indicador"]].drop_duplicates()
    glob, por_ind = sel.seleccion_global(met_total.drop(columns=["indicador_id", "indicador"]),
                                         sel_total, meta_join)

    # --- ensamblar dataset real + proyeccion (bandera origen) ---
    ced_real = ced.copy()
    ced_real["algoritmo"] = pd.NA
    ced_real["modelo_mape"] = np.nan
    ced_real["modelo_mae"] = np.nan
    ced_real["aplico_parsimonia"] = False
    # anota el modelo elegido también en las filas reales de cada serie
    uid_real = (ced_real["indicador_id"].astype(str) + "|" + ced_real["territorio"]
                + "|" + ced_real["genero"])
    modelo_por_uid = sel_total.set_index("unique_id")["modelo"].to_dict()
    ced_real["algoritmo"] = uid_real.map(modelo_por_uid)
    cols = list(ced_real.columns)
    final = pd.concat([ced_real, proy.reindex(columns=cols)], ignore_index=True) \
        if not proy.empty else ced_real
    final = final.sort_values(["indicador_id", "territorio", "genero", "anyo", "trimestre"]).reset_index(drop=True)

    # --- escritura ---
    final.to_csv(cfg.SALIDA_DIR / "ced_empleo.csv", index=False, encoding="utf-8")
    final.to_parquet(cfg.SALIDA_DIR / "ced_empleo.parquet", index=False)
    glob.to_csv(cfg.SALIDA_DIR / "seleccion_algoritmo_proyeccion_global.csv", index=False, encoding="utf-8")
    por_ind.to_csv(cfg.SALIDA_DIR / "seleccion_algoritmo_proyeccion_variables.csv", index=False, encoding="utf-8")
    sel_total.to_csv(cfg.SALIDA_DIR / "seleccion_algoritmo_proyeccion_series.csv", index=False, encoding="utf-8")

    man = {
        "seccion": "Empleo", "fase": "3_modelado", "horizonte_anyo": cfg.HORIZONTE_ANYO,
        "n_series": int(sel_total["unique_id"].nunique()),
        "filas_reales": int((final["origen"] == "real").sum()),
        "filas_proyeccion": int((final["origen"] == "proyeccion").sum()),
        "algoritmo_global_ref": glob.iloc[0]["modelo"],
        "reparto_modelos_ganadores": sel_total["modelo"].value_counts().to_dict(),
        "series_con_parsimonia": int(sel_total["aplicó_parsimonia"].sum()),
        "cv_folds": {"trimestral": cfg.CV_FOLDS_TRIMESTRAL, "anual": cfg.CV_FOLDS_ANUAL},
    }
    with (cfg.SALIDA_DIR / "manifiesto_modelado.json").open("w", encoding="utf-8") as fh:
        json.dump(man, fh, ensure_ascii=False, indent=2, default=str)

    print(f"\n  Reparto de modelos ganadores: {man['reparto_modelos_ganadores']}")
    print(f"  Series donde ganó la parsimonia: {man['series_con_parsimonia']}/{man['n_series']}")
    print(f"  Algoritmo global de referencia (menor NMAE medio): {man['algoritmo_global_ref']}")
    print(f"  Filas: {man['filas_reales']} reales + {man['filas_proyeccion']} proyección")
    print(f"✓ Salida en: {cfg.SALIDA_DIR}")
    return {"final": final, "global": glob, "series": sel_total, "manifiesto": man}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Modelado / proyección — Empleo")
    ap.add_argument("--recompute", action="store_true",
                    help="Recalcula la CV y el forecast ignorando la caché")
    ejecutar(recompute=ap.parse_args().recompute)
