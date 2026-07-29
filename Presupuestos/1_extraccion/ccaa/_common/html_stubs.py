"""
Plantilla común para extractores HTML pendientes de implementación específica.

Las CCAA siguientes publican sus presupuestos en portales HTML/JS donde el
contenido útil queda detrás de selectores AJAX o frames antiguos:

  - bal: pressuposts.caib.es (frames HTML clásicos)
  - val: hisenda.gva.es (HTML estático multi-tabla)
  - cym: datosabiertos.jcyl.es (CKAN — el endpoint CSV requiere navegación)
  - nav: presupuesto.navarra.es (visor JS)
  - gal: transparencia.xunta.gal (índice HTML, PDFs internos)
  - mur: carm.es/chac/presupuestos (visor móvil HTML)

Cada uno necesita un extractor específico (con BeautifulSoup o Playwright).
Mientras tanto, este módulo es la plantilla común que permite cargar un CSV
adjunto en `fuentes/raw/<ccaa>/<año>/programas.csv` con columnas:
  codigo, denominacion, importe_eur
"""
from __future__ import annotations

import csv
from pathlib import Path

from .base import make_row, ExtractionResult, parse_eur


def stub_extract(input_path: Path, anio: int, ccaa: str, hint: str = "") -> ExtractionResult:
    """Carga un CSV adjunto si existe; si no, devuelve vacío con motivo."""
    candidatos = list(input_path.parent.glob("programas*.csv")) + \
                 list(input_path.parent.glob("partidas*.csv"))
    if not candidatos:
        return ExtractionResult(rows=[], motor=f"{ccaa}-pendiente",
                                 notes=hint or "Adjuntar programas.csv en el mismo directorio")
    src = candidatos[0]
    rows: list[dict] = []
    with src.open("r", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            if r.get("codigo"):
                rows.append(make_row(pagina=None, codigo=r["codigo"],
                                      denominacion=r.get("denominacion",""),
                                      importe=parse_eur(r.get("importe_eur","0")),
                                      anio=anio))
    return ExtractionResult(rows=rows, motor=f"{ccaa}-csv-adjunto")
