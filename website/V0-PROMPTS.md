# v0 prompt pack: Groundline Brief website (A9 v1)

A one-page site that covers every required section (Hero, 3 products, About, Contact, responsive), built from the A8 wireframes. Extra pages are optional at the end.

## Contact details (already filled into Prompt 1)

| Field | Value |
|---|---|
| Email | salve.a@northeastern.edu |
| LinkedIn | https://www.linkedin.com/in/agnelsalve/ |
| GitHub | https://github.com/agnelsalve |

Prompt 1 is ready to paste as-is.

## How to run it

1. Go to **v0.dev**, sign in and start a **new chat**.
2. **Attach these images** from `website/v0-attachments/`: `logo-horizontal.png`, `wf-home.png`, `wf-mobile.png`. They show v0 the logo and layout. The prompt explains them in words too.
3. Paste **Prompt 1** and let it generate.
4. Paste Prompts **2 → 5** one at a time. Check the preview after each one, and only continue once it looks right.
5. If v0 drifts off-brand at any point, paste the matching line from **Fix-it prompts** below.
6. Click **Publish / Deploy** (top right). You'll get a `*.vercel.app` URL, which is your **live website link** for Canvas.
7. Test it on **your phone**: open every section, tap the menu, tap a `[n]` citation, submit the form.
8. Optional: use v0's **GitHub** button to push the code. Paste the live URL into the main README.

---

## Prompt 1: Design system + full homepage

```text
Build a one-page marketing website for "Groundline Brief", a B2B SaaS startup. Next.js App Router + Tailwind + TypeScript. It must be fully responsive (375px phone, 768px tablet, 1440px desktop) and accessible (WCAG AA).

WHAT THE PRODUCT IS
Groundline Brief writes the weekly competitor brief for product marketing teams, and a second AI fact-checks every sentence against the source it cites and cuts anything it can't back up. Audience: product marketing leads at B2B software companies (50–1,000 people). The site's one job: get a PMM lead to request a free audit of last week's brief.

BRAND FEEL
A well-set broadsheet newspaper, not a SaaS dashboard. Calm, exacting, plain-spoken, quietly confident. Warm paper, ink-black serif headlines, ONE plum accent. Think Linear's restraint or a newspaper of record.
NEVER: gradients, glows, drop shadows, glassmorphism, 3D blobs, robots, sparkles, emoji, blue, rounded "bubbly" cards, stock-photo people. Use Lucide icons only, 1.5px stroke, always paired with a text label.

DESIGN TOKENS (use exactly; define as CSS variables + Tailwind theme colors)
--ink: #16141A        (all text, headlines, rules, logo)
--plum: #5B3A70       (the ONE primary button per view, links, logo brackets, italic accent words, focus rings)
--paper: #FAF8F4      (page background)
--plum-tint: #EFE8F3  (callout backgrounds)
--lilac: #C9B3D9      (replaces plum on dark/ink backgrounds; plum on ink fails contrast)
--muted: #5B5862      (captions, secondary text)
--line: #DCD9E0       (hairline borders, rules)
--green: #1F7A4D      (ONLY for "backed by source" claims and the trust score)
--amber: #B45309      (ONLY for "partly backed" claims)
--red: #B42318        (ONLY for strikethrough of cut claims and form errors)
Proportion: ~70% paper, 20% ink, 7% plum, 3% state colors. Plum appears once per screen as the primary action.

TYPOGRAPHY (load with next/font/google)
- Headings: Newsreader, weight 600. Accent words in Newsreader italic 400 colored plum.
- Body: IBM Plex Sans 400/500/600, 17px desktop / 16px mobile, line-height 1.6, max-width 68ch.
- Data: IBM Plex Mono 500, used ONLY for numbers the code measured (scores, prices, counts, citation numbers like [3]). Never for sentences.
- Scale: Display 56/36px (desktop/mobile), line-height 1.05. H2 36/28px. H3 24/20px. Eyebrow labels: Plex Sans 600, 12px, uppercase, letter-spacing 0.12em, muted color.

LAYOUT RULES
- "The ground line": every section opens with a full-width 3px ink rule at the top of its content column, with the eyebrow label right under it. This is the signature layout device.
- Paper, not panels: separate sections with space and rules, not boxes. Cards use a 1px --line border, 4px radius max, no shadow.
- Generous whitespace. Max content width 1200px, 16px side gutter on mobile, 24px tablet, 48px desktop. No horizontal scroll at any width.
- Buttons: primary = plum fill, paper text, 4px radius, min-height 44px. Secondary = 1.5px ink outline, ink text, transparent.
- Visible focus ring on everything: 2px plum outline, 2px offset. Respect prefers-reduced-motion (turn off all animation).

LOGO (build as a React <Logo /> component with inline SVG, not an image)
The mark is a citation bracket "[G]" standing on a ground line. See the attached logo-horizontal.png.
- Icon: a left square bracket and a right square bracket drawn as thick plum (#5B3A70) strokes with square corners, a serif capital "G" in Newsreader 600 ink between them, and a thick ink bar directly underneath the whole icon. Icon SVG to use:
  <svg viewBox="0 0 56 64" aria-hidden="true"><path d="M17 6H7v44h10" fill="none" stroke="#5B3A70" stroke-width="6"/><path d="M39 6h10v44H39" fill="none" stroke="#5B3A70" stroke-width="6"/><text x="28" y="37" text-anchor="middle" font-family="Newsreader, Georgia, serif" font-weight="600" font-size="26" fill="#16141A">G</text><rect x="0" y="57" width="56" height="6" fill="#16141A"/></svg>
- Full lockup (header ≥768px): icon + the wordmark "Groundline" (Newsreader 600, ink) + "Brief" (Newsreader italic, plum), with a 3px ink ground line running under the full width of icon + wordmark. ~32px tall in the header.
- Compact lockup (<768px): icon + wordmark, no extended line under the wordmark.
- Always the full name "Groundline Brief", never just "Groundline". Never recolor, add shadows, or put a checkmark in the bracket.

PAGE STRUCTURE (single page, anchor links, smooth scroll)

1. HEADER (sticky after scrolling, paper background with a 1px --line bottom border once scrolled)
   Left: <Logo />. Center/right nav links: How it works · Products · Sample brief · About · Contact. Far right: plum button "Try a free audit" → #contact.
   Mobile: compact logo + hamburger at right. Menu opens full-screen on paper with large tap targets (min 44px) and the "Try a free audit" button repeated at the bottom. Close on Esc and on link tap.

2. HERO (id="top")
   Two columns on desktop (text left 55%, product visual right 45%); stacked on mobile, text first.
   Eyebrow: COMPETITIVE BRIEFS FOR PRODUCT MARKETING
   H1: "Send your Monday competitor brief" + line break + "without fear." where "without fear." is Newsreader italic plum.
   Subline: "A second AI checks every sentence against the article it cites and cuts anything it can't back up. Minutes, not two hours."
   Buttons: primary "Audit last week's brief, free" → #contact ; secondary outline "See a sample brief" → #sample.
   Microcopy under buttons (muted, 14px): "No sign-up for the sample · 2-minute read"
   Right side, the product as the hero image: a "brief card" styled like a printed page on paper (1px line border, white #FFFFFF background). Header row: "Weekly brief · wk 45" in mono on the left, and a green score chip "97% grounded" (mono, green text on #E3F2EA, with a small check icon) on the right. Then 4 short brief lines in Plex Sans, each ending with a mono citation like [1], [2], [3]. Lines 1–3 have a small green check + "backed" label in the margin, line 4 has an amber "partly" label. One more line is shown struck through in red with a small note "cut: no source". Lines fade in one by one on load (skip under reduced motion).
   Use FICTIONAL competitor names only (e.g. Larkspur, Tessellate, Quarryline). Sample lines:
   - "Larkspur raised its Team plan 12% on 3 Nov. [1]"
   - "Tessellate shipped an AI battlecard generator in beta. [2]"
   - "Two Larkspur reviews cite slower support since the price change. [3]"
   - "Quarryline may be shifting focus to mid-market. [4]" (partly)
   - Cut: "Tessellate leads the market in AI features." (cut: no source says "leads")

3. PROOF STRIP
   4 stats in a row (2x2 on tablet, horizontal swipe row with the next card peeking on mobile). Numbers in IBM Plex Mono 500, 40px, ink; labels in muted Plex Sans 14px:
   "97%" grounded, live brief · "$0.089" per verified run · "49 / 66" off-topic results rejected · "3" PMM user tests

4. HOW IT WORKS (id="how")
   Ground line + eyebrow HOW IT WORKS. H2: "One AI writes. A different AI checks. You send."
   Three steps in a row (stacked on mobile), each with a big mono step number, an H3 and one sentence:
   1 "Writer drafts": "Pulls this week's news, pricing pages and reviews for each rival and drafts the brief, citing a source for every sentence."
   2 "Checker verifies": "A separate model reads each sentence against the source it cites. Backed, partly backed, or cut, with the reason logged."
   3 "You send, with receipts": "You get a brief with a trust score and a cut log, ready for Slack or email in minutes."
   Under the steps: a text button "Show the fact-check log" that expands an accordion with a mono log excerpt, e.g.:
   [1] backed   · source quotes "+12% on Team plan"
   [4] partly   · source says "exploring mid-market", not "shifting focus"
   [cut]        · "leads the market" · no source makes this claim
   [gate]       · 49 of 66 "Podium" results rejected · off-topic (motorsport)

5. PRODUCTS (id="products") — three product cards, EACH with an image, title and description
   Ground line + eyebrow WHAT YOU GET. H2: "Three things land in your inbox every Monday."
   3 cards in a row on desktop, 2 columns on tablet, stacked on mobile. Each card: image on top (16:10, object-cover, 4px radius), then H3, then 2-sentence description, then a small mono detail line.
   Card 1 — image /images/product-brief.jpg — "The Weekly Brief" — "Every rival's pricing, launches and customer voice on one page, in the plain language you'd write yourself. Every sentence carries a numbered citation you can open." — mono: "5 rivals · ~2 min read"
   Card 2 — image /images/product-checker.jpg — "The Fact-Check Log" — "A second AI reviews each sentence against its source and tells you exactly what it cut and why. Nothing ships that it can't back up." — mono: "per-sentence verdicts · cut log"
   Card 3 — image /images/product-badge.jpg — "The 'Checked by' Badge" — "Every forwarded brief carries that week's live trust score, so the VP reading it knows it was checked. One click explains what the number means." — mono: "97% grounded · this week"
   For now, use these image paths with a tasteful fallback: if the image is missing, show a paper-colored block with a thin ink line illustration and the card title in Newsreader italic. Do NOT use gray placeholder boxes or stock photos.
   Below the cards, a compact pricing row (3 small columns, 1px line borders):
   "Free audit" — "1 brief, checked" — outline button "Start"
   "Team · $299/mo" — "Weekly, 5 rivals" — plum button "Start a trial" (visually primary)
   "Org · $999/mo" — "Unlimited rivals, same-day alerts" — outline button "Talk to us"
   Under it, muted 14px: "Where we won't fight: media breadth (Meltwater) and social listening depth (Brandwatch). We say so up front."

6. INTERACTIVE SAMPLE BRIEF (id="sample")
   Ground line + eyebrow SAMPLE BRIEF. H2: "Read a real brief." Subline: "Hover or tap any [n] to see its source."
   Tabs: Rivals · Your brand · Customer voice (each shows 3–4 brief lines, fictional companies).
   A legend with three toggle chips: "✓ backed" (green), "partly" (amber), "cut" (red strikethrough). Toggling a chip hides/shows those lines. State is never color-only: backed lines have a check icon + "backed", partly lines have the word "partly", cut lines are struck through with "cut:" + reason.
   Citation [n] in mono plum: on desktop hover/focus shows a popover (source title, date, the exact quoted passage, "Open source →"); on touch devices tap opens a bottom sheet. Dismiss on Esc or outside click. Fully keyboard reachable.

7. WHAT THE CHECKER CUT
   A plum-tint (#EFE8F3) callout block. Eyebrow WHAT THE CHECKER CUT THIS WEEK. Two items, each a red strikethrough sentence followed by the reason in muted text:
   - "Tessellate leads the market in AI features." — no source says "leads"
   - "Podium wins three championships." — off-topic: motorsport, not the software company (rejected by the relevance gate)

8. ABOUT (id="about")
   Ground line + eyebrow ABOUT. H2: "The editor who never grades its own work." ("never grades its own work" in plum italic).
   Two columns on desktop: left a founder photo (/images/founder.jpg, 4:5, desaturated ~30% with a subtle warm paper overlay, 4px radius), right a signed founder note in a plum-tint panel:
   "From the desk of Agnel Salve, founder"
   "I spent three years as a data engineer at Jio Platforms and Probus Insurance, building pipelines whose numbers went straight to executives. The first rule was simple: if you can't trace a number, it doesn't ship.
   Then I asked an LLM to summarize a week of news on Podium. 49 of 66 results were about car-racing podiums, and the model wrote them up as business news in perfect, confident prose. So I put an editor into the pipeline: a second model that checks every sentence the first one writes.
   When a product marketing lead tested it, they read the fact-check log, saw it flag its own fluff, and called it the best thing on the page. Groundline Brief is that editor, built for the people whose names are on the email."
   Signature line: "— Agnel Salve" in Newsreader italic.
   Below: Mission and Vision side by side (stacked on mobile), each with a small eyebrow label:
   MISSION: "To write the Monday competitor brief for product marketing teams and make sure every line is fact-checked before it's sent."
   VISION: "A workplace where every AI-written document comes with its receipts, and 'where did this come from?' takes one click to answer, not a two-hour hunt."
   Then a row of 5 value chips/cards (2 columns on mobile), each with a one-line "where it shows up" in muted text:
   Receipts over rhetoric — "every sentence has a [n]"
   Cut what you can't prove — "the cut log"
   Say what you don't know — "the 'partly' label and stale-data banner"
   Nobody grades their own work — "writer and checker are different models"
   Respect the five minutes — "one page, ~2-minute read"

9. CONTACT (id="contact")
   Ground line + eyebrow CONTACT. H2: "Show us last week's brief." Subline: "We'll send it back checked, with every line we'd cut and why. Free, within one business day."
   Two columns desktop (form left 60%, sidebar right), stacked on mobile.
   Intent chips above the form (radio group): "Get a free audit" (default selected) · "Ask a question" · "Recruiting / press". Fields adapt: Recruiting hides "Rivals you track" and shows "Role you're hiring for".
   Fields: Name* · Work email* (inline validation on blur; errors in red text WITH an icon, never color alone; keep user input on error) · Company · Your role · "Paste last week's brief or a link (optional)" textarea · "Rivals you track" (placeholder "e.g. Larkspur, Tessellate").
   Submit button (plum, full width on mobile): "Send it, we'll reply in 1 business day". Shows a progress state while sending.
   Privacy line under the button (muted, 14px): "We read your brief once to audit it, then delete it. No sales sequence."
   Form handling: put a constant FORM_ENDPOINT = "" at the top of the component. If it is set, POST the form as JSON to it. If it is empty, open a mailto: link to salve.a@northeastern.edu with the subject "Groundline Brief: " + intent and the fields in the body. Success state: "Got it. Your audit lands within one business day." with a link "While you wait, read the sample brief →" (#sample).
   Sidebar: "Elsewhere" — email salve.a@northeastern.edu (mailto link), LinkedIn (https://www.linkedin.com/in/agnelsalve/), GitHub (https://github.com/agnelsalve), "Live demo: groundline.streamlit.app" (https://groundline.streamlit.app). Then "What happens next": 1 We run your brief through the checker · 2 You get the marked-up copy + cut log · 3 No follow-up unless you reply.

10. FINAL CTA BAND
    Full-width ink (#16141A) band, paper text. Newsreader H2: "Paste last week's brief. We'll show you what we'd cut." Button: since plum on ink fails contrast, use a paper-filled button with ink text "Get a free audit" → #contact. Links on ink use lilac #C9B3D9.

11. FOOTER (on ink, continuous with the CTA band, separated by a 1px rule at 20% paper opacity)
    Left: reversed logo (brackets in lilac #C9B3D9, G and wordmark in paper, ground line in paper) + tagline "The competitive brief you can stand behind." Columns: Product (How it works, Products, Sample brief) · Company (About, Contact) · Elsewhere (LinkedIn, GitHub, Live demo). Bottom: "© 2026 Groundline Brief · Built by Agnel Salve".

MOBILE EXTRAS
- After the hero scrolls out of view, show a sticky bottom bar on mobile with a full-width plum button "Get a free audit" → #contact. Hide it while the contact section is in view.
- All tap targets ≥ 44px. Display headline drops to 36px. CTAs become full-width stacked buttons.

SEO / META
Title: "Groundline Brief: the competitive brief you can stand behind". Meta description: "Weekly competitor briefs for product marketing teams, with every sentence fact-checked by a second AI." Favicon: the [G] icon SVG.
```

---

## Prompt 2: Check the brand rules

```text
Review the whole page against the brand rules and fix any violations:
1. Only ONE plum-filled button visible per screen; every other button is ink outline or text.
2. No gradients, shadows, glows, blur, emoji or blue anywhere. Cards: 1px #DCD9E0 border, ≤4px radius, no shadow.
3. Headings are Newsreader 600, body is IBM Plex Sans, and IBM Plex Mono is used ONLY for numbers, prices, scores and [n] citations. Check every element.
4. Every section starts with the 3px ink ground line + uppercase eyebrow label.
5. Green, amber and red appear ONLY on claim states (backed / partly / cut), the trust score and form errors. Nowhere decorative.
6. Body text columns never exceed 68ch.
List what you changed.
```

## Prompt 3: Mobile pass

```text
Do a mobile pass at 375px width and fix everything:
- No horizontal scrolling anywhere (check the proof strip, sample brief tabs, pricing row and logo).
- Header: compact logo + hamburger; the full-screen menu works and closes on link tap.
- Hero: text first, then the brief card scaled to fit; H1 36px; full-width stacked buttons.
- Proof strip: horizontal swipe row with scroll-snap and the next card peeking.
- How it works: the three steps become an accordion (first one open).
- Product cards and value cards stack; pricing columns stack with "Team · $299/mo" first.
- Citation [n] taps open a bottom sheet, not a hover popover.
- Contact form: single column, full-width submit button, inputs 16px font so iOS doesn't zoom.
- Sticky bottom "Get a free audit" bar appears after the hero and hides on the contact section.
- Every tap target is at least 44x44px.
Then check 768px (tablet): product cards 2 columns, nav collapses to the hamburger.
```

## Prompt 4: Accessibility pass

```text
Accessibility pass to WCAG 2.2 AA:
- Semantic landmarks (header, nav, main, section with aria-labelledby, footer); one h1; no skipped heading levels.
- "Skip to content" link as the first focusable element.
- Visible 2px plum focus ring with 2px offset on every interactive element (lilac #C9B3D9 on the ink sections).
- Tabs use the ARIA tabs pattern with arrow-key support; legend toggles are aria-pressed buttons; the accordion uses aria-expanded; the popover and bottom sheet trap focus, close on Esc and return focus to the [n] button.
- Every image has meaningful alt text; decorative SVGs are aria-hidden.
- Form: every input has a visible <label>; errors are linked with aria-describedby and announced with aria-live="polite"; required fields are marked in text, not just with an asterisk color.
- All animation is disabled under prefers-reduced-motion.
- Muted text (#5B5862) must sit on paper or white only, never on plum-tint smaller than 14px.
```

## Prompt 5: Swap in the AI brand images (do this after you've generated them)

Upload your three AI visuals plus your headshot to the v0 chat, then:

```text
I've attached four images. Add them to /public/images with these names and use them:
- [first image] → product-brief.jpg (Products card 1, "The Weekly Brief")
- [second image] → product-checker.jpg (Products card 2, "The Fact-Check Log")
- [third image] → product-badge.jpg (Products card 3, "The 'Checked by' Badge")
- [headshot] → founder.jpg (About section founder photo)
Use next/image with proper width/height and sizes, object-cover, 4px radius. Apply a subtle warm treatment to all four so they match the paper palette: CSS filter saturate(0.75) plus a 6% #FAF8F4 overlay. Write descriptive alt text for each. Remove the fallback placeholder for any image that now exists.
```

---

## Fix-it prompts (paste when v0 drifts)

| v0 did this | Paste this |
|---|---|
| Switched to Inter / Geist | `Replace every font with the brand fonts: Newsreader for headings, IBM Plex Sans for body, IBM Plex Mono only for numbers and [n] citations. Load all three with next/font/google. No Inter or Geist anywhere.` |
| Added gradients / shadows / glow | `Remove all gradients, box-shadows, glows and blur effects. Use flat paper (#FAF8F4) backgrounds and 1px #DCD9E0 borders only.` |
| Used blue or random colors | `Use only the brand tokens: ink #16141A, plum #5B3A70, paper #FAF8F4, plum-tint #EFE8F3, lilac #C9B3D9, muted #5B5862, line #DCD9E0, and green/amber/red only for claim states. Remove every other color.` |
| Logo looks wrong | `Rebuild the <Logo /> exactly from the SVG in my first prompt: plum square brackets, ink serif G, ink ground-line bar underneath; wordmark "Groundline" ink Newsreader 600 + "Brief" plum Newsreader italic.` |
| Too many plum buttons | `Only one plum-filled button per screen. Change all other buttons to ink outline (secondary) or text links.` |
| Mobile overflow | `Something is wider than the viewport at 375px. Find it and fix it: no element may cause horizontal scroll. Add overflow-x: clip on the body as a last resort only after fixing the cause.` |
| Made up stats / logos / testimonials | `Remove any statistics, customer logos or testimonials I didn't provide. Only use: 97% grounded, $0.089 per run, 49/66 off-topic rejected, 3 PMM user tests.` |

---

## Optional: a separate About page (if you have time)

The one-page site already meets every requirement. A10 will expand your brand story, so a separate page can wait. If you still want it now:

```text
Move the About section to its own route /about and expand it following the attached wf-about.png: hero "The editor who never grades its own work.", the signed founder note, an "Origin story" in three beats (Pipelines to executives → The racing-podium run → "Caught its own fluff"), Mission and Vision side by side, the 5 values as cards that flip on hover/tap to show where each one appears in the product, and a final CTA with two buttons: "Read a sample brief" (/#sample) and "Get in touch" (/#contact). Keep the homepage About section as a short teaser that links to /about. Update the nav link.
```
