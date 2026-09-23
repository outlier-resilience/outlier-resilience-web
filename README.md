# Outlier Resilience website

The one-page site for Outlier Resilience LLC at https://outlierresilience.com.
It is static HTML in `index.html`, with no build step and no framework.

Cloudflare Pages serves the site from this repository, so a push to `main`
deploys it. To look at it first on this machine:

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

`assets/` holds the logo, the font, the picture and the social images. The logo
is the wordmark, and its `O` is the mark. There is no separate lockup.

`tools/build-assets.py` draws the logo SVGs from `assets/wordmark-outlines.json`,
so edit the script and not the SVG files. Use the plain SVG, not the `-mono`
one, in an `<img>` tag, because a `-mono` file renders black there.

The page describes the problem only, in about sixty words. Keep it to one screen.
