# Auditoría conceptual en cascada — 16 CCAA (2026-07-02)

> **Pregunta auditada:** ¿la calidad de la extracción conceptual (% filas con concepto,
> nº conceptos) está limitada por el ORIGEN (el documento no da más de sí) o por el
> TRATAMIENTO (el código no se adapta a la estructura real de cada fuente)?
> **Método:** protocolo derivado del caso Galicia (resuelto 2026-07-02): esquema asumido
> vs real, códigos degenerados, varianza entre años, correspondencias muertas, y vista de
> % concepto POR IMPORTE (€) además de por filas. 5 auditores en paralelo, read-only,
> re-extracciones aisladas verificadas contra los raws. Galicia queda como caso patrón ya
> corregido (dataset estratéxico vs funcional + guard de esquema).

## Matriz de dictámenes

| id3 | CCAA | Dictamen | Conf. | Impacto estimado | Nota |
|-----|------|----------|-------|------------------|------|
| cat | Cataluña | **TRATAMIENTO** | alta | 🔴 el mayor del proyecto | dedup first-wins descarta subtotales por servei: educación ×3,3 infra, universitats ×87, dependencia ×15,7 |
| val | C. Valenciana | MIXTO (trat. legacy) | alta | 🔴 ~4,7 B€/año legacy | deuda `011.10` (4 B€) y 313.xx legacy sin mapear en 2016-2023 |
| cym | Cast. y León | MIXTO | alta | 🔴 +30% magnitud 2016-18 | doble conteo filtrable (CONCEPTO 400/401/700/701) — NO era limitación de origen |
| bal | Baleares | **TRATAMIENTO** | alta | 🔴 ~1,5-1,9 B€/año 2015-16 | stubs 404 por zero-padding (`titol00` vs `titol0`); falta Educació entera (~800 M€) |
| pvc | País Vasco | **TRATAMIENTO** | alta | 🔴 ~1,7 B€/año | deuda `0111`→`111`→`direccion` (~990 M€) + empleo real (~700 M€) NULL |
| ara | Aragón | MIXTO | alta | 🟠 ~1 B€/año | `4222 EDUC SECUNDARIA` NULL desde 2020 (424-526 M€) + agrario ~0,6 B€ sin soberanía + `3132` dup infla total 4,6% |
| lar | La Rioja | **TRATAMIENTO** | alta | 🟠 ~0,5 B€ en 2015-16 | clasificación funcional ANTIGUA mis-mapeada: 403 M€ de sanidad→soberania (2016); ventana 2018 corta el bloque social; OCR Ó→Ñ |
| mad | Madrid | MIXTO (trat. dom.) | alta | 🟠 dobles conteos | regex admite subtotales de 2 díg. junto a centros de 5: educación +46%; keywords desalineadas por época |
| and | Andalucía | MIXTO | alta | 🟠 ~0,5 B€ + series incoherentes | ramas CSV/PDF no homogéneas (igualdad ×80); 31G/31P/32E sin mapear; 31B adicciones→sanidad |
| clm | Cast.-La Mancha | MIXTO | media-alta | 🟡 ~90 M€/año + contaminación | rename `324A` 2024 mata empleo (−62%); salud_mental fabricado con menores; `432A`→turismo (es urbanismo) |
| cnt | Cantabria | MIXTO | alta | 🟡 conceptos pequeños | códigos exactos de OTRA añada: `313A`(salud pública)→salud_mental, `231C`(infancia)→discapacidad |
| ext | Extremadura | MIXTO leve | alta | 🟡 ~175 M€/año | `252A`+`252B` (infancia/inclusión) sin mapear a diversidad — fix de 1 línea |
| ast | Asturias | **ORIGEN** | alta | 🟢 | 87% por importe; NULL estructural verificado contra el raw. Pendiente doc.: sanidad 2015 duplicada (413D+412B) |
| can | Canarias | **ORIGEN** | alta | 🟢 | 77,5% por importe; NULL = corporaciones locales/carreteras/deuda |
| nav | Navarra | **ORIGEN** | alta | 🟢 | 89,5% por importe; visor multi-año no mezcla ejercicios |
| mur | Murcia | **ORIGEN** | alta | 🟢 | 92-93% por importe; nit: entrada muerta `'314'` (quiso ser `314*`) |
| gal | Galicia | (resuelto 2026-07-02) | — | — | caso patrón: dataset homónimo equivocado + colapso silencioso |

**Balance: 4 TRATAMIENTO puro · 8 MIXTO · 4 ORIGEN limpio.** La vista POR IMPORTE
demuestra que el "% concepto por filas" del catálogo subestima la cobertura real en las
CCAA sanas (ast 87%, nav 89%, mur 93%) y la SOBREestima en las rotas (cat: 90% por
importe… del dinero que entra; lo descartado por el dedup nunca llega al denominador).

## Hallazgos por CCAA (detalle)

### cat — TRATAMIENTO (alta) · EL MÁS GRAVE
- `extract.py:66-69`: dedup first-wins con `key=(codigo, denom[:30])` se queda con la
  PRIMERA línea `PROGRAMA <cod>` del `vol_p_eid`, pero esa línea aparece UNA VEZ POR
  SERVEI (2026: `421 EDUCACIÓ` en EN01=2.339 M, EN07, EN08, EN09 personal docente=4.102 M,
  EN10…). Solo se captura EN01.
- Cuantificado 2026 (first-wins vs suma real): `421` 2.340→7.745 M (×3,3); `422`
  universitats 15,3→1.332 M (×87); `315` dependencia 164,6→2.586 M (×15,7); `317`
  diversidad 25,6→873 M (×34); `331` empleo 694→1.340 M (×1,9).
- Sanidad es correcta POR ACCIDENTE: la 1ª aparición de `415` es la transferencia a
  CatSalut (12.969 M) → pasa la auditoría de magnitud mientras el resto está a ⅓ o menos.
- Seam 2015→2016 (tot ×0,54, anomalía abierta) es del motor fallback, que suma TODO sin
  perímetro (direcció 9.746 M en 2015 vs 922 M en 2016).
- **Fix:** sumar por código las líneas PROGRAMA del subsector GENERALITAT (mantener
  `_SALUT_DOBLE_CONTEO` y perímetro 415); aplicar mismo perímetro al fallback 2015.
  Validar: sanidad no debe moverse; educación 2026 ≈ 7,3 B.

### val — MIXTO, tratamiento dominante en legacy ≤2023 (alta)
- 2016 usa códigos legacy `NNN.NN` que el yml no contempla: `011.10 Servicio de la Deuda`
  (4.055 M€, 23,6% del total) NULL, mientras el moderno `011A00` sí va a direccion →
  serie direccion 891 M (2016) → 10.734 M (2026), ~8 B del salto es artefacto.
- 313.xx legacy sin mapear: `313.60` (281,8 M), `313.70` (252,0 M) [→dependencia],
  `313.30` menor (107,1 M) [→diversidad]. `313.20 Drogodependencias` (12,4 M) cae en
  dependencia por substring — debería ser salud_mental.
- **Fix (3 líneas yml):** `'011*'`→direccion; exactos `313.60/313.70`→dependencia,
  `313.30`→diversidad, `313.20`→salud_mental.

### cym — MIXTO: conceptual impecable (ORIGEN), magnitud corregible (TRATAMIENTO)
- Calidad conceptual real (95,7% por importe 2017; hoja única consolidada 2021+, sin
  vista dual que confundir).
- El +30% de 2016-18 (anomalía abierta) es doble conteo IDENTIFICABLE en el propio CSV:
  transferencias internas a OOAA con CONCEPTO 400/401/700/701. 2017: sec 05 transfiere
  3.225 M (311A01) a la Gerencia de Salud que TAMBIÉN figura como servicio 0522 con
  3.386 M propios → sanidad 6.672 M ≈ 2× real. Filtrando: total 14,30→10,29 B;
  sanidad→~3,45 B (~1.450 €/hab, en banda).
- **Fix (~3 líneas en `cym/extract.py:113-132`):** en formato "Dotaciones", descartar
  filas con CONCEPTO ∈ {400,401,700,701}; actualizar baseline y registrar seam.

### bal — TRATAMIENTO (alta)
- `titol00_d.pdf`…`titol09_d.pdf` de 2015/2016 son stubs 404 de 34 B: el CAIB nombra las
  secciones de un dígito SIN cero (`titol0_d.pdf`, como está en raw/bal/2017). Faltan las
  secciones 2.1-2.10 enteras: Parlament, Presidència, Hisenda, **Educació (~800 M€)**,
  Turisme… La "educacion" de 2016 es UNA fila de 0,2 M€ (keyword).
- `extract.py:105-115` salta los stubs sin firma %PDF SIN warning (degradación silenciosa).
- La anomalía abierta "2016→2017 tot×1.44" no es crecimiento: es cobertura recuperada.
- **Fix:** re-descargar `titol0-9_d.pdf` (sin cero) de pr2015/pr2016 (patrón ya probado en
  el fix de 2017) + contador de stubs saltados en notes. Recupera ~+1,5-1,9 B€/año y 13 conceptos.

### pvc — TRATAMIENTO (alta)
- El tidy pierde el cero inicial del programa: `0111 Deuda` → `111` → casa `11*` de
  direccion: **989,7 M€/año de deuda como direccion en 2022-26** (direccion 270 M en 2016
  → 1.568 M en 2023, 63% deuda). En el ZIP no matchea (correcto).
- `empleo: ["322*"]` captura igualdad/juventud (3221/3222/3223 Emakunde, 14-26 M€) mientras
  el empleo real — 3211 (425-458 M€) y 3231 formación (225-271 M€) — queda NULL. El yml
  confundió la clasificación estatal con la vasca (en Euskadi 312x=SS, 321x=empleo, 322x=igualdad).
- La ficha exagera el NULL estructural: igualdad (3221+3223) y diversidad (3122 inmigración)
  SÍ son separables; dependencia/discapacidad sí son forales (origen).
- Doble degradación silenciosa: ESTFUNC lee columna euskera como castellano (`extract.py:70`,
  r[5] vs r[6]); tidy en CP850 decodificado como latin-1 → candidato de columna jamás matchea.
- **Fix:** zero-pad `Programa` a 4 díg. en `_extract_tidy` (o excluir grupo 0); remapear
  `empleo: [3211,3231,3212]`, `igualdad: [3221,3223]`, `diversidad: [3122]`, opcional
  `salud_mental: [4116]`; corregir columna castellano y cp850.

### ara — MIXTO (alta)
- `4222 EDUC SECUNDARIA` NULL en 2020-2026: **424-526 M€/año** (~40% de educación). Hasta
  2019 la denominación completa casaba la keyword; desde 2020 la fuente abrevia "EDUC".
  Explica el escalón de pct 60,4→55,8 en 2020.
- Soberanía casi vacía: `7123` (462-472 M€), `5311` (85-131 M€) etc. NULL — keywords
  esperan "agricultura/ganadería", el PDF dice "AGRARIA/AGROALIMENTARIO". ~0,6 B€/año.
- **62 de 103 entradas del yml jamás casan** (genéricos sin `*`; `transform_helpers.py:75-80`
  solo hace prefijo con `*` explícito). El mapeo real descansa en keywords → frágil.
- `3132` duplicado (~400 M€ ×2/año): transferencia sec-20→IASS + entrega sec-53. Hoy ambos
  NULL (no contamina conceptos) pero infla `total` ~4,6%.
- Los 9-11 conceptos (vs 13) SÍ son origen documentado (dependencia/discapacidad en genérico
  3132; salud_mental solo desde 2024).
- **Fix:** exactos `4222,4223,4224,4228,4220,4226,4227,4232`→educacion; `7121,7122,7123,5311`
  →soberania; `4132,4124`→sanidad; valorar excluir transferencia 3132 (patrón `_ARA_TRANSFER_SALUD`).

### lar — TRATAMIENTO (alta)
- 2015-2016 usan la clasificación funcional ANTIGUA (4.1=Sanidad, 3.1=Protección social,
  4.2=Educación, 4.3=Vivienda, 4.5=Cultura) y el yml codifica la NUEVA (2017+). Como el
  código gana a la keyword: **403 M€ de sanidad 2016 → soberania** (`4.1.*`), 112,8 M€ de
  mayores/discapacidad/infancia → sanidad, museos/deporte → turismo, vivienda → soberania.
- RE-DIAGNÓSTICO: la bandera documentada "2016 BAJO 353 €/hab infra-extracción" NO es del
  origen — la sanidad está en el CSV con la etiqueta equivocada.
- 2015: OCR de tokens invertidos produce `INVESTIGACIÑN` (Ó→Ñ, `extract.py:169-178`) →
  keywords de idi no casan (idi 2015 = 0,4 M vs 43,9 M en 2016).
- 2018: `_ORG_PROGRAMA_WINDOWS` corta en pág. 523 pero el bloque social (mayores 37,7 M,
  discapacidad 15,4 M, dependencia 11,8 M, mujer 2,0 M) está en págs. 567-626.
- La ficha `limitaciones-lar.md` está desactualizada (dice 2015/2018/2020/2023 "no incorporados").
- **Fix:** correspondencias condicionadas por año para ≤2016 (esquema antiguo); ampliar
  ventana 2018 a 560-630 con dedup; corregir mapeo Ó del OCR.

### mad — MIXTO, tratamiento dominante (alta)
- `RE_CENTRO` (`extract.py:51`, `\d{2,5}`) mezcla subtotales de sección (2 díg.) con centros
  (5 díg.) y AMBOS reciben concepto: educación 2015 cuenta el agregado "15" (4.326 M) MÁS
  sus 5 hijos (~2.036 M dos veces, +46%).
- Keywords sobre consejerías enteras: "12 ECONOMÍA, HACIENDA Y EMPLEO" (303,9 M) todo a
  empleo; "11 PRESIDENCIA, JUSTICIA…" (854-1.075 M) todo a direccion.
- Centros sociales sin mapear por keywords de otra época: "D.G. DEL MAYOR" 297,4 M (no casa
  "mayores"), "D.G. SERVICIOS SOCIALES" 393,4 M, "AGENCIA MADRILEÑA DE ATENCIÓN SOCIAL" 515,2 M.
  El salto dependencia 256 M→1.193 M es artefacto de renombrado.
- Componente ORIGEN confirmado: el Libro 03 no tiene vista por programas (grep=0 hits);
  el arreglo de fondo sigue siendo el Libro 04.
- **Fix:** excluir códigos de 2 díg. de la asignación (dejarlos como control de total);
  añadir keywords "del mayor", "bienestar social", "atención social", "servicios sociales".

### and — MIXTO (alta)
- Cobertura por importe alta en ambas ramas (91-93%): la cola NULL es no-social legítima.
- PERO las ramas no son serie homogénea por concepto: CSV2021/PDF2024 → sanidad ×1,63 (el
  CSV suma 41H transferencia + programas del SAS = doble conteo intra-concepto), empleo
  ×2,56, soberania ×2,78, **igualdad ×80** (184,5 M vs 2,3 M).
- Frágil por diseño: alias section-aware `12x→41H` SOLO en la rama PDF (`extract.py:142-152`);
  un año CSV con la recodificación 41H→12S dejaría sanidad ~0 en silencio.
- Entradas muertas (numéricos pelados y códigos de formato ajeno); `41M` jamás se emite.
- Sociales sin mapear: `31G` 209,9-237,6 M, `31P` 183,9-330,5 M, `32E` 58,2 M — diversidad
  queda en 4-10 M (implausible). `31B ADICCIONES` (33,8-40,6 M) va a sanidad, no salud_mental.
- **Fix:** mapear 31G/31P/32E (diversidad) y mover 31B a salud_mental; alias 12S↔41H en la
  capa transform (ambas ramas); unificar perímetro de la rama CSV (una sola vista).

### clm — MIXTO (media-alta)
- Seam CSV→PDF 2021↔2022 coherente en lo grande (sanidad ×0,99, educación ×1,05); el parser
  tolerante NO pierde líneas (99/99 verificado 2015).
- Rename tipo Andalucía sin adaptar: `324A` pasa en 2024 de "FP PARA EL EMPLEO" (casa
  keyword) a "…EN EL ÁMBITO LABORAL" (no casa) → **empleo pierde ~90 M€/año en 2024-26**
  (83 M→32 M, −62%), en VERDE sin warning.
- Códigos-plantilla con otro significado en CLM: `313A` (programas sociales básicos,
  26→101 M) y `313E` (menor, 35→66 M) → salud_mental FABRICADO; `313B` familias →
  diversidad (y duplicado en dependencia); `432A` urbanismo (10-15 M) → turismo por colisión.
- **Fix:** exactos `324A/324B`→empleo; retirar `313A/313E` de salud_mental y `313B` de
  diversidad (validar contra Tablas_Correspondencias); quitar `432A` de turismo.

### cnt — MIXTO (alta)
- El ~46% sin concepto ES origen legítimo (deuda 951M 15% del total, carreteras…) — 65-68%
  por importe.
- PERO conceptos pequeños corruptos por códigos exactos de OTRA añada: `313A`→salud_mental
  cuando es "SALUD PÚBLICA" (9,7 M = 100% del concepto); `231C`→discapacidad cuando es
  "INFANCIA Y FAMILIA" (14,5 M = ~100%); `232D`→dependencia siendo "FOMENTO NATALIDAD";
  `232*` arrastra juventud e `323*` innovación a igualdad (solo 3,4 de 32 M es igualdad real).
- `311O` formación sanitaria (20,9-22,3 M) NULL (keyword "sanitaria" no casa "sanitario").
- **Fix:** purgar exactos heredados (313A, 231C, 232D, 323A y muertos de 3 díg.), dejar
  keywords (las denominaciones del PDF son buenas); quitar `232*/323*` de igualdad; `311*`
  o keyword "sanitario" a sanidad.

### ext — MIXTO leve (alta)
- Techo de 11 conceptos = ORIGEN confirmado (sin programa de salud_mental/discapacidad en
  el resumen DOE).
- Tratamiento acotado: `252B Inclusión social` (76,1→97,5 M) y `252A Infancia y familias`
  (40,3→77,3 M) NULL toda la serie; el comentario del yml dice "252/253 social" pero solo
  mapeó 252C/253B/253C. Los 174,8 M de 2024 superan el total actual de diversidad (107,8 M).
- **Fix (1 línea):** añadir `252A, 252B` a diversidad.codigos.

### ast / can / nav / mur — ORIGEN (limpias)
- **ast:** 86,7% por importe; 0 ocurrencias de dependencia/salud mental/discapacidad en el
  raw (verificado pagetext completo). Caveat documentado: sanidad 2015 duplicada
  (413D 1.435,5 M + 412B 1.433,9 M → 2.888 €/hab) — mismo patrón que el fix de ara; y
  `313E Gestión SS` (284 M)→direccion es discutible pero deliberado.
- **can:** 77,5% por importe; NULL concentrado en 942x corporaciones locales (~1.018 M),
  453D carreteras, 951M deuda. Refinamiento opcional: `231B` (mayores) → ¿dependencia? (~0,6%).
- **nav:** 89,5% por importe; visor multi-año verificado (nodos por año, totales cuadran).
- **mur:** 91,7-93,4% por importe; ficheros extra del raw son captchas Radware, no datos
  perdidos. Nit: `'314'` muerta (→ `314*` si se decide mapear pensiones no contributivas).

## Hallazgos transversales (afectan a todo el pipeline)

1. **Entradas muertas masivas en correspondencias:** `asignar_concepto_local` solo hace
   prefijo con `*` explícito → los códigos genéricos de 2-3 díg. heredados de plantilla
   jamás casan (62/103 en ara, 43/109 en cat, también and/cnt/mur). El mapeo real recae en
   KEYWORDS, que se rompen con abreviaturas (ara "EDUC"), renombres (clm 324A) y géneros
   (cnt "sanitario") sin ningún aviso.
2. **La auditoría de magnitud solo vigila sanidad y total** → todos estos defectos
   conviven con "0 anomalías". Un test de continuidad POR CONCEPTO habría cazado
   ara-educación (escalón 2020), cat-first-wins y clm-empleo (escalón 2024).
3. **Degradación silenciosa como patrón sistémico** (gal, bal, pvc, cat, lar): cuando el
   documento no cumple lo asumido, el código no falla — degrada. Falta el patrón "guard +
   contador en notes" aplicado en gal.
4. **La vista por importe debe entrar en el smoke:** el pct por filas del catálogo
   distorsiona en ambas direcciones.

## Plan de fixes priorizado (por € de impacto)

| # | CCAA | Fix | Esfuerzo | Impacto |
|---|------|-----|----------|---------|
| 1 | cat | suma por código en perímetro GENERALITAT (sustituir first-wins) + mismo perímetro en fallback 2015 | medio | educación +5,4 B, dependencia +2,4 B, universitats +1,3 B (2026); cierra seam ×0,54 |
| 2 | val | 3 líneas yml (011*, 313.60/.70/.30, 313.20) | trivial | ~4,7 B€/año legacy; repara serie direccion |
| 3 | cym | filtro CONCEPTO∈{400,401,700,701} rama Dotaciones | bajo | cierra anomalía +30% 2016-18 |
| 4 | bal | re-descarga titol0-9 sin zero-pad 2015/16 + contador stubs | bajo | +1,5-1,9 B€/año; recupera Educació |
| 5 | pvc | zero-pad Programa + remapeo empleo/igualdad/diversidad + cp850 | bajo | −1 B deuda mal asignada; +0,7 B empleo |
| 6 | ara | exactos educación/soberanía/sanidad + transferencia 3132 | bajo | +0,5 B educación, +0,6 B soberanía, −4,6% total inflado |
| 7 | lar | yml condicionado por año ≤2016 + ventana 2018 + OCR Ó | medio | repara 2015-16 completos (403 M sanidad) |
| 8 | mad | excluir códigos 2 díg. + keywords por época | bajo | elimina dobles conteos (+46% educación) |
| 9 | and | 31G/31P/32E→diversidad, 31B→salud_mental, alias 12S↔41H en transform | bajo | +0,5 B diversidad; robustez |
| 10 | clm | 324A→empleo + purga 313A/313E/313B/432A | trivial | +90 M empleo; descontamina salud_mental |
| 11 | cnt | purga exactos de otra añada + 311* | trivial | descontamina 3 conceptos pequeños |
| 12 | ext | 252A/252B→diversidad | trivial | +175 M/año |
| T1 | tools | test continuidad POR CONCEPTO en auditoria_magnitud.py | bajo | red de seguridad para todo lo anterior |
| T2 | tools | linter de entradas yml muertas (0 matches en N años) | bajo | limpia la deuda de plantilla |

> ⚠️ Regla de oro: cada fix debe re-validarse con re-extracción aislada + baseline €/hab
> de la ficha + `auditoria_magnitud.py` ANTES de tocar el catálogo. Los fixes 1, 3, 4 y 7
> cambian magnitudes → actualizar baselines y SEAMS documentados.
