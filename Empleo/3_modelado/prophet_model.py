# -*- coding: utf-8 -*-
"""
Integración de Prophet (Meta) en la competición de la fase 3 — Empleo.

Prophet no forma parte de statsforecast, así que se ejecuta aparte pero con la
MISMA validación cruzada rolling-origin (usa los mismos 'cutoff' que produjo
statsforecast) y el mismo horizonte, de modo que compite en igualdad con
AutoARIMA/AutoETS/… Devuelve una columna 'Prophet' que se fusiona en los frames
de CV y de forecast.

Prophet es lento (un ajuste por serie·fold); los resultados se cachean.
"""
from __future__ import annotations

import contextlib
import io
import logging
import os

import pandas as pd

logging.getLogger("prophet").setLevel(logging.CRITICAL)
logging.getLogger("cmdstanpy").setLevel(logging.CRITICAL)


@contextlib.contextmanager
def _silencio():
    """Silencia el ruido de cmdstanpy/Stan durante el ajuste."""
    with open(os.devnull, "w") as dn, contextlib.redirect_stdout(dn), \
            contextlib.redirect_stderr(dn):
        yield


def _fit_predict(train: pd.DataFrame, h: int, freq: str, estacional: bool) -> list[float]:
    """Ajusta Prophet sobre train[ds,y] y devuelve las h predicciones futuras."""
    from prophet import Prophet
    if len(train) < 4:
        return [float("nan")] * h
    try:
        with _silencio():
            m = Prophet(
                yearly_seasonality=estacional,   # sólo tiene sentido con datos infra-anuales
                weekly_seasonality=False, daily_seasonality=False,
                n_changepoints=max(0, min(25, len(train) - 2)),
            )
            m.fit(train[["ds", "y"]])
            fut = m.make_future_dataframe(periods=h, freq=freq)
            pred = m.predict(fut)
        return pred["yhat"].tail(h).astype(float).tolist()
    except Exception:
        return [float("nan")] * h


def prophet_cv(sf_df: pd.DataFrame, cv_ref: pd.DataFrame, freq: str, estacional: bool) -> pd.DataFrame:
    """Replica la CV rolling-origin (1 paso) de statsforecast para Prophet.

    cv_ref: el dataframe de cross_validation de statsforecast (aporta los 'cutoff'
    y los 'ds' objetivo por serie). Devuelve [unique_id, ds, Prophet].
    """
    ref = cv_ref[["unique_id", "ds", "cutoff"]].drop_duplicates()
    filas = []
    for uid, g in sf_df.groupby("unique_id"):
        g = g.sort_values("ds")
        sub = ref[ref["unique_id"] == uid]
        for _, r in sub.iterrows():
            train = g[g["ds"] <= r["cutoff"]]
            yhat = _fit_predict(train, 1, freq, estacional)[0]
            filas.append({"unique_id": uid, "ds": r["ds"], "Prophet": yhat})
    return pd.DataFrame(filas)


def prophet_forecast(sf_df: pd.DataFrame, h: int, freq: str, estacional: bool) -> pd.DataFrame:
    """Ajusta Prophet sobre la serie completa y proyecta h pasos. → [unique_id, ds, Prophet]."""
    filas = []
    for uid, g in sf_df.groupby("unique_id"):
        g = g.sort_values("ds")
        preds = _fit_predict(g, h, freq, estacional)
        last = g["ds"].max()
        fechas = pd.date_range(last, periods=h + 1, freq=freq)[1:]
        for ds, yhat in zip(fechas, preds):
            filas.append({"unique_id": uid, "ds": ds, "Prophet": yhat})
    return pd.DataFrame(filas)
