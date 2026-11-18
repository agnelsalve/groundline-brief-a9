import sys; sys.path.insert(0, __import__("os").path.dirname(__file__))
from pathlib import Path
from logo import icon
ROOT = Path(__file__).resolve().parent.parent
head = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="brand.css"><style>
body{{width:1584px;height:396px;overflow:hidden;position:relative;background:var(--paper)}}
.ledger{{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,transparent 0 43px,rgba(22,20,26,.05) 43px 44px)}}
.ground{{position:absolute;left:0;right:0;top:318px;height:6px;background:var(--ink)}}
.main{{position:absolute;left:520px;top:62px;width:640px}}
.brand{{display:flex;align-items:center;gap:14px;margin-bottom:22px}}
.brand .wm{{font:600 26px Newsreader;letter-spacing:-.2px}}
h1{{font:600 50px/1.04 Newsreader;letter-spacing:-.6px}}
h1 i{{font-weight:400;color:var(--plum)}}
.sub{{margin-top:18px;font:400 19px/1.4 "IBM Plex Sans";color:var(--muted)}}
.sub b{{color:var(--ink);font-weight:500}}
.card{{position:absolute;left:1196px;top:48px;width:340px;height:270px;border-bottom:none;background:#fff;border:1px solid var(--line);padding:18px 20px;font-size:13.5px;line-height:1.45}}
.card .top{{display:flex;justify-content:space-between;align-items:center;font:500 11.5px "IBM Plex Mono";color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:9px;margin-bottom:10px}}
.chip{{background:var(--gtint);color:var(--green);padding:3px 8px;border-radius:3px}}
.ln{{display:flex;gap:8px;margin:7px 0}} .ln p{{flex:1}}
.n{{font:500 11.5px "IBM Plex Mono";color:var(--plum)}}
.tag{{font:600 9.5px "IBM Plex Sans";letter-spacing:.08em;text-transform:uppercase;width:74px;flex:none;padding-top:3px;white-space:nowrap}}
.badge{{position:absolute;left:20px;right:20px;bottom:14px;border-top:1px solid var(--line);padding-top:9px;font:500 11px 'IBM Plex Mono';color:var(--muted)}}
.ok{{color:var(--green)}} .pt{{color:var(--amber)}} .cut{{color:var(--red)}}
.cut p{{text-decoration:line-through;text-decoration-thickness:1.5px;color:var(--red)}}
</style></head><body><div class="ledger"></div><div class="ground"></div>
<div class="main"><div class="brand">{icon(34)}<span class="wm">Groundline <span class="brief">Brief</span></span></div>
<h1>The competitive brief<br>you can <i>stand behind.</i></h1>
<p class="sub"><b>Agnel Salve</b> · Founder · AI &amp; data engineer. I build AI you can check.</p></div>
<div class="card"><div class="top"><span>wk 45 · brief</span><span class="chip">✓ 97% grounded</span></div>
<div class="ln"><span class="tag ok">✓ backed</span><p>Rival raised its Team plan 12%. <span class="n">[1]</span></p></div>
<div class="ln"><span class="tag ok">✓ backed</span><p>Shipped an AI battlecard tool. <span class="n">[2]</span></p></div>
<div class="ln"><span class="tag pt">partly</span><p>May be moving to mid-market. <span class="n">[3]</span></p></div>
<div class="ln cut"><span class="tag">cut</span><p>Leads the market in AI.</p></div>
<div class="ln"><span class="tag" style="color:var(--muted)">gate</span><p class="mono" style="font-size:11.5px;color:var(--muted);padding-top:2px">49 of 66 off-topic rejected</p></div>
<div class="badge">[G] Checked by Groundline Brief</div></div></body></html>'''
(ROOT/"build"/"linkedin.html").write_text(head, encoding="utf-8")
