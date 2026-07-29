"""
extractors/ara.py — Aragón.

Formato típico (Aragón 2024 ingresos_gastos.pdf):
    SECCION 10 PRESIDENCIA, INTERIOR Y CULTURA
    SERVICIO 010 S.G.T. PRESIDENCIA, INTERIOR Y CULTURA
    PROGRAMA 1216 COMUNIDADES ARAGONESAS EN EL EXTERIOR
    ...
    TOTAL PROGRAMA 399.809,84

Cada página suele contener un único programa con su PROGRAMA <code> + TOTAL.
Códigos: 4 dígitos (subprograma) ó 4d+letra.
"""
from __future__ import annotations

import re
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult


RE_HEADER = re.compile(
    r"^\s*(?:PROGRAMA|Programa)\s+(?P<codigo>\d{4}[A-Z]?)\s+(?P<denominacion>.+)$"
)
RE_TOTAL = re.compile(
    rf"^\s*(?:TOTAL\s+PROGRAMA|Total\s+Programa)\s+(?P<importe>{NUM_RE})\s*€?\s*$"
)

# --- Consolidación del perímetro: neteo de transferencias internas a OOAA ------
# (fix 2026-07-20, generaliza y SUSTITUYE al hardcode de 4131 del 2026-07-01)
#
# El documento consolida en un mismo tomo los DEPARTAMENTOS (secciones < 50) y sus
# ORGANISMOS AUTÓNOMOS (secciones 51-78: Servicio Aragonés de Salud, IASS, INAEM,
# Instituto Aragonés del Agua, IAF…). Como el extractor suma PROGRAMA+TOTAL de
# TODAS las secciones, cada euro que el Departamento transfiere a su OOAA se cuenta
# DOS veces: una como transferencia (art. 41 corriente / 71 capital "A ORGANISMOS
# AUTÓNOMOS") y otra como ejecución real en la sección del OOAA.
#
# Ejemplos verificados en 2024 (mismo patrón 2015-2026):
#   · sec 16 SANIDAD prog 4131 (2.633 M) → 2.469 M art.41 + 97 M art.71 al SALUD,
#     que ejecuta sec 52 prog 4121. Netos quedan 67 M de gasto propio del Dpto.
#   · sec 20 BIENESTAR prog 3132 (432 M) → 418 M art.41 al IASS, que ejecuta el
#     mismo prog 3132 en sec 53 (456 M). Netos quedan 14 M propios.
#
# Regla: se RESTA del TOTAL PROGRAMA el importe de las líneas de ARTÍCULO
# "41|71 A ORGANISMOS AUTÓNOMOS" del bloque. Se cuenta así UNA sola vista
# (la ejecución del OOAA) conservando el gasto propio del Departamento — más
# preciso que el hardcode anterior, que descartaba el programa 4131 entero.
# Efecto estable y sin seam: -25 % a -28 % del total en TODOS los años 2017-2026.
#
# Ver 1_extraccion/ccaa/LIMITACIONES.md §3 (contar una vista, no dos) y los fixes
# homólogos de and (centro gestor), ast (páginas de anexo) y cym (400/401/700/701).
#
# FIX 2026-07-27: re.IGNORECASE añadido. El tomo de 2015 usa mayúscula solo
# inicial ("41 A Organismos Autónomos"), a diferencia de 2017-2026 que van en
# VERSALES ("41 A ORGANISMOS AUTÓNOMOS"). Sin el flag, el neteo no se aplicaba
# en 2015 y el programa 3132 (sec 16, 100% transferencia, 287.920.291,85 €)
# pasaba íntegro como fila espuria, duplicando la ejecución del IASS en sec 53
# (302.993.491,48 €) — ~288 M€ de doble conteo en un solo año. Ver
# logs/progreso.md 2026-07-27.
RE_TRANSF_OOAA = re.compile(
    rf"^\s*(?:41|71)\s+A\s+ORGANISMOS\s+AUT[ÓO]NOMOS\s+(?P<importe>{NUM_RE})\s*€?\s*$",
    re.IGNORECASE,
)


def _unwrap_importes(text: str) -> str:
    """Rejunta importes partidos por salto de línea.

    En los tomos 2015-2021 el ancho de columna corta el decimal:
        '41 A ORGANISMOS AUTÓNOMOS 1.821.394.004,'
        '04'
    Sin esto, el neteo pasaba de -27 % (2019) a -6 % y fabricaba un seam falso.
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        while i + 1 < len(lines):
            m = re.search(r",(\d{0,1})$", ln)
            if not m:
                break
            m2 = re.match(r"^(\d{1,2})(?!\d)\s*$", lines[i + 1].strip())
            if not m2:
                break
            ln = ln + m2.group(1)[: 2 - len(m.group(1))]
            i += 1
        out.append(ln)
        i += 1
    return "\n".join(out)


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows: list[dict] = []
    # Transferencias a OOAA acumuladas del bloque de programa en curso. Un bloque
    # abarca varias páginas (la cabecera PROGRAMA se repite; el TOTAL sólo aparece
    # en la última), así que el acumulador NO se reinicia por página: sólo al
    # cerrar el programa con su TOTAL.
    pend_transf = 0.0
    n_neteados = 0
    total_neteado = 0.0
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            current = None
            for line in _unwrap_importes(text).splitlines():
                line = line.strip()
                if not line:
                    continue
                m_hdr = RE_HEADER.match(line)
                if m_hdr:
                    current = (m_hdr.group("codigo"),
                               m_hdr.group("denominacion").strip())
                    continue
                m_tr = RE_TRANSF_OOAA.match(line)
                if m_tr:
                    pend_transf += base.parse_eur(m_tr.group("importe"))
                    continue
                m_tot = RE_TOTAL.match(line)
                if m_tot and current is not None:
                    importe = base.parse_eur(m_tot.group("importe")) - pend_transf
                    if pend_transf:
                        n_neteados += 1
                        total_neteado += pend_transf
                    pend_transf = 0.0
                    # Un programa que era pura transferencia queda en ~0: no aporta
                    # gasto propio y su ejecución ya consta en la sección del OOAA.
                    if importe > 0.005:
                        rows.append(make_row(pagina=p_num, codigo=current[0],
                                              denominacion=current[1],
                                              importe=importe,
                                              anio=anio))
                    current = None
    except ImportError:
        return ExtractionResult(rows=[], motor="ara",
                                 notes="pdfplumber no disponible")

    notes = (f"neteo transferencias internas a OOAA: {n_neteados} programas, "
             f"{total_neteado / 1e6:.1f} M€ descontados")
    return ExtractionResult(rows=rows, motor="ara-pdf-program-total", notes=notes)
