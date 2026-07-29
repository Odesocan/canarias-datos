"""
extractors/bal.py — Illes Balears.

El portal pressuposts.caib.es publica el "Tom 3 — Estats de despeses"
como un frameset HTML legacy: `menu_tom3_d.html` carga
`desplegable_tom3_d.html`, que es un <SELECT> JavaScript con 27 OPTIONs
(secciones del presupuesto). Cada opción carga
`toms/tom3/titol<N>_d.pdf` con el detalle por capítulo/artículo/
concepto/subconcepto, agrupado por C.Cost (centro de coste) y Programa.

Formato típico de cada PDF de sección:

    C.Cost 18101 Secretaria General de la Conselleria de Salut
    Programa 411A Direcció i serveis generals de la Conselleria de Salut
    CODI Capítol/Article/Concepte/Subconcepte Import
    1 Despeses de personal 6.980.986
    ...
    Total Programa 5.045.365

El mismo programa funcional (e.g. 411A) aparece bajo varios C.Cost
con su propia línea "Total Programa". Este extractor suma esos parciales
por (codigo, denominación) → una fila por programa funcional.

Convención de entrada: el dispatcher pasa la ruta de
`fuentes/raw/bal/<año>/memoria_programas.html`. Buscamos los PDFs
hermanos en `<año>/secciones/titol*_d.pdf`. Si no existen, devolvemos
0 filas con nota explicativa.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult


RE_PROGRAMA = re.compile(
    r"^\s*Programa\s+(?P<codigo>\d{3}[A-Z])\s+(?P<denominacion>.+?)\s*$"
)
RE_TOTAL_PROGRAMA = re.compile(
    rf"^\s*Total\s+Programa\s+(?P<importe>{NUM_RE})\s*€?\s*$"
)
RE_RESUMEN_PROGRAMA = re.compile(
    rf"^\s*(?P<codigo>\d{{3}}[A-Z])\s+"
    rf"(?P<denominacion>.+?)\s+"
    rf"(?P<importe>{NUM_RE})\s*$"
)


def _extract_program_summary_pdf(input_path: Path, anio: int) -> list[dict]:
    """Lee PDFs-resumen con tabla `Clasificación por programas`.

    La prórroga 2026 publica un PDF de estados numéricos, no el frameset
    histórico del Tomo III. Tomamos el bloque de Administración general y
    paramos antes de los presupuestos propios de IB-Salut para no duplicar
    la transferencia sanitaria `411E`.
    """
    rows: list[dict] = []
    in_programs = False
    seen: set[str] = set()
    for p_num, text in base.iter_pdf_text(input_path):
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if "Prórroga de presupuesto del Servicio de Salud" in line:
                return rows
            if "Clasificación por programas" in line:
                in_programs = True
                continue
            if not in_programs:
                continue
            if line.startswith(("Código ", "Capítulo ", "Presupuestos Generales", "Estado de ")):
                continue
            m = RE_RESUMEN_PROGRAMA.match(line)
            if not m:
                continue
            codigo = m.group("codigo")
            if codigo == "011A":  # deuda: fuera del universo Tomo III histórico
                continue
            if codigo in seen:
                continue
            seen.add(codigo)
            rows.append(make_row(pagina=p_num, codigo=codigo,
                                 denominacion=m.group("denominacion"),
                                 importe=m.group("importe"), anio=anio))
    return rows


def _collect_section_pdfs(input_path: Path) -> tuple[list[Path], list[str]]:
    """Devuelve (PDFs de sección reales, nombres de stubs saltados).

    Si `input_path` apunta directamente a un PDF, lo procesamos solo.
    Si apunta al frameset HTML, buscamos `<input_path>.parent/secciones/titol*_d.pdf`.
    Los stubs (índices inexistentes descargados como página de error 404 "No es
    possible…", sin firma %PDF) se SALTAN pero se DEVUELVEN nombrados: un año al
    que le faltan secciones (p.ej. titol0..9 = Educació, Turisme… antes del fix
    2026-07-02, cuando se pedían con cero `titol00` en vez de `titol0` y en el
    path equivocado) degradaba en silencio; ahora el conteo va a `notes`.
    """
    p = Path(input_path)
    if p.suffix.lower() == ".pdf":
        return [p], []
    folder = p.parent / "secciones"
    if not folder.exists():
        return [], []
    reales: list[Path] = []
    stubs: list[str] = []
    for pdf in sorted(folder.glob("titol*_d.pdf")):
        try:
            with open(pdf, "rb") as fh:
                es_pdf = fh.read(5)[:4] == b"%PDF"
        except OSError:
            es_pdf = False
        (reales if es_pdf else stubs).append(pdf if es_pdf else pdf.name)
    return reales, stubs


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows: list[dict] = []
    if Path(input_path).suffix.lower() == ".pdf":
        try:
            rows = _extract_program_summary_pdf(Path(input_path), anio)
        except ImportError:
            return ExtractionResult(rows=[], motor="bal-resumen-programas-pdf",
                                    notes="pdfplumber no disponible")
        if rows:
            return ExtractionResult(
                rows=rows,
                motor="bal-resumen-programas-pdf",
                notes=f"{len(rows)} programas desde Clasificación por programas",
            )

    pdfs, stubs = _collect_section_pdfs(input_path)
    if not pdfs:
        return ExtractionResult(
            rows=[],
            motor="bal-frameset-secciones",
            notes=f"sin PDFs en {Path(input_path).parent / 'secciones'} — descargar titol0..titol25_d.pdf (path toms/tom3/, SIN cero a la izquierda)",
        )
    stub_note = ""
    if stubs:
        stub_note = (f" · ⚠ {len(stubs)} secciones AUSENTES (stubs no-PDF): "
                     f"{','.join(stubs)} — cobertura incompleta, re-descargar de "
                     f"pressuposts.caib.es/.../toms/tom3/ (sin cero a la izquierda)")

    # acumulador por (codigo, denominacion) -> [(pagina, importe), ...]
    acc: dict[tuple[str, str], list[tuple[int, float]]] = defaultdict(list)

    try:
        for pdf in pdfs:
            current = None  # (codigo, denominacion)
            for p_num, text in base.iter_pdf_text(pdf):
                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    m_prog = RE_PROGRAMA.match(line)
                    if m_prog:
                        codigo = m_prog.group("codigo")
                        denom = m_prog.group("denominacion").strip()
                        current = (codigo, denom)
                        continue
                    m_tot = RE_TOTAL_PROGRAMA.match(line)
                    if m_tot and current is not None:
                        acc[current].append((p_num, base.parse_eur(m_tot.group("importe"))))
                        # No reset: el mismo programa puede repetirse en otros C.Cost
                        # con su propio "Programa <code>" antes del siguiente "Total".
                        current = None
    except ImportError:
        return ExtractionResult(rows=[], motor="bal-frameset-secciones",
                                notes="pdfplumber no disponible")

    for (codigo, denom), entries in acc.items():
        total = sum(amt for _, amt in entries if amt == amt)  # NaN-safe
        if total <= 0:
            continue
        pagina = entries[0][0] if entries else None
        rows.append(make_row(pagina=pagina, codigo=codigo,
                             denominacion=denom, importe=total, anio=anio))

    return ExtractionResult(
        rows=rows,
        motor="bal-frameset-secciones",
        notes=f"{len(pdfs)} PDFs sección procesados, {len(rows)} programas únicos{stub_note}",
    )
