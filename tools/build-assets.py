"""Rebuild the OutRes brand SVGs.

Run it from anywhere:  python3 tools/build-assets.py
It writes the seven files in assets/. The PNGs are built separately; see the README.
"""

import json, math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
_glyphs = json.load(open(os.path.join(OUT, "wordmark-outlines.json")))
d_res = _glyphs["Res"]
D_UT = _glyphs["ut"]                      # the u and the t. The mark is the O.
GLYPH = 'transform="translate(0,80) scale(0.107383,-0.107383)"'

INK, ACC, BG = "#eef1f5", "#52b788", "#06090e"
INK_L, ACC_L = "#10151c", "#2f8f66"       # on light grounds

# The typeface O this ring replaces: centre, outer radius, and its stroke weights
# (15.0 at the top, 16.7 at the sides). 15.5 sits between them.
CX, CY, RO = 47.14, 40.0, 42.42
SW, DOT_R = 15.5, 7.5
DOT_D = RO + 10.9 + DOT_R                 # ring outer, clear gap, then the point

# How much daylight the cut shows, as a fraction of the ring's outer width.
# Set the daylight, not the angle. The round caps put half a stroke width back
# on each end of the arc, so the angle that gives this varies with the stroke:
# the same 26 degrees left 5.9% of daylight on the mark and 0.1% on the
# wordmark, which is why the wordmark looked uncut.
# The cut sits on the upper-right diagonal. That angle, not the size, is what
# keeps the letter off a C: rotate the same cut to 0 degrees and the wordmark
# reads "CutRes" at every size.
DAYLIGHT = 0.09


def arc_degrees(ro, sw, daylight=DAYLIGHT):
    """The arc to remove so the cut shows `daylight` once the caps are drawn."""
    r = ro - sw / 2
    return 2 * math.degrees(math.asin(min(1.0, (daylight * 2 * ro + sw) / (2 * r))))


def broken_ring(cx, cy, ro, sw, ringc, dotc, dot_r, dot_d):
    """The ring, cut where the point left it, and the point."""
    r = ro - sw / 2
    gap = arc_degrees(ro, sw)
    a1, a2 = -45 + gap / 2, 360 - 45 - gap / 2
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    dx, dy = cx + dot_d * math.cos(math.radians(-45)), cy + dot_d * math.sin(math.radians(-45))
    return (f'<path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 1 1 {x2:.2f} {y2:.2f}" fill="none" '
            f'stroke="{ringc}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="{dot_r}" fill="{dotc}"/>')


def svg(vb, body, w=None, h=None):
    size = f'width="{w}" height="{h}" ' if w else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" {size}viewBox="{vb}" role="img" '
            f'aria-label="OutRes"><title>OutRes</title>{body}</svg>')


def wordmark(ink, acc, res=None):
    """Primary logo. The O is the mark."""
    res = res or acc
    return svg("0 -14 393.1 94",
               f'<g {GLYPH}><path fill="{ink}" d="{D_UT}"/><path fill="{res}" d="{d_res}"/></g>'
               + broken_ring(CX, CY, RO, SW, ink, acc, DOT_R, DOT_D))


def mark(ring, dot):
    """The mark alone, for tiles, avatars and slides."""
    return svg("0 0 100 100", broken_ring(50, 50, 37, 10, ring, dot, 6.5, 53))


def tile(plate, ring, dot):
    """Favicon. Heavier stroke: at 16 px the web line is too fine."""
    return svg("0 0 200 200",
               f'<rect width="200" height="200" rx="44" fill="{plate}"/>'
               f'<g transform="translate(22,22) scale(1.52)">'
               f'{broken_ring(50, 50, 37, 13, ring, dot, 7.5, 54)}</g>')


files = {
    "logo-wordmark.svg":       wordmark(INK, ACC),
    "logo-wordmark-light.svg": wordmark(INK_L, ACC_L),
    "logo-wordmark-mono.svg":  wordmark("currentColor", "currentColor"),
    "logo-mark.svg":           mark(INK, ACC),
    "logo-mark-light.svg":     mark(INK_L, ACC_L),
    "logo-mark-mono.svg":      mark("currentColor", "currentColor"),
    "favicon.svg":             tile(BG, ACC, INK),
}
for name, data in files.items():
    open(os.path.join(OUT, name), "w").write(data + "\n")
    print(f"{name:26} {len(data):6} bytes")
