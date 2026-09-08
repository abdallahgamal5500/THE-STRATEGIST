# The Strategist — website (beta)

Static marketing site for **The Strategist** — *From Vision to Victory*.
34 pages, no CMS, no database. One contact form that emails the firm.

---

## Run it

```bash
cd src
python build.py          # no dependencies, Python 3.8+
```

Output lands in `src/dist/`. Open `src/dist/index.html` directly in a browser —
it works from the filesystem, no server needed.

## Layout

```
src/
  build.py            generator: templates, page functions, the build itself
  content.py          ALL site content as plain data — edit this, not the HTML
  audit.py            responsive + accessibility audit (see Verification below)
  assets/
    css/site.css      the whole design system (one file, no framework)
    img/              logo lockups + favicons, derived from the client's JPEGs
  dist/               generated output — never edit by hand, it is wiped each build
```

**To change wording**, edit `content.py` and rebuild. Nothing in `dist/` is
hand-maintained: nav, footer and the services panel appear on 30+ pages and are
defined once in `build.py`.

## Pages (34)

| Group | Count | Files |
|---|---|---|
| Core | 4 | `index`, `about`, `approach`, `contact` |
| Services | 14 | `services` + 3 pillar pages + **10 service-family pages** |
| Evidence | 10 | `case-studies` + 3 details, `insights` + 4 articles, `industries` |
| Credibility | 4 | `leadership`, `partners`, `clients`, `testimonials` |
| Utility | 2 | `thank-you`, `privacy` |

Service families come straight from the client's v2 document: 3 pillars →
10 families → ~50 named components. Every family page follows the BRD §8
template (challenges → what we do → capabilities → approach → deliverables →
business value → related work → CTA).

## Design system

**Concept: "the instrument."** This firm sells measurement and governance —
strategy maps, KPI cascades, initiative registers, authority matrices, stage
gates. So the page is built like a calibrated instrument rather than a
brochure. Three devices carry it:

1. **A measure rail** down the left edge of every section, with graduated tick
   marks, carrying the section name. It encodes where you are; it is not
   decoration. Below 1000px it collapses to a ruled label line above the content.
2. **Ruled indices and tabular rows instead of cards.** A consulting portfolio
   genuinely *is* a structured index, so it is set as one — all ten families
   visible and scannable at once. Hierarchy comes from rule weight and column
   position, not from borders, radii and shadows.
3. **One bold moment:** the six-stage lifecycle drawn as a graduated scale with
   tick marks. It is also the only content on the site that carries numbers,
   because it is the only content that is genuinely a sequence.

| Token | Value | Note |
|---|---|---|
| `--navy` | `#1A3047` | sampled from the logo; used mainly as *structure* |
| `--ink` | `#0E1D2B` | body text |
| `--slate` / `--slate-dim` | `#526A80` / `#5E707F` | secondary, tertiary (both AA) |
| `--silver` | `#DBDDD8` | from the wordmark |
| `--rule` | `#CAD5DD` | deliberately visible, not a 5% hairline |
| `--signal` | `#215FA6` | interaction only — links and focus, never decoration |
| Display | **Archivo**, width axis 112% | wide, flat, authoritative |
| Body | **Instrument Sans** | |

There is **no gold and no serif** — neither exists in the brand.

Deliberately excluded, as generic defaults rather than choices: cards with soft
drop shadows, gradient washes, hover-lift transitions, tracked-out ALL-CAPS
eyebrow labels, `→` appended to link text, meta strings joined by middle dots,
and `01 / 02 / 03` markers on content that is not a sequence. The build verifies
all of these stay at zero.

**Motion:** one orchestrated entrance on the lifecycle scale, and nothing else.
No scroll-triggered reveals. `prefers-reduced-motion` disables it.

## Verification

`python audit.py` loads every page in an iframe at **10 widths (320 → 1440)** and
checks for horizontal overflow, elements escaping the viewport, content
overflowing its own box, sub-12px text, and tap targets under 24px (WCAG 2.5.8).

Current state: **PASS across all 340 page/width combinations.** All body text
meets WCAG AA contrast (≥4.5:1) in both light and dark contexts.

Two documented exceptions in the audit: the logo tagline (`.brand-t`, a wordmark
element rather than reading copy) and the consent checkbox (enclosed by a much
larger `<label>`, which is the WCAG 2.5.8 enclosure exception).

Chrome headless on Windows will not open a window narrower than ~485 CSS px,
which is why narrow widths are tested inside iframes — an iframe gets a real
viewport, so media queries and `vw` units resolve correctly.

## Logo assets

**The site uses vector.** `mark-light.svg` is what the nav and footer load.

Generated from the supplied `WhatsApp-Image-...-4.27.21-PM.svg` (the dark-on-white
lockup) by cropping the viewBox and setting a single `fill`, which gives both
colourways from one traced master:

| File | Use |
|---|---|
| `mark-light.svg` / `mark-dark.svg` | symbol only — **nav and footer** |
| `logo-light.svg` / `logo-dark.svg` | full lockup with wordmark and tagline |
| `*.png` equivalents | earlier raster versions, kept as fallbacks |
| `favicon.png`, `favicon-512.png`, `favicon.ico` | browser tab icon |

The nav wordmark is **live HTML text**, not an image, so it stays crisp.

**Still worth asking the client for the designer's original file.** The supplied
SVGs are auto-traces of the JPEGs, not brand masters: the 3D gloss is baked in as
knockout shapes, and the tagline is traced outlines rather than live type. Good
enough for web at any size; not the same as an editable original.

(The white-on-navy SVG, `...4.27.30-PM.svg`, traces the navy background as a
filled rectangle with the logo knocked out of it, so it is not directly usable.
The dark-on-white trace is the better master and is the one used here.)

## What is not real yet

Marked in-page with a `Draft` or `Placeholder` tag, and by the beta banner:

- **Placeholder** — contact email/phone/WhatsApp/LinkedIn, all leadership
  profiles and photos, partner names/logos, client logos, testimonials.
- **Draft** — case studies (3, anonymized), insight articles (4), the industry
  list, and the privacy notice. All written by us for client review.
- Contact form does not submit; it redirects to `thank-you.html`. A honeypot
  field and the consent checkbox are already wired.

Client-supplied copy (Who We Are, Vision, Mission, the 4Ps Lens, Play to Win,
all service names and value propositions, the six-stage lifecycle) is used
verbatim and is marked `CLIENT` in `content.py`.

To remove all beta tagging, set `BETA = None` in `build.py` and drop the `tag()`
calls.

## Going live

The form is the only server-side requirement. Two options:

1. **ASP.NET Core Razor Pages** — port `dist/` into a `_Layout.cshtml` plus
   partials; the form posts to a page handler that validates, checks the
   honeypot, and emails. One codebase, one deploy. Needs a .NET host.
2. **Keep it static** — host `dist/` anywhere, and point the form at a small
   endpoint or a form service. Cheapest, works on any hosting.

Hosting has not been decided, which is what picks between them.

Before launch: real contact details, `SITE["linkedin"]`, an approved privacy
notice, real Open Graph images, and a `sitemap.xml` + `robots.txt`.
