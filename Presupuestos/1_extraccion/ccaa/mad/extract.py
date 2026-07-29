"""
extractors/mad.py — Comunidad de Madrid.

El **Libro 04** (memoria de programas) sigue sin tener una URL canónica
estable, así que mientras tanto trabajamos con el **Libro 03** "Ingresos y
Gastos" (libro_03.pdf). El Libro 03 NO incluye desglose por programa funcional
— Madrid clasifica por sección/centro presupuestario en sus resúmenes.

Estrategia (cobertura mínima esta noche):

Sección IV.3 del Libro 03, "RESUMEN POR TIPO DE CENTROS PRESUPUESTARIOS,
ORGÁNICA Y CAPÍTULOS" (a partir de pág. 102), lista cada **centro
presupuestario** (D.G., S.G.T., …) con sus 9 capítulos económicos y su total:

    04012-D.G. DE TURISMO Y HOSTELERIA   8.528.692  21.810.797  ... 57.406.038
    04014-D.G. DE DEPORTES               16.578.485 18.479.275 ... 55.218.787
    11022-D.G. DE RECURSOS HUMANOS...    382.749.264 ...            466.768.103
    ...
    04-CULTURA, TURISMO Y DEPORTE        84.405.706 ...           300.301.706

Extraemos las líneas de centro (código orgánico 4-5 dígitos + nombre + 10
columnas numéricas) y su TOTAL (última columna). El código orgánico sirve
de proxy del programa hasta que el resolver localice el Libro 04. Las
correspondencias se asignan principalmente por KEYWORD sobre la
denominación (D.G. DE SANIDAD → sanidad, etc.).

Fallback `mad-xlsx-adjunto` si hay programas*.xlsx|csv adjunto, idem clm.
"""
from __future__ import annotations

import csv
import re
import shutil
import subprocess
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult, parse_eur


# Línea de centro: "01001-ASAMBLEA DE MADRID  27.326.200  7.885.900  …  40.728.400"
# - Código orgánico: 4-5 dígitos (sección+centro) o 2 dígitos (sección agregada).
# - Formato reciente (2019+): 10 columnas en una línea (Cap1..Cap9 + TOTAL).
# - Formato antiguo (2015-2018): la tabla se PARTE en dos páginas — Cap.1-5 en
#   una y Cap.6-9+TOTAL en la siguiente (5 números por línea). Por eso aceptamos
#   un número VARIABLE de columnas y nos quedamos con el último número como
#   TOTAL, pero SOLO en páginas cuya cabecera incluye la columna TOTAL (gate
#   `_page_has_total`), de modo que la página parcial Cap.1-5 se ignora.
NUM = r"\d{1,3}(?:\.\d{3})*"  # entero es-ES con miles
# FIX 2026-07-02: exigir código de 4-5 dígitos (CENTRO). El `\d{2,5}` previo
# capturaba también los agregados de SECCIÓN de 2 dígitos ("15 EDUCACIÓN
# 4.326M") que conviven con sus centros hijos ("15xxx"), y ambos recibían
# concepto → doble conteo (educación +46 %). Verificado 2015: para toda sección
# suma(hijos 5-díg) ≥ agregado 2-díg, así que los centros son la representación
# completa y excluir los agregados no pierde gasto (solo elimina el duplicado).
RE_CENTRO = re.compile(
    rf"^(?P<codigo>\d{{4,5}})-\s*(?P<denom>[A-ZÁÉÍÓÚÑ][^\d]+?)\s+"
    rf"(?P<numeros>(?:{NUM}\s+)*{NUM})\s*$"
)


def _page_has_total(text: str) -> bool:
    """True si la página tiene la columna TOTAL (cabecera 'Cap. … TOTAL').

    Discrimina la página con totales (formato nuevo: Cap.1..9 TOTAL; formato
    antiguo: Cap.6..9 TOTAL) de la página parcial Cap.1-5 (sin TOTAL)."""
    for ln in text.splitlines():
        low = ln.lower()
        if ("cap" in low or "orgánica" in low or "organica" in low) and "total" in low:
            return True
    return False


def _iter_text_fast(path: Path):
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


def _extract_from_xlsx_or_csv(input_path: Path, anio: int) -> ExtractionResult | None:
    candidatos = list(input_path.parent.glob("programas*.xlsx")) + \
                 list(input_path.parent.glob("programas*.csv"))
    if not candidatos:
        return None
    src = candidatos[0]
    rows: list[dict] = []
    if src.suffix.lower() == ".csv":
        with src.open("r", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r.get("codigo"):
                    rows.append(make_row(pagina=None, codigo=r["codigo"],
                                         denominacion=r.get("denominacion", ""),
                                         importe=parse_eur(r.get("importe_eur", "0")),
                                         anio=anio))
    return ExtractionResult(rows=rows, motor="mad-xlsx-adjunto") if rows else None


def extract(input_path: Path, anio: int) -> ExtractionResult:
    alt = _extract_from_xlsx_or_csv(input_path, anio)
    if alt is not None and len(alt.rows) >= 20:
        return alt

    rows: list[dict] = []
    seen: set[str] = set()

    for p_num, text in _iter_text_fast(input_path):
        if "RESUMEN POR TIPO DE CENTROS PRESUPUESTARIOS" not in text:
            continue
        # Solo procesamos páginas que tengan la columna TOTAL (evita tomar el
        # Cap.5 como total en la página parcial del formato antiguo 2015-2018).
        if not _page_has_total(text):
            continue
        for line in text.splitlines():
            m = RE_CENTRO.match(line)
            if not m:
                continue
            codigo = m.group("codigo")
            denom = re.sub(r"\s+", " ", m.group("denom")).strip().rstrip(",")
            # Última columna = TOTAL del centro
            numeros = m.group("numeros").split()
            importe = parse_eur(numeros[-1])
            # Evitamos duplicar el mismo centro (aparece varias páginas)
            if codigo in seen:
                continue
            seen.add(codigo)
            rows.append(make_row(pagina=p_num, codigo=codigo,
                                 denominacion=denom,
                                 importe=importe, anio=anio))

    motor = "mad-libro-03-centros" if rows else "mad-vacio"
    notes = ""
    if not rows:
        notes = ("Libro 03 no parseable; falta Libro 04 con memoria de "
                 "programas. Adjuntar programas.xlsx para integrar manualmente.")
    return ExtractionResult(rows=rows, motor=motor, notes=notes)
