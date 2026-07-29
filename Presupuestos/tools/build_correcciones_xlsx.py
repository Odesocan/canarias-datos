#!/usr/bin/env python3
"""Añade la variable `Correcciones` al Excel de estado de extracción, CCAA × año.

Combina dos fuentes, ambas por AÑO CONCRETO:

  A. CURADAS  — recomendaciones leídas en `1_extraccion/ccaa/<id3>/limitaciones-<id3>.md`
                (fixes aplicados, perímetro, prórrogas, NULL estructural, unidades…),
                asignadas a los ejercicios a los que realmente afectan.
  B. AUTOMÁTICAS — hallazgos año-específicos de `trazabilidad-<id3>.md`, recalculados
                desde el staging: saltos/apariciones/desapariciones de concepto,
                códigos duplicados dentro del ejercicio y códigos que cambian de
                concepto respecto al año anterior.

Cada corrección lleva una etiqueta de tipo entre corchetes. Varias correcciones del
mismo CCAA-año se separan por "; ".

Uso:
    python3 tools/build_correcciones_xlsx.py --in "<modelo>.xlsx" --out "<salida>.xlsx"
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_trazabilidad_md import (  # noqa: E402
    cargar, agregar, detectar_alertas, meur, SIN,
)

TODOS = None  # marcador: aplica a todos los años de la CCAA

SEP = "; "  # separador de correcciones dentro de la celda


def limpiar(texto: str) -> str:
    """Elimina los `;` internos para que SEP sea el único separador de registros."""
    return re.sub(r"\s*;\s*", " — ", texto).strip()

# ---------------------------------------------------------------------------
# A. CATÁLOGO CURADO — leído de limitaciones-<id3>.md, año a año.
#    (años, texto). años = set de ejercicios, o TODOS.
# ---------------------------------------------------------------------------
CURADAS: dict[str, list[tuple[set[int] | None, str]]] = {
    "and": [
        (TODOS, "[CONCEPTO] Fix 2026-07-02: 31G/31P/32E → diversidad y 31B → salud_mental (antes NULL/sanidad)"),
        ({2015, 2016, 2020, 2021},
         "[PERÍMETRO] Rama CSV CKAN: mantener el filtro de CENTRO GESTOR (cg[2:4]=='00'); sin él se cuentan a la vez la transferencia 41H de la Consejería y la ejecución del SAS (41C/41G) y sanidad se duplica"),
        ({2017, 2018, 2019, 2022, 2023, 2024, 2025, 2026},
         "[PERÍMETRO] Rama PDF: mantener la recodificación section-aware 12S → 41H dentro de la Consejería de Salud; sin ella 2024-2026 caen a ~0,14 B€"),
        ({2022},
         "[DOBLE CONTEO] CRÍTICO: único ejercicio de la serie con DOS documentos fuente; memoria_programas.pdf aporta 41H=12.086 M€ (transferencia) y estado_iii.pdf aporta 41C=8.808 M€ + 41G=2.239 M€ (ejecución SAS). Quedarse solo con memoria_programas.pdf para ser coherente con 2021 y 2023"),
        ({2024, 2025, 2026}, "[PERÍMETRO] Marcado como consolidado en el staging: verificar que no se solapa con la vista de centro gestor"),
    ],
    "ara": [
        (TODOS, "[DOBLE CONTEO] Excluir 4131 'Protección y promoción de la salud' (transferencia Departamento → SALUD) y contar 4121 (entrega del SALUD); sin ello sanidad sale ~2× (3247 €/hab vs ~1600)"),
        (TODOS, "[CONCEPTO] Usar prefijos reales 421*/422* → educacion y 71*/5311 → soberania: los códigos exactos de 3 dígitos del yml nunca casan los códigos emitidos de 4 (4222 'EDUC SECUNDARIA' iba a NULL)"),
        (TODOS, "[DOBLE CONTEO] PENDIENTE: 3132 'Gestión y desarrollo de los SS' duplicado (sec-20 Departamento + sec-53 IASS) infla el total ~4,6 %; ambos quedan NULL, no contamina conceptos"),
        (TODOS, "[NULL ESTRUCTURAL] dependencia y discapacidad no existen como programa propio en Aragón; no interpretar su ausencia como cero"),
        (TODOS, "[CONCEPTO] 4133 'SALUD MENTAL' separado de sanidad por match exacto (reclasificación 2026-06-05)"),
        ({2016}, "[FUENTE] Raw sustituido: usar 'Presupuesto de ingresos 2016.pdf' del ZIP histórico (pese al nombre trae el detalle por programa); la Ley BOA no contiene líneas 'TOTAL PROGRAMA'"),
        ({2019}, "[PRÓRROGA] Ejercicio idéntico a 2018 en el staging: no es una observación independiente"),
        ({2025, 2026}, "[PRÓRROGA] Prórroga encadenada (2025≡2024, 2026≡2025): no tratar como ejercicios independientes"),
    ],
    "ast": [
        (TODOS, "[CONCEPTO] Envoltorio de servicios sociales: 313A/313E/313G/313D → dependencia (regla ccaa_codigo del correspondencias RAÍZ); es SS general, no ejecución estricta del SAAD"),
        (TODOS, "[NULL ESTRUCTURAL] discapacidad y salud_mental no son separables del envoltorio 313x; los importes que aparecen son residuales de patrones globales, no gasto real de Asturias"),
        (TODOS, "[MAPEO] Residuales conocidos por fuga de patrón global: 313C cooperación (~6,7 M€) → discapacidad, 313B emigración (~1,3-3,3 M€) → diversidad, 514B puertos (~9-13 M€) → salud_mental"),
        ({2015}, "[DOBLE CONTEO] Saltar las páginas sin cabecera 'DISTRIBUCIÓN DEL GASTO': los anexos RESUMEN PROGRAMÁTICO y PRESUPUESTO CONSOLIDADO repiten el 412B del SESPA (1.434 M€) ya contado como transferencia 413D. Sin el gate: sanidad 2,92 B y total 5,13 B (2888 €/hab)"),
        ({2021, 2022, 2023}, "[UNIDAD] Verificar parse_eur con punto único de miles ('852.310' → 852310, no 852,31), que afectaba a estos ejercicios"),
        ({2022}, "[FUENTE] Procede de proyecto_2022_tomoII.pdf (Tomo II de proyecto técnico), no del BOPA final: puede diferir de la aprobación definitiva"),
        ({2024, 2025, 2026}, "[MAGNITUD] Sanidad 2300-2524 €/hab, por encima de la banda: crecimiento real (población más envejecida de España), no doble conteo; el TEST 2 seguirá avisando"),
    ],
    "bal": [
        (TODOS, "[PERÍMETRO] El mismo programa aparece bajo varios C.Cost: sumar los parciales por (código, denominación); procesar solo ficheros con firma %PDF real"),
        ({2015, 2016}, "[FUENTE] Resuelto 2026-07-02: las secciones titol0_d…titol9_d se sirven SIN cero a la izquierda; pedirlas como titol00 devolvía stubs de 34 B saltados en silencio (educación 2016 quedaba en 0,2 M€)"),
        ({2017}, "[FUENTE] Resuelto 2026-07-01: la ruta correcta es pr2017-def (no pr2017) y las secciones van sin cero a la izquierda; los titol*_d.pdf originales eran stubs de 34 B"),
        ({2018, 2019, 2020, 2021},
         "[FUENTE] Resuelto 2026-07-24: titol00_d…titol09_d eran stubs de 34 B; faltaba titol8 = Conselleria d'Educació, con lo que imp_educacion salía ~1,0 M€/año en vez de ~936-1.021 M€ y disparaba var_educacion 2022 a +107.058 %. Re-descargar sin cero a la izquierda"),
        ({2026}, "[PRÓRROGA] Prórroga extraída con motor distinto (bal-resumen-programas-pdf, PDF de estados numéricos): cortar antes de 'Prórroga de presupuesto del Servicio de Salud' para no duplicar 411E y excluir 011A (deuda). Perímetro no comparable sin salvedad con el frameset"),
    ],
    "can": [
        (TODOS, "[DOBLE CONTEO] Usar solo la sección 2.10 'RESUMEN DE GASTOS POR PROGRAMAS'; excluir 2.15/2.16 (desgloses por capítulo cuyos 'Total' repiten los mismos códigos)"),
        (TODOS, "[FUENTE] Sección 2.10 bianual: _pick_importe debe tomar el 2º importe sin coma decimal (columna del año objetivo, no del año-1 ajustado)"),
        (TODOS, "[NULL ESTRUCTURAL] salud_mental no desagregado: va dentro del programa del SCS (412*)"),
        ({2019, 2020, 2021}, "[CONCEPTO] Fix 2026-07-16: el salud_mental aparente de estos años era 313A 'Salud Pública' (0,3 M€) mal mapeado; 313A retirado del catálogo"),
    ],
    "cat": [
        (TODOS, "[DOBLE CONTEO] Sanidad = 415 (CatSalut consolidado) + 414/419; EXCLUIR 411 y 412 (entrega del ICS, ya dentro de 415). Sin el filtro sanidad sale ~2× (~2220 €/hab vs ~1340)"),
        (TODOS, "[CONCEPTO] 412 retirado de soberania: es atenció especialitzada de SALUT, no soberanía alimentaria"),
        (TODOS, "[PERÍMETRO] Sumar la línea PROGRAMA de las páginas 'Servei:' del Subsector GENERALITAT. El first-wins previo truncaba los multi-servei: educació ×3,3, universitats ×87, dependència ×15,7"),
        ({2015}, "[FUENTE] Formato sin denominación en la línea PROGRAMA; el seam 2015→2016 era artefacto del first-wins, ya corregido (2015=32,5 B ≈ 2016=33,7 B)"),
        ({2018, 2021, 2025}, "[PRÓRROGA] SIN FUENTE PROPIA: el ejercicio está relleno por prórroga (2018≡2017, 2021≡2020, 2025≡2024) porque falta el vol_p_eid. No es dato oficial del año: no interpolar ni tratarlo como observación independiente"),
    ],
    "clm": [
        (TODOS, "[CONCEPTO] 324A/324B → empleo por código exacto: el renombre de 2024 a 'FP EN EL ÁMBITO LABORAL' rompía el keyword y empleo perdía ~90 M€/año"),
        (TODOS, "[CONCEPTO] salud_mental estaba FABRICADO con 313A 'Programas sociales básicos' y 313E 'Atención al menor': retirados (313E → diversidad). CLM no tiene programa propio de salud mental"),
        (TODOS, "[CONCEPTO] 432A 'Gestión del urbanismo' retirado de turismo (colisión de código exacto); queda en vivienda"),
        ({2015, 2016, 2017, 2018, 2019, 2020, 2021},
         "[UNIDAD] Rama CSV gastosf en EUROS: no aplicar ×1000. Parser tolerante para líneas entrecomilladas con comillas internas duplicadas"),
        ({2022, 2023, 2024, 2025, 2026}, "[UNIDAD] Rama PDF tomo I en MILES: aplicar ×1000"),
        ({2022}, "[SEAM] Cambio de rama CSV→PDF: el salto del total 9,67 → 12,26 B es artefacto de alcance, no de magnitud. Sanidad SÍ es continua cruzando motores; comparar totales solo dentro de la misma rama"),
    ],
    "cnt": [
        (TODOS, "[CONCEPTO] Fix 2026-07-02: 313A 'SALUD PÚBLICA' → sanidad (era el 100 % de salud_mental, fabricado); 231C 'INFANCIA' → diversidad (era el 100 % de discapacidad); 232D fuera de dependencia; los prefijos 232*/323* ya no arrastran 232A 'JUVENTUD' ni 323A 'INNOVACIÓN' a igualdad"),
        (TODOS, "[CONCEPTO] Keyword 'sanitario' añadido para 311O 'Formación de personal sanitario' (22 M€, iba a NULL): ojo con las variantes de género en los keywords"),
        (TODOS, "[NULL ESTRUCTURAL] salud_mental y discapacidad no se desglosan en programa propio en Cantabria"),
        ({2015, 2016, 2017}, "[FUENTE] Motor distinto (cnt-centros-suma-capitulos, Anexo de Centros Gestores): consolidados por programa y comparables, pero tenerlo en cuenta al depurar diferencias finas"),
        ({2025}, "[FUENTE] Bug corregido 2026-06-29: el slot 2025 apuntaba a la URL de 2026 y el raw en disco era el Proyecto 2026. Usar el 2025 re-extraído (88 filas, total 3,79 B, entre 2024=3,56 y 2026=3,97)"),
    ],
    "cym": [
        ({2016, 2017, 2018},
         "[DOBLE CONTEO] Descartar las líneas de transferencia interna a OOAA (conceptos económicos 400/401/700/701): el formato 'Dotaciones' las incluye mientras el OOAA figura aparte con su gasto ejecutado → ~+30 % (total 2017 14,30 → 10,29 B; sanidad 6,67 → 3,45 B)"),
        ({2015},
         "[FUENTE] Único origen es la Ley 11/2014 (BOCYL, 576 pp) vía motor cym-bocyl-territorial: agregar por SUBPROGRAMA sumando capítulos y RESTANDO las transferencias internas 400/401/700/701. Reconcilia al euro con el estado consolidado oficial (9.920.811.756 €)"),
        ({2019, 2020}, "[PRÓRROGA] Prórroga: 2019≡2018 y 2020≡2019 en el staging; el portal jcyl no publica recurso independiente"),
        ({2022}, "[PRÓRROGA] Prórroga: 2022≡2021 en el staging"),
        ({2025, 2026}, "[FUENTE] La URL de datos abiertos JCyL entrega un .csv que en realidad es un ZIP guardado como gastos.bin: _resolve_source debe detectar la firma PK y extraer el fichero de gastos. 2026≡2025 (prórroga de 2024)"),
        (TODOS, "[PERÍMETRO] No leer la caída 2018→2021 como recorte: es el cambio de perímetro por la consolidación de transferencias internas"),
    ],
    "ext": [
        (TODOS, "[CONCEPTO] 252A 'Atención a la infancia y familias' y 252B 'Inclusión social' añadidos a diversidad (iban a NULL en toda la serie; ~175 M€ recolocados en 2024)"),
        (TODOS, "[FUENTE] Usar la tabla resumen por programa de la Ley DOE; NO la extracción por detalle EIG, que infravalora educación ~3×"),
        (TODOS, "[NULL ESTRUCTURAL] salud_mental y discapacidad no separables: no son cero real"),
        ({2016}, "[FUENTE] Corrección de URL: la fuente real es la Ley 3/2016 (DOE 67); la del catálogo previo (1090o.pdf/N109) no era la ley"),
        ({2024, 2025, 2026}, "[COBERTURA] VERDE_PRAGM con 79,7 % de concepto, justo por debajo del umbral estricto del 80 %"),
        ({2025, 2026}, "[PRÓRROGA] Prórroga de la Ley 1/2024 (órdenes de 6-feb-2025 y 16-dic-2025): resumen por programa idéntico al de 2024, no son observaciones independientes"),
    ],
    "gal": [
        ({2015, 2016, 2017, 2018, 2019, 2020, 2021},
         "[PERÍMETRO] Rama PDF con regla C (transferencia como proxy): sesgo residual conocido ~-4,6 % en sanidad y ~+8 % en el total. No sumar PROGR_I/II en bruto (duplica por transferencias internas)"),
        ({2022, 2023, 2026},
         "[FUENTE] Se había descargado el dataset EQUIVOCADO (gastos-orzamento-<año>-sobre-plan-estratexico, sin grupo de función): el extractor ponía grupo=0 y colapsaba a 1 fila/consellería, degradando en silencio. Usar el dataset FUNCIONAL (2022=0445, 2023=0564, 2026=0692) y mantener el guard _es_csv_funcional()"),
        ({2022}, "[SEAM] Cambio de método y granularidad: PDF-programa (11 conceptos) → CSV-consellería (6-8 conceptos). Puede introducir escalón en conceptos distintos de sanidad"),
        (TODOS, "[NULL ESTRUCTURAL] discapacidad y salud_mental no separables en Galicia"),
        (TODOS, "[DOBLE CONTEO] Riesgo latente con el SERGAS como entidad separada: verificar que la rama CSV consolidada no reintroduce la transferencia interna"),
    ],
    "lar": [
        ({2015, 2016},
         "[CONCEPTO] Los BOLR de estos años usan el esquema funcional ANTIGUO (4.1=Sanidad) mientras el yml codifica el nuevo (3.1=Sanidad): sin correspondencias_legacy.yml, 403 M€ de atención primaria y especializada (4.1.2.1/2) se etiquetan soberania y sanidad cae a 353 €/hab. transform.py debe aplicar el legacy para anio≤2016"),
        ({2018},
         "[COBERTURA] BUG ABIERTO: la ventana _ORG_PROGRAMA_WINDOWS[2018]=(230,523) corta el bloque de servicios sociales (mayores/discapacidad/dependencia), que está en págs. 567-626 con repetición en 732+ (requiere dedup). Solo 53 filas y 9 conceptos: dependencia −83 %, y discapacidad, diversidad e igualdad caen a 0 y reaparecen en 2019"),
        ({2024}, "[FUENTE] Depende del suplemento manual de código: sin él pierde educación y el total baja de 1,947 a 1,317 B"),
        (TODOS, "[MAPEO] El extractor emite códigos punteados (3.1.1.1) que el correspondencias RAÍZ de R no reconoce: la asignación depende del fallback python_local_fallback en transformacion.R. Si sanidad sale 0/NULL en la DB, ese fallback no se aplicó"),
    ],
    "mad": [
        (TODOS, "[DOBLE CONTEO] RE_CENTRO restringido a \\d{4,5} (solo centros): antes capturaba también los agregados de sección de 2 dígitos y ambos recibían concepto (total 2015 32,8 → 20,9 B)"),
        (TODOS, "[COBERTURA] RESIDUAL ABIERTO: infra-captura por proxy-centro (Libro 03). Educación 2015 ~2,1 B vs ~4,3 B reales porque centros como 'D.G. DE RECURSOS HUMANOS' (~2 B) no llevan keyword. Usar cuotas relativas, no importes absolutos; el arreglo definitivo es el Libro 04 (memoria por programas)"),
        (TODOS, "[NULL ESTRUCTURAL] salud_mental sin ninguna línea en toda la serie: revisar si es hueco del catálogo o competencia no desagregada"),
        ({2020, 2021}, "[PRÓRROGA] Prórroga: 2020≡2019 y 2021≡2020 en el staging"),
        ({2023}, "[PRÓRROGA] Prórroga: 2023≡2022 en el staging"),
    ],
    "mur": [
        (TODOS, "[FUENTE] Descarga sensible a Radware/ShieldSquare: el motor descarta los ficheros con captcha y los cuenta en notes. Si caen filas o conceptos al re-extraer, revisar notes antes de dar el año por bueno; regenerar con tools/mur_download.py desde IP no bloqueada"),
        ({2015}, "[FUENTE] Rama PDF (Ley), no visor HTML: hay que seguir las continuaciones del encabezado; buscándolo de forma literal solo se recuperan ~59 programas y 2,98 B€ en vez de 150 filas y 4,91 B€"),
        ({2026}, "[PRÓRROGA] Ejercicio idéntico a 2025 en el staging: verificar si es prórroga real o un fallo de carga del visor HTML"),
    ],
    "nav": [
        (TODOS, "[UNIDAD] Importes en céntimos: dividir entre 100. Si la serie sale ×100, es error de unidad"),
        (TODOS, "[FUENTE] El motor depende de que el HTML siga embebiendo 'var breakdowns'; si el portal cambia de versión cae a nav-pendiente con 0 filas"),
        ({2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026},
         "[CONCEPTO] discapacidad deja de mapearse desde 2019 (12 conceptos en vez de 13): no asumir su presencia ni leer la ausencia como cero"),
    ],
    "pvc": [
        (TODOS, "[DOBLE CONTEO] Filtro Tipo=1 + Entidad 100/2xx: el motor tidy previo sumaba gasto E ingreso y todas las entidades (~38 B€ frente a ~13,5 B reales) y contaminaba el total y direccion. Cualquier dato anterior al fix 2026-07-01 está inflado ~2×"),
        (TODOS, "[CONCEPTO] Aplicar zfill(4) (deuda 0111 fuera de direccion) y el mapeo estatal→vasco: empleo 321*, igualdad 3221/3223, diversidad 3122, salud_mental 4116"),
        (TODOS, "[PERÍMETRO] El total vasco excluye por diseño las transferencias a Diputaciones Forales (función 91, ~13 B€): es perímetro AdErAu, no el sector público vasco consolidado"),
        (TODOS, "[NULL ESTRUCTURAL] dependencia y discapacidad son competencia foral: no aparecen como programa propio"),
        ({2015, 2016, 2017, 2018, 2019, 2020, 2021}, "[FUENTE] Rama ZIP GASTOSC (pvc-gastosc-funcional)"),
        ({2022}, "[SEAM] Cambio de rama ZIP GASTOSC → CSV tidy"),
        ({2019, 2023}, "[FUENTE] Es PROYECTO de presupuesto, no Aprobado (no existe versión Aprobado en el dataset; el Aprobado de 2019 devuelve HTTP 404). Marcarlo como tal en cualquier gráfico"),
        ({2025, 2026}, "[MAGNITUD] Sanidad 2313-2408 €/hab por encima de la banda: inversión vasca real, baseline conocido, no es bug"),
    ],
    "val": [
        (TODOS, "[UNIDAD] Importes en miles: aplicar ×1000"),
        (TODOS, "[FUENTE] Distinguir stubs (secciones inexistentes, HTML 404 con extensión .pdf) de huecos reales (sección con menú válido y sin PDF): estos últimos deben reportarse en notes, no desaparecer en silencio"),
        ({2015}, "[FUENTE] SIN FUENTE: el portal GVA devuelve 404 para ejercicios ≤2015. La serie útil arranca en 2016"),
        ({2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023},
         "[CONCEPTO] Códigos legacy NNN.NN: hay que ENTRECOMILLARLOS en el YAML ('313.60', no 313.60, que YAML lee como float 313.6 y nunca casa). 011* → deuda (4,1 B€ en 2016 iban a NULL), 313.60/.70 → dependencia, 313.30 → diversidad, 313.20 → salud_mental. Sin el fix, direccion saltaba de 0,9 B (2016) a 10,7 B (2026) por artefacto"),
        ({2026}, "[COBERTURA] La sección sec26 devuelve 404 en GVA: falta el gasto de esa sección (reportado en notes); el total del año queda ligeramente por debajo del real"),
    ],
}

# ---------------------------------------------------------------------------
# B. Hallazgos automáticos por año, recalculados desde el staging
# ---------------------------------------------------------------------------
UMBRAL_CODIGO_MATERIAL = 0.005   # 0,5 % del total del año
MAX_INESTABLES_POR_ANIO = 3
MAX_CODIGOS_DUP_LISTADOS = 6


def auto_por_anio(filas: list[dict]) -> dict[int, list[str]]:
    anios, mat, detalle, total_anio, n_anio = agregar(filas)
    alertas, inestables, duplicados = detectar_alertas(anios, mat, detalle, total_anio, filas)
    out: dict[int, list[str]] = collections.defaultdict(list)

    # B1 · saltos / apariciones / desapariciones de concepto
    for anio, concepto, tipo, det, _imp in alertas:
        det = det.replace(" ⚠", "")
        etiqueta = "SALTO" if tipo == "SALTO" else tipo
        if concepto == "TOTAL":
            out[anio].append(f"[ALERTA {etiqueta}] Total extraído del ejercicio: {det}")
        else:
            out[anio].append(f"[ALERTA {etiqueta}] {concepto}: {det}")

    # B2 · códigos duplicados dentro del ejercicio
    dup_anio = collections.defaultdict(list)
    for anio, cod, _con, imp, n in duplicados:
        dup_anio[anio].append((imp, cod, n))
    for anio, items in dup_anio.items():
        items.sort(reverse=True)
        tot = sum(i[0] for i in items)
        cods = ", ".join(f"{c} (×{n})" for _i, c, n in items[:MAX_CODIGOS_DUP_LISTADOS])
        resto = f" y {len(items) - MAX_CODIGOS_DUP_LISTADOS} más" if len(items) > MAX_CODIGOS_DUP_LISTADOS else ""
        out[anio].append(
            f"[DOBLE CONTEO] {len(items)} códigos repetidos dentro del ejercicio ({meur(tot)} M€ acumulados): {cods}{resto}. "
            "Comprobar contra el documento original si son secciones distintas o duplicación"
        )

    # B3 · códigos que cambian de concepto respecto al año anterior
    cod_anio_con = collections.defaultdict(dict)
    cod_anio_imp = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in filas:
        cod_anio_con[r["codigo"]].setdefault(r["anio"], set()).add(r["concepto"])
        cod_anio_imp[r["codigo"]][r["anio"]] += r["importe_eur"]
    cambios = collections.defaultdict(list)
    for cod, por_anio in cod_anio_con.items():
        ys = sorted(por_anio)
        for a, b in zip(ys, ys[1:]):
            if por_anio[a] != por_anio[b]:
                imp = max(cod_anio_imp[cod][a], cod_anio_imp[cod][b])
                if total_anio.get(b) and imp / total_anio[b] >= UMBRAL_CODIGO_MATERIAL:
                    de = "/".join(sorted(x if x != SIN else "NULL" for x in por_anio[a]))
                    aa = "/".join(sorted(x if x != SIN else "NULL" for x in por_anio[b]))
                    cambios[b].append((imp, cod, de, aa))
    for anio, items in cambios.items():
        items.sort(reverse=True)
        for imp, cod, de, aa in items[:MAX_INESTABLES_POR_ANIO]:
            out[anio].append(
                f"[MAPEO] El código {cod} ({meur(imp)} M€) cambia de concepto respecto al año anterior: {de} → {aa}. "
                "Verificar si es reclasificación real del origen o fallo del keyword/prefijo"
            )
        if len(items) > MAX_INESTABLES_POR_ANIO:
            out[anio].append(f"[MAPEO] Otros {len(items) - MAX_INESTABLES_POR_ANIO} códigos materiales cambian de concepto este año (ver trazabilidad §4.2)")
    return out


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--in", dest="entrada", required=True, type=Path)
    ap.add_argument("--out", dest="salida", required=True, type=Path)
    ap.add_argument("--hoja", default="estado de ext")
    args = ap.parse_args()

    filas = cargar(None)
    por_ccaa = collections.defaultdict(list)
    for r in filas:
        por_ccaa[r["ccaa_id3"]].append(r)
    auto = {id3: auto_por_anio(rs) for id3, rs in por_ccaa.items()}

    wb = openpyxl.load_workbook(args.entrada)
    ws = wb[args.hoja]
    hdr = [c.value for c in ws[1]]
    col = hdr.index("Nota") + 2 if "Nota" in hdr else ws.max_column + 1

    cel = ws.cell(row=1, column=col, value="Correcciones")
    cel.font = Font(bold=True)
    cel.fill = PatternFill("solid", fgColor="FFF2CC")

    n_con = n_sin = 0
    total_items = 0
    for fila in range(2, ws.max_row + 1):
        id3 = ws.cell(row=fila, column=1).value
        anio_raw = ws.cell(row=fila, column=3).value
        if not id3 or anio_raw in (None, ""):
            continue
        anio = int(float(anio_raw))
        items: list[str] = []
        for anios, texto in CURADAS.get(id3, []):
            if anios is TODOS or anio in anios:
                items.append(limpiar(texto))
        items.extend(limpiar(t) for t in auto.get(id3, {}).get(anio, []))
        c = ws.cell(row=fila, column=col, value=SEP.join(items) if items else "")
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if items:
            n_con += 1
            total_items += len(items)
        else:
            n_sin += 1
    ws.column_dimensions[cel.column_letter].width = 120

    # hoja auxiliar: catálogo de correcciones curadas (trazabilidad de la fuente)
    if "Catalogo correcciones" in wb.sheetnames:
        del wb["Catalogo correcciones"]
    cat = wb.create_sheet("Catalogo correcciones")
    cat.append(["id3", "Años a los que aplica", "Tipo", "Corrección", "Origen"])
    for c in cat[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="FFF2CC")
    for id3 in sorted(CURADAS):
        for anios, texto in CURADAS[id3]:
            tipo = texto.split("]")[0].lstrip("[") if texto.startswith("[") else ""
            cuerpo = texto.split("] ", 1)[1] if "] " in texto else texto
            cat.append([
                id3,
                "todos" if anios is TODOS else ", ".join(str(a) for a in sorted(anios)),
                tipo, limpiar(cuerpo), f"limitaciones-{id3}.md",
            ])
    cat.append(["—", "por año", "AUTOMÁTICO",
                "Alertas de salto/aparición/desaparición de concepto, códigos duplicados en el ejercicio y "
                "códigos que cambian de concepto respecto al año anterior",
                "trazabilidad-<id3>.md (recalculado desde 1_extraccion/staging_gasto.rds)"])
    for w, letra in zip((8, 30, 18, 120, 34), "ABCDE"):
        cat.column_dimensions[letra].width = w
    for fila in cat.iter_rows(min_row=2):
        fila[3].alignment = Alignment(wrap_text=True, vertical="top")

    args.salida.parent.mkdir(parents=True, exist_ok=True)
    wb.save(args.salida)
    print(f"✓ {args.salida}")
    print(f"  filas con correcciones: {n_con} · sin correcciones: {n_sin} · items totales: {total_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
