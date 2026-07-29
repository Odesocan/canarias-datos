"""
extractors/clm.py — Castilla-La Mancha.

PDF Tomo I (`tomo_I.pdf`). Sección "RESUMEN POR SECCIONES Y PROGRAMAS"
(pág. 122 en el ejercicio 2026). Cada bloque por sección sigue el patrón:

    Sección          11              PRESIDENCIA DE LA JUNTA DE COMUNIDADES DE C-LM
                                                              (IMPORTE EN MILES DE EUROS)
      CÓDIGO                          Programa                         IMPORTE
     112A      DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA           21.047,56
     126C      MEDIOS DE COMUNICACIÓN                                       2.582,92
     ...
                                                    Total   Sección       27.890,22

Patrón de línea: `<código 4 chars: 3 dígitos + letra> <denominación> <importe es-ES>`.
IMPORTANTE: los importes están en MILES de euros → se multiplican por 1.000.

Fallback opcional: si existe un XLSX/CSV adjunto `programas*.{xlsx,csv}` en el
mismo directorio, se prioriza.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult, parse_eur


# Línea típica:   "  112A      DIRECCIÓN Y SERVICIOS GENERALES DE LA PRESIDENCIA   21.047,56"
# Código: 3 dígitos + letra. Importe en miles de euros (es-ES).
RE_PROG_CLM = re.compile(
    rf"^\s*(?P<codigo>\d{{3}}[A-Z])\s+(?P<denom>[A-ZÁÉÍÓÚÑÜ][^\d]*?)\s+(?P<importe>{NUM_RE})\s*$"
)
# Línea de "Total Sección …" — la usamos como marcador de fin de bloque pero no extraemos.
RE_TOTAL_SEC = re.compile(r"^\s*Total\s+Sección", re.IGNORECASE)


def _extract_from_xlsx_or_csv(input_path: Path, anio: int) -> ExtractionResult | None:
    """Si hay un programas*.xlsx o programas*.csv adjunto, úsalo (operador manual)."""
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
    return ExtractionResult(rows=rows, motor="clm-xlsx-adjunto") if rows else None


def _to_float_en(s) -> float:
    """Importe en formato en-US (punto decimal, sin separador de miles)."""
    s = (str(s) if s is not None else "").strip()
    if not s:
        return float("nan")
    try:
        return float(s)
    except ValueError:
        # tolera formato es-ES por si acaso (1.234.567,89)
        return parse_eur(s)


def _split_csv_line(line: str) -> list[str]:
    """Parser tolerante con el dialecto del datos abiertos CLM.

    Algunas líneas que contienen una coma dentro de un campo vienen con la
    LÍNEA COMPLETA entre comillas y las comillas internas duplicadas
    (`""` -> `"`). Se desenvuelve antes de delegar en csv.reader.
    """
    line = line.rstrip("\r\n")
    if len(line) >= 2 and line.startswith('"') and line.endswith('"'):
        line = line[1:-1].replace('""', '"')
    return next(csv.reader([line]))


def _extract_gastos_articulo_csv(input_path: Path, anio: int) -> ExtractionResult:
    """Datos abiertos CLM — gasto funcional multi-año (`gastosf-*.csv`).

    Columnas: Año, Id Política, Nombre Política, Id Programa, Nombre Programa,
    Presupuesto Gasto, Gasto Real. Filtra por `anio`, toma las filas de detalle
    (Id Programa no vacío; se descartan los subtotales de política) y usa
    `Presupuesto Gasto` (euros, formato en-US). El código de programa (3 díg+letra)
    lo mapea a concepto el transform vía correspondencias.yml.
    """
    with input_path.open("r", encoding="utf-8-sig") as fh:
        try:
            header = _split_csv_line(fh.readline())
        except StopIteration:
            return ExtractionResult(rows=[], motor="clm-gastosf-csv", notes="csv vacío")
        idx = {h.strip().lower(): i for i, h in enumerate(header)}

        def col(*cands):
            for c in cands:
                if c in idx:
                    return idx[c]
            return None

        i_anio = col("año", "ano", "anio")
        i_prog = col("id programa", "id_programa", "idprograma")
        i_nom = col("nombre programa", "nombre_programa")
        i_imp = col("presupuesto gasto", "presupuesto_gasto", "presupuesto")
        if None in (i_anio, i_prog, i_nom, i_imp):
            return ExtractionResult(rows=[], motor="clm-gastosf-csv",
                                    notes=f"cabecera inesperada: {header}")

        target = str(anio).strip()
        need = max(i_anio, i_prog, i_nom, i_imp)
        rows: list[dict] = []
        seen: set[str] = set()
        for raw in fh:
            if not raw.strip():
                continue
            try:
                r = _split_csv_line(raw)
            except Exception:
                continue
            if len(r) <= need:
                continue
            if r[i_anio].strip() != target:
                continue
            codigo = (r[i_prog] or "").strip()
            if not codigo or codigo in seen:   # subtotal de política o duplicado
                continue
            seen.add(codigo)
            rows.append(make_row(pagina=None, codigo=codigo,
                                 denominacion=(r[i_nom] or "").strip(),
                                 importe=_to_float_en(r[i_imp]), anio=anio))
    return ExtractionResult(rows=rows, motor="clm-gastosf-csv")


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # Datos abiertos CLM (gasto funcional multi-año) — rama CSV (2015-2021)
    if input_path.suffix.lower() == ".csv":
        res_csv = _extract_gastos_articulo_csv(input_path, anio)
        if res_csv.rows:
            return res_csv
        # si no es el CSV esperado, sigue con el flujo PDF/fallback

    # PDF vacío → cae al fallback adjunto
    if input_path.stat().st_size == 0:
        alt = _extract_from_xlsx_or_csv(input_path, anio)
        if alt is not None:
            return alt
        return ExtractionResult(rows=[], motor="clm-empty",
                                notes="PDF descargado vacío — revisar canonical_url")

    # Si hay un adjunto manual, gana sobre el PDF (operador conoce mejor el dato)
    alt = _extract_from_xlsx_or_csv(input_path, anio)
    if alt is not None and len(alt.rows) >= 30:
        return alt

    rows: list[dict] = []
    seen: set[tuple[str, int]] = set()
    in_resumen = False  # entra cuando vemos cabecera "GASTOS. RESUMEN POR SECCIONES Y PROGRAMAS"
    # No usamos el índice porque el TOC también contiene esos rótulos.

    try:
        for p_num, text in base.iter_pdf_text(input_path):
            has_section_header = "GASTOS. RESUMEN POR SECCIONES Y PROGRAMAS" in text
            if has_section_header:
                in_resumen = True
            if not in_resumen:
                continue
            # Salimos cuando entramos a "DISTRIBUCIÓN DE CAPÍTULOS POR SECCIONES" (sin TOC)
            if "DISTRIBUCIÓN DE CAPÍTULOS POR SECCIONES" in text and not has_section_header:
                break
            for line in text.splitlines():
                line_strip = line.strip()
                if not line_strip:
                    continue
                # Saltar headers de tabla y subtotales
                if RE_TOTAL_SEC.match(line_strip):
                    continue
                if line_strip.startswith("CÓDIGO") or line_strip.startswith("Sección"):
                    continue
                m = RE_PROG_CLM.match(line)
                if not m:
                    continue
                codigo = m.group("codigo")
                denom = m.group("denom").strip()
                # Importe en MILES de euros → x1000
                importe_miles = base.parse_eur(m.group("importe"))
                importe_eur = importe_miles * 1000.0 if importe_miles == importe_miles else importe_miles
                key = (codigo, p_num)
                if key in seen:
                    continue
                seen.add(key)
                rows.append(make_row(pagina=p_num, codigo=codigo,
                                     denominacion=denom,
                                     importe=importe_eur,
                                     anio=anio))
    except ImportError:
        return ExtractionResult(rows=[], motor="clm",
                                notes="pdfplumber no disponible")

    return ExtractionResult(rows=rows, motor="clm-tomo-I-resumen-secciones")
