# Outlier Resilience website

The site at https://outlierresilience.com. It is static HTML in `index.html`, with no build
step. Cloudflare Pages serves it from this repository, so a push to `main` deploys it.

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

`assets/` holds the logo, font, picture and social images. `tools/build-assets.py` draws
the logo SVGs from `assets/wordmark-outlines.json`.

## What the site says (plan version 4, 2026-11-08)

The page follows `outlier-resilience-company/PLAN.md` version 4: **Driving AI you own, proven
by design.** White-box driving models, calibrated on real vehicles, proven to stay within
stated safe limits, low compute and energy efficient. Never "certified safe". The retired
line "Prove more, simulate less" does not come back.

**Next: demos of actual AV features.** Each demo is an AI model that handles one real
driving scenario (for example, braking at dusk, a large animal at speed, a detector trained
with lidar labels), shown with the same three numbers: proven range, compute (watts and
latency) and energy. Add them to the page as they become public, replacing the schematic
map with a real one. Open demo features are for research and benchmarking, not road use.

`assets/og.png` is a 1200x630 screenshot of `tools/og.html`:

    google-chrome --headless=new --hide-scrollbars --window-size=1200,630 \
      --screenshot=assets/og.png "file://$PWD/tools/og.html"
