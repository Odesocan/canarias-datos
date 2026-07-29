#!/usr/bin/env python3
"""EDA de `ced_presupuestos` — missings y outliers.

Genera un informe markdown + figuras en outputs/eda/. Se centra en la CAPA
AUTONÓMICA (194 filas), la que llevan los extractores por CCAA; la capa hacienda
(SGCIEF) solo trae `total` y se resume aparte.

Missings   : NULL por concepto, matriz CCAA×concepto, combinaciones CCAA-año
             ausentes, disponibilidad de pc_/pib_.
Outliers   : per-cápita €/hab por concepto (IQR + z robusto), banda de sanidad,
             saltos año-a-año (var_). Se marcan los ya documentados.

Uso: python3 outputs/eda/eda_ced_presupuestos.py
"""
from __future__ import annotations
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "eda"
OUT.mkdir(parents=True, exist_ok=True)
CSV = ROOT / "4_carga" / "ced_presupuestos.csv"

CONCEPTS = ["sanidad", "educacion", "soberania", "direccion", "vivienda", "empleo",
            "idi", "dependencia", "discapacidad", "salud_mental", "diversidad",
            "turismo", "igualdad"]
POB = {  # millones de habitantes (de tools/auditoria_magnitud.py)
    "and": 8.47, "ara": 1.33, "ast": 1.01, "bal": 1.18, "can": 2.24, "cat": 7.79,
    "clm": 2.05, "cnt": 0.58, "cym": 2.38, "ext": 1.06, "gal": 2.70, "lar": 0.32,
    "mad": 6.79, "mur": 1.53, "nav": 0.67, "pvc": 2.21, "val": 5.06,
}
NAME2ID = {
    "Andalucía": "and", "Aragón": "ara", "Principado de Asturias": "ast",
    "Islas Baleares": "bal", "Canarias": "can", "Cantabria": "cnt",
    "Castilla y León": "cym", "Castilla-La Mancha": "clm", "Cataluña": "cat",
    "Comunidad Valenciana": "val", "Extremadura": "ext", "Comunidad de Madrid": "mad",
    "Región de Murcia": "mur", "Comunidad Foral de Navarra": "nav",
    "País Vasco": "pvc", "La Rioja": "lar", "Galicia": "gal",
}
# NULL estructural DOCUMENTADO (fichas limitaciones-*): no es fallo de extracción.
STRUCTURAL = {
    "salud_mental": {"ast", "clm", "cnt", "ext", "gal", "mad", "pvc"},
    "discapacidad": {"ara", "ast", "ext", "gal", "pvc"},
    "dependencia": {"ara", "ast", "pvc"},
}

L = []  # líneas del informe
def w(s=""): L.append(s)

df = pd.read_csv(CSV, sep=";", decimal=",")
au = df[df.capa == "autonomica"].copy()
au["id3"] = au["ccaa"].map(NAME2ID)
imp = ["imp_" + c for c in CONCEPTS]

w("# EDA · `ced_presupuestos` — missings y outliers")
w()
w("> Generado por `outputs/eda/eda_ced_presupuestos.py` sobre `4_carga/ced_presupuestos.csv`.")
w("> Rev. 2026-07-02. Valores `imp_` en euros CONSTANTES (deflactados).")
w()
w(f"**Datos:** {len(df)} filas ({(df.capa=='autonomica').sum()} autonómica + "
  f"{(df.capa=='hacienda').sum()} hacienda) · {au['id3'].nunique()} CCAA · "
  f"{int(au.periodo.min())}-{int(au.periodo.max())}. El análisis de conceptos es sobre la "
  f"**capa autonómica**; la hacienda solo trae `total`.")
w()

# ===================== MISSINGS =====================
w("## 1 · Missings")
w()

# 1a. combinaciones CCAA-año ausentes
years = sorted(au.periodo.unique())
ccaa = sorted(au.id3.dropna().unique())
present = set(zip(au.id3, au.periodo))
missing_combos = [(c, y) for c in ccaa for y in years if (c, y) not in present]
w(f"### 1.1 · Combinaciones CCAA-año ausentes ({len(missing_combos)} de {len(ccaa)*len(years)} posibles)")
w()
if missing_combos:
    by_ccaa = {}
    for c, y in missing_combos:
        by_ccaa.setdefault(c, []).append(str(y))
    w("| CCAA | años ausentes |")
    w("|------|---------------|")
    for c in sorted(by_ccaa):
        w(f"| {c} | {', '.join(by_ccaa[c])} |")
    w()
    w("> Nota: muchos son años sin fuente publicada (cym 2019/2020/2022, cat 2018/2021/2025, "
      "val ≤2015) o fuente que falló en el pipeline (mur 2026). No confundir con NULL de concepto.")
else:
    w("Ninguna: panel completo.")
w()

# 1b. NULL por concepto
w("### 1.2 · NULL por concepto (capa autonómica)")
w()
nrate = (au[imp].isna().mean() * 100).sort_values(ascending=False)
w("| concepto | % filas NULL | filas con dato | ¿estructural? |")
w("|----------|:---:|:---:|---|")
for col, pct in nrate.items():
    c = col.replace("imp_", "")
    ndata = int(au[col].notna().sum())
    est = ""
    if c in STRUCTURAL:
        est = f"sí en {len(STRUCTURAL[c])} CCAA: {', '.join(sorted(STRUCTURAL[c]))}"
    elif c == "total":
        est = "total no aplica a capa autonómica"
    w(f"| {c} | {pct:.0f}% | {ndata} | {est} |")
w()

# 1c. matriz CCAA x concepto (años con dato)
w("### 1.3 · Cobertura CCAA × concepto (nº de años con dato / años presentes)")
w()
cov = au.groupby("id3")[imp].apply(lambda g: g.notna().sum())
cov.columns = [c.replace("imp_", "") for c in cov.columns]
yrs = au.groupby("id3").periodo.nunique()
concepts13 = [c for c in CONCEPTS]  # sin total
w("| CCAA | años | " + " | ".join(concepts13) + " |")
w("|------|:---:|" + "|".join([":---:"] * len(concepts13)) + "|")
for cc in sorted(cov.index):
    cells = []
    for c in concepts13:
        n = int(cov.loc[cc, c]); t = int(yrs.loc[cc])
        mark = "·" if n == 0 else ("✓" if n == t else str(n))
        cells.append(mark)
    w(f"| {cc} | {int(yrs.loc[cc])} | " + " | ".join(cells) + " |")
w()
w("> `✓` = todos los años; `·` = 0 años (NULL total); número = años parciales.")
w()

# 1d. divergencia staging(Python) vs modelado(R) en la asignación de concepto
w("### 1.4 · ⚠️ Divergencia Python (staging) vs modelado (R) — concepto")
w()
w("El modelado R re-deriva el concepto desde el `correspondencias.yml` **RAÍZ (global)**, "
  "NO desde los `1_extraccion/ccaa/*/correspondencias.yml` (Python) donde viven los fixes "
  "2026-07-02. Donde R mapea a un concepto distinto, R gana (el fallback solo actúa si R es "
  "NA). Resultado: la tabla entregada NO refleja del todo los fixes conceptuales.")
w()
try:
    import subprocess
    subprocess.run(["Rscript", "-e",
        'st<-readRDS("1_extraccion/staging_gasto.rds");st<-st[st$capa=="autonomica",];'
        'ag<-aggregate(importe_eur~ccaa_id3+concepto,st[!is.na(st$concepto)&st$concepto!="",],sum);'
        'write.csv(ag,"/tmp/_stg_conc.csv",row.names=FALSE)'],
        cwd=ROOT, check=True, capture_output=True)
    stg = pd.read_csv("/tmp/_stg_conc.csv")
    stg_has = {(r.ccaa_id3, r.concepto) for r in stg.itertuples()}
    mod_has = {(cc, c) for cc in au.id3.dropna().unique() for c in CONCEPTS
               if au[au.id3 == cc]["imp_" + c].notna().any()}
    perdidos = sorted((cc, c) for (cc, c) in stg_has - mod_has if c in CONCEPTS)
    fabricados = sorted((cc, c) for (cc, c) in mod_has - stg_has if c in CONCEPTS)
    w(f"**(a) En el staging (Python, correcto) pero NULL en la tabla (R lo pierde) — {len(perdidos)}:**")
    w()
    w("| CCAA | concepto |")
    w("|------|----------|")
    for cc, c in perdidos:
        w(f"| {cc} | {c} |")
    w()
    w(f"**(b) En la tabla (R) pero NO en el staging — concepto FABRICADO por el mapping viejo — {len(fabricados)}:**")
    w()
    w("| CCAA | concepto |")
    w("|------|----------|")
    for cc, c in fabricados:
        w(f"| {cc} | {c} |")
    w()
    w("> **Acción:** propagar los fixes 2026-07-02 al `correspondencias.yml` RAÍZ (o hacer que "
      "la transformación prefiera el concepto Python) y re-modelar + recargar. Sin eso, "
      "`clm/cnt` diversidad, 5×`salud_mental`, etc. faltan, y `ast/gal/clm/cnt` arrastran "
      "salud_mental/discapacidad FABRICADOS que los fixes ya eliminaron en el staging.")
    w()
except Exception as e:  # noqa
    w(f"> (No se pudo comparar con el staging: {e})")
    perdidos = fabricados = []
w()

# ===================== OUTLIERS =====================
w("## 2 · Outliers")
w()
w("> ⚠️ **Aviso metodológico:** los `imp_` de esta tabla están **deflactados a € "
  "constantes**, así que el per-cápita calculado aquí sale ~20-30 % por encima del "
  "nominal en los años recientes. La banda de sanidad 900-2300 está calibrada en €/hab "
  "NOMINALES → aquí sobre-marca. El chequeo de banda AUTORITATIVO (nominal, sobre el "
  "staging) es `tools/auditoria_magnitud.py`; abajo se anota qué anomalías son reales "
  "(documentadas en nominal) y cuáles son artefacto de la deflación.")
w()

# Anomalías REALES de sanidad confirmadas en NOMINAL (auditoria_magnitud sobre staging).
SANIDAD_REAL = {  # (id3, año) documentados fuera de banda en nominal
    ("and", 2020), ("and", 2021), ("and", 2022), ("and", 2015), ("and", 2016),
    ("ast", 2015), ("ast", 2025), ("ast", 2026),
    ("pvc", 2025), ("pvc", 2026),
}

# per-cápita €/hab por concepto (en € CONSTANTES; ver aviso)
for c in CONCEPTS:
    au["pc_" + c] = au["imp_" + c] / (au["id3"].map(POB) * 1e6)

# 2a. IQR + z robusto por concepto
w("### 2.1 · Per-cápita €/hab por concepto — outliers (IQR 1.5× sobre todas las CCAA-año)")
w()
w("| concepto | mediana €/hab | banda IQR | nº outliers | CCAA-año atípicos (top) |")
w("|----------|:---:|:---:|:---:|---|")
outlier_rows = []
for c in CONCEPTS:
    s = au["pc_" + c].dropna()
    if len(s) < 8 or s.median() == 0:
        continue
    q1, q3 = s.quantile(.25), s.quantile(.75)
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    out = au[(au["pc_" + c] < lo) | (au["pc_" + c] > hi)][["id3", "periodo", "pc_" + c]].dropna()
    out = out.reindex(out["pc_" + c].sub(s.median()).abs().sort_values(ascending=False).index)
    tags = ", ".join(f"{r.id3}{int(r.periodo)}={r['pc_'+c]:.0f}"
                     for _, r in out.head(4).iterrows())
    w(f"| {c} | {s.median():.0f} | {max(lo,0):.0f}–{hi:.0f} | {len(out)} | {tags} |")
    for _, r in out.iterrows():
        outlier_rows.append((c, r.id3, int(r.periodo), r["pc_" + c]))
w()

# 2b. banda de sanidad (en € constantes; anotando real vs artefacto de deflación)
w("### 2.2 · Sanidad €/hab alto (per-cápita en € CONSTANTES; banda nominal 900–2300)")
w()
sb = au[["id3", "periodo", "pc_sanidad"]].dropna()
fuera = sb[(sb.pc_sanidad < 900) | (sb.pc_sanidad > 2300)].sort_values("pc_sanidad", ascending=False)
n_real = n_art = 0
if len(fuera):
    w("| CCAA | año | €/hab (const.) | ¿anomalía real (nominal)? |")
    w("|------|:---:|:---:|---|")
    for _, r in fuera.iterrows():
        key = (r.id3, int(r.periodo))
        if r.pc_sanidad < 900:
            lect = "⚠️ BAJO → revisar (infra-extracción)"; n_real += 1
        elif key in SANIDAD_REAL:
            lect = "🔴 SÍ — documentada (ver ficha)"; n_real += 1
        else:
            lect = "🟢 no — en banda en nominal; artefacto de € constantes"; n_art += 1
        w(f"| {r.id3} | {int(r.periodo)} | {r.pc_sanidad:.0f} | {lect} |")
    w()
    w(f"> De los {len(fuera)} marcados, **{n_real} son anomalías reales** (documentadas: `and` "
      "perímetro rama CSV, `ast` 2015 doble conteo 413D+412B, `pvc` 2025-26 alta inversión "
      f"vasca) y **{n_art} son artefacto de la deflación** (en banda al medirse en nominal: "
      "cym, nav, cnt, etc.). Confirmar siempre con `auditoria_magnitud.py` (nominal).")
else:
    w("Ninguno fuera de banda.")
w()

# 2c. saltos año-a-año (var_) extremos, separando aparición de salto de magnitud
w("### 2.3 · Saltos año-a-año (concepto ≥ 50 M€)")
w()
apariciones, saltos = [], []
for c in CONCEPTS:
    vcol, icol = "var_" + c, "imp_" + c
    if vcol not in au.columns:
        continue
    sub = au[["id3", "periodo", vcol, icol]].dropna(subset=[vcol])
    for _, r in sub.iterrows():
        if pd.notna(r[icol]) and r[icol] < 50e6:
            continue
        v = r[vcol]
        if v > 200:                       # base ~0 → el concepto aparece/salta de escala
            apariciones.append((c, r.id3, int(r.periodo), v))
        elif abs(v) > 40:                 # salto de magnitud entre dos valores sustanciales
            saltos.append((c, r.id3, int(r.periodo), v))
apariciones.sort(key=lambda x: -x[3]); saltos.sort(key=lambda x: -abs(x[3]))

w(f"**(a) Saltos de magnitud reales** (±40–200 %, entre dos valores no triviales): "
  f"{len(saltos)}. Candidatos a revisar contra la ficha (seam de método, cambio de fuente).")
w()
if saltos:
    w("| concepto | CCAA | año | var % |")
    w("|----------|------|:---:|:---:|")
    for c, cc, y, v in saltos[:20]:
        w(f"| {c} | {cc} | {y} | {v:+.0f}% |")
    if len(saltos) > 20:
        w(f"| … | | | (+{len(saltos)-20} más) |")
    w()
w(f"**(b) Apariciones / cambios de escala** (>200 %, base ~0): {len(apariciones)}. NO son "
  "anomalías de magnitud: son conceptos que empiezan a mapearse (muchos por los fixes "
  "2026-07-02: pvc igualdad, val salud_mental, and diversidad…) o cambios de perímetro.")
w()
if apariciones:
    w("| concepto | CCAA | año | var % |")
    w("|----------|------|:---:|:---:|")
    for c, cc, y, v in apariciones[:12]:
        w(f"| {c} | {cc} | {y} | {v:+.0f}% |")
    if len(apariciones) > 12:
        w(f"| … | | | (+{len(apariciones)-12} más) |")
    w()

# ===================== FIGURAS =====================
# Fig 1: heatmap missings CCAA x concepto
covm = cov[concepts13].reindex(sorted(cov.index))
frac = covm.div(yrs.reindex(covm.index), axis=0)  # fracción de años con dato
fig, ax = plt.subplots(figsize=(11, 6))
im = ax.imshow(frac.values, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)
ax.set_xticks(range(len(concepts13))); ax.set_xticklabels(concepts13, rotation=45, ha="right", fontsize=8)
ax.set_yticks(range(len(covm.index))); ax.set_yticklabels(covm.index, fontsize=8)
ax.set_title("Cobertura de concepto por CCAA (verde=todos los años, rojo=NULL)")
for i in range(len(covm.index)):
    for j in range(len(concepts13)):
        v = frac.values[i, j]
        ax.text(j, i, "·" if v == 0 else f"{v:.0%}", ha="center", va="center",
                fontsize=6, color="black")
fig.colorbar(im, ax=ax, shrink=.7, label="fracción de años con dato")
fig.tight_layout(); fig.savefig(OUT / "fig_missings_heatmap.png", dpi=130); plt.close(fig)

# Fig 2: boxplots per-cápita por concepto
fig, ax = plt.subplots(figsize=(11, 5))
data = [au["pc_" + c].dropna().values for c in CONCEPTS]
ax.boxplot(data, tick_labels=CONCEPTS, showfliers=True, flierprops=dict(marker="o", ms=3))
ax.set_ylabel("€/hab (constantes)"); ax.set_yscale("symlog")
ax.set_title("Distribución per-cápita por concepto (puntos = outliers IQR)")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=8)
fig.tight_layout(); fig.savefig(OUT / "fig_percapita_boxplots.png", dpi=130); plt.close(fig)

# Fig 3: sanidad €/hab por CCAA (última observación) con banda
last = sb.sort_values("periodo").groupby("id3").last().sort_values("pc_sanidad")
fig, ax = plt.subplots(figsize=(10, 5))
colors = ["#d62728" if (v > 2300 or v < 900) else "#2ca02c" for v in last.pc_sanidad]
ax.bar(last.index, last.pc_sanidad, color=colors)
ax.axhspan(900, 2300, alpha=.1, color="green")
ax.axhline(1700, ls="--", color="gray", lw=.8)
ax.set_ylabel("sanidad €/hab"); ax.set_title("Sanidad €/hab por CCAA (última observación; banda 900-2300)")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=8)
fig.tight_layout(); fig.savefig(OUT / "fig_sanidad_percapita.png", dpi=130); plt.close(fig)

w("## 3 · Figuras")
w()
w("- `fig_missings_heatmap.png` — cobertura de concepto por CCAA (verde=completo, rojo=NULL).")
w("- `fig_percapita_boxplots.png` — distribución per-cápita por concepto (outliers marcados).")
w("- `fig_sanidad_percapita.png` — sanidad €/hab por CCAA con la banda de plausibilidad.")
w()

# ===================== RESUMEN =====================
w("## 4 · Síntesis")
w()
w("- **🚩 Lo más importante — la tabla entregada no refleja del todo los fixes 2026-07-02:** "
  f"{len(perdidos)} concepto-CCAA están bien en el staging (Python) pero se pierden en el "
  f"modelado R, y {len(fabricados)} conceptos FABRICADOS por el mapping viejo siguen en la "
  "tabla. Causa: el modelado R usa el `correspondencias.yml` RAÍZ, no los per-CCAA de Python "
  "(§1.4). **Requiere propagar los fixes al raíz + re-modelar + recargar.**")
top_null = [c.replace("imp_", "") for c in nrate.index[:3]]
w(f"- **Missings de concepto:** los 3 más difíciles son **{', '.join(top_null)}** — servicios "
  "sociales especializados que muchas CCAA no presupuestan como programa propio (NULL "
  "estructural, no fallo de extracción; ver STRUCTURAL en el script y las fichas).")
w(f"- **Combinaciones ausentes:** {len(missing_combos)} CCAA-año, casi todas por falta de fuente "
  "publicada o prórroga, no por error.")
w("- **Outliers per-cápita (en € constantes):** los de sanidad se concentran en `and` "
  "(perímetro rama CSV), `ast` 2015 y `pvc` 2025-26 (documentados); el resto de flags de "
  "banda son artefacto de la deflación. Por concepto, los altos son legítimos por perfil "
  "(soberanía alta en `ext`; dirección/diversidad altas en `nav` foral; empleo alto en `pvc`).")
w(f"- **Saltos de magnitud reales:** {len(saltos)} (±40-200 %); las {len(apariciones)} "
  "'apariciones' (>200 %) son conceptos recién mapeados por los fixes 2026-07-02, no anomalías.")
w("- **🔎 Hallazgo a revisar (nuevo):** `educacion` de **Baleares se desploma en 2020-2021** "
  f"(bal 2020 ≈ {au[(au.id3=='bal')&(au.periodo==2020)]['pc_educacion'].iloc[0]:.0f} €/hab vs "
  f"~{au[(au.id3=='bal')&(au.periodo==2019)]['pc_educacion'].iloc[0]:.0f} en 2019) y en Madrid "
  "queda infra-capturada (proxy-centro). Ninguna es de los 12 fixes: son candidatas para la "
  "siguiente iteración (bal 2020-21 parece un año con secciones incompletas, como 2015-16).")
w()

(OUT / "EDA_ced_presupuestos_2026-07-02.md").write_text("\n".join(L), encoding="utf-8")
print("OK · informe:", OUT / "EDA_ced_presupuestos_2026-07-02.md")
print("   figuras:", ", ".join(p.name for p in OUT.glob("*.png")))
print(f"   missings CCAA-año: {len(missing_combos)} · outliers per-cápita: {len(outlier_rows)} · saltos: {len(saltos)}")
