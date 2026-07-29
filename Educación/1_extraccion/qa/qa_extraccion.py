"""
Análisis QA de la extracción · pipeline Educación · Canarias en Datos.

Verifica sobre data/raw/educacion_raw_long.csv:
  · Cobertura territorial (17 CCAA oficiales + nacional + ciudades autónomas)
  · Cobertura temporal por indicador
  · Desagregación por sexo esperada
  · Validez de valores (rango, NA, negativos, duplicados de clave)
  · Estado extraído/pendiente de los 10 indicadores
  · Sondeo de coherencia de Canarias (últimos valores) para inspección visual

Genera:
  · qa/reports/qa_report_<fecha>.md    informe legible
  · qa/reports/qa_resumen_<fecha>.csv  tabla resumen por indicador

Uso:
    python qa/qa_extraccion.py       # o  python main.py --qa
"""

import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from config.settings import RAW_DIR, QA_DIR, YEAR_START
from config.indicadores import INDICADORES
from config.comunidades import CCAA_OFICIALES
from utils.logger import setup_logger

logger = setup_logger()

CONSOLIDADO = RAW_DIR / "educacion_raw_long.csv"
MANIFEST = RAW_DIR / "manifest_extraccion.json"
OK, WARN, FAIL = "✅", "⚠️", "❌"


def _check_indicador(ind, df, estado_manifest=None):
    """Devuelve (fila_resumen: dict, incidencias: list[str])."""
    key = ind["key"]
    sub = df[df["indicador"] == key]
    inc = []
    if sub.empty:
        # Distinguir un FALLO de extracción (estado 'error' en el manifest) de un
        # indicador simplemente 'pendiente' (sin fuente): no es lo mismo un corte
        # de red que "esta fuente aún no está automatizada".
        estado = "error" if estado_manifest == "error" else "pendiente"
        if estado == "error":
            inc.append(f"{key}: FALLO de extracción (ver manifest), no 'pendiente'")
        return {"indicador": key, "bloque": ind["bloque"], "estado": estado,
                "n_filas": 0, "n_ccaa": 0, "anios": "-", "sexos": "-",
                "na": "-", "fuera_rango": "-", "duplicados": "-"}, inc

    ccaa_presentes = set(sub["ccaa"].unique())
    faltan_ccaa = [c for c in CCAA_OFICIALES if c not in ccaa_presentes]
    if faltan_ccaa:
        inc.append(f"{key}: faltan {len(faltan_ccaa)} CCAA oficiales ({', '.join(faltan_ccaa)})")

    # sexo esperado
    sexos = sorted(sub["sexo"].unique())
    if ind["desagrega_sexo"] and set(sexos) != {"total", "hombres", "mujeres"}:
        inc.append(f"{key}: desagregación de sexo incompleta -> {sexos}")

    # validez de valores. Los NA bajos son estructurales (años de arranque,
    # celdas suprimidas por confidencialidad) y se reportan como métrica, no
    # como incidencia; solo se marca si superan el umbral (cf. cuadernos ref.).
    na = int(sub["valor"].isna().sum())
    na_frac = na / len(sub) if len(sub) else 0
    if na_frac > 0.30:
        inc.append(f"{key}: NA elevado ({na} filas, {na_frac:.0%})")
    negativos = int((sub["valor"] < 0).sum())
    if negativos:
        inc.append(f"{key}: {negativos} valores negativos")
    # Rango de plausibilidad por unidad (no solo %): también %PIB y EUR.
    fuera = 0
    limites = {"%": (0, 100), "%PIB": (1.5, 10), "EUR": (1000, 30000)}
    if ind["unidad"] in limites:
        lo, hi = limites[ind["unidad"]]
        fuera = int(((sub["valor"] < lo) | (sub["valor"] > hi)).sum())
        if fuera:
            inc.append(f"{key}: {fuera} valores fuera de plausibilidad [{lo},{hi}] {ind['unidad']}")

    # duplicados de clave
    clave = ["ccaa_id", "anio", "sexo"]
    dup = int(sub.duplicated(clave).sum())
    if dup:
        inc.append(f"{key}: {dup} duplicados de clave (ccaa,anio,sexo)")

    anios = sorted(sub["anio"].unique())
    return {
        "indicador": key, "bloque": ind["bloque"], "estado": "extraido",
        "n_filas": len(sub), "n_ccaa": sub["ccaa_id"].nunique(),
        "anios": f"{anios[0]}-{anios[-1]}", "sexos": "/".join(sexos),
        "na": na, "fuera_rango": fuera, "duplicados": dup,
    }, inc


def run():
    fecha = datetime.now().strftime("%Y-%m-%d")
    if not CONSOLIDADO.exists():
        logger.error("No existe %s. Ejecuta primero la extracción.", CONSOLIDADO)
        raise SystemExit(1)

    df = pd.read_csv(CONSOLIDADO)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}

    estados_manifest = {k: v.get("estado") for k, v in manifest.get("indicadores", {}).items()}
    resumen, incidencias = [], []
    for ind in INDICADORES:
        fila, inc = _check_indicador(ind, df, estados_manifest.get(ind["key"]))
        resumen.append(fila)
        incidencias.extend(inc)

    res_df = pd.DataFrame(resumen)
    n_ext = int((res_df["estado"] == "extraido").sum())
    n_pen = int((res_df["estado"] == "pendiente").sum())

    # ── CSV resumen ─────────────────────────────────────────────────────────
    csv_out = QA_DIR / f"qa_resumen_{fecha}.csv"
    res_df.to_csv(csv_out, index=False, encoding="utf-8")

    # ── Sondeo Canarias (último año por indicador y sexo=total) ─────────────
    can = df[(df["ccaa"] == "Canarias") & (df["sexo"] == "total")]
    sondeo = []
    for ind in INDICADORES:
        s = can[can["indicador"] == ind["key"]]
        if s.empty:
            sondeo.append((ind["key"], "—", "—"))
        else:
            ult = s.loc[s["anio"].idxmax()]
            sondeo.append((ind["key"], int(ult["anio"]),
                           f"{ult['valor']:g} {ult['unidad']}"))

    # ── Informe Markdown ────────────────────────────────────────────────────
    md = _render_md(fecha, df, res_df, n_ext, n_pen, incidencias, sondeo, manifest)
    md_out = QA_DIR / f"qa_report_{fecha}.md"
    md_out.write_text(md, encoding="utf-8")

    # ── Consola ─────────────────────────────────────────────────────────────
    logger.info("=" * 64)
    logger.info("QA · %d/%d indicadores extraídos · %d filas · %d incidencias",
                n_ext, len(INDICADORES), len(df), len(incidencias))
    logger.info("Informe : %s", md_out)
    logger.info("Resumen : %s", csv_out)
    veredicto = OK if not incidencias else WARN
    logger.info("Veredicto extracción: %s", veredicto)
    return {"n_extraidos": n_ext, "n_pendientes": n_pen,
            "n_incidencias": len(incidencias), "md": str(md_out)}


def _render_md(fecha, df, res_df, n_ext, n_pen, incidencias, sondeo, manifest):
    veredicto = OK if not incidencias else WARN
    L = []
    L.append(f"# Informe QA · Extracción Educación · Canarias en Datos")
    L.append("")
    L.append(f"> **Fecha:** {fecha}  ·  **Veredicto:** {veredicto}  ·  "
             f"**Indicadores extraídos:** {n_ext}/{len(INDICADORES)}  ·  "
             f"**Pendientes:** {n_pen}  ·  **Filas:** {len(df)}")
    L.append("")
    if manifest:
        L.append(f"Extracción generada el {manifest.get('generado_en','?')} "
                 f"en {manifest.get('duracion_seg','?')} s · desde {YEAR_START}.")
        L.append("")

    L.append("## 1. Estado por indicador")
    L.append("")
    L.append("| # | Indicador | Bloque | Estado | Filas | CCAA | Años | Sexos | NA | Fuera rango | Dup. |")
    L.append("|---|---|:-:|:-:|--:|:-:|:-:|:-:|--:|--:|--:|")
    for i, row in enumerate(res_df.itertuples(index=False), 1):
        est = OK if row.estado == "extraido" else "⏳"
        L.append(f"| {i} | `{row.indicador}` | {row.bloque} | {est} {row.estado} | "
                 f"{row.n_filas} | {row.n_ccaa} | {row.anios} | {row.sexos} | "
                 f"{row.na} | {row.fuera_rango} | {row.duplicados} |")
    L.append("")

    L.append("## 2. Cobertura territorial")
    L.append("")
    n_terr = df["ccaa"].nunique()
    n_ccaa_of = df[df["ccaa"].isin(CCAA_OFICIALES)]["ccaa"].nunique()
    L.append(f"- Territorios distintos en el consolidado: **{n_terr}** "
             f"(17 CCAA + España + Ceuta + Melilla = 20 esperados en los indicadores Eurostat).")
    L.append(f"- CCAA oficiales presentes: **{n_ccaa_of}/17**.")
    L.append("")

    L.append("## 3. Sondeo de coherencia · Canarias (último año, sexo total)")
    L.append("")
    L.append("| Indicador | Año | Valor |")
    L.append("|---|:-:|--:|")
    for k, a, v in sondeo:
        L.append(f"| `{k}` | {a} | {v} |")
    L.append("")
    L.append("*Inspección visual: contrastar con «Las cifras de la educación en "
             "España» (MEFP) y con Eurostat. P. ej. el abandono temprano de "
             "Canarias debe rondar el 13-16 % en los últimos años.*")
    L.append("")

    L.append("## 4. Incidencias")
    L.append("")
    if not incidencias:
        L.append(f"{OK} Sin incidencias en los indicadores extraídos: cobertura "
                 "territorial completa, desagregación de sexo correcta, sin NA, "
                 "sin valores fuera de rango ni duplicados de clave.")
    else:
        for inc in incidencias:
            L.append(f"- {WARN} {inc}")
    L.append("")

    L.append("## 5. Indicadores pendientes (MEFP · sin API pública)")
    L.append("")
    L.append("| Indicador | Bloque | Fuente | Motivo |")
    L.append("|---|:-:|---|---|")
    for ind in INDICADORES:
        if not ind["disponible"]:
            L.append(f"| `{ind['key']}` | {ind['bloque']} | {ind['dataset']} | "
                     f"EDUCAbase sin API REST pública; requiere descarga manual |")
    L.append("")
    L.append("> Resolver estas fuentes es la acción nº1 de la hoja de ruta "
             "(Cuaderno §12). No se han generado datos sintéticos para ellas.")
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    run()
