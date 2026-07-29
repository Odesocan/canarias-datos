# Estado de extracción — Castilla-La Mancha (`clm`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV/PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `clm-gastosf-csv, clm-tomo-I-resumen-secciones`  
**Portal oficial:** https://transparencia.castillalamancha.es/actuacion/ley-de-presupuestos-generales-de-castilla-la-mancha-2026

## 1 · Fase del proceso

**Extracción consolidada (12/12 años registrados en VERDE).**

- Años en VERDE: **12** (2015–2026)
- Años registrados en `fuentes.yml`: **12** (2015–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 99 | 63.6% | 13/13 |
| 2016 | ✅ Extraído (VERDE) | 99 | 65.7% | 13/13 |
| 2017 | ✅ Extraído (VERDE) | 98 | 66.3% | 13/13 |
| 2018 | ✅ Extraído (VERDE) | 98 | 66.3% | 13/13 |
| 2019 | ✅ Extraído (VERDE) | 99 | 65.7% | 13/13 |
| 2020 | ✅ Extraído (VERDE) | 100 | 66.0% | 13/13 |
| 2021 | ✅ Extraído (VERDE) | 101 | 65.3% | 13/13 |
| 2022 | ✅ Extraído (VERDE) | 111 | 65.8% | 13/13 |
| 2023 | ✅ Extraído (VERDE) | 114 | 64.9% | 13/13 |
| 2024 | ✅ Extraído (VERDE) | 114 | 64.9% | 13/13 |
| 2025 | ✅ Extraído (VERDE) | 113 | 65.5% | 13/13 |
| 2026 | ✅ Extraído (VERDE) | 113 | 65.5% | 13/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 66% de filas con concepto).

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
