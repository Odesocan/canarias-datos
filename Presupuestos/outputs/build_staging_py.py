#!/usr/bin/env python3
"""Staging consolidado (capa autonómica, € NOMINALES) corriendo extract+transform
de las CCAA-año del catálogo COMBOS, sin R/psql. RESUMABLE y con presupuesto de
tiempo por llamada (el sandbox Cowork corta bash a ~45s y no persiste procesos en
background, así que se ejecuta a trozos y cada llamada retoma donde quedó).

Triple propósito: (1) regresión de las verdes, (2) input de auditoria_magnitud,
(3) fuente de la tabla resumen por CCAA × anualidad.

Salidas (se reescriben acumulando en cada llamada):
  outputs/staging_py_<fecha>.csv     ccaa_id3,anio,concepto,importe_eur,codigo,denominacion
  outputs/staging_status_<fecha>.csv ccaa,anio,ok,filas,motor,error

Uso:
  python3 outputs/build_staging_py.py                    # sigue donde quedó, budget 38s
  python3 outputs/build_staging_py.py --only and,pvc     # solo esas CCAA
  python3 outputs/build_staging_py.py --budget 40        # segundos por llamada
"""
import argparse
import csv
import datetime as dt
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from smoke_regresion_py import COMBOS, RAW, EXTR  # noqa: E402

TODAY = dt.date.today().isoformat()
OUT_STAGING = ROOT / "outputs" / f"staging_py_{TODAY}.csv"
OUT_STATUS = ROOT / "outputs" / f"staging_status_{TODAY}.csv"

STAG_COLS = ["ccaa_id3", "anio", "concepto", "importe_eur", "codigo", "denominacion"]
STAT_COLS = ["ccaa", "anio", "ok", "filas", "motor", "error"]


def load_prev():
    rows, status = [], {}
    if OUT_STAGING.exists():
        rows = list(csv.DictReader(open(OUT_STAGING, newline="")))
    if OUT_STATUS.exists():
        for r in csv.DictReader(open(OUT_STATUS, newline="")):
            status[(r["ccaa"], int(r["anio"]))] = r
    return rows, status


def run_one(ccaa, anio, relpath):
    inp = RAW / relpath
    if not inp.exists():
        return {"ok": "False", "filas": 0, "motor": "", "error": f"raw missing: {relpath}"}, []
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tf:
        out = Path(tf.name)
    cmd = [sys.executable, "-m", "ccaa", "--ccaa", ccaa, "--anio", str(anio),
           "--input", str(inp), "--output", str(out)]
    try:
        p = subprocess.run(cmd, cwd=str(EXTR), capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        out.unlink(missing_ok=True)
        return {"ok": "False", "filas": 0, "motor": "", "error": "timeout>40s"}, []
    tail = (p.stdout + p.stderr).strip().splitlines()
    motor = ""
    for ln in tail:
        if "motor=" in ln:
            motor = ln.split("motor=", 1)[1].split()[0]
    rows = []
    if out.exists():
        for r in csv.DictReader(open(out, newline="")):
            rows.append({"ccaa_id3": r.get("ccaa_id3") or ccaa, "anio": r.get("anio") or anio,
                         "concepto": r.get("concepto") or "", "importe_eur": r.get("importe_eur") or "",
                         "codigo": r.get("codigo") or "", "denominacion": r.get("denominacion") or ""})
        out.unlink(missing_ok=True)
    ok = p.returncode == 0 and len(rows) >= 30
    err = "" if ok else (tail[-1] if tail else f"rc={p.returncode}")
    return {"ok": str(ok), "filas": len(rows), "motor": motor, "error": err}, rows


def write_all(all_rows, status):
    with open(OUT_STAGING, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=STAG_COLS)
        w.writeheader(); w.writerows(all_rows)
    with open(OUT_STATUS, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=STAT_COLS)
        w.writeheader()
        w.writerows(sorted(status.values(), key=lambda r: (r["ccaa"], int(r["anio"]))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="CCAA separadas por coma")
    ap.add_argument("--budget", type=float, default=38.0, help="segundos por llamada")
    ap.add_argument("--force", action="store_true", help="re-hacer aunque ya esté OK")
    args = ap.parse_args()

    only = set(x.strip() for x in args.only.split(",") if x.strip())
    all_rows, status = load_prev()

    combos = [(c, a, rel) for c in sorted(COMBOS) for a, rel in sorted(COMBOS[c].items())
              if not only or c in only]
    t0 = time.time()
    done_this = 0
    for ccaa, anio, rel in combos:
        key = (ccaa, anio)
        prev = status.get(key)
        if not args.force and prev is not None:
            # saltar si ya OK, o si falló de forma terminal (no reintentar hangs)
            err = prev.get("error", "")
            terminal = ("timeout" in err) or ("raw missing" in err) or ("deferred" in err) or ("hang" in err)
            if prev.get("ok") == "True" or terminal:
                continue
        if time.time() - t0 > args.budget:
            break
        st, rows = run_one(ccaa, anio, rel)
        # limpia filas viejas de este combo si re-run
        all_rows = [r for r in all_rows if not (r["ccaa_id3"] == ccaa and str(r["anio"]) == str(anio))]
        all_rows.extend(rows)
        status[key] = {"ccaa": ccaa, "anio": anio, **st}
        done_this += 1
        flag = "OK " if st["ok"] == "True" else "XX "
        print(f"{flag}{ccaa} {anio} filas={st['filas']:>4} {st['motor']} {st['error']}", flush=True)
        write_all(all_rows, status)  # persistir tras CADA combo (el sandbox corta a 45s)

    write_all(all_rows, status)
    nok = sum(1 for s in status.values() if s.get("ok") == "True")
    pending = sum(1 for c in COMBOS for a in COMBOS[c]
                  if (not only or c in only) and status.get((c, a), {}).get("ok") != "True")
    print(f"\nprocesadas_esta_llamada={done_this} · OK_acum={nok}/{len(combos)} · pendientes={pending} · filas={len(all_rows)}")


if __name__ == "__main__":
    main()
