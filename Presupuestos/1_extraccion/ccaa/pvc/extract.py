"""
extractors/pvc.py — Euskadi / País Vasco.

Dos formatos oficiales de Open Data Euskadi. Ambos clasifican el gasto por
PROGRAMA de 4 dígitos, cuyos 2 primeros dígitos son la Función de la
clasificación funcional (41*→sanidad, 42*→educacion, …). El concepto se
asigna después por prefijo en correspondencias.yml, así que la MISMA tabla
de correspondencias sirve para los dos formatos.

  · 2015-2021 — GASTOSC.CSV (dentro de AdErAu_c.zip). "Administración General
    + Organismos Autónomos", CONSOLIDADO. Cabecera ÚNICA (castellano), Latin-1,
    separador ';'. Columna "Importe" en EUROS (entero zero-padded, sin
    decimales). Ya viene consolidado (institución 00100 + 002xx) y sólo GASTOS.
    Denominación de programa opcional desde ESTFUNC (fichero hermano o miembro
    del propio zip).

    ⚠️ El input puede llegar como (a) el GASTOSC.csv ya extraído, o (b) el ZIP
    entero — el maestro R descarga la URL .zip y la guarda como "<alias>.csv",
    así que este extractor detecta la firma ZIP (PK\\x03\\x04) y lee GASTOSC.CSV
    de dentro. Si no se maneja esto, R intenta leer el zip con fread, coge el
    primer miembro (ESTECONC.CSV) y peta por encoding — bug del 2026-07-01.

  · 2022-2026 — Datuak_datos.csv (CSV tidy bilingüe). DOS cabeceras (euskera /
    castellano). ⚠️ Contiene GASTOS **e INGRESOS** (col "Tipo Presupuesto":
    1 = gasto, 2 = ingreso) y TODAS las entidades del sector público vasco
    (col "Entidad"). Para una serie de GASTO consolidada y COMPARABLE con el
    ZIP hay que FILTRAR:
        Tipo Presupuesto == "1"                (sólo gasto; descartar ingresos)
        Entidad == "100"  ó  empieza por "2"   (Admin General + OO.AA.)
    Sin ese filtro el total se duplica (gasto+ingreso ≈ 2×) y la cobertura de
    conceptos cae a la mitad. Bug detectado 2026-07-01.

Estrategia común: agrupar por código de Programa (4 díg) y sumar el importe del
ejercicio. Denominación = primera descripción castellana disponible.
"""
from __future__ import annotations

import csv
import zipfile
from pathlib import Path

from .._common import base
from .._common.base import make_row, ExtractionResult, parse_eur


def _decode_lines(path: Path):
    # País Vasco usa ISO-8859-1 (Latin-1) habitualmente
    for enc in ("latin-1", "utf-8-sig", "utf-8"):
        try:
            with path.open("r", encoding=enc) as fh:
                return fh.read().splitlines(), enc
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("pvc", b"", 0, 1, "Encoding desconocido")


def _sniff_delim(sample: str) -> str:
    return ";" if sample.count(";") >= sample.count(",") else ","


def _estfunc_denom(lines, delim: str) -> dict:
    """Programa(4 díg) -> denominación castellana, desde las líneas de un
    ESTFUNC (Año;Grupo;Función;Subfunción;Programa;Desc.cast;Desc.eus).

    FIX 2026-07-27: la cabecera nomina la col. 5 "Descripción castellano" y la
    6 "Descripción euskera", pero el CONTENIDO real del fichero las trae AL
    REVÉS (verificado en 2015/2018/2021: col. 5 = "Zor Publikoa"/"Legebiltzarra"
    en euskera, col. 6 = "Deuda Pública"/"Parlamento" en castellano). Sin este
    fix, todas las denominaciones de programa de pvc (2015-2021 vía ZIP, y
    2022-2026 vía el catálogo cruzado de _load_estfunc_cross_year) salían en
    euskera pese al criterio del proyecto de usar castellano. Ver
    logs/progreso.md 2026-07-27.
    """
    denom: dict[str, str] = {}
    for r in csv.reader(lines[1:], delimiter=delim):
        if len(r) < 7:
            continue
        prog = (r[4] or "").strip()
        if prog.isdigit():
            denom[prog] = " ".join((r[6] or "").split())
    return denom


def _load_estfunc_sibling(gastosc_path: Path, delim: str) -> dict:
    """ESTFUNC.csv hermano del GASTOSC en disco (si existe)."""
    for name in ("ESTFUNC.csv", "ESTFUNC.CSV", "estfunc.csv"):
        p = gastosc_path.with_name(name)
        if p.exists():
            lines, _ = _decode_lines(p)
            return _estfunc_denom(lines, delim)
    return {}


def _load_estfunc_cross_year(input_path: Path) -> dict:
    """Catálogo Programa→denominación construido a partir de los ESTFUNC.csv de
    OTROS ejercicios (2015-2021, rama ZIP).

    FIX 2026-07-27: el CSV tidy (2022-2026) no publica ninguna columna con el
    NOMBRE del programa, solo su código; `_extract_tidy` tomaba antes la
    'Descripción Castellano. Partida' (la partida económica, p.ej.
    "Retribuciones de Altos Cargos") como si fuera el nombre del programa,
    fabricando denominaciones falsas para programas que no tienen nada que ver
    (ese texto salía en el 3121, el 2223, el 3211... — cualquier programa cuya
    primera línea del CSV fuera justo esa partida). El catálogo de programas
    (código de 4 díg = función+subfunción) es estable en el tiempo, así que se
    reutilizan los ESTFUNC.csv YA descargados de 2015-2021 (mismo dataset
    Open Data Euskadi) como fuente de nombres reales para 2022-2026. Se
    fusionan de más antiguo a más reciente para que el nombre más actual gane
    si un código cambia de denominación. Ver logs/progreso.md 2026-07-27.
    """
    raw_root = input_path.parent.parent
    denom: dict[str, str] = {}
    if not raw_root.is_dir():
        return denom
    for anio_dir in sorted(raw_root.glob("2*")):
        for name in ("ESTFUNC.csv", "ESTFUNC.CSV", "estfunc.csv"):
            p = anio_dir / name
            if p.exists():
                try:
                    lines, _ = _decode_lines(p)
                    denom.update(_estfunc_denom(lines, ";"))
                except (OSError, UnicodeDecodeError):
                    continue
                break
    return denom


def _read_zip_gastosc(input_path: Path):
    """Si input_path es un ZIP (firma PK) con GASTOSC.CSV, devuelve
    (lineas_gastosc, denom_estfunc). Si no es zip o no tiene GASTOSC, None."""
    try:
        with open(input_path, "rb") as fh:
            if fh.read(4) != b"PK\x03\x04":
                return None
    except OSError:
        return None
    try:
        with zipfile.ZipFile(input_path) as zf:
            members = {n.upper(): n for n in zf.namelist()}
            gname = members.get("GASTOSC.CSV")
            if not gname:
                return None
            lines = zf.read(gname).decode("latin-1").splitlines()
            denom: dict[str, str] = {}
            ename = members.get("ESTFUNC.CSV")
            if ename:
                denom = _estfunc_denom(zf.read(ename).decode("latin-1").splitlines(), ";")
            return lines, denom
    except (zipfile.BadZipFile, OSError):
        return None


def _rows_from_programs(by_program: dict, anio: int) -> list:
    rows = []
    for codigo, data in sorted(by_program.items()):
        rows.append(make_row(pagina=None, codigo=codigo,
                             denominacion=data["denom"] or f"Programa {codigo}",
                             importe=data["importe_eur"], anio=anio))
    return rows


def _extract_gastosc(lines, denom_map: dict, anio: int, delim: str = ";") -> ExtractionResult:
    """2015-2021 · GASTOSC. Cabecera única; ya consolidado y sólo gasto."""
    hdr = [h.strip() for h in lines[0].split(delim)]

    def col(name):
        for i, h in enumerate(hdr):
            if h == name:
                return i
        return None

    ix_prog = col("Programa")
    ix_imp = col("Importe")
    if ix_prog is None or ix_imp is None:
        return ExtractionResult(rows=[], motor="pvc-gastosc-no-headers",
                                notes=f"cabeceras GASTOSC no reconocidas: {hdr[:16]}")

    by_program: dict[str, dict] = {}
    for r in csv.reader(lines[1:], delimiter=delim):
        if len(r) <= max(ix_prog, ix_imp):
            continue
        codigo = (r[ix_prog] or "").strip()
        if not codigo.isdigit() or len(codigo) < 3:
            continue
        imp = parse_eur(r[ix_imp])
        if not (imp == imp):  # NaN
            continue
        bucket = by_program.setdefault(codigo, {"importe_eur": 0.0, "denom": ""})
        bucket["importe_eur"] += imp
        if not bucket["denom"]:
            bucket["denom"] = denom_map.get(codigo, "")

    return ExtractionResult(rows=_rows_from_programs(by_program, anio),
                            motor="pvc-gastosc-funcional")


def _extract_tidy(lines, delim, anio, denom_map: dict | None = None) -> ExtractionResult:
    """2022-2026 · Datuak_datos.csv. Filtra Tipo=1 (gasto) y Entidad 100/2xx."""
    castellano_hdr = [h.strip() for h in lines[1].split(delim)]
    try:
        ix_prog = castellano_hdr.index("Programa")
        ix_imp = next(i for i, h in enumerate(castellano_hdr)
                      if h.startswith("Importe") or h == str(anio))
    except (ValueError, StopIteration):
        return ExtractionResult(rows=[], motor="pvc-no-headers",
                                notes=f"No se reconocen cabeceras esperadas: {castellano_hdr[:8]}")

    # Columnas de filtro (pueden faltar en formatos antiguos → filtro laxo).
    ix_tipo = castellano_hdr.index("Tipo Presupuesto") if "Tipo Presupuesto" in castellano_hdr else None
    ix_ent = castellano_hdr.index("Entidad") if "Entidad" in castellano_hdr else None

    # FIX 2026-07-27: este CSV NO publica el nombre del programa (solo su
    # código), sólo el de la PARTIDA económica (p.ej. "Retribuciones de Altos
    # Cargos"). Usarlo como denominación del PROGRAMA fabricaba nombres falsos
    # (ver _load_estfunc_cross_year). La denominación real viene de
    # `denom_map` (catálogo ESTFUNC de otros ejercicios); si un código no
    # aparece ahí, se deja vacío y `_rows_from_programs` cae al código desnudo
    # ("Programa <cod>") — NUNCA a la partida.
    denom_map = denom_map or {}

    by_program: dict[str, dict] = {}
    reader = csv.reader(lines[2:], delimiter=delim)
    for r in reader:
        if not r or len(r) <= max(ix_prog, ix_imp):
            continue
        # Filtro gasto-consolidado (ver docstring del módulo).
        if ix_tipo is not None and (r[ix_tipo] or "").strip() != "1":
            continue
        if ix_ent is not None:
            ent = (r[ix_ent] or "").strip()
            if not (ent == "100" or ent.startswith("2")):
                continue
        codigo = (r[ix_prog] or "").strip()
        if not codigo or not codigo.isdigit() or len(codigo) < 3:
            continue
        # El tidy pierde el CERO INICIAL del programa: la deuda `0111` llega como
        # `111` (3 díg) y el prefijo `11*` de direccion la capturaba (~990 M€/año
        # → direccion inflada 2022-26, discontinua con el ZIP que sí trae `0111`
        # y la deja NULL). zfill(4) restaura el cero: 3→4 díg, 4+ intactos. Los
        # programas legítimos de grupo 1 (`1111`,`1112`…) NO se ven afectados.
        codigo = codigo.zfill(4)  # FIX 2026-07-02
        try:
            imp = parse_eur(r[ix_imp])
        except (IndexError, ValueError):
            continue
        if not (imp == imp):  # NaN
            continue
        bucket = by_program.setdefault(codigo, {"importe_eur": 0.0, "denom": ""})
        bucket["importe_eur"] += imp
        if not bucket["denom"]:
            bucket["denom"] = denom_map.get(codigo, "")

    return ExtractionResult(rows=_rows_from_programs(by_program, anio),
                            motor="pvc-csv-tidy")


def extract(input_path: Path, anio: int) -> ExtractionResult:
    if input_path.suffix.lower() == ".html":
        return ExtractionResult(rows=[], motor="pvc-html",
                                 notes="URL canónica devolvió HTML, no CSV. Verificar resolver pvc")

    # (a) ¿Es un ZIP (AdErAu_c) — o bytes zip guardados con extensión .csv?
    z = _read_zip_gastosc(input_path)
    if z is not None:
        lines, denom = z
        return _extract_gastosc(lines, denom, anio, delim=";")

    # (b) Fichero de texto: GASTOSC.csv ya extraído, o Datuak_datos tidy.
    text_lines, _ = _decode_lines(input_path)
    if len(text_lines) < 3:
        return ExtractionResult(rows=[], motor="pvc-empty")

    delim = _sniff_delim("\n".join(text_lines[:5]))
    first_hdr = [h.strip() for h in text_lines[0].split(delim)]
    if "Importe" in first_hdr and "Programa" in first_hdr:
        denom = _load_estfunc_sibling(input_path, delim)
        return _extract_gastosc(text_lines, denom, anio, delim=delim)

    return _extract_tidy(text_lines, delim, anio,
                         denom_map=_load_estfunc_cross_year(input_path))
