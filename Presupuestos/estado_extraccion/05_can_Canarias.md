# Estado de extracción — Canarias (`can`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `can-tomo3-resumen-programas`  
**Portal oficial:** https://www.gobiernodecanarias.org/hacienda/planificacionypresupuesto/

## 1 · Fase del proceso

**Extracción consolidada (12/12 años registrados en VERDE).**

- Años en VERDE: **12** (2015–2026)
- Años registrados en `fuentes.yml`: **12** (2015–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 139 | 65.5% | 12/13 |
| 2016 | ✅ Extraído (VERDE) | 140 | 66.4% | 12/13 |
| 2017 | ✅ Extraído (VERDE) | 141 | 65.2% | 12/13 |
| 2018 | ✅ Extraído (VERDE) | 140 | 66.4% | 12/13 |
| 2019 | ✅ Extraído (VERDE) | 142 | 66.9% | 13/13 |
| 2020 | ✅ Extraído (VERDE) | 144 | 66.7% | 13/13 |
| 2021 | ✅ Extraído (VERDE) | 141 | 66.7% | 13/13 |
| 2022 | ✅ Extraído (VERDE) | 135 | 65.2% | 12/13 |
| 2023 | ✅ Extraído (VERDE) | 135 | 65.2% | 12/13 |
| 2024 | ✅ Extraído (VERDE) | 140 | 65.0% | 12/13 |
| 2025 | ✅ Extraído (VERDE) | 141 | 66.0% | 12/13 |
| 2026 | ✅ Extraído (VERDE) | 143 | 65.7% | 12/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 67% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ✅ capturado |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ✅ capturado |
| I+D+i (`idi`) | ✅ capturado |
| Dependencia (`dependencia`) | ✅ capturado |
| Discapacidad (`discapacidad`) | ✅ capturado |
| Salud mental (`salud_mental`) | ✅ capturado |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Cobertura conceptual completa (13/13).** Ningún concepto del catálogo falta.

## 4 · Próximos pasos

1. Serie completa y conceptos al máximo alcanzable: mantener (no reescribir el motor en VERDE).

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
