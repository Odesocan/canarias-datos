"""
extractors/mur.py — Región de Murcia (CARM).

Portal:  https://www.carm.es/chac/presupuestos<año>/web/

Estructura HTML:
  - `xml/31.xml`  → índice de secciones del Estado de Gastos (Administración
    General).  Cada `urlo` apunta a `datos/p228-<sec>-<servicio>.htm`.
  - `xml/32.xml`  → índice de los organismos autónomos (IMAS, SEF, BORM).
    Apunta a `datos/p230-...`, `p231-...`.
  - `datos/p228-XX-XXXX.htm` (y `p230/p231`) → tabla anidada Servicio /
    Programa / Capítulo / Artículo / Concepto / Subconcepto con clases
    `fila_6 .. fila_1`.

El nivel **programa** lleva el código funcional habitual en la AGE
(3 dígitos + letra: `412A`, `421B`, `911A` …) y un importe agregado del
programa por servicio.  Sumamos por código de programa, ignorando los
desgloses inferiores.

Para 2015 no hay visor HTML equivalente: la fuente disponible es la Ley completa
en PDF, que contiene páginas "Estado de gastos por servicios y programas
presupuestarios". En ese caso se extraen esas líneas y se aplica la misma
agregación por código de programa que en el HTML.

Input esperado por el dispatcher:
  - directorio `fuentes/raw/mur/<año>/`
  - o cualquier fichero dentro que apunte al directorio (ej. `portal_movil.html`)
  - PDF de la Ley completa para 2015

El raw se descarga con `tools/mur_download.py` (genera el árbol `datos/*.htm`).
"""
from __future__ import annotations

import re
from pathlib import Path

from .._common.base import iter_pdf_text, make_row, ExtractionResult


# class="fila_5" → fila de programa (3 dígitos + letra).
# La celda nombre puede cerrar con </TD> o sólo con salto de línea.
# El importe en col_n suele ser `\d{1,3}(\.\d{3})*`.
RE_PROGRAMA = re.compile(
    r'<TR class="fila_5">\s*'
    r'<TD class="col_t">\s*(?P<codigo>\d{3}[A-Z])\s+(?P<denom>[^<\n]+?)(?:</TD>|\n)'
    r'.*?<TD class="col_n">\s*(?P<importe>[\d\.]+)',
    re.S,
)

RE_H1 = re.compile(r'<H1>\s*Sección:\s*(\d{2})\s+([^<]+?)\s*</H1>', re.I)

RE_PDF_PROGRAMA = re.compile(
    r"^\s*(?P<codigo>\d{3}[A-Z])\s+"
    r"(?P<denom>.+?)\s+"
    r"(?P<importe>\d{1,3}(?:\.\d{3})+|\d+)\s*$"
)

RE_PDF_PROGRAMAS_HEADING = re.compile(
    r"estado de gastos por servicios y programas\s+presupuestarios", re.I
)
RE_PDF_END_HEADING = re.compile(
    r"(?:presupuesto de ingresos|ingresos por capítulos|estado de gastos por servicios y capítulos)",
    re.I,
)


def _parse_eur_es(s: str) -> float:
    """'1.234.567' → 1234567.0  /  '1.234,56' → 1234.56."""
    if not s:
        return float("nan")
    s = s.strip().replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif "." in s:
        # importes enteros en euros → todos los puntos son miles
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return float("nan")


def _iter_htm_files(input_path: Path):
    """Devuelve los `datos/p228-*.htm` (y `p230/p231/*`) bajo el raw correspondiente.
    `input_path` puede ser directorio o un fichero dentro del directorio raw.
    """
    base = input_path if input_path.is_dir() else input_path.parent
    candidatos = sorted(base.glob("datos/p228-*.htm")) + \
                 sorted(base.glob("datos/p230-*.htm")) + \
                 sorted(base.glob("datos/p231-*.htm"))
    if not candidatos:
        # layout plano (descarga parcial todavía en raíz del raw)
        candidatos = sorted(base.glob("p228-*.htm")) + \
                     sorted(base.glob("p230-*.htm")) + \
                     sorted(base.glob("p231-*.htm"))
    return candidatos


def _extract_pdf_programas(input_path: Path, anio: int) -> ExtractionResult:
    agg: dict[str, float] = {}
    denom_by: dict[str, str] = {}
    ix_by: dict[str, int] = {}
    pages_with_rows: set[int] = set()
    in_programas = False

    for page_num, text in iter_pdf_text(input_path):
        if RE_PDF_PROGRAMAS_HEADING.search(text):
            in_programas = True
        elif in_programas and RE_PDF_END_HEADING.search(text):
            in_programas = False

        if not in_programas:
            continue

        for line in text.splitlines():
            m = RE_PDF_PROGRAMA.match(line)
            if not m:
                continue
            cod = m.group("codigo").upper()
            denom = " ".join(m.group("denom").split())
            imp = _parse_eur_es(m.group("importe"))
            if imp != imp:  # NaN
                continue
            agg[cod] = agg.get(cod, 0.0) + imp
            denom_by.setdefault(cod, denom)
            ix_by.setdefault(cod, page_num)
            pages_with_rows.add(page_num)

    rows = [
        make_row(
            pagina=ix_by[c],
            codigo=c,
            denominacion=denom_by[c],
            importe=agg[c],
            anio=anio,
        )
        for c in sorted(agg.keys())
    ]
    notes = ""
    if not rows:
        return ExtractionResult(
            rows=[],
            motor="mur-pdf-programas",
            notes="No se detectaron páginas de gasto por servicios y programas en el PDF.",
        )
    return ExtractionResult(
        rows=rows,
        motor=f"mur-pdf-programas ({len(pages_with_rows)} páginas)",
        notes=notes,
    )


def _extract_html(input_path: Path, anio: int) -> ExtractionResult:
    htmls = _iter_htm_files(input_path)
    if not htmls:
        return ExtractionResult(
            rows=[], motor="mur-html",
            notes=("Sin .htm de gastos en raw. Descarga con "
                   f"`python3 tools/mur_download.py --anio {anio}` "
                   "(requiere IP no rate-limitada por Radware)."))

    agg: dict[str, float] = {}
    denom_by: dict[str, str] = {}
    ix_by: dict[str, int] = {}
    skipped_captcha = 0
    for i, h in enumerate(htmls, start=1):
        try:
            txt = h.read_bytes().decode("iso-8859-1", errors="replace")
        except Exception:
            continue
        if "Radware Captcha" in txt or "shieldsquare" in txt:
            skipped_captcha += 1
            continue
        for m in RE_PROGRAMA.finditer(txt):
            cod = m.group("codigo").upper()
            denom = " ".join(m.group("denom").split())
            imp = _parse_eur_es(m.group("importe"))
            if imp != imp:  # NaN
                continue
            agg[cod] = agg.get(cod, 0.0) + imp
            denom_by.setdefault(cod, denom)
            ix_by.setdefault(cod, i)

    rows = [make_row(pagina=ix_by[c], codigo=c,
                     denominacion=denom_by[c], importe=agg[c], anio=anio)
            for c in sorted(agg.keys())]
    notes = ""
    if skipped_captcha:
        notes = f"{skipped_captcha} ficheros Radware ignorados — re-descarga"
    return ExtractionResult(rows=rows, motor=f"mur-html ({len(htmls)} archivos)",
                             notes=notes)


def extract(input_path: Path, anio: int) -> ExtractionResult:
    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        return _extract_pdf_programas(input_path, anio)
    return _extract_html(input_path, anio)
