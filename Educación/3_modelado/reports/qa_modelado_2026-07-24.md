# Informe QA · Modelado (proyección a 2026) · Educación · Canarias en Datos

> **Fecha:** 2026-07-24  ·  **Integridad:** ✅  ·  **Horizonte:** 2015-2026  ·  **global:** 204 filas  ·  **gen:** 612 filas

Algoritmos en competición: base (media, naive, deriva, lineal, ETS, ARIMA) + avanzados (Prophet, RandomForest, XGBoost=no (falta libomp)). Selección por MAPE con regla de parsimonia (el modelo más simple dentro del 15% del mejor MAPE; escalado a avanzados solo si el mejor base supera 10% de MAPE).

## 1. Parsimonia · modelos elegidos

| Modelo | Complejidad | Nº series | % |
|---|:-:|--:|--:|
| `naive` | 0 | 230 | 54% |
| `lineal` | 1 | 87 | 20% |
| `deriva` | 1 | 52 | 12% |
| `media` | 0 | 37 | 9% |
| `ets` | 2 | 11 | 3% |
| `arima` | 3 | 6 | 1% |
| `rf` | 5 | 2 | 0% |

**96% de las series se proyectan con estimadores simples** (complejidad ≤ 1). Solo 106 series escalaron a evaluar modelos avanzados. Prophet no fue seleccionado en ninguna serie: para series anuales cortas los modelos parsimoniosos igualan o superan a los complejos.

## 2. Reparto real vs proyección, y error de validación (por indicador)

| Indicador | reales | proyectadas | % proy | MAPE_CV (mediana) | MAE_CV |
|---|--:|--:|--:|--:|--:|
| `abandono_temprano` | 555 | 57 | 9.3% | 13.9% | 1.68 |
| `nivel_superior_25_34` | 561 | 51 | 8.3% | 4.5% | 2.33 |
| `nivel_bajo_25_64` | 561 | 51 | 8.3% | 3.3% | 1.11 |
| `formacion_adultos_25_64` | 561 | 51 | 8.3% | 7.7% | 1.13 |
| `neet_15_29` | 561 | 51 | 8.3% | 12.3% | 1.62 |
| `idoneidad_15` | 510 | 102 | 16.7% | 1.9% | 1.46 |
| `graduacion_eso` | 459 | 153 | 25.0% | 1.8% | 1.53 |
| `escolarizacion_0_2` | 510 | 102 | 16.7% | 8.5% | 3.44 |
| `gasto_edu_pib` | 156 | 32 | 17.0% | — | — |
| `gasto_por_alumno` | 153 | 51 | 25.0% | 2.8% | 203.70 |

*9 series individuales superan el 25% de MAPE (CCAA pequeñas con series ruidosas, sobre todo por sexo); su proyección es indicativa.*

## 3. Plausibilidad y conservación de la brecha de género (2026)

| Indicador | Brecha 2026 (M−H) | Esperado | |
|---|--:|:-:|:-:|
| `abandono_temprano` | -6.4 pp | neg | ✅ |
| `nivel_superior_25_34` | 11.73 pp | pos | ✅ |
| `idoneidad_15` | 5.6 pp | pos | ✅ |
| `graduacion_eso` | 7.03 pp | pos | ✅ |

NA restantes en global: `gasto_edu_pib` (16) — años fuera de la cobertura de la fuente (no modelados).

## 4. Proyección · Canarias 2026 (global, con modelo elegido)

| Indicador | Valor 2026 | Modelo |
|---|--:|:-:|
| `abandono_temprano` | 15.9 % | `naive` |
| `nivel_superior_25_34` | 43.7 % | `naive` |
| `nivel_bajo_25_64` | 35 % | `deriva` |
| `formacion_adultos_25_64` | 13.1 % | `naive` |
| `neet_15_29` | 14.3 % | `naive` |
| `idoneidad_15` | 78.3556 % | `deriva` |
| `graduacion_eso` | 82.8 % | `naive` |
| `escolarizacion_0_2` | 35.5994 % | `lineal` |
| `gasto_edu_pib` | 3.9552 %PIB | `presupuestos` |
| `gasto_por_alumno` | 9679.38 EUR | `deriva` |

## 5. Integridad del modelado

✅ Sin incidencias: panel 2015-2026 completo (17 CCAA × 12 años), proyecciones dentro del rango de la unidad y brechas de género con el signo esperado en 2026.

## 6. Avisos (confianza de la proyección)

- ⚠️ 9 series con MAPE_CV > 25% (proyección de baja confianza; series ruidosas/CCAA pequeñas)
