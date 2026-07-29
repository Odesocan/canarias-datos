#!/usr/bin/env python3
"""gal_pdftotext_sidecar.py — genera sidecars .pagetext.json para los PDFs
PROGR_*.pdf de Galicia 2015-2021 usando `pdftotext -layout` (poppler, C).

Motivo: el extractor gal (rama PDF `_from_progr_pdf`) reparsea con pdfplumber
cada PROGR_I/II (>42 s/año en el sandbox → timeout 45 s). `pdftotext -layout`
extrae el PDF entero en ~0.5 s conservando las líneas letter-spaced
(`T O T A L   P R O G R A M A   111A   3.376.671`) que necesitan los regex.

El sidecar tiene el formato que `base.iter_pdf_text` ya sabe leer:
    {"pages": {"1": "<texto pág 1>", "2": ...}, "engine": "pdftotext-layout"}
Se usa el form-feed (\f) que pdftotext inserta entre páginas para el split.

Uso:
    python3 outputs/gal_pdftotext_sidecar.py 2015 2016 ... 2021
    python3 outputs/gal_pdftotext_sidecar.py            # todos 2015-2021
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "fuentes" / "raw" / "gal"


def build_sidecar(pdf_path: Path) -> int:
    """Escribe <pdf>.pagetext.json. Devuelve nº de páginas."""
    out = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True, text=True, check=True,
    )
    # pdftotext separa páginas con form-feed \f
    pages_raw = out.stdout.split("\f")
    # La última división suele ser cadena vacía tras el \f final
    pages = {}
    for i, txt in enumerate(pages_raw, start=1):
        if txt.strip() == "" and i == len(pages_raw):
            continue
        pages[str(i)] = txt
    sidecar = pdf_path.with_name(pdf_path.name + ".pagetext.json")
    sidecar.write_text(json.dumps(
        {"pages": pages, "engine": "pdftotext-layout"}, ensure_ascii=False))
    return len(pages)


def main(argv: list[str]) -> int:
    anios = argv or [str(y) for y in range(2015, 2022)]
    for anio in anios:
        d = RAW / anio
        if not d.is_dir():
            print(f"[skip] {anio}: sin carpeta")
            continue
        pdfs = sorted(d.glob("PROGR_*.pdf")) + sorted(d.glob("PROGR_*.PDF"))
        if not pdfs:
            print(f"[skip] {anio}: sin PROGR_*.pdf")
            continue
        for pdf in pdfs:
            n = build_sidecar(pdf)
            print(f"[ok]   {anio}/{pdf.name}: {n} páginas → {pdf.name}.pagetext.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
