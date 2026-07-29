# Informe QA · Transformación Educación · Canarias en Datos

> **Fecha:** 2026-07-24  ·  **Integridad transformación:** ✅  ·  **Calidad de fuente:** ✅  ·  **global:** 187 filas  ·  **gen:** 561 filas

Tablas: `ced_educacion_global` (clave ccaa×periodo) y `ced_educacion_gen` (ccaa×periodo×género). Marco: **17 CCAA**, periodo **2015-2025**, datos observados (origen=real).

## 1. Resumen de calidad por indicador (tabla global)

| Indicador | Bloque | Unidad | n | NA% | mín | máx |
|---|:-:|:-:|--:|--:|--:|--:|
| `abandono_temprano` | A | % | 187 | 0.0% | 3.6 | 26.8 |
| `nivel_superior_25_34` | A | % | 187 | 0.0% | 31.1 | 68.6 |
| `nivel_bajo_25_64` | A | % | 187 | 0.0% | 20.3 | 57.8 |
| `formacion_adultos_25_64` | A | % | 187 | 0.0% | 7.4 | 19.8 |
| `neet_15_29` | B | % | 187 | 0.0% | 7.2 | 24.2 |
| `idoneidad_15` | C | % | 170 | 9.1% | 56.9 | 89.3 |
| `graduacion_eso` | C | % | 153 | 18.2% | 66.8 | 90.1 |
| `escolarizacion_0_2` | C | % | 170 | 9.1% | 13.6 | 64.4 |
| `gasto_edu_pib` | D | %PIB | 156 | 16.6% | 2.44 | 5.63 |
| `gasto_por_alumno` | D | EUR | 153 | 18.2% | 4591.0 | 12484.0 |

*Interpretación: los NA reflejan distintos años de arranque/cierre por fuente (p. ej. graduación y gasto por alumno terminan en 2023), no fallo técnico.*

## 2. Cobertura y consistencia

- CCAA en global: **17/17**.
- Géneros en gen: **hombres, mujeres, total**.
- Clave única: global sí · gen sí.
- Consistencia global ↔ gen(total): ✅ idénticos.

## 3. Brecha de género (mujeres − hombres, media pp)

| Indicador | Brecha media | Signo esperado | |
|---|--:|:-:|:-:|
| `abandono_temprano` | -6.83 | neg | ✅ |
| `nivel_superior_25_34` | 12.46 | pos | ✅ |
| `nivel_bajo_25_64` | -6.38 | — | — |
| `formacion_adultos_25_64` | 2.94 | — | — |
| `neet_15_29` | 0.73 | — | — |
| `idoneidad_15` | 7.35 | pos | ✅ |
| `graduacion_eso` | 8.89 | pos | ✅ |
| `escolarizacion_0_2` | -0.72 | — | — |

*Patrón esperado: menos abandono/NEET en mujeres (brecha negativa) y más titulación superior, idoneidad y graduación en mujeres (positiva).*

## 4. Sondeo de coherencia · Canarias (global, último dato)

| Indicador | Periodo | Valor |
|---|:-:|--:|
| `abandono_temprano` | 2025 | 15.9 % |
| `nivel_superior_25_34` | 2025 | 43.7 % |
| `nivel_bajo_25_64` | 2025 | 36.3 % |
| `formacion_adultos_25_64` | 2025 | 13.1 % |
| `neet_15_29` | 2025 | 14.3 % |
| `idoneidad_15` | 2024 | 75.4 % |
| `graduacion_eso` | 2023 | 82.8 % |
| `escolarizacion_0_2` | 2024 | 32.3 % |
| `gasto_edu_pib` | 2024 | 4.0653 %PIB |
| `gasto_por_alumno` | 2023 | 8431 EUR |

## 5. Integridad de la transformación

✅ Sin incidencias de integridad: cobertura 17/17 CCAA, clave única en ambas tablas, consistencia global↔gen exacta, sin valores fuera de rango y brechas de género con el signo esperado.

## 6. Avisos de calidad de fuente (aguas arriba)

✅ Sin avisos: los valores de las fuentes están dentro de rangos plausibles.
