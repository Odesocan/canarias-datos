# -*- coding: utf-8 -*-
"""
Parámetros de la fase 3 (modelado / proyección) — Empleo · Canarias en Datos.

Réplica en Python del patrón multi-algoritmo del proyecto (modelado.R de
Dependencia/Vivienda/Salud mental): competición de algoritmos con validación
cruzada temporal rolling-origin y selección por menor error. Aquí:

  - Métrica de selección = MAPE y MAE (petición del usuario), con NMAE de apoyo.
  - Regla de PARSIMONIA: ante errores muy semejantes, se elige el modelo más
    simple (navaja de Occam), no sólo el más preciso.
  - Bandera `origen` real/proyeccion fila a fila (§7.6).
"""
from __future__ import annotations

from pathlib import Path

# --- Rutas ---------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
CONSOLIDADO = BASE_DIR.parent / "2_transformacion" / "salida" / "ced_empleo.parquet"
SALIDA_DIR = BASE_DIR

# --- Horizonte de proyección --------------------------------------------- #
# "hasta 2026": se completan las series hasta el final de 2026
#   · trimestrales (EPA/ETCL, acaban en 2026T1) → 2026T2, T3, T4
#   · anuales (EAES/alquiler, acaban en 2024)    → 2025, 2026
HORIZONTE_ANYO = 2026

# --- Validación cruzada temporal (rolling-origin, 1 paso adelante) -------- #
CV_FOLDS_TRIMESTRAL = 4
CV_FOLDS_ANUAL = 3
# nº mínimo de puntos para modelar una serie (si no, proyección sin valor, §9)
MIN_PUNTOS_TRIMESTRAL = 12
MIN_PUNTOS_ANUAL = 6

# --- Regla de parsimonia -------------------------------------------------- #
# Un modelo es "equivalente al mejor" si su MAPE y su MAE no superan al mejor en
# más de esta fracción; entre los equivalentes se elige el de menor complejidad.
PARSIMONIA_TOL_REL = 0.05      # 5 %
MAPE_EPS = 1e-6                # umbral para excluir |y|≈0 del MAPE

# --- Inventario de algoritmos y complejidad (parsimonia) ------------------ #
# rango de complejidad: menor = más simple. 'estimadores' = modelo con
# parámetros ajustados (frente a las reglas triviales de las líneas base).
ALGORITMOS = {
    "Naive":           {"complejidad": 1, "estimadores": False},
    "HistoricAverage": {"complejidad": 1, "estimadores": False},
    "WindowAverage":   {"complejidad": 2, "estimadores": False},
    "SeasonalNaive":   {"complejidad": 2, "estimadores": False},
    "RWD":             {"complejidad": 2, "estimadores": False},  # Random Walk + Drift
    "AutoTheta":       {"complejidad": 3, "estimadores": True},
    "AutoETS":         {"complejidad": 4, "estimadores": True},
    "AutoARIMA":       {"complejidad": 5, "estimadores": True},
    "Prophet":         {"complejidad": 6, "estimadores": True},   # Meta/Prophet (opcional)
}

# Incluir Prophet en la competición (librería aparte; más lento → se cachea).
INCLUIR_PROPHET = True
