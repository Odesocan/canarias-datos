# Estado de extracción — Cantabria (`cnt`)

**Proyecto:** Presupuestos · ODESOCAN / Canarias en Datos  
**Capa:** autonómica · **Formato fuente:** PDF · **Actualizado:** 2026-06-29  
**Motor(es) de extracción:** `cnt-total-programa-suma-servicios`  
**Portal oficial:** https://www.cantabria.es/web/direccion-general-presupuestos

## 1 · Fase del proceso

**Serie completa 2015-2026 en VERDE_PRAGM (12/12).**

- Todos los años a nivel **programa**, 12/13 conceptos.
- 2015-2017 vía el "Anexo de Desarrollo Económico de Gasto por Centros Gestores"
  (motor `cnt-centros-suma-capitulos`); 2018-2026 vía el "Estado de Ingresos y Gastos"
  (motor `cnt-total-programa-suma-servicios`).

| Año | Estado | Motor | Filas | %conc | Conc | sanidad |
|-----|--------|-------|:----:|:----:|:----:|:----:|
| 2015 | ✅ VERDE_PRAGM | `cnt-centros-suma-capitulos` | 83 | 54.2% | 12 | 0.766 |
| 2016 | ✅ VERDE_PRAGM | `cnt-centros-suma-capitulos` | 84 | 54.8% | 12 | 0.787 |
| 2017 | ✅ VERDE_PRAGM | `cnt-centros-suma-capitulos` | 84 | 54.8% | 12 | 0.805 |
| 2018–2026 | ✅ VERDE_PRAGM | `cnt-total-programa-suma-servicios` | 84–91 | 52–55% | 12 | 0.823→1.269 |

Serie de sanidad continua y monótona 2015→2026 (0.766 → 1.269 mil M€).

Pipeline: `descubrir fuente → descargar raw → extraer/parsear → mapear conceptos → cargar DB`.

| Año | Fase | Filas | % concepto | Conceptos | Total (mil M€) |
|-----|------|:----:|:----:|:----:|:----:|
| 2018 | ✅ VERDE_PRAGM | 84 | 54.8% | 12/13 | 2.74 |
| 2019 | ✅ VERDE_PRAGM | 85 | 55.3% | 12/13 | 2.86 |
| 2020 | ✅ VERDE_PRAGM | 85 | 51.8% | 12/13 | 2.90 |
| 2021 | ✅ VERDE_PRAGM | 85 | 51.8% | 12/13 | 3.09 |
| 2022 | ✅ VERDE_PRAGM | 91 | 52.7% | 12/13 | 3.35 |
| 2023 | ✅ VERDE_PRAGM | 91 | 52.7% | 12/13 | 3.52 |
| 2024 | ✅ VERDE_PRAGM | 89 | 53.9% | 12/13 | 3.56 |
| 2025 | ✅ VERDE_PRAGM | 88 | 53.4% | 12/13 | 3.79 |
| 2026 | ✅ VERDE_PRAGM | 91 | 54.9% | 12/13 | 3.97 |

Magnitudes coherentes (sanidad 0,82→1,27 mil M€; serie monótona sin saltos), acordes a
una comunidad de ~580 000 habitantes.

## 2 · Conceptos extraídos (objetivo: 13)

Cobertura máxima alcanzada: **12/13** conceptos (mejor año al 55% de filas con concepto).

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
| Diversidad (LGTBI) (`diversidad`) | ❌ ausente |
| Turismo (`turismo`) | ✅ capturado |
| Igualdad (`igualdad`) | ✅ capturado |

## 3 · Categorías faltantes para el resultado óptimo

- **Conceptos nunca capturados (1):** `diversidad` (Cantabria no lo desglosa como programa
  propio; revisar `keywords` en `correspondencias.yml`).
- **Años sin tomo de gastos (2015-2017):** la URL conocida es el texto legal del BOC, no el
  Estado de Gastos por programa. Falta localizar el tomo correcto en cantabria.es.

## 4 · Próximos pasos

1. Localizar el **Tomo "Estado de Gastos" por programa de 2015, 2016 y 2017** (la Ley del
   BOC no sirve para el motor).
2. Afinar `correspondencias.yml` para intentar capturar `diversidad`.

## 5 · Revisión / test de bugs (2026-06-29)

Ampliación de 1 → 9 ejercicios (2018-2026) y auditoría del motor `cnt-total-programa-suma-servicios`.

**Verificado OK:**
- Motor robusto: pdftotext NO lee estos PDF (0 chars) → cae a pdfplumber (lento, ~450 pags);
  acumula `TOTAL PROGRAMA` por código sumando servicios. 84-91 programas/año.
- Magnitudes monótonas y plausibles (total 2,74 → 3,97 mil M€ 2018-2026).

**🐛 BUG ENCONTRADO Y CORREGIDO — slot 2025 contenía datos de 2026.** El `fuentes.yml`
tenía el ejercicio **2025 apuntando a la URL del 2026** ("2º INGRESOS Y GASTOS DEFINITIVA"),
y el raw en disco `cnt/2025/ingresos_gastos.pdf` era el **Proyecto 2026** (portada "2º
PROYECTO ... 2026"). La fila VERDE de 2025 del catálogo estaba calculada sobre datos de
2026 (total 3,97 en vez de 3,79). Corregido: `fuentes.yml` 2025 → su URL real
(`02.- ESTADO DE INGRESOS Y GASTOS.pdf`), raw sustituido (el erróneo queda como
`_ERRONEO_era_2026_*.bak`), 2025 re-extraído (88 filas, total 3,79, encaja entre 2024 y 2026).

**2015/2016/2017 — RESUELTO A VERDE (2026-06-29).** Primero se intentó la Ley del BOC, que
solo trae la tabla "Política de Gasto" (área 2-díg, 19 filas → AMARILLO). Después el usuario
aportó el **"Anexo de Desarrollo Económico de Gasto por Centros Gestores"**, que SÍ tiene el
desglose por programa (NNNX) — sin línea `TOTAL PROGRAMA`, pero con `TOTAL CAPÍTULO:` por
capítulo. Se añadió la rama **`cnt-centros-suma-capitulos`** (suma los `TOTAL CAPÍTULO` por
programa; solo se activa cuando no hay `TOTAL PROGRAMA`, no toca 2018-2026). Resultado:
83-84 programas/año, 12 conceptos, **VERDE_PRAGM**. Totales 2.453/2.417/2.561 mil M€,
sanidad continua con 2018. El fallback política (`cnt-politica-gastos-boc`) queda como
respaldo si solo hubiera la Ley.

URLs de los anexos (patrón `documents/16870/<carpeta>/Anexo...CENTROS+GESTORES.pdf`):
2015 → carpeta 3151201; 2016 → 3601314 (nombre sin '+de+'); 2017 → 4625307.

---
*Revisado a mano (review + test de bugs) el 2026-06-29. Foto de regresión en
`outputs/smoke_regresion_py.csv`.*
