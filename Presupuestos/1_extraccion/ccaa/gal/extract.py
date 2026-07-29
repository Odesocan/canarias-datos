"""
extractors/gal.py — Galicia.

Fuente real: CSV abierto de la Xunta vía abertos.xunta.gal (datasets
`0665/gastos-orzamento-<año>` y `0666/gastos-orzamento-<año>-sobre-plan-estratexico`).
El CSV viene en ISO-8859-15 con separador `;` y columnas:

    Consellería;Grupo;Capítulo;Orzamento

Granularidad: Consellería × Grupo de Función × Capítulo Económico.  Sin
detalle por programa (la Xunta no publica el desglose programático en CSV
abierto; sí en los PDFs de la Lei de Orzamentos por consellería).

Estrategia tonight:
  1) Si en `fuentes/raw/gal/<año>/` hay un CSV adjunto
     (`gastos_orzamento*.csv` o `programas*.csv` o `partidas*.csv`), parsea
     como CSV ES-ES.
  2) Agrega por (Consellería, Grupo) sumando capítulos → 1 fila por
     consellería-grupo, con la consellería usada como denominación y el
     grupo numérico como prefijo del código.
  3) Si no hay CSV, queda en stub (próximas noches resolverán PDFs por
     consellería para granularidad de programa).

Códigos sintéticos `<grupo>.<consellería_id>` (e.g. `4.13` = grupo 4
Producción bens públicos sociales × consellería 13 Sanidade).  Como los
códigos no son estándar, la correspondencia se hace ENTERA por KEYWORD
sobre la denominación.
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

from .._common import base
from .._common.base import ExtractionResult, make_row, parse_eur


def _normalize(s: str) -> str:
    return " ".join((s or "").split())


def _detect_encoding(src: Path) -> str:
    try:
        with src.open("r", encoding="utf-8") as fh:
            fh.read(2048)
        return "utf-8"
    except UnicodeDecodeError:
        return "latin-1"


def _csv_iter(src: Path):
    enc = _detect_encoding(src)
    with src.open("r", encoding=enc, errors="replace") as fh:
        sniff = fh.read(2048)
        fh.seek(0)
        delim = ";" if sniff.count(";") > sniff.count(",") else ","
        for r in csv.DictReader(fh, delimiter=delim):
            yield r


def _es_csv_funcional(src: Path) -> bool:
    """True si el CSV trae la clasificación FUNCIONAL (Consellería;Grupo;Capítulo).

    La Xunta publica DOS datasets homónimos por ejercicio:
      - `gastos-orzamento-<año>`                    → funcional (Grupo × Capítulo)  ✅
      - `gastos-orzamento-<año>-sobre-plan-estratexico` → estratéxico (Eixo × Prioridade) ❌
    El segundo NO tiene grupo de función: si se procesa como funcional, `Grupo`
    sale vacío, todo colapsa a `grupo=0` (1 fila/consellería) y el año degrada a
    ~16-18 filas / <30 umbral (AMARILLO) sin ninguna señal de error. Este guard
    detecta el esquema y rechaza el estratéxico para no degradar en silencio.
    (Ver logs/progreso.md 2026-07-02; datasets funcionales: 2023=0564, 2026=0692.)
    """
    enc = _detect_encoding(src)
    with src.open("r", encoding=enc, errors="replace") as fh:
        header = fh.readline()
    cols = header.upper()
    return "GRUPO" in cols and "EIXO" not in cols


def _from_csv(input_path: Path, anio: int) -> list[dict]:
    candidatos = (
        list(input_path.parent.glob("gastos_orzamento*utf8*.csv"))
        + list(input_path.parent.glob("gastos_orzamento*.csv"))
        + list(input_path.parent.glob("programas*.csv"))
        + list(input_path.parent.glob("partidas*.csv"))
    )
    if not candidatos:
        return []
    # Guard de esquema: usar SOLO el CSV funcional (Grupo/Capítulo). Si el único
    # adjunto es el estratéxico (Eixo/Prioridade), NO procesarlo como funcional
    # (colapsaría a 1 fila/consellería). Se prefiere fallar a pendiente y avisar.
    funcionales = [c for c in candidatos if _es_csv_funcional(c)]
    if not funcionales:
        return []
    src = funcionales[0]
    agg: dict[tuple[str, str], float] = defaultdict(float)
    grupo_label_map: dict[str, str] = {}
    for r in _csv_iter(src):
        cons = _normalize(
            r.get("Consellería") or r.get("Conselleria")
            or r.get("consellería") or r.get("CONSELLERIA")
            or r.get("denominacion") or ""
        )
        grupo = _normalize(r.get("Grupo") or r.get("grupo") or "")
        importe_raw = (
            r.get("Orzamento") or r.get("orzamento")
            or r.get("importe_eur") or r.get("Importe") or "0"
        )
        importe = parse_eur(importe_raw)
        if importe != importe or importe <= 0 or not cons:
            continue
        m = re.match(r"^\s*(\d+)\s+(.+)$", grupo)
        if m:
            grupo_n = m.group(1)
            grupo_label = m.group(2).strip()
        else:
            grupo_n = "0"
            grupo_label = grupo
        key = (cons, grupo_n)
        agg[key] += importe
        if grupo_n not in grupo_label_map:
            grupo_label_map[grupo_n] = grupo_label

    # ID determinista por consellería (hashlib en vez de hash() builtin)
    import hashlib
    def _cons_id(c: str) -> str:
        h = hashlib.md5(c.encode("utf-8")).hexdigest()
        return f"{int(h[:4], 16) % 100:02d}"

    rows: list[dict] = []
    for (cons, grupo_n), importe in sorted(agg.items()):
        codigo = f"{grupo_n}.{_cons_id(cons)}"
        denom = f"{cons} — Grupo {grupo_n} {grupo_label_map.get(grupo_n, '')}".strip()
        rows.append(make_row(pagina=None, codigo=codigo,
                             denominacion=denom, importe=float(importe),
                             anio=anio))
    return rows


# --------------------------------------------------------------------------- #
# Rama PDF: PROGR_I/II "Orzamentos por programas" (consellerías + organismos).
#
# Cada programa cierra cada bloque (programa × servizo) con una línea
# `T O T A L  P R O G R A M A <cód> <importe>` (euros, sep. miles '.').  El
# documento NO está consolidado: los organismos autónomos (SERGAS, axencias…)
# ejecutan programas financiados por transferencias de las consellerías, así que
# sumar TODO duplica (gross 2023 = 20.2B vs consolidado 12.85B; sanidad +94%).
#
# Regla "C" (consolidación validada contra el CSV de datos abertos 2022-2024):
# sumar el total de programa SOLO de los bloques ejecutados por una CONSELLERÍA
# (excluir los bloques cuyo SERVIZO es un organismo autónomo).  La transferencia
# que financia al organismo queda como proxy de su gasto y se evita el doble
# conteo.  Sesgo residual estable ~ -5% en sanidad, +8% en total (ver progreso.md
# 2026-06-30).  Sólo necesaria para 2015-2021 (2022+ usan el CSV consolidado).
# Cabecera de programa. El código puede venir COMPACTO (2018+: "412A") o
# LETTER-SPACED (2015-2017: "4 1 2 A"); \s* entre dígitos cubre ambos casos.
_PROGHEAD = re.compile(r"PROGRAMA\s*-\s*(\d)\s*(\d)\s*(\d)\s*([A-Z])\s+(.+?)\s*$")
_SERV = re.compile(r"SERVIZO\s*-\s*(\S+)\s+(.+)")
_TOTPROG = re.compile(
    r"T\s*O\s*T\s*A\s*L\s*P\s*R\s*O\s*G\s*R\s*A\s*M\s*A\s+([0-9]{3}[A-Z])\s+([\d.]+)"
)
# Un SERVIZO es organismo autónomo (no consellería) si su nombre contiene:
_ORG_KW = (
    "SERVIZO GALEGO", "AXENCIA", "CONSORCIO", "INSTITUTO GALEGO", "FUNDACION",
    "FONDO GALEGO", "AUGAS DE GALICIA", "ACADEMIA", "SOCIEDADE", "ESCOLA GALEGA",
    "ENTE PUBLICO",
)


def _is_organismo(servizo_nombre: str) -> bool:
    n = (servizo_nombre or "").upper()
    return any(k in n for k in _ORG_KW)


def _from_progr_pdf(input_path: Path, anio: int) -> list[dict]:
    pdfs = sorted(input_path.parent.glob("PROGR_*.pdf")) \
        + sorted(input_path.parent.glob("PROGR_*.PDF"))
    if not pdfs:
        return []

    # Ruta de lectura vía `base.iter_pdf_text`: si existe el sidecar
    # `<pdf>.pagetext.json` (generado por outputs/gal_pdftotext_sidecar.py con
    # `pdftotext -layout`, ~0.5 s/PDF) lo reutiliza; si no, cae a pdfplumber
    # (>42 s/PDF → excede el timeout de 45 s del sandbox nocturno). A/B validado
    # (gal 2015 PROGR_I, pág. 1-60): la lista de TOTAL-PROGRAMA es IDÉNTICA con
    # sidecar pdftotext y con pdfplumber, incluido el formato letter-spaced de
    # 2015-2017. La detección de organismo (SERVIZO) y los códigos no cambian.
    importes: dict[str, float] = defaultdict(float)
    nombres: dict[str, str] = {}
    for pdf_path in pdfs:
        servizo_nombre = ""
        for _pageno, text in base.iter_pdf_text(pdf_path):
            for line in text.split("\n"):
                sm = _SERV.search(line)
                if sm:
                    servizo_nombre = sm.group(1, 2)[1].strip()
                hm = _PROGHEAD.search(line.strip())
                if hm:
                    # código (compacto o letter-spaced) + nombre de programa
                    codigo_h = "".join(hm.group(1, 2, 3, 4))
                    nombres.setdefault(codigo_h, hm.group(5).strip())
                tm = _TOTPROG.search(line)
                if tm and not _is_organismo(servizo_nombre):
                    codigo = tm.group(1)
                    importes[codigo] += float(tm.group(2).replace(".", ""))

    rows: list[dict] = []
    for codigo, importe in sorted(importes.items()):
        if importe <= 0:
            continue
        rows.append(make_row(pagina=None, codigo=codigo,
                             denominacion=nombres.get(codigo, codigo),
                             importe=float(importe), anio=anio))
    return rows


def extract(input_path: Path, anio: int) -> ExtractionResult:
    rows = _from_csv(input_path, anio)
    if rows:
        return ExtractionResult(rows=rows, motor="gal-csv-abertos-xunta")

    rows = _from_progr_pdf(input_path, anio)
    if rows:
        return ExtractionResult(
            rows=rows, motor="gal-progr-consellerias-ruleC",
            notes=("PROGR_I/II consolidado regla C (sólo bloques consellería). "
                   "Sesgo ~-5% sanidad vs CSV datos abertos. Usar CSV si disponible "
                   "(2022+)."),
        )

    return ExtractionResult(
        rows=[], motor="gal-pendiente",
        notes=("Sin CSV FUNCIONAL (Consellería;Grupo;Capítulo) ni PROGR_*.pdf "
               "adjuntos. OJO: el dataset 'gastos-orzamento-<año>-sobre-plan-"
               "estratexico' (Eixo;Prioridade) NO sirve y se rechaza por guard "
               "de esquema. Descarga el FUNCIONAL: abertos.xunta.gal/.../<ID>/"
               "gastos-orzamento-<año>/001/descarga-directa-ficheiro.csv (IDs por "
               "año, ver fuentes.yml; funcional 2023=0564, 2026=0692). PDF: "
               "orzamentos.xunta.gal/orzamentos/<año>/DE/PROGR_I.PDF + PROGR_II.PDF."),
    )
