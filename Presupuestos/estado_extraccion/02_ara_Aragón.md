# Estado de extracción — Aragón (`ara`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `ara-pdf-program-total`  
**Portal oficial:** https://www.aragon.es/es/transparencia/economia-presupuestos/presupuestos-de-la-comunidad-autonoma-de-aragon

## 1 · Fase del proceso

**Extracción parcial (11/12 años en VERDE).**

- Años en VERDE: **11** (2015, 2017–2026)
- Años registrados en `fuentes.yml`: **12** (2015–2026)
- Años en ERROR: 2016

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 163 | 59.5% | 9/13 |
| 2016 | ❌ Error de extracción | — | — | — |
| 2017 | ✅ Extraído (VERDE) | 167 | 58.7% | 9/13 |
| 2018 | ✅ Extraído (VERDE) | 160 | 60.6% | 9/13 |
| 2019 | ✅ Extraído (VERDE) | 160 | 60.6% | 9/13 |
| 2020 | ✅ Extraído (VERDE) | 166 | 56.0% | 10/13 |
| 2021 | ✅ Extraído (VERDE) | 187 | 56.7% | 10/13 |
| 2022 | ✅ Extraído (VERDE) | 182 | 57.7% | 10/13 |
| 2023 | ✅ Extraído (VERDE) | 182 | 57.7% | 10/13 |
| 2024 | ✅ Extraído (VERDE) | 198 | 58.1% | 11/13 |
| 2025 | ✅ Extraído (VERDE) | 198 | 58.1% | 11/13 |
| 2026 | ✅ Extraído (VERDE) | 198 | 58.1% | 11/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **11/13** conceptos (mejor año al 61% de filas con concepto).

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
| Salud mental (`salud_mental`) | ✅ capturado |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (2):** `dependencia`, `discapacidad`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- ⚠️ **Aviso de calidad:** 2016 en ERROR: el raw es la Ley BOPA (texto), no la tabla programa+total.
- **Años en ERROR (raw incorrecto):** 2016 — re-localizar el documento programa+total.

## 4 · Próximos pasos

1. Sustituir el raw de 2016 por el tomo de programa+total correcto.
1. Afinar `correspondencias.yml` para intentar capturar: `dependencia`, `discapacidad`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
