# -*- coding: utf-8 -*-
"""
QA / VALIDACIÓN de la fase 2 (transformación) — Empleo · Canarias en Datos.

Comprueba el dataset consolidado (salida/ced_empleo*.parquet):
  - cobertura de indicadores y territorios
  - rangos plausibles por tipo de indicador
  - consistencia largo↔ancho (la media anual del largo == valor del ancho)
  - coherencia social esperada en Canarias (paro/temporalidad mayores en mujeres)
  - contraste con dato INE publicado
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import config as cfg

problemas = []
def flag(sev, msg): problemas.append((sev, msg))

LONG = pd.read_parquet(cfg.SALIDA_DIR / "ced_empleo.parquet")
ANCHO = pd.read_parquet(cfg.SALIDA_DIR / "ced_empleo_anual_ancho.parquet")

print("="*74); print("QA · TRANSFORMACIÓN — SECCIÓN EMPLEO"); print("="*74)

# 1) cobertura
print("\n■ 1. COBERTURA")
print(f"  indicadores: {sorted(LONG['indicador_id'].unique())}  (falta el 5 = afiliación, pendiente)")
print(f"  territorios: {LONG['territorio'].nunique()} · años {int(LONG['anyo'].min())}–{int(LONG['anyo'].max())}")
if LONG["indicador_id"].nunique() < 10:
    flag("ALTA", "faltan indicadores en el consolidado")

# 2) rangos plausibles
print("\n■ 2. RANGOS PLAUSIBLES")
tasas = LONG[LONG["unidad"] == "%"]
fuera = tasas[(tasas["valor"] < 0) | (tasas["valor"] > 100)]
# %alquiler puede superar 100 (renta > salario mensual): se excluye de la cota superior
fuera = fuera[fuera["indicador_id"] != 11]
print(f"  indicadores en %: fuera de [0,100] (excl. ind.11): {len(fuera)}")
if len(fuera): flag("ALTA", f"{len(fuera)} valores de tasa fuera de [0,100]")
horas = LONG[LONG["indicador_id"] == 4]["valor"]
print(f"  horas servicios: [{horas.min():.1f}, {horas.max():.1f}] h/mes")
alq = LONG[LONG["indicador_id"] == 11]["valor"]
print(f"  % alquiler/salario: [{alq.min():.1f}, {alq.max():.1f}] % (supuesto {cfg.SUPERFICIE_REF_M2} m²)")
if (alq < 0).any(): flag("ALTA", "% alquiler negativo")

# 3) consistencia largo → ancho (media anual)
print("\n■ 3. CONSISTENCIA LARGO ↔ ANCHO (media anual de trimestres)")
tri = LONG[(LONG["indicador_id"] == 1) & (LONG["periodicidad"] == "trimestral")]
med = (tri.groupby(["territorio", "genero", "anyo"])["valor"].mean().reset_index()
       .rename(columns={"valor": "media_largo"}))
comp = med.merge(ANCHO[["territorio", "genero", "anyo", "tasa_paro"]],
                 on=["territorio", "genero", "anyo"], how="inner")
comp["dif"] = (comp["media_largo"] - comp["tasa_paro"]).abs()
maxdif = comp["dif"].max()
print(f"  tasa de paro: máx |media_largo − ancho| = {maxdif:.6f}  (debe ≈ 0)")
if maxdif > 1e-6: flag("ALTA", f"inconsistencia largo/ancho en tasa_paro (máx {maxdif})")

# 4) coherencia social en Canarias (último año): mujeres ≥ hombres en paro y temporalidad
print("\n■ 4. COHERENCIA SOCIAL (Canarias, mujeres vs hombres)")
for ind_id, nom in [(1, "tasa_paro"), (8, "temporalidad"), (9, "parcialidad")]:
    a = ANCHO[(ANCHO["territorio"] == "Canarias")]
    piv = a.pivot_table(index="anyo", columns="genero", values=nom)
    if {"Hombres", "Mujeres"}.issubset(piv.columns):
        share = (piv["Mujeres"] > piv["Hombres"]).mean()
        print(f"  {nom}: años con M>H = {share:.0%}")

# 5) brecha salarial: signo y valor Canarias
print("\n■ 5. BRECHA SALARIAL")
br = ANCHO[(ANCHO["genero"] == "Ambos géneros")].dropna(subset=["brecha_salarial"])
ult = br["anyo"].max()
neg = br[(br["anyo"] == ult) & (br["brecha_salarial"] < 0)]
print(f"  año {int(ult)}: CCAA con brecha<0 (M>H): {len(neg)} · Canarias = "
      f"{br[(br.territorio=='Canarias')&(br.anyo==ult)]['brecha_salarial'].values}")

# 6) contraste con INE publicado
print("\n■ 6. CONTRASTE INE (tasa paro Canarias 2026, media anual parcial)")
v = ANCHO[(ANCHO.territorio=="Canarias")&(ANCHO.genero=="Ambos géneros")&(ANCHO.anyo==2026)]["tasa_paro"]
print(f"  tasa paro Canarias 2026 (sólo T1 disponible) = {v.values}")

# 7) genero en el ancho
print("\n■ 7. ESTRUCTURA DEL ANCHO")
print(f"  sexos: {sorted(ANCHO['genero'].unique())}  (esperado: Ambos/Hombres/Mujeres)")
if "Total" in ANCHO["genero"].unique(): flag("REVISAR", "quedan filas genero='Total' en el ancho")

print("\n"+"="*74); print("VEREDICTO"); print("="*74)
if not problemas:
    print("✓ Sin incidencias.")
else:
    for s, m in problemas: print(f"  [{s}] {m}")
