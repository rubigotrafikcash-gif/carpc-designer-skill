#!/usr/bin/env python3
"""dp <-> px converter and automotive minimums in px.

Usage:
  dp_px.py 213            # table of minimums for a 213 dpi screen
  dp_px.py 213 --dp 76    # 76 dp in px
  dp_px.py 213 --px 96    # 96 px in dp
px = dp * dpi / 160
"""
import argparse

MINS = [("secondary text", 24), ("primary text", 32), ("touch target", 76), ("target gap (working value)", 23)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dpi", type=float)
    ap.add_argument("--dp", type=float)
    ap.add_argument("--px", type=float)
    a = ap.parse_args()
    k = a.dpi / 160.0
    if a.dp is not None:
        print("%.1f dp = %.1f px at %.0f dpi" % (a.dp, a.dp * k, a.dpi))
    if a.px is not None:
        print("%.1f px = %.1f dp at %.0f dpi" % (a.px, a.px / k, a.dpi))
    if a.dp is None and a.px is None:
        print("factor %.3f px per dp at %.0f dpi" % (k, a.dpi))
        for name, dp in MINS:
            print("%-28s %3d dp = %5.1f px" % (name, dp, dp * k))


if __name__ == "__main__":
    main()
