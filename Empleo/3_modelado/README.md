# Fase 3 · Modelado / Proyección — Sección Empleo

**Canarias en Datos · ODESOCAN** · Implementación en **Python** de `3_modelado`
(§9 del cuaderno). Proyecta los indicadores del consolidado
(`2_transformacion/ced_empleo`) **hasta el final de 2026** mediante una
competición de algoritmos de series temporales.

Réplica del patrón multi-algoritmo de las demás secciones (`modelado.R` de
Dependencia/Vivienda/Salud mental), adaptado a Python y a las métricas pedidas.

## Cómo funciona

1. **Competición de algoritmos** (`statsforecast`, Nixtla + `prophet`, Meta):
   - *Con estimadores*: **AutoARIMA**, **AutoETS**, **AutoTheta**, **Prophet**.
   - *Sin estimadores* (líneas base): **Naive**, **SeasonalNaive**,
     **RandomWalkWithDrift**, **WindowAverage**, **HistoricAverage**.
2. **Validación cruzada temporal rolling-origin** (1 paso adelante):
   4 folds en series trimestrales, 3 en anuales. Se calculan **MAPE, MAE**,
   RMSE y NMAE por serie·modelo.
3. **Selección por serie** minimizando **MAPE y MAE**, con **regla de
   parsimonia**: si varios modelos quedan dentro del 5 % del mejor, gana el
   **más simple** (navaja de Occam) — no sólo el más preciso.
4. **Proyección** hasta 2026 refitteando el modelo elegido y marcando cada fila
   con la bandera `origen` (`real` / `proyeccion`, §7.6).
   - trimestrales (EPA/ETCL, acaban 2026T1) → 2026T2, T3, T4.
   - anuales (EAES/alquiler, acaban 2024)   → 2025, 2026.

Series con menos de `min_puntos` observaciones no se modelan y su proyección
queda **sin valor** (§9). Con los datos actuales, todas superan el mínimo.

## Ejecutar

```bash
cd 3_modelado
pip install statsforecast          # requiere statsforecast (Nixtla)
python modelado.py
python validacion.py
```

## Salidas

| Fichero | Contenido |
|---|---|
| `ced_empleo.csv` / `.parquet` | consolidado **real + proyección** con bandera `origen` y columna `algoritmo` |
| `seleccion_algoritmo_proyeccion_global.csv` | ranking de algoritmos (NMAE/MAPE medios, series ganadas) |
| `seleccion_algoritmo_proyeccion_variables.csv` | error por indicador·algoritmo |
| `seleccion_algoritmo_proyeccion_series.csv` | modelo elegido por serie + si aplicó parsimonia |
| `manifiesto_modelado.json` | resumen de la ejecución |

## Decisiones (científico social computacional)

- **Métrica de selección = MAPE + MAE** (petición), con NMAE como criterio
  scale-free para comparar/agregar entre indicadores de magnitudes distintas.
- **Selección por serie** (no un único algoritmo global) porque cada indicador ×
  territorio × género tiene dinámica propia (una tasa estacional de la EPA no se
  comporta como un ratio salarial anual). El algoritmo global de referencia se
  reporta igualmente (convención del proyecto).
- **Parsimonia**: en estas series cortas y ruidosas, los modelos simples
  (SeasonalNaive, drift) a menudo igualan o superan a ARIMA/ETS; preferirlos
  reduce el riesgo de sobreajuste. Se documenta en cuántas series decidió.
- **Prophet** (Meta) está **incluido** en la competición (`prophet_model.py`),
  con la misma CV rolling-origin. Es lento (un ajuste por serie·fold) → su
  resultado se cachea aparte en `.cache_cv/prophet_*`. Se desactiva con
  `INCLUIR_PROPHET = False` en `config.py`.
- **RF/XGBoost** (del inventario del cuaderno) se omiten: con series
  univariantes tan cortas, la parsimonia desaconseja su complejidad. Añadibles.

## Esquema de salida (añade a `ced_empleo`)

`… , origen, algoritmo, modelo_mape, modelo_mae, aplico_parsimonia`

`origen='real'` en las observaciones; `origen='proyeccion'` en lo proyectado.
