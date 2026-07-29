# Estado de extracción — Navarra (`nav`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `nav-breakdowns-functional`  
**Portal oficial:** https://presupuesto.navarra.es

## 1 · Fase del proceso

**Extracción consolidada (9/9 años registrados en VERDE).**

- Años en VERDE: **9** (2018–2026)
- Años registrados en `fuentes.yml`: **9** (2018–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2018 | ✅ Extraído (VERDE) | 172 | 76.7% | 13/13 |
| 2019 | ✅ Extraído (VERDE) | 167 | 77.2% | 12/13 |
| 2020 | ✅ Extraído (VERDE) | 170 | 76.5% | 12/13 |
| 2021 | ✅ Extraído (VERDE) | 170 | 77.1% | 12/13 |
| 2022 | ✅ Extraído (VERDE) | 170 | 76.5% | 12/13 |
| 2023 | ✅ Extraído (VERDE) | 169 | 76.9% | 12/13 |
| 2024 | ✅ Extraído (VERDE) | 167 | 77.8% | 12/13 |
| 2025 | ✅ Extraído (VERDE) | 168 | 77.4% | 12/13 |
| 2026 | ✅ Extraído (VERDE) | 167 | 77.8% | 12/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 78% de filas con concepto).

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
- **Años sin fuente registrada (2015–2026):** 2015–2017 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015–2017.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
