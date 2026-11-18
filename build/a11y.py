from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
P = [  # file, fg, bg, ratio, where used
("01-ink-on-paper","16141A","FAF8F4","17.22","Body text, headlines, logo"),
("02-plum-on-paper","5B3A70","FAF8F4","8.66","Links, italic accent words, [n] citations"),
("03-muted-on-paper","5B5862","FAF8F4","6.56","Captions, eyebrow labels, microcopy"),
("04-paper-on-plum","FAF8F4","5B3A70","8.66","Primary button label"),
("05-ink-on-plumtint","16141A","EFE8F3","15.23","Founder note, callout text"),
("06-plum-on-plumtint","5B3A70","EFE8F3","7.66","Links inside callouts"),
("07-muted-on-plumtint","5B5862","EFE8F3","5.80","Reasons in the 'what the checker cut' block"),
("08-green-on-paper","1F7A4D","FAF8F4","5.01","'backed' claim label"),
("09-green-on-greentint","1F7A4D","E3F2EA","4.59","'97% grounded' score chip"),
("10-amber-on-paper","B45309","FAF8F4","4.73","'partly' claim label"),
("11-amber-on-white","B45309","FFFFFF","5.02","'partly' label on the white brief card"),
("12-red-on-paper","B42318","FAF8F4","6.19","Cut-claim strikethrough, form errors"),
("13-paper-on-ink","FAF8F4","16141A","17.22","Final CTA band, footer text"),
("14-lilac-on-ink","C9B3D9","16141A","9.51","Links and logo brackets on ink"),
("15-plum-on-ink-REJECTED","5B3A70","16141A","1.98","Not used. This failure is why lilac exists"),
]
def verdict(r):
    r=float(r)
    if r>=7: return '<b class="ok">AAA</b>'
    if r>=4.5: return '<b class="ok">AA</b>'
    return '<b class="bad">Fail</b>'
def sw(h): return f'<span class="sw" style="background:#{h}"></span><span class="mono">#{h}</span>'
rows = "".join(f'<tr><td>{sw(f)}</td><td>{sw(b)}</td><td class="mono r">{r}:1</td><td>{verdict(r)}</td><td>{w}</td></tr>' for _,f,b,r,w in P)
shots = ""
for i in range(0,len(P),2):
    cells="".join(f'''<figure><img src="../accessibility/shots/{n}.png"><figcaption><span class="mono">{n[:2]}</span> · #{f} on #{b} · <span class="mono">{r}:1</span> · {verdict(r)}<br><span class="use">{w}</span></figcaption></figure>''' for n,f,b,r,w in P[i:i+2])
    shots += f'<section class="pg shots"><div class="hd"><span class="eyebrow">WebAIM Contrast Checker · screenshots {i+1}–{min(i+2,len(P))} of {len(P)}</span></div><div class="grid">{cells}</div></section>'
html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="brand.css"><style>
@page{{size:11in 8.5in;margin:0}}
.pg{{width:11in;height:8.5in;padding:.55in .65in;page-break-after:always;overflow:hidden;position:relative}}
h1{{font:600 30pt Newsreader;line-height:1.05;margin:.12in 0 .08in}}
.lede{{font-size:10.5pt;line-height:1.5;max-width:8.6in;color:var(--ink)}}
table{{width:100%;border-collapse:collapse;margin-top:.2in;font-size:9.2pt}}
th{{text-align:left;font:600 7.5pt "IBM Plex Sans";letter-spacing:.12em;text-transform:uppercase;color:var(--muted);border-bottom:1.5px solid var(--ink);padding:5px 6px}}
td{{padding:4.2px 6px;border-bottom:1px solid var(--line);vertical-align:middle}}
td.r{{text-align:right;font-weight:500}} tr:last-child td{{background:#F6EDEC}}
.sw{{display:inline-block;width:12px;height:12px;border:1px solid var(--line);vertical-align:-2px;margin-right:6px}}
.ok{{color:var(--green)}} .bad{{color:var(--red)}}
.foot{{position:absolute;bottom:.4in;left:.65in;right:.65in;font-size:8pt;color:var(--muted);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:6px}}
.hd{{border-top:3px solid var(--ink);padding-top:6px;margin-bottom:.15in}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:.35in}}
figure img{{width:100%;height:6.05in;object-fit:contain;object-position:top left;border:1px solid var(--line);background:#fff}}
figcaption{{font-size:9pt;margin-top:6px;line-height:1.45}} .use{{color:var(--muted)}}
</style></head><body>
<section class="pg"><div class="rule"></div><div class="eyebrow" style="margin-top:6px">INFO7375 Branding &amp; AI · Assignment 9 · Color accessibility check</div>
<h1>Groundline <span class="brief">Brief</span>: every text pairing, tested</h1>
<p class="lede">I tested all 14 text/background combinations the website uses, plus one I deliberately rejected, in the WebAIM Contrast Checker (webaim.org/resources/contrastchecker). <b>All 14 pass WCAG AA</b> for normal text (4.5:1 or higher), and 7 also pass AAA (7:1 or higher). Plum on Ink fails at 1.98:1, so on dark backgrounds the brand swaps plum for lilac #C9B3D9 (9.51:1). State is never shown by color alone: backed lines carry a check and the word “backed”, partly-backed lines the word “partly”, and cut lines a strikethrough.</p>
<table><tr><th>Foreground</th><th>Background</th><th style="text-align:right">Ratio</th><th>WCAG</th><th>Where it's used on the site</th></tr>{rows}</table>
<div class="foot"><span>Agnel Salve · Groundline Brief · A9</span><span>Tested in WebAIM, 18 Nov 2026 · screenshots follow</span></div></section>
{shots}</body></html>'''
(ROOT/"build"/"a11y.html").write_text(html, encoding="utf-8")
