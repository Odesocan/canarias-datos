# Estado de extracción — Asturias (`ast`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `ast-distribucion-gasto`  
**Portal oficial:** https://transparencia.asturias.es/web/transparencia/presupuestos

## 1 · Fase del proceso

**Extracción parcial (11/12 años en VERDE).**

- Años en VERDE: **11** (2015–2021, 2023–2026)
- Años registrados en `fuentes.yml`: **12** (2015–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2015 | ✅ Extraído (VERDE) | 107 | 67.3% | 9/13 |
| 2016 | ✅ Extraído (VERDE) | 91 | 70.3% | 9/13 |
| 2017 | ✅ Extraído (VERDE) | 91 | 70.3% | 9/13 |
| 2018 | ✅ Extraído (VERDE) | 90 | 70.0% | 9/13 |
| 2019 | ✅ Extraído (VERDE) | 90 | 70.0% | 9/13 |
| 2020 | ✅ Extraído (VERDE) | 95 | 70.5% | 9/13 |
| 2021 | ✅ Extraído (VERDE) | 96 | 70.8% | 10/13 |
| 2022 | 📥 Raw descargado · extracción pendiente | — | — | — |
| 2023 | ✅ Extraído (VERDE) | 96 | 70.8% | 10/13 |
| 2024 | ✅ Extraído (VERDE) | 104 | 68.3% | 10/13 |
| 2025 | ✅ Extraído (VERDE) | 105 | 68.6% | 10/13 |
| 2026 | ✅ Extraído (VERDE) | 104 | 67.3% | 10/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **10/13** conceptos (mejor año al 71% de filas con concepto).

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
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (3):** `dependencia`, `discapacidad`, `salud_mental`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- **Años registrados sin extraer:** 2022 (raw descargado).

## 4 · Próximos pasos

1. Extraer los raws ya descargados: 2022 (`cd 1_extraccion && python3 -m ccaa --ccaa ast --anio <año> --input ../fuentes/raw/ast/<año>/<f> --output /tmp/t.csv`).
1. Afinar `correspondencias.yml` para intentar capturar: `dependencia`, `discapacidad`, `salud_mental`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
