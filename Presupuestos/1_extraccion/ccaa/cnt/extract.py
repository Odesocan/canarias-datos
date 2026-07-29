"""
extractors/cnt.py — Cantabria.

PDF `ingresos_gastos.pdf` (Tomo I, Estado de Gastos). Cada programa funcional
aparece en cabeceras del tipo:

      SECCIÓN                01      PARLAMENTO DE CANTABRIA
      SERVICIO               00      PARLAMENTO DE CANTABRIA
      PROGRAMA              911M     ACTIVIDAD LEGISLATIVA

… y termina (varias páginas más adelante) con la línea agregada del programa
dentro de ese servicio:

                                                  TOTAL PROGRAMA:      9.327.289

Importes en euros enteros (formato es-ES con punto como separador de miles).
Un mismo programa puede repartirse entre varios servicios (p.ej. 140A
"PERSONAL" aparece en 20 servicios distintos), por lo que SUMAMOS todos los
"TOTAL PROGRAMA" por código para obtener el total del programa.

Soporta enriquecimiento opcional con `totales_program*.xlsx|csv` adjunto en el
mismo directorio: si está, **prevalece** sobre el parser PDF (suele venir más
limpio de mano del operador).
"""
from __future__ import annotations

import csv
import re
import shutil
import subprocess
from pathlib import Path

from .._common import base
from .._common.base import make_row, ExtractionResult, parse_eur


def _iter_text_fast(path: Path):
    """Itera texto del PDF usando pdftotext (poppler) si está disponible.
    Es 10–50x más rápido que pdfplumber para PDFs grandes y suficiente para
    extraer cabeceras + 'TOTAL PROGRAMA'. Devuelve [(page_num, page_text)].
    Fallback a pdfplumber si pdftotext no está disponible.
    """
    if shutil.which("pdftotext"):
        try:
            out = subprocess.check_output(
                ["pdftotext", "-layout", str(path), "-"], timeout=120
            ).decode("utf-8", errors="replace")
            # pdftotext separa páginas con form feed \f
            for i, page in enumerate(out.split("\f"), start=1):
                yield i, page
            return
        except Exception:
            pass
    # Fallback más lento
    yield from base.iter_pdf_text(path)


# Cabecera de programa en cada página: "PROGRAMA  <cod>  <denom>"
# El código suele ser 3 dígitos + 1 letra (ej. 911M, 134M, 412A, 322B…).
RE_PROG_HDR = re.compile(
    r"^\s*PROGRAMA\s+(?P<codigo>\d{3}[A-Z])\s+(?P<denom>.+?)\s*$"
)
# Línea de cierre por programa-servicio: "TOTAL PROGRAMA:   9.327.289"
RE_TOTAL = re.compile(
    r"TOTAL\s+PROGRAMA\s*:\s*(?P<importe>[\d\.]+(?:,\d+)?)\s*$"
)
# Variante "Anexo de Desarrollo Económico de Gasto por Centros Gestores" (años
# antiguos, p.ej. 2015): NO trae "TOTAL PROGRAMA" sino "TOTAL CAPÍTULO:" por cada
# capítulo dentro del programa. El total del programa = suma de sus capítulos.
RE_TOTAL_CAP = re.compile(
    r"TOTAL\s+CAP[IÍ]TULO\s*:\s*(?P<importe>[\d\.]+(?:,\d+)?)\s*$"
)

# --- Fallback política-de-gasto (años solo publicados como Ley en el BOC) ---
# Para 2015-2017, las únicas fuentes son el TEXTO LEGAL del BOC, que NO trae el
# Estado de Gastos por programa pero SÍ una tabla "POLÍTICA DE GASTOS / EUROS"
# (Artículo 2) por área de gasto (2 dígitos), en euros enteros. Es más gruesa
# (~19 filas, < umbral VERDE) pero exacta a nivel de concepto. Línea de dato:
#   "31 SANIDAD 788.821.603"  o, si el nombre se parte:  "13 13.909.692"
RE_POL_DATA = re.compile(
    r"^(?P<cod>\d{2})\s+(?P<mid>.*?)(?P<imp>\d{1,3}(?:\.\d{3})+)\s*$"
)


def _enriquecer_con_xlsx(input_path: Path, anio: int) -> ExtractionResult | None:
    candidatos = list(input_path.parent.glob("totales_program*.xlsx")) + \
                 list(input_path.parent.glob("totales_program*.csv"))
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
    else:
        try:
            from openpyxl import load_workbook  # type: ignore
        except ImportError:
            return None
        wb = load_workbook(filename=str(src), data_only=True, read_only=True)
        ws = wb.active
        xrows = list(ws.iter_rows(values_only=True))
        if not xrows:
            return None
        header = [str(c).strip().lower() if c else "" for c in xrows[0]]
        try:
            ic = header.index("codigo"); idn = header.index("denominacion"); ii = header.index("importe_eur")
        except ValueError:
            return None
        for r in xrows[1:]:
            if r[ic]:
                rows.append(make_row(pagina=None, codigo=str(r[ic]).strip(),
                                     denominacion=str(r[idn] or ""),
                                     importe=parse_eur(r[ii]),
                                     anio=anio))
    return ExtractionResult(rows=rows, motor="cnt-xlsx-adjunto") if rows else None


def _parse_politica_boc(input_path: Path, anio: int) -> list[dict]:
    """Fallback: tabla 'POLÍTICA DE GASTOS / EUROS' del Artículo 2 (Ley BOC).

    Reconstruye los nombres que el PDF parte en varias líneas (p.ej. la política
    13 aparece como 'SEGURIDAD…' / '13 13.909.692' / 'PENITENCIARIAS')."""
    rows: list[dict] = []
    try:
        pages = list(_iter_text_fast(input_path))
    except Exception:
        return rows
    for p_num, text in pages:
        if "POLÍTICA DE GASTOS" not in text.upper() and "POLITICA DE GASTOS" not in text.upper():
            continue
        lines = [l.strip() for l in text.splitlines()]
        entries: list[list] = []          # [cod, name_inline, imp, idx]
        text_frag: dict[int, str] = {}    # idx -> fragmento de nombre (línea sin dato)
        for idx, l in enumerate(lines):
            m = RE_POL_DATA.match(l)
            if m and 10 <= int(m.group("cod")) <= 99:
                imp = parse_eur(m.group("imp"))
                entries.append([m.group("cod"), m.group("mid").strip(" .,"), imp, idx])
            elif re.match(r"^[A-ZÁÉÍÓÚÑ]", l) and not re.search(r"\d{3}", l):
                text_frag[idx] = l
        for e in entries:
            if len(e[1]) < 4:  # nombre partido → unir fragmentos adyacentes
                e[1] = (text_frag.get(e[3] - 1, "") + " " + text_frag.get(e[3] + 1, "")).strip()
        seen: set[str] = set()
        for cod, name, imp, _idx in entries:
            if cod in seen or not imp or imp != imp or imp <= 0:
                continue
            seen.add(cod)
            rows.append(make_row(pagina=p_num, codigo=cod, denominacion=name,
                                 importe=imp, anio=anio))
        if rows:
            break
    return rows


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # Si hay un XLSX/CSV adjunto del operador, gana
    alt = _enriquecer_con_xlsx(input_path, anio)
    if alt is not None and len(alt.rows) >= 20:
        return alt

    # Acumuladores por codigo
    agg_importe: dict[str, float] = {}      # vía "TOTAL PROGRAMA:" (2018-2026)
    agg_capitulo: dict[str, float] = {}     # vía suma de "TOTAL CAPÍTULO:" (centros gestores)
    denom_by_codigo: dict[str, str] = {}
    pagina_by_codigo: dict[str, int] = {}
    current_codigo: str | None = None

    try:
        for p_num, text in _iter_text_fast(input_path):
            for line in text.splitlines():
                # 1) Actualizar programa "activo" cuando vemos cabecera
                m_hdr = RE_PROG_HDR.match(line)
                if m_hdr:
                    current_codigo = m_hdr.group("codigo")
                    current_denom = m_hdr.group("denom").strip()
                    if current_codigo not in pagina_by_codigo:
                        pagina_by_codigo[current_codigo] = p_num
                    prev = denom_by_codigo.get(current_codigo, "")
                    # Guardamos la denominación más larga (más completa)
                    if len(current_denom) > len(prev):
                        denom_by_codigo[current_codigo] = current_denom
                    continue

                # 2) Capturar TOTAL PROGRAMA y acumular sobre el programa activo
                m_tp = RE_TOTAL.search(line)
                if m_tp and current_codigo is not None:
                    importe = parse_eur(m_tp.group("importe"))
                    if importe == importe:  # not NaN
                        agg_importe[current_codigo] = agg_importe.get(current_codigo, 0.0) + importe
                    continue

                # 3) Variante centros gestores: sumar "TOTAL CAPÍTULO:" por programa
                m_tc = RE_TOTAL_CAP.search(line)
                if m_tc and current_codigo is not None:
                    importe = parse_eur(m_tc.group("importe"))
                    if importe == importe:
                        agg_capitulo[current_codigo] = agg_capitulo.get(current_codigo, 0.0) + importe
    except ImportError:
        return ExtractionResult(rows=[], motor="cnt", notes="pdfplumber no disponible")

    # Elegir la fuente de totales: "TOTAL PROGRAMA" si existe; si no, suma de
    # capítulos (formato Anexo de Desarrollo Económico por Centros Gestores).
    if len(agg_importe) >= 20:
        agg, motor_tot = agg_importe, "cnt-total-programa-suma-servicios"
    elif len(agg_capitulo) >= 20:
        agg, motor_tot = agg_capitulo, "cnt-centros-suma-capitulos"
    else:
        agg, motor_tot = agg_importe, "cnt-total-programa-suma-servicios"

    rows: list[dict] = []
    for codigo, importe_total in agg.items():
        rows.append(make_row(
            pagina=pagina_by_codigo.get(codigo),
            codigo=codigo,
            denominacion=denom_by_codigo.get(codigo, ""),
            importe=importe_total,
            anio=anio,
        ))

    # Fallback política-de-gasto (Ley BOC sin Estado de Gastos por programa):
    # se activa cuando el parse por programa no encontró la estructura habitual.
    if len(rows) < 20:
        pol = _parse_politica_boc(input_path, anio)
        if len(pol) > len(rows):
            return ExtractionResult(
                rows=pol, motor="cnt-politica-gastos-boc",
                notes=(f"{len(pol)} políticas de gasto (área 2-díg, Ley BOC) — "
                       "granularidad gruesa, no por programa"),
            )

    motor = motor_tot if rows else "cnt-vacio"
    return ExtractionResult(rows=rows, motor=motor)
