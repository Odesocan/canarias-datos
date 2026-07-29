# Fase 5 · Visualización — Sección Empleo

**Canarias en Datos · ODESOCAN** · Pieza D3 de *storytelling* interactivo,
homogénea con las de Salud mental, Vivienda y Dependencia.

## Artefacto

- **`empleo_storytelling_d3.html`** — visualización autónoma en **D3 v7**, con la
  misma arquitectura que `dependencia_storytelling_d3.html` /
  `saludmental_storytelling_d3.html`: cabecera + barra de controles
  (indicador / año / género) + navegación narrativa de 4 escenas + escenario con
  KPIs y panel de gráfico. Identidad visual propia de Empleo: **paleta índigo**
  con **acento ámbar para Canarias**.

### Las 4 escenas narrativas
1. **Situar Canarias** — mapa coroplético (cuantiles) de las 19 comunidades, con
   Canarias como *inset* destacado y leyenda interactiva por tramos.
2. **Evolución** — serie anual 2010–2026 de todas las CCAA; Canarias resaltada,
   media estatal calculada (línea discontinua) y **zona de proyección**.
3. **Mujeres y hombres** — *dumbbell* por comunidad (dato **observado** de la EPA,
   no estimado, a diferencia de otras secciones).
4. **Cómo se construye** — metodología (fuentes INE, alquiler Supabase, proyección).

### Los 10 indicadores del selector
tasa de paro · actividad · empleo · paro juvenil · paro de larga duración ·
temporalidad · parcialidad · horas efectivas en servicios · brecha salarial ·
% del salario dedicado al alquiler.

## Datos

La pieza carga primero de **Supabase** (`canendatos.ced_empleo_global` /
`_gen`) y, si no están disponibles (aún no cargadas — fase 4_carga pendiente),
cae automáticamente a los **CSV locales**:

- **`ced_empleo_global.csv`** — 1 fila por CCAA·año (19 CCAA, 2010–2026), columnas
  = los 10 indicadores (valor Ambos géneros / territorial).
- **`ced_empleo_gen.csv`** — 1 fila por CCAA·año·género (hombre/mujer), indicadores
  con desglose de género.

Ambos se generan desde el dataset modelado con:

```bash
python preparar_datos_viz.py     # lee ../3_modelado/ced_empleo.parquet
```

### Eje anual y banderas de origen

Empleo mezcla indicadores trimestrales (EPA/ETCL) y anuales (EAES/alquiler). Para
poder compararlos, todo se consolida en un **eje anual** (media anual de los
trimestrales). La marca real/proyección es **honesta por indicador**, con dos
banderas según la cadencia:

| Bandera | Indicadores | Real hasta | Proyección |
|---|---|---|---|
| `origen_q` | trimestrales (EPA/ETCL) | 2025 | 2026 |
| `origen_a` | anuales (EAES/alquiler) | 2024 | 2025–2026 |

Así, el selector marca «2026 (proyección)» para el paro pero «2025 (proyección)»
para la brecha o el alquiler. La geometría se toma de `geodesocan.ccaa`
(Supabase) con *fallback* a NUTS-2 de Eurostat.

## Estado y siguiente paso

- ✅ Visualización funcional (verificada en navegador: mapa 19 CCAA, evolución,
  género, proyección por indicador).
- Pendiente **4_carga**: cargar `ced_empleo_global`/`_gen` en Supabase (schema
  `canendatos`, patrón staging-swap) para que la pieza lea de la BD en producción.
- El `.pbix` (`Empleo.pbix`) es el cuadro de mando Power BI preexistente; esta
  pieza D3 es la versión web interactiva para canariasendatos.org.
