# Estado de extracción — Castilla y León (`cym`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV/XLS/XLSX · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `cym-jcyl-datosabiertos`  
**Portal oficial:** https://datosabiertos.jcyl.es/web/jcyl/set/es/hacienda/presupuestos/1284548037482

## 1 · Fase del proceso

**Extracción consolidada (8/8 años registrados en VERDE).**

- Años en VERDE: **8** (2016–2018, 2021, 2023–2026)
- Años registrados en `fuentes.yml`: **8** (2016–2018, 2021, 2023–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2016 | ✅ Extraído (VERDE) | 103 | 85.4% | 13/13 |
| 2017 | ✅ Extraído (VERDE) | 102 | 85.3% | 13/13 |
| 2018 | ✅ Extraído (VERDE) | 102 | 85.3% | 13/13 |
| 2021 | ✅ Extraído (VERDE) | 104 | 85.6% | 13/13 |
| 2023 | ✅ Extraído (VERDE) | 107 | 86.0% | 13/13 |
| 2024 | ✅ Extraído (VERDE) | 104 | 85.6% | 13/13 |
| 2025 | ✅ Extraído (VERDE) | 103 | 85.4% | 13/13 |
| 2026 | ✅ Extraído (VERDE) | 103 | 85.4% | 13/13 |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **13/13** conceptos (mejor año al 86% de filas con concepto).

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
- ⚠️ **Aviso de calidad:** 2016-2018 sin consolidar (~+30 % sobre el dato homogéneo); 2025≡2026 es prórroga repetida; 2019/2020/2022 sin fuente.
- **Años sin fuente registrada (2015–2026):** 2015, 2019–2020, 2022 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Añadir a `fuentes.yml` las URLs de: 2015, 2019–2020, 2022.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
