#!/usr/bin/env python3
"""tests/test_hacienda.py — Test del parser Hacienda con un XLSX sintético."""
from __future__ import annotations
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "1_extraccion"))

from openpyxl import Workbook  # type: ignore
import extract_hacienda as eh


def build_fixture_xlsx(path: Path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Capítulos"
    # Layout pivot: filas=CCAA, cols=capítulos
    headers = ["CCAA", "1. Personal", "2. Bienes y servicios", "3. Financieros",
               "4. Transferencias corrientes", "6. Inversiones reales",
               "7. Transferencias de capital", "8. Activos financieros",
               "9. Pasivos financieros"]
    ws.append(headers)
    rows = [
        ("Andalucía",        14500000000, 4200000000, 600000000, 18000000000, 2500000000, 1200000000, 200000000, 1100000000),
        ("Canarias",         3100000000, 1100000000, 250000000, 4500000000, 800000000, 300000000, 80000000, 280000000),
        ("Cataluña",         13800000000, 4900000000, 1200000000, 17500000000, 2200000000, 950000000, 300000000, 4500000000),
        ("Comunidad de Madrid", 8200000000, 3800000000, 350000000, 12200000000, 1900000000, 700000000, 150000000, 1700000000),
        ("País Vasco",       3300000000, 1400000000, 220000000, 4800000000, 850000000, 500000000, 100000000, 600000000),
    ]
    for r in rows:
        ws.append(r)
    wb.save(str(path))


def main():
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        src = td / "SGCIEF_2024.xlsx"
        out = td / "out.parquet"
        build_fixture_xlsx(src)

        rows = eh.parse_xlsx(src, 2024)
        assert len(rows) == 5 * 8, f"Esperadas 40 filas tidy, encontradas {len(rows)}"
        ccaa_set = {r['ccaa_id3'] for r in rows}
        assert ccaa_set == {'and','can','cat','mad','pvc'}, ccaa_set
        capa_set = {r['capa'] for r in rows}
        assert capa_set == {'hacienda'}, capa_set
        # Capítulo 4 Andalucía = 18B
        and_t = [r for r in rows if r['ccaa_id3']=='and' and r['capitulo']==4]
        assert len(and_t) == 1 and and_t[0]['importe_eur'] == 18000000000, and_t

        ok = eh.write_output(rows, out, 2024, src)
        assert ok and (out.exists() or out.with_suffix(".csv").exists())

        print(f"[hacienda OK] {len(rows)} filas tidy, capítulos {sorted({r['capitulo'] for r in rows})}, ccaa {ccaa_set}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
