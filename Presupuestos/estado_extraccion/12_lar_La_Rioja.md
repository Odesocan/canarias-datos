# Estado de extracción — La Rioja (`lar`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `lar-camelot-funcional-economico`  
**Portal oficial:** https://www.larioja.org/hacienda/es/presupuestos-generales

## 1 · Fase del proceso

**Extracción consolidada (1/1 años registrados en VERDE).**

- Años en VERDE: **1** (2025)
- Años registrados en `fuentes.yml`: **1** (2025)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2025 | ✅ Extraído (VERDE) | 56 | 76.8% | 11/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **11/13** conceptos (mejor año al 77% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ❌ ausente |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ✅ capturado |
| I+D+i (`idi`) | ✅ capturado |
| Dependencia (`dependencia`) | ✅ capturado |
| Discapacidad (`discapacidad`) | ✅ capturado |
| Salud mental (`salud_mental`) | ✅ capturado |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ❌ ausente |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (2):** `soberania`, `turismo`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- **Años sin fuente registrada (2015–2026):** 2015–2024, 2026 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015–2024, 2026.
1. Afinar `correspondencias.yml` para intentar capturar: `soberania`, `turismo`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
