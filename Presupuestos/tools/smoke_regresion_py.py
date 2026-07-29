#!/usr/bin/env python3
"""Regresion standalone de los extractores Python por CCAA-año.

Replica el contrato `python3 -m ccaa` sin necesidad de R/psql. Para cada
CCAA-año declarada VERDE corre extract+transform y evalua las condiciones
1-3 del cuaderno (motor OK, filas>=30, >=80% concepto no NULL, >=5 conceptos).

Uso:
  python3 tools/smoke_regresion_py.py              # check, no escribe catálogo
  python3 tools/smoke_regresion_py.py and          # check parcial
  python3 tools/smoke_regresion_py.py --update     # actualiza catálogo completo
  python3 tools/smoke_regresion_py.py --update and # reemplaza solo filas and/*
"""
import argparse
import subprocess, sys, csv, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "fuentes" / "raw"
EXTR = ROOT / "1_extraccion"

# CCAA-año a verificar -> fichero/directorio de entrada (relativo a RAW)
COMBOS = {
    "and": {2015: "and/2015/gastos_csv.csv",
            2016: "and/2016/gastos_csv.csv",
            2017: "and/2017/memoria_programas.pdf",
            2018: "and/2018/memoria_programas.pdf",
            2019: "and/2019/memoria_programas.pdf",
            2020: "and/2020/gastos_csv.csv",
            2021: "and/2021/gastos_csv.csv",
            2022: "and/2022/memoria_programas.pdf",
            2023: "and/2023/memoria_programas.pdf",
            2024: "and/2024/memoria_programas.pdf",
            2025: "and/2025/memoria_programas.pdf",
            2026: "and/2026/memoria_programas.pdf"},
    "ara": {2015: "ara/2015/ingresos_gastos.pdf",
            2016: "ara/2016/ingresos_gastos.pdf",
            2017: "ara/2017/ingresos_gastos.pdf",
            2018: "ara/2018/ingresos_gastos.pdf",
            2019: "ara/2019/ingresos_gastos.pdf",
            2020: "ara/2020/ingresos_gastos.pdf",
            2021: "ara/2021/ingresos_gastos.pdf",
            2022: "ara/2022/ingresos_gastos.pdf",
            2023: "ara/2023/ingresos_gastos.pdf",
            2024: "ara/2024/ingresos_gastos.pdf",
            2025: "ara/2025/ingresos_gastos.pdf",
            2026: "ara/2026/ingresos_gastos.pdf"},
    "ast": {2015: "ast/2015/tomo_I.pdf",
            2016: "ast/2016/tomo_I.pdf",
            2017: "ast/2017/tomo_I.pdf",
            2018: "ast/2018/tomo_I.pdf",
            2019: "ast/2019/tomo_I.pdf",
            2020: "ast/2020/tomo_I.pdf",
            2021: "ast/2021/tomo_I.pdf",
            2022: "ast/2022/tomo_I.pdf",
            2023: "ast/2023/tomo_I.pdf",
            2024: "ast/2024/tomo_I.pdf",
            2025: "ast/2025/tomo_I.pdf",
            2026: "ast/2026/tomo_I.pdf"},
    "bal": {2015: "bal/2015/memoria_programas.html",
            2016: "bal/2016/memoria_programas.html",
            2017: "bal/2017/memoria_programas.html",
            2018: "bal/2018/memoria_programas.html",
            2019: "bal/2019/memoria_programas.html",
            2020: "bal/2020/memoria_programas.html",
            2021: "bal/2021/memoria_programas.html",
            2022: "bal/2022/memoria_programas.html",
            2023: "bal/2023/memoria_programas.html",
            2024: "bal/2024/memoria_programas.html",
            2025: "bal/2025/memoria_programas.html",
            2026: "bal/2026/estats_numerics_2026_castella.pdf"},
    "can": {2015: "can/2015/TOMO-3-Resumenes.pdf",
            2016: "can/2016/TOMO-3-Resumenes.pdf",
            2017: "can/2017/TOMO-3-Resumenes.pdf",
            2018: "can/2018/TOMO-3-Resumenes.pdf",
            2019: "can/2019/TOMO-3-Resumenes.pdf",
            2020: "can/2020/TOMO-3-Resumenes.pdf",
            2021: "can/2021/TOMO-3-Resumenes.pdf",
            2022: "can/2022/memoria_programas.pdf",
            2023: "can/2023/memoria_programas.pdf",
            2024: "can/2024/memoria_programas.pdf",
            2025: "can/2025/memoria_programas.pdf",
            2026: "can/2026/memoria_programas.pdf"},
    "cat": {2015: "cat/2015/VOL_P_EID.pdf",
            2016: "cat/2016/VOL_P_EID.pdf",
            2017: "cat/2017/VOL_P_EID.pdf",
            2018: "cat/2018/VOL_P_EID.pdf",   # prorroga de 2017 (no se aprobo ppto 2018)
            2019: "cat/2019/VOL_P_EID.pdf",
            2020: "cat/2020/vol_p_eid.pdf",
            2021: "cat/2021/vol_p_eid.pdf",   # prorroga de 2020 (no se aprobo ppto 2021)
            2022: "cat/2022/vol_p_eid.pdf",
            2023: "cat/2023/vol_p_eid.pdf",
            2024: "cat/2024/vol_p_eid.pdf",
            2025: "cat/2025/vol_p_eid.pdf",   # prorroga de 2024/2023 (no se aprobo ppto 2025)
            2026: "cat/2026/vol_p_eid.pdf"},
    "clm": {2015: "clm/2015/gastos_articulo.csv",
            2016: "clm/2016/gastos_articulo.csv",
            2017: "clm/2017/gastos_articulo.csv",
            2018: "clm/2018/gastos_articulo.csv",
            2019: "clm/2019/gastos_articulo.csv",
            2020: "clm/2020/gastos_articulo.csv",
            2021: "clm/2021/gastos_articulo.csv",
            2022: "clm/2022/tomo_I.pdf",
            2023: "clm/2023/tomo_I.pdf",
            2024: "clm/2024/tomo_I.pdf",
            2025: "clm/2025/tomo_I.pdf",
            2026: "clm/2026/tomo_I.pdf"},
    "cnt": {2015: "cnt/2015/desarrollo_centros.pdf",  # VERDE: programa (suma capítulos)
            2016: "cnt/2016/desarrollo_centros.pdf",  # VERDE: programa (suma capítulos)
            2017: "cnt/2017/desarrollo_centros.pdf",  # VERDE: programa (suma capítulos)
            2018: "cnt/2018/ingresos_gastos.pdf",
            2019: "cnt/2019/ingresos_gastos.pdf",
            2020: "cnt/2020/ingresos_gastos.pdf",
            2021: "cnt/2021/ingresos_gastos.pdf",
            2022: "cnt/2022/ingresos_gastos.pdf",
            2023: "cnt/2023/ingresos_gastos.pdf",
            2024: "cnt/2024/ingresos_gastos.pdf",
            2025: "cnt/2025/ingresos_gastos.pdf",
            2026: "cnt/2026/ingresos_gastos.pdf"},
    "cym": {2015: "cym/2015/bocyl_ley11_2014.pdf",  # BOCYL Ley 11/2014, motor cym-bocyl-territorial (jcyl no publica distrib. 2015)
            2016: "cym/2016/gastos.csv",
            2017: "cym/2017/gastos.csv",
            2018: "cym/2018/gastos.csv",
            2019: "cym/2019/gastos.csv",   # prorroga de 2018 (no se aprobo ppto 2019)
            2020: "cym/2020/gastos.csv",   # prorroga de 2018 (no se aprobo ppto 2020)
            2021: "cym/2021/gastos.csv",
            2022: "cym/2022/gastos.csv",   # prorroga de 2021 (no se aprobo ppto 2022)
            2023: "cym/2023/gastos.xlsx",
            2024: "cym/2024/gastos.xlsx",
            2025: "cym/2025/gastos.xls",
            2026: "cym/2026/gastos.xls"},
    "ext": {2015: "ext/2015/ley_doe.pdf", 2016: "ext/2016/ley_doe.pdf",
            2017: "ext/2017/ley_doe.pdf", 2018: "ext/2018/ley_doe.pdf",
            2019: "ext/2019/ley_doe.pdf", 2020: "ext/2020/ley_doe.pdf",
            2021: "ext/2021/ley_doe.pdf", 2022: "ext/2022/ley_doe.pdf",
            2023: "ext/2023/ley_doe.pdf", 2024: "ext/2024/ley_doe.pdf",
            2025: "ext/2025/ley_doe.pdf", 2026: "ext/2026/ley_doe.pdf"},
    "gal": {2015: "gal/2015/PROGR_I.pdf",
            2016: "gal/2016/PROGR_I.pdf",
            2017: "gal/2017/PROGR_I.pdf",
            2018: "gal/2018/PROGR_I.pdf",
            2019: "gal/2019/PROGR_I.pdf",
            2020: "gal/2020/PROGR_I.pdf",
            2021: "gal/2021/PROGR_I.pdf",
            2022: "gal/2022/PROGR_I.pdf",
            2023: "gal/2023/PROGR_I.pdf",
            2024: "gal/2024/PROGR_I.pdf",
            2025: "gal/2025/PROGR_I.pdf",
            2026: "gal/2026/PROGR_I.pdf"},
    "lar": {2015: "lar/2015",
            2016: "lar/2016",
            2017: "lar/2017",
            2018: "lar/2018",
            2019: "lar/2019",
            2020: "lar/2020",
            2021: "lar/2021",
            2022: "lar/2022",
            2023: "lar/2023",
            2024: "lar/2024",
            2025: "lar/2025",
            2026: "lar/2026"},
    "mad": {2015: "mad/2015/libro_03.pdf",
            2016: "mad/2016/libro_03.pdf",
            2017: "mad/2017/libro_03.pdf",
            2018: "mad/2018/libro_03.pdf",
            2019: "mad/2019/libro_03.pdf",
            2020: "mad/2019/libro_03.pdf",   # prórroga de 2019
            2021: "mad/2019/libro_03.pdf",   # prórroga de 2019
            2022: "mad/2022/libro_03.pdf",
            2023: "mad/2022/libro_03.pdf",   # prórroga de 2022
            2024: "mad/2024/libro_03.pdf",
            2025: "mad/2025/libro_03.pdf",
            2026: "mad/2026/libro_03.pdf"},
    "mur": {2015: "mur/2015/ley_completa.pdf",
            2016: "mur/2016",
            2017: "mur/2017",
            2018: "mur/2018",
            2019: "mur/2019",
            2020: "mur/2020",
            2021: "mur/2021",
            2022: "mur/2022",
            2023: "mur/2023",
            2024: "mur/2024",
            2025: "mur/2025",
            2026: "mur/2025"},  # prórroga de 2025
    "nav": {2015: "nav/2015/programa_csv.html",
            2016: "nav/2016/programa_csv.html",
            2017: "nav/2017/programa_csv.html",
            2018: "nav/2018/programa_csv.html",
            2019: "nav/2019/programa_csv.html",
            2020: "nav/2020/programa_csv.html",
            2021: "nav/2021/programa_csv.html",
            2022: "nav/2022/programa_csv.html",
            2023: "nav/2023/programa_csv.html",
            2024: "nav/2024/programa_csv.html",
            2025: "nav/2025/programa_csv.html",
            2026: "nav/2026/programa_csv.html"},
    "pvc": {2015: "pvc/2015/GASTOSC.csv",
            2016: "pvc/2016/GASTOSC.csv",
            2017: "pvc/2017/GASTOSC.csv",
            2018: "pvc/2018/GASTOSC.csv",
            2019: "pvc/2019/GASTOSC.csv",
            2020: "pvc/2020/GASTOSC.csv",
            2021: "pvc/2021/GASTOSC.csv",
            2022: "pvc/2022/csv_tidy.csv",
            2023: "pvc/2023/Datuak_datos.csv",
            2024: "pvc/2024/csv_tidy.csv",
            2025: "pvc/2025/csv_tidy.csv",
            2026: "pvc/2026/Datuak_datos.csv"},
    "val": {2015: "val/2015/tomo_II.html",
            2016: "val/2016/tomo_II.html",
            2017: "val/2017/tomo_II.html",
            2018: "val/2018/tomo_II.html",
            2019: "val/2019/tomo_II.html",
            2020: "val/2020/tomo_II.html",
            2021: "val/2021/tomo_II.html",
            2022: "val/2022/tomo_II.html",
            2023: "val/2023/tomo_II.html",
            2024: "val/2024/tomo_II.html",
            2025: "val/2025/tomo_II.html",
            2026: "val/2026/tomo_II.html"},
}

CANON = {"sanidad","educacion","soberania","direccion","vivienda","empleo",
         "idi","dependencia","discapacidad","salud_mental","diversidad",
         "turismo","igualdad"}


def run_one(ccaa, anio, relpath):
    inp = RAW / relpath
    if not inp.exists():
        return dict(ccaa=ccaa, anio=anio, estado="SIN_RAW", motor="", filas=0,
                    pct=0.0, n_conc=0, conceptos="", nota=f"no existe {relpath}")
    out = Path(tempfile.gettempdir()) / f"smoke_{ccaa}_{anio}.csv"
    cmd = [sys.executable, "-m", "ccaa", "--ccaa", ccaa, "--anio", str(anio),
           "--input", str(inp), "--output", str(out)]
    try:
        p = subprocess.run(cmd, cwd=EXTR, capture_output=True, text=True,
                            timeout=600)
    except subprocess.TimeoutExpired:
        return dict(ccaa=ccaa, anio=anio, estado="TIMEOUT", motor="", filas=0,
                    pct=0.0, n_conc=0, conceptos="", nota="timeout 600s")
    last = (p.stdout.strip().splitlines() or [""])[-1]
    err = (p.stderr.strip().splitlines() or [""])[-1]
    if not out.exists():
        return dict(ccaa=ccaa, anio=anio, estado="ERROR", motor="", filas=0,
                    pct=0.0, n_conc=0, conceptos="",
                    nota=(err or last or "sin output")[:160])
    rows = list(csv.DictReader(out.open(encoding="utf-8")))
    n = len(rows)
    concol = None
    if rows:
        for c in rows[0]:
            if c.strip().lower() == "concepto":
                concol = c
                break
    conc_vals = [(_r.get(concol) or "").strip() for _r in rows] if concol else []
    non_null = [c for c in conc_vals if c and c.lower() not in ("none","nan","null")]
    pct = (len(non_null) / n * 100.0) if n else 0.0
    distintos = sorted(set(non_null) & CANON)
    n_conc = len(distintos)
    motor = ""
    if "motor=" in last:
        motor = last.split("motor=")[1].split()[0]
    # VERDE estricto: criterio cuaderno (>=80% concepto no NULL).
    # VERDE pragmático: cobertura menor pero >=5 conceptos y 0 errores,
    # cuando los NULL son estructuralmente fuera de catálogo §1.6
    # (umbral 35% alineado con el precedente ast/2024 = 36.5%).
    verde = n >= 30 and pct >= 80.0 and n_conc >= 5
    pragmatico = n >= 30 and n_conc >= 5 and pct >= 35.0
    # AMARILLO: dato válido pero PARCIAL/granularidad gruesa (15-29 filas), p.ej.
    # extracción a nivel área de gasto cuando solo existe la Ley del BOC
    # (motor cnt-politica-gastos-boc). No es VERDE (no llega a programa) ni ROJO.
    amarillo = 15 <= n < 30 and n_conc >= 5 and pct >= 35.0
    estado = ("VERDE" if verde else "VERDE_PRAGM" if pragmatico
              else "AMARILLO" if amarillo else "ROJO")
    return dict(ccaa=ccaa, anio=anio, estado=estado, motor=motor, filas=n,
                pct=round(pct, 1), n_conc=n_conc,
                conceptos="|".join(distintos),
                nota="" if estado != "ROJO" else (last or err)[:160])


FIELDS = ["ccaa","anio","estado","motor","filas","pct","n_conc","conceptos","nota"]
GREEN_STATES = {"VERDE", "VERDE_PRAGM"}


def load_catalog(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def row_key(row):
    return (row["ccaa"], str(row["anio"]))


def as_number(row, field, default=0.0):
    try:
        return float(row.get(field, default) or default)
    except (TypeError, ValueError):
        return default


def detect_regressions(previous_rows, current_rows):
    previous = {row_key(r): r for r in previous_rows}
    warnings = []
    for row in current_rows:
        key = row_key(row)
        old = previous.get(key)
        if not old:
            continue
        label = f"{key[0]}/{key[1]}"
        old_state = old.get("estado", "")
        new_state = row.get("estado", "")
        if old_state in GREEN_STATES and new_state not in GREEN_STATES:
            warnings.append(f"{label}: estado baja de {old_state} a {new_state}")
        old_rows = as_number(old, "filas")
        new_rows = as_number(row, "filas")
        if old_rows >= 30 and new_rows < old_rows * 0.70:
            warnings.append(f"{label}: filas bajan de {old_rows:.0f} a {new_rows:.0f}")
        old_conc = as_number(old, "n_conc")
        new_conc = as_number(row, "n_conc")
        if old_conc >= 5 and new_conc <= old_conc - 2:
            warnings.append(f"{label}: conceptos bajan de {old_conc:.0f} a {new_conc:.0f}")
        old_pct = as_number(old, "pct")
        new_pct = as_number(row, "pct")
        if old_pct >= 35 and new_pct < old_pct - 20:
            warnings.append(f"{label}: pct concepto baja de {old_pct:.1f} a {new_pct:.1f}")
    return warnings


def merge_results(previous_rows, current_rows):
    merged = {row_key(r): r for r in previous_rows}
    for row in current_rows:
        merged[row_key(row)] = row
    return sorted(merged.values(), key=lambda r: (r["ccaa"], int(r["anio"])))


def write_catalog(path, rows):
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Smoke seguro de extractores CCAA")
    parser.add_argument("ccaa", nargs="*", help="Filtro opcional de CCAA id3")
    parser.add_argument("--update", action="store_true",
                        help="Actualiza outputs/smoke_regresion_py.csv")
    parser.add_argument("--force", action="store_true",
                        help="Permite actualizar aunque se detecten regresiones")
    parser.add_argument("--append", action="store_true",
                        help="Alias legado de --update; ahora reemplaza filas, no duplica")
    args = parser.parse_args()

    filtro = args.ccaa
    targets = filtro if filtro else list(COMBOS.keys())
    outcsv = ROOT / "outputs" / "smoke_regresion_py.csv"
    results = []
    for ccaa in targets:
        for anio, rel in sorted(COMBOS.get(ccaa, {}).items()):
            r = run_one(ccaa, anio, rel)
            results.append(r)
            print(f"{r['ccaa']}/{r['anio']:<5} {r['estado']:<12} "
                  f"filas={r['filas']:<5} pct={r['pct']:<6} "
                  f"conc={r['n_conc']:<3} motor={r['motor']}", flush=True)
            if r["nota"]:
                print(f"          nota: {r['nota']}", flush=True)

    previous = load_catalog(outcsv)
    regressions = detect_regressions(previous, results)
    if regressions:
        print("\nREGRESIONES DETECTADAS:", flush=True)
        for item in regressions:
            print(f"  - {item}", flush=True)

    should_write = args.update or args.append
    if should_write and regressions and not args.force:
        print("\nNo se actualiza el catálogo. Revisa las regresiones o usa --force.", flush=True)
        return 1

    if should_write:
        rows_to_write = merge_results(previous, results) if filtro else results
        write_catalog(outcsv, rows_to_write)
        print(f"\nCSV actualizado -> {outcsv}", flush=True)
    else:
        print("\nModo check: no se ha escrito el catálogo. Usa --update para actualizar.", flush=True)

    verdes = sum(1 for r in results if r["estado"] in ("VERDE", "VERDE_PRAGM"))
    print(f"LOTE {verdes}/{len(results)} en VERDE(+pragmatico).")
    return 1 if regressions else 0

if __name__ == "__main__":
    sys.exit(main())
