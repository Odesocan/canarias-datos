#!/usr/bin/env python3
"""Cobertura por CONCEPTO (2026-07-10).

La conciliación §2.6 por-concepto contra Hacienda NO es factible: la capa Hacienda
(SGCIEF) es clasificación ECONÓMICA por capítulos, no funcional, así que no hay
subfunción sanidad/educación con la que casar. Sustituto factible y útil: matriz de
cobertura de los 13 conceptos canónicos sobre las 204 celdas del staging autonómico
(€ nominales). Surfacea qué conceptos son NULOS ESTRUCTURALES por CCAA (p. ej. pvc
dependencia/discapacidad forales, ext salud_mental/discapacidad) frente a huecos
puntuales de un año.

Salidas:
  outputs/cobertura_concepto_2026-07-10.csv   (concepto x CCAA: nº años con importe>0, de 12)
  outputs/cobertura_concepto_2026-07-10.md    (matriz legible + diagnóstico)
"""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAG = ROOT / "outputs" / "staging_py_2026-07-09.csv"   # staging completo vigente
CONCEPTOS = ["sanidad", "educacion", "soberania", "direccion", "vivienda", "empleo",
             "idi", "dependencia", "discapacidad", "salud_mental", "diversidad",
             "turismo", "igualdad"]
YEARS = list(range(2015, 2027))
NOM = {"and": "Andalucía", "ara": "Aragón", "ast": "Asturias", "bal": "Baleares",
       "can": "Canarias", "cat": "Cataluña", "clm": "Cast.-La Mancha", "cnt": "Cantabria",
       "cym": "Cast. y León", "ext": "Extremadura", "gal": "Galicia", "lar": "La Rioja",
       "mad": "Madrid", "mur": "Murcia", "nav": "Navarra", "pvc": "País Vasco",
       "val": "C. Valenciana"}


def num(x):
    try:
        v = float(x)
        return v if v == v else 0.0
    except (TypeError, ValueError):
        return 0.0


# (ccaa,anio,concepto) -> importe
agg = defaultdict(float)
cells = set()
for r in csv.DictReader(open(STAG, newline="")):
    c, a = r["ccaa_id3"], int(r["anio"])
    cells.add((c, a))
    con = (r["concepto"] or "").strip()
    if con:
        agg[(c, a, con)] += num(r["importe_eur"])

ccaa = sorted(NOM)
# nº de años (de 12) con importe>0 por (ccaa, concepto)
years_cov = {(c, k): sum(1 for a in YEARS if agg.get((c, a, k), 0.0) > 0)
             for c in ccaa for k in CONCEPTOS}

# CSV: filas concepto, columnas CCAA
out_csv = ROOT / "outputs" / "cobertura_concepto_2026-07-10.csv"
with open(out_csv, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["concepto"] + ccaa + ["ccaa_con_dato", "total_celdas_con_dato_de_204"])
    for k in CONCEPTOS:
        row = [years_cov[(c, k)] for c in ccaa]
        ccaa_con = sum(1 for c in ccaa if years_cov[(c, k)] > 0)
        w.writerow([k] + row + [ccaa_con, sum(row)])

# MD
md = ["# Cobertura por concepto · capa autonómica — 2026-07-10", ""]
md.append("Nº de años (de 12: 2015-2026) con importe>0 por CCAA×concepto sobre el staging "
          "nominal completo (204 celdas). `12`=serie completa · `0`=nulo estructural en esa "
          "CCAA · valores intermedios = hueco puntual o entrada tardía en catálogo.")
md.append("")
md.append("| Concepto | " + " | ".join(ccaa) + " | ΣCCAA |")
md.append("|------|" + "|".join(["--:"] * (len(ccaa) + 1)) + "|")
for k in CONCEPTOS:
    vals = [years_cov[(c, k)] for c in ccaa]
    ccaa_con = sum(1 for v in vals if v > 0)
    md.append(f"| {k} | " + " | ".join(str(v) for v in vals) + f" | {ccaa_con}/17 |")
md.append("")

# Diagnóstico: nulos estructurales (0 años) y series completas
md.append("### Diagnóstico")
md.append("")
nulos = defaultdict(list)   # ccaa -> conceptos con 0 años
completos = defaultdict(list)
for c in ccaa:
    for k in CONCEPTOS:
        if years_cov[(c, k)] == 0:
            nulos[c].append(k)
        elif years_cov[(c, k)] == 12:
            completos[c].append(k)
md.append("**Nulos estructurales por CCAA** (concepto sin ningún año con dato — normalmente "
          "gasto fuera del catálogo funcional de esa comunidad, no un error de extracción):")
md.append("")
for c in ccaa:
    if nulos[c]:
        md.append(f"- **{NOM[c]}** ({c}): {', '.join(nulos[c])} "
                  f"— {len(completos[c])}/13 conceptos con serie completa.")
md.append("")
# conceptos más y menos cubiertos globalmente
por_concepto = sorted(((sum(1 for c in ccaa if years_cov[(c, k)] > 0), k) for k in CONCEPTOS))
peor = ", ".join(f"{k} ({n}/17)" for n, k in por_concepto[:4])
mejor = ", ".join(f"{k} ({n}/17)" for n, k in por_concepto[-4:][::-1])
md.append(f"**Conceptos más cubiertos** (CCAA con ≥1 año): {mejor}.")
md.append("")
md.append(f"**Conceptos con menos cobertura**: {peor}. Coinciden con partidas que muchas "
          "CCAA no desagregan como línea propia (salud mental suele ir dentro de sanidad; "
          "dependencia/discapacidad dentro de servicios sociales; diversidad/igualdad son "
          "programas pequeños o transversales).")
md.append("")
md.append("> **Sobre la conciliación §2.6 por-concepto:** no se ejecuta contra Hacienda "
          "porque la serie homogénea SGCIEF es económica (capítulos 1-9), no funcional; no "
          "existe subfunción sanidad/educación comparable. La conciliación §2.6 a nivel de "
          "TOTAL ya está superada (187/187 OK, 2026-07-09). Una conciliación funcional real "
          "requeriría la liquidación funcional del Ministerio (BDGEL/clasificación funcional), "
          "no publicada en el SGCIEF descargado.")

(ROOT / "outputs" / "cobertura_concepto_2026-07-10.md").write_text("\n".join(md))
print(f"OK celdas={len(cells)} · conceptos={len(CONCEPTOS)}")
print(f"  {out_csv}")
print(f"  {ROOT / 'outputs' / 'cobertura_concepto_2026-07-10.md'}")
