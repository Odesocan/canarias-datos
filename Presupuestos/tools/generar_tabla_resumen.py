#!/usr/bin/env python3
"""
generar_tabla_resumen.py — Tabla resumen de Presupuestos por CCAA x anualidad.

Lee el staging Python mas reciente (capa autonomica, EUR nominales) y, si existe,
la capa Hacienda (outputs/hacienda_staging.csv), y produce:

  outputs/tabla_resumen_<fecha>.csv   (una fila por CCAA-anio, con imp_<concepto>)
  outputs/tabla_resumen_<fecha>.md    (cobertura + gasto social + sanidad + conciliacion)
  outputs/tabla_resumen_<fecha>.xlsx  (hojas: cobertura, gasto_social, sanidad, conciliacion, detalle)

No toca extractores ni la DB: solo consolida el staging ya extraido.

Uso:
    python3 tools/generar_tabla_resumen.py [--staging <ruta.csv>] [--fecha YYYY-MM-DD]
"""
from __future__ import annotations
import argparse, csv, collections, datetime, glob, os, sys

CONCEPTOS = ["sanidad","educacion","soberania","direccion","vivienda","empleo","idi",
             "dependencia","discapacidad","salud_mental","diversidad","turismo","igualdad"]
NOMBRES = {"and":"Andalucia","ara":"Aragon","ast":"Asturias","bal":"Baleares","can":"Canarias",
           "cat":"Cataluna","clm":"Cast.-La Mancha","cnt":"Cantabria","cym":"Cast. y Leon",
           "ext":"Extremadura","gal":"Galicia","lar":"La Rioja","mad":"Madrid","mur":"Murcia",
           "nav":"Navarra","pvc":"Pais Vasco","val":"C. Valenciana"}
YEARS = list(range(2015,2027))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def latest_staging():
    fs = sorted(glob.glob(os.path.join(ROOT,"outputs","staging_py_*.csv")))
    if not fs: sys.exit("No hay outputs/staging_py_*.csv")
    return fs[-1]

def load_autonomic(path):
    """-> {(ccaa,anio): {concepto: eur, '_total': eur, '_filas': n, '_nconc': k}}"""
    agg = collections.defaultdict(lambda: collections.defaultdict(float))
    filas = collections.Counter(); concset = collections.defaultdict(set)
    for r in csv.DictReader(open(path, encoding="utf-8")):
        c = r["ccaa_id3"]; a = int(r["anio"]); k = (c,a)
        imp = float(r["importe_eur"] or 0)
        con = (r.get("concepto") or "").strip()
        agg[k]["_total"] += imp
        filas[k] += 1
        if con:
            agg[k][con] += imp
            concset[k].add(con)
    out = {}
    for k,d in agg.items():
        row = {con: d.get(con,0.0) for con in CONCEPTOS}
        row["gasto_clasificado"] = sum(row[con] for con in CONCEPTOS)
        # "Social estricto": excluye 'direccion' (que por metodologia actual incluye
        # el servicio de la deuda publica y la alta direccion -> no es gasto social).
        row["gasto_social"] = row["gasto_clasificado"] - row["direccion"]
        row["total_extraido"] = d["_total"]
        row["filas"] = filas[k]
        row["n_conceptos"] = len(concset[k])
        out[k] = row
    return out

def load_hacienda():
    p = os.path.join(ROOT,"outputs","hacienda_staging.csv")
    h = collections.defaultdict(float)
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8")):
            h[(r["ccaa_id3"], int(r["anio"]))] += float(r["importe_eur"] or 0)
    return h

def b(x):  # a mil millones (billones ES), 2 dec
    return round(x/1e9, 2) if x else 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--staging")
    ap.add_argument("--fecha", default=datetime.date.today().isoformat())
    args = ap.parse_args()
    staging = args.staging or latest_staging()
    fecha = args.fecha

    A = load_autonomic(staging)
    H = load_hacienda()
    ccaa = sorted(NOMBRES)
    nceldas = len(A)

    # ---- CSV detalle ----
    csv_path = os.path.join(ROOT,"outputs",f"tabla_resumen_{fecha}.csv")
    cols = ["ccaa","ccaa_nombre","anio","filas","n_conceptos"] + \
           [f"imp_{c}" for c in CONCEPTOS] + \
           ["gasto_social_estricto","gasto_clasificado","total_extraido",
            "total_hacienda","social_estricto_pct","cobertura_clasif_pct"]
    with open(csv_path,"w",newline="",encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cols)
        for c in ccaa:
            for a in YEARS:
                k=(c,a)
                if k not in A: continue
                r=A[k]; ht=H.get(k,0.0)
                soc = round(100*r["gasto_social"]/ht,1) if ht else ""
                cla = round(100*r["gasto_clasificado"]/ht,1) if ht else ""
                w.writerow([c,NOMBRES[c],a,r["filas"],r["n_conceptos"]]+
                           [round(r[cc],2) for cc in CONCEPTOS]+
                           [round(r["gasto_social"],2),round(r["gasto_clasificado"],2),
                            round(r["total_extraido"],2),round(ht,2),soc,cla])

    # ---- helpers de tabla markdown ----
    def grid(valfn):
        lines=["| CCAA | "+" | ".join(str(y) for y in YEARS)+" |",
               "|------|"+"---:|"*len(YEARS)]
        for c in ccaa:
            cells=[]
            for a in YEARS:
                v=valfn(c,a); cells.append(v if v is not None else "·")
            lines.append(f"| {NOMBRES[c]} | "+" | ".join(str(x) for x in cells)+" |")
        return "\n".join(lines)

    def f_social(c,a):
        r=A.get((c,a)); return b(r["gasto_social"]) if r else None
    def f_sanidad(c,a):
        r=A.get((c,a)); return b(r["sanidad"]) if r else None
    def f_cob(c,a):  # share social estricto sobre total Hacienda
        r=A.get((c,a)); ht=H.get((c,a),0.0)
        if not r or not ht: return None
        return round(100*r["gasto_social"]/ht,1)
    def f_clasif(c,a):  # % del presupuesto que queda clasificado (validacion cobertura)
        r=A.get((c,a)); ht=H.get((c,a),0.0)
        if not r or not ht: return None
        return round(100*r["gasto_clasificado"]/ht,1)
    def f_nconc(c,a):
        r=A.get((c,a)); return r["n_conceptos"] if r else None

    tot_social = sum(A[k]["gasto_social"] for k in A)
    tot_clasif = sum(A[k]["gasto_clasificado"] for k in A)
    md_path = os.path.join(ROOT,"outputs",f"tabla_resumen_{fecha}.md")
    with open(md_path,"w",encoding="utf-8") as f:
        f.write(f"# Tabla resumen · Presupuestos por CCAA × anualidad — {fecha}\n\n")
        f.write(f"**Cobertura capa autonomica:** {nceldas}/204 celdas CCAA-año "
                f"(17 CCAA × 2015-2026). **Capa Hacienda (SGCIEF):** {len(H)} celdas "
                f"(2015-2025; 2026 aun sin publicar). Magnitudes en EUR **nominales** del "
                f"staging Python (la DB guarda EUR constantes deflactados).\n\n")
        f.write("## Conceptos sociales cubiertos por celda (de 13)\n\n")
        f.write(grid(f_nconc)+"\n\n")
        f.write("## Gasto social estricto (€ mil M) — 12 conceptos, EXCLUYE `direccion`\n\n")
        f.write("_`direccion` se excluye porque, por metodologia vigente, agrega la alta "
                "direccion y el **servicio de la deuda publica** (arbitraje conceptual abierto, "
                "ver `logs/progreso.md`), y no es gasto social en sentido estricto._\n\n")
        f.write(grid(f_social)+"\n\n")
        f.write("## Sanidad (€ mil M)\n\n")
        f.write(grid(f_sanidad)+"\n\n")
        f.write("## Share social estricto sobre presupuesto liquidado Hacienda (%)\n\n")
        f.write("_Gasto social estricto / total SGCIEF. Bandas plausibles ~30-55%._\n\n")
        f.write(grid(f_cob)+"\n\n")
        f.write("## Validacion — cobertura de clasificacion (13 conceptos incl. direccion) / Hacienda (%)\n\n")
        f.write("_Que fraccion del presupuesto liquidado queda mapeada a algun concepto. "
                "Cercano a 100% = extraccion capta casi todo el presupuesto (deseable). "
                ">100% puntual = desfase perimetro/temporal nominal (p.ej. Cataluna 2019)._\n\n")
        f.write(grid(f_clasif)+"\n\n")
        f.write(f"**Gasto social estricto agregado (17 CCAA, 2015-2026, nominal):** "
                f"{tot_social/1e9:,.1f} mil M€.  \n")
        f.write(f"**Gasto clasificado agregado (incl. direccion+deuda):** "
                f"{tot_clasif/1e9:,.1f} mil M€.\n")

    # ---- XLSX ----
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Alignment
        wb = openpyxl.Workbook()
        def sheet(name, valfn, first="CCAA"):
            ws = wb.create_sheet(name)
            ws.append([first]+[str(y) for y in YEARS])
            for cell in ws[1]:
                cell.font=Font(bold=True); cell.fill=PatternFill("solid",fgColor="1F3864")
                cell.font=Font(bold=True,color="FFFFFF")
            for c in ccaa:
                ws.append([NOMBRES[c]]+[valfn(c,a) if valfn(c,a) is not None else "" for a in YEARS])
            ws.column_dimensions["A"].width=18
            return ws
        wb.remove(wb.active)
        sheet("conceptos", f_nconc)
        sheet("social_estricto_B", f_social)
        sheet("sanidad_B", f_sanidad)
        sheet("share_social_pct", f_cob)
        sheet("cobertura_clasif_pct", f_clasif)
        # detalle
        ws=wb.create_sheet("detalle")
        ws.append(cols)
        for cell in ws[1]:
            cell.font=Font(bold=True,color="FFFFFF"); cell.fill=PatternFill("solid",fgColor="1F3864")
        with open(csv_path, encoding="utf-8") as fr:
            rd=csv.reader(fr); next(rd)
            for row in rd:
                out=[]
                for i,x in enumerate(row):
                    if i>=2:
                        try: out.append(float(x))
                        except (ValueError,TypeError): out.append(x)
                    else:
                        out.append(x)
                ws.append(out)
        xlsx_path=os.path.join(ROOT,"outputs",f"tabla_resumen_{fecha}.xlsx")
        wb.save(xlsx_path)
    except Exception as e:
        xlsx_path=f"(xlsx omitido: {e})"

    print("STAGING :", os.path.relpath(staging,ROOT))
    print("CSV     :", os.path.relpath(csv_path,ROOT))
    print("MD      :", os.path.relpath(md_path,ROOT))
    print("XLSX    :", xlsx_path if xlsx_path.startswith("(") else os.path.relpath(xlsx_path,ROOT))
    print(f"CELDAS  : {nceldas}/204 autonomica · {len(H)} hacienda")
    print(f"GASTO SOCIAL AGREGADO (nominal): {tot_social/1e9:,.1f} mil M€")

if __name__=="__main__":
    main()
