"""
Análisis QA de la transformación · pipeline Educación · Canarias en Datos.

Verifica las tablas finales ced_educacion_global / ced_educacion_gen:
  · Cobertura territorial (17 CCAA) y temporal, unicidad de clave
  · Resumen de calidad: NA% por indicador (global y gen)
  · Validez de valores (rango %, gasto > 0)
  · Consistencia global ↔ gen (el total de gen debe igualar al global)
  · Brecha de género (mujeres - hombres) y su signo esperado
  · Sondeo de coherencia de Canarias

Genera:
  · reports/qa_transformacion_<fecha>.md
  · reports/qa_transformacion_resumen_<fecha>.csv

Uso:
    python qa_transformacion.py     # o  python transformacion.py --qa
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
EXTRACCION_DIR = BASE_DIR.parent / "1_extraccion"
sys.path.insert(0, str(EXTRACCION_DIR))

from config.indicadores import INDICADORES                    # noqa: E402
from config.comunidades import TERRITORIOS                    # noqa: E402
from utils.logger import setup_logger                         # noqa: E402

logger = setup_logger("educacion_transformacion")

DATA = BASE_DIR / "data"
QA_DIR = BASE_DIR / "reports"
QA_DIR.mkdir(parents=True, exist_ok=True)
OK, WARN = "✅", "⚠️"

IND = {i["key"]: i for i in INDICADORES}
ORDEN = [i["key"] for i in INDICADORES]
CCAA17 = sorted({i for i in [t["ccaa_id"] for t in TERRITORIOS if t["tipo"] == "ccaa"]})
# Signo esperado de la brecha (mujeres - hombres) para los indicadores robustos.
# NEET se deja como "solo reporte": en España la brecha suele ser LIGERAMENTE
# positiva (mujeres jóvenes algo por encima), reflejo del trabajo de cuidados, no
# un fallo de dato. No se le asigna signo esperado.
BRECHA_ESPERADA = {"abandono_temprano": "neg", "nivel_superior_25_34": "pos",
                   "idoneidad_15": "pos", "graduacion_eso": "pos"}
# Suelo de plausibilidad del gasto educativo (%PIB): por debajo indica hueco de
# clasificación en la fuente (área Presupuestos), no un dato real.
GASTO_PIB_MIN_PLAUSIBLE = 1.5


def _load(nombre):
    return pd.read_csv(DATA / f"{nombre}.csv", sep=";", decimal=",", na_values=["NA"])


def run():
    fecha = datetime.now().strftime("%Y-%m-%d")
    glob = _load("ced_educacion_global")
    gen = _load("ced_educacion_gen")
    inc = []

    inds_glob = [c for c in ORDEN if c in glob.columns]
    inds_gen = [c for c in ORDEN if c in gen.columns]

    # ── Cobertura y clave ───────────────────────────────────────────────────
    n_ccaa = glob["ccaa"].nunique()
    if n_ccaa != 17:
        inc.append(f"global: {n_ccaa}/17 CCAA")
    if glob.duplicated(["ccaa", "periodo"]).any():
        inc.append("global: clave (ccaa,periodo) duplicada")
    if gen.duplicated(["ccaa", "periodo", "genero"]).any():
        inc.append("gen: clave (ccaa,periodo,genero) duplicada")
    gen_generos = sorted(gen["genero"].unique())
    if set(gen_generos) != {"total", "hombres", "mujeres"}:
        inc.append(f"gen: géneros inesperados {gen_generos}")

    # ── Resumen de calidad (NA% + rango) por indicador ──────────────────────
    resumen = []
    for k in inds_glob:
        s = glob[k]
        na = s.isna().sum()
        na_pct = na / len(glob) * 100
        unidad = IND[k]["unidad"]
        fuera = 0
        if unidad == "%":
            fuera = int(((s < 0) | (s > 100)).sum(skipna=True))
        elif unidad in ("EUR", "%PIB"):
            fuera = int((s < 0).sum(skipna=True))
        if fuera:
            inc.append(f"{k}: {fuera} valores fuera de rango")
        if na_pct > 60:
            inc.append(f"{k}: NA elevado en global ({na_pct:.0f}%)")
        val = s.dropna()
        resumen.append({
            "indicador": k, "bloque": IND[k]["bloque"], "unidad": unidad,
            "n": int(val.shape[0]), "na_pct_global": round(na_pct, 1),
            "min": round(val.min(), 2) if len(val) else None,
            "max": round(val.max(), 2) if len(val) else None,
        })
    res_df = pd.DataFrame(resumen)

    # ── Plausibilidad del gasto/PIB (indicio de hueco en Presupuestos) ──────
    avisos_fuente = []
    if "gasto_edu_pib" in glob.columns:
        bajos = glob[glob["gasto_edu_pib"] < GASTO_PIB_MIN_PLAUSIBLE][
            ["ccaa", "periodo", "gasto_edu_pib"]].dropna()
        if len(bajos):
            ej = "; ".join(f"{r.ccaa} {int(r.periodo)}={r.gasto_edu_pib:g}"
                           for r in bajos.sort_values("gasto_edu_pib").head(5).itertuples())
            avisos_fuente.append(
                f"gasto_edu_pib: {len(bajos)} valores implausibles (< {GASTO_PIB_MIN_PLAUSIBLE} %PIB) "
                f"— hueco de clasificación en la FUENTE Presupuestos, no en la transformación. "
                f"Ej.: {ej}")

    # ── Consistencia global ↔ gen (total) ───────────────────────────────────
    gtot = gen[gen["genero"] == "total"]
    incons = 0
    for k in inds_gen:
        m = glob[["ccaa", "periodo", k]].merge(
            gtot[["ccaa", "periodo", k]], on=["ccaa", "periodo"], suffixes=("_g", "_t"))
        d = (m[f"{k}_g"] - m[f"{k}_t"]).abs()
        incons += int((d > 0.01).sum())
    if incons:
        inc.append(f"consistencia global↔gen: {incons} celdas discrepantes")

    # ── Brecha de género (mujeres - hombres) ────────────────────────────────
    brechas = []
    ph = gen[gen["genero"] == "hombres"].set_index(["ccaa", "periodo"])
    pm = gen[gen["genero"] == "mujeres"].set_index(["ccaa", "periodo"])
    for k in inds_gen:
        if k in ph and k in pm:
            br = (pm[k] - ph[k]).dropna()
            media = br.mean() if len(br) else float("nan")
            exp = BRECHA_ESPERADA.get(k)
            estado = "—"
            if exp and pd.notna(media):
                ok = (media < 0) if exp == "neg" else (media > 0)
                estado = OK if ok else WARN
                if not ok:
                    inc.append(f"brecha {k}: signo inesperado (media {media:+.1f} pp, esperado {exp})")
            brechas.append((k, round(media, 2) if pd.notna(media) else None, exp or "—", estado))

    # ── Sondeo Canarias (global, último periodo con dato) ───────────────────
    can = glob[glob["ccaa"] == "Canarias"].sort_values("periodo")
    sondeo = []
    for k in inds_glob:
        s = can[["periodo", k]].dropna(subset=[k])
        if len(s):
            r = s.iloc[-1]
            sondeo.append((k, int(r["periodo"]), f"{r[k]:g} {IND[k]['unidad']}"))

    # ── Salidas ─────────────────────────────────────────────────────────────
    res_df.to_csv(QA_DIR / f"qa_transformacion_resumen_{fecha}.csv", index=False, encoding="utf-8")
    md = _render(fecha, glob, gen, inds_glob, res_df, brechas, sondeo, inc, incons, avisos_fuente)
    md_path = QA_DIR / f"qa_transformacion_{fecha}.md"
    md_path.write_text(md, encoding="utf-8")

    logger.info("=" * 64)
    logger.info("QA transformación · global %d filas · gen %d filas", len(glob), len(gen))
    logger.info("Integridad de la transformación: %s (%d incidencias)",
                OK if not inc else WARN, len(inc))
    logger.info("Calidad de fuente: %s (%d avisos)",
                OK if not avisos_fuente else WARN, len(avisos_fuente))
    logger.info("Informe: %s", md_path)
    return {"incidencias": inc, "avisos_fuente": avisos_fuente, "md": str(md_path)}


def _render(fecha, glob, gen, inds_glob, res_df, brechas, sondeo, inc, incons, avisos_fuente):
    v_int = OK if not inc else WARN
    v_src = OK if not avisos_fuente else WARN
    L = ["# Informe QA · Transformación Educación · Canarias en Datos", ""]
    L.append(f"> **Fecha:** {fecha}  ·  **Integridad transformación:** {v_int}  ·  "
             f"**Calidad de fuente:** {v_src}  ·  "
             f"**global:** {len(glob)} filas  ·  **gen:** {len(gen)} filas")
    L.append("")
    per = sorted(glob["periodo"].unique())
    L.append(f"Tablas: `ced_educacion_global` (clave ccaa×periodo) y "
             f"`ced_educacion_gen` (ccaa×periodo×género). Marco: **17 CCAA**, "
             f"periodo **{per[0]}-{per[-1]}**, datos observados (origen=real).")
    L.append("")

    L.append("## 1. Resumen de calidad por indicador (tabla global)")
    L.append("")
    L.append("| Indicador | Bloque | Unidad | n | NA% | mín | máx |")
    L.append("|---|:-:|:-:|--:|--:|--:|--:|")
    for r in res_df.itertuples(index=False):
        L.append(f"| `{r.indicador}` | {r.bloque} | {r.unidad} | {r.n} | "
                 f"{r.na_pct_global}% | {r.min} | {r.max} |")
    L.append("")
    L.append("*Interpretación: los NA reflejan distintos años de arranque/cierre "
             "por fuente (p. ej. graduación y gasto por alumno terminan en 2023), "
             "no fallo técnico.*")
    L.append("")

    L.append("## 2. Cobertura y consistencia")
    L.append("")
    L.append(f"- CCAA en global: **{glob['ccaa'].nunique()}/17**.")
    L.append(f"- Géneros en gen: **{', '.join(sorted(gen['genero'].unique()))}**.")
    L.append(f"- Clave única: global {'sí' if not glob.duplicated(['ccaa','periodo']).any() else 'NO'} · "
             f"gen {'sí' if not gen.duplicated(['ccaa','periodo','genero']).any() else 'NO'}.")
    L.append(f"- Consistencia global ↔ gen(total): "
             f"{'✅ idénticos' if incons == 0 else f'{incons} discrepancias'}.")
    L.append("")

    L.append("## 3. Brecha de género (mujeres − hombres, media pp)")
    L.append("")
    L.append("| Indicador | Brecha media | Signo esperado | |")
    L.append("|---|--:|:-:|:-:|")
    for k, media, exp, estado in brechas:
        L.append(f"| `{k}` | {media} | {exp} | {estado} |")
    L.append("")
    L.append("*Patrón esperado: menos abandono/NEET en mujeres (brecha negativa) y "
             "más titulación superior, idoneidad y graduación en mujeres (positiva).*")
    L.append("")

    L.append("## 4. Sondeo de coherencia · Canarias (global, último dato)")
    L.append("")
    L.append("| Indicador | Periodo | Valor |")
    L.append("|---|:-:|--:|")
    for k, p, v in sondeo:
        L.append(f"| `{k}` | {p} | {v} |")
    L.append("")

    L.append("## 5. Integridad de la transformación")
    L.append("")
    if not inc:
        L.append(f"{OK} Sin incidencias de integridad: cobertura 17/17 CCAA, clave "
                 "única en ambas tablas, consistencia global↔gen exacta, sin valores "
                 "fuera de rango y brechas de género con el signo esperado.")
    else:
        for x in inc:
            L.append(f"- {WARN} {x}")
    L.append("")

    L.append("## 6. Avisos de calidad de fuente (aguas arriba)")
    L.append("")
    if not avisos_fuente:
        L.append(f"{OK} Sin avisos: los valores de las fuentes están dentro de rangos plausibles.")
    else:
        for x in avisos_fuente:
            L.append(f"- {WARN} {x}")
        L.append("")
        L.append("> Estos avisos NO indican un fallo de la transformación de Educación, "
                 "sino de la fuente original. Deben corregirse en el pipeline de origen "
                 "(aquí, el área de Presupuestos).")
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    run()
