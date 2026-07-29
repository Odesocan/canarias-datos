# -*- coding: utf-8 -*-
"""
Catálogo de fuentes verificadas para la sección de Empleo (Canarias en Datos).

Cada entrada asocia un indicador del cuaderno metodológico (§5) con la tabla
concreta de la API del INE que lo sustenta, VERIFICADA contra el servicio real
el 2026-07-21 (devuelve datos vivos con desglose de Canarias).

IMPORTANTE (separación de fases):
  La extracción descarga las tablas TAL CUAL (tasas ya publicadas, o conteos y
  porcentajes por categoría). El CÁLCULO de los indicadores derivados
  (p. ej. % de paro de larga duración, tasa de temporalidad, brecha salarial)
  corresponde a la fase 2_transformacion, no a esta. Aquí sólo se indica, en
  ``derivacion``, cómo se obtendrá cada indicador aguas abajo.

Estado de cada indicador:
  OK        -> disponible directamente en la API del INE (tabla confirmada).
  DERIVADO  -> disponible como insumo en el INE; el indicador final se calcula
               en transformación a partir de las categorías de la tabla.
  PENDIENTE -> requiere fuente no-INE o decisión de fuente (ver README §gaps).
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FuenteINE:
    indicador_id: int          # nº de indicador en la matriz del cuaderno (§5)
    nombre: str                # nombre del indicador
    operacion: str             # código de operación INE (EPA / ETCL / EAES)
    id_tabla: int              # id de tabla verificado
    tabla_nombre: str          # nombre de la tabla en el INE
    periodicidad: str          # trimestral / mensual / anual
    estado: str                # OK | DERIVADO
    derivacion: str            # cómo se obtiene el indicador en transformación
    slug: str                  # nombre de fichero de salida (sin extensión)
    desagregacion: str = ""    # dimensiones útiles de la tabla
    notas: str = ""


# --------------------------------------------------------------------------- #
# Tablas INE verificadas (2026-07-21)
# --------------------------------------------------------------------------- #
CATALOGO_INE: list[FuenteINE] = [
    FuenteINE(
        indicador_id=1,
        nombre="Tasa de paro",
        operacion="EPA",
        id_tabla=14506,
        tabla_nombre="Tasas de paro por distintos grupos de edad, genero y comunidad autónoma",
        periodicidad="trimestral",
        estado="OK",
        derivacion="Tasa publicada directamente (grupo de edad = Total).",
        slug="epa_tasa_paro",
        desagregacion="genero · grupo_edad · CCAA",
    ),
    FuenteINE(
        indicador_id=6,
        nombre="Tasa de paro juvenil (<25)",
        operacion="EPA",
        id_tabla=14506,
        tabla_nombre="Tasas de paro por distintos grupos de edad, genero y comunidad autónoma",
        periodicidad="trimestral",
        estado="OK",
        derivacion="Misma tabla que el indicador 1, seleccionando 'Menores de 25 años'.",
        slug="epa_tasa_paro",  # comparte tabla con el indicador 1
        desagregacion="genero · grupo_edad · CCAA",
        notas="Se extrae una sola vez la tabla 14506; cubre indicadores 1 y 6.",
    ),
    FuenteINE(
        indicador_id=2,
        nombre="Tasa de actividad",
        operacion="EPA",
        id_tabla=14509,
        tabla_nombre="Tasas de actividad por distintos grupos de edad, genero y comunidad autónoma",
        periodicidad="trimestral",
        estado="OK",
        derivacion="Tasa publicada directamente (grupo de edad = Total).",
        slug="epa_tasa_actividad",
        desagregacion="genero · grupo_edad · CCAA",
    ),
    FuenteINE(
        indicador_id=3,
        nombre="Tasa de empleo",
        operacion="EPA",
        id_tabla=14508,
        tabla_nombre="Tasas de empleo por distintos grupos de edad, genero y comunidad autónoma",
        periodicidad="trimestral",
        estado="OK",
        derivacion="Tasa publicada directamente (grupo de edad = Total).",
        slug="epa_tasa_empleo",
        desagregacion="genero · grupo_edad · CCAA",
    ),
    FuenteINE(
        indicador_id=7,
        nombre="Paro de larga duración",
        operacion="EPA",
        id_tabla=65340,
        tabla_nombre="Parados por tiempo de búsqueda de empleo, genero y comunidad autónoma. "
        "Porcentajes respecto del total de cada comunidad",
        periodicidad="trimestral",
        estado="DERIVADO",
        derivacion="Suma de los porcentajes de las categorías '≥ 1 año' "
        "('De 1 año a menos de 2 años' + '2 años o más').",
        slug="epa_tiempo_busqueda",
        desagregacion="genero · tiempo_busqueda · CCAA",
    ),
    FuenteINE(
        indicador_id=8,
        nombre="Tasa de temporalidad",
        operacion="EPA",
        id_tabla=65328,
        tabla_nombre="Asalariados por tipo de contrato o relación laboral, genero y comunidad "
        "autónoma. Valores absolutos y porcentajes respecto del total de cada comunidad",
        periodicidad="trimestral",
        estado="DERIVADO",
        derivacion="% de asalariados con contrato temporal sobre el total de asalariados "
        "(porcentaje de la categoría 'De duración temporal').",
        slug="epa_tipo_contrato",
        desagregacion="genero · tipo_contrato · CCAA",
    ),
    FuenteINE(
        indicador_id=9,
        nombre="Tasa de parcialidad",
        operacion="EPA",
        id_tabla=65319,
        tabla_nombre="Ocupados por tipo de jornada, genero y comunidad autónoma. "
        "Valores absolutos y porcentajes respecto del total de cada comunidad",
        periodicidad="trimestral",
        estado="DERIVADO",
        derivacion="% de ocupados a tiempo parcial sobre el total de ocupados "
        "(porcentaje de la categoría 'Jornada a tiempo parcial').",
        slug="epa_tipo_jornada",
        desagregacion="genero · tipo_jornada · CCAA",
    ),
    FuenteINE(
        indicador_id=4,
        nombre="Horas efectivas trabajadas en el sector servicios",
        operacion="ETCL",
        id_tabla=6063,
        tabla_nombre="Tiempo de trabajo por trabajador y mes por comunidad autónoma, "
        "tipo de jornada, sectores de actividad",
        periodicidad="trimestral",
        estado="OK",
        derivacion="Serie 'Servicios · Ambas jornadas · Horas efectivas'. "
        "OJO: la ETCL NO desagrega por genero (ver notas).",
        slug="etcl_tiempo_trabajo",
        desagregacion="sector · tipo_jornada · CCAA  (SIN genero)",
        notas="La ETCL no publica desglose por género. El indicador 4 del cuaderno "
        "pide 'Género · CCAA'; sólo es posible 'sector · CCAA'. Decisión pendiente.",
    ),
    FuenteINE(
        indicador_id=10,
        nombre="Brecha salarial de género",
        operacion="EAES",
        id_tabla=28191,
        tabla_nombre="Encuesta Anual de Estructura Salarial: medias y percentiles por genero y CCAA",
        periodicidad="anual",
        estado="DERIVADO",
        derivacion="Brecha = (ganancia media Hombres − ganancia media Mujeres) / "
        "ganancia media Hombres × 100, a partir de la categoría 'Media'.",
        slug="eaes_ganancia_ccaa",
        desagregacion="genero · CCAA · estadístico(media/percentiles)",
        notas="Frecuencia anual y menor actualidad (último dato 2024 a fecha de verificación).",
    ),
]

# --------------------------------------------------------------------------- #
# Indicadores fuera de la API del INE — DECISIÓN DE FUENTE TOMADA (2026-07-21)
# --------------------------------------------------------------------------- #
FUENTES_NO_INE = [
    {
        "indicador_id": 5,
        "nombre": "Afiliación a la Seguridad Social",
        "fuente_cuaderno": "MISSM (TGSS)",
        "decision": "Ficheros de la Seguridad Social (TGSS), nivel provincial "
        "(Las Palmas 35 · Santa Cruz de Tenerife 38).",
        "extractor": "extraer_seg_social.py",
        "estado": "PREPARADO — pendiente de colocar los ficheros en fuentes_seg_social/",
        "nota_insular": "El nivel ISLA no lo publica la SS; requeriría ISTAC.",
    },
    {
        "indicador_id": 11,
        "nombre": "% del salario dedicado al alquiler",
        "fuente_cuaderno": "Estructura Salarial (INE) + Idealista",
        "decision": "Alquiler desde Supabase (bd_odesocan · public.alquiler_historico_ccaa, "
        "sección Vivienda). El salario (EAES, ya extraído) aporta la desagregación por "
        "género; la derivación (alquiler/salario) se hace en 2_transformacion.",
        "extractor": "extraer_supabase.py",
        "estado": "EXTRAÍDO — salida/alquiler_ccaa_anual.* (2010–2026, 19 CCAA)",
        "nota": "En Supabase La Rioja llega con codigo_ccaa='26' (provincia); el join con "
        "el salario debe hacerse por NOMBRE canónico, no por código de origen.",
    },
]


def catalogo_ine_unico() -> list[FuenteINE]:
    """Devuelve el catálogo sin descargas duplicadas (indicadores 1 y 6 comparten tabla)."""
    vistos: set[tuple[str, int]] = set()
    unico: list[FuenteINE] = []
    for f in CATALOGO_INE:
        clave = (f.operacion, f.id_tabla)
        if clave in vistos:
            continue
        vistos.add(clave)
        unico.append(f)
    return unico
