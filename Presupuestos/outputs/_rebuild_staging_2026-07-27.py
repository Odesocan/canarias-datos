#!/usr/bin/env python3
"""Driver nocturno (sandbox, solo Python) para RE-EXTRAER todas las CCAA-anio
declaradas en COMBOS del smoke y volcar un staging fresco por partes.

Reutiliza COMBOS/RAW/EXTR de tools/smoke_regresion_py.py. Corre el dispatcher
`python3 -m ccaa` combo a combo, lee su salida y appenda las columnas del
staging (ccaa_id3, anio, concepto, importe_eur, codigo, denominacion) a
outputs/staging_parts/<ccaa>.csv. Idempotente por CCAA (reescribe su parte).

Uso:
  python3 outputs/_rebuild_staging_2026-07-27.py and ara ast   # subset CCAA
  python3 outputs/_rebuild_staging_2026-07-27.py --anios 2024,2025 pvc
  python3 outputs/_rebuild_staging_2026-07-27.py --concat      # une partes -> staging_py_<fecha>.csv
"""
import sys, os, csv, subprocess, tempfile, time, glob, datetime
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
from smoke_regresion_py import COMBOS, RAW, EXTR, CANON  # noqa

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "outputs" / "staging_parts"
PARTS.mkdir(exist_ok=True)
STAGING_FIELDS = ["ccaa_id3", "anio", "concepto", "importe_eur", "codigo", "denominacion"]


def run_combo(ccaa, anio, relpath):
    inp = RAW / relpath
    if not inp.exists():
        return None, dict(estado="SIN_RAW", filas=0, nconc=0, nota=f"no existe {relpath}")
    out = Path(tempfile.gettempdir()) / f"reb_{ccaa}_{anio}.csv"
    cmd = [sys.executable, "-m", "ccaa", "--ccaa", ccaa, "--anio", str(anio),
           "--input", str(inp), "--output", str(out)]
    try:
        p = subprocess.run(cmd, cwd=EXTR, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return None, dict(estado="TIMEOUT", filas=0, nconc=0, nota="timeout 120s")
    if not out.exists():
        err = (p.stderr.strip().splitlines() or [""])[-1]
        return None, dict(estado="ERROR", filas=0, nconc=0, nota=err[:120])
    rows = list(csv.DictReader(out.open(encoding="utf-8")))
    # localizar columnas (nombres canonicos del dispatcher)
    def col(r, *names):
        for n in names:
            for k in r:
                if k.strip().lower() == n:
                    return r.get(k)
        return ""
    staging_rows = []
    concs = set()
    for r in rows:
        con = (col(r, "concepto") or "").strip()
        if con and con.lower() in ("none", "nan", "null"):
            con = ""
        if con in CANON:
            concs.add(con)
        staging_rows.append({
            "ccaa_id3": ccaa, "anio": anio, "concepto": con,
            "importe_eur": col(r, "importe_eur", "importe"),
            "codigo": col(r, "codigo"),
            "denominacion": (col(r, "denominacion") or "").replace("\n", " ").strip(),
        })
    n = len(staging_rows)
    non_null = sum(1 for s in staging_rows if s["concepto"])
    pct = round(non_null / n * 100, 1) if n else 0.0
    est = "VERDE" if (n >= 30 and pct >= 80 and len(concs) >= 5) else \
          "VERDE_PRAGM" if (n >= 30 and len(concs) >= 5 and pct >= 35) else "ROJO"
    return staging_rows, dict(estado=est, filas=n, nconc=len(concs), pct=pct, nota="")


DEADLINE = [None]  # deadline global (epoch); se fija en __main__


def do_ccaa(ccaa, years=None, skip_existing=True):
    """Corre combos de una CCAA, escribiendo un fichero por combo
    staging_parts/<ccaa>_<anio>.csv (resumible). Respeta un deadline GLOBAL
    para no rebasar el cap de 45s del sandbox."""
    combos = COMBOS.get(ccaa, {})
    yrs = sorted(combos) if years is None else [y for y in sorted(combos) if y in years]
    for y in yrs:
        part = PARTS / f"{ccaa}_{y}.csv"
        if skip_existing and part.exists():
            continue
        if DEADLINE[0] and time.time() > DEADLINE[0]:
            print(f"  [deadline global alcanzado, corta antes de {ccaa}/{y}]", flush=True)
            return False
        t0 = time.time()
        rows, meta = run_combo(ccaa, y, combos[y])
        dt = time.time() - t0
        if rows is not None:
            with part.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=STAGING_FIELDS)
                w.writeheader(); w.writerows(rows)
        print(f"  {ccaa}/{y}: {meta['estado']:12s} filas={meta['filas']:4d} "
              f"nconc={meta['nconc']:2d} pct={meta.get('pct',0):5.1f} {dt:4.1f}s "
              f"{meta['nota']}", flush=True)
    return True


def concat():
    import collections
    fecha = datetime.date.today().isoformat()
    dest = ROOT / "outputs" / f"staging_py_{fecha}.csv"
    parts = sorted(PARTS.glob("*_*.csv"))
    total = 0
    seen = collections.Counter()
    with dest.open("w", newline="", encoding="utf-8") as out:
        w = csv.DictWriter(out, fieldnames=STAGING_FIELDS)
        w.writeheader()
        for pth in parts:
            c = pth.stem.rsplit("_", 1)[0]
            seen[c] += 1
            for r in csv.DictReader(pth.open(encoding="utf-8")):
                w.writerow(r); total += 1
    print(f"CONCAT -> {dest.name}: {total} filas, {len(parts)} combos, {len(seen)} CCAA")
    for c in sorted(seen):
        print(f"   {c}: {seen[c]} años")
    return dest


if __name__ == "__main__":
    args = sys.argv[1:]
    years = None
    rest = []
    i = 0
    deadline_s = 40.0
    while i < len(args):
        if args[i] == "--anios":
            years = set(int(x) for x in args[i + 1].split(","))
            i += 2
        elif args[i] == "--deadline":
            deadline_s = float(args[i + 1]); i += 2
        elif args[i] == "--concat":
            concat(); sys.exit(0)
        else:
            rest.append(args[i]); i += 1
    DEADLINE[0] = time.time() + deadline_s
    targets = rest if rest else sorted(COMBOS)
    for c in targets:
        if not do_ccaa(c, years):
            break
