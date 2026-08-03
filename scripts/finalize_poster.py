#!/usr/bin/env python3
"""Fail-closed poster finalizer.

One command = render the poster HTML at 2x + run the four sign-off metrics.
The output PNG survives only on PASS; on FAIL it is deleted and no artwork
is delivered. This is the canonical implementation of the metrics — the
table in SKILL.md is a summary of THIS script, not a second source of truth.

The metrics are factory inspection, not creative targets: run this once,
after the user approves the look. User-approved deviations are recorded
explicitly with --waive (they are printed loudly, not hidden).

Usage:
  python3 scripts/finalize_poster.py poster.html output.png --width 1400 --height 931
  python3 scripts/finalize_poster.py poster.html output.png -W 1000 -H 1500 \
      --waive ink --waive thumbnail        # user-approved deviations
  python3 scripts/finalize_poster.py --measure-only existing.png   # report, no render
"""

from __future__ import annotations

import argparse
import colorsys
import json
import shutil
import statistics
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python3 -m pip install Pillow") from exc

BROWSER_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
    "chromium",
    "chromium-browser",
    "google-chrome",
    "chrome",
]

WAIVABLE = ("anchor", "thumbnail", "ink")

# Thresholds — the single source of truth for the four sign-off metrics.
ANCHOR_RANGE = (0.8, 2.5)      # % of canvas with sat>0.35 and v>0.12
THUMBNAIL_MIN = 0.6            # same measure after resizing to 160px wide
INK_RANGE = (8.0, 25.0)        # % of pixels with Manhattan distance >46 from paper
SAT_T, VAL_T, INK_T, THUMB_W = 0.35, 0.12, 46, 160


def find_browser() -> str | None:
    for cand in BROWSER_CANDIDATES:
        p = Path(cand)
        if p.is_absolute():
            if p.is_file():
                return str(p)
        else:
            found = shutil.which(cand)
            if found:
                return found
    return None


def render(browser: str, html: Path, out: Path, width: int, height: int, scale: int) -> None:
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--force-device-scale-factor={scale}",
        f"--screenshot={out}",
        f"--window-size={width},{height}",
        html.resolve().as_uri(),
    ]
    if sys.platform != "darwin":
        cmd.insert(1, "--no-sandbox")
    subprocess.run(cmd, check=True, capture_output=True)
    if not out.is_file():
        raise RuntimeError("browser exited 0 but wrote no screenshot")


def scan(image: Image.Image, paper: tuple[int, int, int]) -> tuple[float, float, list[float]]:
    """Return (anchor %, ink %, anchor hue list) for one image."""
    px = image.load()
    w, h = image.size
    total = w * h
    anchor = ink = 0
    hues: list[float] = []
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if s > SAT_T and v > VAL_T:
                anchor += 1
                hues.append(hh * 360)
            if abs(r - paper[0]) + abs(g - paper[1]) + abs(b - paper[2]) > INK_T:
                ink += 1
    return anchor / total * 100, ink / total * 100, hues


def measure(png: Path, paper_hex: str) -> dict:
    paper_hex = paper_hex.lstrip("#")
    paper = tuple(int(paper_hex[i : i + 2], 16) for i in (0, 2, 4))
    with Image.open(png) as opened:
        im = opened.convert("RGB")
    anchor_pct, ink_pct, hues = scan(im, paper)
    tw = THUMB_W
    th = max(1, round(im.size[1] * tw / im.size[0]))
    thumb_pct, _, _ = scan(im.resize((tw, th)), paper)

    hue_report = None
    if hues:
        hues.sort()
        k = max(1, len(hues) // 20)
        hue_report = {
            "median_deg": round(statistics.median(hues)),
            "p5_deg": round(hues[k - 1]),
            "p95_deg": round(hues[-k]),
        }

    return {
        "file": str(png),
        "size": list(im.size),
        "anchor_pct": round(anchor_pct, 2),
        "thumbnail_anchor_pct": round(thumb_pct, 2),
        "ink_pct": round(ink_pct, 2),
        "paper_pct": round(100 - ink_pct, 1),
        "hue": hue_report,  # informational — dual hue is legal when user-named
        "checks": {
            "anchor": ANCHOR_RANGE[0] <= anchor_pct <= ANCHOR_RANGE[1],
            "thumbnail": thumb_pct >= THUMBNAIL_MIN,
            "ink": INK_RANGE[0] <= ink_pct <= INK_RANGE[1],
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", type=Path, nargs="?")
    ap.add_argument("output", type=Path, nargs="?")
    ap.add_argument("-W", "--width", type=int, help="CSS width of .poster")
    ap.add_argument("-H", "--height", type=int, help="CSS height of .poster")
    ap.add_argument("--scale", type=int, default=2)
    ap.add_argument("--paper", default="#e9e3d5", help="paper colour hex (default #e9e3d5)")
    ap.add_argument("--waive", action="append", default=[], choices=WAIVABLE,
                    help="record a user-approved deviation (repeatable)")
    ap.add_argument("--measure-only", type=Path, metavar="PNG",
                    help="measure an existing PNG; no render, nothing deleted")
    ap.add_argument("--keep-on-fail", action="store_true")
    args = ap.parse_args()

    if args.measure_only:
        report = measure(args.measure_only, args.paper)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    if not (args.html and args.output and args.width and args.height):
        ap.error("html, output, --width and --height are required (or use --measure-only)")
    if not args.html.is_file():
        raise SystemExit(f"HTML not found: {args.html}")
    if args.output.resolve() == args.html.resolve():
        raise SystemExit("output must be a new file")

    browser = find_browser()
    if browser is None:
        raise SystemExit(
            "no Chrome/Chromium found — hand the user the HTML file itself "
            "and ask them to open and screenshot it (see SKILL.md capability check)"
        )

    try:
        render(browser, args.html, args.output, args.width, args.height, args.scale)
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        raise SystemExit(f"FINALIZATION FAILED at render: {exc}")

    report = measure(args.output, args.paper)
    waived = sorted(set(args.waive))
    failed = [k for k, ok in report["checks"].items() if not ok and k not in waived]
    report["waived_user_approved"] = waived

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failed:
        if not args.keep_on_fail:
            args.output.unlink(missing_ok=True)
            print(f"FINALIZATION FAILED: {', '.join(failed)} out of range; output removed — deliver no artwork.")
        else:
            print(f"FINALIZATION FAILED: {', '.join(failed)} out of range (kept for debugging).")
        print("If the user explicitly approved this deviation, rerun with --waive.")
        return 1

    if waived:
        print(f"WAIVED (user-approved deviation, recorded): {', '.join(waived)}")
    print(f"DELIVERY PASS: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
