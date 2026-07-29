"""
ccaa/_common/transform_helpers.py — Utilidades comunes para los transform.py
locales de cada CCAA.

Patrón de uso en `ccaa/<id3>/transform.py`:

    from .._common.transform_helpers import asignar_concepto_local

    def transform(rows, anio):
        return asignar_concepto_local(rows, mapping_path=__file__)
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Iterable

import yaml


def _norm_codigo(s: str) -> str:
    return (s or "").strip().upper()


def _norm_text(s: str) -> str:
    # 2026-06-05: el docstring de asignar_concepto_local promete matching
    # "lower, sin acentos", pero la implementación no quitaba diacríticos:
    # "INMIGRACIÓN" no matcheaba la keyword "migracion". Se normaliza NFKD
    # y se eliminan marcas combinantes; afecta por igual a keywords y a
    # denominaciones (simétrico), nunca pisa conceptos ya asignados.
    s = (s or "").lower().strip()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", s)


def _load_correspondencias(mapping_path: str | Path) -> dict:
    """Carga `correspondencias.yml` adyacente a un módulo CCAA."""
    if isinstance(mapping_path, str) and mapping_path.endswith(".py"):
        mapping_path = Path(mapping_path).parent / "correspondencias.yml"
    p = Path(mapping_path)
    if not p.exists():
        return {"conceptos": {}}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def asignar_concepto_local(rows: Iterable[dict], mapping_path: str | Path) -> list[dict]:
    """Asigna `concepto` a cada fila usando la tabla CCAA-específica.

    El YAML tiene la forma:
        conceptos:
          sanidad:
            codigos: ["41A","41B","41C","41D"]
            keywords: ["sanidad","salud"]
          educacion:
            codigos: ["42A","42B"]
          ...

    La búsqueda es:
      1. match exacto del código (longitud completa)
      2. match por prefijo de código (si el YAML lo permite explícitamente)
      3. match por keyword en la denominación (lower, sin acentos)
    """
    corr = _load_correspondencias(mapping_path)
    conceptos = (corr.get("conceptos") or {})

    # Pre-construye índices
    code_exact: dict[str, str] = {}
    code_prefix: list[tuple[str, str]] = []
    keywords: dict[str, list[str]] = {}
    for concepto, rule in conceptos.items():
        if not rule:
            continue
        for c in rule.get("codigos") or []:
            c = _norm_codigo(str(c))
            if c.endswith("*"):
                code_prefix.append((c[:-1], concepto))
            else:
                code_exact[c] = concepto
        kws = [_norm_text(k) for k in (rule.get("keywords") or [])]
        if kws:
            keywords[concepto] = kws

    out: list[dict] = []
    for r in rows:
        if r.get("concepto"):
            out.append(r); continue
        codigo = _norm_codigo(r.get("codigo", ""))
        denom = _norm_text(r.get("denominacion", ""))
        concepto = None

        if codigo:
            concepto = code_exact.get(codigo)
            if not concepto:
                for prefix, c in code_prefix:
                    if codigo.startswith(prefix):
                        concepto = c; break
        if not concepto and denom:
            for c, kws in keywords.items():
                if any(kw and kw in denom for kw in kws):
                    concepto = c; break

        new = dict(r)
        new["concepto"] = concepto
        out.append(new)
    return out
