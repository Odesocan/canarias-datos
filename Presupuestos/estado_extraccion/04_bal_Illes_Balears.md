# Estado de extracción — Illes Balears (`bal`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** HTML · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `bal-frameset-secciones`  
**Portal oficial:** https://pressuposts.caib.es

## 1 · Fase del proceso

**Extracción parcial (10/11 años en VERDE).**

- Años en VERDE: **10** (2015–2016, 2018–2025)
- Años registrados en `fuentes.yml`: **11** (2015–2025)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 54 | 66.7% | 8/13 |
| 2016 | ✅ Extraído (VERDE) | 73 | 50.7% | 11/13 |
| 2017 | 🔗 Fuente registrada · raw pendiente | — | — | — |
| 2018 | ✅ Extraído (VERDE) | 82 | 64.6% | 13/13 |
| 2019 | ✅ Extraído (VERDE) | 86 | 60.5% | 13/13 |
| 2020 | ✅ Extraído (VERDE) | 95 | 58.9% | 13/13 |
| 2021 | ✅ Extraído (VERDE) | 89 | 61.8% | 13/13 |
| 2022 | ✅ Extraído (VERDE) | 143 | 73.4% | 13/13 |
| 2023 | ✅ Extraído (VERDE) | 150 | 75.3% | 13/13 |
| 2024 | ✅ Extraído (VERDE) | 145 | 75.2% | 13/13 |
| 2025 | ✅ Extraído (VERDE) | 141 | 74.5% | 13/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 75% de filas con concepto).

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
- **Años registrados sin extraer:** 2017 (raw pendiente).
- **Años sin fuente registrada (2015–2026):** 2026 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Descargar los raws de años ya registrados: 2017.
1. Añadir a `fuentes.yml` las URLs de: 2026.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
