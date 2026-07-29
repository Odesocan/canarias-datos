"""
Configuración global del pipeline ETL de histórico de alquiler por CCAA.
Rutas del proyecto, parámetros del scraper y esquema de datos.
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List

from config.comunidades import (
    COMUNIDADES_AUTONOMAS,
    buscar_comunidad,
    normalizar_nombre,
    get_slugs,
)

# ── Rutas del proyecto ──────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
LOGS_DIR = DATA_DIR / "logs"

# Ruta de exportación final dentro del módulo replicado.
EXPORT_DIR = DATA_DIR / "exports"


# ── Configuración del scraper ───────────────────────────────────────────────

@dataclass
class ScraperConfig:
    """Parámetros de configuración del scraper de histórico."""

    # Delays entre requests (segundos) — comportamiento humano
    min_delay: float = 2.0
    max_delay: float = 5.0

    # Delay extra entre comunidades para evitar patrones
    delay_entre_comunidades: float = 5.0

    # Timeout para carga de página (segundos)
    page_timeout: int = 30

    # Reintentos por comunidad fallida
    max_retries: int = 2

    # Espera tras scroll para renderizado dinámico
    scroll_wait: float = 1.5

    # Comunidades por sesión de navegador antes de rotar
    comunidades_por_sesion: int = 10

    # User agents rotativos (actualizados a 2026)
    user_agents: List[str] = field(default_factory=lambda: [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    ])

    # Headers HTTP adicionales para simular navegador real
    default_headers: Dict[str, str] = field(default_factory=lambda: {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    })


# ── Esquema de datos esperado ───────────────────────────────────────────────

CAMPOS_HISTORICO = [
    "comunidad",               # Nombre oficial de la comunidad autónoma
    "codigo_ccaa",             # Código INE de 2 dígitos
    "mes",                     # Número del mes (1-12)
    "periodo",                 # Año (ej: 2026)
    "mes_nombre",              # Nombre del mes (ej: "Marzo")
    "precio_m2",               # Precio por m² en euros
    "variacion_mensual",       # Variación mensual (%)
    "variacion_trimestral",    # Variación trimestral (%)
    "variacion_anual",         # Variación anual (%)
    "fecha_extraccion",        # Timestamp de extracción ISO 8601
]
