# -*- coding: utf-8 -*-
"""
FASE 2 · SUB-FASE B (1/2) — CÁLCULO DE INDICADORES
Canarias en Datos · Sección Empleo · ODESOCAN

Desde las tablas LIMPIAS (intermedio/*_limpio.parquet) calcula los indicadores
del cuaderno (§5) y los devuelve en un esquema largo homogéneo, listo para
consolidar. Cada indicador se resuelve seleccionando la categoría correcta
(tasas directas) o derivándolo (PLD, brecha, % alquiler).

Esquema largo común:
  indicador_id, indicador, unidad, territorio_cod, territorio, genero,
  anyo, trimestre, periodo, periodicidad, t_index, valor, origen, fuente,
  flag_missing, flag_outlier
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import config as cfg
from parsers import PLD_CATEGORIAS

CLAVES = ["territorio_cod", "territorio", "genero", "anyo", "trimestre",
          "periodo", "periodicidad", "t_index"]
ESQUEMA = ["indicador_id", "indicador", "unidad", *CLAVES, "valor",
           "origen", "fuente", "flag_missing", "flag_outlier"]


def _leer(slug: str) -> pd.DataFrame:
    return pd.read_parquet(cfg.INTERMEDIO_DIR / f"{slug}_limpio.parquet")


def _std(df: pd.DataFrame, ind_id: int, nombre: str, unidad: str, fuente: str) -> pd.DataFrame:
    df = df.copy()
    df["indicador_id"] = ind_id
    df["indicador"] = nombre
    df["unidad"] = unidad
    df["origen"] = "real"
    df["fuente"] = fuente
    for c in ("flag_missing", "flag_outlier"):
        if c not in df.columns:
            df[c] = False
    df["flag_missing"] = df["valor"].isna() | df["flag_missing"].fillna(False)
    return df[ESQUEMA]


# --------------------------------------------------------------------------- #
# Indicadores de tasa directa (selección de categoría)
# --------------------------------------------------------------------------- #
def tasa_directa(slug, ind_id, nombre, edad="Total", fuente="INE · EPA") -> pd.DataFrame:
    df = _leer(slug)
    df = df[df["grupo_edad"] == edad]
    return _std(df, ind_id, nombre, "%", fuente)


def porcentaje_categoria(slug, ind_id, nombre, col_cat, categoria, fuente="INE · EPA") -> pd.DataFrame:
    df = _leer(slug)
    df = df[(df["unidad"] == "Porcentaje") & (df[col_cat] == categoria)]
    return _std(df, ind_id, nombre, "%", fuente)


# --------------------------------------------------------------------------- #
# Indicador 7 — Paro de larga duración (suma de categorías ≥ 1 año)
# --------------------------------------------------------------------------- #
def paro_larga_duracion() -> pd.DataFrame:
    df = _leer("epa_tiempo_busqueda")
    df = df[(df["unidad"] == "Porcentaje") & (df["tiempo_busqueda"].isin(PLD_CATEGORIAS))]
    g = (df.groupby(CLAVES, dropna=False)
           .agg(valor=("valor", "sum"), n=("valor", "count"),
                flag_outlier=("flag_outlier", "any"))
           .reset_index())
    g.loc[g["n"] < len(PLD_CATEGORIAS), "valor"] = np.nan  # falta algún componente
    g["flag_missing"] = g["valor"].isna()
    return _std(g.drop(columns="n"), 7, "Paro de larga duración", "%", "INE · EPA")


# --------------------------------------------------------------------------- #
# Indicador 4 — Horas efectivas en servicios (ETCL, sin genero)
# --------------------------------------------------------------------------- #
def horas_servicios() -> pd.DataFrame:
    df = _leer("etcl_tiempo_trabajo")
    df = df[(df["jornada"] == "Ambas jornadas") & (df["sector"] == "Servicios")
            & (df["medida"] == "Horas efectivas")]
    return _std(df, 4, "Horas efectivas en el sector servicios", "horas/mes",
                "INE · ETCL")


# --------------------------------------------------------------------------- #
# Indicador 10 — Brecha salarial de género (H−M)/H×100
# --------------------------------------------------------------------------- #
def brecha_salarial() -> pd.DataFrame:
    df = _leer("eaes_ganancia_ccaa")
    df = df[df["estadistico"] == "Media"]
    # se pivota SÓLO sobre las claves anuales reales (trimestre es todo NaN en la
    # EAES y arrastrarlo al índice haría que pivot_table descartara todas las filas)
    piv = df.pivot_table(index=["territorio_cod", "territorio", "anyo"],
                         columns="genero", values="valor", aggfunc="first").reset_index()
    piv = piv.dropna(subset=["Hombres", "Mujeres"])
    piv["valor"] = ((piv["Hombres"] - piv["Mujeres"]) / piv["Hombres"] * 100).round(3)
    piv["genero"] = cfg.GENERO_SIN_DESGLOSE
    piv["trimestre"] = np.nan
    piv["periodo"] = piv["anyo"].astype(str)
    piv["periodicidad"] = "anual"
    piv["t_index"] = piv["anyo"].astype(float)
    piv["flag_outlier"] = False
    piv["flag_missing"] = piv["valor"].isna()
    return _std(piv, 10, "Brecha salarial de género", "%",
                "INE · EAES (Estructura Salarial)")


# --------------------------------------------------------------------------- #
# Indicador 11 — % del salario dedicado al alquiler
# (alquiler CCAA × superficie ref) / (salario mensual por genero) × 100
# --------------------------------------------------------------------------- #
def pct_salario_alquiler() -> pd.DataFrame:
    alq = _leer("alquiler_ccaa_anual")[["territorio_cod", "territorio", "anyo",
                                        "precio_m2_medio_anual"]]
    sal = _leer("eaes_ganancia_ccaa")
    sal = sal[sal["estadistico"] == "Media"][["territorio", "genero", "anyo", "valor"]]
    sal = sal.rename(columns={"valor": "ganancia_media_anual"})
    # join por NOMBRE canónico (La Rioja llega de Supabase con código de provincia)
    df = sal.merge(alq, on=["territorio", "anyo"], how="inner")
    df["renta_mensual"] = df["precio_m2_medio_anual"] * cfg.SUPERFICIE_REF_M2
    df["salario_mensual"] = df["ganancia_media_anual"] / cfg.PAGAS_ANYO
    df["valor"] = (df["renta_mensual"] / df["salario_mensual"] * 100).round(2)
    df["trimestre"] = np.nan
    df["periodo"] = df["anyo"].astype(str)
    df["periodicidad"] = "anual"
    df["t_index"] = df["anyo"].astype(float)
    df["flag_outlier"] = False
    df["flag_missing"] = df["valor"].isna()
    return _std(df, 11, "% del salario dedicado al alquiler", "%",
                "INE · EAES + Idealista (Supabase Vivienda)")


# --------------------------------------------------------------------------- #
# Orquestación del cálculo
# --------------------------------------------------------------------------- #
def calcular_todos() -> pd.DataFrame:
    piezas = [
        tasa_directa("epa_tasa_paro", 1, "Tasa de paro", "Total"),
        tasa_directa("epa_tasa_actividad", 2, "Tasa de actividad", "Total"),
        tasa_directa("epa_tasa_empleo", 3, "Tasa de empleo", "Total"),
        horas_servicios(),                                                      # 4
        tasa_directa("epa_tasa_paro", 6, "Tasa de paro juvenil (<25)", "Menores de 25 años"),
        paro_larga_duracion(),                                                  # 7
        porcentaje_categoria("epa_tipo_contrato", 8, "Tasa de temporalidad",
                             "tipo_contrato", "Temporal"),
        porcentaje_categoria("epa_tipo_jornada", 9, "Tasa de parcialidad",
                             "tipo_jornada", "Jornada a tiempo parcial"),
        brecha_salarial(),                                                      # 10
        pct_salario_alquiler(),                                                 # 11
    ]
    return pd.concat(piezas, ignore_index=True)
