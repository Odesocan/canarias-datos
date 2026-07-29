# -*- coding: utf-8 -*-
"""
QA / VALIDACIÓN de la fase 3 (modelado) — Empleo · Canarias en Datos.

Comprueba el dataset con proyecciones (ced_empleo.csv):
  - bandera origen real/proyeccion y horizonte alcanzado (2026)
  - continuidad serie real → proyección (sin huecos ni solapes)
  - plausibilidad de las proyecciones (rango y salto vs último real)
  - reparto de modelos ganadores y peso de la parsimonia
  - foto de Canarias (último real + proyección)
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import config as cfg

problemas = []
def flag(sev, msg): problemas.append((sev, msg))

D = pd.read_parquet(cfg.SALIDA_DIR / "ced_empleo.parquet")
G = pd.read_csv(cfg.SALIDA_DIR / "seleccion_algoritmo_proyeccion_global.csv")
S = pd.read_csv(cfg.SALIDA_DIR / "seleccion_algoritmo_proyeccion_series.csv")

print("=" * 74); print("QA · MODELADO — SECCIÓN EMPLEO"); print("=" * 74)

# 1) bandera origen y horizonte
print("\n■ 1. BANDERA ORIGEN Y HORIZONTE")
print(D["origen"].value_counts().to_string())
proy = D[D["origen"] == "proyeccion"]
print(f"  años proyectados: {sorted(proy['anyo'].unique())}")
print(f"  máx año total: {int(D['anyo'].max())} (objetivo {cfg.HORIZONTE_ANYO})")
if int(proy["anyo"].max()) != cfg.HORIZONTE_ANYO:
    flag("ALTA", f"la proyección no llega a {cfg.HORIZONTE_ANYO}")

# 2) continuidad real→proyección por serie (nº de periodos esperados)
print("\n■ 2. CONTINUIDAD (trimestral: +3 periodos; anual: +2)")
for per, esperado in [("trimestral", 3), ("anual", 2)]:
    sub = D[D["periodicidad"] == per]
    if sub.empty: continue
    pp = sub[sub.origen == "proyeccion"].groupby(["indicador_id", "territorio", "genero"]).size()
    ok = (pp == esperado).mean() if len(pp) else 1.0
    print(f"  {per}: {len(pp)} series proyectadas · con {esperado} periodos = {ok:.0%}")
    if len(pp) and ok < 1.0: flag("REVISAR", f"{per}: series con nº de proyecciones distinto de {esperado}")

# 3) plausibilidad: tasas en [0,100]; salto proyección vs último real
print("\n■ 3. PLAUSIBILIDAD DE LAS PROYECCIONES")
tasas = proy[(proy.unidad == "%") & (proy.indicador_id != 11)]
fuera = tasas[(tasas.valor < 0) | (tasas.valor > 100)]
print(f"  tasas proyectadas fuera de [0,100]: {len(fuera)}")
if len(fuera): flag("ALTA", f"{len(fuera)} tasas proyectadas fuera de [0,100]")
# salto relativo del primer valor proyectado respecto al último real
ult_real = (D[D.origen == "real"].sort_values(["anyo", "trimestre"])
            .groupby(["indicador_id", "territorio", "genero"]).tail(1)
            .set_index(["indicador_id", "territorio", "genero"])["valor"])
prim_proy = (proy.sort_values(["anyo", "trimestre"])
             .groupby(["indicador_id", "territorio", "genero"]).head(1)
             .set_index(["indicador_id", "territorio", "genero"]))
prim_proy["ult_real"] = ult_real
prim_proy["salto_%"] = (prim_proy["valor"] - prim_proy["ult_real"]).abs() / prim_proy["ult_real"].abs() * 100
grandes = prim_proy[prim_proy["salto_%"] > 40]
print(f"  saltos >40% entre último real y 1ª proyección: {len(grandes)} (revisar si los hay)")
if len(grandes) > 0.05 * len(prim_proy):
    flag("REVISAR", f"{len(grandes)} series con salto grande en la 1ª proyección")

# 4) reparto de modelos y parsimonia
print("\n■ 4. SELECCIÓN DE MODELOS")
print(S["modelo"].value_counts().to_string())
pars = S["aplicó_parsimonia"].mean() if "aplicó_parsimonia" in S.columns else np.nan
print(f"  series donde ganó la parsimonia: {S['aplicó_parsimonia'].sum()}/{len(S)} ({pars:.0%})")
print("\n  ranking global (menor NMAE medio):")
print(G[["modelo", "series_evaluadas", "mape_medio", "nmae_medio", "n_series_ganadas"]]
      .round(4).to_string(index=False))

# 5) foto Canarias
print("\n■ 5. CANARIAS — tasa de paro (Ambos géneros): último real + proyección")
c = D[(D.territorio == "Canarias") & (D.indicador_id == 1) & (D.genero == "Ambos géneros")]
c = c.sort_values(["anyo", "trimestre"]).tail(6)
print(c[["anyo", "periodo", "valor", "origen", "algoritmo"]].to_string(index=False))

print("\n" + "=" * 74); print("VEREDICTO"); print("=" * 74)
if not problemas: print("✓ Sin incidencias.")
else:
    for s, m in problemas: print(f"  [{s}] {m}")
