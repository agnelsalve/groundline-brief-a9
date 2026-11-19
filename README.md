# Groundline Brief: Assignment 9, Brand-Aligned Digital Presence

INFO7375 Branding & AI · Path B (startup brand) · Due 20 Nov 2026, 11:59 PM

This assignment turns the Groundline Brief identity from Assignment 8 into a live website, a LinkedIn header, brand visuals and two resumes.

## Deliverables

| Folder | Deliverable | Points | Status |
|---|---|---|---|
| [`website/`](website/) | Live website (Vercel v0). Prompts: [`V0-PROMPTS.md`](website/V0-PROMPTS.md) · **Live: [groundline-ten.vercel.app](https://groundline-ten.vercel.app/)** | 25 | Live (v1) |
| [`accessibility/`](accessibility/) | [`Salve_Agnel_A9_ColorAccessibility.pdf`](accessibility/Salve_Agnel_A9_ColorAccessibility.pdf): 15 WebAIM screenshots | 5 | Done |
| [`linkedin-header/`](linkedin-header/) | [`Salve_Agnel_A9_LinkedInHeader.pdf`](linkedin-header/Salve_Agnel_A9_LinkedInHeader.pdf) + 1584×396 PNG | 10 | Done |
| [`brand-visuals/`](brand-visuals/) | [`Salve_Agnel_A9_BrandVisuals.pdf`](brand-visuals/Salve_Agnel_A9_BrandVisuals.pdf). Prompts: [`IMAGE-PROMPTS.md`](brand-visuals/IMAGE-PROMPTS.md) | 10 | Done |
| [`resumes/ats/`](resumes/ats/) | `Agnel_Salve_Resume_ATS.pdf` + `.docx` | 15 | Done |
| [`resumes/visual/`](resumes/visual/) | `Agnel_Salve_Resume_Visual.pdf` | 15 | Done |

## Rebuilding

All documents are generated from [`build/`](build/) (Python + Playwright/Edge, fonts embedded):

```bash
python build/a11y.py && python build/render.py build/a11y.html accessibility/Salve_Agnel_A9_ColorAccessibility.pdf
python build/linkedin.py && python build/render.py build/linkedin.html linkedin-header/Salve_Agnel_LinkedIn_Header_1584x396.png 1584x396 1
python build/resume_ats.py          # ATS PDF (content: build/resume_content.json)
node build/resume_docx.js           # ATS Word (needs the docx npm package)
python build/resume_visual.py       # visual resume
python build/brand_visuals.py "Adobe Firefly"   # after adding brand-visuals/visual-1..3
```

## Brand tokens (from Assignment 8)

**Color**

| Token | Hex | Use |
|---|---|---|
| Ink | `#16141A` | Text, logo, ground-line rules |
| Plum | `#5B3A70` | One primary CTA per view, links, brackets |
| Paper | `#FAF8F4` | Page background |
| Grounded green | `#1F7A4D` | Verified claims, trust score only |
| Check amber | `#B45309` | Partly-backed claims |
| Cut red | `#B42318` | Strikethrough of cut claims, form errors |
| Plum tint | `#EFE8F3` | Callouts |
| Lilac | `#C9B3D9` | Plum replacement on dark backgrounds |
| Muted | `#5B5862` | Captions |
| Line | `#DCD9E0` | Rules, borders |

**Type:** Newsreader 600 / italic 400 (headings) · IBM Plex Sans (body) · IBM Plex Mono (data only).

**Tagline:** *The competitive brief you can stand behind.*

## Contrast pairs to check (WebAIM)

| Foreground | Background | A8 ratio |
|---|---|---|
| Ink `#16141A` | Paper `#FAF8F4` | 17.2:1 |
| Plum `#5B3A70` | Paper `#FAF8F4` | 8.7:1 |
| Muted `#5B5862` | Paper `#FAF8F4` | — |
| Grounded green `#1F7A4D` | Paper `#FAF8F4` | 5.0:1 |
| Check amber `#B45309` | Paper `#FAF8F4` | 4.7:1 |
| Cut red `#B42318` | Paper `#FAF8F4` | 6.2:1 |
| Paper `#FAF8F4` | Plum `#5B3A70` (button) | — |
| Lilac `#C9B3D9` | Ink `#16141A` | 9.5:1 |
| Paper `#FAF8F4` | Ink `#16141A` (footer) | — |
