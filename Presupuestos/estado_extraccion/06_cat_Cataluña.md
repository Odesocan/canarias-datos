# Estado de extracción — Cataluña (`cat`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `cat-programa-suma-secciones, cat-programa-totals`  
**Portal oficial:** https://aplicacions.economia.gencat.cat/wpres/

## 1 · Fase del proceso

**Extracción consolidada (9/9 años registrados en VERDE).**

- Años en VERDE: **9** (2015–2017, 2019–2020, 2022–2024, 2026)
- Años registrados en `fuentes.yml`: **9** (2015–2017, 2019–2020, 2022–2024, 2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 96 | 66.7% | 13/13 |
| 2016 | ✅ Extraído (VERDE) | 103 | 64.1% | 13/13 |
| 2017 | ✅ Extraído (VERDE) | 103 | 64.1% | 13/13 |
| 2019 | ✅ Extraído (VERDE) | 105 | 63.8% | 13/13 |
| 2020 | ✅ Extraído (VERDE) | 105 | 63.8% | 13/13 |
| 2022 | ✅ Extraído (VERDE) | 105 | 63.8% | 13/13 |
| 2023 | ✅ Extraído (VERDE) | 105 | 63.8% | 13/13 |
| 2024 | ✅ Extraído (VERDE) | 105 | 63.8% | 13/13 |
| 2026 | ✅ Extraído (VERDE) | 106 | 63.2% | 13/13 |

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
- **Años sin fuente registrada (2015–2026):** 2018, 2021, 2025 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2018, 2021, 2025.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
