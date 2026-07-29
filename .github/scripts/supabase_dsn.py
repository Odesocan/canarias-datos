#!/usr/bin/env python3
"""Compone la cadena de conexión de Supabase a partir de los secretos por partes.

Empleo/4_carga/cargar_supabase.py espera SUPABASE_DB_URL, una cadena única,
mientras que el resto de áreas usan SUPABASE_HOST/PORT/DBNAME/USER/PASS. Como
todas apuntan a la misma base y el mismo esquema, la cadena es derivable y no
hace falta dar de alta un secreto adicional.

Se emite en formato **clave=valor** de libpq, no como URI, y es una decisión
deliberada:

  * Una URI obliga a percent-codificar la contraseña. El valor codificado ya no
    coincide con el secreto registrado en GitHub, así que dejaría de estar
    enmascarado en los logs. Una contraseña como `p@ss:w/rd?#&=` además rompe el
    parseo de la URI si no se codifica.
  * En formato clave=valor la contraseña viaja literal entre comillas simples, de
    modo que el enmascarado de SUPABASE_PASS la sigue cubriendo. Solo hay que
    escapar comillas simples y barras invertidas.

psycopg2.connect() acepta ambos formatos indistintamente: los pasa tal cual a
libpq.

Uso desde un workflow (la cadena nunca se imprime en claro):

    DSN="$(python3 .github/scripts/supabase_dsn.py)"
    echo "::add-mask::$DSN"
    export SUPABASE_DB_URL="$DSN"
"""

from __future__ import annotations

import os
import sys

REQUERIDOS = ("SUPABASE_HOST", "SUPABASE_USER", "SUPABASE_PASS")


def cita(valor: str) -> str:
    """Entrecomilla un valor según las reglas de libpq (clave=valor)."""
    return "'" + str(valor).replace("\\", "\\\\").replace("'", "\\'") + "'"


def main() -> int:
    faltan = [v for v in REQUERIDOS if not os.environ.get(v)]
    if faltan:
        print(
            "Faltan secretos para componer la conexión: " + ", ".join(faltan),
            file=sys.stderr,
        )
        return 1

    partes = {
        "host": os.environ["SUPABASE_HOST"],
        "port": os.environ.get("SUPABASE_PORT") or "5432",
        "dbname": os.environ.get("SUPABASE_DBNAME") or "postgres",
        "user": os.environ["SUPABASE_USER"],
        "password": os.environ["SUPABASE_PASS"],
        # Supabase acepta SSL siempre; 'require' es lo que ya usa Educación
        # (4_carga/config_carga.py) y es más estricto que el 'prefer' por defecto.
        "sslmode": os.environ.get("SUPABASE_SSLMODE") or "require",
    }

    print(" ".join(f"{clave}={cita(valor)}" for clave, valor in partes.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
