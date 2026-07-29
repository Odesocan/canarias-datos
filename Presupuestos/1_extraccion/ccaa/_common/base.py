"""
extractors/base.py — Interfaz común para los extractores CCAA-específicos.

Cada extractor implementa `extract(input_path, anio) -> list[dict]` y devuelve
filas con el esquema mínimo del staging del pipeline:

    codigo         (str)  — código presupuestario tal cual aparece en la fuente
    denominacion   (str)  — texto literal de la línea / cabecera del programa
    importe_eur    (float) — importe total del programa, en euros
    pagina         (int|None) — opcional: nº de página para auditoría
    ccaa_id3       (str)  — id3 canónico (and, ara, …) — opcional si ya viene del alias
    anio           (int)  — ejercicio
    capitulo       (int|None) — opcional: capítulo económico si la fuente lo da

El dispatcher añade después `ccaa`, `capa`, `fuente_url`, `fuente_sha256`, etc.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ----------------------------------------------------------------------------
# Utilidades comunes
# ----------------------------------------------------------------------------

# Importes en formato es-ES: 1.234.567,89  /  1234567  /  1234,56
NUM_RE = r"(?:\d{1,3}(?:\.\d{3}){1,}(?:,\d+)?|\d{4,}(?:,\d+)?|\d{1,3},\d{2})"


def parse_eur(s) -> float:
    """Convierte string es-ES (o numérico) a float. NaN si no parsea."""
    if s is None:
        return float("nan")
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).strip().replace(" ", "").replace("€", "")
    if not s or s in {"-", "..", "n.d.", "N/A"}:
        return float("nan")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif re.match(r"^\d{1,3}\.\d{3}$", s):
        s = s.replace(".", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return float("nan")


def make_row(*, pagina: Optional[int], codigo: str, denominacion: str,
             importe: str | float, anio: int, capitulo: Optional[int] = None) -> dict:
    """Construye una fila normalizada del staging."""
    return {
        "pagina": pagina,
        "codigo": (codigo or "").strip(),
        "denominacion": " ".join((denominacion or "").split()),
        "importe_eur": parse_eur(importe) if not isinstance(importe, float) else importe,
        "anio": anio,
        "capitulo": capitulo,
    }


@dataclass
class ExtractionResult:
    """Resultado tipado de una extracción."""
    rows: list[dict]
    motor: str          # "pdf-progr", "pdf-tabla", "html", "csv", "xlsx", …
    notes: str = ""

    @property
    def ok(self) -> bool:
        return len(self.rows) > 0


# ----------------------------------------------------------------------------
# Helpers PDF — solo se importa pdfplumber si está instalado
# ----------------------------------------------------------------------------

def open_pdf(path: Path):
    """Devuelve un context manager pdfplumber.PDF, o lanza ImportError."""
    import pdfplumber  # type: ignore
    return pdfplumber.open(str(path))


def iter_pdf_text(path: Path):
    """Itera (página_num, texto) sobre todas las páginas del PDF.

    Tras emitir cada página se libera su caché interno de objetos
    (`flush_cache`) para que la memoria no crezca de forma lineal con el
    número de páginas: sin esto, los PDF grandes (>800 págs.) agotan la
    RAM del sandbox y el proceso muere con OOM (exit 137). El texto ya
    se ha extraído antes del yield, así que liberar el caché no altera
    en absoluto el resultado.
    """
    # Sidecar opcional: si existe `<pdf>.pagetext.json` (generado por
    # tools/build_pagetext_cache.py para PDFs grandes que no caben en una
    # sola pasada del sandbox), se reutiliza ese texto ya extraído.
    cache_path = Path(str(path) + ".pagetext.json")
    if cache_path.exists():
        import json
        cache = json.loads(cache_path.read_text())
        pages = cache.get("pages", {})
        for i in sorted((int(k) for k in pages), key=int):
            yield i, pages[str(i)]
        return

    with open_pdf(path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            yield i, text
            try:
                page.flush_cache()
                page.get_textmap.cache_clear()
            except Exception:  # noqa: BLE001 — limpieza best-effort
                pass


# ----------------------------------------------------------------------------
# Compiladores de expresiones comunes
# ----------------------------------------------------------------------------

# Patrones de código presupuestario funcional habituales:
#   - 3-4 dígitos + letra: 412A, 313D, 4131A
#   - 2 dígitos + letra (Andalucía página agregada): 61N, 41A, 41M
#   - 4-5 dígitos puros (Aragón): 4131, 42211
#   - Estructura X.Y.Z (Andalucía 2026 fichas): 2.2.B
#   - Estructura X.Y.W (Aragón programas detallados): 11.21.1, 31.1.M, 31.6.B
PROG_CODIGO_RE = (
    r"(?:"
    r"\d{2,4}[A-Z]\d?"            # 41A, 312D, 412A, 4131A, 61N
    r"|\d\.\d{1,2}\.[A-Z\d]"      # 2.2.B, 4.2.C, 11.21.1
    r"|\d{4,5}"                   # 4131, 42211
    r")"
)


# Excluye códigos que en realidad son subconceptos económicos (200.00, 226.01, ...)
ANCHOR_NO_DOT_DIGITS = r"(?![\d\.]\d)"
