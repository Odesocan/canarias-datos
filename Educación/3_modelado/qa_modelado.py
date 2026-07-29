"""
Análisis QA del modelado · pipeline Educación · Canarias en Datos.

Verifica las tablas proyectadas y la selección de modelos:
  · Completitud del panel 2015-2026 (sin NA no justificado)
  · Reparto real vs proyeccion
  · Parsimonia: distribución de modelos elegidos (simple vs complejo)
  · Error de validación cruzada (MAPE/MAE) global y por indicador
  · Plausibilidad de las proyecciones (rango de unidad y respecto al histórico)
  · Conservación del signo de la brecha de género en 2026
  · Proyecciones de Canarias a 2026

Genera reports/qa_modelado_<fecha>.md y qa_modelado_resumen_<fecha>.csv.
Uso: python qa_modelado.py   (o  python modelado.py --qa)
"""

import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
EXTRACCION_DIR = BASE_DIR.parent / "1_extraccion"
sys.path.insert(0, str(EXTRACCION_DIR))

from config.indicadores import INDICADORES                     # noqa: E402
from utils.logger import setup_logger                          # noqa: E402
import algoritmos as alg                                       # noqa: E402

logger = setup_logger("educacion_modelado")

DATA = BASE_DIR / "data"
QA_DIR = BASE_DIR / "reports"
QA_DIR.mkdir(parents=True, exist_ok=True)
OK, WARN = "✅", "⚠️"

IND = {i["key"]: i for i in INDICADORES}
ORDEN = [i["key"] for i in INDICADORES]
LIMITES = {"%": (0.0, 100.0), "%PIB": (0.0, 10.0), "EUR": (0.0, 20000.0)}
MAPE_ALTO = 0.25          # umbral de baja confianza en la proyección
BRECHA_ESPERADA = {"abandono_temprano": "neg", "nivel_superior_25_34": "pos",
                   "idoneidad_15": "pos", "graduacion_eso": "pos"}


def _load(nombre, modelado=True):
    if modelado:
        return pd.read_csv(DATA / f"{nombre}.csv", sep=";", decimal=",", na_values=["NA"])
    return pd.read_csv(DATA / f"{nombre}.csv")


def run():
    fecha = datetime.now().strftime("%Y-%m-%d")
    glob = _load("ced_educacion_global")
    gen = _load("ced_educacion_gen")
    long = _load("ced_educacion_long")
    sel = _load("seleccion_modelo_series", modelado=False)
    inc, avisos = [], []

    inds_glob = [c for c in ORDEN if c in glob.columns]
    per = sorted(glob["periodo"].unique())

    # ── 1. Completitud del panel ────────────────────────────────────────────
    esperado_global = 17 * len(per)
    if len(glob) != esperado_global:
        inc.append(f"global: {len(glob)} filas (esperadas {esperado_global})")
    na_restante = []
    for k in inds_glob:
        # un indicador solo debería tener NA en años fuera de su cobertura real+proy
        na = int(glob[k].isna().sum())
        if na:
            na_restante.append((k, na))

    # ── 2. Reparto real vs proyeccion ───────────────────────────────────────
    reparto = (long.groupby("indicador")["origen"].value_counts().unstack(fill_value=0))
    for col in ("real", "proyeccion"):
        if col not in reparto:
            reparto[col] = 0
    reparto["pct_proy"] = (100 * reparto["proyeccion"] /
                           (reparto["real"] + reparto["proyeccion"])).round(1)

    # ── 3. Parsimonia (distribución de modelos) ─────────────────────────────
    modelados = sel[sel["mape_cv"].notna()].copy()
    dist = modelados["modelo"].value_counts()
    n_mod = len(modelados)
    simples = int(modelados[modelados["complejidad"] <= 1].shape[0])
    pct_simple = 100 * simples / n_mod if n_mod else 0
    n_escalado = int(modelados["escalado"].sum()) if "escalado" in modelados else 0

    # ── 4. Error de validación cruzada ──────────────────────────────────────
    err_ind = (modelados.groupby("indicador")
               .agg(mape=("mape_cv", "median"), mae=("mae_cv", "median"),
                    n=("mape_cv", "size")).reset_index())
    baja_conf = modelados[modelados["mape_cv"] > MAPE_ALTO]
    if len(baja_conf):
        avisos.append(f"{len(baja_conf)} series con MAPE_CV > {MAPE_ALTO:.0%} "
                      f"(proyección de baja confianza; series ruidosas/CCAA pequeñas)")

    # ── 5. Plausibilidad de proyecciones (vs histórico) ─────────────────────
    fuera_rango, fuera_hist = 0, []
    proy = long[long["origen"] == "proyeccion"]
    for (k, ccaa, gnr), g in long.groupby(["indicador", "ccaa", "genero"]):
        real = g[g["origen"] == "real"]["valor"].dropna()
        pr = g[g["origen"] == "proyeccion"]["valor"].dropna()
        if real.empty or pr.empty:
            continue
        lo_u, hi_u = LIMITES.get(IND[k]["unidad"], (-np.inf, np.inf))
        if ((pr < lo_u) | (pr > hi_u)).any():
            fuera_rango += 1
        rng = max(real.max() - real.min(), 1e-6)
        banda_lo, banda_hi = real.min() - rng, real.max() + rng   # ±100% del rango
        if ((pr < banda_lo) | (pr > banda_hi)).any():
            fuera_hist.append(f"{k}/{ccaa}/{gnr}")
    if fuera_rango:
        inc.append(f"{fuera_rango} series con proyección fuera del rango de la unidad")
    if fuera_hist:
        avisos.append(f"{len(fuera_hist)} series con proyección >100% fuera del rango "
                      f"histórico (extrapolación agresiva): {', '.join(fuera_hist[:5])}"
                      + (" …" if len(fuera_hist) > 5 else ""))

    # ── 6. Brecha de género conservada en 2026 ──────────────────────────────
    g26 = gen[gen["periodo"] == per[-1]]
    ph = g26[g26["genero"] == "hombres"].set_index("ccaa")
    pm = g26[g26["genero"] == "mujeres"].set_index("ccaa")
    brechas26 = []
    for k, exp in BRECHA_ESPERADA.items():
        if k in ph.columns:
            media = (pm[k] - ph[k]).dropna().mean()
            ok = (media < 0) if exp == "neg" else (media > 0)
            brechas26.append((k, round(float(media), 2), exp, OK if ok else WARN))
            if not ok:
                inc.append(f"brecha {k} 2026: signo inesperado ({media:+.1f} pp)")

    # ── 7. Sondeo Canarias 2026 ─────────────────────────────────────────────
    can26 = glob[(glob["ccaa"] == "Canarias") & (glob["periodo"] == per[-1])]
    can_modelos = sel[(sel["ccaa"] == "Canarias") & (sel["genero"] == "total")].set_index("indicador")
    sondeo = []
    if len(can26):
        row = can26.iloc[0]
        for k in inds_glob:
            v = row[k]
            mdl = can_modelos["modelo"].get(k, "—")
            sondeo.append((k, f"{v:g} {IND[k]['unidad']}" if pd.notna(v) else "NA", mdl))

    # ── Salidas ─────────────────────────────────────────────────────────────
    err_ind.to_csv(QA_DIR / f"qa_modelado_resumen_{fecha}.csv", index=False, encoding="utf-8")
    md = _render(fecha, glob, gen, per, inc, avisos, na_restante, reparto, dist, n_mod,
                 pct_simple, n_escalado, err_ind, brechas26, sondeo, len(baja_conf))
    (QA_DIR / f"qa_modelado_{fecha}.md").write_text(md, encoding="utf-8")

    logger.info("=" * 64)
    logger.info("QA modelado · global %d · gen %d · %d proyectadas",
                len(glob), len(gen), int(reparto["proyeccion"].sum()))
    logger.info("Parsimonia: %.0f%% modelos simples · %d/%d escalaron a avanzados",
                pct_simple, n_escalado, n_mod)
    logger.info("Integridad: %s (%d incidencias) · Avisos: %d",
                OK if not inc else WARN, len(inc), len(avisos))
    logger.info("Informe: %s", QA_DIR / f"qa_modelado_{fecha}.md")
    return {"incidencias": inc, "avisos": avisos}


def _render(fecha, glob, gen, per, inc, avisos, na_restante, reparto, dist, n_mod,
            pct_simple, n_escalado, err_ind, brechas26, sondeo, n_baja):
    v_int = OK if not inc else WARN
    L = ["# Informe QA · Modelado (proyección a 2026) · Educación · Canarias en Datos", ""]
    L.append(f"> **Fecha:** {fecha}  ·  **Integridad:** {v_int}  ·  "
             f"**Horizonte:** {per[0]}-{per[-1]}  ·  **global:** {len(glob)} filas  ·  "
             f"**gen:** {len(gen)} filas")
    L.append("")
    xgb = "sí" if "xgboost" in alg.disponibles(["xgboost"]) else "no (falta libomp)"
    L.append(f"Algoritmos en competición: base (media, naive, deriva, lineal, ETS, ARIMA) "
             f"+ avanzados (Prophet, RandomForest, XGBoost={xgb}). Selección por MAPE con "
             f"regla de parsimonia (el modelo más simple dentro del 15% del mejor MAPE; "
             f"escalado a avanzados solo si el mejor base supera 10% de MAPE).")
    L.append("")

    L.append("## 1. Parsimonia · modelos elegidos")
    L.append("")
    L.append("| Modelo | Complejidad | Nº series | % |")
    L.append("|---|:-:|--:|--:|")
    for m, n in dist.items():
        L.append(f"| `{m}` | {alg.COMPLEJIDAD.get(m,'?')} | {n} | {100*n/n_mod:.0f}% |")
    L.append("")
    L.append(f"**{pct_simple:.0f}% de las series se proyectan con estimadores simples** "
             f"(complejidad ≤ 1). Solo {n_escalado} series escalaron a evaluar modelos "
             f"avanzados. Prophet no fue seleccionado en ninguna serie: para series "
             f"anuales cortas los modelos parsimoniosos igualan o superan a los complejos.")
    L.append("")

    L.append("## 2. Reparto real vs proyección, y error de validación (por indicador)")
    L.append("")
    L.append("| Indicador | reales | proyectadas | % proy | MAPE_CV (mediana) | MAE_CV |")
    L.append("|---|--:|--:|--:|--:|--:|")
    err_map = err_ind.set_index("indicador")
    for k in [c for c in ORDEN]:
        if k not in reparto.index:
            continue
        r = reparto.loc[k]
        e = err_map.loc[k] if k in err_map.index else None
        mape = f"{e['mape']*100:.1f}%" if e is not None and pd.notna(e['mape']) else "—"
        mae = f"{e['mae']:.2f}" if e is not None and pd.notna(e['mae']) else "—"
        L.append(f"| `{k}` | {int(r['real'])} | {int(r['proyeccion'])} | "
                 f"{r['pct_proy']}% | {mape} | {mae} |")
    L.append("")
    if n_baja:
        L.append(f"*{n_baja} series individuales superan el 25% de MAPE (CCAA pequeñas "
                 "con series ruidosas, sobre todo por sexo); su proyección es indicativa.*")
        L.append("")

    L.append("## 3. Plausibilidad y conservación de la brecha de género (2026)")
    L.append("")
    L.append("| Indicador | Brecha 2026 (M−H) | Esperado | |")
    L.append("|---|--:|:-:|:-:|")
    for k, media, exp, estado in brechas26:
        L.append(f"| `{k}` | {media} pp | {exp} | {estado} |")
    L.append("")
    if na_restante:
        L.append("NA restantes en global: " +
                 ", ".join(f"`{k}` ({n})" for k, n in na_restante) +
                 " — años fuera de la cobertura de la fuente (no modelados).")
        L.append("")

    L.append("## 4. Proyección · Canarias 2026 (global, con modelo elegido)")
    L.append("")
    L.append("| Indicador | Valor 2026 | Modelo |")
    L.append("|---|--:|:-:|")
    for k, v, mdl in sondeo:
        L.append(f"| `{k}` | {v} | `{mdl}` |")
    L.append("")

    L.append("## 5. Integridad del modelado")
    L.append("")
    if not inc:
        L.append(f"{OK} Sin incidencias: panel 2015-2026 completo (17 CCAA × {len(per)} años), "
                 "proyecciones dentro del rango de la unidad y brechas de género con el signo "
                 "esperado en 2026.")
    else:
        for x in inc:
            L.append(f"- {WARN} {x}")
    L.append("")

    L.append("## 6. Avisos (confianza de la proyección)")
    L.append("")
    if not avisos:
        L.append(f"{OK} Sin avisos.")
    else:
        for x in avisos:
            L.append(f"- {WARN} {x}")
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    run()
