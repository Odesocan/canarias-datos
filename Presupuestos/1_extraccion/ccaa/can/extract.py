"""
extractors/can.py — Canarias.

Fuente real: `tomo_3.pdf` (Resúmenes Económicos), sección 2.10 "Por Programas".
La sección tiene un cuadro "RESUMEN DE GASTOS POR PROGRAMAS — COMUNIDAD AUTÓNOMA"
con el formato (es-ES, importes en euros enteros):

    Cod.   Programa                                  PRES.INICIAL    %     PRES.INICIAL  %    2/1 %
                                                       AJUSTADO       2024            2025
    112A   Tribunales de Justicia                   182.200.137  1,70  193.288.385  1,74    6,09
    112B   Relaciones con la Administración de J.    6.697.306  0,06    7.405.694  0,07   10,58
    ...

El segundo importe (sin coma decimal) es PRESUPUESTO INICIAL <anio>.  La
sección 2.16 ("Por Secciones, Programas y Capítulos") repite los códigos con
desglose por capítulos: la *evitamos* para no duplicar/contaminar.

Estrategia:
  1) Si en `fuentes/raw/can/<año>/` hay un CSV adjunto (`seflogic*.csv`,
     `programas*.csv`, `partidas*.csv`) con columnas (codigo, denominacion,
     importe_eur), gana sobre el PDF.
  2) En caso contrario, parsea la sección 2.10 del tomo_3.pdf vía
     pdftotext -layout (poppler) — más rápido y estable que pdfplumber.

Códigos canarios: 3 dígitos + letra (`312A`, `412A`, `231M`, `261A`, …).
"""
from __future__ import annotations

import csv
import re
import shutil
import subprocess
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult, parse_eur


# Cualquier número en formato es-ES (heredado de base.NUM_RE).
_NUM_RE_C = re.compile(NUM_RE)

# Línea de programa: 3 dígitos + 1 letra al inicio + denom + numeros.
RE_PROG_LINE = re.compile(
    rf"^\s*(?P<codigo>\d{{3}}[A-Z])\s+(?P<resto>\S.+?)\s*$"
)

# Cabeceras de sección que delimitan "RESUMEN DE GASTOS POR PROGRAMAS"
# (consolidado, sin capítulos).  NB: sección 2.16 "POR SECCIONES, PROGRAMAS Y
# CAPÍTULOS" o 2.15 "POR PROGRAMAS Y CAPÍTULOS" DEBEN excluirse: son
# desgloses por capítulo donde la "Total" repite los mismos códigos.
RE_INIT_PROGRAMAS = re.compile(r"RESUMEN\s+DE\s+GASTOS\s+POR\s+PROGRAMAS\s*$",
                                re.IGNORECASE)
RE_INIT_PROG_CAP = re.compile(
    r"RESUMEN\s+DE\s+GASTOS\s+POR\s+PROGRAMAS\s+Y\s+CAP[IÍ]TULOS", re.IGNORECASE
)
RE_INIT_SEC_PROG = re.compile(
    r"POR\s+SECCIONES\s*,?\s*PROGRAMAS", re.IGNORECASE
)


def _iter_text_fast(path: Path):
    """Itera (página, texto) usando pdftotext -layout si está disponible."""
    if shutil.which("pdftotext"):
        try:
            out = subprocess.check_output(
                ["pdftotext", "-layout", str(path), "-"], timeout=120
            ).decode("utf-8", errors="replace")
            for i, page in enumerate(out.split("\f"), start=1):
                yield i, page
            return
        except Exception:
            pass
    yield from base.iter_pdf_text(path)


def _from_csv(input_path: Path, anio: int) -> list[dict]:
    candidatos = list(input_path.parent.glob("seflogic*.csv")) + \
                 list(input_path.parent.glob("programas*.csv")) + \
                 list(input_path.parent.glob("partidas*.csv"))
    if not candidatos:
        return []
    src = candidatos[0]
    rows: list[dict] = []
    with src.open("r", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            if not r.get("codigo"):
                continue
            rows.append(make_row(pagina=None, codigo=r["codigo"],
                                  denominacion=r.get("denominacion", ""),
                                  importe=parse_eur(r.get("importe_eur", "0")),
                                  anio=anio))
    return rows


def _is_importe_token(tok: str) -> bool:
    """Considera 'importe' los números enteros sin coma decimal.
    p.ej. '182.200.137', '1.000.000', '12345' → True
          '1,70', '0,06', '6,09' (porcentajes) → False
    """
    return "," not in tok


def _pick_importe(tokens: list[str], anio_target: int) -> str | None:
    """Selecciona el importe asociado al año-objetivo.

    Formato típico en sección 2.10 (4-5 tokens):
        importe_2024  %_2024  importe_2025  %_2025  [%_delta]

    El 2º importe (sin coma) es el del año objetivo (la PDF usa PRESUPUESTO
    INICIAL <anio>=2025, columna PRES.INICIAL AJUSTADO <anio-1>=2024).
    """
    importes = [t for t in tokens if _is_importe_token(t)]
    if not importes:
        return None
    if len(importes) >= 2:
        return importes[1]
    return importes[0]


def _parse_pdf(input_path: Path, anio: int) -> list[dict]:
    rows: list[dict] = []
    in_programas = False
    seen: set[str] = set()  # códigos ya capturados → evita duplicados
    pagina_actual = None

    for p_num, text in _iter_text_fast(input_path):
        for raw_line in text.splitlines():
            line = raw_line.rstrip()
            # Activadores / desactivadores de sección
            if RE_INIT_PROG_CAP.search(line) or RE_INIT_SEC_PROG.search(line):
                in_programas = False
                continue
            if RE_INIT_PROGRAMAS.search(line):
                in_programas = True
                pagina_actual = p_num
                continue
            if not in_programas:
                continue
            m = RE_PROG_LINE.match(line)
            if not m:
                continue
            codigo = m.group("codigo")
            resto = m.group("resto")
            # split: la denominación termina cuando empieza el bloque numérico
            # (2+ espacios y luego un número).  Usamos NUM_RE para cortar.
            nums = list(_NUM_RE_C.finditer(resto))
            if not nums:
                continue
            denom = resto[:nums[0].start()].strip().rstrip(" .")
            if not denom:
                continue
            tokens = [m_.group(0) for m_ in nums]
            importe = _pick_importe(tokens, anio)
            if importe is None:
                continue
            val = parse_eur(importe)
            if val is None or val != val or val <= 0:
                # NaN o cero/negativo: saltar (un programa con presupuesto 0 no
                # aporta señal y suele ser placeholder)
                continue
            if codigo in seen:
                # Si lo vemos otra vez (p.ej. cabildos), nos quedamos con el
                # primero (sección 2.10 va antes que 2.11+).
                continue
            seen.add(codigo)
            rows.append(make_row(pagina=p_num, codigo=codigo,
                                 denominacion=denom, importe=val, anio=anio))
    return rows


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # 1) CSV adjunto manda
    csv_rows = _from_csv(input_path, anio)
    if csv_rows:
        return ExtractionResult(rows=csv_rows, motor="can-csv-seflogic")

    # 2) PDF tomo_3.pdf — sección 2.10 RESUMEN DE GASTOS POR PROGRAMAS
    try:
        rows = _parse_pdf(input_path, anio)
    except ImportError:
        rows = []
    motor = "can-tomo3-resumen-programas" if rows else "can-pendiente"
    notes = "" if rows else (
        "No se localizó la sección 'RESUMEN DE GASTOS POR PROGRAMAS' en el PDF; "
        "considerar tomo_I o CSV SEFLogiC."
    )
    return ExtractionResult(rows=rows, motor=motor, notes=notes)
