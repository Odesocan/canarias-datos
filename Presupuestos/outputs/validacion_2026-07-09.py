#!/usr/bin/env python3
"""Validación §2.6: conciliación autonómica↔Hacienda + Benford (primer dígito).
Fuentes: outputs/staging_py_<f>.csv (autonómico nominal) y outputs/hacienda_staging.csv.
Salidas: outputs/conciliacion_2026-07-09.csv y outputs/benford_2026-07-09.csv (+ resumen stdout)."""
import csv, math
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
STAG = ROOT/"outputs"/"staging_py_2026-07-09.csv"
HAC  = ROOT/"outputs"/"hacienda_staging.csv"
NOM = {"and":"Andalucía","ara":"Aragón","ast":"Asturias","bal":"Baleares","can":"Canarias",
 "cat":"Cataluña","clm":"Cast.-La Mancha","cnt":"Cantabria","cym":"Cast. y León","ext":"Extremadura",
 "gal":"Galicia","lar":"La Rioja","mad":"Madrid","mur":"Murcia","nav":"Navarra","pvc":"País Vasco","val":"C. Valenciana"}

def num(x):
    try: v=float(x); return v if v==v else 0.0
    except: return 0.0

# --- totales autonómicos (suma todas las filas) ---
auto=defaultdict(float); imps=[]
for r in csv.DictReader(open(STAG)):
    v=num(r["importe_eur"]); auto[(r["ccaa_id3"],int(r["anio"]))]+=v
    if v>0: imps.append(v)
# --- totales hacienda (suma capítulos) ---
hac=defaultdict(float)
for r in csv.DictReader(open(HAC)):
    hac[(r["ccaa_id3"],int(r["anio"]))]+=num(r["importe_eur"])

# --- conciliación ---
rows=[]
for (c,a),ha in sorted(hac.items()):
    au=auto.get((c,a))
    ratio = (au/ha) if (au and ha) else None
    flag=""
    if ratio is not None:
        if ratio>1.5: flag="AUTO_ALTO(perímetro/doble conteo)"
        elif ratio<0.6: flag="AUTO_BAJO(infra-captura)"
        else: flag="OK"
    else:
        flag="sin_autonomico" if au is None else "sin_hacienda"
    rows.append(dict(ccaa=c,nombre=NOM.get(c,c),anio=a,
        total_hacienda_b=round(ha/1e9,3),
        total_auto_b=(round(au/1e9,3) if au else None),
        ratio=(round(ratio,3) if ratio else None), flag=flag))
with open(ROOT/"outputs"/"conciliacion_2026-07-09.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

ok=sum(1 for r in rows if r["flag"]=="OK")
alto=[r for r in rows if r["flag"].startswith("AUTO_ALTO")]
bajo=[r for r in rows if r["flag"].startswith("AUTO_BAJO")]
print(f"CONCILIACIÓN: {len(rows)} celdas con Hacienda; OK(0.6-1.5)={ok}  ALTO={len(alto)}  BAJO={len(bajo)}")
def agg(lst):
    d=defaultdict(list)
    for r in lst: d[r["ccaa"]].append(r["anio"])
    return ", ".join(f"{k}({min(v)}-{max(v)},n={len(v)})" for k,v in sorted(d.items()))
if alto: print("  ALTO:", agg(alto))
if bajo: print("  BAJO:", agg(bajo))

# --- Benford primer dígito ---
cnt=defaultdict(int)
for v in imps:
    d=str(int(v))[0]
    if d in "123456789": cnt[int(d)]+=1
N=sum(cnt.values())
exp={d:math.log10(1+1/d) for d in range(1,10)}
chi=0.0; brows=[]
for d in range(1,10):
    obs=cnt[d]/N; e=exp[d]
    chi+=(cnt[d]-e*N)**2/(e*N)
    brows.append(dict(digito=d,obs_pct=round(obs*100,2),esp_pct=round(e*100,2),n=cnt[d]))
with open(ROOT/"outputs"/"benford_2026-07-09.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["digito","obs_pct","esp_pct","n"]); w.writeheader(); w.writerows(brows)
# chi2 crit 8 gl, alpha .05 = 15.51
print(f"\nBENFORD (1er dígito, N={N}): chi2={chi:.2f}  (crítico 8gl α.05=15.51 → {'CONFORME' if chi<15.51 else 'DESVÍA'})")
print("  d: obs% / esp%  " + "  ".join(f"{r['digito']}:{r['obs_pct']}/{r['esp_pct']}" for r in brows))
