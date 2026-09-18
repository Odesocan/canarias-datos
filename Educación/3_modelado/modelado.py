"""
Etapa 3 · Modelado / proyección · pipeline Educación · Canarias en Datos.

Para cada serie (indicador × CCAA × género):
  1. Competición de algoritmos con validación cruzada temporal (rolling-origin,
     un paso adelante) → MAPE y MAE fuera de muestra.
  2. Escalado con parsimonia: se evalúan siempre los modelos base (media, naive,
     deriva, lineal, ETS, ARIMA) y solo se escala a los avanzados (Prophet,
     RandomForest, XGBoost) si el mejor base no baja del umbral de MAPE. Se elige
     el modelo MÁS SIMPLE que quede dentro de una tolerancia del mejor MAPE
     (un modelo complejo solo gana si la mejora es evidente).
  3. Relleno a 2026: huecos internos por interpolación lineal; años futuros con
     la proyección del modelo elegido. Bandera origen real/proyeccion + modelo.

Salidas (data/):
  · ced_educacion_global · ced_educacion_gen (2015-2026, con origen) + .xlsx
  · ced_educacion_long (por celda, con modelo)
  · seleccion_modelo_series.csv · seleccion_modelo_global.csv

Uso:
    python modelado.py --qa
    python modelado.py --horizon-end 2026
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
EDUCACION_DIR = BASE_DIR.parent
EXTRACCION_DIR = EDUCACION_DIR / "1_extraccion"
sys.path.insert(0, str(EXTRACCION_DIR))
sys.path.insert(0, str(BASE_DIR))

from config.indicadores import INDICADORES                     # noqa: E402
from utils.logger import setup_logger                          # noqa: E402
import algoritmos as alg                                       # noqa: E402

logger = setup_logger("educacion_modelado")

LONG_IN = EDUCACION_DIR / "2_transformacion" / "data" / "ced_educacion_long.csv"
OUT_DIR = BASE_DIR / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

WINDOW_START = 2015
GASTO_PIB_MIN = 1.5           # umbral de plausibilidad de gasto_edu_pib (%PIB)
MIN_OBS = 5                    # mínimo de puntos para competir (ref. proyecto)
UMBRAL_ESCALADO = 0.10        # MAPE base > 10% -> también se evalúan avanzados
TOL_PARSIMONIA = 1.15         # un modelo complejo solo gana si mejora >15% el MAPE

IND = {i["key"]: i for i in INDICADORES}
ORDEN = [i["key"] for i in INDICADORES]
IND_SEXO = [i["key"] for i in INDICADORES if i["desagrega_sexo"]]

# Límites de plausibilidad por unidad (recorte de proyecciones). Techos realistas
# —no 50.000 €/6× lo observado— para que el recorte no publique extrapolaciones
# absurdas como si fueran normales (el QA además valida contra el rango histórico).
LIMITES = {"%": (0.0, 100.0), "%PIB": (0.0, 10.0), "EUR": (0.0, 20000.0)}


def _cv_mape_mae(nombre, years, vals, max_folds=6):
    """Validación rolling-origin un paso adelante. Devuelve (mape, mae, n_folds).

    El denominador del MAPE tiene un SUELO relativo a la escala de la serie
    (1% de la magnitud media), no un 1e-6 absoluto: así un valor real cercano a
    cero no dispara el MAPE a miles por cien ni distorsiona la selección de
    modelo (protección frente a huecos de fuente que pasen los filtros previos).
    """
    n = len(vals)
    piso = max(0.01 * float(np.mean(np.abs(vals))), 1e-6)
    errs_ap, errs_ab = [], []
    for t in range(max(MIN_OBS, n - max_folds), n):  # folds recientes
        pred = alg.forecast_many(nombre, years[:t], vals[:t], [years[t]])
        if not pred:
            return None
        f = pred[years[t]]
        a = vals[t]
        if not np.isfinite(f):
            return None
        errs_ab.append(abs(a - f))
        errs_ap.append(abs(a - f) / max(abs(a), piso))
    if len(errs_ab) < 2:          # con <2 folds la CV no es fiable -> no se compite
        return None
    return float(np.mean(errs_ap)), float(np.mean(errs_ab)), len(errs_ab)


def _competir(years, vals):
    """Competición con escalado + parsimonia. Devuelve (elegido, tabla_dict)."""
    tabla = {}
    for nombre in alg.disponibles(alg.BASE):
        r = _cv_mape_mae(nombre, years, vals)
        if r:
            tabla[nombre] = {"mape": r[0], "mae": r[1], "folds": r[2],
                             "complejidad": alg.COMPLEJIDAD[nombre]}
    mejor_base = min((v["mape"] for v in tabla.values()), default=np.inf)
    escalado = mejor_base > UMBRAL_ESCALADO
    if escalado:
        # Los avanzados (Prophet/RF/XGB) se evalúan con los MISMOS folds que los
        # base: la comparación de MAPE debe ser sobre el mismo conjunto de test
        # (si no, el ruido de una CV corta puede premiar a un modelo complejo).
        for nombre in alg.disponibles(alg.AVANZADOS):
            r = _cv_mape_mae(nombre, years, vals)
            if r:
                tabla[nombre] = {"mape": r[0], "mae": r[1], "folds": r[2],
                                 "complejidad": alg.COMPLEJIDAD[nombre]}
    if not tabla:
        return None, {}, escalado
    mejor_mape = min(v["mape"] for v in tabla.values())
    umbral = mejor_mape * TOL_PARSIMONIA + 1e-4
    comparables = {k: v for k, v in tabla.items() if v["mape"] <= umbral}
    # el más simple entre los comparables; desempate por MAE y luego MAPE
    elegido = min(comparables,
                  key=lambda k: (comparables[k]["complejidad"],
                                 comparables[k]["mae"], comparables[k]["mape"]))
    return elegido, tabla, escalado


def _rellenar_serie(years, vals, modelo, horizonte):
    """Devuelve {periodo: (valor, origen, metodo)} para WINDOW_START..horizonte."""
    obs = dict(zip(years, vals))
    ymin, ymax = int(years[0]), int(years[-1])
    fila = {}
    futuros = [y for y in range(ymax + 1, horizonte + 1)]
    pred_fut = alg.forecast_many(modelo, years, vals, futuros) if futuros else {}
    lo, hi = LIMITES.get(_UNI, (-np.inf, np.inf))
    for y in range(WINDOW_START, horizonte + 1):
        if y in obs:
            fila[y] = (round(float(obs[y]), 4), "real", None)
        elif ymin < y < ymax:                        # hueco interno -> interpolación
            v = np.interp(y, years, vals)
            fila[y] = (round(float(np.clip(v, lo, hi)), 4), "proyeccion", "interpolacion")
        elif y > ymax and pred_fut and np.isfinite(pred_fut.get(y, np.nan)):
            v = np.clip(pred_fut[y], lo, hi)
            fila[y] = (round(float(v), 4), "proyeccion", modelo)
        # y < ymin (no debería ocurrir: todas arrancan en 2015) -> se omite
    return fila


_UNI = "%"   # unidad de la serie en curso (para el recorte); se fija por indicador


def modelar(horizonte=2026):
    global _UNI
    logger.info("=" * 64)
    logger.info("MODELADO · Educación · horizonte %d · escalado si MAPE>%.0f%%",
                horizonte, UMBRAL_ESCALADO * 100)
    logger.info("=" * 64)
    logger.info("Algoritmos disponibles: base=%s · avanzados=%s",
                alg.disponibles(alg.BASE), alg.disponibles(alg.AVANZADOS))

    df = pd.read_csv(LONG_IN, sep=";", decimal=",", na_values=["NA"], dtype={"ccaa_id": str})
    meta = df.drop_duplicates("ccaa").set_index("ccaa")[["ccaa_id", "nuts2"]].to_dict("index")
    ccaas = sorted(df["ccaa"].unique())

    # gasto_edu_pib NO se modela: es un insumo ya proyectado por el área de
    # Presupuestos. Cargamos su proyección oficial (origen='proyeccion') del raw,
    # enmascarando los valores implausibles (< 1.5 %PIB) igual que en transformación.
    presup_proy = {}
    raw_gp = EXTRACCION_DIR / "data" / "raw" / "gasto_edu_pib.csv"
    if raw_gp.exists():
        g = pd.read_csv(raw_gp, dtype={"ccaa_id": str})
        g = g[(g["origen"] == "proyeccion") & (g["valor"] >= GASTO_PIB_MIN)]
        presup_proy = {(r.ccaa_id, int(r.anio)): round(float(r.valor), 4) for r in g.itertuples()}
        logger.info("Presupuestos: %d proyecciones oficiales de gasto_edu_pib cargadas", len(presup_proy))

    filas, seleccion = [], []
    for key in ORDEN:
        _UNI = IND[key]["unidad"]
        generos = ["total", "hombres", "mujeres"] if IND[key]["desagrega_sexo"] else ["total"]
        for ccaa in ccaas:
            for genero in generos:
                s = df[(df["indicador"] == key) & (df["ccaa"] == ccaa) & (df["genero"] == genero)]
                s = s.dropna(subset=["valor"]).sort_values("periodo")
                years = s["periodo"].to_numpy(float)
                vals = s["valor"].to_numpy(float)
                n = len(vals)
                mrec = meta.get(ccaa, {"ccaa_id": None, "nuts2": None})

                # ── gasto_edu_pib: pass-through de Presupuestos (no se modela) ──
                if key == "gasto_edu_pib":
                    obs = {int(y): v for y, v in zip(years, vals)}
                    ymax = int(years.max()) if n else WINDOW_START - 1
                    n_proj = 0
                    for y in range(WINDOW_START, horizonte + 1):
                        if y in obs:                          # real observado (ya enmascarado)
                            valor, origen, metodo = round(float(obs[y]), 4), "real", None
                        elif y > ymax and (mrec["ccaa_id"], y) in presup_proy:
                            valor, origen, metodo = presup_proy[(mrec["ccaa_id"], y)], "proyeccion", "presupuestos"
                            n_proj += 1
                        else:
                            continue                          # hueco enmascarado -> NA (no se inventa)
                        filas.append({"indicador": key, "ccaa": ccaa,
                                      "ccaa_id": mrec["ccaa_id"], "nuts2": mrec["nuts2"],
                                      "periodo": y, "genero": genero, "valor": valor,
                                      "unidad": _UNI, "origen": origen, "modelo": metodo})
                    seleccion.append({"indicador": key, "ccaa": ccaa, "genero": genero,
                                      "modelo": "presupuestos", "n_obs": n, "mape_cv": None,
                                      "mae_cv": None, "escalado": False, "n_proyectado": n_proj,
                                      "complejidad": None})
                    continue

                if n < 2:
                    seleccion.append({"indicador": key, "ccaa": ccaa, "genero": genero,
                                      "modelo": "sin_datos", "n_obs": n, "mape_cv": None,
                                      "mae_cv": None, "escalado": False, "complejidad": None})
                    continue
                if n < MIN_OBS:                        # fallback parsimonioso
                    modelo = "lineal" if n >= 3 else "naive"
                    tabla, escalado, mape, mae = {}, False, None, None
                else:
                    modelo, tabla, escalado = _competir(years, vals)
                    if modelo is None:
                        modelo = "lineal"
                    mape = tabla.get(modelo, {}).get("mape")
                    mae = tabla.get(modelo, {}).get("mae")
                fila = _rellenar_serie(years, vals, modelo, horizonte)
                n_proj = 0
                for periodo, (valor, origen, metodo) in fila.items():
                    if origen == "proyeccion":
                        n_proj += 1
                    filas.append({"indicador": key, "ccaa": ccaa,
                                  "ccaa_id": mrec["ccaa_id"], "nuts2": mrec["nuts2"],
                                  "periodo": periodo, "genero": genero, "valor": valor,
                                  "unidad": _UNI, "origen": origen, "modelo": metodo})
                seleccion.append({"indicador": key, "ccaa": ccaa, "genero": genero,
                                  "modelo": modelo, "n_obs": n,
                                  "mape_cv": round(mape, 4) if mape is not None else None,
                                  "mae_cv": round(mae, 4) if mae is not None else None,
                                  "escalado": escalado, "n_proyectado": n_proj,
                                  "complejidad": alg.COMPLEJIDAD.get(modelo)})

    long_mod = pd.DataFrame(filas).sort_values(["indicador", "ccaa", "genero", "periodo"])
    sel_df = pd.DataFrame(seleccion)
    _exportar(long_mod, sel_df, horizonte)
    return {"long": long_mod, "seleccion": sel_df}


def _exportar(long_mod, sel_df, horizonte):
    # El origen va en la clave de las tablas anchas: un mismo año puede tener
    # una fila con lo real y otra con lo proyectado, y cada indicador sólo tiene
    # valor en la fila de su origen. Antes había una fila por (ccaa, periodo) y
    # se marcaba entera como proyección en cuanto un indicador lo era: la EPA de
    # 2024-2025, real, se publicaba como proyección porque la graduación en ESO
    # y el gasto por persona estudiante de esos años sí lo son (220 celdas). El
    # índice único de la carga ya era (ccaa, periodo, origen).
    # ── Wide global (genero=total, 10 indicadores) ──────────────────────────
    gt = long_mod[long_mod["genero"] == "total"]
    glob = gt.pivot_table(index=["ccaa", "periodo", "origen"], columns="indicador",
                          values="valor", aggfunc="first").reset_index()
    cols = ["ccaa", "periodo", "origen"] + [c for c in ORDEN if c in glob.columns]
    glob = glob[cols].sort_values(["ccaa", "periodo", "origen"])

    # ── Wide gen (8 indicadores × 3 géneros) ────────────────────────────────
    gs = long_mod[long_mod["indicador"].isin(IND_SEXO)]
    gen = gs.pivot_table(index=["ccaa", "periodo", "genero", "origen"], columns="indicador",
                         values="valor", aggfunc="first").reset_index()
    cols2 = ["ccaa", "periodo", "genero", "origen"] + [c for c in IND_SEXO if c in gen.columns]
    gen = gen[cols2].sort_values(["ccaa", "periodo", "genero", "origen"])

    for d, nombre in [(glob, "ced_educacion_global"), (gen, "ced_educacion_gen")]:
        d.to_csv(OUT_DIR / f"{nombre}.csv", sep=";", decimal=",", na_rep="NA", index=False)
        try:
            d.to_excel(OUT_DIR / f"{nombre}.xlsx", index=False)
        except Exception as e:  # noqa: BLE001
            logger.warning("xlsx %s: %s", nombre, e)
    long_mod.to_csv(OUT_DIR / "ced_educacion_long.csv", sep=";", decimal=",",
                    na_rep="NA", index=False)
    sel_df.to_csv(OUT_DIR / "seleccion_modelo_series.csv", index=False, encoding="utf-8")

    # Resumen global de selección (por algoritmo)
    modelados = sel_df[sel_df["mape_cv"].notna()]
    resumen = (modelados.groupby("modelo")
               .agg(n_series=("modelo", "size"),
                    mape_medio=("mape_cv", "mean"),
                    mae_medio=("mae_cv", "mean"),
                    complejidad=("complejidad", "first"))
               .reset_index().sort_values("n_series", ascending=False))
    resumen["mape_medio"] = resumen["mape_medio"].round(4)
    resumen["mae_medio"] = resumen["mae_medio"].round(3)
    resumen.to_csv(OUT_DIR / "seleccion_modelo_global.csv", index=False, encoding="utf-8")

    n_real = int((long_mod["origen"] == "real").sum())
    n_proj = int((long_mod["origen"] == "proyeccion").sum())
    logger.info("-" * 64)
    logger.info("Global: %d filas (%d-%d) · Gen: %d filas", len(glob),
                glob["periodo"].min(), glob["periodo"].max(), len(gen))
    logger.info("Celdas: %d reales · %d proyectadas (%.1f%%)", n_real, n_proj,
                100 * n_proj / (n_real + n_proj))
    logger.info("Modelos elegidos: %s",
                dict(zip(resumen["modelo"], resumen["n_series"])))
    logger.info("  -> ced_educacion_global/_gen/_long + seleccion_modelo_*.csv")


def main():
    p = argparse.ArgumentParser(description="Modelado · pipeline Educación")
    p.add_argument("--horizon-end", type=int, default=2026)
    p.add_argument("--qa", action="store_true")
    args = p.parse_args()
    modelar(args.horizon_end)
    if args.qa:
        logger.info("Lanzando análisis QA de modelado...")
        import qa_modelado
        qa_modelado.run()


if __name__ == "__main__":
    main()
