"""render.py page.html out.pdf|out.png [WxH css px for png] [scale]"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()


def edge_cli_pdf():
    """Fallback when Playwright can't launch Edge: Edge's own headless print."""
    import os, subprocess, tempfile
    edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    prof = tempfile.mkdtemp(prefix="edge-pdf-")  # fresh profile: no cached page
    subprocess.run([edge, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={prof}",
                    "--virtual-time-budget=5000", f"--print-to-pdf={out}", src.as_uri() + "?v=" + str(os.getpid())], check=True, timeout=120)


if out.suffix == ".pdf":
    try:
        import playwright  # noqa: F401
        with sync_playwright() as _p:
            _p.chromium.launch(channel="msedge").close()
    except Exception:
        edge_cli_pdf()
        print("wrote", out, "(edge cli)")
        sys.exit(0)

with sync_playwright() as p:
    try:
        b = p.chromium.launch(channel="msedge")
    except Exception:
        b = p.chromium.launch()
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
