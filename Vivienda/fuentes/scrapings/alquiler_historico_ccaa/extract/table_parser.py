"""
Parser de la tabla de histórico de precios de alquiler de Idealista.
Extrae datos de la tabla HTML de la página de histórico de Idealista.
"""

import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup

from utils.logger import setup_logger

logger = setup_logger("table_parser")


class HistoricoTableParser:
    """
    Parsea la tabla de evolución de precios de alquiler de la página
    de histórico de Idealista.

    La tabla contiene columnas:
    - Mes (ej: "Marzo 2026")
    - Precio m² (ej: "12,5 €/m²")
    - Variación mensual (ej: "1,2%")
    - Variación trimestral (ej: "3,5%")
    - Variación anual (ej: "8,1%")
    """

    def __init__(self, html: str, comunidad_info: Dict):
        self.soup = BeautifulSoup(html, "html.parser")
        self.comunidad_info = comunidad_info
        self._fecha_extraccion = datetime.now(timezone.utc).isoformat()

    def parse_table(self) -> List[Dict[str, Any]]:
        """
        Extrae todas las filas de la tabla de histórico.
        Intenta múltiples estrategias de selector para robustez.

        Returns:
            Lista de diccionarios con datos crudos por fila.
        """
        table = self._find_table()
        if not table:
            logger.warning(
                f"No se encontró tabla de histórico para "
                f"{self.comunidad_info['nombre']}"
            )
            return []

        rows = []
        tbody = table.find("tbody")
        tr_elements = tbody.find_all("tr") if tbody else table.find_all("tr")

        for tr in tr_elements:
            cells = tr.find_all("td")
            if len(cells) < 2:
                continue

            row = self._parse_row(cells)
            if row:
                rows.append(row)

        logger.info(
            f"Tabla parseada: {len(rows)} filas para "
            f"{self.comunidad_info['nombre']}"
        )
        return rows

    def _find_table(self) -> Optional[Any]:
        """
        Busca la tabla de histórico con múltiples estrategias de selector.
        Las páginas de histórico pueden variar en estructura.
        """
        # Estrategia 1: tabla con clase específica de evolución
        for cls in [
            "priceEvolutionTable",
            "evolution-table",
            "price-evolution",
            "historic-table",
        ]:
            table = self.soup.find("table", class_=cls)
            if table:
                logger.debug(f"Tabla encontrada por clase: {cls}")
                return table

        # Estrategia 2: tabla que contenga encabezados de precio
        for table in self.soup.find_all("table"):
            headers = table.find_all("th")
            header_text = " ".join(th.get_text(strip=True).lower() for th in headers)
            if "precio" in header_text or "€" in header_text:
                logger.debug("Tabla encontrada por contenido de encabezados")
                return table

        # Estrategia 3: tabla dentro de sección de evolución
        for section_cls in ["price-evolution", "evolution", "historic"]:
            section = self.soup.find(class_=re.compile(section_cls, re.I))
            if section:
                table = section.find("table")
                if table:
                    logger.debug(f"Tabla encontrada dentro de sección: {section_cls}")
                    return table

        # Estrategia 4: primera tabla con suficientes filas (>3)
        for table in self.soup.find_all("table"):
            rows = table.find_all("tr")
            if len(rows) > 3:
                # Verificar que tiene datos numéricos (€, %, números)
                text = table.get_text()
                if "€" in text or "%" in text:
                    logger.debug("Tabla encontrada por heurística (filas + datos numéricos)")
                    return table

        return None

    def _parse_row(self, cells) -> Optional[Dict[str, Any]]:
        """
        Parsea una fila de la tabla.
        Adapta la extracción según el número de columnas disponibles.
        """
        try:
            mes_text = cells[0].get_text(strip=True)

            # Validar que parece un mes+año (ej: "Marzo 2026")
            if not mes_text or not any(c.isdigit() for c in mes_text):
                return None

            row = {
                "mes_raw": mes_text,
                "precio_m2_raw": cells[1].get_text(strip=True) if len(cells) > 1 else None,
                "variacion_mensual_raw": cells[2].get_text(strip=True) if len(cells) > 2 else None,
                "variacion_trimestral_raw": cells[3].get_text(strip=True) if len(cells) > 3 else None,
                "variacion_anual_raw": cells[4].get_text(strip=True) if len(cells) > 4 else None,
                "comunidad": self.comunidad_info["nombre"],
                "codigo_ccaa": self.comunidad_info["codigo_ine"],
                "fecha_extraccion": self._fecha_extraccion,
            }

            return row

        except Exception as e:
            logger.debug(f"Error parseando fila: {e}")
            return None
