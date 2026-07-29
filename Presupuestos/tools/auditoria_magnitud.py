#!/usr/bin/env python3
"""
Auditoría de magnitud — evaluador POST-EXTRACCIÓN.

El smoke (`tools/smoke_regresion_py.py`) certifica la EXTRACCIÓN (filas ≥30,
%concepto, nº conceptos). Pero un extractor puede estar VERDE y devolver el gasto
al doble, a la mitad o en ~0 si el documento cambió de estructura y el patrón fijo
no se adaptó (lección 2026-07-01: Aragón salió VERDE 12/12 con la sanidad ~2x
durante 12 años sin que nadie lo viera). Este evaluador cubre ese hueco con dos
tests de MAGNITUD:

  · Test 1 — CONTINUIDAD: salto de sanidad o total año-a-año > ±40%. Delata un
    fallo estructural en un año CONCRETO (cambio de formato no manejado; p.ej.
    Andalucía recodificó la transferencia al SAS de 41H a 12S y 2024 cayó a ~0).
    Los cambios de método documentados (SEAMS) se marcan como esperados, no error.

  · Test 2 — PLAUSIBILIDAD: sanidad €/habitante fuera de banda. Delata un error
    SOSTENIDO en toda la serie (doble conteo o infra-extracción) que la continuidad
    NO ve porque no hay salto. Banda por defecto 900-2300 €/hab (España ~1600-1800).

Datos: agrega `1_extraccion/staging_gasto.rds` vía Rscript (capa autonómica). Con
`--csv <ruta>` lee un CSV con columnas ccaa_id3,anio,concepto,importe_eur en su lugar.

Uso:
  python3 tools/auditoria_magnitud.py                 # todas las CCAA
  python3 tools/auditoria_magnitud.py ara pvc         # solo esas
  python3 tools/auditoria_magnitud.py --baseline      # tabla sanidad €/hab por CCAA-año
  python3 tools/auditoria_magnitud.py --csv /tmp/x.csv

Código de salida: 0 si no hay anomalías; 1 si hay (para usarlo como gate en el cierre).
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING_RDS = ROOT / "1_extraccion" / "staging_gasto.rds"

# Población INE ~2022 (millones). Ajustable; sólo se usa para el per cápita.
POBLACION = {
    "and": 8.47, "ara": 1.33, "ast": 1.01, "bal": 1.18, "can": 2.24, "cat": 7.79,
    "clm": 2.05, "cnt": 0.58, "cym": 2.38, "ext": 1.06, "gal": 2.70, "lar": 0.32,
    "mad": 6.79, "mur": 1.53, "nav": 0.67, "pvc": 2.21, "val": 5.06,
}
NOMBRE = {
    "and": "Andalucía", "ara": "Aragón", "ast": "Asturias", "bal": "Baleares",
    "can": "Canarias", "cat": "Cataluña", "clm": "Cast-La Mancha", "cnt": "Cantabria",
    "cym": "Cast. y León", "ext": "Extremadura", "gal": "Galicia", "lar": "La Rioja",
    "mad": "Madrid", "mur": "Murcia", "nav": "Navarra", "pvc": "País Vasco",
    "val": "C. Valenciana",
}

# Banda plausible de sanidad €/hab (España ~1600-1800). Fuera de aquí = sospecha.
BANDA_SANIDAD = (900, 2300)
# Umbral de salto año-a-año (ratio). Fuera de [0.70, 1.43] ≈ ±40%.
SALTO_MIN, SALTO_MAX = 0.70, 1.43
# Test 3 (por concepto): umbral más laxo (±60% ≈ [0.625, 1.60]) y tamaño mínimo
# del concepto para evitar ruido de conceptos pequeños. Un concepto individual es
# más volátil que sanidad/total, pero un salto >60% en un concepto ≥20 M€ suele
# ser un fallo de mapeo (keyword rota, first-wins, rename), no crecimiento real.
SALTO_CONC_MIN, SALTO_CONC_MAX = 0.625, 1.60
CONC_MIN_EUR = 20e6

# SEAMS = cambios de método/fuente DOCUMENTADOS entre dos años: un salto ahí es
# esperado (no un fallo). Formato: ccaa -> set de años "destino" del cambio.
SEAMS = {
    # and RETIRADO (FIX 2026-07-16): la rama CSV ahora consolida el perímetro
    # (filtro CENTRO GESTOR consejería "00") y la serie CSV↔PDF es continua
    # sin salto; mantener el seam solo enmascararía regresiones futuras.
    "clm": {2022},               # CSV gastosf (2015-21) → PDF tomo I (2022-26)
    "gal": {2022},               # PDF regla C (2015-21) → CSV abertos (2022-26)
    "pvc": {2022},               # ZIP GASTOSC (2015-21) → CSV tidy (2022-26)
    "lar": {2019},               # resumen-programas → funcional-economico
}


def _aggregate_from_rds() -> list[dict]:
    """Agrega el staging (capa autonómica) por (ccaa, anio, concepto) vía Rscript."""
    if not STAGING_RDS.exists():
        sys.exit(f"ERROR: no existe {STAGING_RDS}. Corre la extracción antes.")
    out = Path(tempfile.gettempdir()) / "auditoria_magnitud_agg.csv"
    r_code = f'''
st <- readRDS("{STAGING_RDS.as_posix()}")
if ("capa" %in% names(st)) st <- st[is.na(st$capa) | st$capa != "hacienda", ]
st$concepto[is.na(st$concepto)] <- ""
ag <- aggregate(importe_eur ~ ccaa_id3 + anio + concepto, st,
                function(x) sum(x, na.rm = TRUE))
nf <- aggregate(importe_eur ~ ccaa_id3 + anio, st, length)
names(nf)[3] <- "nfilas_total"
m <- merge(ag, nf, by = c("ccaa_id3", "anio"), all.x = TRUE)
write.csv(m, "{out.as_posix()}", row.names = FALSE)
'''
    try:
        subprocess.run(["Rscript", "-e", r_code], check=True,
                       capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit("ERROR: Rscript no disponible. Usa --csv con un export del staging.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"ERROR al leer el staging con R:\n{e.stderr[-800:]}")
    return list(csv.DictReader(out.open()))


def _load_csv(path: str) -> list[dict]:
    return list(csv.DictReader(Path(path).open()))


def _metrics(rows: list[dict]) -> dict:
    """(ccaa, anio) -> {total, san, edu, nconc, nfilas, por_concepto}."""
    m: dict = defaultdict(lambda: {"total": 0.0, "san": 0.0, "edu": 0.0,
                                    "conc": set(), "nfilas": 0,
                                    "por_concepto": defaultdict(float)})
    for r in rows:
        ccaa, anio = r["ccaa_id3"], int(r["anio"])
        con = (r.get("concepto") or "").strip()
        try:
            imp = float(r["importe_eur"])
        except (ValueError, KeyError):
            imp = 0.0
        cell = m[(ccaa, anio)]
        cell["total"] += imp
        if con == "sanidad":
            cell["san"] += imp
        if con == "educacion":
            cell["edu"] += imp
        if con:
            cell["conc"].add(con)
            cell["por_concepto"][con] += imp
        if "nfilas_total" in r:
            cell["nfilas"] = int(float(r["nfilas_total"]))
    return m


def auditar(rows: list[dict], filtro: list[str] | None) -> int:
    m = _metrics(rows)
    ccaas = sorted({k[0] for k in m} if not filtro else set(filtro),
                   key=lambda c: NOMBRE.get(c, c))
    anomalias = 0

    print("== TEST 2 · PLAUSIBILIDAD (sanidad €/hab; banda %d-%d) ==" % BANDA_SANIDAD)
    for c in ccaas:
        pob = POBLACION.get(c)
        fuera = []
        años = sorted(y for (cc, y) in m if cc == c)
        for y in años:
            san = m[(c, y)]["san"]
            if san <= 0 or not pob:
                continue
            pc = san / (pob * 1e6)
            if pc < BANDA_SANIDAD[0] or pc > BANDA_SANIDAD[1]:
                fuera.append((y, pc))
        if fuera:
            anomalias += len(fuera)
            direc = "ALTO→doble conteo" if fuera[len(fuera) // 2][1] > 2300 else "BAJO→infra-extracción"
            det = " ".join(f"{y}:{pc:.0f}" for y, pc in fuera[:8])
            marca = "  ⚠️ SOSTENIDO" if len(fuera) >= max(1, len(años) // 2) else ""
            print(f"  {NOMBRE.get(c, c):14} {len(fuera)}/{len(años)} fuera ({direc}){marca}: {det}")

    print("\n== TEST 1 · CONTINUIDAD (salto sanidad/total año-a-año > ±40%) ==")
    for c in ccaas:
        años = sorted(y for (cc, y) in m if cc == c)
        flags = []
        for i in range(1, len(años)):
            a, b = años[i - 1], años[i]
            seam = b in SEAMS.get(c, set())
            for etq, key in (("san", "san"), ("tot", "total")):
                va, vb = m[(c, a)][key], m[(c, b)][key]
                if va > 1e8 and vb > 1e8:
                    r = vb / va
                    if r < SALTO_MIN or r > SALTO_MAX:
                        flags.append(f"{a}→{b} {etq}×{r:.2f}" + (" [seam ok]" if seam else ""))
                elif va > 1e8 and vb <= 1e8:
                    flags.append(f"{a}→{b} {etq}¡a~0!" + (" [seam ok]" if seam else ""))
                elif vb > 1e8 and va <= 1e8:
                    flags.append(f"{a}→{b} {etq}¡de~0!" + (" [seam ok]" if seam else ""))
        reales = [f for f in flags if "[seam ok]" not in f]
        if flags:
            anomalias += len(reales)
            print(f"  {NOMBRE.get(c, c):14} " + " | ".join(flags))

    # TEST 3 · CONTINUIDAD POR CONCEPTO. Un extractor puede tener sanidad/total
    # continuos (test 1) y aun así romper un concepto concreto: keyword que deja
    # de casar por una abreviatura (ara "EDUC SECUNDARIA" 2020), first-wins que
    # trunca (cat), rename que descoloca (clm "324A" 2024). Se vigila cada
    # concepto material (≥ CONC_MIN_EUR) año-a-año con un umbral más laxo que
    # sanidad (±60 %), ignorando apariciones/desapariciones limpias (0↔valor, que
    # suelen ser cambios de método/estructura) y los seams documentados.
    print("\n== TEST 3 · CONTINUIDAD POR CONCEPTO (AVISO, no bloquea; salto > ±%d%% "
          "en concepto ≥ %d M€) ==" % (int((SALTO_CONC_MAX - 1) * 100),
                                        int(CONC_MIN_EUR / 1e6)))
    avisos = 0
    hubo3 = False
    for c in ccaas:
        años = sorted(y for (cc, y) in m if cc == c)
        flags = []
        for i in range(1, len(años)):
            a, b = años[i - 1], años[i]
            if b != a + 1:
                continue  # años no consecutivos: el hueco amplifica el salto (ruido)
            if b in SEAMS.get(c, set()):
                continue  # seam de método documentado: los conceptos pueden saltar
            pa = m[(c, a)]["por_concepto"]
            pb = m[(c, b)]["por_concepto"]
            for con in set(pa) | set(pb):
                va, vb = pa.get(con, 0.0), pb.get(con, 0.0)
                if va < CONC_MIN_EUR and vb < CONC_MIN_EUR:
                    continue  # concepto menor en ambos años → ruido
                if va <= 0 or vb <= 0:
                    continue  # aparición/desaparición: no es un salto de continuidad
                r = vb / va
                if r < SALTO_CONC_MIN or r > SALTO_CONC_MAX:
                    flags.append(f"{a}→{b} {con}×{r:.2f}")
        if flags:
            hubo3 = True
            avisos += len(flags)
            print(f"  {NOMBRE.get(c, c):14} " + " | ".join(flags[:6])
                  + (f"  (+{len(flags) - 6} más)" if len(flags) > 6 else ""))
    if not hubo3:
        print("   Sin saltos por concepto. ✓")
    elif avisos:
        print(f"   ({avisos} avisos — revísalos; NO cuentan como anomalía bloqueante)")

    print(f"\n== RESULTADO: {anomalias} anomalías (excl. seams documentados) ==")
    if anomalias == 0:
        print("   Sin anomalías de magnitud. ✓")
    return 1 if anomalias else 0


def imprimir_baseline(rows: list[dict], filtro: list[str] | None):
    m = _metrics(rows)
    ccaas = sorted({k[0] for k in m} if not filtro else set(filtro),
                   key=lambda c: NOMBRE.get(c, c))
    years = list(range(2015, 2027))
    print("SANIDAD €/hab por CCAA-año (baseline; guarda este número: si una "
          "re-extracción se desvía, el formato de ese año cambió)\n")
    print("CCAA".ljust(14) + " " + " ".join(str(y)[2:].rjust(5) for y in years))
    for c in ccaas:
        pob = POBLACION.get(c)
        cells = []
        for y in years:
            san = m.get((c, y), {}).get("san", 0.0)
            if san > 0 and pob:
                cells.append(f"{san / (pob * 1e6):.0f}".rjust(5))
            else:
                cells.append("    ·")
        print(f"{NOMBRE.get(c, c):14} " + " ".join(cells))


def main():
    ap = argparse.ArgumentParser(description="Auditoría de magnitud post-extracción")
    ap.add_argument("ccaa", nargs="*", help="filtro de id3 (vacío = todas)")
    ap.add_argument("--csv", help="CSV alternativo (ccaa_id3,anio,concepto,importe_eur)")
    ap.add_argument("--baseline", action="store_true", help="imprime baseline €/hab y sale")
    args = ap.parse_args()
    rows = _load_csv(args.csv) if args.csv else _aggregate_from_rds()
    filtro = args.ccaa or None
    if args.baseline:
        imprimir_baseline(rows, filtro)
        return
    sys.exit(auditar(rows, filtro))


if __name__ == "__main__":
    main()
