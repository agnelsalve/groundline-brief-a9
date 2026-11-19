"""python build/brand_visuals.py "Tool name"  -> brand-visuals/Salve_Agnel_A9_BrandVisuals.pdf

Expects brand-visuals/visual-1|2|3.(png|jpg|jpeg|webp).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "brand-visuals"
tool = sys.argv[1] if len(sys.argv) > 1 else "ChatGPT image generation"
md = (D / "IMAGE-PROMPTS.md").read_text(encoding="utf-8")
prompts = re.findall(r"```text\n(.*?)\n```", md, re.S)
INFO = [
    ("The Weekly Brief", "Products card 1",
     "The product is a document you read, not a dashboard: one printed sheet, plum underlines, [n] marks in the margin, coffee at 8 a.m."),
    ("The Fact-Check Log", "Products card 2",
     "“Cut what you can't prove”: the checker's core action is an editor's strikethrough, with green checks on the lines that survived."),
    ("The ‘Checked by’ Badge", "Products card 3",
     "The trust score as a feeling: balanced, settled, nothing to fix. The spirit level is the ground line made physical."),
]

POS = ["center", "center", "78% center"]  # visual 3 is wide: keep the level in frame
HERO = ["", "", "height:auto;margin:.4in 0 .5in"]  # show the wide image uncropped
imgs = []
for i in (1, 2, 3):
    f = next((D / f"visual-{i}.{e}" for e in ("png", "jpg", "jpeg", "webp") if (D / f"visual-{i}.{e}").exists()), None)
    if not f:
        sys.exit(f"missing brand-visuals/visual-{i}.png or .jpg")
    imgs.append(f)

pages = ""
for i, (img, (t, use, why), pr) in enumerate(zip(imgs, INFO, prompts), 1):
    short = pr.split(" Documentary editorial photograph")[0]
    pages += f'''<section class="pg"><div class="rule"></div><div class="eyebrow" style="margin-top:6px">Brand visual {i} of 3 · {use}</div>
<h2>{t}</h2><img class="hero" style="object-position:{POS[i-1]};{HERO[i-1]}" src="../brand-visuals/{img.name}">
<div class="cols"><div><h4>Why it belongs</h4><p>{why}</p></div>
<div><h4>Prompt ({tool})</h4><p class="pr">{short} <span class="m">+ shared style block</span></p></div></div>
<div class="foot"><span>Agnel Salve · Groundline Brief · A9</span><span>{i + 1} / 4</span></div></section>'''

thumbs = "".join(f'<img style="object-position:{POS[k]}" src="../brand-visuals/{p.name}">' for k, p in enumerate(imgs))
html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="brand.css"><style>
@page{{size:11in 8.5in;margin:0}}
.pg{{width:11in;height:8.5in;padding:.5in .65in;position:relative;overflow:hidden;page-break-after:always}}
h1{{font:600 28pt Newsreader;margin:.1in 0 .06in}} h2{{font:600 22pt Newsreader;margin:.06in 0 .12in}}
h4{{font:600 8pt "IBM Plex Sans";letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}}
p{{font-size:9.6pt;line-height:1.5}}
.hero{{width:100%;height:4.85in;object-fit:cover;border-radius:4px;display:block}}
.cols{{display:grid;grid-template-columns:1fr 1.5fr;gap:.35in;margin-top:.16in}}
.pr{{font-size:8.6pt}} .m{{color:var(--muted)}}
.tri{{display:grid;grid-template-columns:repeat(3,1fr);gap:.18in;margin:.25in 0 .2in}}
.tri img{{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:4px}}
.style{{background:var(--tint);padding:.16in .2in;font-size:9pt;line-height:1.5}}
.foot{{position:absolute;bottom:.35in;left:.65in;right:.65in;font-size:8pt;color:var(--muted);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:6px}}
</style></head><body>
<section class="pg"><div class="rule"></div><div class="eyebrow" style="margin-top:6px">INFO7375 Branding &amp; AI · Assignment 9 · AI-generated brand visuals</div>
<h1>Three images, one brand family</h1>
<p style="max-width:9.4in">Generated with {tool}. All three share one style block taken from the A8 photography direction, so they read as a set: documentary, early-morning light, warm paper, ink, and a single plum accent. A8 rules out glowing brains, robots, holograms and AI faces, so every image shows evidence (a page, a pen, a measurement) rather than “AI”. They illustrate the three product cards on the website.</p>
<div class="tri">{thumbs}</div>
<div class="style"><b>Shared style block:</b> Documentary editorial photograph, natural early-morning window light from the left, warm off-white paper tones (#FAF8F4), deep near-black ink, a single muted plum-purple accent (#5B3A70), muted desaturated color grade, shallow depth of field, calm and uncluttered, lots of negative space, 50mm lens. No faces, no robots, no glowing or holographic elements, no readable text, no logos.</div>
<div class="foot"><span>Agnel Salve · Groundline Brief · A9</span><span>1 / 4</span></div></section>
{pages}</body></html>'''

(ROOT / "build" / "brand_visuals.html").write_text(html, encoding="utf-8")
subprocess.run([sys.executable, str(ROOT / "build" / "render.py"), str(ROOT / "build" / "brand_visuals.html"),
                str(D / "Salve_Agnel_A9_BrandVisuals.pdf")], check=True)
