"""ATS resume PDF: single column, real text, subtle brand (ink name, plum headings, ground line)."""
import json
import subprocess
import sys
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = json.loads((ROOT / "build" / "resume_content.json").read_text(encoding="utf-8"))
c = R["contact"]


def section(title, body):
    return f'<section><h2>{title}</h2>{body}</section>'


def bullets(bs):
    return "<ul>" + "".join(f"<li>{e(b)}</li>" for b in bs) + "</ul>"


skills = "".join(f'<p class="sk"><b>{e(k)}:</b> {e(v)}</p>' for k, v in R["skills"])
exp = "".join(
    f'<div class="item"><div class="row"><span><b>{e(x["role"])}</b>, {e(x["org"])}, {e(x["place"])}</span><span class="d">{e(x["dates"])}</span></div>{bullets(x["bullets"])}</div>'
    for x in R["experience"])
proj = "".join(
    f'<div class="item"><div class="row"><span><b>{e(p["name"])}</b> | {e(p["stack"])}</span><span class="d">{e(p["dates"])}</span></div>{bullets(p["bullets"])}</div>'
    for p in R["projects"])
edu = "".join(
    f'<div class="item"><div class="row"><span><b>{e(x["degree"])}</b>, {e(x["org"])}, {e(x["place"])}</span><span class="d">{e(x["dates"])}</span></div>'
    + (f'<p class="note">{e(x["note"])}</p>' if x["note"] else "") + "</div>"
    for x in R["education"])

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Agnel Salve Resume</title><link rel="stylesheet" href="brand.css"><style>
@page{{size:Letter;margin:.42in .55in .38in}}
html,body{{background:#fff}}
body{{font:400 9.2pt/1.28 "IBM Plex Sans",Arial,sans-serif;color:var(--ink)}}
h1{{font:600 22pt/1 Newsreader,Georgia,serif;letter-spacing:-.2px}}
.title{{font:500 10.2pt "IBM Plex Sans";color:var(--plum);margin-top:3px}}
.contact{{margin-top:3px;font-size:9.2pt}}
.ground{{height:2.5px;background:var(--ink);margin:6px 0 2px}}
h2{{font:600 9pt "IBM Plex Sans";letter-spacing:.12em;text-transform:uppercase;color:var(--plum);border-bottom:1px solid var(--line);padding-bottom:1.5px;margin:7px 0 3px}}
.row{{display:flex;justify-content:space-between;gap:12px}} .d{{white-space:nowrap}}
.item{{margin-bottom:3px}}
ul{{margin:1.5px 0 0 14px}} li{{margin:0 0 1px}}
.sk{{margin-bottom:1.6px}} .note{{font-size:9.2pt}}
a{{color:inherit;text-decoration:none}}
</style></head><body>
<h1>{e(R["name"])}</h1>
<div class="title">{e(R["title"])}</div>
<div class="contact">{e(c["location"])} | {e(c["phone"])} | <a href="mailto:{c["email"]}">{e(c["email"])}</a> | <a href="https://www.{c["linkedin"]}">{e(c["linkedin"])}</a> | <a href="https://{c["github"]}">{e(c["github"])}</a></div>
<div class="ground"></div>
{section("Summary", f"<p>{e(R['summary'])}</p>")}
{section("Technical Skills", skills)}
{section("Experience", exp)}
{section("Projects", proj)}
{section("Education", edu)}
</body></html>'''
(ROOT / "build" / "resume_ats.html").write_text(html, encoding="utf-8")
subprocess.run([sys.executable, str(ROOT / "build" / "render.py"), str(ROOT / "build" / "resume_ats.html"),
                str(ROOT / "resumes" / "ats" / "Agnel_Salve_Resume_ATS.pdf")], check=True)
