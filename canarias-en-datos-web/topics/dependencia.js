// Configuracion de la tematica Dependencia.
// Alineada con el Cuaderno Metodologico v2 (29-04-2026):
//   * 10 indicadores del dashboard (cuaderno §4)
//   * Tablas hub: ced_dependencia_global + ced_dependencia_gen
//   * Genero como palanca (cuaderno §6): pct_mujeres_benef es directo;
//     en ced_dependencia_gen los demas indicadores son ESTIMACION INDICATIVA.

export const TOPIC = {
  id: "dependencia",
  label: "Dependencia",
  eyebrow: "Canarias en Datos · Dependencia",
  title: "El derecho a los cuidados, contado como una historia de cobertura, limbo y feminizacion.",
  lead: "Pieza D3 conectada a la base de datos del Observatorio: mapa coropletico, evolucion autonomica, brecha estimada por genero, trazabilidad metodologica y descarga directa del indicador seleccionado. Las tasas PPD se muestran como porcentaje equivalente de la PPD.",

  data: {
    globalTable: "ced_dependencia_global",
    genderTable: "ced_dependencia_gen",
    geoTable: "ccaa",
    geoNameColumn: "ccaa",
    geoGeometryColumn: "geom",
  },

  // Indicador de portada: el "limbo de la dependencia" es el mensaje central
  // del cuaderno §1 y el mas comunicativo del bloque limbo.
  defaultMetric: "tasa_pendiente_pia_ppd",

  // Los 10 indicadores del cuaderno §4 (matriz de variables seleccionadas).
  metrics: [
    {
      key: "tasa_cobertura_ppd",
      label: "Cobertura del SAAD",
      short: "Cobertura",
      unit: "% de la PPD",
      format: ".1f",
      suffix: " %",
      displayFactor: 0.1,
      min: 0,
      hasGender: true,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "tasa_solicitud_ppd",
      label: "Solicitudes acumuladas",
      short: "Solicitudes",
      unit: "% de la PPD",
      format: ".1f",
      suffix: " %",
      displayFactor: 0.1,
      min: 0,
      hasGender: true,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "pct_mujeres_benef",
      label: "% mujeres en expedientes",
      short: "% mujeres",
      unit: "% sobre total expedientes",
      format: ".1f",
      suffix: " %",
      min: 0,
      max: 100,
      hasGender: false,
      source: "IMSERSO · perfil del cuidador por CCAA",
    },
    {
      key: "tasa_pendiente_pia_ppd",
      label: "Limbo de la dependencia (pendientes de PIA)",
      short: "Limbo PIA",
      unit: "% de la PPD",
      format: ".2f",
      suffix: " %",
      displayFactor: 0.1,
      min: 0,
      hasGender: true,
      source: "IMSERSO + general.censo_ppd",
    },
    {
      key: "tasa_pendiente_grado_ppd",
      label: "Pendientes de resolución de grado ≥6 meses",
      short: "Pend. grado",
      unit: "% de la PPD",
      format: ".2f",
      suffix: " %",
      displayFactor: 0.1,
      min: 0,
      hasGender: true,
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
      id: "gender",
      type: "gender",
      title: "Género",
      sub: "Comparación mujeres-hombres por comunidad. Estimación indicativa: el IMSERSO no desagrega solicitudes ni pendientes por sexo en origen (cuaderno §6.3).",
    },
    {
      id: "method",
      type: "method",
      title: "Cómo se construye",
      sub: "Fuentes, denominador PPD, palanca de género, automatización mensual y descarga.",
    },
  ],

  method: [
    {
      title: "Fuente de datos",
      body: "Estadísticas mensuales del Sistema para la Autonomía y Atención a la Dependencia (SAAD) del IMSERSO, publicadas en formato xlsx desde 2023. Se procesan 7 hojas operativas: solicitudes (solsaad), beneficiarios (benefefect_pre), dictámenes (dictsaad), pendientes de resolución (pendResol/pendPrest), tiempos de espera (TiempoEspera) y perfil del cuidador por CCAA (perfcuidadorCCAA).",
    },
    {
      title: "Denominador PPD",
      body: "Los indicadores de cobertura (1, 2, 4, 5) se relativizan respecto a la Población Potencialmente Dependiente (PPD = población ≥65 años + 16-64 con discapacidad reconocida). Fuente primaria: tabla general.censo_ppd. Fallback automático: hoja 22solcasaadpot del propio IMSERSO. El dato se almacena como personas por cada 1.000 PPD y el D3 lo muestra como porcentaje equivalente de la PPD.",
    },
    {
      title: "Perspectiva de género",
      body: "El IMSERSO no publica solicitudes, pendientes ni tiempos desagregados por sexo. Sólo el perfil del cuidador (61aperfcuidadorCCAA) cruza CCAA × género. La tabla ced_dependencia_gen aplica este ratio como factor de escala a las métricas absolutas, marcadas con flag origen_genero='estimado'. Es una aproximación metodológicamente útil pero no equivale a datos oficiales desagregados.",
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
