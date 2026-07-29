#!/usr/bin/env python3
"""Builder de sidecar pagetext RESUMABLE y sin re-iteración O(n^2).

A diferencia de tools/build_pagetext_cache.py (que re-itera todas las páginas ya
cacheadas en cada llamada), este salta DIRECTO a la primera página no cacheada
por índice (pdfplumber es indexable), así el coste por llamada es constante.
Procesa `chunk` páginas nuevas contiguas y persiste. Compatible con el mismo
sidecar `<pdf>.pagetext.json` que lee _common/base.py.

Uso: python3 ext_cache_fast.py <pdf> [chunk]
"""
import json
import sys
import time
from pathlib import Path

import pdfplumber


def main() -> int:
    pdf_path = Path(sys.argv[1])
    chunk = int(sys.argv[2]) if len(sys.argv) > 2 else 260
    cache_path = pdf_path.with_suffix(pdf_path.suffix + ".pagetext.json")
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {"complete": False, "pages": {}}
    if cache.get("complete"):
        print(f"OK ya completo {len(cache['pages'])}")
        return 0
    t0 = time.time()
    done = 0
    with pdfplumber.open(str(pdf_path)) as pdf:
        total = len(pdf.pages)
        # primera página (1-based) que falta, asumiendo caché contiguo
        start = 1
        while str(start) in cache["pages"]:
            start += 1
        i = start
        while i <= total and done < chunk:
            page = pdf.pages[i - 1]
            cache["pages"][str(i)] = page.extract_text() or ""
            try:
                page.flush_cache()
                page.get_textmap.cache_clear()
            except Exception:
                pass
            done += 1
            i += 1
    if len(cache["pages"]) >= total:
        cache["complete"] = True
    cache["total"] = total
    cache_path.write_text(json.dumps(cache))
    print(f"OK +{done} págs {time.time()-t0:.1f}s; {len(cache['pages'])}/{total}; complete={cache['complete']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
