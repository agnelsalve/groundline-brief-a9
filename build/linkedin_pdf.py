from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
html = '''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="brand.css"><style>
@page{size:11in 8.5in;margin:0}
.pg{width:11in;height:8.5in;padding:.55in .65in;position:relative;overflow:hidden}
h1{font:600 26pt Newsreader;margin:.1in 0 .06in} p{font-size:10pt;line-height:1.5;max-width:9.2in}
.banner{width:100%;border:1px solid var(--line);display:block;margin-top:.18in}
.cap{font-size:8.5pt;color:var(--muted);margin-top:5px}
.mock{margin-top:.28in;width:5.5in;flex:none;border:1px solid var(--line);background:#fff;border-radius:8px;overflow:hidden;position:relative}
.mock img.b{width:100%;display:block}
.mock .ph{position:absolute;left:.22in;top:.72in;width:1.05in;height:1.05in;border-radius:50%;border:4px solid #fff;object-fit:cover;object-position:center 20%}
.mock .info{padding:.66in .25in .2in}
.mock .nm{font:600 15pt "IBM Plex Sans"} .mock .hl{font-size:9.5pt;color:var(--muted);margin-top:2px}
.row{display:flex;gap:.35in;align-items:flex-start}
.notes{flex:1;margin-top:.24in;font-size:8.7pt;line-height:1.42}
.notes h3{font:600 12pt Newsreader;margin:.0in 0 .04in} .notes li{margin:0 0 .05in .16in}
.foot{position:absolute;bottom:.4in;left:.65in;right:.65in;font-size:8pt;color:var(--muted);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:6px}
</style></head><body><section class="pg"><div class="rule"></div>
<div class="eyebrow" style="margin-top:6px">INFO7375 Branding &amp; AI · Assignment 9 · LinkedIn header, first version</div>
<h1>LinkedIn header · 1584 × 396 px</h1>
<img class="banner" src="../linkedin-header/Salve_Agnel_LinkedIn_Header_1584x396.png">
<div class="cap">Full size: Salve_Agnel_LinkedIn_Header_1584x396.png</div>
<div class="row"><div class="mock"><img class="b" src="../linkedin-header/Salve_Agnel_LinkedIn_Header_1584x396.png"><img class="ph" src="../assets/headshot.png">
<div class="info"><div class="nm">Agnel Salve</div><div class="hl">Founder, Groundline Brief · AI &amp; Data Engineer · MS Information Systems, Northeastern</div></div></div>
<div class="notes"><h3>How it follows the brand system</h3><ul>
<li><b>Tagline</b> in Newsreader, with “stand behind.” in plum italic, the one expressive move the type system allows.</li>
<li><b>The ground line</b>, the logo's base, runs the full width. The brief card stands on it: claims standing on evidence.</li>
<li><b>Product as image:</b> a real brief excerpt with backed / partly / cut states, each labelled in words, not color alone.</li>
<li><b>Profile photo zone:</b> the left ~480 px is left empty (faint ledger rules only) so the photo never covers text, as the preview shows.</li>
<li><b>Clean:</b> one headline, one line of identity, no URL or contact clutter.</li></ul>
<h3 style="margin-top:.1in">Tools</h3><p style="font-size:8.7pt">Composed with Claude (AI) from my A8 tokens (Paper #FAF8F4, Ink #16141A, Plum #5B3A70; Newsreader + IBM Plex) and rendered to PNG at exact LinkedIn size.</p></div></div>
<div class="foot"><span>Agnel Salve · Groundline Brief · A9</span><span>Upload: LinkedIn profile → camera icon on the banner</span></div></section></body></html>'''
(ROOT/"build"/"linkedin_pdf.html").write_text(html, encoding="utf-8")
