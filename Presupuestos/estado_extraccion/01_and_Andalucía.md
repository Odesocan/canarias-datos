# Estado de extracción — Andalucía (`and`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV/PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `and-ckan-csv, and-resumen-cap-prog`  
**Portal oficial:** https://www.juntadeandalucia.es/datosabiertos/portal/dataset?tags=presupuestos

## 1 · Fase del proceso

**Extracción consolidada (12/12 años registrados en VERDE).**

- Años en VERDE: **12** (2015–2026)
- Años registrados en `fuentes.yml`: **12** (2015–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 114 | 70.2% | 12/13 |
| 2016 | ✅ Extraído (VERDE) | 115 | 67.8% | 12/13 |
| 2017 | ✅ Extraído (VERDE) | 102 | 72.5% | 12/13 |
| 2018 | ✅ Extraído (VERDE) | 102 | 72.5% | 12/13 |
| 2019 | ✅ Extraído (VERDE) | 103 | 72.8% | 12/13 |
| 2020 | ✅ Extraído (VERDE) | 111 | 66.7% | 12/13 |
| 2021 | ✅ Extraído (VERDE) | 112 | 66.1% | 12/13 |
| 2022 | ✅ Extraído (VERDE) | 97 | 69.1% | 12/13 |
| 2023 | ✅ Extraído (VERDE) | 88 | 73.9% | 12/13 |
| 2024 | ✅ Extraído (VERDE) | 88 | 75.0% | 12/13 |
| 2025 | ✅ Extraído (VERDE) | 88 | 75.0% | 12/13 |
| 2026 | ✅ Extraído (VERDE) | 88 | 75.0% | 12/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **12/13** conceptos (mejor año al 75% de filas con concepto).

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
| Salud mental (`salud_mental`) | ❌ ausente |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (1):** `salud_mental`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.

## 4 · Próximos pasos

1. Afinar `correspondencias.yml` para intentar capturar: `salud_mental`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
