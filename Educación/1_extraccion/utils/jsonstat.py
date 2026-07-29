"""
Decodificador de respuestas JSON-stat 2.0 (formato de la API de Eurostat).

Una respuesta JSON-stat almacena los valores en un diccionario plano `value`
indexado por posición lineal (row-major) sobre el producto cartesiano de las
dimensiones. Este módulo lo desenrolla a filas tidy: una lista de dicts, cada
uno con los códigos de todas las dimensiones más su `valor`.
"""

from typing import Dict, List


def a_filas(j: Dict) -> List[Dict]:
    """Convierte un objeto JSON-stat en una lista de filas {dim: codigo, ..., valor}."""
    ids = j["id"]                 # nombres de dimensiones en orden
    size = j["size"]              # tamaño de cada dimensión
    dim = j["dimension"]
    values = j.get("value", {}) or {}

    # posición -> código, para cada dimensión
    pos2code = {}
    for d in ids:
        index = dim[d]["category"]["index"]
        if isinstance(index, dict):
            pos2code[d] = {v: k for k, v in index.items()}
        else:  # a veces es una lista de códigos
            pos2code[d] = {i: code for i, code in enumerate(index)}

    # strides row-major
    n = len(size)
    strides = [1] * n
    for i in range(n - 2, -1, -1):
        strides[i] = strides[i + 1] * size[i + 1]

    # `value` en JSON-stat 2.0 puede venir como dict disperso {indice: valor} o
    # como array denso [valor, ...] (ambos válidos). Soportamos las dos formas.
    items = values.items() if isinstance(values, dict) else enumerate(values)

    filas = []
    for lin_key, val in items:
        if val is None:                 # celda vacía (habitual en arrays densos)
            continue
        lin = int(lin_key)
        fila = {}
        for i, d in enumerate(ids):
            fila[d] = pos2code[d][(lin // strides[i]) % size[i]]
        fila["valor"] = val
        filas.append(fila)
    return filas
