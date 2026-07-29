#!/usr/bin/env python3
"""Genera el sidecar pagetext de un PDF usando pdftotext -layout (poppler, C,
~100x mas rapido que pdfplumber). Formato identico al que lee _common/base.py:
    {"complete": true, "total": N, "pages": {"1": "...", ...}}
pdftotext separa paginas con form-feed (\\f). Uso:
    python3 ext_pdftotext_sidecar.py <pdf> [--out <sidecar>]
Si no se pasa --out, escribe <pdf>.pagetext.json (in place)."""
import json
import subprocess
import sys
from pathlib import Path


def build(pdf_path: Path, out_path: Path) -> None:
    txt = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"],
                         capture_output=True, text=True, check=True).stdout
    parts = txt.split("\f")
    # pdftotext suele dejar un \f final -> elemento vacio; lo quitamos si es asi
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    pages = {str(i): t for i, t in enumerate(parts, start=1)}
    cache = {"complete": True, "total": len(pages), "pages": pages}
    out_path.write_text(json.dumps(cache))
    print(f"OK {out_path.name}: {len(pages)} paginas")


def main() -> int:
    args = sys.argv[1:]
    pdf = Path(args[0])
    out = None
    if "--out" in args:
        out = Path(args[args.index("--out") + 1])
    if out is None:
        out = pdf.with_suffix(pdf.suffix + ".pagetext.json")
    build(pdf, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
