# Outlier Resilience website

The site at https://outlierresilience.com. It is static HTML in `index.html`, with no build
step. Cloudflare Pages serves it from this repository, so a push to `main` deploys it.

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

`assets/` holds the logo, font, picture and social images. `tools/build-assets.py` draws
the logo SVGs from `assets/wordmark-outlines.json`.
