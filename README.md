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
| `linkedin-banner.jpg` | 2256x382 cover image for the LinkedIn company page |

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

The page follows the pre-product rule in James Sinclair, *Starting a StartUp*,
page 69. Before there is a product or a customer, the page describes the
problem and nothing else. No solution, no features, no benefits.

The shape is fixed:

| Part | Rule |
|---|---|
| Headline | Five words. "Test driving cannot prove safety." |
| Explanation | One sentence, fifteen words. The problem, not the product. |
| Who we serve | One sentence. Sinclair says name the niche and go as narrow as you can. |
| One fact | The RAND figure, with the citation. It sizes the problem. |
| The ask | One sentence and an email address. |

Keep it to one screen. The whole page is about sixty words. If you add a
sentence, take one out.

The preprint link is the one judgment call. Sinclair would cut it. It stays
because a technical reader needs one reason to believe the problem is
understood here. If the page ever starts reading as a pitch, cut it first.

The RAND figure is from RR-1478 and is quoted accurately. If you edit it, keep
the number tied to the citation.
