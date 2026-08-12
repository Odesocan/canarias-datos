// Configuración de la temática Sanidad.
// Migrada del modelo D3 consolidado (master/canendatos_storytelling_d3.html).
//   * 11 indicadores: resultados en salud, recursos, gasto y tiempos de espera.
//   * Tablas hub: global_sanidad + gen_sanidad (schema canendatos). Ojo: NO siguen
//     el patrón de nombre ced_<área>_global/_gen del resto de secciones.
//   * Género = DATO OBSERVADO del INCLASNS, y solo en los indicadores de
//     resultado: gen_sanidad no contiene recursos, gasto ni esperas.
//   * Eje anual 1990–2025; proyección por bagged ETS.

export const TOPIC = {
  id: "sanidad",
  label: "Sanidad",
  eyebrow: "Canarias en Datos · Sanidad",
  title: "Sanidad: investiga el funcionamiento del sistema sanitario en cada comunidad autónoma",
  lead: "Elige el indicador que más te interese analizar, vigila su evolución temporal y la brecha de género existente. Si quieres saber algo más sobre los datos que estás visualizando, acude al apartado de metodología en «Cómo se construye».",

  data: {
    globalTable: "global_sanidad",
    genderTable: "gen_sanidad",
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  defaultMetric: "mort_evitable_idx_0_100",

  metrics: [
    // --- Resultados en salud (con desglose por género en gen_sanidad) ---
    { key: "mort_evitable_idx_0_100", label: "Índice de mortalidad evitable (0–100)", short: "Mort. evitable",   unit: "índice 0–100 · ↑ peor",  format: ".1f", suffix: "",      min: 0, max: 100, hasGender: true,  source: "ODESOCAN sobre INCLASNS" },
    { key: "avs_65",                  label: "Años de vida saludable a los 65",       short: "AVS 65",           unit: "años",                   format: ".1f", suffix: " años", min: 0,           hasGender: true,  source: "INCLASNS" },
    { key: "reingresos_psiq",         label: "Reingresos urgentes psiquiátricos",     short: "Reingresos psiq.", unit: "% sobre altas psiq.",    format: ".1f", suffix: " %",    min: 0, max: 100, hasGender: true,  source: "INCLASNS · CMBD" },

    // --- Gasto (territorial, sin desglose por género) ---
    { key: "pct_pib_sanidad",         label: "Gasto sanitario sobre PIB",             short: "Gasto/PIB",        unit: "% del PIB regional",     format: ".2f", suffix: " %",    min: 0,           hasGender: false, source: "Presupuestos · Canarias en Datos" },
    { key: "gasto_farmacia_pct",      label: "Porcentaje del gasto en farmacia",      short: "Farmacia",         unit: "% del gasto sanitario",  format: ".1f", suffix: " %",    min: 0, max: 100, hasGender: false, source: "INCLASNS" },

    // --- Recursos (territoriales) ---
    { key: "med_ap",                  label: "Médicos de atención primaria",          short: "Médicos AP",       unit: "por 1.000 hab.",         format: ".2f", suffix: "",      min: 0,           hasGender: false, source: "INCLASNS · SIAP" },
    { key: "med_ae",                  label: "Médicos de atención especializada",     short: "Médicos AE",       unit: "por 1.000 hab.",         format: ".2f", suffix: "",      min: 0,           hasGender: false, source: "INCLASNS · SIAP" },
    { key: "enf_ap",                  label: "Enfermería de atención primaria",       short: "Enfermería AP",    unit: "por 1.000 hab.",         format: ".2f", suffix: "",      min: 0,           hasGender: false, source: "INCLASNS · SIAP" },
    { key: "camas",                   label: "Camas hospitalarias",                   short: "Camas",            unit: "por 1.000 hab.",         format: ".2f", suffix: "",      min: 0,           hasGender: false, source: "INCLASNS" },

    // --- Tiempos de espera (territoriales) ---
    { key: "espera_quir",             label: "Espera para intervención quirúrgica",   short: "Espera cirugía",   unit: "días",                   format: ".0f", suffix: " d",    min: 0,           hasGender: false, source: "INCLASNS" },
    { key: "espera_ae",               label: "Espera 1ª consulta (especializada)",    short: "Espera consulta",  unit: "días",                   format: ".0f", suffix: " d",    min: 0,           hasGender: false, source: "INCLASNS" },
  ],

  scenes: [
    { id: "context",   type: "map",       title: "Situar Canarias",   sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas para el indicador y año seleccionados." },
    { id: "evolution", type: "evolution", title: "Evolución",         sub: "Serie anual de todas las comunidades, con la proyección por bagged ETS marcada en discontinuo." },
    { id: "gender",    type: "gender",    title: "Mujeres y hombres", sub: "Comparación por comunidad en los indicadores de resultado. Desglose oficial del INCLASNS (dato observado, no estimación)." },
    { id: "method",    type: "method",    title: "Cómo se construye", sub: "Fuente INCLASNS, gasto importado de Presupuestos, índice sintético de mortalidad evitable y proyección bagged ETS." },
  ],

  method: [
    { title: "Fuentes de datos", body: "Fuente troncal: los Indicadores Clave del SNS (INCLASNS) del Ministerio de Sanidad, vía su API REST. El esfuerzo de gasto se importa del área de Presupuestos de Canarias en Datos (gasto sanitario autonómico sobre PIB regional). Origen último: SIAP, CMBD, INE, ISCIII. La geometría del mapa se sirve desde geodesocan." },
    { title: "Índice de mortalidad evitable", body: "Único índice sintético del área, construido por ODESOCAN a partir de la mortalidad prematura ajustada por edad por cáncer, cardiopatía isquémica, diabetes, ictus y EPOC. Cada componente se normaliza por su media histórica nacional y se promedia; se reescala a 0–100, donde un valor mayor indica mayor mortalidad evitable." },
    { title: "Perspectiva de género (observada)", body: "Los indicadores de resultado (mortalidad evitable, años de vida saludable, reingresos psiquiátricos) traen el desglose directo por género del INCLASNS, sin imputación. Los indicadores de sistema —recursos, gasto y esperas— no se desagregan por género: son territoriales por naturaleza de la fuente, y la escena de género los omite." },
    { title: "Comparabilidad entre comunidades", body: "Las tasas de mortalidad se descargan ajustadas por edad en origen, lo que las hace comparables entre comunidades con estructuras demográficas distintas. El gasto se expresa como porcentaje del PIB, una medida de esfuerzo relativa e intercomunitaria." },
    { title: "Proyección (bagged ETS)", body: "Las series anuales continuas de al menos diez años se proyectan con bagged ETS (Bergmeir–Hyndman–Benítez, 2016): bootstrap por bloques (STL + MBB) con 100 réplicas, un ETS por réplica y promedio de las previsiones, con intervalo de confianza del 95 %. El horizonte proyectado se marca a nivel de fila y se dibuja en línea discontinua." },
    { title: "Notas y límites", body: "Los indicadores de sistema no tienen desglose por género. El gasto sobre PIB cubre 17 comunidades (sin Ceuta ni Melilla) y es gasto presupuestado, no liquidado. La bandera de origen es a nivel de fila: un año se marca como proyección si contiene alguna estimación. La tabla incluye además enfermería de atención especializada (enf_ae), que el selector no expone para mantener la selección de indicadores del modelo consolidado." },
  ],

  sourceText: "Fuente: INCLASNS (Ministerio de Sanidad) + Presupuestos · Canarias en Datos · datos en canendatos · geometría en geodesocan · cuaderno metodológico Sanidad",
};
