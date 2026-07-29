// Configuración de la temática Vivienda.
// Migrada 1:1 del prototipo Vivienda/vivienda_storytelling_d3_divi.html.

export const TOPIC = {
  id: "vivienda",
  label: "Vivienda",
  eyebrow: "Canarias en Datos · Vivienda",
  title: "El acceso a la vivienda contado como una historia de presión, género y evidencia.",
  lead: "Pieza D3 conectable a Supabase: mapa coroplético, evolución autonómica, brecha de género, trazabilidad metodológica y descarga directa del indicador seleccionado.",

  data: {
    globalTable: "ced_vivienda_global",
    genderTable: "ced_vivienda_gen",
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "salario_destinado",

  metrics: [
    { key: "precio_alquiler", label: "Precio del alquiler", short: "Alquiler", unit: "euros/mes", format: ",.2f", suffix: " EUR/mes", source: "Idealista" },
    { key: "precio_venta", label: "Precio de venta", short: "Venta", unit: "EUR/m2", format: ",.2f", suffix: " EUR/m2", source: "Idealista" },
    { key: "salario_destinado", label: "Salario destinado al alquiler", short: "Esfuerzo", unit: "%", format: ".2f", suffix: "%", source: "INE + Idealista" },
    { key: "gasto_elevado", label: "Gasto elevado en vivienda", short: "Gasto elevado", unit: "%", format: ".2f", suffix: "%", source: "INE" },
    { key: "retrasos_pagos", label: "Retrasos en pagos", short: "Retrasos", unit: "%", format: ".2f", suffix: "%", source: "INE" },
    { key: "dif_finmes", label: "Dificultad para llegar a fin de mes", short: "Fin de mes", unit: "%", format: ".2f", suffix: "%", source: "INE" },
    { key: "espacio_insuf", label: "Espacio insuficiente en la vivienda", short: "Espacio insuf.", unit: "%", format: ".2f", suffix: "%", source: "INE" },
    { key: "hogares_mono", label: "Hogares monoparentales", short: "Monoparentales", unit: "miles", format: ".2f", suffix: " mil", source: "INE" },
  ],

  scenes: [
    { id: "context", type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie temporal de todas las comunidades para el indicador seleccionado." },
    { id: "gender",  type: "gender",    title: "Género",            sub: "Comparación mujeres-hombres por comunidad con una lectura clara de la brecha." },
    { id: "method",  type: "method",    title: "Cómo se construye", sub: "Fuentes, conexión Supabase, automatización mensual, estimaciones y descarga." },
  ],

  method: [
    { title: "Fuente de datos", body: "Encuesta de Condiciones de Vida del INE, Encuesta de Estructura Salarial del INE y portal inmobiliario Idealista. La geometría del mapa se sirve desde `geodesocan`." },
    { title: "Actualización mensual", body: "La actualización mensual aplica específicamente a los precios de vivienda en venta y alquiler procedentes de Idealista. El resto de variables se actualiza anualmente por las limitaciones de publicación de las fuentes originales del INE." },
    { title: "Estimaciones", body: "Para todas las variables salvo los precios de vivienda en venta y alquiler, el pipeline compara ARIMA, ETS, Prophet, Random Forest y XGBoost mediante validación temporal y selecciona el algoritmo con menor error global normalizado. Los precios de vivienda se incorporan como dato observado cuando Idealista publica actualización." },
  ],

  sourceText: "Fuente: Supabase REST · datos en canendatos · geometría en geodesocan",
};
