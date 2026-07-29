#!/usr/bin/env python3
"""
nav_longitudinal.py — Extractor longitudinal del presupuesto de Navarra.

Fuente: https://presupuesto.navarra.es/es/politicas  (visor SPA cuyo HTML inicial
embebe TODOS los datos en variables JavaScript). NO se ejecuta navegador: se
descarga el HTML con `requests`, se parsea con BeautifulSoup, y se extraen los
literales JS con emparejamiento balanceado de llaves/corchetes.

Variables JS relevantes (verificadas 2026-06-29):
  years, budgetStatuses, stats, financialExpenseBreakdown, breakdowns, areas

`breakdowns` tiene 4 vistas: income, functional, expense, institutional (esta
última puede ser null). Cada vista es un árbol: {expense:{...}, income:{...},
years:[...], sub:{<code>: <nodo>}}. Cada nodo: {label, expense, income, sub}.
`expense`/`income` son dicts {"<YYYY>": <cents>, "actual_<YYYY>": <cents>}.

⚠️ Importes embebidos están escalados x100 (céntimos) → dividir por 100 = EUR.

Salida: dataset largo (una fila por vista × campo × año × medida × nodo),
JSON jerárquico normalizado, e informe de validación.

Uso:
    python3 tools/nav_longitudinal.py [--html <ruta_local.html>] [--no-download]

Sin --html descarga en vivo y cachea el HTML en fuentes/raw/nav/longitudinal/.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import io
import json
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Falta beautifulsoup4 (pip install beautifulsoup4)", file=sys.stderr)
    raise

SOURCE_URL = "https://presupuesto.navarra.es/es/politicas"
CSV_VALID = {
    "functional": "https://presupuesto.navarra.es/es/comunidad_navarra_gastosf.csv",
    "expense": "https://presupuesto.navarra.es/es/comunidad_navarra_gastos.csv",
    "income": "https://presupuesto.navarra.es/es/comunidad_navarra_ingresos.csv",
}
# Campo de medida por vista (functional/expense miden gasto; income mide ingreso)
VIEW_FIELD = {
    "functional": "expense",
    "expense": "expense",
    "income": "income",
    "institutional": "expense",
}
JS_VARS = ["years", "budgetStatuses", "stats",
           "financialExpenseBreakdown", "breakdowns", "areas"]

ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = ROOT / "outputs" / "nav_longitudinal.csv"
OUT_JSON = ROOT / "outputs" / "nav_longitudinal_tree.json"
CACHE_DIR = ROOT / "fuentes" / "raw" / "nav" / "longitudinal"

COLUMNS = [
    "source_url", "extraction_date", "view", "field", "year", "measure",
    "amount_eur", "amount_raw", "code", "label", "parent_code", "parent_label",
    "level", "path_codes", "path_labels", "area_code", "area_label",
    "budget_status", "inflation", "inflation_index", "population",
]

VALIDATION_2025_FUNCTIONAL_EUR = 5986566198.00


# --------------------------------------------------------------------------- #
# 1-2. Descarga + parseo HTML
# --------------------------------------------------------------------------- #
def fetch_html(local: str | None, allow_download: bool) -> tuple[str, str]:
    """Devuelve (html, origen). Prioriza --html local; si no, descarga."""
    if local:
        p = Path(local)
        return p.read_text(encoding="utf-8", errors="replace"), f"local:{p}"
    if not allow_download:
        # usa la última caché si existe
        cached = sorted(CACHE_DIR.glob("politicas_*.html"))
        if cached:
            return cached[-1].read_text(encoding="utf-8", errors="replace"), f"cache:{cached[-1].name}"
        raise SystemExit("Sin --html y --no-download sin caché disponible.")
    import requests  # import tardío
    headers = {"User-Agent": "Mozilla/5.0 (ODESOCAN nav-extractor)"}
    last_err = None
    for verify in (True, False):  # algunos Mac fallan la verificación TLS
        try:
            r = requests.get(SOURCE_URL, headers=headers, timeout=120, verify=verify)
            r.raise_for_status()
            html = r.text
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            stamp = _dt.date.today().isoformat()
            (CACHE_DIR / f"politicas_{stamp}.html").write_text(html, encoding="utf-8")
            return html, ("download(verify)" if verify else "download(noverify)")
        except Exception as e:  # noqa: BLE001
            last_err = e
    raise SystemExit(f"No se pudo descargar {SOURCE_URL}: {last_err}")


# --------------------------------------------------------------------------- #
# 3-5. Extracción robusta de literales JS → estructuras Python
# --------------------------------------------------------------------------- #
def _all_script_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return "\n".join(s.string or "" for s in soup.find_all("script") if s.string)


def extract_js_literal(js: str, var_name: str) -> str | None:
    """Literal asignado a `var <name> = …` con balanceo de {}/[] y respeto de
    strings (comillas simples/dobles y escapes)."""
    import re
    m = re.search(rf"\bvar\s+{re.escape(var_name)}\s*=\s*", js)
    if not m:
        return None
    i = m.end()
    if i >= len(js) or js[i] not in "{[":
        return None
    open_c, close_c = js[i], ("}" if js[i] == "{" else "]")
    depth, in_str, quote, esc = 0, False, "", False
    start = i
    while i < len(js):
        c = js[i]
        if esc:
            esc = False
        elif c == "\\":
            esc = True
        elif in_str:
            if c == quote:
                in_str = False
        elif c in "\"'":
            in_str, quote = True, c
        elif c == open_c:
            depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return js[start:i + 1]
        i += 1
    return None


def js_to_obj(literal: str):
    """Literal JS de objeto/array → objeto Python. Normaliza claves/comas y
    null/true/false, luego json.loads (robusto para árboles anidados)."""
    import re
    s = literal
    s = re.sub(r"'([^'\\]*)'\s*:", r'"\1":', s)          # 'clave': → "clave":
    s = re.sub(r"([{,]\s*)([A-Za-z_]\w*)\s*:", r'\1"\2":', s)  # clave sin comillas
    s = re.sub(r",(\s*[}\]])", r"\1", s)                  # comas finales
    # valores string en comillas simples → dobles (cuidando escapes)
    s = re.sub(r":\s*'((?:[^'\\]|\\.)*)'", lambda m: ': "%s"' % m.group(1).replace('"', '\\"'), s)
    return json.loads(s)


def load_vars(html: str) -> dict:
    js = _all_script_text(html) or html  # fallback al HTML completo
    out = {}
    for v in JS_VARS:
        lit = extract_js_literal(js, v)
        out[v] = js_to_obj(lit) if lit is not None else None
    return out


# --------------------------------------------------------------------------- #
# 6-13. Construcción del dataset largo
# --------------------------------------------------------------------------- #
def _cents_to_eur(v):
    if v is None:
        return None
    try:
        return round(float(v) / 100.0, 2)
    except (TypeError, ValueError):
        return None


def walk_view(view: str, tree: dict, years: list[str], areas: dict,
              stats: dict, budget_statuses: dict, extraction_date: str) -> list[dict]:
    field = VIEW_FIELD.get(view, "expense")
    area_map = (areas or {}).get(view) or {}
    infl = (stats or {}).get("inflation") or {}
    popu = (stats or {}).get("population") or {}
    rows: list[dict] = []

    def emit(node: dict, path_codes: list[str], path_labels: list[str]):
        code = path_codes[-1]
        label = (node.get("label") or "").strip()
        level = len(path_codes) - 1
        parent_code = path_codes[-2] if level >= 1 else None
        parent_label = path_labels[-2] if level >= 1 else None
        area_code = code[:1] if code else None
        area_label = area_map.get(area_code) if area_code else None
        amounts = node.get(field) or {}
        for year in years:
            stat_y = budget_statuses.get(year) if isinstance(budget_statuses, dict) else None
            infl_y = infl.get(year) or {}
            base = dict(
                source_url=SOURCE_URL, extraction_date=extraction_date,
                view=view, field=field, year=year,
                code=code, label=label,
                parent_code=parent_code, parent_label=parent_label,
                level=level,
                path_codes=">".join(path_codes),
                path_labels=" > ".join(path_labels),
                area_code=area_code, area_label=area_label,
                budget_status=(stat_y if stat_y not in ("", None) else None),
                inflation=infl_y.get("inflation") if isinstance(infl_y, dict) else None,
                inflation_index=infl_y.get("inflation_index") if isinstance(infl_y, dict) else None,
                population=popu.get(year),
            )
            for measure, key in (("budget", year), ("actual", f"actual_{year}")):
                raw = amounts.get(key) if isinstance(amounts, dict) else None
                rows.append({**base, "measure": measure,
                             "amount_raw": raw, "amount_eur": _cents_to_eur(raw)})
        for ccode, child in (node.get("sub") or {}).items():
            if isinstance(child, dict):
                emit(child, path_codes + [ccode], path_labels + [(child.get("label") or "").strip()])

    for code, node in (tree.get("sub") or {}).items():
        if isinstance(node, dict):
            emit(node, [code], [(node.get("label") or "").strip()])
    return rows


# --------------------------------------------------------------------------- #
# 14-15. Validación
# --------------------------------------------------------------------------- #
def fetch_csv(url: str) -> str | None:
    try:
        import requests
        for verify in (True, False):
            try:
                r = requests.get(url, timeout=120, verify=verify,
                                 headers={"User-Agent": "Mozilla/5.0"})
                if r.status_code == 200:
                    return r.text
            except Exception:  # noqa: BLE001
                continue
    except Exception:  # noqa: BLE001
        pass
    return None


def validate(rows: list[dict], vars_: dict) -> dict:
    report = {}
    # 15. functional 2025, suma nivel-0 budget = 5.986.566.198,00 EUR
    s = sum(
        r["amount_eur"] or 0 for r in rows
        if r["view"] == "functional" and r["year"] == "2025"
        and r["measure"] == "budget" and r["level"] == 0 and r["amount_eur"] is not None
    )
    report["functional_2025_nivel0_eur"] = round(s, 2)
    report["functional_2025_match"] = abs(s - VALIDATION_2025_FUNCTIONAL_EUR) < 0.01

    # 14. cotejo NUMÉRICO por año contra el CSV oficial. El CSV funcional
    # (separador coma) trae Presupuesto Gasto en EUR a nivel política (Id
    # Programa vacío) y programa → cotejamos la suma nivel-0 por año de nuestro
    # HTML (escalado /100) contra la suma de filas-política del CSV. Esto valida
    # de paso el escalado céntimos→euros en TODOS los años, no solo 2025.
    csv_checks = {}
    # 14a. functional: cross-check numérico
    txt = fetch_csv(CSV_VALID["functional"])
    if txt:
        csv_year_pol = {}
        for r in csv.DictReader(io.StringIO(txt)):  # coma por defecto
            if (r.get("Id Programa") or "").strip():
                continue  # solo filas política (nivel 0)
            y = (r.get("Año") or "").strip()
            try:
                csv_year_pol[y] = csv_year_pol.get(y, 0.0) + float(r["Presupuesto Gasto"])
            except (TypeError, ValueError, KeyError):
                pass
        html_year0 = {}
        for r in rows:
            if r["view"] == "functional" and r["measure"] == "budget" and r["level"] == 0 \
                    and r["amount_eur"] is not None:
                html_year0[r["year"]] = html_year0.get(r["year"], 0.0) + r["amount_eur"]
        años_ok, años_diff = [], []
        for y in sorted(set(csv_year_pol) & set(html_year0)):
            if abs(csv_year_pol[y] - html_year0[y]) < 1.0:
                años_ok.append(y)
            else:
                años_diff.append((y, round(html_year0[y], 2), round(csv_year_pol[y], 2)))
        csv_checks["functional"] = {
            "status": "ok", "filas_csv": txt.count("\n"),
            "años_cotejados": len(años_ok) + len(años_diff),
            "años_coinciden": len(años_ok),
            "discrepancias": años_diff,
        }
    else:
        csv_checks["functional"] = {"status": "csv_no_disponible"}
    # 14b. expense/income: verificación de origen (descarga + filas)
    for view in ("expense", "income"):
        t = fetch_csv(CSV_VALID[view])
        csv_checks[view] = ({"status": "ok", "filas_csv": t.count("\n")} if t
                            else {"status": "csv_no_disponible"})
    report["csv_oficial"] = csv_checks
    return report


# --------------------------------------------------------------------------- #
def build_tree_json(vars_: dict) -> dict:
    """JSON jerárquico normalizado (vistas no nulas con su árbol original)."""
    bd = vars_.get("breakdowns") or {}
    return {v: bd.get(v) for v in ("functional", "expense", "income", "institutional")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", help="ruta a HTML local (evita descarga)")
    ap.add_argument("--no-download", action="store_true",
                    help="no descargar; usar caché si existe")
    args = ap.parse_args()

    extraction_date = _dt.date.today().isoformat()
    html, origen = fetch_html(args.html, allow_download=not args.no_download)
    vars_ = load_vars(html)

    years = vars_.get("years") or []
    areas = vars_.get("areas") or {}
    stats = vars_.get("stats") or {}
    bstat = vars_.get("budgetStatuses") or {}
    bd = vars_.get("breakdowns") or {}

    views_present = {v: (bd.get(v) is not None) for v in
                     ("functional", "expense", "income", "institutional")}

    rows: list[dict] = []
    per_view = {}
    for view in ("functional", "expense", "income", "institutional"):
        tree = bd.get(view)
        if not isinstance(tree, dict):
            per_view[view] = 0
            continue
        vr = walk_view(view, tree, years, areas, stats, bstat, extraction_date)
        rows.extend(vr)
        per_view[view] = len(vr)

    # escritura CSV largo
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)

    # JSON jerárquico
    with OUT_JSON.open("w", encoding="utf-8") as fh:
        json.dump(build_tree_json(vars_), fh, ensure_ascii=False)

    rep = validate(rows, vars_)

    # ----- informe -----
    print("=" * 70)
    print("INFORME — Extracción longitudinal Navarra (presupuesto.navarra.es)")
    print("=" * 70)
    print(f"Origen HTML            : {origen}")
    print(f"Fecha extracción       : {extraction_date}")
    print(f"Años disponibles       : {len(years)}  [{years[0]}–{years[-1]}]" if years else "Años: 0")
    print(f"Vistas presentes       : " +
          ", ".join(f"{v}={'sí' if p else 'NO/null'}" for v, p in views_present.items()))
    print(f"Filas totales (largo)  : {len(rows):,}")
    print(f"  con importe (no null): {sum(1 for r in rows if r['amount_eur'] is not None):,}")
    print("Filas por vista        :")
    for v, n in per_view.items():
        print(f"    {v:<14}: {n:,}")
    print("Metadatos longitudinales:")
    print(f"    inflación años     : {len((stats.get('inflation') or {}))}")
    print(f"    población años     : {len((stats.get('population') or {}))}")
    print(f"    budgetStatuses años: {len(bstat) if isinstance(bstat, dict) else 0}")
    print("-" * 70)
    print("VALIDACIÓN")
    print(f"  functional 2025 nivel-0 (budget): {rep['functional_2025_nivel0_eur']:,.2f} EUR")
    print(f"  esperado                        : {VALIDATION_2025_FUNCTIONAL_EUR:,.2f} EUR")
    print(f"  MATCH                           : {'OK ✔' if rep['functional_2025_match'] else 'FALLO ✘'}")
    print("  CSV oficiales:")
    fc = rep["csv_oficial"].get("functional", {})
    if fc.get("status") == "ok":
        print(f"    functional  : cotejo numérico {fc['años_coinciden']}/{fc['años_cotejados']} "
              f"años coinciden con Presupuesto Gasto del CSV")
        if fc.get("discrepancias"):
            for y, h, c in fc["discrepancias"][:5]:
                print(f"        ⚠ {y}: html={h:,.2f} vs csv={c:,.2f}")
    else:
        print(f"    functional  : {fc.get('status')}")
    for v in ("expense", "income"):
        c = rep["csv_oficial"].get(v, {})
        print(f"    {v:<12}: {c.get('status')}" +
              (f"  ({c.get('filas_csv')} filas)" if c.get("filas_csv") else ""))
    print("-" * 70)
    print("ADVERTENCIAS")
    if not views_present["institutional"]:
        print("  - vista 'institutional' = null en /es/politicas (no disponible).")
    print("  - importes JS en céntimos: divididos /100 → EUR (columna amount_eur).")
    print("  - filas con amount_eur=null preservadas (nodo sin importe ese año).")
    print(f"  - CSV largo  → {OUT_CSV.relative_to(ROOT)}")
    print(f"  - JSON árbol → {OUT_JSON.relative_to(ROOT)}")
    print("=" * 70)

    return 0 if rep["functional_2025_match"] else 1


if __name__ == "__main__":
    sys.exit(main())
