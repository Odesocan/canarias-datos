"""
extractors/cat.py — Cataluña (Generalitat).

PDF Estats d'Ingressos i Despeses (vol_p_eid.pdf). Cada programa termina con:

    PROGRAMA 310 ALTRES PROGRAMES SOCIALS 18.319,54

Patrón muy fiable. Códigos de 3 dígitos (`310`, `412`, `551`, `111`, `414`, …).
"""
from __future__ import annotations

import re
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult


RE_TOTAL_PROG_CAT = re.compile(
    rf"^\s*PROGRAMA\s+(?P<codigo>\d{{3}}[A-Z]?)\s+"
    rf"(?P<denom>[A-ZÀÁÈÉÍÓÚÏÜÑ].+?)\s+"
    rf"(?P<importe>{NUM_RE})\s*$"
)

# Variante histórica (p.ej. 2015): la línea de programa no trae denominación,
# sólo `PROGRAMA <codigo> <importe>`, y aparece desglosada por sección/servicio.
# Se agregan los importes por código para obtener el total consolidado del
# programa. La denominación queda vacía; el transform asigna concepto por código.
RE_PROG_NO_DENOM_CAT = re.compile(
    rf"^\s*PROGRAMA\s+(?P<codigo>\d{{3}}[A-Z]?)\s+"
    rf"(?P<importe>{NUM_RE})\s*$"
)

# --- Consolidación de la función SALUT (fix 2026-07-01) -----------------------
# La sanidad catalana se financia en cadena de transferencias INTERNES:
#   Generalitat --(prog 415 "Al Servei Català de la Salut")--> CatSalut (entitat
#   5100, ≈ presupuesto sanitario consolidado) --(415 "A l'ICS")--> ICS, que
#   ejecuta prog 411 (primària) y 412 (especialitzada).
# El PDF lista los programas de TODAS las entidades, así que sumar 415 (la
# transferencia = el presupuesto de CatSalut) MÁS 411/412 (la entrega del ICS que
# esa transferencia ya financia) DUPLICA el gasto (~2x, ~2220 €/hab vs ~1340 real).
# Verificado: staging 415 (8.476 B) ≈ CatSalut total (8.475 B, entitat 5100, 2016).
# Decisión: la sanidad = 415 (CatSalut consolidado) + 414/419 (salut pública, aparte);
# se EXCLUYEN 411 y 412 (entrega ICS, subconjunto ya dentro de 415). Per cápita
# resultante ≈ 1340 €/hab (2022), en línea con Madrid/Canarias; sin excluirlos daba
# ~2220 €/hab. Ver logs/progreso.md 2026-07-01.
_SALUT_DOBLE_CONTEO = {"411", "412"}


# Cabeceras del EID detallado que fijan el nivel de agregación de cada página.
_RE_AMBIT = re.compile(r"^\s*Àmbit:\s*(.+?)\s*$")
_RE_SERVEI = re.compile(r"^\s*Servei:\s*")
_SUBSECTOR_GENERALITAT = "Subsector GENERALITAT"


def _page_headers(text: str) -> tuple[str | None, bool]:
    """Devuelve (àmbit de la página o None si no lo trae, ¿tiene cabecera Servei?).

    Las cabeceras aparecen SIEMPRE en las primeras líneas de la página; se
    limita la búsqueda a ellas para no confundir una denominación de programa
    que contenga la palabra con una cabecera real.
    """
    ambit = None
    has_servei = False
    for line in text.splitlines()[:10]:
        m = _RE_AMBIT.match(line)
        if m:
            ambit = m.group(1)
        elif _RE_SERVEI.match(line):
            has_servei = True
    return ambit, has_servei


def extract(input_path: Path, anio: int) -> ExtractionResult:
    """Total consolidado de cada programa dentro del Subsector GENERALITAT.

    El EID detallado lista cada programa UNA VEZ POR SERVEI, y repite el mismo
    programa en otros subsectores (entitats autònomes, consorcis, societats…)
    que la Generalitat financia por transferencia interna.  Sumar la línea
    `PROGRAMA <cód> <denom> <importe>` de todas las páginas de detalle
    (cabecera `Servei:`) del Subsector GENERALITAT da el total consolidado del
    programa SIN doble conteo:
      - dentro de GENERALITAT no hay líneas PROGRAMA a nivel agregado
        (Secció/Àmbit), verificado 2015/2016/2026 → sumar los serveis es exacto;
      - excluir los demás subsectores evita contar dos veces las transferencias
        internas (mismo criterio que la cadena SALUT 415→411/412).
    Antes de 2026-07-02 el motor se quedaba con la PRIMERA aparición de cada
    programa (first-wins), truncando los programas multi-servei: educació ×3,3,
    universitats ×87, dependència ×15,7 infra-extraídas (sanidad se salvaba por
    accidente al ser 415 mono-servei).  Maneja los dos formatos de línea: con
    denominación (2016+) y sin ella (2015).
    """
    sums: dict[str, float] = {}
    denoms: dict[str, str] = {}
    last_page: dict[str, int] = {}
    cur_ambit: str | None = None
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            ambit, has_servei = _page_headers(text)
            if ambit is not None:
                cur_ambit = ambit  # persiste en páginas de continuación sin cabecera
            if cur_ambit != _SUBSECTOR_GENERALITAT or not has_servei:
                continue
            for line in text.splitlines():
                line = line.strip()
                if not line.startswith("PROGRAMA "):
                    continue
                m = RE_TOTAL_PROG_CAT.match(line)
                denom = m.group("denom").strip() if m else ""
                if not m:
                    m = RE_PROG_NO_DENOM_CAT.match(line)
                    if not m:
                        continue
                codigo = m.group("codigo")
                if codigo in _SALUT_DOBLE_CONTEO:
                    continue  # entrega ICS ya dentro de la transferencia 415 (ver arriba)
                val = base.parse_eur(m.group("importe"))
                if val != val:  # NaN
                    continue
                sums[codigo] = sums.get(codigo, 0.0) + val
                if denom and codigo not in denoms:
                    denoms[codigo] = denom
                last_page[codigo] = p_num
    except ImportError:
        return ExtractionResult(rows=[], motor="cat", notes="pdfplumber no disponible")

    rows = [make_row(pagina=last_page.get(codigo), codigo=codigo,
                     denominacion=denoms.get(codigo, ""), importe=float(total),
                     anio=anio)
            for codigo, total in sums.items()]

    if not rows:
        return ExtractionResult(
            rows=[], motor="cat-pendiente",
            notes=("Sin líneas PROGRAMA en páginas 'Subsector GENERALITAT' con "
                   "cabecera 'Servei:'. ¿Cambió el formato del vol_p_eid?"))

    return ExtractionResult(rows=rows, motor="cat-programa-generalitat-suma")
