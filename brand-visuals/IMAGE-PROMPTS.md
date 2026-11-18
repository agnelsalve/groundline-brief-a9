# AI brand visuals: 3 prompts

These follow the photography direction from A8: *real, documentary, early-morning light, warm paper tones, desaturated about 30%. Never glowing brains, robots, holograms or AI-generated faces.* All three share one style block, so they look like the same brand family.

## Where to generate

- **ChatGPT** (GPT image / DALL·E): paste one prompt per message. Ask for **landscape 3:2**.
- **Adobe Firefly** (free with your Adobe account): Text to Image, aspect **Landscape (4:3 or 3:2)**, content type **Photo**, and turn the **Visual intensity** down.

Generate 2–4 variations of each and keep the best one. **Reject any image with readable fake text, warped hands or a visible face.**

## Save them as

| File (in this folder) | Used on the website as |
|---|---|
| `visual-1.png` (or .jpg) | Products card 1, "The Weekly Brief" → `product-brief.jpg` |
| `visual-2.png` | Products card 2, "The Fact-Check Log" → `product-checker.jpg` |
| `visual-3.png` | Products card 3, "The 'Checked by' Badge" → `product-badge.jpg` |

Then tell Claude "images are in". It runs `python build/brand_visuals.py "<tool you used>"` to build the PDF.

---

### Shared style block (already included at the end of each prompt)

> Documentary editorial photograph, natural early-morning window light from the left, warm off-white paper tones (#FAF8F4), deep near-black ink, a single muted plum-purple accent (#5B3A70), muted desaturated color grade (about 30% less saturation), shallow depth of field, calm and uncluttered, lots of negative space, shot on a 50mm lens. No people's faces, no robots, no glowing or holographic elements, no neon, no gradients, no readable text, no logos.

### Visual 1: The Weekly Brief

```text
Overhead flat-lay of a single printed one-page newsletter-style document lying on a pale oak desk at 8 a.m. on a Monday. The page has a serif headline area, neat columns of small text (blurred and unreadable) and a few lines underlined in plum-purple ink, with tiny bracketed footnote marks in the margin. A plum-colored fountain pen lies diagonally across the corner of the page, and a white ceramic cup of black coffee sits at the top right edge of the frame. Documentary editorial photograph, natural early-morning window light from the left, warm off-white paper tones (#FAF8F4), deep near-black ink, a single muted plum-purple accent (#5B3A70), muted desaturated color grade (about 30% less saturation), shallow depth of field, calm and uncluttered, lots of negative space, shot on a 50mm lens. No people's faces, no robots, no glowing or holographic elements, no neon, no gradients, no readable text, no logos.
```

### Visual 2: The Fact-Check Log

```text
Close-up, low angle across a printed page on a desk: an editor's hand (only the hand and wrist, sleeve of a dark navy sweater) holding a plum-ink pen, drawing a single clean strikethrough line across one sentence. In the margin are small hand-drawn check marks in dark green next to other lines, and one short margin note. The rest of the page is softly out of focus. Documentary editorial photograph, natural early-morning window light from the left, warm off-white paper tones (#FAF8F4), deep near-black ink, a single muted plum-purple accent (#5B3A70), muted desaturated color grade (about 30% less saturation), shallow depth of field, calm and uncluttered, lots of negative space, shot on a 50mm lens. No people's faces, no robots, no glowing or holographic elements, no neon, no gradients, no readable text, no logos.
```

### Visual 3: The "Checked by" Badge

```text
A small brass-and-wood spirit level resting perfectly flat on a neat stack of printed pages on a pale oak desk, its green bubble exactly centered between the two marks. Behind it, softly blurred, an open laptop and a white coffee cup in morning window light. A thin dark ruled line runs along the edge of the top page like a baseline. The composition leaves the left third as calm empty desk space. Documentary editorial photograph, natural early-morning window light from the left, warm off-white paper tones (#FAF8F4), deep near-black ink, a single muted plum-purple accent (#5B3A70), muted desaturated color grade (about 30% less saturation), shallow depth of field, calm and uncluttered, lots of negative space, shot on a 50mm lens. No people's faces, no robots, no glowing or holographic elements, no neon, no gradients, no readable text, no logos.
```

## Why these three (goes into the PDF)

1. **The brief on the desk**: the product is a document you read, not a dashboard (A8: "Paper, not panels"; inspiration #10, "8 a.m. Monday, one sheet").
2. **The editor's strikethrough**: "Cut what you can't prove", the checker's core action (A8 inspiration #2, proofreader's delete mark).
3. **The level, bubble centered**: the trust score, balanced and settled (A8 inspiration #5 spirit level, and the "ground line" itself).
