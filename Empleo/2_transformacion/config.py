# -*- coding: utf-8 -*-
"""
Parámetros de la fase 2 (limpieza + transformación) — Empleo · Canarias en Datos.

Se centralizan aquí todas las decisiones que afectan al resultado para dejar
trazabilidad (§7 del cuaderno) y poder ajustarlas sin tocar la lógica.
"""
from __future__ import annotations

from pathlib import Path

# --- Rutas ---------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
EXTRACCION_DIR = BASE_DIR.parent / "1_extraccion" / "salida"
INTERMEDIO_DIR = BASE_DIR / "intermedio"      # salida de la fase A (limpieza)
SALIDA_DIR = BASE_DIR / "salida"              # salida de la fase B (consolidación)

# --- Ámbito temporal ------------------------------------------------------ #
ANYO_DESDE = 2010

# --- Territorio objetivo (para reportes de QA orientados a Canarias) ------ #
TERRITORIO_FOCO = "Canarias"

# --- Detección de outliers (SÓLO se marcan; nunca se eliminan) ------------ #
# Regla robusta por grupo (indicador · genero · categoría): mediana ± K·IQR.
OUTLIER_IQR_K = 3.0
# Rango imposible por tipo de variable (violarlo sí es error de datos):
RANGO_TASA = (0.0, 100.0)          # tasas y porcentajes
RANGO_HORAS = (0.0, 300.0)         # horas/trabajador·mes
RANGO_SALARIO = (0.0, 200_000.0)   # € brutos/año

# --- Política de valores perdidos ----------------------------------------- #
# En LIMPIEZA no se imputa (la imputación/proyección es 3_modelado, §7.6).
# Se marcan (flag) y se documenta su origen (submuestra EPA Ceuta/Melilla, etc.).
IMPUTAR_EN_LIMPIEZA = False

# --- Indicador 11 (% del salario dedicado al alquiler) -------------------- #
# El cuaderno define "Precio alquiler / salario x 100" pero no fija ni la
# superficie de la vivienda de referencia ni el nº de pagas. Se explicitan aquí;
# AJUSTAR si el criterio del observatorio es otro (p. ej. superficie ISTAC).
SUPERFICIE_REF_M2 = 80        # vivienda tipo de referencia (m²)
PAGAS_ANYO = 12               # ganancia bruta anual repartida en 12 mensualidades
# %_alquiler = (precio_m2 * SUPERFICIE_REF_M2) / (ganancia_media_anual / PAGAS_ANYO) * 100

# --- Etiquetas de genero ---------------------------------------------------- #
GENERO_AMBOS = "Ambos géneros"
GENERO_SIN_DESGLOSE = "Total"   # fuentes sin dimensión de género (ETCL, brecha)
