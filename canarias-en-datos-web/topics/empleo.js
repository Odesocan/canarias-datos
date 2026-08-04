// Configuración de la temática Empleo.
// Migrada del prototipo Empleo/5_visualizacion/empleo_storytelling_d3.html.
//   * 10 indicadores (cuaderno §5): volumen, calidad, brecha y presión del alquiler.
//   * Tablas hub: ced_empleo_global + ced_empleo_gen (schema canendatos).
//   * Género = DATO OBSERVADO de la EPA (no estimación, a diferencia de Dependencia).
//   * Eje anual; proyección hasta 2026. 'origen' general (cadencia trimestral) y
//     '<metrica>_origen' para los indicadores anuales (brecha, alquiler).

export const TOPIC = {
  id: "empleo",
  label: "Empleo",
  eyebrow: "Canarias en Datos · Empleo",
  title: "El trabajo, contado como una historia de volumen, calidad, género y presión del alquiler.",
  lead: "Pieza D3 conectada a la base de datos del Observatorio: tasas de paro, actividad y empleo, calidad del empleo (temporalidad, parcialidad, paro de larga duración), horas en servicios, brecha salarial y peso del alquiler sobre el salario. Canarias frente a las comunidades, serie anual 2010–2026 con proyección multi-algoritmo. La perspectiva de género es dato observado de la EPA, no una estimación.",

  data: {
    globalTable: "ced_empleo_global",
    genderTable: "ced_empleo_gen",
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "tasa_paro",

  metrics: [
    { key: "tasa_paro",            label: "Tasa de paro",                         short: "Paro",             unit: "% de activos",        format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "tasa_actividad",       label: "Tasa de actividad",                    short: "Actividad",        unit: "% pob. 16+",          format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "tasa_empleo",          label: "Tasa de empleo",                       short: "Empleo",           unit: "% pob. 16+",          format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "paro_juvenil",         label: "Tasa de paro juvenil (<25)",           short: "Paro juvenil",     unit: "% de activos <25",    format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "paro_larga_duracion",  label: "Paro de larga duración",               short: "PLD",              unit: "% de parados ≥1 año", format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "temporalidad",         label: "Tasa de temporalidad",                 short: "Temporalidad",     unit: "% de asalariados",    format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "parcialidad",          label: "Tasa de parcialidad",                  short: "Parcialidad",      unit: "% de ocupados",       format: ".1f", suffix: " %", min: 0, max: 100, hasGender: true,  source: "INE · EPA" },
    { key: "horas_servicios",      label: "Horas efectivas · sector servicios",   short: "Horas servicios",  unit: "horas/mes",           format: ".1f", suffix: " h", min: 0,          hasGender: false, source: "INE · ETCL" },
    { key: "brecha_salarial",      label: "Brecha salarial de género",            short: "Brecha salarial",  unit: "% (H−M)/H",           format: ".1f", suffix: " %",                    hasGender: false, source: "INE · EAES" },
    { key: "pct_alquiler_salario", label: "% del salario dedicado al alquiler",   short: "Alquiler/salario", unit: "% del salario mensual", format: ".1f", suffix: " %", min: 0,        hasGender: true,  source: "INE · EAES + Idealista" },
  ],

  scenes: [
    { id: "context",   type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas para el indicador y año seleccionados." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie anual 2010–2026 de todas las comunidades, con la proyección marcada en discontinuo." },
    { id: "gender",    type: "gender",    title: "Mujeres y hombres", sub: "Comparación por comunidad. Desglose oficial de la EPA (dato observado, no estimación)." },
    { id: "method",    type: "method",    title: "Cómo se construye", sub: "Fuentes INE (EPA · ETCL · EAES), alquiler desde la base de datos, proyección multi-algoritmo y descarga." },
  ],

  method: [
    { title: "Fuentes de datos", body: "Tres operaciones del INE vía API JSON (Tempus3): EPA (tasas y calidad del empleo, trimestral), ETCL (horas efectivas por sector, trimestral) y EAES (ganancia media por sexo y CCAA, anual). El precio de alquiler procede de Idealista, reutilizado desde la base de datos de la sección Vivienda. La geometría del mapa se sirve desde geodesocan." },
    { title: "Los diez indicadores", body: "Volumen (paro, actividad, empleo, paro juvenil), calidad (temporalidad, parcialidad, paro de larga duración), intensidad (horas efectivas en servicios) y dos indicadores de condiciones de vida: brecha salarial y % del salario dedicado al alquiler. Todos por CCAA; los de la EPA, además, por género." },
    { title: "Perspectiva de género (observada)", body: "A diferencia de otras secciones, la EPA publica el desglose directo por género, sin imputación. La brecha salarial se calcula como (ganancia H − ganancia M) / ganancia H × 100 desde la EAES. El % del salario en alquiler se desagrega por el denominador salarial." },
    { title: "Eje temporal anual", body: "Para comparar indicadores de distinta cadencia, los trimestrales (EPA/ETCL) se agregan a media anual y los anuales (EAES/alquiler) se toman directos. Cada indicador marca real o proyección según su cadencia: los trimestrales son reales hasta 2025; los anuales, hasta 2024." },
    { title: "Proyección hasta 2026", body: "Competición de AutoARIMA, AutoETS, AutoTheta y Prophet frente a líneas base (Naive, SeasonalNaive, drift…), con validación cruzada temporal rolling-origin. Se elige por serie el de menor MAPE/MAE con regla de parsimonia (ante empate, el más simple). La proyección se dibuja en línea discontinua." },
    { title: "Notas y límites", body: "Las horas efectivas (ETCL) y la brecha salarial son indicadores territoriales sin desglose por género. La afiliación a la Seguridad Social (indicador 5 del cuaderno) queda pendiente de incorporar. El % de alquiler asume una vivienda de referencia de 80 m² (parámetro ajustable)." },
  ],

  sourceText: "Fuente: INE (EPA · ETCL · EAES) + Idealista · datos en canendatos · geometría en geodesocan · cuaderno metodológico Empleo (CED-05)",
};
