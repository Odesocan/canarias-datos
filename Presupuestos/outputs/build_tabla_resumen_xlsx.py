#!/usr/bin/env python3
"""Genera el .xlsx de la tabla resumen (CCAA x anualidad) desde el CSV largo
outputs/tabla_resumen_<fecha>.csv. Hojas: Cobertura, pivotes por concepto
(Sanidad/Educacion/Gasto social/Total en mil M EUR) y Detalle completo."""
import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
FECHA = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
CSV = ROOT / "outputs" / f"tabla_resumen_{FECHA}.csv"
XLSX = ROOT / "outputs" / f"tabla_resumen_{FECHA}.xlsx"
YEARS = list(range(2015, 2027))

rows = list(csv.DictReader(open(CSV, newline="")))
# orden estable de CCAA por nombre
ccaa_order = []
seen = set()
for r in rows:
    if r["ccaa"] not in seen:
        seen.add(r["ccaa"]); ccaa_order.append((r["ccaa"], r["ccaa_nombre"]))

NAVY = "1F3A5F"; GREY = "E8ECF1"; hdr_fill = PatternFill("solid", fgColor=NAVY)
hdr_font = Font(bold=True, color="FFFFFF"); bold = Font(bold=True)
center = Alignment(horizontal="center"); right = Alignment(horizontal="right")
thin = Side(style="thin", color="C0C8D4"); border = Border(bottom=thin, right=thin)


def style_header(ws, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(1, c); cell.fill = hdr_fill; cell.font = hdr_font
        cell.alignment = center; cell.border = border
    ws.freeze_panes = "B2"
    ws.column_dimensions["A"].width = 18
    for c in range(2, ncols + 1):
        ws.column_dimensions[get_column_letter(c)].width = 9


def pivot_sheet(wb, title, field, scale=1e9, ndec=2):
    ws = wb.create_sheet(title)
    ws.cell(1, 1, "CCAA")
    for j, y in enumerate(YEARS, start=2):
        ws.cell(1, j, y)
    val = {(r["ccaa"], int(r["anio"])): r for r in rows}
    for i, (cid, cname) in enumerate(ccaa_order, start=2):
        ws.cell(i, 1, cname).font = bold
        for j, y in enumerate(YEARS, start=2):
            r = val.get((cid, y))
            v = ""
            if r and r.get("magnitud_disp") == "si" and r.get(field):
                try:
                    v = round(float(r[field]) / scale, ndec)
                except ValueError:
                    v = ""
            cell = ws.cell(i, j, v if v != "" else "·")
            cell.alignment = right
            if isinstance(v, float):
                cell.number_format = "#,##0.00"
            if i % 2 == 0:
                pass
    style_header(ws, len(YEARS) + 1)
    return ws


wb = openpyxl.Workbook()
# ---- Hoja Cobertura (estado + nº conceptos) ----
ws = wb.active; ws.title = "Cobertura"
ws.cById = None
ws.cell(1, 1, "CCAA")
for j, y in enumerate(YEARS, start=2):
    ws.cell(1, j, y)
val = {(r["ccaa"], int(r["anio"])): r for r in rows}
for i, (cid, cname) in enumerate(ccaa_order, start=2):
    ws.cell(i, 1, cname).font = bold
    for j, y in enumerate(YEARS, start=2):
        r = val.get((cid, y))
        if not r:
            ws.cell(i, j, "—"); continue
        estado = r["estado"]; nc = r["n_conceptos"]
        tag = ("V" if estado == "VERDE" else "v") + str(nc)
        cell = ws.cell(i, j, tag); cell.alignment = center
        if estado == "VERDE":
            cell.font = Font(bold=True, color="15803D")
style_header(ws, len(YEARS) + 1)

# ---- Pivotes por concepto (mil M EUR nominales) ----
pivot_sheet(wb, "Sanidad (mil M€)", "imp_sanidad")
pivot_sheet(wb, "Educacion (mil M€)", "imp_educacion")
pivot_sheet(wb, "Gasto social 13 (mil M€)", "gasto_social")
pivot_sheet(wb, "Total extraido (mil M€)", "total_extraido")

# ---- Detalle completo (largo) ----
ws = wb.create_sheet("Detalle")
cols = list(rows[0].keys())
ws.append(cols)
for r in rows:
    out = []
    for c in cols:
        v = r[c]
        if c.startswith("imp_") or c in ("total_extraido", "gasto_social"):
            try:
                v = round(float(v) / 1e9, 3) if v else ""
            except ValueError:
                v = ""
        out.append(v)
    ws.append(out)
for c in range(1, len(cols) + 1):
    cell = ws.cell(1, c); cell.fill = hdr_fill; cell.font = hdr_font; cell.alignment = center
ws.freeze_panes = "D2"
ws.column_dimensions["B"].width = 16

wb.save(XLSX)
print(f"OK {XLSX.name} · hojas={wb.sheetnames}")
