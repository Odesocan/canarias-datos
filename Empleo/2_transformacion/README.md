# Fase 2 · Transformación — Sección Empleo

**Canarias en Datos · ODESOCAN** · Implementación en **Python** de `2_transformacion`
(§8 del cuaderno). Toma los artefactos de `1_extraccion/salida` y produce el
dataset longitudinal consolidado `ced_empleo`.

Se organiza en las dos sub-fases pedidas:

## A · Limpieza (`limpieza.py`)

1. **Valores perdidos** → se **cuantifican y marcan** (`flag_missing`); **no se
   imputan** (la imputación/proyección es `3_modelado`, §7.6). Se documenta su
   origen (submuestras EPA de Ceuta/Melilla, celdas suprimidas por «Secreto»).
2. **Outliers** → se detectan con regla robusta **mediana ± 3·IQR por serie de
   cada territorio** (anomalía temporal, no tamaño) y con **rangos imposibles**
   por tipo de variable. Se **marcan** (`flag_outlier`, `flag_rango`); **no se
   eliminan** (los extremos reales — p. ej. el desplome de horas en 2020T2 por
   COVID, o el paro juvenil de Ceuta/Melilla — son informativos).
3. **Homogeneización** → territorio canónico, género estandarizado
   ({Ambos géneros, Hombres, Mujeres} · `Total` si no hay género), **categorías**
   extraídas con vocabulario controlado (`parsers.py`) y **periodo unificado**
   (`anyo`, `trimestre`, `t_index`).

Salida: `intermedio/*_limpio.parquet` + `intermedio/reporte_limpieza.csv`.

## B · Consolidación / join (`indicadores.py` + `consolidar.py`)

Calcula los indicadores del cuaderno (§5) desde los datos limpios y los une en un
**dataset único**. Se generan dos vistas del mismo contenido:

| Fichero | Forma | Uso |
|---|---|---|
| `salida/ced_empleo.csv` | **largo/tidy**, frecuencia nativa | fuente de verdad, sin pérdida de info |
| `salida/ced_empleo_anual_ancho.csv` | **ancho anual** (1 fila por territorio·género·año) | Power BI y comparativas entre CCAA |

> **Por qué el largo es el canónico**: los indicadores tienen frecuencias
> (trimestral/anual) y desagregaciones (con/sin género) distintas; una única
> matriz ancha nativa quedaría llena de huecos. El largo lo evita y el ancho
> anual se deriva de él (§7.1 «agregados anuales homogéneos»).

### Cómo se obtiene cada indicador

| # | Indicador | Cálculo |
|---|-----------|---------|
| 1 | Tasa de paro | selección directa (grupo edad = Total) |
| 2 | Tasa de actividad | selección directa |
| 3 | Tasa de empleo | selección directa |
| 6 | Paro juvenil | selección (Menores de 25 años) |
| 7 | Paro larga duración | suma de % de categorías ≥ 1 año |
| 8 | Temporalidad | % de contrato temporal |
| 9 | Parcialidad | % de jornada parcial |
| 4 | Horas servicios | ETCL (Servicios · Ambas jornadas · Horas efectivas) — **sin género** |
| 10 | Brecha salarial | (media H − media M) / media H × 100 |
| 11 | % salario en alquiler | (precio_m² × 80 m²) / (ganancia_media / 12) × 100 |

## Cómo ejecutar

```bash
cd 2_transformacion
python transformar.py               # limpieza → consolidación
python transformar.py --solo limpieza
python validacion.py                # QA del consolidado
```

## Decisiones y avisos (trazabilidad, §7)

- **Indicador 11**: el cuaderno da la fórmula pero no fija superficie ni nº de
  pagas. Supuesto explícito y **ajustable** en `config.py`:
  **80 m²** de vivienda de referencia y **12 pagas/año** (ganancia bruta).
  Con ello, en Canarias 2024 el ratio es ~53%. Cambiar el supuesto cambia el nivel.
- **Indicador 4** (horas): sin desglose por género → sólo fila `Total` en el largo;
  en el ancho anual se muestra en la fila `Ambos géneros` (es un dato territorial).
- **Indicador 10** (brecha): territorial (no gendered); mismo tratamiento que el 4.
- **Indicador 5** (afiliación): **NO** incluido aún — pendiente de los ficheros de
  la Seguridad Social (ver `1_extraccion/fuentes_seg_social/`). El pipeline está
  preparado para incorporarlo sin reescribir la consolidación.
- **Join alquiler↔salario** por **nombre canónico** de CCAA (La Rioja llega de
  Supabase con código de provincia). Excluye Ceuta/Melilla (sin EAES) y el total
  nacional (sin alquiler) → 17 CCAA en el indicador 11.

## Esquema del consolidado largo

`indicador_id, indicador, unidad, territorio_cod, territorio, género, anyo,
trimestre, periodo, periodicidad, t_index, valor, origen, fuente,
flag_missing, flag_outlier`

`origen='real'` en toda la fase 2; `proyeccion` se añadirá en `3_modelado` (§7.6).
