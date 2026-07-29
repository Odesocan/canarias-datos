# Limitaciones conocidas — Galicia (gal)

> Advertencias de la extracción de Galicia. Léelo antes de usar estos datos.
> Fuentes: extract.py, correspondencias.yml, logs/progreso.md, catálogo. Rev.: 2026-07-01.

## Motor(es) y cobertura
- Motor(es): `gal-progr-consellerias-ruleC` para 2015-2021 (PDF, regla C) y `gal-csv-abertos-xunta` para 2022-2026 (CSV consolidado), ambos + `gal-transform` · Años: 2015-2026 (serie completa, 12 ejercicios) · Estado global: 7 VERDE_PRAGM (2015-2021, 11 conceptos) + 2 VERDE_PRAGM (2024, 2025) + **3 AMARILLO (2022, 2023, 2026)**.

## Perímetro / decisiones de consolidación
- **Dos fuentes / dos métodos, con un seam en 2021↔2022:**
  - **2015-2021 — PDF `PROGR_I/II` con "regla C":** cada programa cierra con `TOTAL PROGRAMA <cód> <importe>`. El documento NO está consolidado (los organismos autónomos —SERGAS, axencias— ejecutan programas financiados por transferencias de las consellerías, así que sumar TODO duplica: gross 2023 = 20.2B vs 12.85B real). **Regla C:** sumar el total de programa SOLO de los bloques ejecutados por una CONSELLERÍA (excluir los bloques cuyo servizo es un organismo autónomo: "SERVIZO GALEGO", "AXENCIA", "CONSORCIO", "INSTITUTO GALEGO", "FUNDACION"…). La transferencia que financia al organismo queda como proxy de su gasto → evita el doble conteo. Granularidad de programa; 11 conceptos.
  - **2022-2026 — CSV de datos abertos (`abertos.xunta.gal`) consolidado:** SÍ incluye al SERGAS. El id del dataset NO es rolling (`2022=0443, 2023=0562, 2024=0607, 2025=0665, 2026=0690`). Granularidad más gruesa: consellería×grupo (no programa); el concepto se asigna por KEYWORD sobre el nombre de la consellería, no por código. 7-8 conceptos.
- **OJO clasificación funcional gallega:** sanidad = grupo 41x y servizos sociais = 31x (al revés que el genérico/Cantabria). El correspondencias se reescribió el 2026-06-30 con los códigos reales; el override raíz `ccaa['Galicia']` estaba OBSOLETO y MAL (mandaba el 298M de dependencia a discapacidad, sanidad sin 412/413/414) y se corrigió.

## Conceptos NO separables (NULL estructural por diseño)
- **discapacidad** y **salud_mental:** `codigos: []` — Galicia no tiene programa propio para estos conceptos → NULL estructural.
- Programas de servizos sociais generales dejados a propósito sin mapear a un concepto social (312A protección/inserción, 312B prestacións familias, 312F solidariedade, 312G conciliación, 313C servizos comunitarios, 311A) — pendiente validar su asignación contra `Tablas_Correspondencias_CCAA` / cuaderno §1.6.

## Advertencias de calidad del dato
- **Sesgo residual de la regla C (2015-2021):** ~-4.6 % en sanidad y ~+8 % en total, estable (validado contra el CSV consolidado 2022-2024). Es el precio de usar la transferencia como proxy; frente a las alternativas (gross +94 % sanidad, o dedup -70 %) es la opción defendible.
- **Seam de método/granularidad en 2021↔2022:** el salto PDF-programa (11 conceptos) → CSV-consellería (6-8 conceptos) puede introducir un pequeño escalón en conceptos distintos de sanidad. La serie de sanidad SÍ es continua y monótona (3.17B en 2015 → 5.67B en 2026).
- **Riesgo latente de doble conteo de transferencias internas** con el SERGAS como entidad separada: la regla C lo controla en la rama PDF; revisar que la rama CSV consolidada no lo reintroduzca (ver `LIMITACIONES.md` §3).
- La certificación VERDE/AMARILLO no valida magnitudes (ver `LIMITACIONES.md` §1).

## Años faltantes / problemáticos
- **2022, 2023, 2026: RESUELTO 2026-07-02 (no era origen, era tratamiento).** Estaban en
  AMARILLO (16-18 filas) porque se había descargado el dataset EQUIVOCADO: el
  `gastos-orzamento-<año>-sobre-plan-estratexico` (columnas `Consellería;Eixo;Prioridade
  de inversión`), que NO tiene grupo de función. El extractor buscaba la columna `Grupo`,
  no la encontraba, ponía `grupo=0` para todo y colapsaba a 1 fila/consellería → degradaba
  en silencio. Corregido descargando el dataset FUNCIONAL (`Consellería;Grupo;Capítulo`):
  **2022=0445, 2023=0564, 2026=0692**. Resultado: 2022→41 filas (sanidad 4.59B, 1706 €/hab),
  2023→42 filas (4.97B, 1848 €/hab), 2026→47 filas VERDE (5.67B, 2107 €/hab) — todos cuadran
  con el baseline. Añadido `_es_csv_funcional()` (guard de esquema) en `extract.py`: rechaza
  el CSV estratéxico en vez de degradar. **Galicia: 12/12 sin AMARILLO.**
- 2015-2021 en VERDE_PRAGM (~77.6-77.8 % concepto) por regla C.
- Antes del 2026-06-30 la serie era mono-año (solo 2025); PROGR_I/II se descartó primero por un bug de dedup propio y luego se rehabilitó con la regla C.

## Notas de uso
- Para análisis interanual usa preferentemente sanidad (serie continua). Para otros conceptos, ten en cuenta el seam 2021↔2022 (cambio de granularidad).
- No busques `imp_discapacidad` ni `imp_salud_mental` para Galicia: NULL estructural, no cero real.
- Los tres años AMARILLO (2022/2023/2026) son usables a nivel de agregado; su baja granularidad limita el número de conceptos, no la fiabilidad del total.
- No sumes PROGR_I/II en bruto (duplica por transferencias); usa siempre la regla C o el CSV consolidado.

## Evaluación post-extracción (magnitud)

Corre tras re-extraer: `python3 tools/auditoria_magnitud.py gal` (Test continuidad + Test per-cápita). Ver `CLAUDE.md §5.1` y [`../LIMITACIONES.md`](../LIMITACIONES.md).

- **Banda esperada** (sanidad €/hab): ~1200-2000 (España ~1600-1800).
- **Baseline** (sanidad €/hab, 2026-07-01): `15:1174 16:1226 17:1264 18:1357 19:1401 20:1444 21:1622 22:1700 23:1842 24:1923 25:2022 26:2101` — si una re-extracción se desvía, el formato de ese año cambió; revísalo antes de dar VERDE.
- **Bandera(s) roja(s):** 2022/2023/2026 en AMARILLO (CSV con pocas filas). Serie plausible salvo el escalón del seam.
- **Seams documentados** (salto esperado, NO error): 2021→22 (PDF regla C → CSV abertos)

---
*Limitaciones transversales del pipeline (aplican a todas las CCAA): ver [`LIMITACIONES.md`](../LIMITACIONES.md).*
