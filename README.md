# outlier-resilience-web

Website for **OutRes** (Outlier Resilience LLC). https://outlierresilience.com

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

Use a local server rather than opening `index.html` directly. Asset paths are
absolute (`/assets/...`) and will not resolve over `file://`.

## Brand assets (`assets/`)

Everything is vector and hand-authored. There are no raster logos and no
generated/AI artwork.

**The logo is the wordmark.** Its `O` is the mark: a ring, cut where a single
point escaped it. The point is the outlier. There is no separate horizontal
lockup, and there should not be one. Setting the mark next to the word puts two
`O` shapes side by side and the eye reads "O OutRes".

| File | Use |
|---|---|
| `logo-wordmark.svg` | **Primary logo**, for dark backgrounds |
| `logo-wordmark-light.svg` | Same, for light backgrounds |
| `logo-wordmark-mono.svg` | Single color (`currentColor`), for inline SVG only |
| `logo-mark.svg` | The ring alone, for tiles, avatars and slide corners |
| `logo-mark-light.svg` | Same, for light backgrounds |
| `logo-mark-mono.svg` | Single color (`currentColor`), for inline SVG only |
| `favicon.svg` | Square tile, browser tab / avatar |
| `logo-wordmark.png` | 1600x383 transparent PNG, for slides and LinkedIn |
| `icon-512.png` | 512x512 tile, for profile pictures |
| `og.png` | 1200x630 social preview |

**Use the plain file, not the `-mono` one, in an `<img>` tag.** `currentColor`
does not cross an `<img>` boundary, so a `-mono` file dropped into a page
renders black. The `-mono` files are for inline SVG and CSS masks.

**Color.** Accent `#52b788` on dark, `#2f8f66` on light. Ink `#eef1f5`,
background `#06090e`. Green marks the outlier and the word "Res". Nothing else
on the page is green except the accent furniture that was already there.

**Rebuilding.** The SVGs are generated, so edit the script and not the files:

```bash
python3 tools/build-assets.py
```

It reads outlined glyph geometry from `assets/wordmark-outlines.json` and draws
the ring from the numbers at the top of the script. The wordmark is *outlined*
glyphs, not live text, so it renders identically everywhere without the font.
The outlines were extracted from `plus-jakarta-sans-latin.woff2` with
`fontTools`; see `assets/FONT-LICENSE.md`. The `O` is deliberately absent from
the outlines: the mark takes its place.

The three PNGs are screenshots of the SVGs, taken at a fixed window size:

```bash
google-chrome --headless --screenshot=assets/og.png --window-size=1200,630 \
  --default-background-color=00000000 file://$PWD/<page>.html
```

## Writing

No em dashes. Short sentences, active voice, one idea each. Avoid the tells
listed at [Wikipedia:Signs of AI
writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), in
particular the "not X, but Y" construction, which is easy to overuse.

## Content note

The page deliberately describes the *problem* and makes no claims about our own
methods or results. The two figures cited are from published sources
(RAND RR-1478; ISO 21448:2022) and are quoted accurately. If you edit that
section, keep the numbers tied to the citations.
