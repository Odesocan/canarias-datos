// Configuracion de la tematica Dependencia.
// Alineada con el Cuaderno Metodologico v2 (29-04-2026):
//   * 10 indicadores del dashboard (cuaderno §4)
//   * Tabla hub: ced_dependencia_global (sin tabla de genero, ver data).
//   * Genero: ningun indicador llega desagregado por sexo. ced_dependencia_gen
//     reparte cobertura, solicitudes y limbos con el % de mujeres entre las
//     personas CUIDADORAS familiares, que no es el de las personas
//     dependientes: la "brecha" resultante es el indicador total por una
//     constante, no una medicion. Por eso no se usa, igual que en el modelo
//     de master/. La perspectiva de genero se lee en pct_mujeres_benef
//     (feminizacion del cuidado) y pct_pecef.

export const TOPIC = {
  id: "dependencia",
  label: "Dependencia",
  eyebrow: "Canarias en Datos · Dependencia",
  title: "Dependencia: analiza el Sistema para la Autonomía y Atención a la Dependencia",
  lead: "Elige el indicador que más te interese analizar, compara comunidades y vigila su evolución mes a mes. Si quieres saber algo más sobre los datos que estás visualizando, acude al apartado de metodología en «Cómo se construye».",

  data: {
    globalTable: "ced_dependencia_global",
    genderTable: null,  // sin desagregacion por sexo: el motor oculta la escena "genero" (ver cabecera)
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  // Indicador de portada: el "limbo de la dependencia" es el mensaje central
  // del cuaderno §1 y el mas comunicativo del bloque limbo.
  defaultMetric: "limbo_pia_pct_ppd",

  // Los 10 indicadores del cuaderno §4 (matriz de variables seleccionadas).
  metrics: [
    {
      key: "cobertura_pct_ppd",
      label: "Cobertura del SAAD",
      short: "Cobertura",
      unit: "% de la PPD",
      format: ".1f",
      suffix: " %",
      min: 0,
      hasGender: false,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "solicitudes_pct_ppd",
      label: "Solicitudes acumuladas",
      short: "Solicitudes",
      unit: "% de la PPD",
      format: ".1f",
      suffix: " %",
      min: 0,
      hasGender: false,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "pct_mujeres_benef",
      label: "Mujeres entre las personas cuidadoras familiares (%)",
      short: "% cuidadoras",
      unit: "% de personas cuidadoras",
      format: ".1f",
      suffix: " %",
      min: 0,
      max: 100,
      hasGender: false,
      source: "IMSERSO · perfil del cuidador por CCAA",
    },
    {
      key: "limbo_pia_pct_ppd",
      label: "Limbo de la dependencia (pendientes de PIA)",
      short: "Limbo PIA",
      unit: "% de la PPD",
      format: ".2f",
      suffix: " %",
      min: 0,
      hasGender: false,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "limbo_grado_pct_ppd",
      label: "Pendientes de resolución de grado ≥6 meses",
      short: "Pend. grado",
      unit: "% de la PPD",
      format: ".2f",
      suffix: " %",
      min: 0,
      hasGender: false,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "tiempo_espera_total_dias",
      label: "Tiempo de espera (solicitud → prestación)",
      short: "Días espera",
      unit: "días",
      format: ",.0f",
      suffix: " días",
      min: 0,
      hasGender: false,
      source: "IMSERSO · 9TiempoEspera",
    },
    {
      key: "pct_pecef",
      label: "% PECEF (cuidados familiares)",
      short: "% PECEF",
      unit: "% sobre total prestaciones",
      format: ".1f",
      suffix: " %",
      min: 0,
      max: 100,
      hasGender: false,
      source: "IMSERSO · benefefect_pre",
    },
    {
      key: "pct_atencion_residencial",
      label: "% atención residencial",
      short: "% residencial",
      unit: "% sobre total prestaciones",
      format: ".1f",
      suffix: " %",
      min: 0,
      max: 100,
      hasGender: false,
      source: "IMSERSO · benefefect_pre",
    },
    {
      key: "ratio_prest_x_benef",
      label: "Intensidad de atención (prestaciones por persona)",
      short: "Intensidad",
      unit: "prestaciones por beneficiario",
      format: ".2f",
      suffix: "",
      min: 0,
      hasGender: false,
      source: "IMSERSO · benefefect_pre",
    },
    {
      key: "pct_grado3",
      label: "% Grado III (gran dependencia)",
      short: "% Grado III",
      unit: "% sobre resoluciones de grado",
      format: ".1f",
      suffix: " %",
      min: 0,
      max: 100,
      hasGender: false,
      source: "IMSERSO · dictsaad",
    },
  ],

  scenes: [
    {
      id: "context",
      type: "map",
      title: "Situar Canarias",
      sub: "Mapa coroplético interactivo para comparar Canarias con el resto de comunidades autónomas.",
    },
    {
      id: "evolution",
      type: "evolution",
      title: "Evolución",
      sub: "Serie temporal mensual desde 2023 para el indicador seleccionado, con proyección a 12 meses marcada en discontinuo.",
    },
    {
      id: "method",
      type: "method",
      title: "Cómo se construye",
      sub: "Fuentes, denominador PPD, perspectiva de género, automatización mensual y descarga.",
    },
  ],

  method: [
    {
      title: "Fuente de datos",
      body: "Estadísticas mensuales del Sistema para la Autonomía y Atención a la Dependencia (SAAD) del IMSERSO, publicadas en formato xlsx desde 2023. Se procesan 7 hojas operativas: solicitudes (solsaad), beneficiarios (benefefect_pre), dictámenes (dictsaad), pendientes de resolución (pendResol/pendPrest), tiempos de espera (TiempoEspera) y perfil del cuidador por CCAA (perfcuidadorCCAA).",
    },
    {
      title: "Denominador PPD",
      body: "Los indicadores de cobertura (1, 2, 4, 5) se relativizan respecto a la Población Potencialmente Dependiente (PPD = población ≥65 años + 16-64 con discapacidad reconocida). Fuente primaria: tabla general.censo_ppd. Fallback automático: hoja 22solcasaadpot del propio IMSERSO. El dato se almacena ya como porcentaje de la PPD (columnas *_pct_ppd).",
    },
    {
      title: "Perspectiva de género",
      body: "El IMSERSO no publica por género y comunidad las solicitudes, las personas beneficiarias ni las esperas, así que ningún indicador de esta sección está desagregado por género. Repartirlos con el porcentaje de mujeres entre las personas cuidadoras no sirve: es otra población, y la brecha resultante sería el mismo indicador multiplicado por una constante. La perspectiva de género se lee en dos indicadores: el porcentaje de mujeres entre las personas cuidadoras familiares y el peso de la prestación para cuidados en el entorno familiar (PECEF), un cuidado que recae sobre todo en mujeres.",
    },
    {
      title: "Actualización mensual",
      body: "El IMSERSO publica entre 6 y 8 semanas después del cierre de mes. El pipeline se ejecuta automáticamente el día 5 de cada mes vía GitHub Actions. La carga a la base de datos es atómica (staging + RENAME + reinstalación de índices únicos y RLS): el dashboard nunca lee una tabla en estado intermedio.",
    },
    {
      title: "Proyección de 12 meses",
      body: "Para cada uno de los 10 indicadores se compara ARIMA, ETS, Random Forest y XGBoost mediante validación cruzada temporal rolling-origin de 3 folds, seleccionando el algoritmo con menor NMAE global. Prophet se descarta por defecto al tener NMAE ~4× peor con series mensuales cortas. La proyección se renderiza en línea discontinua para diferenciarla del observado.",
    },
  ],

  sourceText: "Fuente: API REST del Observatorio · datos en canendatos · geometría en geodesocan · cuaderno metodológico v2",
};
