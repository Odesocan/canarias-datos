"""
extractors/ast.py — Principado de Asturias.

Formato (tomo_I.pdf — DISTRIBUCIÓN DEL GASTO POR SECCIONES, PROGRAMAS Y CAPÍTULOS):

    01 PRESIDENCIA DEL PRINCIPADO DE ASTURIAS 4.034.260 0,06
    112F INFORMACIÓN Y COMUNICACIÓN 1.559.000 0,02
        2 GASTOS EN BIENES CORRIENTES Y SERVICIOS 1.528.500 0,02
        4 TRANSFERENCIAS CORRIENTES 30.000 0,00

Estructura:
  - Sección con código 2 dígitos
  - Programa con 3-4 dígitos + letra (`112F`, `313B`, `612H`, ...)
  - Subdivisiones por capítulo económico (1 dígito) — IGNORAR

El importe es el penúltimo número de la línea; el último es porcentaje.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult


# Programa Asturias: 3-4 dígitos + letra mayúscula
RE_PROG_AST = re.compile(
    rf"^\s*(?P<codigo>\d{{3,4}}[A-Z])\s+"
    rf"(?P<denom>[A-Za-zÁÉÍÓÚÑáéíóúñÜü].+?)\s+"
    rf"(?P<importe>{NUM_RE})\s+"
    r"(?P<pct>\d+,\d+)\s*$"
)

# Programa SIN denominación inline: `<codigo> <importe> <pct>` (fix 2026-07-22).
# Cuando el nombre del programa es largo, el layout del PDF lo ENVUELVE alrededor
# de la línea numérica → el código queda solo con importe y % (p.ej. `011C` DEUDA
# 652,6 M y `712F` producciones ganaderas 145,2 M en 2024, ~0,8 B€ que el regex
# principal se saltaba → cobertura ast 86% vs Hacienda). El nombre se reconstruye
# de las líneas de texto anterior y siguiente.
RE_PROG_AST_NODENOM = re.compile(
    rf"^\s*(?P<codigo>\d{{3,4}}[A-Z])\s+"
    rf"(?P<importe>{NUM_RE})\s+"
    r"(?P<pct>\d+,\d+)\s*$"
)


def _es_fragmento_denom(s: str) -> bool:
    """True si la línea es texto de denominación (no empieza por dígito ni es
    una línea 'importe pct')."""
    s = s.strip()
    return bool(s) and not s[:1].isdigit() and not re.search(rf"{NUM_RE}\s+\d+,\d+$", s)

# Solo el bloque "DISTRIBUCIÓN DEL GASTO POR SECCIONES, PROGRAMAS Y CAPÍTULOS"
# (perímetro consejerías). El tomo de 2015 trae además anexos "RESUMEN
# PROGRAMÁTICO" y "PRESUPUESTO CONSOLIDADO" que listan los programas de los
# organismos (SESPA 412B = 1.434 M, la entrega ya contada como transferencia
# en 413D de la Consejería): barrer todas las páginas duplicaba sanidad ~×2.
_HDR_DISTRIBUCION = "DISTRIBUCION DEL GASTO"


def _sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows: list[dict] = []
    seen = set()
    paginas_fuera = 0
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            if _HDR_DISTRIBUCION not in _sin_acentos(text).upper():
                paginas_fuera += 1
                continue
            lineas = [ln.strip() for ln in text.splitlines()]
            for i, line in enumerate(lineas):
                if not line:
                    continue
                m = RE_PROG_AST.match(line)
                if m:
                    codigo = m.group("codigo")
                    denom = m.group("denom").strip()
                    importe = m.group("importe")
                else:
                    m2 = RE_PROG_AST_NODENOM.match(line)
                    if not m2:
                        continue
                    codigo = m2.group("codigo")
                    importe = m2.group("importe")
                    # Nombre partido: línea de texto anterior + siguiente (envuelto).
                    prev = lineas[i - 1] if i > 0 else ""
                    nxt = lineas[i + 1] if i + 1 < len(lineas) else ""
                    partes = [p for p in (prev, nxt) if _es_fragmento_denom(p)]
                    denom = " ".join(partes).strip() or codigo
                key = (codigo, denom[:30])
                if key in seen:
                    continue
                seen.add(key)
                rows.append(make_row(pagina=p_num, codigo=codigo, denominacion=denom,
                                      importe=importe, anio=anio))
    except ImportError:
        return ExtractionResult(rows=[], motor="ast", notes="pdfplumber no disponible")

    return ExtractionResult(
        rows=rows, motor="ast-distribucion-gasto",
        notes=f"{paginas_fuera} págs fuera del bloque DISTRIBUCIÓN saltadas")
