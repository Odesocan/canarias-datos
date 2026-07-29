"""
extractors/nav.py — Navarra.

El visor de presupuesto.navarra.es es una SPA JavaScript pero el HTML servido
embebe TODOS los datos en variables `var ... = {…}` dentro de un <script>:

  - `breakdowns.functional.sub[<fcode>].sub[<pcode>]` da el desglose por
    función (2 dígitos) → programa (4 dígitos o 3+letra).  Cada nodo tiene
    {expense: {<year>: <cents>, actual_<year>: <cents>}, income: {…}, label}.
  - `breakdowns.income` y `breakdowns.expense` dan agregados por capítulo.
  - `breakdowns.institutional` está vacío en 2026.

Importes en CENTS, hay que dividir entre 100.  Códigos canónicos en Navarra
tienen la forma `<fcode>.<pcode>`, p.ej. `31.3122` = Sanidad / Atención
primaria de salud, `32.322D` = Educación / Educación primaria.

El JS no es JSON estricto: las claves de los objetos van con comillas
simples y hay comas finales antes de '}/]'.  Normalizamos eso antes de
parsear con `json.loads`.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from .._common import base
from .._common.base import make_row, ExtractionResult, parse_eur


def _extract_js_assignment(html: str, var_name: str) -> str | None:
    """Devuelve el literal JS asignado a `var <name> = …;` con
    emparejamiento balanceado de llaves/corchetes."""
    m = re.search(rf"var\s+{re.escape(var_name)}\s*=\s*", html)
    if not m:
        return None
    start = m.end()
    if start >= len(html) or html[start] not in "{[":
        return None
    open_c = html[start]
    close_c = "}" if open_c == "{" else "]"
    depth = 0
    in_str = False
    escape = False
    i = start
    while i < len(html):
        c = html[i]
        if escape:
            escape = False
        elif c == "\\":
            escape = True
        elif in_str:
            if c == '"' or c == "'":
                in_str = False
        else:
            if c in "\"'":
                in_str = True
            elif c == open_c:
                depth += 1
            elif c == close_c:
                depth -= 1
                if depth == 0:
                    return html[start:i + 1]
        i += 1
    return None


def _js_to_json(s: str) -> str:
    """Convierte un literal JS de tipo objeto en JSON estricto."""
    # Claves entre comillas simples: 'foo': → "foo":
    s = re.sub(r"'([a-zA-Z_]\w*)'\s*:", r'"\1":', s)
    # Claves sin comilla: foo: → "foo":
    s = re.sub(r"([{,]\s*)([a-zA-Z_]\w*)\s*:", r'\1"\2":', s)
    # Comas finales antes de } o ]
    s = re.sub(r",(\s*[}\]])", r"\1", s)
    return s


def _from_csv(input_path: Path, anio: int) -> list[dict]:
    """Si el operador adjunta un CSV/XLSX limpio, gana sobre el HTML."""
    candidatos = list(input_path.parent.glob("programa*.csv")) + \
                 list(input_path.parent.glob("partidas*.csv")) + \
                 list(input_path.parent.glob("gastosf*.csv"))
    # Excluye el HTML mal renombrado del propio input
    candidatos = [c for c in candidatos if c.suffix.lower() != ".html"]
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


def _parse_html(input_path: Path, anio: int) -> list[dict]:
    html = input_path.read_text(encoding="utf-8", errors="replace")
    block = _extract_js_assignment(html, "breakdowns")
    if not block:
        return []
    try:
        data = json.loads(_js_to_json(block))
    except json.JSONDecodeError:
        return []
    f = (data.get("functional") or {}).get("sub") or {}
    if not f:
        return []
    rows: list[dict] = []
    year_str = str(anio)
    for fcode, fnode in f.items():
        if not isinstance(fnode, dict) or fcode == "XX":
            continue
        fname = (fnode.get("label") or "").strip()
        for pcode, pnode in (fnode.get("sub") or {}).items():
            if not isinstance(pnode, dict):
                continue
            plabel = (pnode.get("label") or "").strip()
            exp = (pnode.get("expense") or {}).get(year_str)
            if not exp or exp <= 0:
                continue
            # Importes en CENTS → euros
            importe = float(exp) / 100.0
            codigo = f"{fcode}.{pcode}"
            denom = f"{fname} / {plabel}".strip(" /")
            rows.append(make_row(pagina=None, codigo=codigo,
                                 denominacion=denom, importe=importe,
                                 anio=anio))
    return rows


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # 1) CSV adjunto (más limpio) manda
    rows = _from_csv(input_path, anio)
    if rows:
        return ExtractionResult(rows=rows, motor="nav-csv-adjunto")

    # 2) HTML embebido con breakdowns.functional
    rows = _parse_html(input_path, anio)
    motor = "nav-breakdowns-functional" if rows else "nav-pendiente"
    notes = "" if rows else (
        "No se encontró `var breakdowns = …` en el HTML; comprobar versión."
    )
    return ExtractionResult(rows=rows, motor=motor, notes=notes)
