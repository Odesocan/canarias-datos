// Configuración de la temática Presupuestos (stub).
// Esta temática solo tiene tabla global (sin desagregación por género),
// lo cual valida que el motor oculta automáticamente la escena "Género".
//
// Los indicadores y tablas aquí son un ejemplo: cuando el pipeline R cargue
// datos reales a `ced_presupuestos_global`, habrá que ajustar las claves.

export const TOPIC = {
  id: "presupuestos",
  label: "Presupuestos",
  eyebrow: "Canarias en Datos · Presupuestos",
  title: "Cómo se reparten los presupuestos públicos de Canarias, por política y por territorio.",
  lead: "Pieza D3 conectada a la base de datos del Observatorio. Al no disponer de desagregación por género, el capítulo \"Género\" se omite automáticamente y solo se muestran contexto, evolución y metodología.",

  data: {
    globalTable: "ced_presupuestos_global",
    genderTable: null,
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "gasto_social_pib",

  metrics: [
    { key: "gasto_social_pib", label: "Gasto social sobre PIB", short: "Gasto/PIB", unit: "%", format: ".2f", suffix: "%", source: "IGAE" },
    { key: "gasto_social_pc", label: "Gasto social por habitante", short: "€ por habitante", unit: "EUR", format: ",.0f", suffix: " EUR", source: "IGAE + INE" },
  ],

  scenes: [
    { id: "context", type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie temporal de todas las comunidades para el indicador seleccionado." },
    { id: "method",  type: "method",    title: "Cómo se construye", sub: "Fuentes, conexión a la base de datos y notas de cálculo." },
  ],

  method: [
    { title: "Fuente de datos", body: "Liquidación presupuestaria de la IGAE, combinada con datos del INE para denominadores poblacionales y de PIB." },
    { title: "Actualización", body: "Anual, al cierre del ejercicio. Los datos provisionales se marcan con el campo `origen = provisional`." },
    { title: "Notas", body: "Los presupuestos no incluyen desagregación por género en origen, por lo que esta temática solo dispone de lectura territorial y evolución." },
  ],

  sourceText: "Fuente: API REST del Observatorio · tabla ced_presupuestos_global en canendatos",
};
