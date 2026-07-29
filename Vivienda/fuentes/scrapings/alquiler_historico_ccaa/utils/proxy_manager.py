"""
Gestor de proxies para rotación de IP.
Soporta lista estática de proxies o integración con servicios de proxy.
"""

import random
from typing import List, Optional, Dict

from utils.logger import setup_logger

logger = setup_logger("proxy_manager")


class ProxyManager:
    """
    Gestiona la rotación de proxies para evitar bloqueos por IP.

    Modos de uso:
    1. Sin proxies (desarrollo/testing): proxy_list vacía
    2. Lista estática: proxies propios o comprados
    3. Servicio de proxy rotativo: un único endpoint que rota automáticamente

    Para scraping profesional de Idealista, se recomienda usar proxies
    residenciales españoles para evitar geo-blocking.
    """

    def __init__(
        self,
        proxy_list: Optional[List[str]] = None,
        rotating_proxy_url: Optional[str] = None,
    ):
        self.proxy_list = proxy_list or []
        self.rotating_proxy_url = rotating_proxy_url
        self._failed_proxies: set = set()
        self._current_index = 0

        if self.proxy_list:
            logger.info(f"ProxyManager inicializado con {len(self.proxy_list)} proxies")
        elif self.rotating_proxy_url:
            logger.info("ProxyManager usando proxy rotativo")
        else:
            logger.warning(
                "ProxyManager sin proxies configurados. "
                "Se usará IP directa (riesgo de bloqueo)."
            )

    def get_proxy(self) -> Optional[Dict[str, str]]:
        """Obtiene el siguiente proxy disponible."""
        if self.rotating_proxy_url:
            return {
                "http": self.rotating_proxy_url,
                "https": self.rotating_proxy_url,
            }

        available = [p for p in self.proxy_list if p not in self._failed_proxies]

        if not available:
            if self._failed_proxies:
                logger.warning("Todos los proxies fallaron. Reseteando lista.")
                self._failed_proxies.clear()
                available = self.proxy_list
            else:
                return None

        proxy = random.choice(available)
        return {"http": proxy, "https": proxy}

    def mark_failed(self, proxy_url: str) -> None:
        """Marca un proxy como fallido temporalmente."""
        self._failed_proxies.add(proxy_url)
        logger.warning(
            f"Proxy marcado como fallido: {proxy_url[:30]}... "
            f"({len(self._failed_proxies)}/{len(self.proxy_list)} fallidos)"
        )

    def get_playwright_proxy(self) -> Optional[Dict[str, str]]:
        """Genera configuración de proxy para Playwright/nodriver."""
        proxy_dict = self.get_proxy()
        if not proxy_dict:
            return None

        proxy_url = proxy_dict.get("https") or proxy_dict.get("http")
        return {"server": proxy_url}
