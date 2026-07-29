# -*- coding: utf-8 -*-
"""
Cliente para la API JSON del INE (sistema Tempus3 / wstempus).

Documentación oficial: https://www.ine.es/dyngs/DAB/index.htm?cid=1099
Base del servicio:      https://servicios.ine.es/wstempus/js/{idioma}/{funcion}/{input}[?parametros]

Diseño:
  - Cache en disco (JSON) para no repetir descargas y permitir ejecución offline/reproducible.
  - Reintentos con back-off ante errores transitorios (5xx, timeouts).
  - Pausa entre llamadas para no saturar el servicio (buena praxis con APIs públicas).

Este módulo pertenece a la FASE DE EXTRACCIÓN del pipeline de Empleo
(Canarias en Datos · ODESOCAN). No transforma ni calcula indicadores: sólo
descarga y cachea respuestas crudas de la API.
"""
from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE_URL = "https://servicios.ine.es/wstempus/js"
IDIOMA = "ES"
USER_AGENT = "CanariasEnDatos-Empleo/1.0 (ODESOCAN; investigacion@odesocan.org)"


class INEClient:
    """Cliente ligero y cacheado para la API JSON del INE."""

    def __init__(
        self,
        cache_dir: str | Path,
        idioma: str = IDIOMA,
        pausa_seg: float = 0.4,
        reintentos: int = 3,
        timeout: int = 60,
    ) -> None:
        self.idioma = idioma
        self.pausa_seg = pausa_seg
        self.reintentos = reintentos
        self.timeout = timeout
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Núcleo HTTP
    # ------------------------------------------------------------------ #
    def _url(self, funcion: str, path: str = "", params: dict | None = None) -> str:
        url = f"{BASE_URL}/{self.idioma}/{funcion}"
        if path:
            url += f"/{path}"
        if params:
            # ordenamos los parámetros para que la clave de cache sea estable
            url += "?" + urllib.parse.urlencode(sorted(params.items()))
        return url

    def _cache_path(self, url: str) -> Path:
        clave = urllib.parse.quote(url, safe="")
        # nombres de fichero acotados para evitar rutas demasiado largas
        if len(clave) > 180:
            clave = clave[:150] + "_" + str(abs(hash(url)))
        return self.cache_dir / f"{clave}.json"

    def get(
        self,
        funcion: str,
        path: str = "",
        params: dict | None = None,
        usar_cache: bool = True,
    ) -> Any:
        """Realiza una llamada a la API y devuelve el JSON parseado.

        Devuelve un dict con clave ``__error__`` si la descarga falla tras los
        reintentos, para que el orquestador pueda registrar el fallo sin abortar.
        """
        url = self._url(funcion, path, params)
        cache_file = self._cache_path(url)

        if usar_cache and cache_file.exists():
            with cache_file.open(encoding="utf-8") as fh:
                return json.load(fh)

        ultimo_error = None
        for intento in range(1, self.reintentos + 1):
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    datos = json.loads(resp.read().decode("utf-8", "replace"))
                if usar_cache:
                    with cache_file.open("w", encoding="utf-8") as fh:
                        json.dump(datos, fh, ensure_ascii=False)
                time.sleep(self.pausa_seg)
                return datos
            except Exception as exc:  # noqa: BLE001 (registramos y reintentamos)
                ultimo_error = f"{type(exc).__name__}: {exc}"
                time.sleep(self.pausa_seg * intento * 3)

        return {"__error__": ultimo_error, "url": url}

    # ------------------------------------------------------------------ #
    # Envoltorios de las funciones de la API usadas en la extracción
    # ------------------------------------------------------------------ #
    def operacion(self, cod: str) -> Any:
        """Metadatos de una operación estadística (p. ej. 'EPA')."""
        return self.get("OPERACION", cod)

    def tablas_operacion(self, cod_operacion: str) -> Any:
        """Listado de tablas de una operación."""
        return self.get("TABLAS_OPERACION", cod_operacion)

    def datos_tabla(
        self,
        id_tabla: str | int,
        nult: int | None = None,
        det: int = 2,
        tip: str | None = None,
    ) -> Any:
        """Descarga todas las series de una tabla.

        Parámetros:
          nult : nº de últimos periodos. Si es None se solicita la serie completa.
          det  : nivel de detalle (2 = incluye estructura de periodo y tipo de dato).
          tip  : 'A' amigable, 'M' incluye metadatos; None por defecto.
        """
        params: dict[str, Any] = {"det": det}
        if nult is not None:
            params["nult"] = nult
        if tip:
            params["tip"] = tip
        return self.get("DATOS_TABLA", str(id_tabla), params=params)
