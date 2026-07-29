#!/usr/bin/env python3
"""
tools/sgcief_per_ccaa_download.py — Descarga vía Playwright los XLSX
per-CCAA de SGCIEF (Hacienda) para los años indicados.

Mecánica real (validada via probe 2026-05-19 en SelDescargaDC.aspx):
  1. GET inicio.aspx (ASP.NET ViewState).
  2. Click en link "../aspx/SelDescargaDC.aspx".
  3. Formulario con tres selects + botón imagen:
       select #MainContent_ano             (value = '2024')
       select #MainContent_autonomia       (value = '01' .. '19')
       select #MainContent_tipoDescarga    (default = Ingresos y Gastos
                                            por capítulos)
       input#MainContent_botonAceptar      (type=image)
  4. Aceptar dispara la descarga del XLSX.

Salida: fuentes/raw/hacienda/<anio>/per_ccaa/SGCIEF_<anio>_<id3>.xlsx
"""
from __future__ import annotations
import argparse, sys, time
from pathlib import Path

# id3 → código autonomía SGCIEF (los códigos del dropdown del portal).
CCAA_CODES = {
    "and": "01",
    "ara": "02",
    "ast": "03",
    "bal": "04",
    "can": "05",
    "cnt": "06",
    "cym": "07",  # Castilla-León
    "clm": "08",  # Castilla-Mancha
    "cat": "09",
    "ext": "10",
    "gal": "11",
    "mad": "12",
    "mur": "13",
    "nav": "14",
    "pvc": "15",
    "lar": "16",
    "val": "17",
}

PROJECT_ROOT = Path(__file__).resolve().parents[1]
URL_INICIO = (
    "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/"
    "PublicacionPresupuestos/aspx/inicio.aspx"
)


def open_descarga(page) -> bool:
    """inicio.aspx + click en 'Descargar Datos Consolidados'."""
    try:
        page.goto(URL_INICIO, wait_until="domcontentloaded", timeout=60_000)
        page.click("a[href*='SelDescargaDC.aspx']", timeout=10_000)
        page.wait_for_load_state("networkidle", timeout=20_000)
        return True
    except Exception as e:
        print(f"    [WARN] no se pudo abrir SelDescargaDC: {e}", file=sys.stderr)
        return False


def download_one(page, anio: int, id3: str, out_path: Path) -> bool:
    """Descarga un XLSX (anio, id3). True si OK; False si error."""
    if not open_descarga(page):
        return False

    code = CCAA_CODES[id3]
    try:
        page.select_option("#MainContent_ano", str(anio))
        page.wait_for_load_state("networkidle", timeout=10_000)
    except Exception as e:
        print(f"    [WARN] select año {anio}: {e}", file=sys.stderr)
        return False

    try:
        page.select_option("#MainContent_autonomia", code)
        page.wait_for_load_state("networkidle", timeout=10_000)
    except Exception as e:
        print(f"    [WARN] select autonomia {id3}/{code}: {e}", file=sys.stderr)
        return False

    try:
        with page.expect_download(timeout=90_000) as dlinfo:
            page.click("#MainContent_botonAceptar")
        download = dlinfo.value
        out_path.parent.mkdir(parents=True, exist_ok=True)
        download.save_as(str(out_path))
        return out_path.exists() and out_path.stat().st_size > 4_000
    except Exception as e:
        print(f"    [WARN] descarga {anio}/{id3}: {e}", file=sys.stderr)
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--anios", nargs="+", type=int, required=True)
    ap.add_argument("--ccaa", nargs="*", default=list(CCAA_CODES.keys()))
    ap.add_argument("--out-base", default=None,
                     help="Override out base. Default fuentes/raw/hacienda")
    args = ap.parse_args()

    base = Path(args.out_base) if args.out_base else (
        PROJECT_ROOT / "fuentes" / "raw" / "hacienda"
    )

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: pip install playwright && playwright install chromium",
              file=sys.stderr)
        return 3

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(accept_downloads=True)
        page = ctx.new_page()

        ok_total, fail_total = 0, 0
        t0 = time.time()
        for anio in args.anios:
            print(f"\n=== {anio} ===")
            for id3 in args.ccaa:
                if id3 not in CCAA_CODES:
                    print(f"  [SKIP] {id3} no en catálogo", file=sys.stderr)
                    continue
                out_path = base / str(anio) / "per_ccaa" / f"SGCIEF_{anio}_{id3}.xlsx"
                if out_path.exists() and out_path.stat().st_size > 4_000:
                    print(f"  [cache] {anio}/{id3}")
                    ok_total += 1
                    continue
                ok = download_one(page, anio, id3, out_path)
                if ok:
                    size = out_path.stat().st_size // 1024
                    print(f"  [OK] {anio}/{id3} -> {out_path.name} ({size} KB)")
                    ok_total += 1
                else:
                    fail_total += 1

        browser.close()
        dt = round(time.time() - t0, 1)
        print(f"\nResumen: OK={ok_total} FAIL={fail_total} ({dt}s)")
        return 0 if fail_total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
