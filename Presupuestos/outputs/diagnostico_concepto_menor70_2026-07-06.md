# Diagnóstico en cascada — casos con `%concepto` < 70 % (2026-07-06)

> **Pregunta:** ¿por qué la tasa de asignación de concepto queda por debajo del 70 % en 9
> comunidades, y es NULL estructural legítimo (gasto no-social) o defecto de extracción?
> **Método:** re-extracción fresca con el dispatcher real (`python3 -m ccaa`) de años
> representativos por CCAA (rama nueva + rama antigua donde el formato cambia), descomponiendo
> el € SIN concepto en cubos por denominación y marcando posible fuga social; cruzado con
> `auditoria_conceptual_2026-07-02.md` (dictamen ORIGEN/TRATAMIENTO) y las fichas
> `limitaciones-<id3>.md`. Los 12 fixes conceptuales del 2026-07-02 están aplicados: lo que
> se mide aquí es el estado real de hoy.
> **Alcance:** ara, ast, bal, can, cat, clm, cnt, mad, pvc.

---

## Hallazgo central: la métrica engaña

El `%concepto` del catálogo es **% de filas**. Pero un presupuesto son euros, no filas: una
CCAA sana tiene *muchos programas pequeños* no-sociales (deuda, carreteras, justicia) que
correctamente quedan NULL y hunden el % por fila sin que falte ni un euro social. Al medir
**% por importe (€)**, los 9 casos < 70 % se parten en tres grupos que exigen estrategias
opuestas:

| CCAA (2024) | %fila | **%€** | €NULL | Mayor(es) ítem(s) en NULL — evidencia | Dictamen |
|---|:--:|:--:|:--:|---|---|
| **mad** | 49 | **58** | 12,7 B | Deuda 4,0 B · **D.G. RRHH 3,0 B** · Consorcio Transp. 2,0 B | 🔴 Techo estructural (proxy-centro) |
| **pvc** | 48 | **65** | 5,7 B | Deuda 0,9 B · **LANBIDE 1,5 B** (empleo/RGI) | 🔴 Tratamiento (entidad sin función) |
| **ara** | 64 | **63** | 3,4 B | Deuda 1,23 B · **Serv. Sociales 0,89 B** | 🟠 Mixto (fuga social grande) |
| **cnt** | 52 | 67 | 1,2 B | Deuda 0,42 B · MRR 0,16 B · Serv. Sociales 0,07 B | 🟠 Mixto |
| **clm** | 65 | 73 | 3,4 B | Deuda 1,9 B · Regadíos/agrario 0,16 B | 🟠 Mixto leve |
| **bal** | 75 | 76 | 1,7 B | Deuda 1,08 B (+ años pre-2024 con fuentes CID ilegibles) | 🟢 Origen (+ caveat técnico) |
| **can** | 65 | 77 | 2,4 B | Cabildos + Fondo Municipal + Carreteras ~1,1 B | 🟢 Origen limpio |
| **ast** | 68 | 82 | 0,96 B | Minería + Agua + Carreteras + Transportes | 🟢 Origen limpio |
| **cat** | 65 | **90** | 5,4 B | Seguretat 1,4 B · Ferroviari 0,9 B · Transport 0,6 B | 🟢 Origen (fix ya aplicado) |

> Lee la columna **%€**, no %fila. `cat` no es un problema (90 % del dinero clasificado);
> `mad` sí (42 % del dinero sin poder clasificar). El catálogo actual los pinta a ambos
> igual (~65 % / ~48 %), y eso es lo primero a corregir.

---

## Cascada — diagnóstico por caso

### 🔴 Tier 1 · Techo estructural / defecto de fondo (por € siguen bajos)

**MADRID — 58 % €. El caso más grave y el único con techo real.**
El motor `mad-libro-03-centros` no lee programas: lee **centros presupuestarios** (el Libro 04
de memoria-programas no tiene URL estable). Consecuencia demostrada en la re-extracción:
**"D.G. DE RECURSOS HUMANOS" = 3.032 M€** cae en NULL — es la nómina de profesorado/sanitarios
que *debería* ir a educación/sanidad pero cuelga de un centro horizontal de RRHH que no se
puede repartir sin el desglose funcional. El fix del 2026-07-02 (quitar doble conteo
agregado+centro) fue correcto pero no toca este techo. `salud_mental` y `diversidad` no existen
como centro → NULL estructural.

**PAÍS VASCO — 65 % €. Tratamiento: entidades sin clasificación funcional.**
El fix del 2026-07-02 arregló el empleo *funcional* (`321*`+`3231`) y la deuda mal mapeada,
pero la extracción de hoy destapa una fuga que sobrevivió: **"LANBIDE" = 1.494 M€** sigue en
NULL. Lanbide (Servicio Vasco de Empleo: RGI + activación) aparece en el `csv_tidy` como
*línea de entidad*, sin código funcional, así que el mapeo por prefijo no la ve. En 2019 el
equivalente es "Gizarteratzea" (inclusión/RGI, 989 M€). `dependencia`/`discapacidad` sí son
NULL estructural honesto (competencia foral de diputaciones).

**BALEARES (años pre-2024) — caveat técnico, no de fondo.**
2024 está sano (76 % €, NULL = deuda). Pero la re-extracción de 2019 devuelve denominaciones
`(cid:36)(cid:80)…` — **fuentes PDF sin tabla ToUnicode**: el texto no se decodifica. El mapeo
por código funcional aguanta (el gran NULL sigue siendo deuda), pero rompe el *fallback por
keyword* y la auditabilidad. Los stubs 404 de 2015-16 ya se arreglaron; falta verificar qué
años intermedios arrastran el problema CID.

### 🟠 Tier 2 · Mixto — estructural + una fuga social grande y mapeable

**ARAGÓN — 63 % €.** La deuda (1,23 B) es estructural, pero **"GESTIÓN Y DESARROLLO DE LOS
SERVICIOS SOCIALES" = 888 M€** está en NULL: es el programa genérico `3132` donde Aragón mete
dependencia+discapacidad juntas (no las desglosa). Además el agrario ("AGRARIA/AGROALIMENTARIO",
~0,6 B) no casa la keyword "agricultura" → soberanía vacía. El `3132` duplicado (transferencia
sec-20 + entrega sec-53) infla el *total* ~4,6 %.

**CANTABRIA — 67 % €.** Presupuesto pequeño (3,6 B): deuda 418 M + MRR 159 M ya son el 16 % en
NULL legítimo. La única fuga clara: **"PRESTACIONES Y PROGRAMAS DE SERVICIOS SOCIALES" 72 M€**.
El fix del 2026-07-02 ya purgó los códigos-plantilla contaminantes (`313A`,`231C`…);
`diversidad` es NULL estructural (Cantabria no publica programa LGTBI/migración).

**CAST-LA MANCHA — 73 % €.** Rama CSV 2019 (88 % €) mucho más sana que la rama PDF 2024 (73 %).
Fugas: **"REGADÍOS Y EXPLOTACIONES AGRARIAS" 162 M** (→ soberanía) y "PROGRAMAS SOCIALES
BÁSICOS" 98 M. Ojo a un salto sospechoso: la línea "DEUDA PÚBLICA" pasa de 214 M (CSV 2019) a
**1.903 M (PDF 2024)** — probable diferencia de perímetro (cap. 9 amortización) entre las dos
ramas; no contamina conceptos pero infla el total del tramo PDF.

### 🟢 Tier 3 · Origen limpio — el < 70 % es un falso positivo de la métrica

- **CATALUÑA — 90 % €.** El defecto grave del audit (first-wins que truncaba educación ×3,3,
  dependència ×15,7) **ya está corregido** (motor `cat-programa-generalitat-suma`). Hoy el NULL
  es policía (Seguretat 1,4 B), ferrocarril, carreteras, cultura — todo no-social. Residual
  mínimo: "Atenció a la infància i l'adolescència" 400 M (→ diversidad). *Nota secundaria:* el
  total bruto (~51 B) supera el consolidado catalán (~44 B) — coherente con vista por-programa
  sin eliminaciones, pero conviene verificarlo.
- **CANARIAS — 77 % €.** Serie de referencia. NULL = Cabildos + Fondo Canario de Financiación
  Municipal + Convenio de Carreteras + deuda. Impecable.
- **ASTURIAS — 82 % €.** NULL = minería, agua, carreteras, transportes. Fugas menores:
  "Atención a infancia/familias" 51 M, "Ayudas con fines sociales" 69 M.

---

## Estrategia de abordaje (priorizada por € y esfuerzo)

**Transversal — hacer una vez, beneficia a las 17:**

1. **Cambiar la métrica de calidad de %fila → %€** en `smoke_regresion_py.py` y en el catálogo.
   No es cosmético: reordena las prioridades (saca a cat/can/ast de la lista roja y deja solas a
   mad/pvc, que es donde de verdad falta dinero). Es el cambio de mayor ROI y el más barato.
2. **Linter de entradas muertas** en `correspondencias.yml` (0 matches en N años): hoy el
   40-60 % de las entradas nunca casan y el mapeo real recae en keywords frágiles que se rompen
   en silencio con abreviaturas/renombres.
3. **Subir el TEST 3 (continuidad por concepto) a bloqueante** para conceptos > 20 M€ — es la
   red que habría cazado ara-educación, clm-empleo y la fuga de Lanbide.

**Por tier:**

| Prioridad | CCAA | Acción | Esfuerzo | Efecto sobre %€ |
|:--:|---|---|---|---|
| 1 | **pvc** | Mapear la entidad **LANBIDE → empleo/inclusión** (mapa entidad→concepto complementario al funcional); decidir destino de RGI/Gizarteratzea (989 M) | bajo | +1,5 B clasificados |
| 2 | **ara** | Decidir política para "Servicios Sociales" `3132` (889 M): ¿concepto agregado o NULL honesto?; keywords agrario "AGRARIA/AGROALIMENTARIO"→soberanía; excluir `3132` duplicado del total | bajo | +0,9 B + total correcto |
| 3 | **mad** | **Conseguir el Libro 04 (memoria de programas)** — única solución de fondo. Sin él, marcar mad como *"cobertura estructuralmente limitada, usar solo cuotas relativas %"* y NO publicar sus magnitudes absolutas | alto (fuente) | techo real; hoy inarreglable con Libro 03 |
| 4 | **clm** | Exactos `regadíos→soberanía`, `programas sociales básicos→diversidad`; investigar el salto de deuda 214 M→1.903 M (perímetro cap.9 CSV vs PDF) | bajo | +0,26 B + total homogéneo |
| 5 | **cnt** | Mapear "Prestaciones y programas de servicios sociales" (72 M) | trivial | +0,07 B |
| 6 | **cat/ast/can** | Micro-fixes de keyword para "infància i adolescència / infancia y familias" (→ diversidad). Nada más: no tocar el extractor | trivial | cierre fino |
| 7 | **bal** | Verificar qué años pre-2024 tienen fuentes CID; arreglar decodificación (ToUnicode/OCR) o re-descargar PDF con capa de texto | medio | auditabilidad + fallback keyword |

**Regla de oro** (del propio proyecto): cada fix se re-valida con re-extracción aislada +
baseline €/hab de la ficha + `auditoria_magnitud.py` **antes** de tocar el catálogo.

---

## Anexo · Evidencia de la re-extracción (dispatcher real, € nominales)

Descomposición del € sin concepto por año representativo. `%€` = % del importe con concepto
asignado; `Fuga social` = € en NULL cuya denominación casa un patrón social (candidato a mapeo).

| CCAA | año | filas | %fila | %€ | €tot | €NULL | Fuga social |
|---|--:|--:|--:|--:|--:|--:|--:|
| ara | 2024 | 197 | 64 | 63 | 9,13 B | 3,37 B | ~1.070 M |
| ara | 2018 | 159 | 67 | 64 | 6,58 B | 2,39 B | ~821 M |
| ast | 2024 | 104 | 68 | 82 | 5,44 B | 0,96 B | ~163 M |
| ast | 2019 | 90 | 70 | 88 | 3,92 B | 0,48 B | ~68 M |
| bal | 2024 | 145 | 75 | 76 | 7,11 B | 1,73 B | ~79 M |
| bal | 2019 | 86 | 60 | 63 | 4,26 B | 1,57 B | ~27 M (CID) |
| can | 2024 | 140 | 65 | 77 | 10,75 B | 2,42 B | ~160 M |
| can | 2019 | 142 | 67 | 78 | 7,51 B | 1,68 B | ~107 M |
| cat | 2024 | 99 | 65 | 90 | 51,54 B | 5,39 B | ~467 M |
| cat | 2018 | 94 | 67 | 90 | 33,94 B | 3,40 B | ~184 M |
| clm | 2024 | 114 | 65 | 73 | 12,47 B | 3,36 B | ~109 M |
| clm | 2019 | 99 | 65 | 88 | 7,61 B | 0,94 B | ~110 M |
| cnt | 2024 | 89 | 52 | 67 | 3,57 B | 1,19 B | ~138 M |
| cnt | 2016 | 84 | 54 | 69 | 2,48 B | 0,76 B | ~97 M |
| mad | 2024 | 87 | 49 | 58 | 30,45 B | 12,71 B | ~273 M |
| mad | 2018 | 76 | 49 | 61 | 21,63 B | 8,52 B | ~205 M |
| pvc | 2024 | 114 | 48 | 65 | 16,35 B | 5,67 B | ~453 M |
| pvc | 2019 | 110 | 47 | 64 | 12,85 B | 4,57 B | ~84 M |

> Fuentes cruzadas: `outputs/auditoria_conceptual_2026-07-02.md`,
> `1_extraccion/ccaa/<id3>/limitaciones-<id3>.md`, `1_extraccion/ccaa/LIMITACIONES.md`,
> `logs/progreso.md` (entradas 2026-07-01 a 2026-07-06).
