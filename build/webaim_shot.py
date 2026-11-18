import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
PAIRS = [l.split() for l in sys.argv[2:]]
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width": 1100, "height": 1400}, device_scale_factor=2)
    for name, fg, bg in PAIRS:
        pg.goto(f"https://webaim.org/resources/contrastchecker/?fcolor={fg}&bcolor={bg}", wait_until="networkidle")
        pg.wait_for_timeout(600)
        el = pg.locator("#main") if pg.locator("#main").count() else pg.locator("main")
        el.first.screenshot(path=str(out / f"{name}.png"))
        print(name, pg.locator("#ratio").inner_text() if pg.locator("#ratio").count() else "?")
    b.close()
