#!/usr/bin/env python3
"""
extract_pdf.py — Helper Python para parsear PDFs presupuestarios.

Estrategia:
  1. pdfplumber: regex sobre el texto extraído línea a línea
  2. fallback camelot (si está instalado): tablas estructuradas
  3. fallback texto: cualquier número con denominación adyacente

Cualquier salida respeta el esquema mínimo que espera 2_transformacion:
  codigo (str), denominacion (str), importe_eur (float)
Además persiste columnas auxiliares (pagina, ccaa, anio, fuente_path,
fecha_captura).

Si pyarrow no está disponible, escribe CSV con el mismo nombre. Devuelve
exit code 0 cuando consigue ≥1 fila; 2 cuando no hay ninguna.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Detecta importes con formato es-ES (mínimo 4 dígitos para evitar números de
# referencia o numeración de página): 1.234.567,89 ó 12345 ó 1.234,00
_NUM = r"\d{1,3}(?:\.\d{3}){1,}(?:,\d+)?|\d{4,}(?:,\d+)?|\d{1,3},\d{2}"

# Códigos de PROGRAMA presupuestario (clasificación funcional, sec. 1.6 del
# cuaderno). Características distintivas frente a la clasificación económica:
#   - 3-4 dígitos + letra mayúscula: 412A, 313D, 4131A, 41A1 (Aragón)
#   - 2 dígitos + letra: 31A (Andalucía 41A-41M), 41M (Cataluña)
#   - 3 dígitos + . + dígitos: 313.70 (Valencia), 412.50
#   - 4 dígitos consecutivos: 4131, 4221 (Aragón) — programa-subprograma
# La clasificación económica (subconceptos 120, 220, 226, 411 sin letra)
# se EXCLUYE explícitamente porque genera ruido masivo en las memorias.
_CODIGO = (
    r"(?:"
    r"\d{2,4}[A-Z]\d?"            # 41A, 312D, 412A, 4131A, 41A1, 61N
    r"|\d\.\d\.[A-Z]"             # 2.2.B, 4.2.C, 1.1.J (Andalucía 2026)
    r"|\d{4,5}(?=\s)"             # 4131, 42211 (Aragón) — exige espacio
    r")"
    r"(?![\d\.])"                  # no admite ".XX" detrás → bloquea subconceptos 202.00
)

# Tabular: <codigo> <denominacion+importes intermedios> <ultimo_importe>
RE_PROGRAMA = re.compile(
    rf"^\s*(?P<codigo>{_CODIGO})\s+"
    rf"(?P<denominacion>[A-Za-zÁÉÍÓÚÑáéíóúñÜü].+?)\s+"   # denom empieza con letra
    rf"(?P<importe>{_NUM})\s*€?\s*$"
)

# Línea sin código pero con denominación + importe (último número de la línea).
RE_DENOM_IMPORTE = re.compile(
    rf"^(?P<denominacion>[A-Za-zÁÉÍÓÚÑáéíóúñÜü][^\d].{{8,}}?)\s+(?P<importe>{_NUM})\s*€?\s*$"
)


def parse_eur(s: str) -> float:
    """Convierte string es-ES a float. Devuelve NaN si no parsea."""
    s = (s or "").strip().replace(" ", "")
    if not s:
        return float("nan")
    # Si solo hay punto, asumimos miles ES "1.234.567" sin decimales
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return float("nan")


def _build_row(p_num: int, codigo: str, denom: str, importe: str) -> dict:
    return {
        "pagina": p_num,
        "codigo": (codigo or "").strip(),
        "denominacion": " ".join(denom.split()),
        "importe_eur": parse_eur(importe),
    }


RE_PROGRAMA_HEADER = re.compile(
    r"^\s*(?:PROGRAMA|Programa|PROGRAMMA)\s+"
    r"(?P<codigo>\d{2,5}[A-Z]?)\s+"
    r"(?P<denominacion>.+)$"
)

RE_TOTAL_PROGRAMA = re.compile(
    r"^\s*(?:TOTAL\s+PROGRAMA|Total\s+programa|TOTAL\s+PROGRAMMA)\s+"
    rf"(?P<importe>{_NUM})\s*€?\s*$"
)


def _extract_with_pdfplumber(path: Path) -> list[dict]:
    """Parser por página: detecta PROGRAMA <codigo> <denom> + TOTAL PROGRAMA <importe>.

    Este patrón cubre las memorias de programas habituales (Aragón, Asturias,
    Cantabria, Extremadura, Cataluña, La Rioja, Madrid). Cuando no encuentra
    encabezado de programa, intenta RE_PROGRAMA línea a línea (formato
    tabular de Andalucía).
    """
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        return []

    rows: list[dict] = []
    with pdfplumber.open(str(path)) as pdf:
        for p_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            lines = text.splitlines()

            # Modo 1: cabecera PROGRAMA + TOTAL PROGRAMA en la misma página
            current = None
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                m_hdr = RE_PROGRAMA_HEADER.match(stripped)
                if m_hdr:
                    current = (m_hdr.group("codigo"), m_hdr.group("denominacion").strip())
                    continue
                m_tot = RE_TOTAL_PROGRAMA.match(stripped)
                if m_tot and current is not None:
                    rows.append(_build_row(p_num, current[0], current[1], m_tot.group("importe")))
                    current = None
                    continue

            # Modo 2: tabular (cada línea con código de programa funcional)
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                m = RE_PROGRAMA.match(stripped)
                if m:
                    rows.append(_build_row(p_num, m.group("codigo"),
                                           m.group("denominacion"),
                                           m.group("importe")))
    return rows


def _extract_with_camelot(path: Path) -> list[dict]:
    try:
        import camelot  # type: ignore
    except ImportError:
        return []

    rows: list[dict] = []
    try:
        tables = camelot.read_pdf(str(path), pages="all", flavor="lattice")
    except Exception:
        try:
            tables = camelot.read_pdf(str(path), pages="all", flavor="stream")
        except Exception:
            return []

    for t in tables:
        try:
            df = t.df
        except AttributeError:
            continue
        if df.empty:
            continue

        # Heurística: buscar columnas con muchos códigos y números
        cols = df.columns.tolist()
        # Aplanamos: por cada fila, intentamos detectar (codigo, denominacion, importe)
        for _, fila in df.iterrows():
            cells = [str(c).strip() for c in fila.tolist()]
            cells = [c for c in cells if c]
            if not cells:
                continue

            codigo = ""
            denom_parts: list[str] = []
            importe = ""
            for c in cells:
                if re.fullmatch(_CODIGO, c) and not codigo:
                    codigo = c
                elif re.fullmatch(_NUM, c.replace("€", "").strip()):
                    importe = c
                else:
                    denom_parts.append(c)
            if importe and (codigo or denom_parts):
                rows.append(_build_row(0, codigo, " ".join(denom_parts), importe))
    return rows


def _extract_text_fallback(path: Path) -> list[dict]:
    """Última red: cualquier línea con denominación + importe."""
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        return []
    rows: list[dict] = []
    with pdfplumber.open(str(path)) as pdf:
        for p_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            for line in text.splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                m = RE_DENOM_IMPORTE.match(stripped)
                if m:
                    rows.append(_build_row(p_num, "", m.group("denominacion"),
                                           m.group("importe")))
    return rows


def _write_parquet(rows: list[dict], output: Path, ccaa: str, anio: int,
                   src: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    enriched = [
        {**r, "ccaa_id3": ccaa, "anio": anio,
         "fuente_path": str(src), "fecha_captura": now}
        for r in rows
    ]

    try:
        import pandas as pd  # type: ignore
        df = pd.DataFrame(enriched)
        ext = output.suffix.lower()
        if ext == ".csv":
            df.to_csv(output, index=False)
            return True
        try:
            df.to_parquet(output, index=False)
            return True
        except Exception:
            csv_path = output.with_suffix(".csv")
            df.to_csv(csv_path, index=False)
            return True
    except ImportError:
        csv_path = output.with_suffix(".csv")
        with csv_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh,
                fieldnames=["pagina", "codigo", "denominacion", "importe_eur",
                            "ccaa_id3", "anio", "fuente_path", "fecha_captura"]
            )
            writer.writeheader()
            writer.writerows(enriched)
        return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--ccaa", required=True)
    ap.add_argument("--anio", required=True, type=int)
    args = ap.parse_args()

    src = Path(args.input)
    output = Path(args.output)

    rows = _extract_with_pdfplumber(src)
    motor = "pdfplumber"
    if not rows:
        rows = _extract_with_camelot(src)
        motor = "camelot"
    # Text fallback queda detrás de un opt-in (ENV=PDF_TEXT_FALLBACK=1) porque
    # genera demasiados falsos positivos en PDFs sin estructura de programa.
    import os
    if not rows and os.environ.get("PDF_TEXT_FALLBACK") == "1":
        rows = _extract_text_fallback(src)
        motor = "text-fallback"

    if not rows:
        print(f"WARN sin filas en {src}", file=sys.stderr)
        return 2

    ok = _write_parquet(rows, output, args.ccaa, args.anio, src)
    print(f"OK motor={motor} filas={len(rows)} -> {output} ok={ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
