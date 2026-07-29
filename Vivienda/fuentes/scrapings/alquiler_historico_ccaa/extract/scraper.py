"""
Scraper principal de histórico de alquiler de Idealista para CCAA de España.
Orquesta la extracción navegando via Google a las páginas de histórico.

Flujo de navegación (anti-detección):
1. Google → buscar "idealista precio alquiler [comunidad] historico"
2. Clic en resultado de histórico → referrer orgánico
3. Scroll para renderizar DOM dinámico → extraer tabla
4. Volver a Google → siguiente comunidad
5. Rotar sesión de navegador cada N comunidades
"""

import asyncio
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any

from config.settings import ScraperConfig, RAW_DIR
from config.comunidades import COMUNIDADES_AUTONOMAS
from extract.browser import BrowserManager, human_scroll
from extract.table_parser import HistoricoTableParser
from utils.logger import setup_logger
from utils.rate_limiter import RateLimiter
from utils.proxy_manager import ProxyManager

logger = setup_logger("scraper")


class HistoricoScraper:
    """
    Scraper de histórico de precios de alquiler de Idealista.

    Flujo por comunidad:
    1. Buscar en Google "idealista precio alquiler {comunidad} historico"
    2. Clic en primer resultado (histórico)
    3. Scroll para renderizar contenido dinámico
    4. Extraer tabla HTML con datos históricos
    5. Volver a Google para siguiente comunidad

    Rotación de sesión cada N comunidades:
    - Cierra y reabre navegador
    - Nuevo viewport, fatiga reiniciada
    """

    def __init__(
        self,
        config: Optional[ScraperConfig] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        self.config = config or ScraperConfig()
        self.proxy_manager = proxy_manager
        self.rate_limiter = RateLimiter(
            min_delay=self.config.min_delay,
            max_delay=self.config.max_delay,
            delay_entre_municipios=self.config.delay_entre_comunidades,
        )
        self.browser = None
        self._all_records: List[Dict[str, Any]] = []
        self._skipped: List[str] = []
        self._failed: List[str] = []
        self._successful: List[str] = []

    def run(
        self,
        municipios: Optional[List[Dict]] = None,
    ) -> List[Dict[str, Any]]:
        """Ejecuta la extracción completa (punto de entrada síncrono)."""
        return asyncio.run(self._run_async(municipios))

    async def _run_async(
        self,
        comunidades: Optional[List[Dict]] = None,
    ) -> List[Dict[str, Any]]:
        """Ejecuta la extracción completa de forma asíncrona."""
        comunidades = list(comunidades or COMUNIDADES_AUTONOMAS)
        random.shuffle(comunidades)
        self._all_records = []
        self._skipped = []
        self._failed = []
        self._successful = []
        total = len(comunidades)

        logger.info(
            f"Iniciando extracción de {total} comunidades | "
            f"rotación cada {self.config.comunidades_por_sesion} comunidades"
        )

        # Dividir en lotes para rotación de sesión
        batch_size = self.config.comunidades_por_sesion
        batches = [
            comunidades[i:i + batch_size]
            for i in range(0, total, batch_size)
        ]

        global_idx = 0

        try:
            for batch_num, batch in enumerate(batches, 1):
                logger.info(
                    f"=== Sesión {batch_num}/{len(batches)} "
                    f"({len(batch)} comunidades) ==="
                )

                # Pausa entre sesiones (excepto la primera)
                if batch_num > 1:
                    self.rate_limiter.wait_between_sessions()
                    self.rate_limiter.reset_session()

                # Nuevo navegador para cada sesión
                self.browser = BrowserManager(
                    config=self.config, proxy_manager=self.proxy_manager
                )
                await self.browser.start()

                try:
                    for ccaa in batch:
                        global_idx += 1
                        logger.info(
                            f"[{global_idx}/{total}] Procesando: "
                            f"{ccaa['nombre']}"
                        )

                        # Pausa entre comunidades (excepto la primera del batch)
                        if ccaa != batch[0]:
                            self.rate_limiter.wait_between_municipios()

                        records = await self._scrape_comunidad(ccaa)

                        if records is None:
                            # Error de conexión — reiniciar navegador
                            logger.warning(
                                "Conexión perdida, reiniciando navegador..."
                            )
                            await self.browser.stop()
                            await asyncio.sleep(3)
                            self.browser = BrowserManager(
                                config=self.config,
                                proxy_manager=self.proxy_manager,
                            )
                            await self.browser.start()
                            self._failed.append(ccaa["nombre"])
                            continue

                        if records:
                            self._all_records.extend(records)
                            self._successful.append(ccaa["nombre"])
                            self._save_raw(ccaa["slug_idealista"], records)
                            logger.info(
                                f"  -> {len(records)} registros extraídos "
                                f"de {ccaa['nombre']}"
                            )
                        else:
                            logger.info(
                                f"  -> Sin datos para {ccaa['nombre']}"
                            )

                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    logger.error(
                        f"Error en sesión {batch_num}: {e}", exc_info=True
                    )
                finally:
                    await self.browser.stop()

        except KeyboardInterrupt:
            logger.warning("Extracción interrumpida por el usuario")
        except Exception as e:
            logger.error(f"Error fatal en extracción: {e}", exc_info=True)

        # Guardar dataset consolidado
        self._save_consolidated()

        logger.info(
            f"Extracción completada: {len(self._all_records)} registros "
            f"totales | {len(self._successful)} comunidades con datos | "
            f"{len(self._skipped)} sin datos | {len(self._failed)} fallidas"
        )

        return self._all_records

    async def _scrape_comunidad(
        self, ccaa: Dict
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Scrapea una comunidad: buscar en Google → extraer tabla.
        Maneja captchas, páginas sin datos y errores.

        Returns:
            Lista de registros, [] si no hay datos, None si error de conexión.
        """
        nombre = ccaa["nombre"]
        slug = ccaa["slug_idealista"]
        # Usar nombre_busqueda si existe (desambigua ciudad vs CCAA en Google)
        nombre_query = ccaa.get("nombre_busqueda", nombre)
        query = self.browser._random_search_query(nombre_query)

        try:
            # Buscar en Google y navegar al resultado
            if not await self.browser.search_and_navigate(query, slug):
                # Verificar si fue un CAPTCHA
                if await self.browser.check_captcha():
                    logger.error(
                        f"  CAPTCHA detectado para {nombre}. "
                        "Saltando a la siguiente comunidad."
                    )
                    self._failed.append(nombre)
                    await self.browser.navigate_back_to_google()
                    return []

                # No se encontró resultado en Google
                self._skipped.append(nombre)
                return []

            # Verificar si hay datos disponibles
            if await self.browser.detect_no_data():
                logger.info(f"  Comunidad sin datos históricos: {nombre}")
                self._skipped.append(nombre)
                await self.browser.navigate_back_to_google()
                return []

            # Verificar captcha antes de extraer
            if await self.browser.check_captcha():
                logger.error(f"  CAPTCHA detectado tras cargar {nombre}")
                self._failed.append(nombre)
                await self.browser.navigate_back_to_google()
                return []

            # Obtener HTML con scroll para renderizar DOM
            html = await self.browser.get_page_html()
            if not html:
                logger.warning(f"  No se pudo obtener HTML de {nombre}")
                self._failed.append(nombre)
                await self.browser.navigate_back_to_google()
                return []

            # Parsear tabla
            parser = HistoricoTableParser(html, ccaa)
            records = parser.parse_table()

            if not records:
                self._skipped.append(nombre)

            # Volver a Google para siguiente búsqueda
            await self.browser.navigate_back_to_google()

            return records

        except Exception as e:
            err = str(e).lower()
            if "websocket" in err or "connection" in err or "500" in err:
                logger.error(f"  Error de conexión en {nombre}: {e}")
                return None
            logger.warning(f"  Error scrapeando {nombre}: {e}")
            self._failed.append(nombre)
            return []

    def _save_raw(self, slug: str, records: List[Dict[str, Any]]) -> None:
        """Guarda datos crudos de una comunidad en JSON."""
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = RAW_DIR / f"{slug}_{timestamp}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "comunidad": slug,
                    "fecha_extraccion": datetime.now(timezone.utc).isoformat(),
                    "total_registros": len(records),
                    "registros": records,
                },
                f,
                ensure_ascii=False,
                indent=2,
            )

        logger.debug(f"  Datos crudos guardados: {filepath}")

    def _save_consolidated(self) -> None:
        """Guarda el dataset consolidado de todas las comunidades."""
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = RAW_DIR / f"consolidado_{timestamp}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "fecha_extraccion": datetime.now(timezone.utc).isoformat(),
                    "total_registros": len(self._all_records),
                    "comunidades_con_datos": len(self._successful),
                    "comunidades_sin_datos": self._skipped,
                    "comunidades_fallidas": self._failed,
                    "registros": self._all_records,
                },
                f,
                ensure_ascii=False,
                indent=2,
            )

        logger.info(f"Dataset consolidado guardado: {filepath}")
