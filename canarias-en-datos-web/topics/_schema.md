# Esquema de configuración por temática

Cada archivo `topics/<tematica>.js` exporta un objeto con esta forma:

```js
export const TOPIC = {
  id: "vivienda",                     // slug único, usado en la URL (?tematica=vivienda)
  label: "Vivienda",                  // texto del botón en la botonera
  order: 9,                           // posición si no quieres orden alfabético (opcional)
  eyebrow: "Canarias en Datos · Vivienda",
  title: "El acceso a la vivienda contado como una historia de presión, género y evidencia.",
  lead: "Pieza D3 conectable a Supabase: mapa coroplético, evolución autonómica, brecha de género...",

  // Tablas en Supabase. _gen es opcional: si no existe, el motor oculta la escena "género".
  data: {
    globalTable: "ced_vivienda_global",
    genderTable: "ced_vivienda_gen",  // o null si esta temática no tiene brecha de género
  },

  // Indicadores disponibles en el selector. Claves deben coincidir con columnas de la tabla.
  metrics: [
    { key: "esfuerzo", label: "Esfuerzo de acceso (% ingresos)", unit: "%", format: "pct" },
    { key: "precio_m2", label: "Precio medio €/m²", unit: "€/m²", format: "currency" },
    // ...
  ],

  // Escenas narrativas. El orden aquí define el orden en la navegación lateral.
  // Tipos soportados: "map" | "evolution" | "gender" | "method"
  scenes: [
    { id: "context",    type: "map",       title: "Situar Canarias",    sub: "..." },
    { id: "evolution",  type: "evolution", title: "Evolución",          sub: "..." },
    { id: "gender",     type: "gender",    title: "Género",             sub: "..." },  // se omite si data.genderTable es null
    { id: "method",     type: "method",    title: "Cómo se construye",  sub: "..." },
  ],

  // Metadatos de la fuente y metodología (se muestran en la escena "method" y en el pie).
  source: {
    label: "Fuente: Supabase · canendatos · flujo ETL Vivienda",
    methodologyUrl: "https://canariasendatos.org/metodologia/vivienda",  // opcional
  },
};
```

## Temáticas planificadas (orden alfabético)

1. Comunicación
2. Dependencia
3. Educación
4. Empleo
5. Migraciones
6. Presupuestos
7. Salud mental
8. Sanidad
9. Vivienda

La primera en implementarse será **Vivienda** (migración del prototipo actual).
Las demás se añadirán creando su archivo `topics/<slug>.js` cuando el pipeline de datos esté disponible en Supabase.

## Campos completos de cada `metric`

El bloque de arriba está simplificado. El motor admite, por indicador:

```js
{
  key: "tasa_paro",            // = nombre de columna en la tabla
  label: "Tasa de paro",       // texto del selector
  short: "Paro",               // etiqueta corta (leyendas, tooltips)
  unit: "% de activos",        // unidad (subtítulos)
  format: ".1f",               // patrón d3-format
  suffix: " %",                // se añade tras el número
  min: 0, max: 100,            // recorte opcional del valor mostrado
  displayFactor: 0.1,          // opcional: multiplica el valor guardado (p. ej. por-1000 → %)
  hasGender: true,             // ¿existe en la tabla _gen? (si no, la escena "género" avisa)
  source: "INE · EPA",         // procedencia (escena método)
}
```

Además, el TOPIC admite `defaultMetric: "<key>"` (indicador de portada).

## Cadencias mixtas: `origen` y periodo POR MÉTRICA

Por defecto el motor lee una columna **`origen`** por fila (`real` / `proyeccion`)
y un **`periodo`** común. Pero cuando una temática mezcla indicadores de distinta
cadencia (p. ej. **Empleo**: EPA/ETCL trimestrales vs EAES/alquiler anuales, con
distinta frontera real→proyección, o **Vivienda**: precios mensuales vs variables
INE anuales), el motor soporta **override por métrica**, resuelto así:

```
origen efectivo   = fila[`${metric}_origen`]        || fila.origen        || "real"
periodo efectivo  = fila[`${metric}_periodo_label`] || fila.periodo_label || periodo
```

Es decir: añade en la tabla una columna **`<key>_origen`** (y/o
**`<key>_periodo_label`**) SÓLO para los indicadores cuya cadencia difiere de la
general; el resto usa la columna común `origen` / `periodo`. No hay que tocar el
motor ni el TOPIC: basta con que las columnas existan en Supabase.

**Ejemplo real (Empleo):** columna general `origen` = cadencia trimestral
(real ≤2025) para los 8 indicadores EPA/ETCL; y columnas `brecha_salarial_origen`
y `pct_alquiler_salario_origen` = cadencia anual (real ≤2024) para los dos
indicadores anuales. Así el selector marca «2026 (proyección)» para el paro pero
«2025 (proyección)» para la brecha y el alquiler, sin mentir sobre qué es real.

El generador del pipeline (`Empleo/5_visualizacion/preparar_datos_viz.py`) es la
referencia de cómo emitir estas columnas.
