"""
extractors/val.py — Comunitat Valenciana.

El portal hisenda.gva.es publica el Tomo II como un frameset con
índice por sección (`T2_menu_epp_ES.html` → `T2_sec##_ES.html`). Cada
sección enlaza una RPC (Resumen General por Programas y Capítulos)
en formato PDF que contiene la tabla canónica:

    SECCIÓN: G0110 - Sanidad
    Subprograma  Cap I  Cap II  Cap III  Cap IV  Cap V  Total Op.Corr.
    Cap VI  Cap VII  Total Op.Cap.  Cap VIII  Cap IX  Total Op.Fin.  Total General
    411A00  Dirección y Servicios Generales  ...  28.559,74
    412B22  Atención Hospitalaria             ...  4.398.211,03
    ...
    TOTAL GENERAL  ...

Los importes están en miles de euros (encabezado: "(En miles de euros)").
Este extractor procesa todos los `secciones/sec*_RPC.pdf` y extrae el
"Total General" por subprograma (×1000 para pasar a euros).

Convención de entrada: el dispatcher pasa la ruta de
`fuentes/raw/val/<año>/tomo_II.html`. Buscamos los PDFs en
`<año>/secciones/sec*_RPC.pdf`. Si no existen, devolvemos 0 filas
con nota explicativa.
"""
from __future__ import annotations

import re
from pathlib import Path

from .._common import base
from .._common.base import make_row, ExtractionResult


# Subprograma code: 3 dígitos + letra + 2 dígitos (e.g. 411A00, 313D00, 322F00)
# o el formato legacy NNN.NN usado en ediciones <=2023 (e.g. 111.10, 411.00).
RE_SUBPROG_LINE = re.compile(
    r"^(?P<codigo>\d{3}[A-Z]\d{2}|\d{3}\.\d{2})\s+(?P<rest>.+)$"
)
# Numbers in es-ES with dot thousand separator and comma decimal
RE_NUM = re.compile(r"-?\d{1,3}(?:\.\d{3})*,\d{2}|-?\d+,\d{2}|0,00")


def _parse_subprog_line(line: str) -> tuple[str, str, float] | None:
    """De una línea estilo '411A00 Denominación …  N1 N2 … Nk' extrae
    (codigo, denominación, total_general). El Total General es el ÚLTIMO
    número de la línea.

    Devuelve None si no es una fila de subprograma o si no hay números.
    """
    m = RE_SUBPROG_LINE.match(line)
    if not m:
        return None
    codigo = m.group("codigo")
    rest = m.group("rest")
    nums = list(RE_NUM.finditer(rest))
    if not nums:
        return None  # row con denominación sin importes (continuación rara)
    last = nums[-1]
    denom = rest[: nums[0].start()].strip()
    if not denom:
        return None
    total_miles = base.parse_eur(last.group(0))
    if total_miles != total_miles or total_miles <= 0:  # NaN o 0
        return None
    return codigo, denom, total_miles * 1000.0  # miles → euros


def _is_real_pdf(pdf: Path) -> bool:
    try:
        with pdf.open("rb") as fh:
            return fh.read(4) == b"%PDF"
    except OSError:
        return False


def _collect_section_pdfs(input_path: Path) -> tuple[list[Path], list[str]]:
    """Devuelve (pdfs_validos, secciones_stub).

    Las secciones inexistentes quedan como stubs HTML 404 con extensión .pdf
    (el mount de Cowork no permite borrar). Pero también puede haber secciones
    cuyo PDF da 404 sin ser un stub vacío (menú `T2_sec##_ES.html` con
    contenido real): se reportan en `notes` en vez de desaparecer en
    silencio, aunque no siempre implican gasto perdido — p.ej. val 2026
    sec26 da 404 porque esa sección se FUSIONÓ con la 05 en la
    reorganización de gobierno de 2026 (verificado 2026-07-27, ver
    limitaciones-val.md); el gasto ya está en sec05_RPC.pdf, no falta nada.
    """
    p = Path(input_path)
    if p.suffix.lower() == ".pdf":
        return ([p], []) if _is_real_pdf(p) else ([], [])
    folder = p.parent / "secciones"
    if not folder.exists():
        return [], []
    pdfs, stubs = [], []
    for pdf in sorted(folder.glob("sec*_RPC.pdf")):
        if _is_real_pdf(pdf):
            pdfs.append(pdf)
            continue
        # ¿hay un menú de sección con contenido real (> placeholder de 196 b)?
        sec = re.search(r"sec(\d+)_RPC", pdf.name)
        menu = folder / f"T2_sec{sec.group(1)}_ES.html" if sec else None
        if menu and menu.exists() and menu.stat().st_size > 196:
            stubs.append(sec.group(1))  # sección real con PDF ausente → hueco
    return pdfs, stubs


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows: list[dict] = []
    pdfs, stub_secs = _collect_section_pdfs(input_path)
    if not pdfs:
        return ExtractionResult(
            rows=[], motor="val-rpc-secciones",
            notes=f"sin PDFs en {Path(input_path).parent / 'secciones'} — descargar sec*_RPC.pdf",
        )

    seen: set[tuple[str, str]] = set()
    try:
        for pdf in pdfs:
            for p_num, text in base.iter_pdf_text(pdf):
                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    parsed = _parse_subprog_line(line)
                    if not parsed:
                        continue
                    codigo, denom, importe = parsed
                    key = (codigo, pdf.name)
                    if key in seen:
                        continue
                    seen.add(key)
                    rows.append(make_row(pagina=p_num, codigo=codigo,
                                         denominacion=denom, importe=importe,
                                         anio=anio))
    except ImportError:
        return ExtractionResult(rows=[], motor="val-rpc-secciones",
                                notes="pdfplumber no disponible")

    notes = f"{len(pdfs)} PDFs RPC procesados, {len(rows)} subprogramas"
    if stub_secs:
        notes += (f" | ⚠️ {len(stub_secs)} sección(es) con menú pero sin PDF "
                  f"(hueco de datos): sec{', sec'.join(stub_secs)}")
    return ExtractionResult(rows=rows, motor="val-rpc-secciones", notes=notes)
