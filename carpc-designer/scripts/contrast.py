#!/usr/bin/env python3
"""WCAG 2.x contrast ratio checker for car-UI palettes.

Usage:
  contrast.py "#c9d2e0" "#0b0f17"            # one pair
  contrast.py --min 4.5 --json palette.json   # many pairs

palette.json format (translucent colours as #RRGGBBAA are composited over the pair's "bg"):
  {"night": [["text", "#c9d2e0", "#0b0f17"], ["hint", "#7f8ba0", "#0b0f17"]]}

Exit code 1 if any pair is below --min (default 4.5, the automotive text minimum).
"""
import argparse
import json
import sys


def parse(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) not in (6, 8):
        raise ValueError("bad colour: " + h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return r, g, b, a


def over(fg, bg):
    r, g, b, a = fg
    return tuple(round(a * f + (1 - a) * k) for f, k in zip((r, g, b), bg[:3]))


def lum(rgb):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(fg_hex, bg_hex):
    bg = parse(bg_hex)
    fg = over(parse(fg_hex), bg)
    l1, l2 = lum(fg), lum(bg[:3])
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fg", nargs="?")
    ap.add_argument("bg", nargs="?")
    ap.add_argument("--json")
    ap.add_argument("--min", type=float, default=4.5)
    a = ap.parse_args()
    bad = 0
    pairs = []
    if a.json:
        with open(a.json, encoding="utf-8") as f:
            data = json.load(f)
        for theme, items in data.items():
            for name, fg, bg in items:
                pairs.append((theme + ":" + name, fg, bg))
    elif a.fg and a.bg:
        pairs.append(("pair", a.fg, a.bg))
    else:
        ap.error("give FG BG or --json FILE")
    for name, fg, bg in pairs:
        r = ratio(fg, bg)
        ok = r >= a.min
        bad += not ok
        print("%-28s %s on %s  %5.2f:1  %s" % (name, fg, bg, r, "ok" if ok else "FAIL (< %.1f)" % a.min))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
