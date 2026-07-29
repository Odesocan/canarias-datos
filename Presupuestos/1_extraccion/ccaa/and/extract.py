"""
extractors/and.py — Andalucía.

Formato Andalucía (PDF "memoria_programas" / "tomo12-5b"):

    RESUMEN CAPÍTULOS-PROGRAMAS
    SECCIÓN: CONSEJERÍA DE SANIDAD ... 0100
    CAPÍTULOS I II III IV V ... TOTAL
    PROGRAMAS                       GENERAL
    11A D.S.G. PRESIDENCIA Y EMERGENCIAS 65.984.139 14.482.560 ... 87.391.701
    22B INTERIOR, EMERGENCIAS Y PROTECCIÓN CIVIL 10.914.428 ... 311.323.690
    TOTAL FUNCIÓN 11 ...
    TOTAL GRUPO 1 ...

Códigos: 2-3 dígitos + letra (`11A`, `22B`, `52C`, `41M`, `41A`, `61N`, `31P`,
`32G`, ...) — clasificación funcional Junta de Andalucía.

Estrategia: captar líneas con `^<codigo> <denom> [<n_capitulos> ...] <total>$`
en las páginas RESUMEN. El último número es el total del programa.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, parse_eur, ExtractionResult


# Código funcional Junta de Andalucía: 2-3 dígitos + letra mayúscula
RE_CODIGO_AND = r"\d{2,3}[A-Z]"


# ---------------------------------------------------------------------------
# Rama CSV — ejercicios publicados en el portal de datos abiertos (CKAN)
# ---------------------------------------------------------------------------
# Algunos ejercicios (p.ej. 2015) no tienen PDF "tomo de programas" sino el
# CSV de líneas de gasto del portal datosabiertos.juntadeandalucia.es:
#   EJERCICIO;CENTRO GESTOR;FUNCIONAL;ECONOMICA;FINANCIACION;DESCRIPCION;IMPORTE
# Se agrega IMPORTE por código FUNCIONAL (= programa, p.ej. 41C, 42D) para
# reproducir las mismas filas programa+total que emite la rama PDF. El nombre
# del programa se toma del CSV-diccionario `estructura_funcional_*.csv`
# (columna SUBFUNCION -> DESCRIPCION), si está disponible junto al input.

def _nombres_funcionales(folder: Path) -> dict[str, str]:
    """Mapa código funcional -> denominación, leído del CSV-diccionario."""
    nombres: dict[str, str] = {}
    for cand in sorted(folder.glob("estructura_funcional*.csv")):
        try:
            with cand.open(encoding="utf-8-sig") as fh:
                for x in csv.DictReader(fh, delimiter=";"):
                    sf = (x.get("SUBFUNCION") or "").strip()
                    if sf:
                        nombres[sf] = (x.get("DESCRIPCION LARGA")
                                       or x.get("DESCRIPCION CORTA") or "").strip()
        except Exception:
            continue
    return nombres


def _extract_csv(input_path: Path, anio: int) -> ExtractionResult:
    """Agrega el CSV de líneas de gasto CKAN por programa funcional.

    Perímetro consolidado (fix 2026-07-16): solo se suman las filas cuyo
    CENTRO GESTOR es una consejería (dígitos 3-4 == "00"). Las filas de
    organismos/agencias (SAS `xx31...`, SAE, agencias `xx39/5x...`) ejecutan
    dinero que YA figura como transferencia en los programas de su consejería
    (p.ej. 41H financia el 41C/41G del SAS): sumar ambas vistas duplicaba
    sanidad ~×2 en 2015/16/20/21. Con el filtro, los totales cuadran con el
    presupuesto publicado de la Junta (2020: 38,28 B ≈ 38,5 B oficial) y la
    serie es continua con la rama PDF (perímetro secciones).
    """
    nombres = _nombres_funcionales(input_path.parent)
    agg: dict[str, float] = {}
    fuera_n, fuera_eur = 0, 0.0
    try:
        with input_path.open(encoding="utf-8-sig") as fh:
            rdr = csv.DictReader(fh, delimiter=";")
            cols = {(c or "").strip().upper(): c for c in (rdr.fieldnames or [])}
            fcol, icol = cols.get("FUNCIONAL"), cols.get("IMPORTE")
            gcol = cols.get("CENTRO GESTOR")
            if not fcol or not icol:
                return ExtractionResult(
                    rows=[], motor="and-ckan-csv",
                    notes="columnas FUNCIONAL/IMPORTE ausentes — ¿no es CSV CKAN?")
            for row in rdr:
                fn = (row.get(fcol) or "").strip()
                if not fn:
                    continue
                v = parse_eur(row.get(icol))
                if v != v:  # NaN
                    continue
                cg = (row.get(gcol) or "").strip() if gcol else ""
                if len(cg) >= 4 and cg[2:4] != "00":
                    fuera_n += 1
                    fuera_eur += v
                    continue
                agg[fn] = agg.get(fn, 0.0) + v
    except Exception as e:  # noqa: BLE001
        return ExtractionResult(rows=[], motor="and-ckan-csv",
                                notes=f"error leyendo CSV: {e}")

    rows: list[dict] = []
    for cod, imp in sorted(agg.items()):
        if imp <= 0:
            continue
        rows.append(make_row(pagina=None, codigo=cod,
                             denominacion=nombres.get(cod, ""),
                             importe=imp, anio=anio))
    notes = (f"{len(rows)} programas funcionales agregados desde CSV · "
             f"{fuera_n} líneas de organismos/agencias excluidas "
             f"({fuera_eur/1e9:.2f} B ya contados como transferencia)")
    if not gcol:
        notes += " · ⚠️ sin columna CENTRO GESTOR: perímetro NO consolidado"
    return ExtractionResult(rows=rows, motor="and-ckan-csv", notes=notes)

# Línea de programa en el RESUMEN: cod denom (números intermedios) total
RE_PROGRAMA_AND = re.compile(
    rf"^\s*(?P<codigo>{RE_CODIGO_AND})\s+"
    rf"(?P<denom>[A-Za-zÁÉÍÓÚÑáéíóúñÜü].+?)\s+"
    rf"(?P<importe>{NUM_RE})\s*$"
)

# Cabecera de sección/consejería en las páginas resumen.
RE_SECCION_AND = re.compile(r"SECCIÓN:\s*(.+)", re.IGNORECASE)


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # Enrutado por tipo de fuente: CSV de líneas de gasto (CKAN) vs PDF de
    # tomo de programas. La rama CSV cubre ejercicios sin PDF (p.ej. 2015).
    p = Path(input_path)
    if p.suffix.lower() == ".csv":
        return _extract_csv(p, anio)

    rows: list[dict] = []
    seen_keys = set()
    seccion = ""  # se arrastra entre páginas (una sección abarca varias)
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            if "RESUMEN CAPÍTULOS-PROGRAMAS" not in text and "RESUMEN CAPITULOS-PROGRAMAS" not in text:
                # Solo procesamos páginas con la rúbrica resumen
                continue
            # Las cabeceras "TOTAL FUNCIÓN" / "TOTAL GRUPO" / "TOTAL GENERAL"
            # también matchearían si no se filtran
            for line in text.splitlines():
                line = line.strip()
                ms = RE_SECCION_AND.search(line)
                if ms:
                    seccion = ms.group(1).upper()
                if not line or line.startswith("TOTAL "):
                    continue
                m = RE_PROGRAMA_AND.match(line)
                if not m:
                    continue
                codigo = m.group("codigo")
                # Filtra falsos positivos: el código debe empezar con dígito (ya garantizado)
                # y la denominación no debe ser sólo dígitos
                denom = m.group("denom").strip()
                if not denom or denom.isdigit():
                    continue
                # --- Fix hueco sanidad 2024-2026 (section-aware, 2026-07-01) ------
                # La transferencia al Servicio Andaluz de Salud (SAS) —el grueso
                # del gasto sanitario, ~13 B€— se recodificó de programa 41H
                # "Planificación y Financiación" (≤2022, función 41) a 12S
                # "Dirección y Servicios Generales" (≥2024, función 12). El motor
                # mapea 41*→sanidad pero no 12S, así que 2024-2026 caían a ~0. En la
                # sección de la CONSEJERÍA DE SALUD, los programas de dirección (12x)
                # SON presupuesto sanitario (la transferencia al SAS) → se recodifican
                # a 41H para que mapeen a sanidad y la serie sea consistente con 2022.
                if ("SALUD" in seccion or "SANIDAD" in seccion) and codigo.startswith("12"):
                    codigo = "41H"
                # Clave de dedup POR SECCIÓN (fix 2026-07-22): Andalucía reutiliza el
                # mismo código de programa en varias secciones con idéntica denominación
                # (p.ej. `81B` "COOPER. ECONÓMICA..." en Economía 0,001 B y en
                # Corporaciones Locales P.I.E. 3,153 B; `71F` en Agricultura 0,155 B y en
                # FAGA 1,569 B; `12S` "DIRECCIÓN Y SERVICIOS GENERALES" en las 12
                # consejerías). Con la clave antigua `(codigo, denom)` la 1ª aparición
                # (la pequeña) ganaba y las grandes se descartaban → −7,4 B (cobertura
                # 82% vs Hacienda). Incluir la sección conserva las líneas homónimas.
                key = (seccion, codigo, denom[:30])
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                rows.append(make_row(pagina=p_num, codigo=codigo, denominacion=denom,
                                      importe=m.group("importe"), anio=anio))
    except ImportError:
        return ExtractionResult(rows=[], motor="and", notes="pdfplumber no disponible")

    return ExtractionResult(rows=rows, motor="and-resumen-cap-prog")
