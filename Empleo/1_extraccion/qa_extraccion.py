# -*- coding: utf-8 -*-
"""QA de la fase de extracción — Empleo (Canarias en Datos)."""
import json
from pathlib import Path
import numpy as np
import pandas as pd

SAL = Path(__file__).resolve().parent / "salida"
CCAA_ESPERADAS = {"Total Nacional","Andalucía","Aragón","Principado de Asturias","Illes Balears",
"Canarias","Cantabria","Castilla y León","Castilla-La Mancha","Cataluña","Comunitat Valenciana",
"Extremadura","Galicia","Comunidad de Madrid","Región de Murcia","Comunidad Foral de Navarra",
"País Vasco","La Rioja","Ceuta","Melilla"}

EPA_TASAS = ["epa_tasa_paro","epa_tasa_actividad","epa_tasa_empleo"]
EPA_PCT = ["epa_tipo_jornada","epa_tipo_contrato","epa_tiempo_busqueda"]

problemas = []   # (severidad, tabla, mensaje)
def flag(sev, tabla, msg): problemas.append((sev, tabla, msg))

print("="*78)
print("QA · FASE DE EXTRACCIÓN — SECCIÓN EMPLEO")
print("="*78)

# ---------------------------------------------------------------- #
# 1) QA estructural por tabla
# ---------------------------------------------------------------- #
resumen = []
tablas = sorted(p.stem for p in SAL.glob("*.parquet"))
for t in tablas:
    df = pd.read_parquet(SAL/f"{t}.parquet")
    n = len(df)
    row = {"tabla": t, "filas": n}
    # duplicados por serie+periodo
    if {"serie_cod","anyo","periodo"}.issubset(df.columns):
        dup = df.duplicated(subset=["serie_cod","anyo","periodo"]).sum()
        row["dups"] = int(dup)
        if dup: flag("ALTA", t, f"{dup} filas duplicadas (serie_cod,anyo,periodo)")
    # NAs de valor
    valcol = "valor" if "valor" in df.columns else ("precio_m2_medio_anual" if "precio_m2_medio_anual" in df.columns else None)
    if valcol:
        na = df[valcol].isna().mean()
        neg = (df[valcol] < 0).sum()
        row["na_valor_%"] = round(na*100,2)
        row["negativos"] = int(neg)
        if na > 0.05: flag("MEDIA", t, f"tasa de NA en valor = {na:.1%}")
        if neg: flag("ALTA", t, f"{neg} valores negativos en {valcol}")
    # territorio
    if "territorio" in df.columns:
        terr = set(df["territorio"].dropna().unique())
        row["n_terr"] = len(terr)
        nulos_terr = df["territorio"].isna().sum()
        if nulos_terr: flag("ALTA", t, f"{nulos_terr} filas con territorio sin mapear")
        # balance de series por territorio (deben ser homogéneas en tablas INE)
        if "serie_cod" in df.columns and terr:
            spt = df.groupby("territorio")["serie_cod"].nunique()
            if spt.min()!=spt.max():
                flag("REVISAR", t, f"series por territorio no homogéneas: min={spt.min()} max={spt.max()}")
    # tipo_dato
    if "tipo_dato" in df.columns:
        row["tipos_dato"] = "|".join(sorted(str(x) for x in df["tipo_dato"].dropna().unique()))
    # rango temporal
    if "anyo" in df.columns:
        row["años"] = f"{int(df['anyo'].min())}-{int(df['anyo'].max())}"
    resumen.append(row)

print("\n■ 1. RESUMEN ESTRUCTURAL POR TABLA")
print(pd.DataFrame(resumen).to_string(index=False))

# ---------------------------------------------------------------- #
# 2) Cobertura territorial (¿faltan CCAA?)
# ---------------------------------------------------------------- #
print("\n■ 2. COBERTURA TERRITORIAL (vs 20 territorios canónicos)")
for t in tablas:
    df = pd.read_parquet(SAL/f"{t}.parquet")
    if "territorio" not in df.columns: continue
    terr = set(df["territorio"].dropna().unique())
    faltan = CCAA_ESPERADAS - terr
    extra = terr - CCAA_ESPERADAS
    estado = "completo" if not faltan else f"FALTAN: {sorted(faltan)}"
    print(f"  {t:24} {len(terr):>2} terr · {estado}")
    if faltan and t not in ("eaes_ganancia_ccaa","alquiler_ccaa_anual","etcl_tiempo_trabajo"):
        flag("MEDIA", t, f"faltan territorios: {sorted(faltan)}")
    if extra:
        flag("REVISAR", t, f"territorios no esperados: {sorted(extra)}")

# ---------------------------------------------------------------- #
# 3) Coherencia: porcentajes por categoría suman ~100
# ---------------------------------------------------------------- #
print("\n■ 3. COHERENCIA DE PORCENTAJES (deben sumar ~100 por territorio·genero·periodo)")

def cat_jornada(s):
    if "tiempo completo" in s: return "completo"
    if "tiempo parcial" in s: return "parcial"
    if ". Total." in s: return "total"
    return None
def cat_contrato(s):
    if "indefinida" in s: return "indefinido"
    if "Temporal:" in s or "duración temporal" in s.lower(): return "temporal"
    if "Canarias. Total." in s or ". Total. " in s and "duración" not in s.lower(): return "total"
    return None

def check_pct(t, categorizador, cats_suma, tol=0.6):
    df = pd.read_parquet(SAL/f"{t}.parquet")
    df = df[df["unidad"]=="Porcentaje"].copy()
    df["cat"] = df["serie_nombre"].map(categorizador)
    sub = df[df["cat"].isin(cats_suma)]
    g = sub.groupby(["territorio","genero","anyo","periodo"])["valor"].sum().reset_index()
    g["desv"] = (g["valor"]-100).abs()
    malos = g[g["desv"]>tol]
    print(f"  {t}: {len(g)} grupos · suma media={g['valor'].mean():.2f} · fuera de [100±{tol}]: {len(malos)}")
    if len(malos):
        ej = malos.iloc[0]
        flag("REVISAR", t, f"{len(malos)}/{len(g)} grupos donde {'+'.join(cats_suma)} no suma 100 "
             f"(ej: {ej['territorio']}/{ej['genero']}/{ej['periodo']} = {ej['valor']:.1f})")
    return g

check_pct("epa_tipo_jornada", cat_jornada, ["completo","parcial"])
check_pct("epa_tipo_contrato", cat_contrato, ["indefinido","temporal"])

# tiempo_busqueda: todas las categorías salvo 'Total' suman 100
def cat_busqueda(s):
    return "total" if s.strip().endswith("Total. Porcentaje.") else "detalle"
df_tb = pd.read_parquet(SAL/"epa_tiempo_busqueda.parquet")
df_tb = df_tb[df_tb["unidad"]=="Porcentaje"].copy()
df_tb["cat"]=df_tb["serie_nombre"].map(cat_busqueda)
g_tb = df_tb[df_tb["cat"]=="detalle"].groupby(["territorio","genero","anyo","periodo"])["valor"].sum().reset_index()
g_tb["desv"]=(g_tb["valor"]-100).abs()
malos_tb = g_tb[g_tb["desv"]>0.6]
print(f"  epa_tiempo_busqueda: {len(g_tb)} grupos · suma media={g_tb['valor'].mean():.2f} · fuera de 100: {len(malos_tb)}")
if len(malos_tb): flag("REVISAR","epa_tiempo_busqueda",f"{len(malos_tb)} grupos no suman 100")

# ---------------------------------------------------------------- #
# 4) Coherencia absolutos: completo+parcial = Total (jornada)
# ---------------------------------------------------------------- #
print("\n■ 4. COHERENCIA VALORES ABSOLUTOS (completo+parcial = Total)")
dj = pd.read_parquet(SAL/"epa_tipo_jornada.parquet")
dj = dj[dj["unidad"]=="Personas"].copy()
dj["cat"]=dj["serie_nombre"].map(cat_jornada)
piv = dj.pivot_table(index=["territorio","genero","anyo","periodo"],columns="cat",values="valor",aggfunc="first")
piv=piv.dropna(subset=["total"])
piv["suma"]=piv.get("completo",0)+piv.get("parcial",0)
piv["dif"]=(piv["suma"]-piv["total"]).abs()
malos_abs=piv[piv["dif"]>piv["total"]*0.01+0.05]
print(f"  epa_tipo_jornada: {len(piv)} grupos · desajustes (>1%): {len(malos_abs)}")
if len(malos_abs): flag("REVISAR","epa_tipo_jornada",f"{len(malos_abs)} grupos donde completo+parcial != total")

# ---------------------------------------------------------------- #
# 5) Rangos plausibles
# ---------------------------------------------------------------- #
print("\n■ 5. RANGOS PLAUSIBLES")
for t in EPA_TASAS:
    df=pd.read_parquet(SAL/f"{t}.parquet")
    fuera=df[(df["valor"]<0)|(df["valor"]>100)]
    print(f"  {t}: valor en [{df['valor'].min():.1f},{df['valor'].max():.1f}] · fuera [0,100]: {len(fuera)}")
    if len(fuera): flag("ALTA",t,f"{len(fuera)} tasas fuera de [0,100]")
etcl=pd.read_parquet(SAL/"etcl_tiempo_trabajo.parquet")
he=etcl[etcl["serie_nombre"].str.contains("Horas efectivas")]
print(f"  etcl horas efectivas: [{he['valor'].min():.1f},{he['valor'].max():.1f}] (esperado ~80-190 h/mes)")
if he["valor"].max()>250 or he["valor"].min()<0: flag("REVISAR","etcl_tiempo_trabajo","horas fuera de rango")
eaes=pd.read_parquet(SAL/"eaes_ganancia_ccaa.parquet")
med=eaes[eaes["serie_nombre"].str.strip().str.endswith("Media.")]
print(f"  eaes ganancia media: [{med['valor'].min():.0f},{med['valor'].max():.0f}] €/año")

# ---------------------------------------------------------------- #
# 6) Signo de la brecha salarial (Hombres >= Mujeres, típico)
# ---------------------------------------------------------------- #
print("\n■ 6. BRECHA SALARIAL — signo (H vs M) por CCAA, último año")
med2 = med.copy()
ult = med2["anyo"].max()
m = med2[med2["anyo"]==ult]
piv2 = m.pivot_table(index="territorio",columns="genero",values="valor",aggfunc="first")
piv2=piv2.dropna(subset=["Hombres","Mujeres"])
piv2["brecha_%"]=((piv2["Hombres"]-piv2["Mujeres"])/piv2["Hombres"]*100).round(2)
neg=piv2[piv2["brecha_%"]<0]
print(f"  año {ult}: {len(piv2)} CCAA · brecha media={piv2['brecha_%'].mean():.2f}% · negativas (M>H): {len(neg)}")
print("  Canarias:", piv2.loc["Canarias","brecha_%"] if "Canarias" in piv2.index else "n/d","%")
if len(neg): flag("INFO","eaes_ganancia_ccaa",f"{len(neg)} CCAA con brecha negativa (M>H): {list(neg.index)}")

# ---------------------------------------------------------------- #
# 7) Continuidad temporal (serie de referencia Canarias)
# ---------------------------------------------------------------- #
print("\n■ 7. CONTINUIDAD TEMPORAL (Canarias · Ambos géneros · Total)")
for t in EPA_TASAS:
    df=pd.read_parquet(SAL/f"{t}.parquet")
    ref=df[(df.territorio=="Canarias")&(df.genero=="Ambos géneros")&(df.serie_nombre.str.strip().str.endswith("Total."))]
    ref=ref.sort_values(["anyo","periodo"])
    per=ref["periodo"].tolist()
    # esperado: 4 trimestres/año desde 2010
    n_years=ref["anyo"].nunique()
    print(f"  {t}: {len(ref)} periodos · {n_years} años · {per[0]}→{per[-1]}")
    esperado = n_years*4
    if not (esperado-4 <= len(ref) <= esperado+1):
        flag("REVISAR",t,f"nº de periodos ({len(ref)}) no cuadra con {n_years} años trimestrales")

# ---------------------------------------------------------------- #
# 8) tipo_dato: cuántos periodos son Avance/Provisional
# ---------------------------------------------------------------- #
print("\n■ 8. TIPO DE DATO (avances/provisionales — sensibles a revisión)")
for t in EPA_TASAS+["etcl_tiempo_trabajo"]:
    df=pd.read_parquet(SAL/f"{t}.parquet")
    vc=df["tipo_dato"].value_counts(dropna=False)
    nodef=df[df["tipo_dato"]!="Definitivo"]
    print(f"  {t}: {dict(vc)}")

# ---------------------------------------------------------------- #
# 9) Alquiler (Supabase)
# ---------------------------------------------------------------- #
print("\n■ 9. ALQUILER CCAA (Supabase)")
al=pd.read_parquet(SAL/"alquiler_ccaa_anual.parquet")
parc=al[al["n_meses"]<12]
print(f"  {len(al)} filas · {al['territorio'].nunique()} CCAA · años {al['anyo'].min()}-{al['anyo'].max()}")
print(f"  años parciales (n_meses<12): {len(parc)} (normal en 2026 y arranques)")
can=al[al.territorio=="Canarias"].sort_values("anyo")
mono = can["precio_m2_medio_anual"].is_monotonic_increasing
print(f"  Canarias 2010→2026: {can['precio_m2_medio_anual'].iloc[0]}→{can['precio_m2_medio_anual'].iloc[-1]} €/m²")
if al["precio_m2_medio_anual"].min()<=0: flag("ALTA","alquiler","precio<=0")

# ---------------------------------------------------------------- #
# 10) Cross-check vs valor INE publicado conocido
# ---------------------------------------------------------------- #
print("\n■ 10. CONTRASTE CON DATO PUBLICADO (spot-check)")
dp=pd.read_parquet(SAL/"epa_tasa_paro.parquet")
v=dp[(dp.territorio=="Canarias")&(dp.genero=="Ambos géneros")&(dp.serie_nombre.str.strip().str.endswith("Total."))&(dp.periodo=="2026T1")]["valor"]
print(f"  Tasa paro Canarias 2026T1 extraída = {v.values[0] if len(v) else 'n/d'}%  (INE publica 11,40%)")

# ---------------------------------------------------------------- #
# Veredicto
# ---------------------------------------------------------------- #
print("\n"+"="*78)
print("VEREDICTO QA")
print("="*78)
orden={"ALTA":0,"MEDIA":1,"REVISAR":2,"INFO":3}
if not problemas:
    print("✓ Sin incidencias.")
else:
    for sev,tab,msg in sorted(problemas,key=lambda x:orden.get(x[0],9)):
        print(f"  [{sev:7}] {tab}: {msg}")
print(f"\nTotal incidencias: {len(problemas)}  "
      f"(ALTA={sum(1 for p in problemas if p[0]=='ALTA')}, "
      f"MEDIA={sum(1 for p in problemas if p[0]=='MEDIA')}, "
      f"REVISAR={sum(1 for p in problemas if p[0]=='REVISAR')}, "
      f"INFO={sum(1 for p in problemas if p[0]=='INFO')})")
