# Estado de extracción — Extremadura (`ext`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `ext-tomo-eig-suma-capitulos`  
**Portal oficial:** https://www.asambleaex.es/

## 1 · Fase del proceso

**Extracción consolidada (2/2 años registrados en VERDE).**

- Años en VERDE: **2** (2025–2026)
- Años registrados en `fuentes.yml`: **2** (2025–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2025 | ✅ Extraído (VERDE) | 74 | 68.9% | 13/13 |
| 2026 | ✅ Extraído (VERDE) | 73 | 72.6% | 13/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 73% de filas con concepto).

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
- **Años sin fuente registrada (2015–2026):** 2015–2024 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015–2024.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
