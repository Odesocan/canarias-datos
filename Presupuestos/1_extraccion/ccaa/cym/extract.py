"""
extractors/cym.py — Castilla y León.

datosabiertos.jcyl.es publica el presupuesto de gastos por ejercicio en el
recurso CKAN `1284548037482-<N>.csv`, que en realidad es un ZIP. El N NO es el
año: hay que datar cada recurso por la etiqueta de columna (formatos ricos) o
por la fecha interna del ZIP. Mapa real verificado (2026-06-29):

    -1 → 2016   -2 → 2017   -3 → 2018   -4 → 2021
    -5 → 2023   -6 → 2024   -7 → 2025   -8 → 2026

(2019, 2020 y 2022 NO tienen recurso propio en el portal — no se fabrican.)

El ZIP trae el fichero de gastos en TRES formatos según la época, que este
extractor normaliza todos a (Subprograma → importe del ejercicio):

  A) Excel consolidado / "Datos abiertos" (.xls/.xlsx, 2023-2026): hoja con
     columnas `Subprograma`, `Desc. Subprograma` y una columna de importe
     ETIQUETADA con el año (`2024`, `2026`…). Las filas-totales sin Subprograma
     se descartan al agrupar (dropna).
  B) "WEB Datos csv gastos.csv" (2021): mismo esquema en CSV `;` latin-1, la
     columna de importe se llama como el año (`2021`).
  C) "Dotaciones Presupuesto de Gastos.csv" (2016-2018): CSV `;` latin-1 con
     cabeceras en mayúsculas (`SUBPROGRAMA`, `PRESUPUESTO`), sin descripción de
     subprograma (denominación vacía; el concepto se asigna por código).

  D) BOCYL Ley (PDF, 2015): `datosabiertos.jcyl` NO publica distribución 2015
     (los recursos -1..-8 = 2016..2026). La única fuente con detalle por programa
     es el PDF del BOCYL (Ley 11/2014, 576 pp). El estado de gastos figura SOLO
     como "9.- Detalle económico territorial por secciones y subprogramas"
     (SECCIÓN → SERVICIO → PROGRAMA → SUBPROGRAMA → económico capítulo/artículo/
     concepto/subconcepto × 9 provincias + SIN TERRITORIALIZAR + TOTAL), repetido
     por cada entidad del grupo (Administración General + cada OOAA). Se agrega
     por SUBPROGRAMA sumando las líneas de CAPÍTULO (código económico de 1 díg.,
     columna TOTAL) y RESTANDO las transferencias internas a OOAA (concepto 400/
     401/700/701) — mismo criterio de consolidación que la rama CSV 2016-18. El
     neto reconcilia al euro con el "Estado de gastos consolidado" oficial
     (9.920.811.756 €; sanidad 3,27B, educación 1,84B). Motor `cym-bocyl-territorial`.

Convención de entrada: el dispatcher pasa la ruta del fichero de gastos ya
staged en `fuentes/raw/cym/<año>/gastos.{xls,xlsx,csv}` (o el PDF del BOCYL 2015).

Notas:
- Los .xls (97-2003) requieren `xlrd>=2.0`; los .xlsx usan `openpyxl`.
- Importes en euros. CSV en formato es-ES (punto miles, coma decimal).
- Códigos de subprograma de 6 caracteres uniformes en los 3 formatos
  (p.ej. `312A01`, `322A01`) → `correspondencias.yml` aplica a todos los años.
"""
from __future__ import annotations

import csv as _csv
import re as _re
import shutil
import tempfile
import zipfile
from pathlib import Path

from .._common.base import make_row, ExtractionResult


def _to_eur(v) -> float:
    """Importe → float (euros). Acepta numérico o string es-ES."""
    if isinstance(v, (int, float)):
        return float(v) if v == v else 0.0  # descarta NaN
    s = str(v).strip().replace("\xa0", "").replace(" ", "")
    if not s or s.lower() == "nan":
        return 0.0
    if "," in s:                      # es-ES: '.' miles, ',' decimal
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1:            # '1.234.567' → miles sin decimal
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def _norm(c) -> str:
    return str(c).strip().lower()


def _is_pdf(path: Path) -> bool:
    """PDF por extensión o por firma `%PDF` (el dispatcher puede stagear sin
    extensión reconocible)."""
    if path.suffix.lower() == ".pdf":
        return True
    try:
        with path.open("rb") as fh:
            return fh.read(4) == b"%PDF"
    except OSError:
        return False


# Conceptos económicos de TRANSFERENCIA INTERNA a organismos autónomos de la CA
# (Gerencia Regional de Salud, Gerencia de Servicios Sociales, ECYL…). En el
# formato "Dotaciones" (2016-2018) la Consejería figura con estos conceptos
# transfiriendo a su OOAA, y el OOAA figura APARTE con su gasto propio en el
# mismo fichero → sumar ambos DUPLICA (~+30%: total 2017 14,30B vs 10,29B real;
# sanidad ~2×). Se descartan las líneas de transferencia (contamos el gasto
# ejecutado del OOAA, no la transferencia que lo financia; mismo criterio que
# cat-SALUT / ara-4131 / gal-reglaC). Fix 2026-07-02. Verificado: 2017 filtrado
# = 10,29B, continuo con el CSV consolidado 2021 (12,29B, que ya viene sin estas
# líneas → el filtro es no-op ahí). Corrientes 400/401, capital 700/701.
_TRANSFER_INTERNA_OOAA = {"400", "401", "700", "701"}


# ---------------------------------------------------------------------------
# Rama PDF BOCYL 2015 (motor cym-bocyl-territorial)
# ---------------------------------------------------------------------------
_SUB_RE = _re.compile(r"^SUBPROGRAMA\s+([0-9A-Z]{4,7})\s+(.+)$")
_NUMTOK_RE = _re.compile(r"^\d[\d.]*$")
# Marca de las páginas del estado de gastos (bloques 2 y 3); las de ingresos
# usan "Estado de Ingresos" y NO se seleccionan.
_GASTOS_MARK = "9.- Detalle económico territorial"


def _pdf_eur(s: str) -> float:
    """Importe entero en euros del PDF BOCYL. El '.' es SEPARADOR DE MILES
    (no decimal): '973.791' → 973791, '3.158.070.822' → 3158070822. La tabla
    territorial no lleva decimales. (No reutilizar `_to_eur`, que trata el punto
    simple como decimal.)"""
    return float(s.replace(".", ""))


def _records_from_pdf_bocyl(path: Path, anio: int):
    """Agrega el gasto por SUBPROGRAMA desde el detalle económico territorial.

    Para cada subprograma: neto = Σ líneas de CAPÍTULO (código económico de 1
    dígito, columna TOTAL = último token numérico) − Σ transferencias internas a
    OOAA (concepto de 3 dígitos en {400,401,700,701}). Sumar todas las entidades
    del grupo y restar esas transferencias reproduce el consolidado oficial (el
    mismo doble conteo Consejería→OOAA que filtra la rama CSV 2016-18).
    """
    from .._common import base  # iter_pdf_text usa el sidecar .pagetext.json si existe

    gross: dict[str, float] = {}
    transfer: dict[str, float] = {}
    name: dict[str, str] = {}
    page_of: dict[str, int] = {}
    cur = None
    # iter_pdf_text lee el sidecar `<pdf>.pagetext.json` (pdftotext -layout) cuando
    # existe — el BOCYL de 576 pp cuelga pdfplumber en el sandbox (>40s). La columna
    # TOTAL (último token numérico) se conserva idéntica en el layout de pdftotext,
    # así que la agregación por capítulo/transferencia reproduce el mismo neto.
    for pageno, t in base.iter_pdf_text(path):
            t = t or ""
            if _GASTOS_MARK not in t:
                continue
            for raw in t.split("\n"):
                line = raw.strip()
                m = _SUB_RE.match(line)
                if m:
                    cur = m.group(1)
                    name.setdefault(cur, m.group(2).strip())
                    page_of.setdefault(cur, pageno)
                    continue
                if (line.startswith("PROGRAMA") or line.startswith("SECCIÓN")
                        or line.startswith("SERVICIO")):
                    continue
                toks = line.split()
                if len(toks) < 3 or cur is None:
                    continue
                code = toks[0]
                if not code.isdigit() or not _NUMTOK_RE.match(toks[-1]):
                    continue
                total = _pdf_eur(toks[-1])
                if len(code) == 1:                       # capítulo económico
                    gross[cur] = gross.get(cur, 0.0) + total
                elif len(code) == 3 and code in _TRANSFER_INTERNA_OOAA:
                    transfer[cur] = transfer.get(cur, 0.0) + total

    recs = []
    for cod, g in gross.items():
        net = g - transfer.get(cod, 0.0)
        if net <= 0:
            continue
        recs.append((cod, name.get(cod, ""), net, page_of.get(cod)))
    return recs


def _find_concepto_economico(header) -> int | None:
    """Índice de la columna 'Concepto' ECONÓMICO (no 'Desc. Concepto' ni
    'Subconcepto'). Solo el formato detallado (Dotaciones 2016-18, CSV 2021) la
    trae; el consolidado por subprograma no → devuelve None y no se filtra."""
    for i, c in enumerate(header):
        if _norm(c) == "concepto":
            return i
    return None


def _pick_amount_col(cols, anio: int):
    """Columna de importe: año etiquetado → 'presupuesto' → última."""
    for c in cols:
        n = _norm(c)
        if n == str(anio) or n == f"{anio}.0" or n.startswith(str(anio)):
            return c
    for c in cols:
        if _norm(c) == "presupuesto":
            return c
    return cols[-1]


def _pick(cols, *needles):
    """Primera columna cuyo nombre normalizado contiene TODOS los needles."""
    for c in cols:
        n = _norm(c)
        if all(k in n for k in needles):
            return c
    return None


def _records_from_excel(path: Path, anio: int):
    import pandas as pd  # type: ignore
    xl = pd.ExcelFile(path)
    # hoja de datos = la primera que tenga una columna 'subprograma'
    sheet = None
    for sh in xl.sheet_names:
        head = xl.parse(sh, nrows=0)
        if _pick(list(head.columns), "subprograma"):
            sheet = sh
            break
    if sheet is None:
        sheet = xl.sheet_names[-1]
    df = xl.parse(sheet)
    cols = list(df.columns)
    sub = _pick(cols, "subprograma")
    den = _pick(cols, "desc", "subprograma")
    amt = _pick_amount_col(cols, anio)
    out = []
    for _, r in df.iterrows():
        codigo = str(r[sub]).strip()
        if not codigo or codigo.lower() == "nan":
            continue
        denom = str(r[den]).strip() if den is not None else ""
        out.append((codigo, denom, _to_eur(r[amt])))
    return out, f"excel:{sheet}"


def _records_from_csv(path: Path, anio: int):
    with path.open("r", encoding="latin-1", newline="") as fh:
        reader = _csv.reader(fh, delimiter=";")
        header = next(reader)
        sub = _pick(header, "subprograma")
        den = _pick(header, "desc", "subprograma")
        amt = _pick_amount_col(header, anio)
        i_sub = header.index(sub)
        i_amt = header.index(amt)
        i_den = header.index(den) if den is not None else None
        i_con = _find_concepto_economico(header)  # transferencias internas a OOAA
        out = []
        for row in reader:
            if len(row) <= max(i_sub, i_amt):
                continue
            codigo = row[i_sub].strip()
            if not codigo:
                continue
            if (i_con is not None and i_con < len(row)
                    and row[i_con].strip() in _TRANSFER_INTERNA_OOAA):
                continue  # transferencia interna a OOAA: doble conteo (ver arriba)
            denom = row[i_den].strip() if i_den is not None and i_den < len(row) else ""
            out.append((codigo, denom, _to_eur(row[i_amt])))
    return out, "csv"


def _resolve_source(path: Path) -> tuple[Path, str, str | None]:
    """Resuelve la fuente REAL a parsear y su extensión.

    La URL de datos abiertos JCyL (`1284548037482-N.csv`) es en realidad un ZIP;
    el pipeline R lo guarda con extensión `.bin` (o el dispatcher puede pasar el
    ZIP directamente). Si el fichero es un ZIP (firma `PK`), se extrae de dentro
    el fichero de GASTOS (.xlsx/.xls/.csv; se prefiere el que contenga "gasto"/
    "consolidad" y se descarta "ingreso") a un temporal. Devuelve
    (ruta_a_parsear, extensión, tmpdir_a_limpiar_o_None). Fix 2026-07-02: antes,
    con el `.bin` el extractor caía a la rama CSV y fallaba → cym 2025/2026 no
    cargaban pese a existir el `.xls` correcto.
    """
    try:
        with path.open("rb") as fh:
            magic = fh.read(2)
    except OSError:
        return path, path.suffix.lower(), None
    if magic != b"PK":
        return path, path.suffix.lower(), None
    with zipfile.ZipFile(path) as zf:
        cand = [n for n in zf.namelist()
                if not n.endswith("/")
                and Path(n).suffix.lower() in (".xls", ".xlsx", ".csv")]
        if not cand:
            return path, path.suffix.lower(), None

        def _score(n: str) -> tuple:
            nl = n.lower()
            ext_rank = {".xlsx": 3, ".xls": 2, ".csv": 1}.get(Path(nl).suffix.lower(), 0)
            gasto = ("gasto" in nl or "consolidad" in nl) and "ingreso" not in nl
            return (0 if "ingreso" in nl else 1, gasto, ext_rank)

        best = max(cand, key=_score)
        tmpdir = tempfile.mkdtemp(prefix="cym_zip_")
        out = Path(zf.extract(best, tmpdir))
    return out, out.suffix.lower(), tmpdir


def extract(input_path: Path, anio: int) -> ExtractionResult:
    path = Path(input_path)
    if not path.exists():
        return ExtractionResult(rows=[], motor="cym-jcyl-datosabiertos",
                                notes=f"no existe {path}")

    # Rama PDF BOCYL (2015): detalle económico territorial → subprograma.
    if _is_pdf(path):
        try:
            recs = _records_from_pdf_bocyl(path, anio)
        except ImportError as e:
            return ExtractionResult(rows=[], motor="cym-bocyl-territorial",
                                    notes=f"dependencia ausente: {e}")
        except Exception as e:  # noqa: BLE001
            return ExtractionResult(rows=[], motor="cym-bocyl-territorial",
                                    notes=f"error leyendo {path.name}: {e}")
        rows = [make_row(pagina=pg, codigo=c, denominacion=d, importe=v, anio=anio)
                for c, d, v, pg in recs]
        return ExtractionResult(
            rows=rows, motor="cym-bocyl-territorial",
            notes=(f"{len(rows)} subprogramas (BOCYL territorial, neto de "
                   f"transferencias internas OOAA) desde {path.name}"))

    src, ext, tmpdir = _resolve_source(path)
    try:
        if ext in (".xls", ".xlsx"):
            recs, fmt = _records_from_excel(src, anio)
        else:
            recs, fmt = _records_from_csv(src, anio)
    except ImportError as e:
        return ExtractionResult(rows=[], motor="cym-jcyl-datosabiertos",
                                notes=f"dependencia ausente: {e}")
    except Exception as e:
        return ExtractionResult(rows=[], motor="cym-jcyl-datosabiertos",
                                notes=f"error leyendo {path.name}: {e}")
    finally:
        if tmpdir:
            shutil.rmtree(tmpdir, ignore_errors=True)

    # agrega por subprograma (suma capítulos/económicas), denom = primera no vacía
    agg: dict[str, list] = {}
    for codigo, denom, imp in recs:
        if imp <= 0:
            continue
        if codigo not in agg:
            agg[codigo] = [denom, 0.0]
        if not agg[codigo][0] and denom:
            agg[codigo][0] = denom
        agg[codigo][1] += imp

    rows = [make_row(pagina=None, codigo=c, denominacion=d, importe=v, anio=anio)
            for c, (d, v) in agg.items()]
    return ExtractionResult(
        rows=rows, motor="cym-jcyl-datosabiertos",
        notes=f"{len(rows)} subprogramas ({fmt}) desde {path.name}",
    )
