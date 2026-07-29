#!/usr/bin/env python3
"""
tools/mur_download.py — Espejado offline del portal CARM Presupuestos.

Lee `xml/31.xml` y `xml/32.xml` del portal de Murcia, descarga todas las
páginas `datos/p228-*.htm`, `p230-*.htm` y `p231-*.htm` y las deja en
`fuentes/raw/mur/<año>/datos/`.

El portal tiene anti-bot (Radware/Shieldsquare).  Pulsado >2 req/seg
salta a captcha durante varios minutos.  Esta utilidad:
  - Calienta la sesión (visita index + xml).
  - Espera 1.5–3 s entre requests.
  - Reintenta hasta 3× con back-off exponencial.
  - Es idempotente (omite ficheros ya descargados).

Lanzar desde la raíz del proyecto:

    python3 tools/mur_download.py --anio 2025

Si quieres reanudar tras un corte:

    python3 tools/mur_download.py --anio 2025 --resume
"""
from __future__ import annotations

import argparse
import os
import random
import re
import sys
import time
from pathlib import Path

import requests

BASES_BY_YEAR = {
    2021: "https://www.carm.es/chac/presupuesto2021/web",
    2022: "https://www.carm.es/chac/leypresup2022/web",
    2023: "https://www.carm.es/chac/leypresup2023/web",
    2024: "https://www.carm.es/chac/leypresup2024/web",
}
BASE_TPL = "https://www.carm.es/chac/presupuestos{anio}/web"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) "
      "Version/17.5 Safari/605.1.15")


def _is_captcha(content: bytes) -> bool:
    head = content[:2500].lower()
    markers = (
        b"radware captcha",
        b"shieldsquare",
        b"_incapsula_resource",
        b"incapsula",
        b"noindex,nofollow",
        b"noindex, nofollow",
    )
    return any(m in head for m in markers)


def _base_for_year(anio: int) -> str:
    return BASES_BY_YEAR.get(anio, BASE_TPL.format(anio=anio))


def _base_from_url(url: str) -> str:
    return url.rstrip("/").replace("/movil/index.html", "/web").replace("/index.html", "")


def _safe_save(target: Path, content: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)


def _list_urls(sess: requests.Session, base: str, raw_dir: Path) -> list[str]:
    """Devuelve la lista de URLs relativas a base ('datos/p2...').
    Saca primero las XML índice y las cachea en raw_dir/xml/."""
    urls: set[str] = set()
    xml_dir = raw_dir / "xml"
    xml_dir.mkdir(parents=True, exist_ok=True)
    for xid in ("31", "32"):
        target = xml_dir / f"{xid}.xml"
        if target.exists() and target.stat().st_size > 1000:
            txt = target.read_bytes().decode("iso-8859-1", "replace")
        else:
            r = sess.get(f"{base}/xml/{xid}.xml", timeout=15)
            r.raise_for_status()
            target.write_bytes(r.content)
            txt = r.content.decode("iso-8859-1", "replace")
        for u in re.findall(r'urlo="(datos/p2[2-3][0-9][^"]+)"', txt):
            if u.endswith(".htm") and any(k in u for k in ("p228-", "p230-", "p231-")):
                urls.add(u)
        time.sleep(1.0)
    return sorted(urls)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--anio", type=int, required=True)
    ap.add_argument("--out", type=Path, default=None,
                    help="raw dir (default: fuentes/raw/mur/<anio>)")
    ap.add_argument("--url", default=None,
                    help="URL del portal móvil/web; se normaliza a .../web")
    ap.add_argument("--max", type=int, default=200,
                    help="Tope de descargas por ejecución")
    ap.add_argument("--delay-base", type=float, default=1.8,
                    help="Segundos entre requests (base; random jitter +0..1)")
    ap.add_argument("--resume", action="store_true",
                    help="Continúa solo con lo que falta (idempotente)")
    args = ap.parse_args()

    out_dir = args.out or Path(f"fuentes/raw/mur/{args.anio}")
    base = _base_from_url(args.url) if args.url else _base_for_year(args.anio)
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Referer": f"{base}/index.html",
    })

    # Warm-up
    sess.get(f"{base}/index.html", timeout=15)
    time.sleep(0.8)

    urls = _list_urls(sess, base, out_dir)
    print(f"[mur] catálogo: {len(urls)} URLs", file=sys.stderr)

    pending: list[str] = []
    for u in urls:
        target = out_dir / u
        if args.resume and target.exists() and target.stat().st_size > 1000:
            if not _is_captcha(target.read_bytes()):
                continue
        pending.append(u)
    print(f"[mur] pendientes: {len(pending)}", file=sys.stderr)

    ok = cap = 0
    for u in pending[: args.max]:
        target = out_dir / u
        target.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(3):
            try:
                r = sess.get(f"{base}/{u}", timeout=15)
            except requests.RequestException as e:
                print(f"  ERR {u}: {e}", file=sys.stderr)
                time.sleep(3 + attempt * 2)
                continue
            if r.status_code == 200 and len(r.content) > 1000 and not _is_captcha(r.content):
                _safe_save(target, r.content)
                ok += 1
                break
            print(f"  RETRY {u}: status={r.status_code} bytes={len(r.content)} "
                  f"blocked={_is_captcha(r.content)}", file=sys.stderr)
            cap += 1
            time.sleep(6 + attempt * 4)
        time.sleep(args.delay_base + random.random())
    print(f"[mur] descargados={ok}  captcha={cap}  total_local="
          f"{sum(1 for p in out_dir.rglob('p2*.htm') if p.stat().st_size > 1000 and not _is_captcha(p.read_bytes()))}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
