# Estado de extracción — Región de Murcia (`mur`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** HTML · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `mur-html`  
**Portal oficial:** https://www.carm.es/chac/presupuestos2025/movil/index.html

## 1 · Fase del proceso

**Extracción consolidada (1/1 años registrados en VERDE).**

- Años en VERDE: **1** (2025)
- Años registrados en `fuentes.yml`: **1** (2025)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2025 | ✅ Extraído (VERDE) | 106 | 86.8% | 10/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **10/13** conceptos (mejor año al 87% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ✅ capturado |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ❌ ausente |
| I+D+i (`idi`) | ✅ capturado |
| Dependencia (`dependencia`) | ✅ capturado |
| Discapacidad (`discapacidad`) | ✅ capturado |
| Salud mental (`salud_mental`) | ✅ capturado |
| Diversidad (LGTBI) (`diversidad`) | ❌ ausente |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ❌ ausente |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (3):** `empleo`, `diversidad`, `igualdad`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- **Años sin fuente registrada (2015–2026):** 2015–2024, 2026 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015–2024, 2026.
1. Afinar `correspondencias.yml` para intentar capturar: `empleo`, `diversidad`, `igualdad`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
