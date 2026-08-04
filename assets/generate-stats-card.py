#!/usr/bin/env python3
"""Build an animated isometric GitHub stats card straight from the GitHub API.

No third-party image host involved — the SVG is committed to this repo and
refreshed by .github/workflows/stats.yml, so it cannot 503 on the README.

Usage:  python3 assets/generate-stats-card.py [username]
Env:    GITHUB_TOKEN (optional locally, provided in Actions) raises the rate limit.
"""
import json, math, os, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

g3 = import_module("generate-3d-assets".replace("-", "_")) if False else None  # noqa

# --- shared drawing helpers (kept local so this script stands alone) ---------
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,monospace"
KX, KY, KZ = math.cos(math.radians(30)), 0.30, 0.62
USER = sys.argv[1] if len(sys.argv) > 1 else "Het161"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "github-stats-3d.svg")

LANG_COLORS = {
    "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "Python": "#3572A5", "HTML": "#e34c26",
    "CSS": "#563d7c", "Java": "#b07219", "C++": "#f34b7d", "C": "#555555", "Shell": "#89e051",
    "Jupyter Notebook": "#DA5B0B", "SCSS": "#c6538c", "Dockerfile": "#384d54", "Go": "#00ADD8",
    "PHP": "#4F5D95", "Ruby": "#701516", "Rust": "#dea584", "Vue": "#41b883", "Svelte": "#ff3e00",
    "EJS": "#a91e50", "Handlebars": "#f7931e", "Makefile": "#427819", "PLpgSQL": "#336790",
}
FALLBACK = ["#8b5cf6", "#22d3ee", "#f472b6", "#38bdf8", "#a855f7", "#34d399", "#f59e0b"]


def iso(x, y, z=0.0, s=30.0, ox=0.0, oy=0.0):
    return (ox + (x - y) * KX * s, oy + (x + y) * KY * s - z * KZ * s)


def shade(hexcol, f):
    hexcol = hexcol.lstrip("#")
    r, g, b = (int(hexcol[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(c * f))) for c in (r, g, b))


def poly(pts, fill, extra=""):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{d}" fill="{fill}" {extra}/>'


def box(gx, gy, w, d, h, color, s=30.0, ox=0.0, oy=0.0, stroke=None):
    P = lambda x, y, z: iso(x, y, z, s, ox, oy)
    top = [P(gx, gy, h), P(gx + w, gy, h), P(gx + w, gy + d, h), P(gx, gy + d, h)]
    right = [P(gx + w, gy, h), P(gx + w, gy, 0), P(gx + w, gy + d, 0), P(gx + w, gy + d, h)]
    left = [P(gx, gy + d, h), P(gx, gy + d, 0), P(gx + w, gy + d, 0), P(gx + w, gy + d, h)]
    st = f'stroke="{stroke}" stroke-width="1" stroke-linejoin="round"' if stroke else ""
    return poly(left, shade(color, .45), st) + poly(right, shade(color, .68), st) + poly(top, color, st)


def label(x, y, text, size=13, fill="#e2e8f0", anchor="middle", font=FONT, weight="600", ls="0"):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(text)}</text>')


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def float_anim(dy=6, dur=4.0, begin=0.0):
    return (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -{dy};0 0" '
            f'dur="{dur}s" begin="{begin}s" repeatCount="indefinite" calcMode="spline" '
            f'keyTimes="0;0.5;1" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>')


# --- data -------------------------------------------------------------------
def api(path):
    req = urllib.request.Request("https://api.github.com" + path,
                                 headers={"Accept": "application/vnd.github+json",
                                          "User-Agent": "profile-stats-card"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect(user):
    profile = api(f"/users/{user}")
    repos, page = [], 1
    while True:
        chunk = api(f"/users/{user}/repos?per_page=100&page={page}&type=owner&sort=pushed")
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r.get("fork")]
    langs = {}
    for r in own:
        try:
            for name, byts in api(f"/repos/{r['full_name']}/languages").items():
                langs[name] = langs.get(name, 0) + byts
        except urllib.error.HTTPError:
            if r.get("language"):
                langs[r["language"]] = langs.get(r["language"], 0) + 1
    return {
        "name": profile.get("name") or user,
        "repos": len(own),
        "stars": sum(r.get("stargazers_count", 0) for r in own),
        "followers": profile.get("followers", 0),
        "since": (profile.get("created_at") or "")[:7],
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
    }


# --- drawing ----------------------------------------------------------------
def build(d):
    W, H = 1200, 460
    top = d["langs"][:6]
    total = sum(v for _, v in top) or 1
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">',
         '<defs>'
         '<linearGradient id="sbg" x1="0" y1="0" x2="1" y2="1">'
         '<stop offset="0%" stop-color="#0b1020"/><stop offset="55%" stop-color="#0d1226"/>'
         '<stop offset="100%" stop-color="#140d2b"/></linearGradient>'
         '<radialGradient id="sgA" cx="50%" cy="50%"><stop offset="0%" stop-color="#8b5cf6" stop-opacity=".42"/>'
         '<stop offset="100%" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>'
         '<radialGradient id="sgB" cx="50%" cy="50%"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".32"/>'
         '<stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>'
         '<filter id="ssoft" x="-60%" y="-60%" width="220%" height="220%">'
         '<feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/>'
         '<feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="url(#sbg)" stroke="#26304d" stroke-width="1.5"/>',
         f'<ellipse cx="330" cy="120" rx="420" ry="230" fill="url(#sgA)"/>',
         f'<ellipse cx="940" cy="380" rx="360" ry="200" fill="url(#sgB)"/>',
         label(600, 48, "GITHUB — BUILT FROM THE API, REFRESHED DAILY", 15.5, "#c7d2fe", ls="3.5"),
         label(600, 72, f"@{USER} · building in public since {d['since']}", 12, "#7f8fb3", font=MONO)]

    # stat tiles
    tiles = [("PUBLIC REPOS", d["repos"], "#8b5cf6"), ("TOTAL STARS", d["stars"], "#f5b32a"),
             ("FOLLOWERS", d["followers"], "#22d3ee"), ("LANGUAGES", len(d["langs"]), "#34d399")]
    for i, (k, v, c) in enumerate(tiles):
        x, y = 86 + (i % 2) * 190, 130 + (i // 2) * 132
        o.append(f'<rect x="{x}" y="{y}" width="166" height="106" rx="14" fill="{c}" fill-opacity=".08" '
                 f'stroke="{c}" stroke-opacity=".45"/>')
        o.append(f'<rect x="{x}" y="{y}" width="166" height="3" rx="1.5" fill="{c}" opacity=".9">'
                 f'<animate attributeName="opacity" values=".35;1;.35" dur="{3.2+i*0.5}s" repeatCount="indefinite"/></rect>')
        o.append(label(x + 83, y + 62, str(v), 38, shade(c, 1.4), font=MONO, weight="800"))
        o.append(label(x + 83, y + 86, k, 10.5, "#8c9bbd", font=MONO, weight="700", ls="1.2"))

    # isometric language bars — a row descending to the right, legend beside it
    n = len(top)
    s, step, bw = 30.0, 1.6, 1.15
    span = ((n - 1) * step + bw) * KX * s
    gox, goy = 690 - span / 2, 208
    o.append(label(gox - 6, 110, "TOP LANGUAGES BY BYTES", 12, "#93a4c8", anchor="start",
                   font=MONO, weight="700", ls="1.5"))
    maxv = top[0][1] if top else 1
    for i, (name, v) in enumerate(top):
        pct = 100.0 * v / total
        hgt = 0.5 + 3.1 * (v / maxv)
        col = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        gx = i * step
        b = box(gx, 0, bw, bw, hgt, col, s, gox, goy, stroke=shade(col, 1.5))
        o.append(f'<g>{float_anim(5, 4.0 + i * 0.4, i * 0.3)}{b}</g>')
        tx, ty = iso(gx + bw / 2, bw / 2, hgt, s, gox, goy)
        o.append(label(tx, ty - 12, f"{pct:.0f}%", 10.5, shade(col, 1.5), font=MONO, weight="800"))

    # legend
    lx0 = 946
    for i, (name, v) in enumerate(top):
        col = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        ly = 152 + i * 42
        o.append(f'<rect x="{lx0}" y="{ly-11}" width="13" height="13" rx="3.5" fill="{col}">'
                 f'<animate attributeName="opacity" values=".45;1;.45" dur="{3.0+i*0.35}s" repeatCount="indefinite"/></rect>')
        o.append(label(lx0 + 24, ly, name, 12, "#cbd5e1", anchor="start", font=MONO, weight="600"))
        o.append(label(1146, ly, f"{100.0 * v / total:.1f}%", 12, shade(col, 1.45),
                       anchor="end", font=MONO, weight="800"))
        o.append(f'<rect x="{lx0}" y="{ly+8}" width="200" height="2" rx="1" fill="#1e293b"/>')
        o.append(f'<rect x="{lx0}" y="{ly+8}" width="{200.0 * v / maxv:.0f}" height="2" rx="1" fill="{col}" opacity=".8"/>')

    o.append(label(600, 432, "no third-party image host — this card is generated from the GitHub API and committed to the repo",
                   11, "#6b7ba3", font=MONO, weight="500"))
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    try:
        data = collect(USER)
    except Exception as e:                                  # keep the last good card
        print(f"stats fetch failed ({e}) — leaving existing card untouched")
        sys.exit(0)
    with open(OUT, "w") as f:
        f.write(build(data))
    print(f"wrote {OUT}: {data['repos']} repos, {data['stars']} stars, "
          f"{data['followers']} followers, {len(data['langs'])} languages")
