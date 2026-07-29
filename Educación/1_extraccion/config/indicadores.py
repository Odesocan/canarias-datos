"""
Registro de los 10 indicadores del dashboard de Educación (Cuaderno §4).

Cada indicador declara su bloque, fuente, dataset y los filtros necesarios para
la extracción. Los indicadores del MEFP se declaran con `disponible=False`
porque EDUCAbase no ofrece API pública (ver extract/mefp.py).

Bloques (Cuaderno §4):
  A · Nivel de formación y abandono (población, EPA vía Eurostat)
  B · Desconexión juvenil
  C · Trayectoria y equidad escolar (sistema, MEFP)
  D · Esfuerzo y recursos
"""

# Cada entrada Eurostat: filtros = códigos exactos verificados contra la API.
INDICADORES = [
    # ── Bloque A · Nivel de formación y abandono ────────────────────────────
    {
        "key": "abandono_temprano",
        "nombre": "Abandono educativo temprano (18-24)",
        "bloque": "A",
        "fuente": "eurostat",
        "dataset": "edat_lfse_16",
        "filtros": {"sex": ["T", "M", "F"], "age": ["Y18-24"], "unit": ["PC"]},
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": "< 9 %",
        "disponible": True,
    },
    {
        "key": "nivel_superior_25_34",
        "nombre": "Población 25-34 con educación superior (FP superior + universitaria)",
        "bloque": "A",
        "fuente": "eurostat",
        "dataset": "edat_lfse_04",
        "filtros": {"sex": ["T", "M", "F"], "age": ["Y25-34"],
                    "isced11": ["ED5-8"], "unit": ["PC"]},
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": "≥ 45 %",
        "disponible": True,
    },
    {
        "key": "nivel_bajo_25_64",
        "nombre": "Población 25-64 con como máximo 1ª etapa de secundaria",
        "bloque": "A",
        "fuente": "eurostat",
        "dataset": "edat_lfse_04",
        "filtros": {"sex": ["T", "M", "F"], "age": ["Y25-64"],
                    "isced11": ["ED0-2"], "unit": ["PC"]},
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": None,
        "disponible": True,
    },
    {
        "key": "formacion_adultos_25_64",
        "nombre": "Participación en formación permanente (25-64, 4 semanas)",
        "bloque": "A",
        "fuente": "eurostat",
        "dataset": "trng_lfse_04",
        "filtros": {"sex": ["T", "M", "F"], "age": ["Y25-64"], "unit": ["PC"]},
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": None,
        "disponible": True,
    },
    # ── Bloque B · Desconexión juvenil ──────────────────────────────────────
    {
        "key": "neet_15_29",
        "nombre": "Jóvenes 15-29 que ni estudian ni trabajan (NEET)",
        "bloque": "B",
        "fuente": "eurostat",
        "dataset": "edat_lfse_22",
        "filtros": {"sex": ["T", "M", "F"], "age": ["Y15-29"],
                    "training": ["NO_FE_NO_NFE"], "wstatus": ["NEMP"],
                    "unit": ["PC"]},
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": "< 9 %",
        "disponible": True,
    },
    # ── Bloque C · Trayectoria y equidad escolar (MEFP · EDUCAbase PC-Axis) ──
    {
        "key": "idoneidad_15",
        "nombre": "Tasa de idoneidad a los 15 años",
        "bloque": "C",
        "fuente": "educabase",
        "dataset": "EDUCAbase · gen-idoneidad/idoneidad_05.px",
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": None,
        "disponible": True,
    },
    {
        "key": "graduacion_eso",
        "nombre": "Tasa bruta de graduación en ESO",
        "bloque": "C",
        "fuente": "educabase",
        "dataset": "EDUCAbase · resultados/series_1_03.px",
        "unidad": "%",
        "desagrega_sexo": True,
        "meta_ue2030": None,
        "disponible": True,
    },
    {
        "key": "escolarizacion_0_2",
        "nombre": "Tasa neta de escolarización 0-2 años (1er ciclo Ed. Infantil)",
        "bloque": "C",
        "fuente": "educabase",
        "dataset": "EDUCAbase · gen-escolar/escolar_05.px",
        "unidad": "%",
        "desagrega_sexo": True,   # EDUCAbase la publica por sexo
        "meta_ue2030": "45 % (objetivo Barcelona)",
        "disponible": True,
    },
    # ── Bloque D · Esfuerzo y recursos ──────────────────────────────────────
    {
        "key": "gasto_edu_pib",
        "nombre": "Gasto/presupuesto público en educación sobre PIB regional",
        "bloque": "D",
        "fuente": "presupuestos",
        "dataset": "presupuestos_pib_integrado (concepto=educacion)",
        "unidad": "%PIB",
        "desagrega_sexo": False,
        "meta_ue2030": None,
        "disponible": True,
    },
    {
        "key": "gasto_por_alumno",
        "nombre": "Gasto público por alumno en enseñanzas no universitarias (centros públicos)",
        "bloque": "D",
        "fuente": "cifras",
        "dataset": "MEFP · Cifras de la Educación · B4.6 (presupuesto liquidado)",
        "unidad": "EUR",
        "desagrega_sexo": False,
        "meta_ue2030": None,
        "disponible": True,
    },
]

# Mapeo de códigos de sexo Eurostat -> etiqueta canónica del proyecto
SEXO_MAP = {"T": "total", "M": "hombres", "F": "mujeres"}

DISPONIBLES = [i for i in INDICADORES if i["disponible"]]
PENDIENTES = [i for i in INDICADORES if not i["disponible"]]


def por_key(key):
    for i in INDICADORES:
        if i["key"] == key:
            return i
    return None
