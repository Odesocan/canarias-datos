// Configuración de la temática Educación.
// Pipeline Educación · Canarias en Datos (extracción Python → transformación →
// modelado a 2026 → carga a canendatos). Ver Educación/Cuaderno_metodologico_educacion.docx.

export const TOPIC = {
  id: "educacion",
  label: "Educación",
  eyebrow: "Canarias en Datos · Educación",
  title: "Educación: indaga en las condiciones educativas de Canarias en comparación con el resto del Estado",
  lead: "Elige el indicador que más te interese analizar, vigila su evolución temporal y la brecha de género existente. Si quieres saber algo más sobre los datos que estás visualizando, acude al apartado de metodología en «Cómo se construye».",

  data: {
    globalTable: "ced_educacion_global",
    genderTable: "ced_educacion_gen",
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "abandono_temprano",

  metrics: [
    { key: "abandono_temprano", label: "Abandono educativo temprano (18-24)", short: "Abandono", unit: "%", format: ".1f", suffix: "%", source: "INE·EPA / Eurostat" },
    { key: "nivel_superior_25_34", label: "Población con educación superior (25-34)", short: "Titulación superior", unit: "%", format: ".1f", suffix: "%", source: "INE·EPA / Eurostat" },
    { key: "nivel_bajo_25_64", label: "Población con bajo nivel formativo (25-64)", short: "Bajo nivel", unit: "%", format: ".1f", suffix: "%", source: "INE·EPA / Eurostat" },
    { key: "formacion_adultos_25_64", label: "Participación en formación permanente (25-64)", short: "Formación adulta", unit: "%", format: ".1f", suffix: "%", source: "INE·EPA / Eurostat" },
    { key: "neet_15_29", label: "Jóvenes que ni estudian ni trabajan (15-29)", short: "NEET", unit: "%", format: ".1f", suffix: "%", source: "INE·EPA / Eurostat" },
    { key: "idoneidad_15", label: "Tasa de idoneidad a los 15 años", short: "Idoneidad", unit: "%", format: ".1f", suffix: "%", source: "MEFP · EDUCAbase" },
    { key: "graduacion_eso", label: "Tasa bruta de graduación en ESO", short: "Graduación ESO", unit: "%", format: ".1f", suffix: "%", source: "MEFP · EDUCAbase" },
    { key: "escolarizacion_0_2", label: "Escolarización 0-2 años (1er ciclo de Infantil)", short: "Escolarización 0-2", unit: "%", format: ".1f", suffix: "%", source: "MEFP · EDUCAbase" },
    { key: "gasto_edu_pib", label: "Gasto/presupuesto en educación sobre PIB regional", short: "Gasto/PIB", unit: "%", format: ".2f", suffix: "%", source: "Presupuestos · Canarias en Datos" },
    { key: "gasto_por_alumno", label: "Gasto público por alumno (enseñanza no universitaria)", short: "Gasto/alumno", unit: "euros", format: ",.0f", suffix: " EUR", source: "MEFP · Cifras de la Educación" },
  ],

  scenes: [
    { id: "context", type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie temporal de todas las comunidades para el indicador seleccionado (2015-2026, con proyección)." },
    { id: "gender",  type: "gender",    title: "Género",            sub: "Comparación mujeres-hombres por comunidad. La brecha suele estar invertida: más abandono en hombres, más titulación superior en mujeres." },
    { id: "method",  type: "method",    title: "Cómo se construye", sub: "Fuentes, conexión a la base de datos, proyección a 2026 y descarga." },
  ],

  method: [
    { title: "Fuente de datos", body: "Explotación de las variables educativas de la Encuesta de Población Activa del INE, servida a nivel autonómico (NUTS-2) por Eurostat; estadística del MEFP (EDUCAbase, plataforma PC-Axis, y anuario «Las cifras de la Educación en España»); y el área de Presupuestos de Canarias en Datos para el esfuerzo sobre el PIB regional. La geometría del mapa se sirve desde `geodesocan`." },
    { title: "Actualización anual", body: "Los indicadores se actualizan anualmente, tras la publicación efectiva de cada fuente (EPA del INE, estadísticas del MEFP y cierre del ejercicio en Presupuestos). El género es dato observado en origen, no imputado; los indicadores de gasto no admiten desglose por sexo." },
    { title: "Proyección a 2026", body: "Cada serie (indicador × comunidad × género) compite entre estimadores simples (media, tendencia), ETS, ARIMA, Prophet, Random Forest y XGBoost mediante validación temporal rolling-origin; se elige el modelo con menor MAPE bajo una regla de parsimonia (el más simple dentro del margen del mejor). Los huecos internos se completan por interpolación y los años futuros por proyección, con la bandera `origen` distinguiendo dato real de proyectado." },
  ],

  sourceText: "Fuente: API REST del Observatorio · datos en canendatos · geometría en geodesocan",
};
