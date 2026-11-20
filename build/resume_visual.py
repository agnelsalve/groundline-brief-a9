"""Visual resume: full Groundline brand system, headshot, 6-second scan. -> resumes/visual/Agnel_Salve_Resume_Visual.pdf"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from logo import icon

ROOT = Path(__file__).resolve().parent.parent

METRICS = [("3+ yrs", "data & AI engineering"), ("92%", "ROC-AUC, fraud model"), ("1 TB+", "daily Spark/Kafka load"), ("97%", "grounded, live LLM brief")]
JOBS = [
    ("AI Engineer", "Probus Insurance Broker", "Mumbai", "Mar 2024 – Jul 2025", [
        "Built claims fraud detection end to end (XGBoost, SMOTE, TF-IDF on adjuster notes): <b class='m'>92% ROC-AUC</b>, <b class='m'>85% precision</b>.",
        "Architected the firm's first cloud ML platform on AWS (S3, Glue, Redshift): data freshness from <b class='m'>T+2</b> to near real time.",
        "Rebuilt feature pipelines across 15+ sources in Python and MS SQL: <b class='m'>70% faster</b>, reproducible datasets.",
        "Owned the ML function with no MLOps team: drift reviews, retraining cadence, review standards.",
    ]),
    ("Software Development Engineer I", "Jio Platforms (Reliance)", "Mumbai", "Jul 2022 – Mar 2024", [
        "Stabilized <b class='m'>1 TB+</b> daily Hadoop, Spark and Kafka workloads with CI/CD on Azure DevOps: <b class='m'>+30%</b> stability.",
        "Real-time streaming features (Kafka, Spark Streaming, HiveQL) closed a one-day lag: <b class='m'>45% faster</b> for 200+ users.",
        "Standardized 50+ metric definitions, an early feature store: <b class='m'>40% faster</b> queries.",
        "Led 5G infrastructure analytics as delivery point of contact: 2 production use cases shipped.",
    ]),
]
PROJECTS = [
    ("Multi-Agent Investor Intelligence", "LangGraph · MCP · FastAPI · GCP Cloud Run · Pinecone",
     "Parallel agents for pitch-deck summaries and market research over Snowflake + vectors."),
    ("Email RAG Assistant", "LangChain · Ollama · ChromaDB",
     "Fully local RAG over Gmail: <b class='m'>&lt;100 ms</b> retrieval, zero data leaves the machine."),
    ("MedVeritas", "XGBoost · SHAP · spaCy · Streamlit",
     "Drug-effectiveness prediction from 215K+ reviews: <b class='m'>86.3% ROC-AUC</b>, explained with SHAP."),
]
SKILLS = [
    ("LLM & GenAI", ["RAG", "LangGraph", "LangChain", "MCP", "Multi-agent", "LLM evals", "n8n", "Gemini", "Ollama", "Pinecone"]),
    ("Data", ["Python", "SQL", "Spark", "Kafka", "Airflow", "Snowflake", "Redshift", "Hive"]),
    ("ML", ["PyTorch", "TensorFlow", "XGBoost", "scikit-learn", "SHAP", "NLP"]),
    ("Cloud", ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "FastAPI"]),
]

metrics = "".join(f'<div class="met"><div class="mv mono">{v}</div><div class="ml">{l}</div></div>' for v, l in METRICS)
jobs = "".join(
    f'<div class="job"><div class="jr"><h3>{r}</h3><span class="mono d">{d}</span></div><div class="org">{o} · {p}</div>'
    f'<ul>{"".join(f"<li>{b}</li>" for b in bs)}</ul></div>' for r, o, p, d, bs in JOBS)
projects = "".join(f'<div class="pj"><h4>{n}</h4><div class="st mono">{s}</div><p>{t}</p></div>' for n, s, t in PROJECTS)
skills = "".join(f'<div class="sg"><div class="sh">{h}</div><div class="chips">{"".join(f"<span>{x}</span>" for x in xs)}</div></div>' for h, xs in SKILLS)

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Agnel Salve, Visual Resume</title><link rel="stylesheet" href="brand.css"><style>
@page{{size:Letter;margin:0}}
html{{height:10.98in;overflow:hidden}} body{{width:8.5in;height:10.98in;overflow:hidden;display:grid;grid-template-columns:2.55in 1fr;font-size:8.6pt;line-height:1.42}}
.m{{font-family:"IBM Plex Mono";font-weight:500;color:var(--ink)}}
/* sidebar: the dark context, lilac replaces plum */
aside{{background:var(--ink);color:var(--paper);padding:.42in .3in .35in;display:flex;flex-direction:column;gap:.2in}}
.photo{{width:1.62in;height:1.62in;border-radius:50%;object-fit:cover;object-position:center 22%;filter:saturate(.75);border:3px solid var(--lilac);align-self:center}}
aside h5{{font:600 7.2pt "IBM Plex Sans";letter-spacing:.16em;text-transform:uppercase;color:var(--lilac);border-top:2px solid var(--paper);padding-top:5px;margin-bottom:6px}}
aside a,aside .ct{{color:var(--paper);text-decoration:none;display:block;font-size:8.1pt;margin-bottom:3px;word-break:break-word}}
aside .ct b{{color:var(--lilac);font-weight:500;font-family:"IBM Plex Mono";font-size:7pt;display:block;letter-spacing:.06em}}
.sg{{margin-bottom:7px}} .sh{{font-size:7.6pt;color:var(--lilac);margin-bottom:3px}}
.chips{{display:flex;flex-wrap:wrap;gap:3px}} .chips span{{border:1px solid rgba(250,248,244,.35);padding:1px 5px;border-radius:2px;font-size:7.3pt}}
.ed{{margin-bottom:7px}} .ed b{{display:block;font:600 9.2pt Newsreader}} .ed span{{font-size:7.8pt;color:#D9D5DE}}
.badge{{margin-top:auto;display:flex;gap:8px;align-items:center;font-size:7.4pt;color:#D9D5DE}}
/* main */
main{{padding:.38in .45in .28in .4in;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:7px;font:600 8.5pt Newsreader}}
h1{{font:600 34pt/1 Newsreader;letter-spacing:-.6px;margin-top:.08in}}
.role{{font:400 13pt Newsreader;font-style:italic;color:var(--plum);margin-top:4px}}
.line{{height:3px;background:var(--ink);margin:.12in 0 .1in}}
.lede{{font-size:9.3pt;line-height:1.5}}
.mets{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:.14in 0 .04in}}
.met{{padding:7px 8px 6px}} .met+.met{{border-left:1px solid var(--line)}}
.mv{{font-size:17pt;font-weight:500;line-height:1.1}} .ml{{font-size:7.2pt;color:var(--muted);margin-top:2px}}
h2{{font:600 7.6pt "IBM Plex Sans";letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border-top:3px solid var(--ink);padding-top:4px;margin:.12in 0 .06in}}
.feat{{background:var(--tint);padding:.12in .15in;display:grid;grid-template-columns:1fr 1.5in;gap:.14in}}
.feat h3{{font:600 13pt Newsreader}} .feat h3 i{{color:var(--plum);font-weight:400}}
.feat .st{{font-size:7.4pt;color:var(--muted);margin:1px 0 4px}} .feat p{{font-size:8.5pt}}
.mini{{background:#fff;border:1px solid var(--line);padding:6px 7px;font-size:6.9pt;line-height:1.35;align-self:start}}
.mini .tp{{display:flex;justify-content:space-between;font-family:"IBM Plex Mono";color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:3px;margin-bottom:3px}}
.mini .sc{{color:var(--green)}} .ok{{color:var(--green);font-weight:600}} .pt{{color:var(--amber);font-weight:600}} .ct2{{color:var(--red);text-decoration:line-through}}
.job{{margin-bottom:.09in}} .jr{{display:flex;justify-content:space-between;align-items:baseline}}
h3{{font:600 11.2pt Newsreader}} .d{{font-size:7.4pt;color:var(--muted)}} .org{{color:var(--plum);font-weight:500;font-size:8.4pt;margin-bottom:2px}}
ul{{margin-left:12px}} li{{margin-bottom:1.5px}} li::marker{{color:var(--plum)}}
.pjs{{display:grid;grid-template-columns:repeat(3,1fr);gap:.14in}}
.pj h4{{font:600 9.6pt Newsreader;line-height:1.2}} .pj .st{{font-size:6.8pt;color:var(--muted);margin:2px 0 3px}} .pj p{{font-size:8pt;line-height:1.38}}
.foot{{margin-top:auto;font-size:7.2pt;color:var(--muted);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:5px}}
</style></head><body>
<aside>
  <img class="photo" src="../assets/headshot.png" alt="Agnel Salve">
  <div><h5>Contact</h5>
    <div class="ct"><b>EMAIL</b>salve.a@northeastern.edu</div>
    <div class="ct"><b>PHONE</b>(857) 423-8028</div>
    <div class="ct"><b>LINKEDIN</b>linkedin.com/in/agnelsalve</div>
    <div class="ct"><b>GITHUB</b>github.com/agnelsalve</div>
    <div class="ct"><b>LIVE DEMO</b>groundline.streamlit.app</div>
    <div class="ct"><b>BASED IN</b>Boston, MA</div></div>
  <div><h5>Skills</h5>{skills}</div>
  <div><h5>Education</h5>
    <div class="ed"><b>MS, Information Systems</b><span>Northeastern University · exp. Dec 2027</span></div>
    <div class="ed"><b>BE, Computer Engineering</b><span>University of Mumbai · 2018–2022</span></div></div>
  <div class="badge">{icon(18, bracket="#C9B3D9", g="#FAF8F4", line="#FAF8F4")}<span>Every number on this page has a source.</span></div>
</aside>
<main>
  <div class="brand">{icon(16)}<span>Groundline <span class="brief">Brief</span> · founder</span></div>
  <h1>Agnel Salve</h1>
  <div class="role">AI &amp; data engineer. I build AI you can check.</div>
  <div class="line"></div>
  <p class="lede">Years of building pipelines for executives taught me one rule: if you can't trace it, it doesn't ship. Now I build LLM systems where a second model checks the first.</p>
  <div class="mets">{metrics}</div>
  <h2>Featured · founder project</h2>
  <div class="feat"><div><h3>Groundline <i>Brief</i></h3><div class="st mono">n8n · Gemini (3 models) · Python · Streamlit · 2026–now</div>
    <p>Weekly competitor briefs for product marketing teams. One model writes, a different model fact-checks every claim against its source, and unsupported lines are cut and logged. Relevance gate rejected <b class="m">49 of 66</b> off-topic results; <b class="m">$0.089</b> per run; load-tested to <b class="m">2,000</b> requests; 3 PMM user tests.</p></div>
    <div class="mini"><div class="tp"><span>wk 45</span><span class="sc">97% grounded</span></div>
      <div><span class="ok">✓</span> Team plan +12% <span class="m" style="color:var(--plum)">[1]</span></div>
      <div><span class="ok">✓</span> AI battlecards <span class="m" style="color:var(--plum)">[2]</span></div>
      <div><span class="pt">partly</span> Mid-market shift <span class="m" style="color:var(--plum)">[3]</span></div>
      <div><span class="ct2">Leads the market</span></div></div></div>
  <h2>Experience</h2>{jobs}
  <h2>More projects</h2><div class="pjs">{projects}</div>
  <div class="foot"><span>Agnel Salve · AI &amp; Data Engineer</span><span>agnelsalve.github.io</span></div>
</main></body></html>'''
(ROOT / "build" / "resume_visual.html").write_text(html, encoding="utf-8")
subprocess.run([sys.executable, str(ROOT / "build" / "render.py"), str(ROOT / "build" / "resume_visual.html"),
                str(ROOT / "resumes" / "visual" / "Agnel_Salve_Resume_Visual.pdf")], check=True)
