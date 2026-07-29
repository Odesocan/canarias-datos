# cym — Castilla y León

## Estado: ✅ VERDE Python · 8 ejercicios (2026-06-29)

Años en VERDE: **2016, 2017, 2018, 2021, 2023, 2024, 2025, 2026** (≈85 % concepto,
13/13 conceptos → VERDE estricto). Motor: `cym-jcyl-datosabiertos`.

datosabiertos.jcyl.es sirve el presupuesto de gastos por ejercicio en el recurso CKAN
`1284548037482-<N>.csv`, que en realidad es un **ZIP** (mal etiquetado: el `Content-Type`
real es `application/x-zip-compressed`). **El índice `<N>` NO es el año** — hay que datar
cada recurso por la etiqueta de columna (formatos ricos) o por la fecha interna del ZIP:

| `-N` | año | fichero de gastos dentro del ZIP | formato |
|:---:|:---:|---|---|
| -1 | 2016 | `Dotaciones Presupuesto de Gastos.csv` | CSV `;` latin-1 ⚠️ sin consolidar |
| -2 | 2017 | `Dotaciones Presupuesto de Gastos.csv` | CSV ⚠️ sin consolidar |
| -3 | 2018 | `Dotaciones Presupuesto de Gastos.csv` | CSV ⚠️ sin consolidar |
| -4 | 2021 | `WEB Datos csv gastos.csv` | CSV `;` (consolidado) |
| -5 | 2023 | `Datos abiertos 2023 gastos.XLSX` | XLSX |
| -6 | 2024 | `Ppto. gastos consolidado 2024.xlsx` | XLSX (hoja `Datos`) |
| -7 | 2025 | `Presupuesto. Gastos consolidado.2025.xls` | XLS |
| -8 | 2026 | `Presupuesto de gastos consolidado_2026.xls` | XLS (hoja `DATOS`) |

Todos comparten el código de **subprograma** de 6 caracteres (NNN+L+NN, p. ej. `312A01`
Atención primaria, `322A01` Educ. infantil), por lo que `correspondencias.yml` aplica a
todos los años sin cambios.

El extractor (`extract.py`) es **multi-formato**:
1. Lee el fichero de gastos ya staged en `fuentes/raw/cym/<año>/gastos.{csv,xls,xlsx}`.
2. Detecta esquema (Excel con hoja que tenga `Subprograma`; CSV `;` latin-1 "WEB" o
   "Dotaciones") y localiza la columna de importe (año etiquetado → `PRESUPUESTO` → última).
3. Agrega por subprograma sumando capítulos/económicas; descarta filas-total sin código.
4. Devuelve una fila por subprograma en euros.

## Caveats (ver también `estado_extraccion/09_cym_Castilla_y_León.md`)

- **2016-2018 sin consolidar**: la "Dotaciones" no elimina transferencias internas →
  importes ~25-30 % superiores a 2021+ (caída aparente 2018→2021). No comparables 1:1.
- **2025 ≡ 2026 (prórroga)**: cifras idénticas a nivel de subprograma; difieren de 2024
  en 3 subprogramas. Reales pero no independientes.
- **2019, 2020, 2022**: sin recurso propio en el portal (no fabricar).

## TODO

- Conciliar 2016-2018 contra la base consolidada (capa Hacienda) o localizar una versión
  consolidada de esos años.
- Vigilar si jcyl publica recursos propios para 2019/2020/2022.
