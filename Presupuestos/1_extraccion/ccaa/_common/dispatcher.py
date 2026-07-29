"""
ccaa/_common/dispatcher.py — Selecciona el sub-pipeline de la CCAA.

Para cada CCAA hay una carpeta autocontenida `ccaa/<id3>/` con su propio
`extract.py` (y opcionalmente `transform.py`, `correspondencias.yml`).

Uso CLI (mismo contrato que antes):
    python3 -m ccaa --ccaa ara --anio 2024 --input file.pdf --output out.csv
"""
from __future__ import annotations

import argparse
import csv
import importlib
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import base


def get_extractor(ccaa: str):
    """Carga `ccaa.<id3>.extract`. Si no existe, devuelve el genérico."""
    ccaa = (ccaa or "").lower().strip()
    try:
        return importlib.import_module(f"ccaa.{ccaa}.extract")
    except ImportError:
        try:
            return importlib.import_module("ccaa._common.generic")
        except ImportError:
            raise ImportError(f"No hay extractor para CCAA '{ccaa}' "
                              f"y no se encontró ccaa._common.generic")


def dispatch(ccaa: str, input_path: Path, anio: int) -> base.ExtractionResult:
    extractor = get_extractor(ccaa)
    result = extractor.extract(input_path, anio)
    if not isinstance(result, base.ExtractionResult):
        result = base.ExtractionResult(rows=list(result), motor=ccaa)
    for r in result.rows:
        r.setdefault("ccaa_id3", ccaa)
    return result


def get_transformer(ccaa: str):
    """Carga `ccaa.<id3>.transform`. Devuelve None si no hay."""
    try:
        return importlib.import_module(f"ccaa.{ccaa}.transform")
    except ImportError:
        return None


def _write_output(rows: list[dict], output: Path, ccaa: str, anio: int, src: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    enriched = [{**r, "ccaa_id3": r.get("ccaa_id3", ccaa),
                  "anio": r.get("anio", anio),
                  "fuente_path": str(src),
                  "fecha_captura": now}
                 for r in rows]

    try:
        import pandas as pd  # type: ignore
        df = pd.DataFrame(enriched)
        ext = output.suffix.lower()
        if ext == ".csv":
            df.to_csv(output, index=False); return True
        try:
            df.to_parquet(output, index=False); return True
        except Exception:
            df.to_csv(output.with_suffix(".csv"), index=False); return True
    except ImportError:
        out_path = output if output.suffix == ".csv" else output.with_suffix(".csv")
        with out_path.open("w", newline="", encoding="utf-8") as fh:
            fieldnames = ["pagina","codigo","denominacion","importe_eur","ccaa_id3",
                          "anio","capitulo","concepto","fuente_path","fecha_captura"]
            writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader(); writer.writerows(enriched)
        return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Sub-pipeline CCAA")
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--ccaa", required=True)
    ap.add_argument("--anio", required=True, type=int)
    ap.add_argument("--skip-transform", action="store_true",
                     help="No aplicar el transform.py local de la CCAA")
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"ERROR: no existe {src}", file=sys.stderr); return 2

    result = dispatch(args.ccaa, src, args.anio)
    rows = result.rows
    motor = result.motor

    # Aplica transform.py local si existe
    if rows and not args.skip_transform:
        tr = get_transformer(args.ccaa)
        if tr is not None and hasattr(tr, "transform"):
            try:
                rows = tr.transform(rows, args.anio)
                motor = f"{motor}+{args.ccaa}-transform"
            except Exception as e:
                print(f"WARN: transform falló para {args.ccaa}: {e}", file=sys.stderr)

    if not rows:
        print(f"WARN sin filas en {src} (motor={motor})", file=sys.stderr); return 2

    ok = _write_output(rows, Path(args.output), args.ccaa, args.anio, src)
    print(f"OK motor={motor} filas={len(rows)} -> {args.output} ok={ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
