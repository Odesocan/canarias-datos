"""
extractors/ext.py — Extremadura.

Tomo II EIG estructura:

    02006 SECRETARÍA GENERAL DE IGUALDAD Y CONCILIACIÓN          ← servicio
    253A IGUALDAD DE GÉNERO Y ESTRATEGIA CONTRA LA VIOLENCIA ... ← programa (sin importe)
    CAPITULO ARTÍCULO CONCEPTO ...                               ← header tabla
    1 10 100 10000 CA RETRIBUCIONES ... 80.587                   ← subconcepto
    TOTAL CAPITULO GASTOS DE PERSONAL  4.447.823                 ← suma de capítulo
    ...
    TOTAL PROGRAMA  X.XXX.XXX                                    ← (a veces sí, a veces no)

Estrategia: detectar cabecera de programa y acumular `TOTAL CAPITULO` siguientes
hasta la próxima cabecera de programa o de servicio. Suma = importe del programa.
"""
from __future__ import annotations

import re
from pathlib import Path

from .._common import base
from .._common.base import NUM_RE, make_row, ExtractionResult


# Cabecera de programa: 3 dígitos + letra al inicio + denominación (no termina en número)
RE_PROGRAMA_HDR = re.compile(
    r"^\s*(?P<codigo>\d{3}[A-Z])\s+(?P<denom>[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ \-,/().ÜÑ]{5,})$"
)
# Línea TOTAL CAPITULO ... <importe>  (CAPÍTULO con o sin tilde: la sección de
# organismos autónomos la escribe con tilde, la de administración general sin)
RE_TOTAL_CAP = re.compile(
    rf"^\s*TOTAL\s+CAP[IÍ]TULO\s+.+?\s+(?P<importe>{NUM_RE})\s*$"
)
# Línea TOTAL PROGRAMA <importe> (cuando aparece)
RE_TOTAL_PROG = re.compile(
    rf"^\s*TOTAL\s+PROGRAMA\s+.*?\s*(?P<importe>{NUM_RE})\s*$"
)
# Cabecera de servicio (5 dígitos + denom SIN importe). El charset de la denom
# excluye dígitos para no confundir con líneas de subconcepto económico de 5
# dígitos que SÍ terminan en importe (p.ej. "12001 CA SUELDOS ... 25.515.523").
RE_SERVICIO_HDR = re.compile(
    r"^\s*(?P<codigo>\d{5})\s+(?P<denom>[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ \-,/().ÜÑ]{5,})$"
)


def _flush(rows: list, current, totales_cap, anio: int, p_num):
    if current is None:
        return
    codigo, denom, hdr_pagina = current
    importe = sum(totales_cap)
    rows.append(make_row(pagina=hdr_pagina, codigo=codigo, denominacion=denom,
                          importe=importe, anio=anio))


def _from_eig_pdf(input_path: Path, anio: int) -> ExtractionResult:
    rows: list[dict] = []
    seen = set()
    try:
        current = None              # (codigo, denom, page_inicio)
        current_servicio = None     # código de servicio (5 díg) abierto
        totales_cap: list[float] = []
        for p_num, text in base.iter_pdf_text(input_path):
            for line in text.splitlines():
                line = line.strip()
                if not line:
                    continue

                # 1) Cabecera de programa
                m_prog = RE_PROGRAMA_HDR.match(line)
                if m_prog and not line.startswith("TOTAL"):
                    # La cabecera del programa se repite como encabezado en CADA
                    # página del programa. Si es el MISMO código que el programa
                    # abierto, es un encabezado de continuación: ignorar para no
                    # resetear el acumulador de capítulos (bug que dropeaba
                    # programas multipágina, p.ej. 212B en 2024).
                    if current is not None and m_prog.group("codigo") == current[0]:
                        continue
                    # Volcar programa anterior
                    if current is not None and totales_cap:
                        codigo, denom, hdr_pagina = current
                        key = (codigo, denom[:30])
                        if key not in seen:
                            seen.add(key)
                            rows.append(make_row(pagina=hdr_pagina, codigo=codigo,
                                                  denominacion=denom,
                                                  importe=sum(totales_cap), anio=anio))
                    current = (m_prog.group("codigo"), m_prog.group("denom").strip(), p_num)
                    totales_cap = []
                    continue

                # 2) TOTAL PROGRAMA explícito (precedencia sobre suma capitulos)
                m_tp = RE_TOTAL_PROG.match(line)
                if m_tp and current is not None:
                    codigo, denom, hdr_pagina = current
                    key = (codigo, denom[:30])
                    if key not in seen:
                        seen.add(key)
                        rows.append(make_row(pagina=hdr_pagina, codigo=codigo,
                                              denominacion=denom,
                                              importe=m_tp.group("importe"), anio=anio))
                    current = None
                    totales_cap = []
                    continue

                # 3) TOTAL CAPITULO — acumular
                m_tc = RE_TOTAL_CAP.match(line)
                if m_tc and current is not None:
                    totales_cap.append(base.parse_eur(m_tc.group("importe")))
                    continue

                # 4) Cambio de servicio cierra programa abierto sin TOTAL.
                #    El encabezado de servicio se repite en cada página: sólo
                #    cuenta como cambio si el código es NUEVO (si no, es runner).
                m_svc = RE_SERVICIO_HDR.match(line)
                if m_svc:
                    if m_svc.group("codigo") == current_servicio:
                        continue
                    current_servicio = m_svc.group("codigo")
                    if current is not None:
                        if totales_cap:
                            codigo, denom, hdr_pagina = current
                            key = (codigo, denom[:30])
                            if key not in seen:
                                seen.add(key)
                                rows.append(make_row(pagina=hdr_pagina, codigo=codigo,
                                                      denominacion=denom,
                                                      importe=sum(totales_cap), anio=anio))
                        current = None
                        totales_cap = []

        # Cierre final
        if current is not None and totales_cap:
            codigo, denom, hdr_pagina = current
            key = (codigo, denom[:30])
            if key not in seen:
                rows.append(make_row(pagina=hdr_pagina, codigo=codigo, denominacion=denom,
                                      importe=sum(totales_cap), anio=anio))

    except ImportError:
        return ExtractionResult(rows=[], motor="ext", notes="pdfplumber no disponible")

    return ExtractionResult(rows=rows, motor="ext-tomo-eig-suma-capitulos")


# --------------------------------------------------------------------------- #
# Motor PRIMARIO: tabla "Resumen por programa" de la Ley de Presupuestos (DOE).
#
# La Ley (DOE) trae un anexo con la tabla CONSOLIDADA por programa:
#     Programa Denominación Programa Ley 2019
#     111A Actividad legislativa            13.929.940
#     212B Atención primaria de salud      645.812.045
#     222A Educación infantil y primaria   396.934.942
#     ...
# Cada programa aparece UNA vez con su total real (≈ presupuesto consolidado).
# Mucho más fiable que sumar el detalle EIG (que infravalora educación ~3x por
# el dedup sobre un documento no consolidado). Ver logs/progreso.md 2026-06-30.
#
# Fila: <3 díg + letra> <denom opcional> <importe con separador de miles '.'>.
# Sólo se aceptan filas de PÁGINAS-RESUMEN (≥5 filas-programa en la página), lo
# que aísla la tabla del detalle (cuyas líneas empiezan por capítulo "1 10 ...").
RE_RESUMEN_ROW = re.compile(
    r"^\s*(?P<codigo>\d{3}[A-Z])\s+(?P<resto>.*?)(?P<importe>\d{1,3}(?:\.\d{3})+)\s*$"
)


def _from_resumen_pdf(input_path: Path, anio: int) -> ExtractionResult:
    # 1ª pasada: localizar filas-programa por página
    por_pagina: dict[int, list[tuple[str, str, int]]] = {}
    try:
        for p_num, text in base.iter_pdf_text(input_path):
            hits = []
            for line in text.splitlines():
                m = RE_RESUMEN_ROW.match(line.strip())
                if not m:
                    continue
                denom = m.group("resto").strip(" .-")
                importe = int(m.group("importe").replace(".", ""))
                hits.append((m.group("codigo"), denom, importe))
            if len(hits) >= 5:        # página-resumen (no detalle)
                por_pagina[p_num] = hits
    except ImportError:
        return ExtractionResult(rows=[], motor="ext-resumen", notes="pdfplumber no disponible")

    # Consolida: un importe por código (la tabla lo lista una vez; si reapareciera
    # en varias páginas-resumen, nos quedamos con el mayor = total de programa).
    mejor: dict[str, tuple[str, int]] = {}
    for p_num in sorted(por_pagina):
        for codigo, denom, importe in por_pagina[p_num]:
            if codigo not in mejor or importe > mejor[codigo][1]:
                # conserva la denominación más larga vista
                prev_denom = mejor.get(codigo, ("", 0))[0]
                d = denom if len(denom) >= len(prev_denom) else prev_denom
                mejor[codigo] = (d, importe)

    rows = [make_row(pagina=None, codigo=c, denominacion=(d or c), importe=float(imp), anio=anio)
            for c, (d, imp) in sorted(mejor.items())]
    return ExtractionResult(rows=rows, motor="ext-doe-resumen-programa")


def extract(input_path: Path, anio: int) -> ExtractionResult:
    # Primario: tabla resumen por programa (Ley DOE). Si no hay tabla resumen
    # (p.ej. el documento es sólo el detalle EIG), cae al motor EIG.
    res = _from_resumen_pdf(input_path, anio)
    if len(res.rows) >= 30:
        return res
    return _from_eig_pdf(input_path, anio)
