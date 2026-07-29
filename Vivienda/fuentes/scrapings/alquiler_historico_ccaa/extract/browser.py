"""
Gestión del navegador para scraping de histórico de Idealista.
Usa nodriver (sucesor de undetected-chromedriver) con flujo
Google → Idealista histórico para evitar detección de DataDome.
"""

import asyncio
import random
import re
from typing import Optional

import nodriver as uc

from config.settings import ScraperConfig
from utils.logger import setup_logger
from utils.proxy_manager import ProxyManager

logger = setup_logger("browser")


# ── Comportamiento humano ─────────────────────────────────────────────────────


async def human_type(page, element, text: str) -> None:
    """
    Escribe texto simulando un humano real:
    - Velocidad variable (más lento al inicio de palabra)
    - Errores de teclado ocasionales con corrección
    - Micro-pausas de duda
    """
    for char in text:
        # ~4% probabilidad de typo en letras
        if random.random() < 0.04 and char.isalpha():
            keyboard_neighbors = "qwertyuiop asdfghjkl zxcvbnm"
            idx = keyboard_neighbors.find(char.lower())
            # Bounds check: idx puede ser -1 (no encontrado) o estar
            # al borde del string (ej. 'q' al inicio, 'm' al final).
            if 0 < idx < len(keyboard_neighbors) - 1:
                wrong = keyboard_neighbors[idx + random.choice([-1, 1])]
                await element.send_keys(wrong)
                await asyncio.sleep(random.uniform(0.15, 0.4))
                # Pausa de "me di cuenta del error"
                await asyncio.sleep(random.uniform(0.2, 0.5))
                # Borrar con Backspace via CDP
                await _press_key(page, "Backspace", 8)
                await asyncio.sleep(random.uniform(0.08, 0.2))

        await element.send_keys(char)

        # Timing variable
        if char == " ":
            await asyncio.sleep(random.uniform(0.15, 0.45))
        elif random.random() < 0.07:
            # Micro-pausa de duda (~7%)
            await asyncio.sleep(random.uniform(0.3, 0.9))
        else:
            await asyncio.sleep(random.uniform(0.04, 0.18))


async def _press_key(page, key: str, code: int) -> None:
    """Envía un evento de teclado via CDP."""
    await page.send(uc.cdp.input_.dispatch_key_event(
        type_="keyDown", key=key, code=key,
        windows_virtual_key_code=code, native_virtual_key_code=code,
    ))
    await page.send(uc.cdp.input_.dispatch_key_event(
        type_="keyUp", key=key, code=key,
        windows_virtual_key_code=code, native_virtual_key_code=code,
    ))


async def human_scroll(page) -> None:
    """
    Simula scroll humano rápido pero irregular.
    Solo necesitamos renderizar el DOM dinámico, no simular lectura.
    """
    try:
        total_height = await page.evaluate("document.body.scrollHeight")
        current = 0

        while current < total_height:
            # Scroll rápido en bloques grandes
            if random.random() < 0.4:
                scroll_amount = random.randint(600, 1200)
            else:
                scroll_amount = random.randint(300, 600)

            current += scroll_amount
            await page.evaluate(
                f"window.scrollTo({{top: {current}, behavior: 'smooth'}})"
            )

            # Pausa breve entre scrolls
            await asyncio.sleep(random.uniform(0.1, 0.3))

            # ~8% pausa algo más larga (simula lectura puntual)
            if random.random() < 0.08:
                await asyncio.sleep(random.uniform(0.4, 1.0))

    except Exception:
        pass


# ── BrowserManager ────────────────────────────────────────────────────────────


# Plantillas de búsqueda — orientadas a sala de prensa / informe CCAA
SEARCH_TEMPLATES = [
    "idealista sala de prensa alquiler {region}",
    "idealista informe precio alquiler {region}",
    "sala de prensa idealista alquiler {region}",
    "idealista precio alquiler {region} informe",
    "informe alquiler {region} idealista sala prensa",
    "idealista alquiler {region} report",
]

# Viewports realistas (resoluciones comunes en España, 2024-2026)
VIEWPORTS = [
    (1920, 1080),  # Full HD — mayoritario
    (1366, 768),   # HD — portátiles
    (1536, 864),   # Escala 125% en Full HD
    (1440, 900),   # MacBook Air
    (1680, 1050),  # WSXGA+
    (2560, 1440),  # QHD
]


class BrowserManager:
    """
    Gestiona una instancia de Chrome con nodriver.

    Estrategia anti-detección:
    - nodriver: CDP directo sin chromedriver
    - Flujo Google → Idealista histórico: referrer orgánico
    - Typing humano con errores y correcciones
    - Scroll con patrones irregulares
    - Consultas de búsqueda variadas
    - Viewport aleatorio por sesión
    """

    def __init__(
        self,
        config: Optional[ScraperConfig] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        self.config = config or ScraperConfig()
        self.proxy_manager = proxy_manager
        self._browser = None
        self._page = None

    def _random_search_query(self, region: str) -> str:
        """Genera una consulta de búsqueda variada para parecer natural."""
        template = random.choice(SEARCH_TEMPLATES)
        # Variaciones en capitalización
        if random.random() < 0.3:
            region = region.lower()
        return template.format(region=region)

    async def start(self, max_retries: int = 3) -> None:
        """Inicia el navegador con viewport aleatorio y reintentos."""
        proxy_arg = None
        if self.proxy_manager:
            proxy_info = self.proxy_manager.get_playwright_proxy()
            if proxy_info:
                proxy_arg = f"--proxy-server={proxy_info['server']}"

        width, height = random.choice(VIEWPORTS)
        browser_args = [
            "--lang=es-ES",
            f"--window-size={width},{height}",
        ]
        if proxy_arg:
            browser_args.append(proxy_arg)

        last_error = None
        for attempt in range(1, max_retries + 1):
            try:
                self._browser = await uc.start(
                    headless=False,
                    lang="es-ES",
                    browser_args=browser_args,
                    sandbox=False,
                )
                logger.info(
                    f"Navegador iniciado (nodriver) — viewport {width}x{height}"
                )
                return
            except Exception as e:
                last_error = e
                logger.warning(
                    f"Intento {attempt}/{max_retries} fallido: {e}"
                )
                if attempt < max_retries:
                    await asyncio.sleep(2)

        logger.error(f"Error al iniciar navegador tras {max_retries} intentos: {last_error}")
        raise last_error

    async def search_and_navigate(
        self, search_query: str, slug: str = ""
    ) -> bool:
        """
        Busca en Google y navega al resultado de sala-de-prensa de la CCAA.

        Args:
            search_query: Consulta para buscar en Google.
            slug: Slug de Idealista de la CCAA (ej: "cataluna") para
                  filtrar el enlace correcto y no el genérico de España.

        Returns:
            True si se llegó a la página de histórico exitosamente.
        """
        if not self._browser:
            raise RuntimeError("Navegador no iniciado.")

        try:
            # 1. Ir a Google
            self._page = await self._browser.get("https://www.google.com")
            await asyncio.sleep(random.uniform(2, 3.5))

            # Aceptar cookies de Google
            try:
                accept = await self._page.find("Aceptar todo", timeout=4)
                if accept:
                    await asyncio.sleep(random.uniform(0.8, 1.8))
                    await accept.click()
                    await asyncio.sleep(random.uniform(0.5, 1.2))
            except Exception:
                pass

            # 2. Buscar en Google
            await asyncio.sleep(random.uniform(0.5, 1.2))
            search_box = await self._page.find(
                'textarea[name="q"]', timeout=5
            )
            if not search_box:
                search_box = await self._page.find(
                    'input[name="q"]', timeout=5
                )
            if not search_box:
                logger.warning("No se encontró el campo de búsqueda de Google")
                return False

            await search_box.click()
            await asyncio.sleep(random.uniform(0.3, 0.8))

            await human_type(self._page, search_box, search_query)
            await asyncio.sleep(random.uniform(0.5, 1.2))

            # Submit con Enter via CDP
            await _press_key(self._page, "Enter", 13)
            logger.info(f"Google search: {search_query}")
            await asyncio.sleep(random.uniform(3, 5))

            # 3. Intentar clicar resultado de Idealista sala-de-prensa (CCAA)
            link = await self._find_idealista_link(slug)
            if link:
                await link.click()
                logger.info("Click en resultado de Idealista sala-de-prensa")
                await asyncio.sleep(random.uniform(4, 7))
            else:
                # Fallback: Google no surface el enlace CCAA (URL con query
                # string, tracking, o simplemente no aparece). Navegamos
                # directamente al histórico construyendo la URL con el slug.
                #
                # Algunos slugs en comunidades.py no coinciden con los reales
                # de Idealista (p.ej. Madrid real es "madrid-comunidad"
                # para distinguirlo de la ciudad de Madrid). Probamos varios
                # candidatos hasta encontrar uno que no dé 404.
                if not slug:
                    logger.warning(
                        "No se encontró enlace en Google y no hay slug para fallback"
                    )
                    return False

                candidates = [slug, f"{slug}-comunidad"]
                reached = False
                for candidate in candidates:
                    direct_url = (
                        f"https://www.idealista.com/sala-de-prensa/"
                        f"informes-precio-vivienda/alquiler/{candidate}/historico/"
                    )
                    logger.warning(
                        f"Google no surface enlace CCAA, probando: {direct_url}"
                    )
                    try:
                        self._page = await self._browser.get(direct_url)
                        await asyncio.sleep(random.uniform(3, 5))
                        title = await self._page.evaluate("document.title") or ""
                        if "no encontrada" in title.lower() or "not found" in title.lower():
                            logger.warning(
                                f"404 en {candidate}, probando siguiente slug"
                            )
                            continue
                        reached = True
                        break
                    except Exception as e:
                        logger.error(f"Error navegando a {candidate}: {e}")
                        continue

                if not reached:
                    logger.error(
                        f"Ningún slug candidato funcionó: {candidates}"
                    )
                    return False

            # Aceptar cookies Idealista
            await self._accept_cookies()

            # 4. Navegar a la página de histórico completo
            #    La antesala solo muestra datos recientes;
            #    hay que hacer scroll y clicar "Ver datos más antiguos"
            historico_ok = await self._navigate_to_historico()
            if not historico_ok:
                logger.warning("No se pudo acceder al histórico completo")
                return False

            # Esperar a que cargue la tabla de histórico
            loaded = await self._wait_for_table()
            if not loaded:
                logger.warning("Timeout esperando tabla de histórico")
                return False

            # Validar que la URL final es a nivel CCAA y no sub-región.
            # Patrón CCAA aceptable: .../alquiler/{slug}(-comunidad|-region-de)?/historico/
            # Rechazar: .../alquiler/{slug}/{provincia}/{ciudad}/historico/
            if slug and not await self._verify_ccaa_url(slug):
                logger.error(
                    "URL final no es a nivel CCAA (contiene sub-región). "
                    "Abortando para no extraer datos de ciudad/provincia."
                )
                return False

            logger.info("Tabla de histórico cargada correctamente")
            return True

        except Exception as e:
            logger.warning(f"Error en búsqueda/navegación: {e}")
            return False

    async def _find_idealista_link(self, slug: str = ""):
        """
        Busca el enlace de Idealista sala-de-prensa de la CCAA en Google.
        Prioriza el enlace a nivel de comunidad autónoma (antesala o
        histórico), descartando URLs de provincia/municipio (más
        profundas) y el enlace genérico de España (/alquiler/report/).

        Orden de preferencia:
            1. /alquiler/{slug}/historico/   (directo al histórico CCAA)
            2. /alquiler/{slug}/             (antesala CCAA)
        """
        if slug:
            # Probar slug directo y variante "-comunidad" (usada en Madrid
            # y otras CCAA que comparten nombre con una ciudad/provincia).
            slug_candidates = [slug, f"{slug}-comunidad"]
            for candidate in slug_candidates:
                selectors = [
                    f'a[href$="/alquiler/{candidate}/historico/"]',
                    f'a[href$="/alquiler/{candidate}/historico"]',
                    f'a[href$="/alquiler/{candidate}/"]',
                    f'a[href$="/alquiler/{candidate}"]',
                ]
                for selector in selectors:
                    try:
                        link = await self._page.find(selector, timeout=2)
                        if link:
                            logger.debug(f"Enlace CCAA encontrado: {selector}")
                            return link
                    except Exception:
                        continue

        # Fallback genérico (excluye /report/ y sub-rutas de municipio)
        try:
            link = await self._page.find(
                'a[href*="idealista.com/sala-de-prensa/informes-precio-vivienda/alquiler"]:not([href*="/report"])',
                timeout=4,
            )
            if link:
                return link
        except Exception:
            pass
        return None

    async def _accept_cookies(self) -> None:
        """Acepta el banner de cookies de Didomi si está presente."""
        if not self._page:
            return
        try:
            btn = await self._page.find(
                "#didomi-notice-agree-button", timeout=4
            )
            if btn:
                await asyncio.sleep(random.uniform(0.6, 1.5))
                await btn.click()
                logger.info("Banner de cookies Didomi aceptado")
                await asyncio.sleep(random.uniform(0.4, 1.0))
        except Exception:
            pass

    async def _navigate_to_historico(self) -> bool:
        """
        Desde la antesala de sala-de-prensa, hace scroll y clica
        "Ver datos más antiguos" para llegar a la página /historico/
        con la tabla completa.

        Si la navegación desde Google ya nos dejó directamente en
        /historico/, no hacemos clic en nada: los datos completos ya
        están en la página. Clicar de nuevo en "Ver datos más antiguos"
        desde /historico/ dispara un muro de login de Idealista.
        """
        if not self._page:
            return False

        try:
            # Si ya estamos en /historico/ no navegamos más:
            # los datos definitivos ya están cargados en esta página.
            try:
                url = await self._page.evaluate("window.location.href")
                if "/historico" in (url or "").lower():
                    logger.info(f"Ya en página de histórico: {url}")
                    await human_scroll(self._page)
                    await asyncio.sleep(random.uniform(1.0, 2.0))
                    return True
            except Exception:
                pass

            # Scroll por la antesala como un usuario que lee
            await human_scroll(self._page)
            await asyncio.sleep(random.uniform(1.0, 2.0))

            # Buscar el enlace "Ver datos más antiguos" → /historico/
            selectors = [
                'a[href*="/historico/"]',
                'a[href*="historico"]',
            ]
            link = None
            for selector in selectors:
                try:
                    link = await self._page.find(selector, timeout=5)
                    if link:
                        break
                except Exception:
                    continue

            # Fallback: buscar por texto
            if not link:
                try:
                    link = await self._page.find(
                        "Ver datos más antiguos", timeout=5
                    )
                except Exception:
                    pass

            if not link:
                try:
                    link = await self._page.find(
                        "datos más antiguos", timeout=3
                    )
                except Exception:
                    pass

            if link:
                await asyncio.sleep(random.uniform(0.5, 1.5))
                await link.click()
                logger.info("Click en 'Ver datos más antiguos' → /historico/")
                await asyncio.sleep(random.uniform(4, 7))

                # Verificar que el click nos llevó al histórico y no a un login
                try:
                    url_after = await self._page.evaluate("window.location.href")
                    if "/historico" in (url_after or "").lower():
                        return True
                    if "login" in (url_after or "").lower():
                        logger.warning(
                            f"Click redirigió a login: {url_after}. "
                            "Idealista está exigiendo sesión."
                        )
                        return False
                    logger.warning(
                        f"Click no llevó a /historico/ (URL actual: {url_after})"
                    )
                    return False
                except Exception:
                    return True

            logger.warning("No se encontró enlace a histórico en la antesala")
            return False

        except Exception as e:
            logger.warning(f"Error navegando a histórico: {e}")
            return False

    async def _wait_for_table(self, max_wait: int = 40) -> bool:
        """
        Espera a que se cargue la tabla de histórico en la página.
        Busca indicadores de que el contenido dinámico se ha renderizado.

        Hace scroll progresivo durante la espera para forzar el render
        de contenido lazy-loaded (las CCAA grandes tardan más en renderizar
        la tabla completa tras una navegación directa).
        """
        html = ""
        for i in range(max_wait // 2):
            await asyncio.sleep(2)

            # Scroll progresivo cada 3 iteraciones para forzar lazy-load
            if i > 0 and i % 3 == 0:
                try:
                    await self._page.evaluate(
                        "window.scrollTo({top: document.body.scrollHeight, "
                        "behavior: 'smooth'})"
                    )
                except Exception:
                    pass

            try:
                html = await self._page.get_content()
            except Exception:
                continue

            html_lower = html.lower()

            # Si detectamos DataDome, abortar
            if "captcha-delivery" in html_lower:
                logger.warning("DataDome detectado esperando tabla")
                return False

            # Tabla con símbolo euro (€ UTF-8 o entidad HTML)
            if "<table" in html_lower and (
                "€" in html or "&euro;" in html_lower or "&#8364;" in html
            ):
                return True

            # Clase específica de tabla de evolución
            if "evolution" in html_lower and "precio" in html_lower:
                return True

            # Señal alternativa: encabezados típicos de la tabla de histórico
            if "<table" in html_lower and any(
                kw in html_lower
                for kw in ("variación mensual", "variacion mensual",
                           "variación anual", "variacion anual",
                           "€/m", "eur/m")
            ):
                return True

        # Dump de diagnóstico si timeout
        try:
            from pathlib import Path
            from datetime import datetime
            from config.settings import RAW_DIR
            debug_dir = Path(RAW_DIR).parent / "debug"
            debug_dir.mkdir(parents=True, exist_ok=True)
            url = await self._page.evaluate("window.location.href") or ""
            slug = url.rstrip("/").split("/")[-2] if url else "unknown"
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            debug_file = debug_dir / f"timeout_{slug}_{ts}.html"
            debug_file.write_text(html, encoding="utf-8")
            logger.warning(
                f"Timeout — HTML volcado en {debug_file} "
                f"(URL: {url}, size: {len(html):,} chars)"
            )
        except Exception as e:
            logger.debug(f"No se pudo volcar HTML de diagnóstico: {e}")

        return False

    async def detect_no_data(self) -> bool:
        """
        Detecta si la comunidad no tiene datos históricos disponibles.
        """
        if not self._page:
            return True
        try:
            html = await self._page.get_content()
            html_lower = html.lower()
            # Página sin tabla de datos
            if "<table" not in html_lower and "idealista" in html_lower:
                return True
            # Página de error de Idealista
            if "no corresponde a ninguna" in html_lower:
                return True
            # Página genérica sin datos de precio
            if "€" not in html and "precio" not in html_lower:
                return True
            return False
        except Exception:
            return True

    async def _verify_ccaa_url(self, slug: str) -> bool:
        """
        Verifica que la URL actual es a nivel CCAA y no una sub-región
        (provincia/ciudad). Rechaza p.ej.:
            /alquiler/madrid-comunidad/madrid-provincia/madrid/historico/
        y acepta p.ej.:
            /alquiler/madrid-comunidad/historico/
            /alquiler/euskadi/historico/
        """
        if not self._page:
            return False
        try:
            url = await self._page.evaluate("window.location.href") or ""
        except Exception:
            return True  # Si no podemos verificar, no bloqueamos

        # Extraer la parte de la ruta después de /alquiler/
        marker = "/alquiler/"
        idx = url.find(marker)
        if idx < 0:
            logger.warning(f"URL no contiene /alquiler/: {url}")
            return False
        tail = url[idx + len(marker):].rstrip("/")

        # Segmentos válidos tras el slug CCAA: vacío, "historico", "report"
        # Slugs CCAA aceptables: slug, slug-comunidad, slug-region-de
        valid_slug_variants = {slug, f"{slug}-comunidad", f"{slug}-region-de"}
        segments = tail.split("/")
        if not segments:
            return False

        first = segments[0]
        if first not in valid_slug_variants:
            logger.warning(
                f"URL slug '{first}' no coincide con variantes esperadas "
                f"{valid_slug_variants}: {url}"
            )
            return False

        # Tras el slug CCAA solo admitimos: nada, /historico, /report
        rest = segments[1:]
        if len(rest) == 0:
            return True
        if len(rest) == 1 and rest[0] in ("historico", "report"):
            return True

        logger.warning(
            f"URL contiene sub-región ({rest}) tras slug CCAA '{first}': {url}"
        )
        return False

    async def check_captcha(self) -> bool:
        """
        Detecta si se ha activado un CAPTCHA o bloqueo de DataDome.
        Solo detecta la página de bloqueo real (HTML corto con iframe de captcha-delivery).
        """
        if not self._page:
            return False
        try:
            html = await self._page.get_content()
            if len(html) < 3000 and "captcha-delivery.com" in html:
                logger.warning("Bloqueo DataDome detectado (página CAPTCHA)")
                return True
            if "access denied" in html.lower() and len(html) < 5000:
                logger.warning("Bloqueo detectado (access denied)")
                return True
            return False
        except Exception:
            return False

    async def get_page_html(self) -> Optional[str]:
        """
        Retorna el HTML de la página actual tras scroll humano.
        El scroll es necesario para renderizar el DOM dinámico.
        """
        if not self._page:
            return None

        try:
            await human_scroll(self._page)
            await asyncio.sleep(self.config.scroll_wait)
            html = await self._page.get_content()
            logger.info(f"Página obtenida: {len(html):,} chars")
            return html
        except Exception as e:
            logger.error(f"Error obteniendo HTML: {e}")
            return None

    async def navigate_back_to_google(self) -> bool:
        """
        Navega de vuelta a Google para la siguiente búsqueda.
        Simula un usuario que vuelve al buscador.
        """
        if not self._page:
            return False
        try:
            await asyncio.sleep(random.uniform(0.5, 1.5))
            await self._page.evaluate('window.location.href = "https://www.google.com"')
            await asyncio.sleep(random.uniform(2, 3.5))
            return True
        except Exception as e:
            logger.warning(f"Error volviendo a Google: {e}")
            return False

    async def stop(self) -> None:
        """Cierra el navegador."""
        if self._browser:
            try:
                self._browser.stop()
            except Exception:
                pass
            self._browser = None
            self._page = None
            logger.info("Navegador cerrado.")
