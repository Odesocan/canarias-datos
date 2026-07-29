#!/usr/bin/env python3
"""Genera `1_extraccion/ccaa/<id3>/trazabilidad-<id3>.md` para cada CCAA.

Documenta, AÑO POR AÑO, de qué códigos/programas presupuestarios sale cada uno de
los 13 conceptos canónicos y con qué importe total, más un bloque de detección de
outliers (saltos interanuales, conceptos que aparecen/desaparecen, códigos que
cambian de concepto entre años, códigos duplicados).

Fuente: `2_transformacion/gasto_detalle.rds`, capa autonómica, € NOMINALES. Es el
concepto FINAL calculado por `asignar_concepto` en R (root correspondencias.yml +
overrides por CCAA + fallback al local de Python) — el mismo que carga la base de
datos. NO usar `1_extraccion/staging_gasto.rds`: ese es el concepto LOCAL de Python,
previo a la fase de transformación, y diverge del final en ~3 % de las filas
(verificado 2026-07-27: 768/23662 filas, ~25.000 M€ nominales, 16/17 CCAA) siempre
que el código emitido en extracción no coincide byte a byte con el que ve R tras la
normalización numérica (p. ej. val emite "121.20" en extracción pero R lo colapsa a
"121.2"), o el override raíz por CCAA gana explícitamente al local. Requiere haber
corrido el paso `transformacion` del maestro (Rscript 00_maestro.R
--steps=extraccion,transformacion,...); si solo se corrió `extraccion`, este fichero
no existe o está desactualizado — el script lo comprueba por fecha.
El RDS se exporta a CSV con Rscript la primera vez (cache en `outputs/.cache/`).

Uso:
    python3 tools/build_trazabilidad_md.py            # todas las CCAA
    python3 tools/build_trazabilidad_md.py and ara    # solo esas
    python3 tools/build_trazabilidad_md.py --csv X.csv --dry-run
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RDS = ROOT / "2_transformacion" / "gasto_detalle.rds"
CACHE = ROOT / "outputs" / ".cache" / "staging_autonomica.csv"
CCAA_DIR = ROOT / "1_extraccion" / "ccaa"

CONCEPTOS = [
    "sanidad", "educacion", "soberania", "direccion", "vivienda", "empleo", "idi",
    "dependencia", "discapacidad", "salud_mental", "diversidad", "turismo", "igualdad",
]
SIN = "(sin concepto)"

# Umbrales del detector de outliers
UMBRAL_SALTO = 0.40          # |Δ| interanual que se marca como sospechoso
UMBRAL_MATERIAL = 0.005      # el concepto debe pesar >0,5 % del total del año para alertar
UMBRAL_CODIGO = 0.01         # un código que aparece/desaparece pesando >1 % del año
TOP_SIN_CONCEPTO = 25        # nº de líneas sin concepto que se listan por año

CSV_COLS = [
    "ccaa_id3", "ccaa", "anio", "codigo", "denominacion", "importe_eur", "concepto",
    "capitulo", "pagina", "fuente_path", "fuente_url", "es_prorroga", "consolidacion",
    "unidad_origen", "alias",
]


# ---------------------------------------------------------------- carga de datos
def exportar_rds(destino: Path) -> None:
    """Vuelca la capa autonómica del gasto_detalle (concepto FINAL de R) a CSV."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    r = f'''
x <- readRDS("{RDS}")
a <- subset(x, capa != "hacienda")
a$concepto[is.na(a$concepto)] <- ""
write.csv(a[, c({",".join(f'"{c}"' for c in CSV_COLS)})],
          "{destino}", row.names = FALSE, na = "")
'''
    subprocess.run(["Rscript", "-e", r], check=True, capture_output=True, text=True)


def cargar(csv_path: Path | None) -> list[dict]:
    if csv_path is None:
        if not RDS.exists():
            raise SystemExit(
                f"✗ No existe {RDS.relative_to(ROOT)}. Corre el paso `transformacion` del "
                "maestro primero (Rscript 00_maestro.R --steps=extraccion,transformacion,...); "
                "NO uses 1_extraccion/staging_gasto.rds, que es el concepto pre-R y diverge "
                "del final en ~3% de las filas."
            )
        if not CACHE.exists() or CACHE.stat().st_mtime < RDS.stat().st_mtime:
            print(f"· exportando {RDS.relative_to(ROOT)} → {CACHE.relative_to(ROOT)}")
            exportar_rds(CACHE)
        csv_path = CACHE
    with open(csv_path, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    for r in filas:
        r["anio"] = int(r["anio"])
        r["importe_eur"] = float(r["importe_eur"] or 0)
        r["concepto"] = (r["concepto"] or "").strip() or SIN
        r["denominacion"] = " ".join((r["denominacion"] or "").split())
    return filas


# ---------------------------------------------------------------- formateo
def eur(x: float) -> str:
    """12345678.9 -> '12.345.679'"""
    s = f"{round(x):,}".replace(",", ".")
    return s


def meur(x: float) -> str:
    """En millones con 2 decimales, coma decimal."""
    return f"{x / 1e6:,.2f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def pct(x: float) -> str:
    return f"{x * 100:,.1f}".replace(".", ",") + " %"


def celda_var(v: float | None) -> str:
    if v is None:
        return "·"
    marca = " ⚠" if abs(v) >= UMBRAL_SALTO else ""
    sig = "+" if v >= 0 else "−"
    return f"{sig}{abs(v) * 100:,.1f}".replace(".", ",") + f" %{marca}"


def esc(s: str) -> str:
    return s.replace("|", "\\|")


# ---------------------------------------------------------------- agregaciones
def agregar(filas: list[dict]):
    """Devuelve estructuras agregadas para una CCAA."""
    anios = sorted({r["anio"] for r in filas})
    # (anio, concepto) -> importe
    mat = collections.defaultdict(float)
    # (anio, concepto) -> {(codigo, denominacion): [importe, n_filas]}
    detalle = collections.defaultdict(lambda: collections.defaultdict(lambda: [0.0, 0]))
    total_anio = collections.defaultdict(float)
    n_anio = collections.Counter()
    for r in filas:
        k = (r["anio"], r["concepto"])
        mat[k] += r["importe_eur"]
        d = detalle[k][(r["codigo"], r["denominacion"])]
        d[0] += r["importe_eur"]
        d[1] += 1
        total_anio[r["anio"]] += r["importe_eur"]
        n_anio[r["anio"]] += 1
    return anios, mat, detalle, total_anio, n_anio


def ficha_anual(filas: list[dict]):
    """Metadatos por año: fuentes, prórroga, unidad, % con concepto."""
    out = {}
    por_anio = collections.defaultdict(list)
    for r in filas:
        por_anio[r["anio"]].append(r)
    for anio, rs in por_anio.items():
        fuentes = sorted({os.path.basename(r["fuente_path"]) for r in rs if r["fuente_path"]})
        urls = sorted({r["fuente_url"] for r in rs if r["fuente_url"]})
        con_c = sum(1 for r in rs if r["concepto"] != SIN)
        out[anio] = {
            "fuentes": fuentes,
            "urls": urls,
            "n": len(rs),
            "pct_concepto": con_c / len(rs) if rs else 0.0,
            "prorroga": any(str(r["es_prorroga"]).upper() in ("TRUE", "1") for r in rs),
            "consolidacion": sorted({r["consolidacion"] for r in rs if r["consolidacion"]}),
            "unidad": sorted({r["unidad_origen"] for r in rs if r["unidad_origen"]}),
            "alias": sorted({r["alias"] for r in rs if r["alias"]}),
            "total": sum(r["importe_eur"] for r in rs),
            "n_conceptos": len({r["concepto"] for r in rs if r["concepto"] != SIN}),
        }
    return out


def detectar_alertas(anios, mat, detalle, total_anio, filas):
    """Devuelve (alertas_concepto, codigos_inestables, codigos_duplicados)."""
    alertas = []
    # A. saltos interanuales y apariciones/desapariciones por concepto
    for c in CONCEPTOS:
        for a, b in zip(anios, anios[1:]):
            v0, v1 = mat.get((a, c), 0.0), mat.get((b, c), 0.0)
            peso = max(v0 / total_anio[a] if total_anio[a] else 0,
                       v1 / total_anio[b] if total_anio[b] else 0)
            if peso < UMBRAL_MATERIAL:
                continue
            if v0 == 0 and v1 > 0:
                alertas.append((b, c, "APARECE", f"0 → {meur(v1)} M€", v1))
            elif v0 > 0 and v1 == 0:
                alertas.append((b, c, "DESAPARECE", f"{meur(v0)} M€ → 0", v0))
            elif v0 > 0:
                d = (v1 - v0) / v0
                if abs(d) >= UMBRAL_SALTO:
                    alertas.append((b, c, "SALTO", f"{meur(v0)} → {meur(v1)} M€ ({celda_var(d)})", abs(v1 - v0)))
    # A2. salto del total extraído
    for a, b in zip(anios, anios[1:]):
        if total_anio[a] > 0:
            d = (total_anio[b] - total_anio[a]) / total_anio[a]
            if abs(d) >= 0.25:
                alertas.append((b, "TOTAL", "SALTO",
                                f"{meur(total_anio[a])} → {meur(total_anio[b])} M€ ({celda_var(d)})",
                                abs(total_anio[b] - total_anio[a])))
    alertas.sort(key=lambda t: (t[0], t[1]))

    # B. códigos cuyo concepto cambia entre años
    cod_concepto = collections.defaultdict(dict)   # codigo -> anio -> set(conceptos)
    cod_importe = collections.defaultdict(dict)
    for r in filas:
        cod_concepto[r["codigo"]].setdefault(r["anio"], set()).add(r["concepto"])
        cod_importe[r["codigo"]][r["anio"]] = cod_importe[r["codigo"]].get(r["anio"], 0) + r["importe_eur"]
    inestables = []
    for cod, por_anio in cod_concepto.items():
        vistos = set()
        for s in por_anio.values():
            vistos |= s
        if len(vistos) > 1:
            imp_max = max(cod_importe[cod].values())
            traza = ", ".join(
                f"{a}:{'/'.join(sorted(por_anio[a]))}" for a in sorted(por_anio)
            )
            inestables.append((imp_max, cod, traza))
    inestables.sort(reverse=True)

    # C. códigos duplicados dentro de un mismo año (posible doble conteo)
    dup = collections.defaultdict(lambda: [0.0, 0])
    cnt = collections.Counter()
    for r in filas:
        cnt[(r["anio"], r["codigo"])] += 1
    for r in filas:
        if cnt[(r["anio"], r["codigo"])] > 1:
            d = dup[(r["anio"], r["codigo"], r["concepto"])]
            d[0] += r["importe_eur"]
            d[1] += 1
    duplicados = sorted(
        ((a, c, con, v[0], v[1]) for (a, c, con), v in dup.items()),
        key=lambda t: -t[3],
    )
    return alertas, inestables, duplicados


# ---------------------------------------------------------------- render
def render(id3: str, nombre: str, filas: list[dict], hoy: str) -> str:
    anios, mat, detalle, total_anio, n_anio = agregar(filas)
    ficha = ficha_anual(filas)
    alertas, inestables, duplicados = detectar_alertas(anios, mat, detalle, total_anio, filas)

    L: list[str] = []
    A = L.append

    # ---- cabecera
    A(f"# Trazabilidad de la extracción — {nombre} (`{id3}`)")
    A("")
    A("> **Qué códigos presupuestarios alimentan cada concepto, año por año, y con qué importe.**")
    A("> Generado automáticamente por [`tools/build_trazabilidad_md.py`](../../../tools/build_trazabilidad_md.py)")
    A(f"> desde `1_extraccion/staging_gasto.rds` (capa `autonomica`). Rev.: {hoy}.")
    A("")
    A("## 0 · Cómo leer este documento")
    A("")
    A("- **Unidad: € NOMINALES.** El staging guarda euros corrientes; la tabla final")
    A("  `presupuestos.ced_presupuestos` guarda € **constantes** (deflactados), así que los")
    A("  números de la BD y de la visualización D3 serán distintos (~×1,3 en los años antiguos).")
    A("  Para auditar el ORIGEN de un outlier, usa estas cifras; para auditar la serie publicada,")
    A("  recuerda aplicar el deflactor.")
    A("- El **importe de cada concepto-año es la suma de los importes de los códigos listados**")
    A("  en §5. Si un concepto salta de un año a otro, §4 te dice en qué año y §5 qué código")
    A("  entró o salió.")
    A("- `(sin concepto)` = líneas extraídas que **no** mapean a ninguno de los 13 conceptos")
    A("  (deuda, dirección general no social, etc.). Es esperable que sea el 25-40 % del total;")
    A("  no es un error, pero un salto brusco aquí suele señalar un cambio de clasificación.")
    A(f"- Marca ⚠ = variación interanual ≥ {int(UMBRAL_SALTO * 100)} % en un concepto que pesa")
    A(f"  ≥ {UMBRAL_MATERIAL * 100:.1f} % del total del año".replace(".", ",") +
      ". Es un **candidato a revisión**, no un error probado:")
    A("  puede ser un cambio presupuestario real.")
    A("")

    # ---- §1 ficha por año
    A("## 1 · Fuente y cobertura, año por año")
    A("")
    A("| Año | Filas | Documento fuente | Conceptos | % líneas con concepto | Total extraído (M€ nom.) | Prórroga | Consolidación |")
    A("|---|---:|---|---:|---:|---:|:-:|---|")
    for a in anios:
        f = ficha[a]
        fuentes = "<br>".join(f"`{esc(x)}`" for x in f["fuentes"]) or "—"
        A(f"| **{a}** | {f['n']} | {fuentes} | {f['n_conceptos']} | {pct(f['pct_concepto'])} | "
          f"{meur(f['total'])} | {'sí' if f['prorroga'] else '—'} | {', '.join(f['consolidacion']) or '—'} |")
    A("")
    urls = sorted({u for f in ficha.values() for u in f["urls"]})
    if urls:
        A("**URL(s) de origen:**")
        for u in urls[:12]:
            A(f"- <{u}>")
        if len(urls) > 12:
            A(f"- … y {len(urls) - 12} más (ver `fuentes.yml`).")
        A("")

    # ---- §2 matriz concepto × año
    A("## 2 · Matriz concepto × año — importe total (M€ nominales)")
    A("")
    A("| Concepto | " + " | ".join(str(a) for a in anios) + " |")
    A("|---|" + "---:|" * len(anios))
    presentes = [c for c in CONCEPTOS if any(mat.get((a, c), 0) for a in anios)]
    ausentes = [c for c in CONCEPTOS if c not in presentes]
    for c in presentes:
        celdas = []
        for a in anios:
            v = mat.get((a, c), 0.0)
            celdas.append(meur(v) if v else "—")
        A(f"| `{c}` | " + " | ".join(celdas) + " |")
    A("| **Σ asignado** | " + " | ".join(
        meur(sum(mat.get((a, c), 0.0) for c in CONCEPTOS)) for a in anios) + " |")
    A("| *(sin concepto)* | " + " | ".join(
        meur(mat.get((a, SIN), 0.0)) for a in anios) + " |")
    A("| **TOTAL extraído** | " + " | ".join(meur(total_anio[a]) for a in anios) + " |")
    A("")
    if ausentes:
        A(f"**Conceptos sin ninguna línea en toda la serie:** {', '.join('`' + c + '`' for c in ausentes)} "
          "— revisa si es NULL estructural (competencia no autonómica o no separable en esta clasificación) "
          "o un hueco de `correspondencias.yml`.")
        A("")

    # ---- §3 variación interanual
    A("## 3 · Variación interanual (%) — detector de saltos")
    A("")
    pares = list(zip(anios, anios[1:]))
    A("| Concepto | " + " | ".join(f"{a}→{b}" for a, b in pares) + " |")
    A("|---|" + "---:|" * len(pares))
    for c in presentes:
        celdas = []
        for a, b in pares:
            v0, v1 = mat.get((a, c), 0.0), mat.get((b, c), 0.0)
            if v0 == 0 and v1 == 0:
                celdas.append("·")
            elif v0 == 0:
                celdas.append("**nuevo** ⛔")
            elif v1 == 0:
                celdas.append("**a 0** ⛔")
            else:
                celdas.append(celda_var((v1 - v0) / v0))
        A(f"| `{c}` | " + " | ".join(celdas) + " |")
    celdas = []
    for a, b in pares:
        celdas.append(celda_var((total_anio[b] - total_anio[a]) / total_anio[a]) if total_anio[a] else "·")
    A("| **TOTAL** | " + " | ".join(celdas) + " |")
    A("")

    # ---- §4 alertas
    A("## 4 · Alertas automáticas (candidatos a revisión)")
    A("")
    if alertas:
        A("| Año | Concepto | Tipo | Detalle |")
        A("|---|---|---|---|")
        for a, c, tipo, det, _imp in alertas:
            A(f"| {a} | `{c}` | **{tipo}** | {det} |")
    else:
        A("Sin saltos ≥ 40 % en conceptos materiales. Serie estable.")
    A("")

    if duplicados:
        tot_dup = sum(d[3] for d in duplicados)
        A(f"### 4.1 · Códigos duplicados dentro del mismo año ({len(duplicados)} casos, {meur(tot_dup)} M€ acumulados)")
        A("")
        A("> Un mismo código aparece en **varias filas del mismo ejercicio**. Puede ser legítimo")
        A("> (mismo programa en varias secciones/centros gestores) o **doble conteo** que infla el total.")
        A("> Compruébalo contra el documento original antes de dar el año por bueno.")
        A("")
        A("| Año | Código | Concepto | Filas | Importe sumado (M€) |")
        A("|---|---|---|---:|---:|")
        for a, cod, con, imp, n in duplicados[:30]:
            A(f"| {a} | `{esc(cod)}` | `{con}` | {n} | {meur(imp)} |")
        if len(duplicados) > 30:
            A(f"| … | *{len(duplicados) - 30} casos más* | | | |")
        A("")

    if inestables:
        A(f"### 4.2 · Códigos que CAMBIAN de concepto entre años ({len(inestables)} casos)")
        A("")
        A("> Causa habitual de saltos interanuales artificiales: el mismo programa se contabiliza")
        A("> en un concepto un año y en otro al siguiente (renombre de la denominación, cambio de")
        A("> clasificación funcional, o keyword que deja de casar). Los 25 de mayor importe:")
        A("")
        A("| Código | Importe máx. (M€) | Concepto por año |")
        A("|---|---:|---|")
        for imp, cod, traza in inestables[:25]:
            A(f"| `{esc(cod)}` | {meur(imp)} | {esc(traza)} |")
        if len(inestables) > 25:
            A(f"| … | | *{len(inestables) - 25} códigos más* |")
        A("")

    # ---- §5 detalle año por año
    A("## 5 · Detalle año por año — qué códigos componen cada concepto")
    A("")
    for a in anios:
        f = ficha[a]
        A(f"### {a}")
        A("")
        A(f"*Fuente: {', '.join('`' + esc(x) + '`' for x in f['fuentes']) or '—'} · "
          f"{f['n']} líneas · total extraído **{meur(f['total'])} M€** (nominales)"
          f"{' · PRÓRROGA' if f['prorroga'] else ''}*")
        A("")
        for c in CONCEPTOS:
            items = detalle.get((a, c))
            if not items:
                continue
            tot = mat[(a, c)]
            share = tot / total_anio[a] if total_anio[a] else 0
            orden = sorted(items.items(), key=lambda kv: -kv[1][0])
            A(f"<details open><summary><b><code>{c}</code> — {meur(tot)} M€ "
              f"({eur(tot)} €) · {len(orden)} códigos · {pct(share)} del año</b></summary>")
            A("")
            A("| Código | Denominación | Importe (€) | % concepto |")
            A("|---|---|---:|---:|")
            for (cod, den), (imp, n) in orden:
                sufijo = f" *(×{n} filas)*" if n > 1 else ""
                A(f"| `{esc(cod)}` | {esc(den)}{sufijo} | {eur(imp)} | {pct(imp / tot) if tot else '—'} |")
            A("")
            A("</details>")
            A("")
        # sin concepto
        items = detalle.get((a, SIN))
        if items:
            tot = mat[(a, SIN)]
            orden = sorted(items.items(), key=lambda kv: -kv[1][0])
            A(f"<details><summary><code>(sin concepto)</code> — {meur(tot)} M€ · {len(orden)} códigos · "
              f"{pct(tot / total_anio[a] if total_anio[a] else 0)} del año "
              f"(se listan los {min(TOP_SIN_CONCEPTO, len(orden))} mayores)</summary>")
            A("")
            A("| Código | Denominación | Importe (€) |")
            A("|---|---|---:|")
            for (cod, den), (imp, n) in orden[:TOP_SIN_CONCEPTO]:
                sufijo = f" *(×{n} filas)*" if n > 1 else ""
                A(f"| `{esc(cod)}` | {esc(den)}{sufijo} | {eur(imp)} |")
            resto = orden[TOP_SIN_CONCEPTO:]
            if resto:
                A(f"| … | *resto: {len(resto)} códigos* | {eur(sum(v[0] for _, v in resto))} |")
            A("")
            A("</details>")
            A("")

    # ---- §6 reproducir
    A("## 6 · Cómo reproducir / verificar")
    A("")
    A("```bash")
    A(f"python3 tools/build_trazabilidad_md.py {id3}     # regenera este documento")
    A(f"python3 tools/auditoria_magnitud.py {id3}        # test de continuidad y per cápita")
    A(f"cd 1_extraccion && python3 -m ccaa --ccaa {id3} --anio <año> \\")
    A(f"    --input ../fuentes/raw/{id3}/<año>/<fichero> --output /tmp/{id3}.csv")
    A("```")
    A("")
    A(f"Mapeo código→concepto: [`correspondencias.yml`](correspondencias.yml) · "
      f"Motor: [`extract.py`](extract.py) · Limitaciones conocidas: "
      f"[`limitaciones-{id3}.md`](limitaciones-{id3}.md)")
    A("")
    resumen = {
        "id3": id3, "nombre": nombre, "anios": anios,
        "alertas": alertas, "inestables": inestables, "duplicados": duplicados,
        "n_conceptos": len(presentes), "ausentes": ausentes,
        "total_dup": sum(d[3] for d in duplicados),
    }
    return "\n".join(L) + "\n", resumen


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ccaa", nargs="*", help="id3 a generar (por defecto todas)")
    ap.add_argument("--csv", type=Path, default=None, help="CSV de staging alternativo")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, solo informa")
    args = ap.parse_args()

    filas = cargar(args.csv)
    hoy = dt.date.today().isoformat()
    por_ccaa = collections.defaultdict(list)
    for r in filas:
        por_ccaa[r["ccaa_id3"]].append(r)

    objetivo = args.ccaa or sorted(por_ccaa)
    resumenes = []
    for id3 in objetivo:
        if id3 not in por_ccaa:
            print(f"  ! {id3}: sin filas en el staging", file=sys.stderr)
            continue
        rs = por_ccaa[id3]
        nombre = rs[0]["ccaa"] or id3
        md, resumen = render(id3, nombre, rs, hoy)
        resumenes.append(resumen)
        destino = CCAA_DIR / id3 / f"trazabilidad-{id3}.md"
        if args.dry_run:
            print(f"  · {id3}: {len(md):,} chars ({len(rs)} filas) → {destino}")
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(md, encoding="utf-8")
        print(f"  ✓ {destino.relative_to(ROOT)}  ({len(rs)} filas, {len(md) // 1024} KB)")

    if not args.dry_run and len(resumenes) > 1:
        escribir_indice(resumenes, hoy)
    return 0


def escribir_indice(resumenes: list[dict], hoy: str) -> None:
    """Índice transversal de alertas: por dónde empezar a revisar los outliers del D3."""
    L: list[str] = []
    A = L.append
    A(f"# Índice de alertas de trazabilidad — {len(resumenes)} CCAA · rev. {hoy}")
    A("")
    A("> Resumen transversal generado por `tools/build_trazabilidad_md.py`. El detalle")
    A("> código-a-concepto está en `1_extraccion/ccaa/<id3>/trazabilidad-<id3>.md`.")
    A("> Importes en € NOMINALES (la BD y el D3 usan € constantes deflactados).")
    A("")
    A("## 1 · Semáforo por CCAA")
    A("")
    A("| CCAA | Años | Conceptos | Alertas | Cód. inestables | Cód. duplicados | M€ duplicados | Conceptos ausentes |")
    A("|---|---|---:|---:|---:|---:|---:|---|")
    for r in sorted(resumenes, key=lambda x: -len(x["alertas"])):
        A(f"| [`{r['id3']}`](../1_extraccion/ccaa/{r['id3']}/trazabilidad-{r['id3']}.md) "
          f"{r['nombre']} | {min(r['anios'])}-{max(r['anios'])} | {r['n_conceptos']} | "
          f"{len(r['alertas'])} | {len(r['inestables'])} | {len(r['duplicados'])} | "
          f"{meur(r['total_dup']) if r['total_dup'] else '—'} | "
          f"{', '.join(r['ausentes']) or '—'} |")
    A("")
    A("## 2 · Top 60 alertas por impacto absoluto (M€ nominales)")
    A("")
    A("> Ordenadas por el importe en juego, no por el % — son las que más pueden distorsionar")
    A("> la visualización. `TOTAL` = salto del total extraído del ejercicio (≥ 25 %).")
    A("")
    todas = []
    for r in resumenes:
        for a, c, tipo, det, imp in r["alertas"]:
            todas.append((imp, r["id3"], a, c, tipo, det))
    todas.sort(reverse=True)
    A("| # | Impacto (M€) | CCAA | Año | Concepto | Tipo | Detalle |")
    A("|---:|---:|---|---|---|---|---|")
    for i, (imp, id3, a, c, tipo, det) in enumerate(todas[:60], 1):
        A(f"| {i} | {meur(imp)} | `{id3}` | {a} | `{c}` | **{tipo}** | {det} |")
    A("")
    A(f"*Total de alertas en las {len(resumenes)} CCAA: {len(todas)}.*")
    A("")
    destino = ROOT / "outputs" / f"trazabilidad_alertas_{hoy}.md"
    destino.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"  ✓ {destino.relative_to(ROOT)}  ({len(todas)} alertas)")


if __name__ == "__main__":
    raise SystemExit(main())
