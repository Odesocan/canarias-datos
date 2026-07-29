#!/usr/bin/env python3
"""
extract_hacienda.py — Capa Hacienda (SGCIEF) del pipeline Presupuestos.

El visor SGCIEF (https://serviciostelematicosext.hacienda.gob.es/SGCIEF/
PublicacionPresupuestos/) entrega los datos mediante un formulario ASP.NET
con sesión y ViewState; no admite descargas directas vía GET.

Solución de doble vía:

  1. **Descarga automatizada con Playwright** (modo `download`). Navega:
       inicio.aspx → Sel_Proyecto.aspx → selector de ejercicio →
       SelDescargaDC.aspx → botón "Descargar Excel". Guarda el XLSX en
       fuentes/raw/hacienda/<anio>/SGCIEF_<anio>.xlsx. Si Playwright no
       está disponible, el modo "download" devuelve exit=3 y el operador
       debe descargar manualmente (ver punto 2).

  2. **Parser de XLSX local** (modo `parse`). Lee un XLSX colocado en
       fuentes/raw/hacienda/<anio>/ y lo convierte al schema staging del
       pipeline:
           codigo, denominacion, importe_eur, ccaa, anio, capa='hacienda'

Uso:
   python3 extract_hacienda.py --mode parse --input  archivo.xlsx --output salida.parquet --anio 2024
   python3 extract_hacienda.py --mode download --anio 2024 --out_dir fuentes/raw/hacienda/2024
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Mapeo nombre CCAA Hacienda → id3 del pipeline
HACIENDA_CCAA_ID3 = {
    "andalucía": "and", "andalucia": "and",
    "aragón": "ara", "aragon": "ara",
    "asturias": "ast", "principado de asturias": "ast",
    "balears, illes": "bal", "islas baleares": "bal", "illes balears": "bal",
    "canarias": "can",
    "cantabria": "cnt",
    "castilla y león": "cym", "castilla y leon": "cym",
    "castilla-la mancha": "clm",
    "cataluña": "cat", "cataluna": "cat", "catalunya": "cat",
    "comunitat valenciana": "val", "comunidad valenciana": "val",
    "extremadura": "ext",
    "galicia": "gal",
    "madrid, comunidad de": "mad", "comunidad de madrid": "mad", "madrid": "mad",
    "murcia, región de": "mur", "región de murcia": "mur", "murcia": "mur",
    "navarra, comunidad foral de": "nav", "comunidad foral de navarra": "nav", "navarra": "nav",
    "país vasco": "pvc", "pais vasco": "pvc", "euskadi": "pvc",
    "rioja, la": "lar", "la rioja": "lar",
    "ceuta": "ceu",
    "melilla": "mel",
}

# Códigos de capítulo SGCIEF
CAPITULOS = {
    1: "Gastos de personal",
    2: "Gastos corrientes en bienes y servicios",
    3: "Gastos financieros",
    4: "Transferencias corrientes",
    5: "Fondo de contingencia",
    6: "Inversiones reales",
    7: "Transferencias de capital",
    8: "Activos financieros",
    9: "Pasivos financieros",
}

# Mapeo políticas funcionales → concepto del pipeline (parcial; se afina con
# correspondencias.yml en transformacion.R)
POLITICAS_FUNCION = {
    "sanidad": "sanidad",
    "salud": "sanidad",
    "educación": "educacion",
    "educacion": "educacion",
    "vivienda y servicios urbanos": "vivienda",
    "acceso a la vivienda": "vivienda",
    "fomento del empleo": "empleo",
    "agricultura, pesca y alimentación": "soberania",
    "agricultura, ganadería y pesca": "soberania",
    "investigación, desarrollo": "idi",
    "i+d+i": "idi",
    "alta dirección": "direccion",
    "dirección política": "direccion",
    "turismo": "turismo",
}


def _normalize_ccaa(s: str) -> str | None:
    key = re.sub(r"[\d\.]+\s*", "", (s or "").strip().lower())
    key = key.strip(",.;:- ")
    return HACIENDA_CCAA_ID3.get(key)


def _parse_eur(value) -> float:
    """Convierte celda XLSX (numérica o string es-ES) a float."""
    if value is None:
        return float("nan")
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip().replace(" ", "")
    if not s or s in {"-", "..", "n.d.", "N/A"}:
        return float("nan")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return float("nan")


def parse_xlsx(path: Path, anio: int) -> list[dict]:
    """Lee un XLSX Hacienda. Heurística:
       - Detecta la tabla con CCAA en una columna y políticas/capítulos en otras.
       - Soporta el formato "pivot" (filas=CCAA, cols=política).
       - Funciona también con CSV: la lectura se delega según extensión.
    """
    rows: list[dict] = []
    if path.suffix.lower() == ".csv":
        return _parse_csv(path, anio)

    try:
        from openpyxl import load_workbook  # type: ignore
    except ImportError:
        print("ERROR: openpyxl no instalado (pip install openpyxl)", file=sys.stderr)
        return []

    wb = load_workbook(filename=str(path), data_only=True, read_only=True)
    for ws in wb.worksheets:
        cells = list(ws.iter_rows(values_only=True))
        if not cells:
            continue
        # 1) Intento formato pivot (CCAA en filas) — stub legacy 2024
        rows.extend(_parse_table(cells, anio))
        if rows:
            break
        # 2) Fallback: XLSX per-CCAA real (SGCIEF DescargaEconomicaDC) —
        #    la CCAA aparece en celda A10 y los capítulos de gasto en filas
        #    con prefijo "<N>. ". Detecta este formato y emite filas tidy.
        rows.extend(_parse_sgcief_per_ccaa(cells, anio, path))
        if rows:
            break
    return rows


# Mapa nombre Hacienda → id3 ampliado para detectar el encabezado interno
# (e.g. "Junta de Andalucía", "Comunidad de Madrid", "Generalitat de Catalunya").
_SGCIEF_NAME_TO_ID3 = {
    "junta de andalucía": "and", "junta de andalucia": "and",
    "gobierno de aragón": "ara", "gobierno de aragon": "ara",
    "principado de asturias": "ast", "comunidad autónoma del principado de asturias": "ast",
    "govern de les illes balears": "bal", "govern illes balears": "bal", "illes balears": "bal",
    "comunidad autónoma de canarias": "can", "gobierno de canarias": "can", "canarias": "can",
    "comunidad autónoma de cantabria": "cnt", "gobierno de cantabria": "cnt", "cantabria": "cnt",
    "junta de castilla y león": "cym", "junta de castilla y leon": "cym",
    "junta de comunidades de castilla-la mancha": "clm", "castilla-la mancha": "clm",
    "generalitat de catalunya": "cat", "generalidad de cataluña": "cat",
    "junta de extremadura": "ext",
    "xunta de galicia": "gal", "galicia": "gal",
    "comunidad de madrid": "mad",
    "comunidad autónoma de la región de murcia": "mur", "región de murcia": "mur",
    "comunidad foral de navarra": "nav", "navarra": "nav",
    "gobierno vasco": "pvc", "país vasco": "pvc", "euskadi": "pvc",
    "gobierno de la rioja": "lar", "la rioja": "lar",
    "generalitat valenciana": "val", "comunitat valenciana": "val",
    "ciudad autónoma de ceuta": "ceu", "ceuta": "ceu",
    "ciudad autónoma de melilla": "mel", "melilla": "mel",
}


def _parse_sgcief_per_ccaa(cells: list, anio: int, src: Path,
                            id3_hint: str | None = None) -> list[dict]:
    """Parser para los XLSX de SGCIEF descargados con autonomia != 00.

    Formato observado:
      Row 7: 'Ingresos y Gastos por capítulos'
      Row 8: 'Presupuestos iniciales de las CCAA' (o similar)
      Row 9: '<Nombre del organismo CCAA>'
      Row 12: 'Capítulos de ingresos' | 'Miles de euros' | '%'
      Rows 14-26: capítulos de ingresos (1.-9.)
      Row 31: 'Capítulos de gastos'
      Rows 33-45: capítulos de gasto (1.-9.)

    id3_hint: si se pasa, se usa como id3 cuando no se reconoce el
    nombre del organismo (los XLSX de 2022/2023 usan etiquetas más
    cortas como 'CAIB' o 'Generalitat' que no estaban en el mapa).
    """
    rows: list[dict] = []
    # Detecta CCAA en las primeras 15 filas
    id3 = None
    for r in cells[:15]:
        if not r: continue
        first = (str(r[0]).strip() if r and r[0] is not None else "").lower()
        if first in _SGCIEF_NAME_TO_ID3:
            id3 = _SGCIEF_NAME_TO_ID3[first]
            break
    if not id3:
        # Fallback: nombre extraído del path SGCIEF_<anio>_<id3>.xlsx
        if id3_hint is None and src is not None:
            stem = Path(src).stem  # e.g. SGCIEF_2023_and
            parts = stem.split("_")
            if len(parts) >= 3 and len(parts[-1]) == 3:
                id3_hint = parts[-1].lower()
        if id3_hint:
            id3 = id3_hint
    if not id3:
        return rows
    in_gastos = False
    for r in cells:
        if not r: continue
        first = str(r[0]).strip() if r[0] is not None else ""
        if "Capítulos de gastos" in first:
            in_gastos = True; continue
        if not in_gastos:
            continue
        m = re.match(r"^(\d+)\.\s+(.+)$", first)
        if not m or len(r) < 2 or r[1] is None:
            continue
        cap = int(m.group(1))
        denom_oficial = m.group(2).strip()
        try:
            miles = float(str(r[1]).replace(",", "."))
        except (TypeError, ValueError):
            continue
        if miles == 0:
            continue
        rows.append({
            "codigo": f"{cap:02d}",
            "denominacion": CAPITULOS.get(cap, denom_oficial),
            "importe_eur": miles * 1000.0,
            "ccaa_id3": id3,
            "anio": anio,
            "capa": "hacienda",
            "capitulo": cap,
        })
    return rows


def _parse_csv(path: Path, anio: int) -> list[dict]:
    rows: list[dict] = []
    # Intenta locale es-ES y luego anglosajón
    with path.open("r", encoding="utf-8-sig", errors="replace") as fh:
        sample = fh.read(4096); fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=";,|\t")
        except csv.Error:
            dialect = csv.excel
        reader = csv.reader(fh, dialect)
        cells = [r for r in reader]
    rows.extend(_parse_table(cells, anio))
    return rows


def _detect_header(cells: list) -> tuple[int, int, list[str]]:
    """Devuelve (header_row_index, ccaa_col_index, columnas)."""
    for i, row in enumerate(cells[:30]):
        if row is None: continue
        normalized = [(str(c).strip().lower() if c is not None else "") for c in row]
        # Buscamos celda con "ccaa", "comunidad", "territorio"
        for j, val in enumerate(normalized):
            if val in ("ccaa","comunidad","comunidad autonoma","comunidad autónoma","territorio"):
                return i, j, list(row)
    # fallback: primera fila no vacía
    for i, row in enumerate(cells[:5]):
        if row and any(c is not None for c in row):
            return i, 0, list(row)
    return 0, 0, list(cells[0]) if cells else (0, 0, [])


def _parse_table(cells: list, anio: int) -> list[dict]:
    if not cells:
        return []
    h_idx, ccaa_col, header = _detect_header(cells)
    rows: list[dict] = []
    # Por cada celda numérica de la tabla, genera una fila tidy.
    for r in cells[h_idx + 1:]:
        if r is None or not any(c is not None for c in r):
            continue
        ccaa_raw = r[ccaa_col] if ccaa_col < len(r) else None
        if not ccaa_raw or not isinstance(ccaa_raw, str):
            continue
        id3 = _normalize_ccaa(ccaa_raw)
        if not id3:
            continue
        for c_idx, value in enumerate(r):
            if c_idx == ccaa_col or value is None:
                continue
            try:
                col_label = str(header[c_idx]).strip() if c_idx < len(header) else f"col{c_idx}"
            except IndexError:
                col_label = f"col{c_idx}"
            if not col_label or col_label.lower() in ("none","",ccaa_raw.lower()):
                continue
            imp = _parse_eur(value)
            if not (imp == imp) or imp == 0:  # NaN or zero
                continue
            # Si el header es un nº (capítulo económico): asigna codigo "01".."09"
            try:
                cap_num = int(re.search(r"\d+", col_label).group()) if re.search(r"\d+", col_label) else None
            except (AttributeError, ValueError):
                cap_num = None
            if cap_num and cap_num in CAPITULOS:
                codigo = f"{cap_num:02d}"
                denominacion = CAPITULOS[cap_num]
            else:
                codigo = ""
                denominacion = col_label
            rows.append({
                "codigo": codigo,
                "denominacion": denominacion,
                "importe_eur": imp,
                "ccaa_id3": id3,
                "anio": anio,
                "capa": "hacienda",
                "capitulo": cap_num,
            })
    return rows


def write_output(rows: list[dict], output: Path, anio: int, src: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    enriched = [{**r, "fuente_path": str(src), "fecha_captura": now} for r in rows]

    try:
        import pandas as pd  # type: ignore
        df = pd.DataFrame(enriched)
        ext = output.suffix.lower()
        if ext == ".csv":
            df.to_csv(output, index=False)
            return True
        try:
            df.to_parquet(output, index=False)
            return True
        except Exception:
            df.to_csv(output.with_suffix(".csv"), index=False)
            return True
    except ImportError:
        out_path = output.with_suffix(".csv")
        with out_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh,
                fieldnames=["codigo","denominacion","importe_eur","ccaa_id3","anio",
                            "capa","capitulo","fuente_path","fecha_captura"]
            )
            writer.writeheader(); writer.writerows(enriched)
        return True


def _download_with_playwright(anio: int, out_dir: Path) -> int:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print("Playwright no instalado. Instalar con:", file=sys.stderr)
        print("  pip install playwright && python -m playwright install chromium", file=sys.stderr)
        print("Mientras tanto, descarga manualmente el XLSX desde", file=sys.stderr)
        print("  https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PublicacionPresupuestos/", file=sys.stderr)
        print(f"y colócalo en {out_dir}", file=sys.stderr)
        return 3

    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"SGCIEF_{anio}.xlsx"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(accept_downloads=True)
        page = ctx.new_page()
        page.goto("https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PublicacionPresupuestos/aspx/inicio.aspx",
                  wait_until="domcontentloaded", timeout=60000)
        # Navegar a "Datos Consolidados"
        try:
            page.click("a[href*='SelconsultaDC.aspx']", timeout=10000)
            page.wait_for_load_state("networkidle", timeout=20000)
        except Exception as e:
            print(f"No se pudo abrir Consultas DC: {e}", file=sys.stderr)
            browser.close(); return 4

        # Seleccionar año si hay un dropdown
        try:
            page.select_option("select[name*='Ejer']", str(anio))
        except Exception:
            pass

        # Buscar el botón "Descargar Excel" o equivalente
        try:
            with page.expect_download(timeout=120000) as dlinfo:
                page.click("input[value*='Excel'], a:has-text('Excel'), input[value*='Descargar']")
            download = dlinfo.value
            download.save_as(str(target))
        except Exception as e:
            print(f"No se pudo descargar el XLSX: {e}", file=sys.stderr)
            browser.close(); return 5

        browser.close()
    print(f"OK descargado {target}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["parse","download"], required=True)
    ap.add_argument("--anio", type=int, required=True)
    ap.add_argument("--input")
    ap.add_argument("--output")
    ap.add_argument("--out_dir")
    args = ap.parse_args()

    if args.mode == "download":
        if not args.out_dir:
            print("ERROR: --out_dir requerido en modo download", file=sys.stderr); return 2
        return _download_with_playwright(args.anio, Path(args.out_dir))

    # mode=parse
    if not args.input or not args.output:
        print("ERROR: --input y --output requeridos en modo parse", file=sys.stderr); return 2
    src = Path(args.input)
    if not src.exists():
        print(f"ERROR: no existe {src}", file=sys.stderr); return 2

    rows = parse_xlsx(src, args.anio)
    if not rows:
        print(f"WARN sin filas en {src}", file=sys.stderr); return 2

    ok = write_output(rows, Path(args.output), args.anio, src)
    print(f"OK filas={len(rows)} -> {args.output} ok={ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
