"""render.py page.html out.pdf|out.png [WxH css px for png] [scale]"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    if out.suffix == ".pdf":
        pg = b.new_page(); pg.goto(src.as_uri(), wait_until="networkidle"); pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
    else:
        w, h = map(int, sys.argv[3].split("x")); s = float(sys.argv[4]) if len(sys.argv) > 4 else 1
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=s)
        pg.goto(src.as_uri(), wait_until="networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": w, "height": h})
    b.close()
print("wrote", out)
