#!/usr/bin/env python3
"""Probe del DOM de SelDescargaDC.aspx para entender los selects."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(accept_downloads=True)
    page = ctx.new_page()
    page.goto(
        "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/"
        "PublicacionPresupuestos/aspx/inicio.aspx",
        wait_until="domcontentloaded",
        timeout=60_000,
    )
    print("--- inicio.aspx ---")
    print("title:", page.title())
    links = page.eval_on_selector_all(
        "a", "els => els.map(e => ({href:e.getAttribute('href'), text:e.textContent.trim()})).slice(0,40)"
    )
    for l in links:
        if l["href"]:
            print(" link:", l["href"], "::", l["text"][:60])

    # Try clicking DC
    try:
        page.click("a[href*='SelDescargaDC.aspx']", timeout=8_000)
        page.wait_for_load_state("networkidle", timeout=15_000)
        print("\n--- después de click SelDescargaDC ---")
    except Exception as e:
        print("\n[WARN] click directo falló:", e)
        page.goto(
            "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/"
            "PublicacionPresupuestos/aspx/SelDescargaDC.aspx",
            wait_until="domcontentloaded",
            timeout=30_000,
        )
        print("\n--- navegado directo a SelDescargaDC ---")

    print("title:", page.title())
    print("url:", page.url)
    selects = page.eval_on_selector_all(
        "select",
        "els => els.map(e => ({name:e.name, id:e.id, "
        "options:Array.from(e.options).slice(0,30).map(o=>({v:o.value,t:o.textContent.trim()}))}))",
    )
    for s in selects:
        print(f"\nSELECT name={s['name']} id={s['id']}")
        for o in s["options"][:25]:
            print(f"  v={o['v']!r:>20}  t={o['t'][:70]!r}")

    inputs = page.eval_on_selector_all(
        "input[type='image'], input[type='submit'], button",
        "els => els.map(e => ({tag:e.tagName, name:e.name, id:e.id, value:e.value, type:e.type, text:e.textContent.trim().slice(0,40)}))",
    )
    print("\nBUTTONS:")
    for i in inputs:
        print(" ", i)

    browser.close()
