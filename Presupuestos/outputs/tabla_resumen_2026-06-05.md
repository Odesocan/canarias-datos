# Tabla resumen — Presupuestos extraídos por anualidad y CCAA

**Fecha:** 2026-06-05 (Noche 16) · ODESOCAN · Canarias en Datos
**Fuente:** capa autonómica (motor Python verificado; regresión parcial de esta noche, ver notas)

Leyenda: ● VERDE (extraído y verificado) · ✗ ERROR (raw no válido) · · sin datos

| CCAA | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Años | Conc. medio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andalucía | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 12 | 12.0 |
| Aragón | ● | ✗ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 11 | 9.9 |
| Asturias | ● | ● | ● | ● | ● | ● | ● | · | ● | ● | ● | ● | 11 | 9.5 |
| Baleares | ● | ● | · | ● | ● | ● | ● | ● | ● | ● | ● | · | 10 | 12.3 |
| Canarias | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 | 12.3 |
| Cataluña | ● | ● | ● | · | ● | ● | · | ● | ● | ● | · | ● | 9 | 13.0 |
| Castilla-La Mancha | · | · | · | · | · | · | · | · | · | ● | ● | ● | 3 | 13.0 |
| Cantabria | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 12.0 |
| Castilla y León | · | · | · | · | · | · | · | · | · | · | · | ● | 1 | 13.0 |
| Extremadura | · | · | · | · | · | · | · | · | · | · | ● | ● | 2 | 13.0 |
| Galicia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 8.0 |
| La Rioja | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 11.0 |
| Madrid | · | · | · | · | · | · | · | · | · | · | · | ● | 1 | 11.0 |
| Murcia | · | · | · | · | · | · | · | · | · | · | ● | · | 1 | 10.0 |
| Navarra | · | · | · | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 | 12.1 |
| País Vasco | · | · | · | · | · | · | · | ● | · | ● | ● | ● | 4 | 8.0 |
| C. Valenciana | · | · | · | · | · | · | · | ● | ● | ● | ● | ● | 5 | 12.6 |
| **TOTAL/año** | **5** | **4** | **4** | **6** | **7** | **7** | **6** | **8** | **8** | **10** | **14** | **12** | **91** | |

## Notas

- **91 ejercicios-año VERDE** (17/17 CCAA) + capa Hacienda 2015–2025. Cobertura de ejercicios sin cambios; **cobertura de conceptos mejorada en 17 cells** esta noche (nueva columna "Conc. medio" = nº medio de conceptos canónicos detectados por ejercicio).
- **Mejoras de la noche (sin tocar ningún extract.py):**
  - **Aragón:** conceptos 8-9 → 9-11 en los 11 ejercicios (gana `salud_mental` vía programa 4133 y `diversidad` vía 3241/keyword); % mapeado +4 a +6 puntos en toda la serie.
  - **Extremadura:** 12 → **13/13 conceptos** en 2025 y 2026.
  - **Canarias:** 2019–2021 suben a **13/13**; resto de la serie +0,5 a +1,5 puntos de % mapeado.
  - **Andalucía** 2024–2026: % mapeado 72,7-73,9 → 75,0.
  - **Galicia 2025:** 78,7 → **80,9 %** — pasa de VERDE pragmático a **VERDE estricto** (criterio ≥80 % del cuaderno).
- **Causa:** fix en `_norm_text` (`ccaa/_common/transform_helpers.py`): ahora elimina diacríticos como prometía el docstring ("INMIGRACIÓN" no matcheaba la keyword `migracion`). Cambio simétrico keywords↔denominaciones; nunca pisa asignaciones por código.
- **Validación:** regresión re-ejecutada en **59 cells** (14 motores distintos): 17 mejoras, 42 idénticas, **0 degradaciones**. Las ~32 cells restantes no se pudieron re-verificar esta noche por fallo I/O del mount del sandbox (deadlocks de lectura en ~570 archivos raw); su código no cambió salvo el fix global → **re-ejecutar `python3 tools/smoke_regresion_py.py` completo en el Mac antes del run matinal**.
- **Único ROJO:** ara/2016 (articulado BOA, sin estados numéricos).
- CCAA delgadas (1 año) sin cambios: cnt, cym, gal, lar, mad, mur — bloqueadas por descarga (sin red en el sandbox).
