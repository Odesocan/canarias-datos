// Configuración global del hub D3 "Canarias en Datos".
//
// La anon key de Supabase es PÚBLICA por diseño: está pensada para ir en el
// navegador y la seguridad real la impone Row Level Security (RLS) sobre las
// tablas. Por eso este archivo se commitea al repositorio.
//
// NUNCA añadir aquí la service_role key ni la contraseña de Postgres.
// Esas credenciales son para el pipeline R (.Renviron) y solo deben vivir en
// tu máquina local.

export const SUPABASE_CONFIG = Object.freeze({
  url: "https://kdpsjutsgvghdtzoskkg.supabase.co",
  anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtkcHNqdXRzZ3ZnaGR0em9za2tnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUxOTE3MzEsImV4cCI6MjA4MDc2NzczMX0.1W2H42tPmOSvVWPd65jS3m13k_M3gH_X1ifysTKppPo",
  dataSchema: "canendatos",
  geoSchema: "geodesocan",
});

// Fallback geográfico si la tabla geodesocan.ccaa no responde:
export const GEO_FALLBACK = Object.freeze({
  geojsonUrl:
    "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/NUTS_RG_01M_2021_4326_LEVL_2.geojson",
});
