#!/usr/bin/env python3
"""Render PNG fallbacks for every animated scene SVG.

The GitHub mobile app's image decoder renders static SVG but fails on animated
SVG, so README.md serves the .svg above 768px and these PNGs everywhere else.
Re-run after changing any artwork:

    python3 assets/generate-3d-assets.py
    python3 assets/make-png-fallbacks.py

macOS only — uses qlmanage (render), sips (crop/resize) and pngquant (compress).
"""

import os, re, subprocess
SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "png")
os.makedirs(OUT, exist_ok=True)
W = 1600
for n in sorted(os.listdir(SRC)):
    if not n.endswith(".svg"): continue
    src = open(os.path.join(SRC, n)).read()
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', src)
    w, h = int(m.group(1)), int(m.group(2))
    inner = src.split(">", 1)[1].rsplit("</svg>", 1)[0]
    ch = 1200 * h / w
    y = (1200 - ch) / 2
    wrap = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="1200" height="1200" viewBox="0 0 1200 1200">'
            f'<svg x="0" y="{y:.2f}" width="1200" height="{ch:.2f}" viewBox="0 0 {w} {h}">{inner}</svg></svg>')
    tmp = os.path.join("/tmp", f"w_{n}")
    open(tmp, "w").write(wrap)
    subprocess.run(["qlmanage", "-t", "-s", str(W), "-o", "/tmp", tmp],
                   capture_output=True)
    png = f"{tmp}.png"
    if not os.path.exists(png):
        print("RENDER FAILED", n); continue
    crop_h = round(W * h / w)
    dest = os.path.join(OUT, n[:-4] + ".png")
    subprocess.run(["sips", "-c", str(crop_h), str(W), png, "--out", dest],
                   capture_output=True)
    print(f"{n[:-4]+'.png':<28} {W}x{crop_h}  {os.path.getsize(dest)//1024} KB")
    subprocess.run(["sips", "-Z", "1200", dest, "--out", dest], capture_output=True)
    subprocess.run(["pngquant", "--quality=60-88", "--speed", "1", "--force",
                    "--output", dest, dest], capture_output=True)
    os.remove(png); os.remove(tmp)
    print(f"  -> compressed to {os.path.getsize(dest)//1024} KB")
