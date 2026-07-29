# Detección de MEMORIAS de programas presupuestarios · CCAA × año

**Sesión 2026-07-28** · Sweep automatizado en 2 pasadas sobre las URL del catálogo
(`DIRECCIONES URL_correcciones_2026-07-27.xlsx` + `fuentes.yml`), con verificación de
cada documento: magia PDF, nº páginas, marcadores narrativos multilingües
(objetivo/obxectivo/objectiu/helburu, indicador, actividad/actuación, memoria) y año.
Alojadas en `fuentes/raw/<id3>/<año>/memoria/` (128 MB, 31 carpetas + 8 tomos ya en repo).

**Semáforo:** 🟢 verificada en disco · 🟡 descargada, señal débil · 🟠 localizada sin descarga automatizable · 🔴 no localizada · ⬜ no existe (prórroga sin presupuesto)

| CCAA | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | ✔ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andalucía | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 8/12 |
| Aragón | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Asturias | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 1/12 |
| Baleares | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Canarias | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 8/12 |
| Cataluña | 🟢 | 🟢 | 🟢 | ⬜ | 🟢 | 🟢 | ⬜ | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 10/12 |
| C.-La Mancha | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Cantabria | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Cast. y León | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Extremadura | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Galicia | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 12/12 |
| La Rioja | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Madrid | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| Murcia | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 0/12 |
| Navarra | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| País Vasco | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 0/12 |
| C. Valenciana | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 🟠 | 0/12 |

**Total verificadas: 39/204** · 24 localizadas-no-automatizables · resto sin localizar.

## Qué documento es cada memoria verificada

| CCAA | Años 🟢 | Documento | Naturaleza |
|---|---|---|---|
| Andalucía | 2017-19, 2022-26 (8) | `memoria_programas.pdf` (tomo12-5b, **ya era la fuente de extracción**) | Fichas por programa con objetivos OE/OO/ACT + indicadores (886-1622 marcas/tomo) — **la más rica de España** |
| Cataluña | 2015-17, 2019-20, 2022-26 (10) | `VOL_P_MEM.pdf` — *Memòries de programes* (839-987 págs) | Memoria por programa: objetivos, indicadores, actividades. 2025/26 = doc de 2024 (prórroga). 2018/21 ⬜ sin presupuesto |
| Galicia | 2015-2026 (12) | `MEMORIA_II.PDF` (2015-21) / `MEMORIA_I.PDF` (2022-26), junto a PROGR_* | Memoria de obxectivos por programa (284-636 págs) |
| Canarias | 2018-19, 2021-26 (8) | `TOMO-4-Informe-Economico-y-Financiero-y-Memorias-explicativas.pdf` | Memorias explicativas por **sección** + informe económico-financiero (201-257 págs). No es ficha-por-programa |
| Asturias | 2020 (1) | `tomo_III.pdf` (Tomo 3 de los PGA) | Memoria de objetivos; el resto de años el Liferay exige uuid por fichero |

## No localizadas con sospecha de ubicación (accionables)

| CCAA | Sospecha concreta | Bloqueo |
|---|---|---|
| Murcia 🟠×12 | `carm.es/chac/presupuestos<año>/` junto al articulado (el visor móvil es un subproducto) | **Captcha Radware** — requiere descarga manual en navegador |
| C. Valenciana 🟠×12 | Árbol `hisenda.gva.es/auto/presupuestos/<año>/` T1-T7: fichas **FP4 'Memoria de actuaciones' por programa** dentro del Tomo II por sección | Multi-fichero (~30 PDF/año) — requiere crawl dedicado, factible sin captcha |
| Andalucía 2015/16/20/21 | Tomo 12 del archivo histórico CEHAP (web antigua economiayhacienda) — los patrones `presup<año>`/drupal legacy no resuelven | URL histórica no derivable; buscar en archivo web de la Junta |
| Canarias 2015-17, 2020 | Mismo TOMO-4 con **nombre distinto** en la galería de esos años (naming cambió) | Enumerar galería del año en gobiernodecanarias.org |
| Asturias 2015-19, 2021-26 | `tomo_III.pdf` existe (2020 lo prueba) pero cada año vive en un folder Liferay distinto que exige uuid | Localizar uuid por año en transparencia.asturias.es (manual o buscador del portal) |
| Madrid ×12 | **Libro 04** junto al Libro 03 en `comunidad.madrid/docs/assets/` (blocker ya documentado: 'sin URL estable') | comunidad.madrid devuelve 403 a clientes no-navegador; requiere sesión de navegador |
| País Vasco ×12 | Memorias por sección en `aurrekontuak.euskadi.eus` (los `adjuntos/<año>A/` son opacos) | Multi-fichero + naming euskera no derivable |
| Baleares ×12 | Framesets `pressuposts.caib.es/www/ant/pr<año>/` — tomos con memòries tras 3 niveles de frames | Crawl de frames profundo; factible con esfuerzo dedicado |
| C-La Mancha ×12 | Los tomos del proyecto en la página de la Consejería de Hacienda (castillalamancha.es), NO en transparencia (Drupal sin adjuntos estáticos) | Localizar página real de tomos por año |
| Extremadura ×12 | Tomos `PLP<yy>_XX` hermanos del `Tomo02_EIG` en asambleaex.es (listado da 403) | Naming del tomo memoria no derivable a ciegas |

## Sin localizar (nada encontrado)

- **Aragón** — slugs `aragon.es/documents/d/guest/<slug>` opacos; presupuesto.aragon.es no enlaza memorias estáticamente. *(Las memorias existen: 'Memorias de objetivos' por sección en el proyecto de ley; requiere navegación manual del portal.)*
- **Cantabria** — solo publica 'Memoria de Beneficios Fiscales' (3 falsos positivos detectados por el verificador y **eliminados**). Sin memoria de objetivos por programa en cantabria.es.
- **Cast. y León** — las páginas de hacienda.jcyl.es solo llevan estados consolidados; ni rastro del tomo memoria.
- **La Rioja** — todo el repositorio va por `idMmedia` opaco; sin página índice estable localizada.
- **Navarra** — el visor presupuesto.navarra.es no publica memoria descargable; CKAN de datos abiertos sin memorias PDF.

## Utilidad inmediata (conexión con la auditoría conceptual)

Las memorias verificadas cubren justo donde hay trabajo conceptual pendiente:
**Cataluña** (VOL_P_MEM permite auditar el bucket diversidad/inclusió), **Galicia**
(MEMORIA_II para revisar el bucket ancho de diversidad 2015-21), **Andalucía** (fichas
OE/OO/ACT para justificar cada asignación). Los 2 casos Tier-1 del diagnóstico del
2026-07-06 (Madrid Libro-04 y Lanbide/PVC) siguen bloqueados por 403/naming — son
los de mayor valor pendiente.