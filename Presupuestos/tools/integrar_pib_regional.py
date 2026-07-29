#!/usr/bin/env python3
# =============================================================================
# integrar_pib_regional.py — ODESOCAN · Canarias en Datos · Presupuestos
#
# Integra el gasto de las 17 CCAA en una sola tabla, le une el PIB REGIONAL de
# cada comunidad (no el nacional) y calcula el % del PIB regional destinado a
# cada área — el indicador que hace comparables las prioridades políticas entre
# territorios (dividir por el PIB nacional penalizaría a las CCAA pequeñas por
# tamaño, no por prioridad).
#
# FASE 1 · TRANSFORMACIÓN  (fase_transformacion)
#   - Integra staging_py_*.csv (todas las CCAA, nominal €) en un df ancho
#     (ccaa × ejercicio) con una columna imp_<concepto> por cada uno de los 13
#     conceptos + imp_social_total.
#   - Une el PIB regional real (INE Contabilidad Regional, op. 30679; 2015-2024)
#     desde fuentes/externos/pib_regional_ccaa.csv.
#
# FASE 2 · MODELADO  (fase_modelado)
#   - Proyecta el PIB regional de los años sin dato (2025, 2026) mediante un
#     BOOTSTRAP de las tasas de crecimiento históricas (ver docstring de
#     proyectar_pib_bootstrap): punto = mediana, banda P05-P95, origen marcado.
#   - Calcula pct_pib_<concepto> = imp_<concepto> / pib_regional × 100 y el
#     agregado pct_pib_social_total.
#
# Salidas (outputs/):
#   presupuestos_pib_integrado_<fecha>.csv   — tabla ancha final (indicador)
#   presupuestos_pib_integrado_<fecha>_long.csv — formato largo (viz/BI)
#   pib_regional_proyeccion_<fecha>.csv      — detalle de la proyección + banda
#
# Uso:
#   python3 tools/integrar_pib_regional.py \
#       [--staging outputs/staging_py_2026-07-16.csv] [--horizonte 2026] \
#       [--n-boot 5000] [--seed 20260716]
# =============================================================================
from __future__ import annotations

import argparse
import datetime as _dt
from pathlib import Path

import numpy as np
import pandas as pd

# --- Constantes de dominio -------------------------------------------------
CONCEPTOS = [
    "sanidad", "educacion", "soberania", "direccion", "vivienda", "empleo",
    "idi", "dependencia", "discapacidad", "salud_mental", "diversidad",
    "turismo", "igualdad",
]
CCAA_NOMBRE = {
    "and": "Andalucía", "ara": "Aragón", "ast": "Asturias", "bal": "Baleares",
    "can": "Canarias", "cat": "Cataluña", "clm": "Cast.-La Mancha",
    "cnt": "Cantabria", "cym": "Cast. y León", "ext": "Extremadura",
    "gal": "Galicia", "lar": "La Rioja", "mad": "Madrid", "mur": "Murcia",
    "nav": "Navarra", "pvc": "País Vasco", "val": "C. Valenciana",
}
BASE = Path(__file__).resolve().parent.parent
PIB_CSV = BASE / "fuentes" / "externos" / "pib_regional_ccaa.csv"


# ===========================================================================
# FASE 1 · TRANSFORMACIÓN
# ===========================================================================
def fase_transformacion(staging_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Integra el gasto de las 17 CCAA y le une el PIB regional real.

    Devuelve (gasto_ancho, pib_real):
      - gasto_ancho: una fila por (ccaa_id3, anio) con imp_<concepto> (13) +
        imp_social_total (suma de los 13 conceptos clasificados).
      - pib_real: PIB regional nominal por (ccaa_id3, anio), origen='real'.
    """
    st = pd.read_csv(staging_path, dtype={"anio": int})
    st["importe_eur"] = pd.to_numeric(st["importe_eur"], errors="coerce").fillna(0.0)
    st = st[st["concepto"].isin(CONCEPTOS)]

    # Suma por (ccaa, anio, concepto) → pivote ancho imp_<concepto>
    largo = (st.groupby(["ccaa_id3", "anio", "concepto"], as_index=False)["importe_eur"]
               .sum())
    ancho = (largo.pivot_table(index=["ccaa_id3", "anio"], columns="concepto",
                               values="importe_eur", fill_value=0.0)
                  .reset_index())
    ancho.columns.name = None
    ancho = ancho.rename(columns={c: f"imp_{c}" for c in CONCEPTOS})
    for c in CONCEPTOS:                       # garantiza las 13 columnas
        if f"imp_{c}" not in ancho:
            ancho[f"imp_{c}"] = 0.0
    ancho["imp_social_total"] = ancho[[f"imp_{c}" for c in CONCEPTOS]].sum(axis=1)
    ancho["ccaa"] = ancho["ccaa_id3"].map(CCAA_NOMBRE)

    if not PIB_CSV.exists():
        raise SystemExit(f"ERROR: falta {PIB_CSV}. Extrae el PIB regional primero.")
    pib = pd.read_csv(PIB_CSV, dtype={"anio": int})
    pib = pib[["ccaa_id3", "anio", "pib_regional_eur"]].copy()
    pib["origen_pib"] = "real"

    return ancho, pib


# ===========================================================================
# FASE 2 · MODELADO — proyección bootstrap del PIB + indicador
# ===========================================================================
def proyectar_pib_bootstrap(pib_real: pd.DataFrame, horizonte: int,
                            n_boot: int, seed: int) -> pd.DataFrame:
    """Proyecta el PIB regional de los años faltantes con un BOOTSTRAP.

    Motivación: el PIB regional del INE (op. 30679) es firme hasta 2024; 2025 y
    2026 no están publicados cuando se cierran los presupuestos. En vez de una
    extrapolación puntual (lineal/Prophet) que oculta la incertidumbre, se usa
    un bootstrap no paramétrico de las tasas de crecimiento nominal históricas.

    Algoritmo (por CCAA, serie 2015..t_max):
      1. g_t = ln(PIB_t / PIB_{t-1})  para todos los pares consecutivos
         (log-crecimientos; multiplicativos, nunca dan PIB negativo).
      2. Para cada réplica b=1..B y cada año a proyectar, se muestrea con
         reemplazo una g del histórico y se encadena:
            PIB*_{t+1} = PIB_t · exp(g*)   ;   PIB*_{t+2} = PIB*_{t+1} · exp(g*)
         El muestreo por año propaga la incertidumbre hacia el horizonte.
      3. Punto = MEDIANA de las réplicas (robusta al outlier COVID-2020, que se
         conserva en el pool para que la banda refleje el riesgo de recesión);
         banda = percentiles 5 y 95.

    Devuelve un df con (ccaa_id3, anio, pib_regional_eur, pib_lo, pib_hi,
    origen_pib='proyeccion', g_media_hist, n_growths).
    """
    rng = np.random.default_rng(seed)
    filas = []
    for cc, g in pib_real.groupby("ccaa_id3"):
        g = g.sort_values("anio")
        anios = g["anio"].to_numpy()
        vals = g["pib_regional_eur"].to_numpy(dtype=float)
        t_max = int(anios.max())
        if t_max >= horizonte:
            continue
        growths = np.diff(np.log(vals))           # log-crecimientos históricos
        growths = growths[np.isfinite(growths)]
        if len(growths) < 3:                       # serie demasiado corta
            continue
        pib_t = float(vals[-1])
        anios_proj = list(range(t_max + 1, horizonte + 1))
        # matriz réplicas × años proyectados
        sims = np.empty((n_boot, len(anios_proj)))
        actual = np.full(n_boot, pib_t)
        for j in range(len(anios_proj)):
            g_star = rng.choice(growths, size=n_boot, replace=True)
            actual = actual * np.exp(g_star)
            sims[:, j] = actual
        for j, a in enumerate(anios_proj):
            col = sims[:, j]
            filas.append({
                "ccaa_id3": cc, "anio": a,
                "pib_regional_eur": float(np.median(col)),
                "pib_lo": float(np.percentile(col, 5)),
                "pib_hi": float(np.percentile(col, 95)),
                "origen_pib": "proyeccion",
                "g_media_hist": float(np.mean(growths)),
                "n_growths": int(len(growths)),
            })
    return pd.DataFrame(filas)


def fase_modelado(ancho: pd.DataFrame, pib_real: pd.DataFrame,
                  horizonte: int, n_boot: int, seed: int
                  ) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Une PIB real+proyectado al gasto y calcula el indicador % PIB regional."""
    proj = proyectar_pib_bootstrap(pib_real, horizonte, n_boot, seed)
    pib_full = pd.concat([pib_real, proj], ignore_index=True, sort=False)

    df = ancho.merge(pib_full, on=["ccaa_id3", "anio"], how="left")

    # INDICADOR OBJETIVO: % del PIB regional por área
    pib = df["pib_regional_eur"]
    valido = pib.notna() & (pib > 0)
    for c in CONCEPTOS:
        df[f"pct_pib_{c}"] = np.where(valido, df[f"imp_{c}"] / pib * 100, np.nan)
    df["pct_pib_social_total"] = np.where(
        valido, df["imp_social_total"] / pib * 100, np.nan)

    # Orden de columnas legible
    id_cols = ["ccaa_id3", "ccaa", "anio", "pib_regional_eur", "origen_pib",
               "pib_lo", "pib_hi", "imp_social_total", "pct_pib_social_total"]
    imp_cols = [f"imp_{c}" for c in CONCEPTOS]
    pct_cols = [f"pct_pib_{c}" for c in CONCEPTOS]
    df = df[id_cols + imp_cols + pct_cols].sort_values(["ccaa_id3", "anio"])
    return df, proj


# ===========================================================================
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--staging", default=None,
                    help="CSV de staging (por defecto el más reciente en outputs/)")
    ap.add_argument("--horizonte", type=int, default=2026)
    ap.add_argument("--n-boot", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20260716)
    args = ap.parse_args()

    out_dir = BASE / "outputs"
    if args.staging:
        staging = Path(args.staging)
    else:
        cands = sorted(out_dir.glob("staging_py_*.csv"))
        if not cands:
            raise SystemExit("No hay staging_py_*.csv en outputs/")
        staging = cands[-1]
    fecha = _dt.date.today().isoformat()

    print(f"▶ staging: {staging.name}")
    ancho, pib_real = fase_transformacion(staging)
    print(f"  · integrado: {ancho['ccaa_id3'].nunique()} CCAA × "
          f"{ancho['anio'].nunique()} años = {len(ancho)} celdas")
    print(f"  · PIB real: {pib_real['anio'].min()}-{pib_real['anio'].max()} "
          f"({pib_real['ccaa_id3'].nunique()} CCAA)")

    df, proj = fase_modelado(ancho, pib_real, args.horizonte, args.n_boot, args.seed)
    n_proj = (df["origen_pib"] == "proyeccion").sum()
    print(f"  · PIB proyectado (bootstrap n={args.n_boot}): {n_proj} celdas "
          f"({sorted(proj['anio'].unique()) if len(proj) else '—'})")

    # Salidas
    f_wide = out_dir / f"presupuestos_pib_integrado_{fecha}.csv"
    df.round(4).to_csv(f_wide, index=False)

    long = df.melt(
        id_vars=["ccaa_id3", "ccaa", "anio", "pib_regional_eur", "origen_pib"],
        value_vars=[f"pct_pib_{c}" for c in CONCEPTOS],
        var_name="concepto", value_name="pct_pib_regional")
    long["concepto"] = long["concepto"].str.replace("pct_pib_", "", regex=False)
    imp_long = df.melt(id_vars=["ccaa_id3", "anio"],
                       value_vars=[f"imp_{c}" for c in CONCEPTOS],
                       var_name="concepto", value_name="importe_eur")
    imp_long["concepto"] = imp_long["concepto"].str.replace("imp_", "", regex=False)
    long = long.merge(imp_long, on=["ccaa_id3", "anio", "concepto"])
    f_long = out_dir / f"presupuestos_pib_integrado_{fecha}_long.csv"
    long.round(4).to_csv(f_long, index=False)

    f_proj = out_dir / f"pib_regional_proyeccion_{fecha}.csv"
    if len(proj):
        proj.round(2).to_csv(f_proj, index=False)

    print(f"\n✓ escrito: {f_wide.name}\n           {f_long.name}"
          + (f"\n           {f_proj.name}" if len(proj) else ""))

    # Vista rápida del indicador (sanidad, % PIB regional, 2015 vs horizonte)
    print("\n── % del PIB regional en SANIDAD (indicador objetivo) ──")
    piv = (df.pivot_table(index="ccaa", columns="anio", values="pct_pib_sanidad")
             .round(2))
    cols = [c for c in (2015, 2019, 2024, args.horizonte) if c in piv.columns]
    print(piv[cols].to_string())


if __name__ == "__main__":
    main()
