"""ccaa/_common/generic.py — Fallback genérico (PROGRAMA <code> + TOTAL PROGRAMA)."""
from __future__ import annotations
import re
from pathlib import Path
from . import base
from .base import NUM_RE, PROG_CODIGO_RE, make_row, ExtractionResult


RE_PROGRAMA_HEADER = re.compile(
    r"^\s*(?:PROGRAMA|Programa)\s+(?P<codigo>\d{2,5}[A-Z]?)\s+(?P<denominacion>.+)$"
)
RE_TOTAL_PROGRAMA = re.compile(
    rf"^\s*(?:TOTAL\s+PROGRAMA|Total\s+programa)\s+(?P<importe>{NUM_RE})\s*€?\s*$"
)
RE_PROGRAMA_TABULAR = re.compile(
    rf"^\s*(?P<codigo>{PROG_CODIGO_RE})\s+"
    rf"(?P<denominacion>[A-Za-zÁÉÍÓÚÑáéíóúñÜü].+?)\s+"
    rf"(?P<importe>{NUM_RE})\s*€?\s*$"
)


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows = []
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            current = None
            for line in lines:
                m_hdr = RE_PROGRAMA_HEADER.match(line)
                if m_hdr:
                    current = (m_hdr.group("codigo"), m_hdr.group("denominacion").strip())
                    continue
                m_tot = RE_TOTAL_PROGRAMA.match(line)
                if m_tot and current is not None:
                    rows.append(make_row(pagina=p_num, codigo=current[0],
                                          denominacion=current[1],
                                          importe=m_tot.group("importe"), anio=anio))
                    current = None
            for line in lines:
                m = RE_PROGRAMA_TABULAR.match(line)
                if m:
                    rows.append(make_row(pagina=p_num, codigo=m.group("codigo"),
                                          denominacion=m.group("denominacion"),
                                          importe=m.group("importe"), anio=anio))
    except ImportError:
        return ExtractionResult(rows=[], motor="generic", notes="pdfplumber no disponible")
    return ExtractionResult(rows=rows, motor="generic-pdf")
