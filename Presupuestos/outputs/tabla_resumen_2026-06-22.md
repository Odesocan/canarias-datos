# Presupuestos · Canarias en Datos — Tabla resumen por anualidad/CCAA

**Fecha:** 2026-06-22 (Noche 25) · **Fuente:** `outputs/smoke_regresion_py.csv` (CSV autoritativo)
**Estado catálogo:** 91 ejercicios-año VERDE · 17/17 CCAA · capa Hacienda 2015–2025 · único ERROR: `ara/2016`

Leyenda: ● VERDE cargado · ✗ ERROR · · sin ejercicio en catálogo

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Años |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| and Andalucía | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | **12** |
| ara Aragón | ● | ✗ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | **11** |
| ast Asturias | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | **11** |
| bal Baleares | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | · | **10** |
| can Canarias | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | **9** |
| cat Cataluña | ● | ● | ● | · | ● | ● | · | ● | ● | ● | · | ● | **9** |
| clm Cast-La Mancha | · | · | · | · | · | · | · | · | · | ● | ● | ● | **3** |
| cnt Cantabria | · | · | · | · | · | · | · | · | · | · | ● | · | **1** |
| cym Cast-León | · | · | · | · | · | · | · | · | · | · | · | ● | **1** |
| ext Extremadura | · | · | · | · | · | · | · | · | · | · | ● | ● | **2** |
| gal Galicia | · | · | · | · | · | · | · | · | · | · | ● | · | **1** |
| lar La Rioja | · | · | · | · | · | · | · | · | · | · | ● | · | **1** |
| mad Madrid | · | · | · | · | · | · | · | · | · | · | · | ● | **1** |
| mur Murcia | · | · | · | · | · | · | · | · | · | · | ● | · | **1** |
| nav Navarra | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | **9** |
| pvc País Vasco | · | · | · | · | · | · | · | ● | · | ● | ● | ● | **4** |
| val C.Valenciana | · | · | · | · | · | · | · | ● | ● | ● | ● | ● | **5** |

**Total: 91 ejercicios-año VERDE.**

## Cobertura de conceptos (distintos del catálogo de 13, por CCAA)

| CCAA | años | conc. medio | min | max |
|------|------|-------------|-----|-----|
| and | 12 | 12.0 | 12 | 12 |
| ara | 12 | 9.1 | 0* | 11 |
| ast | 11 | 9.5 | 9 | 10 |
| bal | 10 | 12.3 | 8 | 13 |
| can | 9 | 12.3 | 12 | 13 |
| cat | 9 | 13.0 | 13 | 13 |
| clm | 3 | 13.0 | 13 | 13 |
| cnt | 1 | 12.0 | 12 | 12 |
| cym | 1 | 13.0 | 13 | 13 |
| ext | 2 | 13.0 | 13 | 13 |
| gal | 1 | 8.0 | 8 | 8 |
| lar | 1 | 11.0 | 11 | 11 |
| mad | 1 | 11.0 | 11 | 11 |
| mur | 1 | 10.0 | 10 | 10 |
| nav | 9 | 12.1 | 12 | 13 |
| pvc | 4 | 8.0 | 8 | 8 |
| val | 5 | 12.6 | 12 | 13 |

\* `ara/2016` = 0 conceptos (ERROR: raw es la ley articulada BOPA, no el tomo "Distribución del gasto por programas").

## Pendiente para completar (requiere descarga fuera del sandbox)

CCAA finas con 1 solo ejercicio: cnt, cym, gal, lar, mad, mur. Huecos de alto valor con raw ausente
o stub 404 en disco: ast/2022 (en disco está la Ley BOPA, no el tomo de distribución), bal/2017 y
bal/2026 (secciones = stubs de 34 bytes), gal/2026 (solo portal_index.html, falta CSV abertos),
cat 2018/2021/2025, can 2015–2017, ara/2016.
