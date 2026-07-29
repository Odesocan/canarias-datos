"""
Orquestador principal del pipeline ETL de histórico de alquiler por CCAA de España.
Coordina extracción, transformación y carga de datos de precios históricos.

Uso:
    python main.py                          # Pipeline completo
    python main.py --stage extract          # Solo extracción
    python main.py --stage transform        # Solo transformación (requiere datos crudos)
    python main.py --stage load             # Solo carga (requiere datos procesados)
    python main.py --no-supabase            # Solo exportar CSV, sin cargar a Supabase
    python main.py --ccaa Madrid Cataluña   # Comunidades específicas
    python main.py --proxy-file proxies.txt # Usar lista de proxies
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# Añadir el directorio raíz al path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config.settings import (
    ScraperConfig,
    RAW_DIR,
    PROCESSED_DIR,
    EXPORT_DIR,
)
from config.comunidades import (
    COMUNIDADES_AUTONOMAS,
    buscar_comunidad,
)
from extract.scraper import HistoricoScraper
from transform.cleaner import HistoricoCleaner
from transform.validator import HistoricoValidator
from load.csv_exporter import CSVExporter
from load.supabase_loader import SupabaseLoader
from utils.logger import setup_logger
from utils.proxy_manager import ProxyManager

logger = setup_logger("main")


def parse_args() -> argparse.Namespace:
    """Parsea argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="ETL Pipeline: Histórico de Alquiler por CCAA (Idealista)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--stage",
        choices=["extract", "transform", "load", "all"],
        default="all",
        help="Etapa del pipeline a ejecutar (default: all)",
    )
    parser.add_argument(
        "--no-supabase",
        action="store_true",
        default=False,
        help="No cargar a Supabase, solo exportar CSV",
    )
    parser.add_argument(
        "--input-file",
        type=str,
        default=None,
        help="Archivo JSON de entrada para transform/load (omite extracción)",
    )
    parser.add_argument(
        "--proxy-file",
        type=str,
        default=None,
        help="Archivo con lista de proxies (uno por línea)",
    )
    parser.add_argument(
        "--ccaa",
        type=str,
        nargs="+",
        default=None,
        help="Nombres o slugs de comunidades autónomas específicas a scrapear",
    )
    return parser.parse_args()


def load_proxies(proxy_file: Optional[str]) -> ProxyManager:
    """Carga proxies desde archivo."""
    if not proxy_file:
        return ProxyManager()

    path = Path(proxy_file)
    if not path.exists():
        logger.warning(f"Archivo de proxies no encontrado: {proxy_file}")
        return ProxyManager()

    proxies = [
        line.strip()
        for line in path.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    logger.info(f"Cargados {len(proxies)} proxies desde {proxy_file}")
    return ProxyManager(proxy_list=proxies)


def filter_comunidades(
    slugs: Optional[List[str]] = None,
) -> List[Dict[str, str]]:
    """
    Filtra comunidades por slug/nombre o devuelve la lista completa.
    Búsqueda flexible: acepta slugs, nombres oficiales, aliases.
    """
    result = list(COMUNIDADES_AUTONOMAS)

    if slugs:
        filtered = []
        for query in slugs:
            c = buscar_comunidad(query)
            if c:
                filtered.append(c)
            else:
                logger.warning(f"Comunidad no reconocida: '{query}'")

        if not filtered:
            logger.error(f"Ninguna comunidad coincide con: {slugs}")
            sys.exit(1)

        result = filtered
        logger.info(
            f"Filtrado por: {', '.join(slugs)} "
            f"→ {len(result)} comunidades"
        )

    return result


def load_raw_data(input_file: Optional[str] = None) -> List[Dict[str, Any]]:
    """Carga datos crudos desde archivo o el más reciente."""
    if input_file:
        path = Path(input_file)
    else:
        raw_files = sorted(RAW_DIR.glob("consolidado_*.json"), reverse=True)
        if not raw_files:
            logger.error(
                "No se encontraron datos crudos. "
                "Ejecutar primero --stage extract"
            )
            sys.exit(1)
        path = raw_files[0]

    logger.info(f"Cargando datos crudos: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data.get("registros", data if isinstance(data, list) else [])
    logger.info(f"Cargados {len(records)} registros crudos")
    return records


# ── Etapas del pipeline ─────────────────────────────────────────────────────


def stage_extract(args: argparse.Namespace) -> List[Dict[str, Any]]:
    """Etapa de extracción: scraping de Idealista histórico."""
    logger.info("=" * 60)
    logger.info("ETAPA 1: EXTRACCIÓN")
    logger.info("=" * 60)

    config = ScraperConfig()
    proxy_manager = load_proxies(args.proxy_file)
    comunidades = filter_comunidades(slugs=args.ccaa)

    scraper = HistoricoScraper(
        config=config,
        proxy_manager=proxy_manager,
    )

    records = scraper.run(municipios=comunidades)
    return records


def stage_transform(
    records: List[Dict[str, Any]],
) -> "pd.DataFrame":
    """Etapa de transformación: limpieza y validación."""
    import pandas as pd

    logger.info("=" * 60)
    logger.info("ETAPA 2: TRANSFORMACIÓN")
    logger.info("=" * 60)

    # Paso 1: Limpieza
    cleaner = HistoricoCleaner()
    df = cleaner.clean(records)

    # Paso 2: Validación de calidad
    validator = HistoricoValidator()
    quality_report = validator.validate(df)

    return df


def stage_load(
    df: "pd.DataFrame",
    skip_supabase: bool = False,
) -> None:
    """Etapa de carga: CSV + Supabase."""
    logger.info("=" * 60)
    logger.info("ETAPA 3: CARGA")
    logger.info("=" * 60)

    # Siempre exportar CSV
    csv_exporter = CSVExporter()
    paths = csv_exporter.export(df, output_dir=EXPORT_DIR)

    for name, path in paths.items():
        logger.info(f"  {name}: {path}")

    # Cargar a Supabase (opcional)
    if not skip_supabase:
        try:
            loader = SupabaseLoader()
            loader.print_create_table_sql()
            loader.connect()
            stats = loader.load(df)
            logger.info(f"Carga Supabase: {stats}")
        except Exception as e:
            logger.error(
                f"Error en carga a Supabase: {e}. "
                "Los CSV se generaron correctamente."
            )
    else:
        logger.info("Carga a Supabase omitida (--no-supabase)")


# ── Punto de entrada ─────────────────────────────────────────────────────────


def main():
    """Ejecuta el pipeline ETL."""
    args = parse_args()
    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("PIPELINE ETL: HISTORICO ALQUILER CCAA ESPAÑA")
    logger.info(f"Inicio: {start_time.isoformat()}")
    logger.info(f"Etapa: {args.stage}")
    logger.info("=" * 60)

    try:
        if args.stage in ("extract", "all"):
            records = stage_extract(args)
        else:
            records = load_raw_data(args.input_file)

        if args.stage in ("transform", "all"):
            df = stage_transform(records)
        else:
            import pandas as pd
            csv_files = sorted(
                PROCESSED_DIR.glob("alquiler_historico_ccaa_*.csv"),
                reverse=True,
            )
            if csv_files:
                df = pd.read_csv(csv_files[0])
            else:
                df = stage_transform(records)

        if args.stage in ("load", "all"):
            stage_load(df, skip_supabase=args.no_supabase)

    except KeyboardInterrupt:
        logger.warning("Pipeline interrumpido por el usuario")
    except Exception as e:
        logger.error(f"Error en pipeline: {e}", exc_info=True)
        sys.exit(1)

    elapsed = datetime.now() - start_time
    logger.info(f"Pipeline completado en {elapsed}")


if __name__ == "__main__":
    main()
