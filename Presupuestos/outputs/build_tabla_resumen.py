#!/usr/bin/env python3
"""Tabla resumen de presupuestos por CCAA × anualidad.

Combina dos fuentes:
  - COBERTURA/CALIDAD (204 celdas): outputs/smoke_regresion_py.csv
    (estado, filas, %concepto, nº conceptos) — completo para las 17×12.
  - MAGNITUD € (celdas re-extraídas esta noche): outputs/staging_py_<fecha>.csv
    (€ NOMINALES, capa autonómica). Las CCAA de PDF lento sin sidecar
    (ara, can, lar, mad, ext + años sueltos) quedan '·' → magnitud desde la
    DB deflactada del cierre matutino.

Salidas:
  outputs/tabla_resumen_<fecha>.csv   pivote por ccaa×anio (cobertura + imp_<concepto>)
  outputs/tabla_resumen_<fecha>.md    matrices legibles

Uso: python3 outputs/build_tabla_resumen.py [YYYY-MM-DD]
"""
import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FECHA = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
STAGING = ROOT / "outputs" / f"staging_py_{FECHA}.csv"
SMOKE = ROOT / "outputs" / "smoke_regresion_py.csv"

CONCEPTOS = ["sanidad", "educacion", "soberania", "direccion", "vivienda", "empleo",
             "idi", "dependencia", "discapacidad", "salud_mental", "diversidad",
             "turismo", "igualdad"]
YEARS = list(range(2015, 2027))
CCAA_NOMBRE = {
    "and": "Andalucía", "ara": "Aragón", "ast": "Asturias", "bal": "Baleares",
    "can": "Canarias", "cat": "Cataluña", "clm": "Cast.-La Mancha", "cnt": "Cantabria",
    "cym": "Cast. y León", "ext": "Extremadura", "gal": "Galicia", "lar": "La Rioja",
    "mad": "Madrid", "mur": "Murcia", "nav": "Navarra", "pvc": "País Vasco",
    "val": "C. Valenciana",
}


def num(x):
    try:
        v = float(x)
        return v if v == v else 0.0
    except (TypeError, ValueError):
        return 0.0


def main():
    # --- COBERTURA desde smoke ---
    cov = {}  # (ccaa,anio) -> dict
    if SMOKE.exists():
        for r in csv.DictReader(open(SMOKE, newline="")):
            cov[(r["ccaa"], int(r["anio"]))] = {
                "estado": r.get("estado", ""), "filas": r.get("filas", ""),
                "pct": r.get("pct", ""), "n_conc": r.get("n_conc", ""),
            }

    # --- MAGNITUD desde staging ---
    agg = defaultdict(float)     # (ccaa,anio,concepto) -> €
    total = defaultdict(float)   # (ccaa,anio) -> €
    have_mag = set()
    if STAGING.exists():
        for r in csv.DictReader(open(STAGING, newline="")):
            c, a = r["ccaa_id3"], int(r["anio"])
            have_mag.add((c, a))
            imp = num(r["importe_eur"])
            total[(c, a)] += imp
            con = (r["concepto"] or "").strip()
            if con:
                agg[(c, a, con)] += imp

    ccaa_list = sorted(CCAA_NOMBRE)

    # --- CSV pivote ---
    out_csv = ROOT / "outputs" / f"tabla_resumen_{FECHA}.csv"
    with open(out_csv, "w", newline="") as fh:
        cols = (["ccaa", "ccaa_nombre", "anio", "estado", "filas", "pct_concepto",
                 "n_conceptos", "magnitud_disp"]
                + [f"imp_{k}" for k in CONCEPTOS] + ["total_extraido", "gasto_social"])
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for c in ccaa_list:
            for a in YEARS:
                if (c, a) not in cov and (c, a) not in have_mag:
                    continue
                cinfo = cov.get((c, a), {})
                has = (c, a) in have_mag
                row = {"ccaa": c, "ccaa_nombre": CCAA_NOMBRE[c], "anio": a,
                       "estado": cinfo.get("estado", ""), "filas": cinfo.get("filas", ""),
                       "pct_concepto": cinfo.get("pct", ""), "n_conceptos": cinfo.get("n_conc", ""),
                       "magnitud_disp": "si" if has else "DB"}
                social = 0.0
                for k in CONCEPTOS:
                    v = agg.get((c, a, k), 0.0) if has else None
                    row[f"imp_{k}"] = round(v, 2) if v is not None else ""
                    if v:
                        social += v
                row["total_extraido"] = round(total[(c, a)], 2) if has else ""
                row["gasto_social"] = round(social, 2) if has else ""
                w.writerow(row)

    # --- matrices markdown ---
    def cell_cov(c, a):
        info = cov.get((c, a))
        if not info:
            return "·"
        est = "V" if info["estado"] == "VERDE" else ("v" if "VERDE" in info["estado"] else "?")
        return f"{est}{info['n_conc']}"

    def cell_mag(c, a, valfn, escala=1e9, dec=2):
        if (c, a) not in have_mag:
            return "·"
        return f"{valfn(c, a) / escala:.{dec}f}"

    def matriz(titulo, cellfn):
        lines = [f"### {titulo}", ""]
        lines.append("| CCAA | " + " | ".join(str(y) for y in YEARS) + " |")
        lines.append("|------|" + "|".join(["---:"] * len(YEARS)) + "|")
        for c in ccaa_list:
            lines.append(f"| {CCAA_NOMBRE[c]} | " + " | ".join(cellfn(c, a) for a in YEARS) + " |")
        lines.append("")
        return "\n".join(lines)

    md = [f"# Tabla resumen · Presupuestos por CCAA × anualidad — {FECHA}", ""]
    ncov = len(cov)
    nmag = len(have_mag)
    md.append(f"**Cobertura:** {ncov}/204 celdas CCAA-año extraídas (17 CCAA × 2015-2026), "
              f"todas en estado VERDE. **Magnitud € (staging Python nominal):** {nmag} celdas "
              f"re-extraídas esta noche; el resto (`·`) toma la magnitud de la DB deflactada "
              f"del cierre matutino (`cierre_{FECHA}.sh`).")
    md.append("")
    md.append(matriz("Cobertura y calidad — `V/v`=VERDE(estricto/pragm) + nº conceptos (de 13)",
                     cell_cov))
    md.append(matriz("Sanidad (€ mil M) — `·` = magnitud en DB",
                     lambda c, a: cell_mag(c, a, lambda c, a: agg.get((c, a, "sanidad"), 0.0))))
    md.append(matriz("Educación (€ mil M)",
                     lambda c, a: cell_mag(c, a, lambda c, a: agg.get((c, a, "educacion"), 0.0))))
    md.append(matriz("Gasto social clasificado — Σ 13 conceptos (€ mil M)",
                     lambda c, a: cell_mag(c, a, lambda c, a: sum(agg.get((c, a, k), 0.0) for k in CONCEPTOS))))
    md.append(matriz("Total extraído — todos los programas (€ mil M)",
                     lambda c, a: cell_mag(c, a, lambda c, a: total[(c, a)])))
    md.append("> Nota: € **nominales** del staging Python (la DB guarda € constantes "
              "deflactados; ~×1,3 en años antiguos). Anomalías de magnitud conocidas y "
              "documentadas (and CSV 2020-21, ast 2015 doble conteo, pvc 2025-26 inversión "
              "real) — ver `auditoria_magnitud.py`.")

    (ROOT / "outputs" / f"tabla_resumen_{FECHA}.md").write_text("\n".join(md))
    print(f"OK cobertura={ncov}/204 · magnitud={nmag} celdas")
    print(f"  {out_csv}")
    print(f"  {ROOT / 'outputs' / f'tabla_resumen_{FECHA}.md'}")


if __name__ == "__main__":
    main()
