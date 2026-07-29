# Limitaciones conocidas — País Vasco (pvc)

> Advertencias de la extracción de País Vasco. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `pvc-gastosc-funcional` (ZIP `AdErAu_c.zip` → GASTOSC.CSV, 2015-2021) y `pvc-csv-tidy` (`Datuak_datos.csv`, 2022-2026); ambos + `pvc-transform`. · Años: 2015-2026 · Estado global: 12/12 VERDE_PRAGM (~43-46 %, 8 conceptos).

## Perímetro / decisiones de consolidación
- **Perímetro AdErAu = Administración General + Organismos Autónomos, CONSOLIDADO.** Los ZIP 2015-2021 ya vienen consolidados (instituciones 00100 + 002xx, sólo gastos). Para 2022-2026 el `Datuak_datos.csv` trae TODO el sector público vasco, así que el motor **FILTRA** para reproducir ese mismo perímetro:
  - `Tipo Presupuesto == "1"` → sólo **gasto** (descarta ingresos, tipo 2).
  - `Entidad == "100"` o empieza por `"2"` → sólo Admin General + OO.AA.
  - Verificado: 2021 (ZIP) 13,58 B€ ≈ 2022 (tidy filtrado) 13,54 B€ → serie continua.
- Clasificación **funcional** por PROGRAMA de 4 dígitos; concepto por prefijo de función (`41*`→sanidad, `42*`→educacion, `71*`→soberania, `11/12/13*`→direccion, `43*`→vivienda, `321*`+`3231`→empleo, `54*`→idi, `75*`→turismo, `3221/3223`→igualdad, `3122`→diversidad, `4116`→salud_mental). **Sin keywords** (la única descripción del CSV es de subconcepto económico, no fiable para mapear). Importe en euros.
- **FIX 2026-07-02 (dos bugs de tratamiento):** (1) el tidy 2022-26 perdía el CERO INICIAL del programa → la deuda `0111` llegaba como `111` y el prefijo `11*` la metía en `direccion` (~990 M€/año; direccion 2023 1.568→579 M, ya continua con el ZIP). Corregido con `zfill(4)`. (2) El mapping confundía la clasificación estatal con la VASCA: `322*`→empleo capturaba igualdad/juventud (26 M) mientras el empleo real (321 Empleo 425 M + 323 Formación 271 M ≈ 700 M/año) quedaba NULL. Corregido: empleo=`321*`+`3231`; y `3221/3223` (igualdad, Emakunde), `3122` (inmigración→diversidad), `4116` (adicciones→salud_mental) recuperados. **8 → 11 conceptos.**

## Conceptos NO separables (NULL estructural por diseño)
- **`dependencia` y `discapacidad`** (2 conceptos, `codigos: []` a propósito). Motivo: son competencia FORAL (diputaciones) y van integrados en la protección social agregada (subfunción 312/323) sin subfunción propia en este CSV autonómico. Forzarlos sería un error de datos (misma decisión honesta que ast).
- (Revisión 2026-07-02: `igualdad`, `diversidad` y `salud_mental`, antes listados aquí como NULL estructural, SÍ tienen programa funcional propio —3221/3223, 3122, 4116— y se han recuperado. El %fila se mantiene ~46 % porque el grueso del gasto vasco —RGI/inclusión 3121, Osakidetza— no se desglosa más en este CSV.)

## Advertencias de calidad del dato
- **⚠️ Fix crítico de doble conteo (2026-07-01).** El motor tidy previo sumaba gasto **e ingreso** y todas las entidades → total irreal **~38 B€** cuando el presupuesto real es **~13,5 B€**; `sanidad`/`educación` salían bien por casualidad (los ingresos no tienen función 41/42) pero el **total y `direccion` estaban contaminados** y la serie era incomparable con el resto de años y con Hacienda. Corregido con el filtro Tipo=1 + Entidad 100/2xx. Cualquier dato pvc anterior a este fix está inflado ~2x: NO usar.
- El total vasco excluye por diseño las transferencias a las Diputaciones Forales (función 91, ~13 B€) y demás gasto no-social; es un perímetro AdErAu, no el gasto consolidado del sector público vasco completo.

## Años faltantes / problemáticos
- Serie completa 2015-2026. Matiz: **2019 y 2023 son PROYECTO de presupuesto, no Aprobado** (no existe versión Aprobado en el dataset; el 2019 Aprobado devuelve HTTP 404). Interpretar esos dos años con esa salvedad.

## Notas de uso
- Comparable año a año y contra Hacienda **sólo tras el fix del 2026-07-01** (~13,5 B€ reales).
- No esperes los 5 conceptos de servicios sociales/igualdad: son NULL estructural, no huecos a rellenar.
- Marca 2019 y 2023 como Proyecto en cualquier análisis o pie de gráfico.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py pvc` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1534 16:1548 17:1603 18:1664 19:1720 20:1784 21:1807 22:1897 23:2097 24:2214 25:2313 26:2408` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** **Arreglada** (fix: filtro Tipo=1 + Entidad 100/2xx). Baseline ~1534-2408 €/hab. Si el total salta a ~38 B€, volvió el doble conteo gasto+ingreso.
- **Seams documentados** (salto esperado, NO error): 2021→22 (ZIP GASTOSC → CSV tidy)

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
