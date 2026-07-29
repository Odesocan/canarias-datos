# Estado de extracción — Galicia (`gal`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** CSV/HTML · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `gal-csv-abertos-xunta`  
**Portal oficial:** https://transparencia.xunta.gal/es/tema/informacion-economica-orzamentaria-e-estatistica/orzamentos

## 1 · Fase del proceso

**Extracción parcial (1/2 años en VERDE).**

- Años en VERDE: **1** (2025)
- Años registrados en `fuentes.yml`: **2** (2025–2026)

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos |
|-----|------|:----:|:----:|:----:|
| 2025 | ✅ Extraído (VERDE) | 47 | 80.9% | 8/13 |
| 2026 | 📥 Raw descargado · extracción pendiente | — | — | — |

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **8/13** conceptos (mejor año al 81% de filas con concepto).

| Concepto | Estado |
|----------|:------:|
| Sanidad (`sanidad`) | ✅ capturado |
| Educación (`educacion`) | ✅ capturado |
| Soberanía (alimentaria/agraria) (`soberania`) | ✅ capturado |
| Dirección y gobernanza (`direccion`) | ✅ capturado |
| Vivienda (`vivienda`) | ✅ capturado |
| Empleo (`empleo`) | ✅ capturado |
| I+D+i (`idi`) | ❌ ausente |
| Dependencia (`dependencia`) | ✅ capturado |
| Discapacidad (`discapacidad`) | ❌ ausente |
| Salud mental (`salud_mental`) | ❌ ausente |
| Diversidad (LGTBI) (`diversidad`) | ✅ capturado |
| Turismo (`turismo`) | ❌ ausente |
| Igualdad (`igualdad`) | ❌ ausente |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (5):** `idi`, `discapacidad`, `salud_mental`, `turismo`, `igualdad`.
  Revisar si la clasificación funcional de la fuente los desglosa o si hay que ampliar `codigos`/`keywords` en `correspondencias.yml`.
- **Años registrados sin extraer:** 2026 (raw descargado).
- **Años sin fuente registrada (2015–2026):** 2015–2024 — falta añadir URL a `fuentes.yml`.

## 4 · Próximos pasos

1. Extraer los raws ya descargados: 2026 (`cd 1_extraccion && python3 -m ccaa --ccaa gal --anio <año> --input ../fuentes/raw/gal/<año>/<f> --output /tmp/t.csv`).
1. Añadir a `fuentes.yml` las URLs de: 2015–2024.
1. Afinar `correspondencias.yml` para intentar capturar: `idi`, `discapacidad`, `salud_mental`, `turismo`, `igualdad`.

---
*Generado automáticamente desde `outputs/smoke_regresion_py.csv` y `fuentes.yml` (2026-06-29).*
