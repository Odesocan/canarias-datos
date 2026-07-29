"""
Familia de algoritmos de proyección para el pipeline Educación.

Interfaz uniforme: `forecast_many(nombre, years, vals, targets) -> {year: valor}`
para años FUTUROS (targets > max(years)). Se usa tanto en la validación cruzada
(un paso) como en el relleno final (varios pasos). Devuelve None si el algoritmo
no puede ajustarse (serie demasiado corta, no converge, dependencia ausente…),
para que la competición lo descarte con elegancia.

Los huecos internos NO se predicen aquí: se rellenan por interpolación lineal en
modelado.py (un modelo de proyección extrapola, no interpola).

Registro de complejidad (para la regla de parsimonia) y disponibilidad:
  media/naive = 0 · deriva/lineal = 1 · ets = 2 · arima = 3 · prophet = 4 · rf/xgb = 5
"""

import contextlib
import io
import logging
import warnings

import numpy as np

warnings.filterwarnings("ignore")
for _n in ("cmdstanpy", "prophet", "statsmodels"):
    logging.getLogger(_n).setLevel(logging.CRITICAL)

# ── Disponibilidad de dependencias (degradación elegante) ───────────────────
try:
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from statsmodels.tsa.arima.model import ARIMA
    _HAS_SM = True
except Exception:  # noqa: BLE001
    _HAS_SM = False
try:
    from prophet import Prophet
    _HAS_PROPHET = True
except Exception:  # noqa: BLE001
    _HAS_PROPHET = False
try:
    from sklearn.ensemble import RandomForestRegressor
    _HAS_RF = True
except Exception:  # noqa: BLE001
    _HAS_RF = False
try:
    import xgboost as _xgb
    _xgb.XGBRegressor()          # fuerza la carga de la lib nativa (libomp)
    _HAS_XGB = True
except Exception:  # noqa: BLE001
    _HAS_XGB = False

COMPLEJIDAD = {"media": 0, "naive": 0, "deriva": 1, "lineal": 1,
               "ets": 2, "arima": 3, "prophet": 4, "rf": 5, "xgboost": 5}
BASE = ["media", "naive", "deriva", "lineal", "ets", "arima"]
AVANZADOS = ["prophet", "rf", "xgboost"]


def disponibles(cands):
    out = []
    for c in cands:
        if c in ("ets", "arima") and not _HAS_SM:
            continue
        if c == "prophet" and not _HAS_PROPHET:
            continue
        if c == "rf" and not _HAS_RF:
            continue
        if c == "xgboost" and not _HAS_XGB:
            continue
        out.append(c)
    return out


def forecast_many(nombre, years, vals, targets):
    years = np.asarray(years, float)
    vals = np.asarray(vals, float)
    tg = sorted(targets)
    last = years[-1]
    try:
        if nombre == "media":
            m = float(np.mean(vals))
            return {t: m for t in tg}
        if nombre == "naive":
            return {t: float(vals[-1]) for t in tg}
        if nombre == "deriva":
            span = years[-1] - years[0]
            slope = (vals[-1] - vals[0]) / span if span > 0 else 0.0
            return {t: float(vals[-1] + slope * (t - last)) for t in tg}
        if nombre == "lineal":
            if len(vals) < 2:
                return None
            b, a = np.polyfit(years, vals, 1)
            return {t: float(b * t + a) for t in tg}
        if nombre == "ets":
            if len(vals) < 4:
                return None
            fit = ExponentialSmoothing(vals, trend="add", damped_trend=True,
                                       initialization_method="estimated").fit()
            h = int(max(tg) - last)
            fc = np.asarray(fit.forecast(h), float)
            return {t: float(fc[int(t - last) - 1]) for t in tg}
        if nombre == "arima":
            if len(vals) < 5:
                return None
            best, best_aic = None, np.inf
            for order in [(0, 1, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1), (1, 0, 0)]:
                try:
                    trend = "t" if order[1] == 0 else None
                    r = ARIMA(vals, order=order, trend=trend).fit()
                    if r.aic < best_aic:
                        best, best_aic = r, r.aic
                except Exception:  # noqa: BLE001
                    continue
            if best is None:
                return None
            h = int(max(tg) - last)
            fc = np.asarray(best.forecast(h), float)
            return {t: float(fc[int(t - last) - 1]) for t in tg}
        if nombre == "prophet":
            if len(vals) < 5:
                return None
            import pandas as pd
            dfp = pd.DataFrame({"ds": pd.to_datetime([f"{int(y)}-01-01" for y in years]),
                                "y": vals})
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                m = Prophet(yearly_seasonality=False, weekly_seasonality=False,
                            daily_seasonality=False, growth="linear")
                m.fit(dfp)
                fut = pd.DataFrame({"ds": pd.to_datetime([f"{int(t)}-01-01" for t in tg])})
                pred = m.predict(fut)
            return {t: float(v) for t, v in zip(tg, pred["yhat"].values)}
        if nombre in ("rf", "xgboost"):
            X = years.reshape(-1, 1)
            if nombre == "rf":
                mdl = RandomForestRegressor(n_estimators=200, random_state=0,
                                            min_samples_leaf=1)
            else:
                mdl = _xgb.XGBRegressor(n_estimators=200, max_depth=3, random_state=0)
            mdl.fit(X, vals)
            return {t: float(mdl.predict(np.array([[t]]))[0]) for t in tg}
    except Exception:  # noqa: BLE001
        return None
    return None
