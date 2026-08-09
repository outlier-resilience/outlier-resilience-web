# outlier-resilience-web

Website for **OutRes** (Outlier Resilience LLC) — https://outlierresilience.com

A single static page. No build step, no framework, no external requests.

## Deploying

The site is served by **Cloudflare Pages**, connected to this repository.
**Pushing to `main` deploys it.** There is nothing to run and no dashboard step:

```bash
git add -A && git commit -m "..." && git push
```

Cloudflare rebuilds within a minute or so. To preview locally first:

```bash
python3 -m http.server 8000    # then open http://localhost:8000
```

Use a local server rather than opening `index.html` directly — asset paths are
absolute (`/assets/...`) and will not resolve over `file://`.

## Brand assets (`assets/`)

Everything is vector and hand-authored. There are no raster logos and no
generated/AI artwork.

| File | Use |
|---|---|
| `logo-lockup.svg` | Primary logo, icon + wordmark, for dark backgrounds |
| `logo-lockup-light.svg` | Same, for light backgrounds |
| `logo-wordmark.svg` | Wordmark only, two-tone |
| `logo-wordmark-mono.svg` | Wordmark only, single color (`currentColor`) |
| `logo-mark.svg` | Icon only (`currentColor`) — the ring with one point outside it |
| `favicon.svg` | Square tile, browser tab / avatar |
| `logo-lockup.png` | 1600×256 transparent PNG, for slides and LinkedIn |
| `icon-512.png` | 512×512 tile, for profile pictures |
| `og.png` | 1200×630 social preview |

**The mark:** a ring — the *O* of OutRes — with a single point sitting outside
it. The point is the outlier. It is built from two circles and nothing else, so
it stays legible down to 16px and recolors cleanly.

**Regenerating the wordmark.** The wordmark is *outlined* glyph geometry, not
live text, so it renders identically everywhere without the font. If it ever
needs rebuilding (different weight, different string), the outlines were
extracted from `plus-jakarta-sans-latin.woff2` with `fontTools`. See
`assets/FONT-LICENSE.md`.

**Color.** Accent `#52b788`, ink `#eef1f5`, background `#06090e`.

## Content note

The page deliberately describes the *problem* and makes no claims about our own
methods or results. The two figures cited are from published sources
(RAND RR-1478; ISO 21448:2022) and are quoted accurately — if you edit that
section, keep the numbers tied to the citations.
