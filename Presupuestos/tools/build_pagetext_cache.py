#!/usr/bin/env python3
"""build_pagetext_cache.py — cachea el texto por página de un PDF grande.

Uso:
    python3 build_pagetext_cache.py <pdf> <chunk_size>

Procesa el PDF en bloques resumibles y deja un sidecar JSON
`<pdf>.pagetext.json` con la lista de textos por página. Pensado para
PDFs de >600 págs. que no caben en una sola llamada de 45 s del sandbox
Cowork: cada invocación procesa el siguiente bloque pendiente y termina;
al completar todas las páginas marca el cache como `complete`.

`iter_pdf_text` (en _common/base.py) detecta el sidecar y lo reutiliza,
de modo que el extractor corre en milisegundos una vez cacheado.
"""
import json
import sys
import time
from pathlib import Path

import pdfplumber


def main() -> int:
    pdf_path = Path(sys.argv[1])
    chunk = int(sys.argv[2]) if len(sys.argv) > 2 else 250
    cache_path = pdf_path.with_suffix(pdf_path.suffix + ".pagetext.json")

    if cache_path.exists():
        cache = json.loads(cache_path.read_text())
    else:
        cache = {"complete": False, "pages": {}}

    if cache.get("complete"):
        print(f"OK cache ya completo: {len(cache['pages'])} páginas")
        return 0

    t0 = time.time()
    done = 0
    with pdfplumber.open(str(pdf_path)) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages, start=1):
            if str(i) in cache["pages"]:
                continue
            cache["pages"][str(i)] = page.extract_text() or ""
            try:
                page.flush_cache()
                page.get_textmap.cache_clear()
            except Exception:
                pass
            done += 1
            if done >= chunk:
                break
    if len(cache["pages"]) >= total:
        cache["complete"] = True
    cache["total"] = total
    cache_path.write_text(json.dumps(cache))
    print(f"OK procesadas {done} págs en {time.time()-t0:.1f}s; "
          f"{len(cache['pages'])}/{total} cacheadas; complete={cache['complete']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
