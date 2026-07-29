# Estado de extracción — País Vasco (`pvc`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `pvc-csv-tidy`  
**Portal oficial:** https://www.euskadi.eus/gobierno-vasco/contenidos/informacion/presupuestos_cae_fich/es_def/index.shtml

## 1 · Fase del proceso

**Extracción consolidada (4/4 años registrados en VERDE).**

- Años en VERDE: **4** (2022, 2024–2026)
- Años registrados en `fuentes.yml`: **4** (2022, 2024–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2022 | ✅ Extraído (VERDE) | 116 | 44.0% | 8/13 |
| 2024 | ✅ Extraído (VERDE) | 118 | 44.1% | 8/13 |
| 2025 | ✅ Extraído (VERDE) | 122 | 44.3% | 8/13 |
| 2026 | ✅ Extraído (VERDE) | 122 | 43.4% | 8/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **8/13** conceptos (mejor año al 44% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ✅ capturado |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ✅ capturado |
| I+D+i (`idi`) | ✅ capturado |
| Dependencia (`dependencia`) | ❌ ausente |
| Discapacidad (`discapacidad`) | ❌ ausente |
| Salud mental (`salud_mental`) | ❌ ausente |
| Diversidad (LGTBI) (`diversidad`) | ❌ ausente |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ❌ ausente |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (5):** `dependencia`, `discapacidad`, `salud_mental`, `diversidad`, `igualdad`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- **Años sin fuente registrada (2015–2026):** 2015–2021, 2023 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015–2021, 2023.
1. Afinar `correspondencias.yml` para intentar capturar: `dependencia`, `discapacidad`, `salud_mental`, `diversidad`, `igualdad`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
