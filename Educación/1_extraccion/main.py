"""
Orquestador de la ETAPA DE EXTRACCIÓN del pipeline de Educación · Canarias en Datos.

Extrae todos los indicadores del dashboard (Cuaderno §4) desde sus fuentes:
  · Eurostat (5 indicadores de población, EPA regional, CCAA × sexo)
  · Presupuestos (gasto/PIB regional, enlace inter-área)
  · MEFP (4 indicadores de sistema — pendientes de fuente automatizable)

Salidas en data/raw/:
  · <indicador>.csv           una tabla por indicador extraído
  · educacion_raw_long.csv    consolidado en formato largo (tidy)
  · manifest_extraccion.json  estado por indicador (extraído / pendiente)

Uso:
    python main.py                     # extracción completa
    python main.py --source eurostat   # solo una fuente (eurostat|presupuestos|mefp)
    python main.py --qa                # extrae y ejecuta el análisis QA a continuación
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pandas as pd

from config.settings import RAW_DIR, SCHEMA, YEAR_START
from config.indicadores import INDICADORES, DISPONIBLES
from extract.eurostat_edu import extraer_indicador
from extract import educabase, mefp
from extract.presupuestos import extraer_gasto_pib
from extract import cifras_educacion
from utils.logger import setup_logger

logger = setup_logger()

CONSOLIDADO = RAW_DIR / "educacion_raw_long.csv"
MANIFEST = RAW_DIR / "manifest_extraccion.json"


def _guardar_indicador(key: str, filas: list) -> None:
    if not filas:
        return
    df = pd.DataFrame(filas, columns=SCHEMA)
    # Orden determinista (independiente del orden de respuesta de la fuente)
    df = df.sort_values([c for c in ("ccaa_id", "anio", "sexo") if c in df.columns])
    out = RAW_DIR / f"{key}.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    logger.info("  -> %s (%d filas)", out.name, len(df))


def ejecutar(source: str = "all") -> dict:
    inicio = datetime.now()
    todas = []
    estado = {}   # key -> ficha de estado

    # ── Eurostat (5 indicadores de población) ───────────────────────────────
    if source in ("all", "eurostat"):
        for ind in DISPONIBLES:
            if ind["fuente"] != "eurostat":
                continue
            try:
                filas = extraer_indicador(ind)
                _guardar_indicador(ind["key"], filas)
                todas.extend(filas)
                estado[ind["key"]] = _ficha(ind, filas)
            except Exception as e:  # noqa: BLE001
                logger.error("FALLO en %s: %s", ind["key"], e)
                estado[ind["key"]] = _ficha(ind, [], error=str(e))

    # ── EDUCAbase / MEFP (indicadores de sistema, PC-Axis csv_bd) ────────────
    if source in ("all", "educabase", "mefp"):
        for ind in DISPONIBLES:
            if ind["fuente"] != "educabase":
                continue
            try:
                filas = educabase.extraer(ind["key"], ind["bloque"])
                _guardar_indicador(ind["key"], filas)
                todas.extend(filas)
                estado[ind["key"]] = _ficha(ind, filas)
            except Exception as e:  # noqa: BLE001
                logger.error("FALLO en %s: %s", ind["key"], e)
                estado[ind["key"]] = _ficha(ind, [], error=str(e))

    # ── Presupuestos ────────────────────────────────────────────────────────
    if source in ("all", "presupuestos"):
        ind = next(i for i in INDICADORES if i["key"] == "gasto_edu_pib")
        try:
            filas = extraer_gasto_pib()
            _guardar_indicador(ind["key"], filas)
            todas.extend(filas)
            estado[ind["key"]] = _ficha(ind, filas)
        except Exception as e:  # noqa: BLE001
            logger.error("FALLO en gasto_edu_pib: %s", e)
            estado[ind["key"]] = _ficha(ind, [], error=str(e))

    # ── Cifras de la Educación (gasto por alumno · Excel B4.6) ───────────────
    if source in ("all", "cifras"):
        ind = next(i for i in INDICADORES if i["key"] == "gasto_por_alumno")
        try:
            filas = cifras_educacion.extraer()
            _guardar_indicador(ind["key"], filas)
            todas.extend(filas)
            estado[ind["key"]] = _ficha(ind, filas)
        except Exception as e:  # noqa: BLE001
            logger.error("FALLO en gasto_por_alumno: %s", e)
            estado[ind["key"]] = _ficha(ind, [], error=str(e))

    # ── Pendientes (sin fuente automatizable a día de hoy) ──────────────────
    if source in ("all", "educabase", "mefp"):
        for ficha in mefp.estado_pendientes():
            estado[ficha["indicador"]] = {
                "indicador": ficha["indicador"], "bloque": ficha["bloque"],
                "fuente": ficha["fuente"], "estado": "pendiente",
                "motivo": ficha["motivo"], "fuente_url": ficha["fuente_url"],
                "n_filas": 0,
            }

    # ── Consolidado + manifest (solo en ejecución completa) ─────────────────
    if source == "all":
        df = pd.DataFrame(todas, columns=SCHEMA)
        df.sort_values(["indicador", "ccaa_id", "anio", "sexo"], inplace=True)
        df.to_csv(CONSOLIDADO, index=False, encoding="utf-8")
        logger.info("Consolidado: %s (%d filas)", CONSOLIDADO.name, len(df))

        manifest = {
            "generado_en": inicio.isoformat(timespec="seconds"),
            "duracion_seg": round((datetime.now() - inicio).total_seconds(), 1),
            "year_start": YEAR_START,
            "n_indicadores_total": len(INDICADORES),
            "n_indicadores_extraidos": sum(1 for v in estado.values()
                                           if v.get("estado") == "extraido"),
            "n_indicadores_pendientes": sum(1 for v in estado.values()
                                            if v.get("estado") == "pendiente"),
            "n_filas_total": len(df),
            "indicadores": estado,
        }
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        logger.info("Manifest: %s", MANIFEST.name)
        return manifest

    return {"indicadores": estado}


def _ficha(ind: dict, filas: list, error: str = None) -> dict:
    if error:
        return {"indicador": ind["key"], "bloque": ind["bloque"],
                "fuente": ind["fuente"], "estado": "error",
                "motivo": error, "n_filas": 0}
    anios = sorted({f["anio"] for f in filas})
    return {
        "indicador": ind["key"], "bloque": ind["bloque"], "fuente": ind["fuente"],
        "dataset": ind["dataset"], "estado": "extraido",
        "n_filas": len(filas),
        "n_ccaa": len({f["ccaa_id"] for f in filas}),
        "anios": f"{anios[0]}-{anios[-1]}" if anios else None,
        "sexos": sorted({f["sexo"] for f in filas}),
    }


def parse_args():
    p = argparse.ArgumentParser(description="Extracción · pipeline Educación (Canarias en Datos)")
    p.add_argument("--source",
                   choices=["all", "eurostat", "educabase", "presupuestos", "cifras", "mefp"],
                   default="all", help="Fuente a extraer (default: all)")
    p.add_argument("--qa", action="store_true",
                   help="Ejecutar el análisis QA tras la extracción")
    return p.parse_args()


def main():
    args = parse_args()
    logger.info("=" * 64)
    logger.info("EXTRACCIÓN · Educación · fuente=%s · desde %d", args.source, YEAR_START)
    logger.info("=" * 64)

    manifest = ejecutar(args.source)

    if args.source == "all":
        ext = manifest["n_indicadores_extraidos"]
        pen = manifest["n_indicadores_pendientes"]
        logger.info("-" * 64)
        logger.info("RESUMEN: %d indicadores extraídos, %d pendientes, %d filas",
                    ext, pen, manifest["n_filas_total"])

    if args.qa:
        logger.info("Lanzando análisis QA...")
        from qa import qa_extraccion
        qa_extraccion.run()


if __name__ == "__main__":
    main()
