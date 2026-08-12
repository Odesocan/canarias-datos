// Configuración de la temática Salud mental.
// Migrada del modelo D3 consolidado (master/canendatos_storytelling_d3.html).
//   * 4 indicadores: prevalencia, consumo de psicofármacos (DHD) y suicidio.
//   * UNA SOLA tabla: ced_saludmental, con la columna `genero` incluyendo 'total'.
//     Por eso globalTable y genderTable apuntan a la misma relación; el motor lo
//     detecta y parte las filas (ver loadData en core/engine.js). El resto de
//     temáticas usan dos tablas separadas, <area>_global y <area>_gen.
//   * Género: OBSERVADO en prevalencia; IMPUTADO en antidepresivos e
//     hipnosedantes, porque el SNS solo publica el agregado total de DHD.
//   * Eje anual: 2010–2026 en el total, 2013–2026 en el desglose por género.

export const TOPIC = {
  id: "salud-mental",
  label: "Salud mental",
  eyebrow: "Canarias en Datos · Salud mental",
  title: "Salud mental: investiga el estado de la salud mental en todo el Estado en comparación con Canarias",
  lead: "Elige el indicador que más te interese analizar, vigila su evolución temporal y la brecha de género existente. Si quieres saber algo más sobre los datos que estás visualizando, acude al apartado de metodología en «Cómo se construye».",

  data: {
    globalTable: "ced_saludmental",
    genderTable: "ced_saludmental",   // misma tabla: el género vive en la columna `genero`
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "t_mental",

  metrics: [
    { key: "t_mental",         label: "Prevalencia de trastornos mentales", short: "Trastornos mentales", unit: "% población",   format: ".1f", suffix: " %",    min: 0, max: 100, hasGender: true, source: "INCLASNS · Ministerio de Sanidad" },
    { key: "antidep_ajustado", label: "Consumo de antidepresivos (DHD)",    short: "Antidepresivos",      unit: "DHD",           format: ".1f", suffix: " DHD",  min: 0,           hasGender: true, source: "INCLASNS (género imputado)" },
    { key: "hipno_ajustado",   label: "Consumo de hipnosedantes (DHD)",     short: "Hipnosedantes",       unit: "DHD",           format: ".1f", suffix: " DHD",  min: 0,           hasGender: true, source: "INCLASNS (género imputado)" },
    { key: "suicidios",        label: "Tasa de suicidio",                   short: "Suicidios",           unit: "/100.000 hab.", format: ".2f", suffix: " /100k", min: 0,          hasGender: true, source: "INE · tabla 46688" },
  ],

  scenes: [
    { id: "context",   type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas para el indicador y año seleccionados." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie anual 2010–2026 de todas las comunidades, con la proyección marcada en discontinuo." },
    { id: "gender",    type: "gender",    title: "Mujeres y hombres", sub: "Comparación por comunidad. Observado en prevalencia; en el consumo de psicofármacos es una reconstrucción, no dato oficial desagregado." },
    { id: "method",    type: "method",    title: "Cómo se construye", sub: "Fuentes INCLASNS e INE, imputación de género en los DHD, competición de algoritmos y proyección a 2026." },
  ],

  method: [
    { title: "Fuentes de datos", body: "API del INCLASNS (Ministerio de Sanidad) para la prevalencia de trastornos mentales y el consumo de antidepresivos e hipnosedantes en dosis diarias definidas por 1.000 habitantes (DHD), e INE para la mortalidad por suicidio (tabla 46688) y el censo trimestral (tabla 56940). La geometría del mapa se sirve desde geodesocan." },
    { title: "Imputación de género en los psicofármacos", body: "El SNS solo publica el agregado total de DHD, sin desglose por sexo. Hombres y mujeres se reconstruyen aplicando la brecha relativa observada en la prevalencia por género de cada comunidad y año. Es una aproximación, no un dato oficial desagregado: en antidepresivos e hipnosedantes la escena de género debe leerse como una estimación. La prevalencia y el suicidio sí son observados." },
    { title: "Variables-etiqueta", body: "Las tasas se multiplican por el censo anual (media de los cuatro trimestres) para poder mostrar magnitudes absolutas: personas con trastorno mental, dosis anuales y número de muertes. Viajan en la tabla como n_personas_tm, antidep_anual_total, hipno_anual_total y n_suicidios." },
    { title: "Modelado y proyección", body: "El pipeline compara ARIMA, ETS, Prophet, Random Forest y XGBoost con validación cruzada temporal (3 particiones, NMAE) y aplica el algoritmo de menor error global. El horizonte llega a 2026." },
    { title: "Cobertura y actualización", body: "El total cubre 2010–2026 y el desglose por género 2013–2026, en las 17 comunidades. La actualización es anual; el pipeline se ejecuta semanalmente porque la fuente publica con retraso variable y el coste de comprobarlo es bajo." },
    { title: "Origen de cada fila", body: "Cada fila lleva la marca origen = real | proyeccion. Si al menos una variable de esa fila es proyectada, la fila entera se marca como proyección, criterio conservador que evita presentar como observado lo que en parte es estimado." },
  ],

  sourceText: "Fuente: INCLASNS (Ministerio de Sanidad) + INE · datos en canendatos · geometría en geodesocan · cuaderno metodológico Salud mental",
};
