#!/usr/bin/env python3
"""Generate animated isometric SVG assets for the Het161 profile README."""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,monospace"

# ---------------------------------------------------------------- iso helpers
KX = math.cos(math.radians(30))   # 0.866
KY = 0.30                          # flattened (dimetric) — reads better for stacks
KZ = 0.62


def iso(x, y, z=0.0, s=30.0, ox=0.0, oy=0.0):
    return (ox + (x - y) * KX * s, oy + (x + y) * KY * s - z * KZ * s)


def shade(hexcol, f):
    hexcol = hexcol.lstrip('#')
    r, g, b = (int(hexcol[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (max(0, min(255, int(c * f))) for c in (r, g, b))
    return f'#{r:02x}{g:02x}{b:02x}'


def poly(pts, fill, extra=""):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{d}" fill="{fill}" {extra}/>'


def box(gx, gy, w, d, h, color, s=30.0, ox=0.0, oy=0.0, op=1.0, stroke=None):
    """3D box: top + right(+x) + left(+y) faces."""
    P = lambda x, y, z: iso(x, y, z, s, ox, oy)
    top = [P(gx, gy, h), P(gx + w, gy, h), P(gx + w, gy + d, h), P(gx, gy + d, h)]
    right = [P(gx + w, gy, h), P(gx + w, gy, 0), P(gx + w, gy + d, 0), P(gx + w, gy + d, h)]
    left = [P(gx, gy + d, h), P(gx, gy + d, 0), P(gx + w, gy + d, 0), P(gx + w, gy + d, h)]
    st = f'stroke="{stroke}" stroke-width="1" stroke-linejoin="round"' if stroke else ''
    o = f'opacity="{op}"' if op != 1.0 else ''
    return (f'<g {o}>' +
            poly(left, shade(color, .45), st) +
            poly(right, shade(color, .68), st) +
            poly(top, color, st) + '</g>')


def plate(W, D, color, s=30.0, ox=0.0, oy=0.0, th=0.5, op=1.0, stroke=None):
    return box(0, 0, W, D, th, color, s, ox, oy, op, stroke)


def grid_lines(W, D, s, ox, oy, color, op=0.25, step=1):
    out = []
    for i in range(0, W + 1, step):
        a, b = iso(i, 0, 0, s, ox, oy), iso(i, D, 0, s, ox, oy)
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="1" opacity="{op}"/>')
    for j in range(0, D + 1, step):
        a, b = iso(0, j, 0, s, ox, oy), iso(W, j, 0, s, ox, oy)
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="1" opacity="{op}"/>')
    return "".join(out)


def defs_common(extra=""):
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0b1020"/><stop offset="55%" stop-color="#0d1226"/><stop offset="100%" stop-color="#140d2b"/>
</linearGradient>
<radialGradient id="glowA" cx="50%" cy="50%">
  <stop offset="0%" stop-color="#8b5cf6" stop-opacity=".45"/><stop offset="100%" stop-color="#8b5cf6" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glowB" cx="50%" cy="50%">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".35"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glowGold" cx="50%" cy="50%">
  <stop offset="0%" stop-color="#f5b32a" stop-opacity=".30"/><stop offset="100%" stop-color="#f5b32a" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glowGreen" cx="50%" cy="50%">
  <stop offset="0%" stop-color="#34d399" stop-opacity=".28"/><stop offset="100%" stop-color="#34d399" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glowBlue" cx="50%" cy="50%">
  <stop offset="0%" stop-color="#3b82f6" stop-opacity=".38"/><stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
</radialGradient>
<filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="soft2" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
{extra}</defs>'''


def card(w, h, gA="glowA", gB="glowB"):
    return (f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20" fill="url(#bg)" stroke="#26304d" stroke-width="1.5"/>'
            f'<ellipse cx="{w*0.28:.0f}" cy="{h*0.25:.0f}" rx="{w*0.35:.0f}" ry="{h*0.5:.0f}" fill="url(#{gA})"/>'
            f'<ellipse cx="{w*0.78:.0f}" cy="{h*0.8:.0f}" rx="{w*0.3:.0f}" ry="{h*0.45:.0f}" fill="url(#{gB})"/>')


def stars(w, h, n=60, seed=7):
    rnd = seed
    out = []
    for i in range(n):
        rnd = (rnd * 1103515245 + 12345) % 2147483648
        x = (rnd / 2147483648) * w
        rnd = (rnd * 1103515245 + 12345) % 2147483648
        y = (rnd / 2147483648) * h
        rnd = (rnd * 1103515245 + 12345) % 2147483648
        r = 0.6 + (rnd / 2147483648) * 1.1
        dur = 2.2 + (i % 7) * 0.45
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#c7d2fe" opacity=".5">'
                   f'<animate attributeName="opacity" values=".12;.75;.12" dur="{dur:.1f}s" begin="{i*0.13:.2f}s" repeatCount="indefinite"/></circle>')
    return "".join(out)


def float_anim(dy=6, dur=4.0, begin=0.0):
    return (f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 0;0 -{dy};0 0" dur="{dur}s" begin="{begin}s" '
            f'repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>')


def label(x, y, text, size=13, fill="#e2e8f0", anchor="middle", font=FONT, weight="600", op=1.0, ls="0"):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" opacity="{op}" letter-spacing="{ls}">{text}</text>')


def wire(p0, p1, color="#8b5cf6", bend=42, dur=2.2, begin=0.0, dots=2, width=1.6):
    """Vertical-ish connector with marching dashes + traveling packets."""
    (x0, y0), (x1, y1) = p0, p1
    d = f"M {x0:.1f} {y0:.1f} C {x0:.1f} {y0+bend:.1f} {x1:.1f} {y1-bend:.1f} {x1:.1f} {y1:.1f}"
    out = [f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-opacity=".45" '
           f'stroke-dasharray="6 8" stroke-linecap="round">'
           f'<animate attributeName="stroke-dashoffset" values="28;0" dur="1.4s" repeatCount="indefinite"/></path>']
    for k in range(dots):
        b = begin + k * (dur / dots)
        out.append(f'<circle r="3.2" fill="{color}" filter="url(#soft2)">'
                   f'<animateMotion dur="{dur}s" begin="{b:.2f}s" repeatCount="indefinite" path="{d}"/>'
                   f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="{dur}s" begin="{b:.2f}s" repeatCount="indefinite"/>'
                   f'</circle>')
    return "".join(out)


def svg_open(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">')


# ============================================================ 1. HERO SKYLINE
def hero():
    W, H = 1200, 340
    s = 24.0
    o = [svg_open(W, H), defs_common('''
<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#a78bfa"/><stop offset="45%" stop-color="#f0abfc"/>
  <stop offset="55%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#a78bfa"/>
  <animate attributeName="x1" values="-1;1" dur="6s" repeatCount="indefinite"/>
  <animate attributeName="x2" values="0;2" dur="6s" repeatCount="indefinite"/>
</linearGradient>'''), card(W, H), stars(W, H, 70)]

    GW, GD = 12, 7
    city_cx = 878
    gox = city_cx - (GW - GD) * KX * s / 2
    goy = 132
    o.append(f'<g opacity=".55">{grid_lines(GW, GD, s, gox, goy, "#3b4a7a", .5)}</g>')

    # skyline: heights driven by a wave so it reads as an equalizer city
    palette = ["#8b5cf6", "#6366f1", "#22d3ee", "#a855f7", "#38bdf8", "#c084fc"]
    towers = []
    for gx in range(0, GW, 2):
        for gy in range(0, GD, 2):
            k = (gx // 2) + (gy // 2)
            h = 1.1 + 2.6 * abs(math.sin(gx * 0.55 + gy * 0.9))
            col = palette[k % len(palette)]
            towers.append((gx, gy, h, col, k))
    towers.sort(key=lambda t: (t[0] + t[1]))
    for gx, gy, h, col, k in towers:
        dur = 3.2 + (k % 5) * 0.55
        b = (k % 6) * 0.35
        inner = box(gx, gy, 1.5, 1.5, h, col, s, gox, goy, stroke=shade(col, 1.45))
        o.append(f'<g>{float_anim(9, dur, b)}{inner}</g>')

    # floating cubes
    o.append(f'<g filter="url(#soft)" opacity=".9">{float_anim(12, 5.5, .4)}'
             f'{box(0,0,1,1,1,"#22d3ee",26.0,700,74,op=.9,stroke="#a5f3fc")}</g>')
    o.append(f'<g opacity=".85">{float_anim(10, 6.2, 1.1)}'
             f'{box(0,0,1,1,1,"#f472b6",20.0,1108,272,op=.85,stroke="#fbcfe8")}</g>')

    # headline block (left)
    o.append(f'<text x="72" y="140" font-family="{MONO}" font-size="50" font-weight="800" fill="url(#shine)" letter-spacing="5">HET PATEL</text>')
    o.append(f'<rect x="74" y="158" width="118" height="3" rx="1.5" fill="#8b5cf6"><animate attributeName="width" values="0;340;340" keyTimes="0;.35;1" dur="4s" repeatCount="indefinite"/></rect>')
    o.append(label(72, 192, "FULL-STACK DEVELOPER  ·  SAAS  ·  AI PRODUCTS", 14, "#9fb0d0", anchor="start", ls="2.4"))
    o.append(label(72, 226, "Next.js · Express · Prisma · PostgreSQL · Groq · Claude", 12.5, "#7c8db5", anchor="start", font=MONO, weight="500"))
    for i, (t, c) in enumerate([("LIVE SAAS", "#8b5cf6"), ("25+ FEATURES", "#22d3ee"), ("19+ SITES", "#f472b6")]):
        bx = 72 + i * 132
        o.append(f'<g><rect x="{bx}" y="254" width="118" height="30" rx="15" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-opacity=".55"/>'
                 f'{label(bx + 59, 273, t, 11, shade(c, 1.55), font=MONO, weight="700")}'
                 f'<animate attributeName="opacity" values=".55;1;.55" dur="{3.4 + i*0.6}s" begin="{i*0.5}s" repeatCount="indefinite"/></g>')
    o.append('</svg>')
    return "".join(o)


# ==================================================== 2. FIRSTBOOKIT ARCH
def architecture():
    W, H = 1200, 820
    o = [svg_open(W, H), defs_common(), card(W, H), stars(W, H, 55, seed=19)]
    o.append(label(600, 48, "FIRSTBOOKIT — PRODUCTION ARCHITECTURE", 17, "#e9d5ff", ls="4"))
    o.append(label(600, 74, "multi-role booking SaaS · Next.js 15 · Express · Prisma · PostgreSQL", 12.5, "#8093b8", font=MONO))

    s = 26.0
    PW, PD = 15, 6
    layers = [
        ("CLIENT",      "#8b5cf6", 212, [("Next.js 15 App", 0.4, 0.6, 4.4, 4.2, 1.5), ("React 19 UI", 5.6, 0.6, 4.0, 4.2, 1.1), ("TanStack Query", 10.4, 0.6, 4.2, 4.2, 0.9)]),
        ("API LAYER",   "#6366f1", 368, [("Express REST", 0.4, 0.6, 4.4, 4.2, 1.5), ("JWT · 3 Roles", 5.6, 0.6, 4.0, 4.2, 1.2), ("node-cron Jobs", 10.4, 0.6, 4.2, 4.2, 0.9)]),
        ("DOMAIN",      "#22d3ee", 524, [("Scheduling", 0.4, 0.6, 4.4, 4.2, 1.4), ("Dynamic Pricing", 5.6, 0.6, 4.0, 4.2, 1.4), ("Analytics", 10.4, 0.6, 4.2, 4.2, 1.0)]),
        ("DATA + EDGE", "#a855f7", 680, [("PostgreSQL", 0.4, 0.6, 4.4, 4.2, 1.6), ("Prisma ORM", 5.6, 0.6, 4.0, 4.2, 1.0), ("Razorpay · WA", 10.4, 0.6, 4.2, 4.2, 1.2)]),
    ]

    notes = [
        ["role-aware dashboards", "venue owner · admin · player"],
        ["REST + JWT middleware", "scheduled jobs, timezone-safe"],
        ["templates, overrides, slots", "peak / off-peak price rules"],
        ["Prisma migrations · N+1 fixed", "Razorpay refunds · WhatsApp"],
    ]
    ox = 545 - (PW - PD) * KX * s / 2
    anchors = []  # per layer: list of (screen x, top y, bottom y)
    body = []
    for li, (name, col, cy, boxes) in enumerate(layers):
        gox = ox
        goy = cy - (PW + PD) * KY * s / 2
        g = [f'<g opacity=".96">']
        g.append(plate(PW, PD, shade(col, .30), s, gox, goy, th=0.45, stroke=shade(col, .75)))
        g.append(f'<g opacity=".5">{grid_lines(PW, PD, s, gox, goy - 0.45*KZ*s, shade(col, 1.5), .18)}</g>')
        lay_anchor = []
        for bi, (txt, bx, by, bw, bd, bh) in enumerate(boxes):
            bcol = shade(col, 1.0 + 0.12 * bi)
            inner = box(bx, by, bw, bd, bh + 0.45, bcol, s, gox, goy, stroke=shade(bcol, 1.5))
            g.append(f'<g>{float_anim(4, 4.6 + bi * 0.5, li * 0.4 + bi * 0.3)}{inner}</g>')
            # label at centre of box top face
            tx, ty = iso(bx + bw / 2, by + bd / 2, bh + 0.45, s, gox, goy)
            g.append(label(tx, ty + 4, txt, 11.5, "#f8fafc", font=MONO, weight="700"))
            top = iso(bx + bw / 2, by + bd / 2, bh + 0.45, s, gox, goy)
            bot = iso(bx + bw / 2, by + bd, 0, s, gox, goy)
            lay_anchor.append((top, bot))
        g.append('</g>')
        # layer caption to the left
        lx, ly = iso(0, PD, 0, s, gox, goy)
        body.append("".join(g))
        body.append(label(lx - 22, ly - 26, name, 12.5, shade(col, 1.5), anchor="end", font=MONO, ls="1.5"))
        # right-hand annotation column
        nx, ny = 1140, cy - 26
        body.append(f'<rect x="{nx-268}" y="{ny-18}" width="2.5" height="46" rx="1.25" fill="{shade(col,1.4)}" opacity=".75">'
                    f'<animate attributeName="opacity" values=".3;.9;.3" dur="{3.5+li*0.4}s" repeatCount="indefinite"/></rect>')
        body.append(label(nx, ny, notes[li][0], 12, shade(col, 1.45), anchor="end", font=MONO, weight="700"))
        body.append(label(nx, ny + 22, notes[li][1], 11.5, "#7f8fb3", anchor="end", font=MONO, weight="500"))
        anchors.append(lay_anchor)

    # connectors drawn beneath the plates
    links = []
    for li in range(len(layers) - 1):
        col = layers[li + 1][1]
        for bi in range(3):
            p0 = anchors[li][bi][1]
            p1 = anchors[li + 1][bi][0]
            links.append(wire(p0, p1, shade(col, 1.35), bend=34, dur=2.4 + bi * .3, begin=li * .4 + bi * .5, dots=2))
    o.append("".join(links))
    o.append("".join(body))

    # side stats
    o.append(f'<g opacity=".9">{label(600, 796, "25+ shipped features  ·  real venues  ·  real payments  ·  live in production", 12, "#7c8db5", font=MONO)}</g>')
    o.append('</svg>')
    return "".join(o)


# ========================================================== 3. STACK ORBIT
def ellipse_path(cx, cy, rx, ry, rot_deg, segs=8):
    a = math.radians(rot_deg)
    ca, sa = math.cos(a), math.sin(a)

    def P(t):
        x, y = rx * math.cos(t), ry * math.sin(t)
        return (cx + x * ca - y * sa, cy + x * sa + y * ca)

    def D(t):
        x, y = -rx * math.sin(t), ry * math.cos(t)
        return (x * ca - y * sa, x * sa + y * ca)

    step = 2 * math.pi / segs
    d = []
    p0 = P(0)
    d.append(f"M {p0[0]:.2f} {p0[1]:.2f}")
    for i in range(segs):
        t0, t1 = i * step, (i + 1) * step
        pa, pb = P(t0), P(t1)
        da, db = D(t0), D(t1)
        f = (t1 - t0) / 3
        c1 = (pa[0] + da[0] * f, pa[1] + da[1] * f)
        c2 = (pb[0] - db[0] * f, pb[1] - db[1] * f)
        d.append(f"C {c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {pb[0]:.2f} {pb[1]:.2f}")
    d.append("Z")
    return " ".join(d)


def orbit():
    W, H = 1200, 460
    cx, cy = 600, 232
    o = [svg_open(W, H), defs_common(), card(W, H), stars(W, H, 55, seed=31)]
    o.append(label(600, 44, "THE STACK — IN ORBIT", 16, "#e9d5ff", ls="4"))

    rings = [
        (300, 92, -14, "#8b5cf6", 22.0, [("TS", 0), ("React", .25), ("Next.js", .5), ("Node", .75)]),
        (400, 122, 10, "#22d3ee", 28.0, [("Express", .1), ("Prisma", .35), ("PostgreSQL", .6), ("MongoDB", .85)]),
        (505, 152, -6, "#f472b6", 34.0, [("Tailwind", .05), ("Groq", .3), ("Claude API", .55), ("Vercel", .8)]),
    ]

    for rx, ry, rot, col, dur, nodes in rings:
        p = ellipse_path(cx, cy, rx, ry, rot)
        o.append(f'<path d="{p}" fill="none" stroke="{col}" stroke-width="1.3" stroke-opacity=".32" stroke-dasharray="3 7">'
                 f'<animate attributeName="stroke-dashoffset" values="20;0" dur="3s" repeatCount="indefinite"/></path>')
        for name, phase in nodes:
            beg = -phase * dur
            w = max(46, 8.4 * len(name))
            node = (f'<g>'
                    f'<rect x="{-w/2:.0f}" y="-13" width="{w:.0f}" height="26" rx="13" fill="#0f1730" fill-opacity=".92" stroke="{col}" stroke-width="1.4"/>'
                    f'{label(0, 4.5, name, 11.5, "#e6ecff", font=MONO, weight="700")}'
                    f'</g>')
            o.append(f'<g filter="url(#soft2)">'
                     f'<animateMotion dur="{dur}s" begin="{beg:.2f}s" repeatCount="indefinite" rotate="0" path="{p}"/>'
                     f'<animate attributeName="opacity" values="1;.98;.4;.35;.4;.98;1" keyTimes="0;.12;.3;.5;.7;.88;1" dur="{dur}s" begin="{beg:.2f}s" repeatCount="indefinite"/>'
                     f'{node}</g>')

    # core cube
    core = box(0, 0, 1, 1, 1, "#a855f7", 46.0, cx, cy - 6, stroke="#e9d5ff")
    o.append(f'<g filter="url(#soft)">{float_anim(7, 5.0, 0)}<g opacity=".95">{core}</g></g>')
    o.append(f'<circle cx="{cx}" cy="{cy+2}" r="76" fill="none" stroke="#c084fc" stroke-opacity=".35" stroke-width="1.2" stroke-dasharray="4 10">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy+2}" to="360 {cx} {cy+2}" dur="18s" repeatCount="indefinite"/></circle>')
    o.append(label(600, 430, "typescript · react · next · node · express · prisma · postgres · mongo · groq · claude", 11.5, "#7c8db5", font=MONO))
    o.append('</svg>')
    return "".join(o)


# ========================================================== 4. SHIP LOOP
def shiploop():
    W, H = 1200, 300
    o = [svg_open(W, H), defs_common(), card(W, H), stars(W, H, 30, seed=53)]
    o.append(label(600, 44, "SHIP IT.  ITERATE.  SHIP AGAIN.", 16, "#e9d5ff", ls="5"))

    s = 24.0
    steps = [("PLAN", "#8b5cf6"), ("BUILD", "#6366f1"), ("SHIP", "#22d3ee"), ("MEASURE", "#a855f7"), ("ITERATE", "#f472b6")]
    tops = []
    x0 = 150
    for i, (name, col) in enumerate(steps):
        gox = x0 + i * 225
        goy = 158
        b = box(0, 0, 3.2, 3.2, 1.5, col, s, gox, goy, stroke=shade(col, 1.5))
        o.append(f'<g>{float_anim(6, 4.0, i * 0.45)}{b}</g>')
        tx, ty = iso(1.6, 1.6, 1.5, s, gox, goy)
        o.append(label(tx, ty + 4, name, 12, "#f8fafc", font=MONO, weight="800"))
        tops.append((tx, ty))

    # forward links
    for i in range(len(steps) - 1):
        a = (tops[i][0] + 62, tops[i][1] + 26)
        b = (tops[i + 1][0] - 62, tops[i + 1][1] + 26)
        d = f"M {a[0]:.1f} {a[1]:.1f} L {b[0]:.1f} {b[1]:.1f}"
        o.append(f'<path d="{d}" stroke="#7dd3fc" stroke-width="1.6" stroke-opacity=".4" stroke-dasharray="5 7" fill="none">'
                 f'<animate attributeName="stroke-dashoffset" values="24;0" dur="1.2s" repeatCount="indefinite"/></path>')
        o.append(f'<circle r="3.4" fill="#7dd3fc" filter="url(#soft2)">'
                 f'<animateMotion dur="1.6s" begin="{i*1.6:.1f}s;{i*1.6+8:.1f}s" repeatCount="indefinite" path="{d}"/></circle>')

    # loop-back arc
    a = (tops[-1][0], tops[-1][1] + 58)
    b = (tops[0][0], tops[0][1] + 58)
    d = f"M {a[0]:.1f} {a[1]:.1f} C {a[0]:.1f} {a[1]+58:.1f} {b[0]:.1f} {b[1]+58:.1f} {b[0]:.1f} {b[1]:.1f}"
    o.append(label(600, 278, "plan → build → ship → measure → iterate", 11.5, "#6b7ba3", font=MONO))
    o.append(f'<path d="{d}" stroke="#f472b6" stroke-width="1.6" stroke-opacity=".45" fill="none" stroke-dasharray="6 8">'
             f'<animate attributeName="stroke-dashoffset" values="28;0" dur="1.6s" repeatCount="indefinite"/></path>')
    o.append(f'<circle r="3.6" fill="#f9a8d4" filter="url(#soft2)"><animateMotion dur="2.2s" repeatCount="indefinite" path="{d}"/></circle>')
    o.append('</svg>')
    return "".join(o)


def wire_h(p0, p1, color="#8b5cf6", dur=2.2, begin=0.0, dots=2, width=1.6, r=3.2):
    """Horizontal connector with marching dashes + traveling packets."""
    (x0, y0), (x1, y1) = p0, p1
    mid = (x1 - x0) * 0.45
    d = f"M {x0:.1f} {y0:.1f} C {x0+mid:.1f} {y0:.1f} {x1-mid:.1f} {y1:.1f} {x1:.1f} {y1:.1f}"
    out = [f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-opacity=".45" '
           f'stroke-dasharray="6 8" stroke-linecap="round">'
           f'<animate attributeName="stroke-dashoffset" values="28;0" dur="1.4s" repeatCount="indefinite"/></path>']
    for k in range(dots):
        b = begin + k * (dur / dots)
        out.append(f'<circle r="{r}" fill="{color}" filter="url(#soft2)">'
                   f'<animateMotion dur="{dur}s" begin="{b:.2f}s" repeatCount="indefinite" path="{d}"/>'
                   f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.85;1" dur="{dur}s" begin="{b:.2f}s" repeatCount="indefinite"/>'
                   f'</circle>')
    return "".join(out)


def chip(cx, cy, text, color, w=None, size=11, dur=None):
    w = w or (9.2 * len(text) + 26)
    a = (f'<animate attributeName="opacity" values=".6;1;.6" dur="{dur}s" repeatCount="indefinite"/>' if dur else '')
    return (f'<g>{a}<rect x="{cx-w/2:.0f}" y="{cy-15:.0f}" width="{w:.0f}" height="30" rx="15" '
            f'fill="{color}" fill-opacity=".13" stroke="{color}" stroke-opacity=".55"/>'
            f'{label(cx, cy + 4.5, text, size, shade(color, 1.5), font=MONO, weight="700")}</g>')


# ===================================================== 5. DHANRAKSHAK PIPELINE
def dhanrakshak():
    W, H = 1200, 630
    GOLD, GREEN, BLUE, INDIGO = "#f5b32a", "#34d399", "#38bdf8", "#818cf8"
    o = [svg_open(W, H), defs_common(), card(W, H, "glowGold", "glowGreen"), stars(W, H, 40, seed=71)]
    o.append(label(600, 48, "DHANRAKSHAK — THE VERDICT IS DECIDED ON THE PHONE", 17, "#fde68a", ls="3.5"))
    o.append(label(600, 74, "message · link · screenshot · voice note  →  one engine, one honest answer, in Gujarati", 12.5, "#8093b8", font=MONO))

    # device boundary
    o.append(f'<rect x="58" y="108" width="1084" height="370" rx="22" fill="{GREEN}" fill-opacity=".035" '
             f'stroke="{GREEN}" stroke-opacity=".5" stroke-width="1.6" stroke-dasharray="9 7">'
             f'<animate attributeName="stroke-dashoffset" values="32;0" dur="3.2s" repeatCount="indefinite"/></rect>')
    o.append(label(84, 136, "ON THE DEVICE · NOTHING LEAVES THE PHONE", 11.5, shade(GREEN, 1.15), anchor="start", font=MONO, weight="700", ls="1.2"))

    # inputs
    inputs = [("message / link", BLUE), ("screenshot", BLUE), ("voice note", BLUE), ("practice call", GOLD)]
    in_pts = []
    for i, (name, col) in enumerate(inputs):
        cx, cy = 168, 200 + i * 64
        o.append(f'<g>{float_anim(4, 4.2 + i * 0.4, i * 0.35)}{box(0, 0, 2.4, 2.4, 0.85, col, 16.0, cx, cy - 10, stroke=shade(col, 1.5))}</g>')
        o.append(label(cx + 46, cy - 6, name, 11.5, "#cbd5e1", anchor="start", font=MONO, weight="600"))
        in_pts.append((cx + 40, cy - 10))

    stages = [
        (455, "Read + clean", "OCR · speech-to-text", BLUE, None),
        (676, "Detection engine", "rules + LightGBM", GOLD, "THE VERDICT IS SET HERE"),
        (890, "Explainer", "local Qwen + RBI / NPCI", INDIGO, "only translates"),
        (1058, "Verdict card", "flags · why · what to do", GREEN, None),
    ]
    goy = 302
    pts = []
    body = []
    for i, (cx, name, sub, col, tag) in enumerate(stages):
        w = 3.9 if i < 3 else 3.3
        h = 1.6 if i == 1 else 1.15
        body.append(f'<g>{float_anim(5, 4.4 + i * 0.5, i * 0.4)}'
                    f'{box(0, 0, w, w, h, col, 20.0, cx, goy, stroke=shade(col, 1.5))}</g>')
        tx, ty = iso(w / 2, w / 2, h, 20.0, cx, goy)
        body.append(label(cx, ty - 26, name, 13, shade(col, 1.45), font=MONO, weight="800"))
        body.append(label(cx, 414, sub, 11, "#8c9bbd", font=MONO, weight="500"))
        if tag:
            body.append(label(cx, 434, tag, 10.5, shade(col, 1.3), font=MONO, weight="700", ls="1"))
        pts.append((cx, ty + 18))

    links = []
    for p in in_pts:
        links.append(wire_h(p, (pts[0][0] - 62, pts[0][1]), BLUE, dur=2.6, begin=0.4, dots=1, width=1.3, r=2.6))
    for i in range(len(stages) - 1):
        col = stages[i + 1][3]
        links.append(wire_h((pts[i][0] + 62, pts[i][1]), (pts[i + 1][0] - 62, pts[i + 1][1]), shade(col, 1.3), dur=2.0, begin=i * 0.5))
    o.append("".join(links))
    o.append("".join(body))

    o.append(chip(196, 528, "AIRPLANE MODE OK", GREEN, dur=3.4))
    o.append(chip(430, 528, "VERDICT IN 150 ms", GOLD, dur=4.0))
    o.append(chip(672, 528, "GUJARATI · HINDI · EN", INDIGO, dur=3.7))
    o.append(chip(900, 528, "ZERO CLOUD COST", BLUE, dur=4.3))
    o.append(chip(1076, 528, "ONLINE = MORE", "#94a3b8", dur=4.6))
    o.append(label(600, 592, "the model never decides what is a scam — the detector does, and the model only puts it in her words", 12, "#7c8db5", font=MONO))
    o.append('</svg>')
    return "".join(o)


# ======================================================== 6. DRIFTLOCK MATCHER
def driftlock():
    W, H = 1200, 660
    BLUE, CYAN, GOLD, GREEN = "#3b82f6", "#22d3ee", "#f5b32a", "#4ade80"
    o = [svg_open(W, H), defs_common(), card(W, H, "glowBlue", "glowA"), stars(W, H, 40, seed=97)]
    o.append(label(600, 48, "DRIFTLOCK — FINDING ONE DIE SITE IN A PATTERN THAT REPEATS", 17, "#bfdbfe", ls="3"))
    o.append(label(600, 74, "SEMICON India · Applied Materials PS · classical CV, CPU-only, under a second per pair", 12.5, "#8093b8", font=MONO))

    # ---- wafer field (left)
    s = 21.0
    GW, GD = 13, 9
    gox, goy = 356 - (GW - GD) * KX * s / 2, 196
    o.append(label(356, 128, "SEARCH FIELD · 10x · noisy", 11.5, "#93a4c8", font=MONO, weight="700", ls="1"))

    cells = []
    truth = (7, 3)
    rnd = 12345
    for gx in range(GW):
        if gx % 4 == 3:      # mat separator — incommensurate pitch
            continue
        for gy in range(GD):
            if gy % 5 == 4:
                continue
            rnd = (rnd * 1103515245 + 12345) % 2147483648
            hit = (gx in (truth[0], truth[0] + 1)) and (gy in (truth[1], truth[1] + 1))
            col = GOLD if hit else shade("#46557a", 0.82 + (rnd / 2147483648) * 0.42)
            hh = 1.0 if hit else 0.42
            cells.append((gx, gy, box(gx, gy, 0.72, 0.72, hh, col, s, gox, goy,
                                      stroke=shade(col, 1.5) if hit else None)))
    cells.sort(key=lambda c: c[0] + c[1])
    o.append(f'<g>{"".join(c[2] for c in cells)}</g>')

    # decoy near-equal matches
    for i, (dx, dy) in enumerate([(1, 6), (10, 6), (2, 1)]):
        p = [iso(dx, dy, 0.62, s, gox, goy), iso(dx + 2, dy, 0.62, s, gox, goy),
             iso(dx + 2, dy + 2, 0.62, s, gox, goy), iso(dx, dy + 2, 0.62, s, gox, goy)]
        pd = " ".join(f"{a:.1f},{b:.1f}" for a, b in p)
        o.append(f'<polygon points="{pd}" fill="none" stroke="#f87171" stroke-width="1.4" stroke-dasharray="4 4">'
                 f'<animate attributeName="opacity" values=".75;.12;.75" dur="{4.0 + i*0.6}s" '
                 f'begin="{i*0.5}s" repeatCount="indefinite"/></polygon>')

    # scanning band sweeping along +x
    band = [iso(0, 0, 0.9, s, gox, goy), iso(1.1, 0, 0.9, s, gox, goy),
            iso(1.1, GD, 0.9, s, gox, goy), iso(0, GD, 0.9, s, gox, goy)]
    dx, dy = (GW - 1.1) * KX * s, (GW - 1.1) * KY * s
    bd = " ".join(f"{a:.1f},{b:.1f}" for a, b in band)
    o.append(f'<g opacity=".38"><polygon points="{bd}" fill="{CYAN}" opacity="0.45"/>'
             f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx:.1f} {dy:.1f}" '
             f'dur="4.5s" repeatCount="indefinite"/></g>')

    # crosshair on the true site
    tx, ty = iso(truth[0] + 1, truth[1] + 1, 1.0, s, gox, goy)
    o.append(f'<g filter="url(#soft2)"><circle cx="{tx:.1f}" cy="{ty:.1f}" r="10" fill="none" stroke="{GOLD}" stroke-width="1.8">'
             f'<animate attributeName="r" values="9;20;9" dur="2.6s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="1;0;1" dur="2.6s" repeatCount="indefinite"/></circle>'
             f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="3.4" fill="{GOLD}"/>'
             f'<line x1="{tx-18:.1f}" y1="{ty:.1f}" x2="{tx+18:.1f}" y2="{ty:.1f}" stroke="{GOLD}" stroke-width="1.2" opacity=".8"/>'
             f'<line x1="{tx:.1f}" y1="{ty-14:.1f}" x2="{tx:.1f}" y2="{ty+14:.1f}" stroke="{GOLD}" stroke-width="1.2" opacity=".8"/></g>')
    o.append(f'<line x1="{tx+16:.1f}" y1="{ty-12:.1f}" x2="{tx+56:.1f}" y2="{ty-44:.1f}" stroke="{GOLD}" stroke-width="1.2" opacity=".55"/>')
    o.append(label(tx + 62, ty - 46, "true site · 0.43 px", 11.5, shade(GOLD, 1.25), anchor="start", font=MONO, weight="800"))

    # reference patch inset
    rx, ry = 92, 466
    o.append(f'<rect x="{rx}" y="{ry}" width="112" height="72" rx="8" fill="#0f1730" stroke="{CYAN}" stroke-opacity=".5"/>')
    for i in range(7):
        o.append(f'<rect x="{rx+10+i*14}" y="{ry+12}" width="7" height="48" rx="1.5" fill="#93a4c8" opacity=".55"/>')
    o.append(label(rx + 56, ry + 88, "REFERENCE · 100x", 10.5, "#93a4c8", font=MONO, weight="700"))
    o.append(f'<path d="M {rx+120} {ry+30} C {rx+210} {ry+18} {tx-140:.0f} {ty+120:.0f} {tx-34:.0f} {ty+22:.0f}" fill="none" '
             f'stroke="{CYAN}" stroke-width="1.4" stroke-opacity=".45" stroke-dasharray="5 6">'
             f'<animate attributeName="stroke-dashoffset" values="22;0" dur="1.6s" repeatCount="indefinite"/></path>')
    o.append(label(392, 452, "the layout repeats everywhere —", 11, "#7f8fb3", anchor="start", font=MONO, weight="500"))
    o.append(label(392, 472, "hundreds of near-equal matches;", 11, "#7f8fb3", anchor="start", font=MONO, weight="500"))
    o.append(label(392, 492, "incommensurate mat pitches give", 11, "#7f8fb3", anchor="start", font=MONO, weight="500"))
    o.append(label(392, 512, "the frame its real landmarks", 11, "#7f8fb3", anchor="start", font=MONO, weight="500"))

    # ---- pipeline (right)
    px = 900
    ps = 17.0
    steps = [
        ("clean up", "CLAHE · denoise both", BLUE),
        ("ZNCC sweep", "scale 9.6-10.4 · rot 2 deg", CYAN),
        ("peak set", "every near-equal match", CYAN),
        ("centre rule", "official tie-break", BLUE),
        ("sub-pixel fit", "parabolic refine", BLUE),
        ("(x, y) + PSR", "confidence ships with it", GOLD),
    ]
    o.append(label(px, 128, "ONE PASS · NO GPU · NO WEIGHTS", 11.5, "#93a4c8", font=MONO, weight="700", ls="1"))
    stack = []
    joins = []
    for i, (name, sub, col) in enumerate(steps):
        cy = 176 + i * 72
        stack.append(f'<g>{float_anim(3.5, 4.2 + i * 0.35, i * 0.3)}'
                     f'{box(0, 0, 5.6, 2.6, 1.0, col, ps, px, cy, stroke=shade(col, 1.5))}</g>')
        lx, ly = iso(2.8, 1.3, 1.0, ps, px, cy)
        stack.append(label(lx, ly + 4, name, 11, "#f8fafc", font=MONO, weight="700"))
        stack.append(label(px + 86, ly + 4, sub, 10.5, shade(col, 1.35), anchor="start", font=MONO, weight="500"))
        if i:
            joins.append(wire((lx, cy - 30), (lx, cy - 12), shade(col, 1.3), bend=5, dur=1.5,
                              begin=i * 0.3, dots=1, width=1.5))
    o.append("".join(joins))
    o.append("".join(stack))

    o.append(chip(300, 596, "RANK 0 · 0.43 px", GOLD, dur=3.6))
    o.append(chip(600, 596, "CPU ONLY · NO DEEP LEARNING", GREEN, dur=4.1))
    o.append(chip(930, 596, "PSR FLAGS THE AMBIGUOUS ONES", CYAN, dur=3.8))
    o.append('</svg>')
    return "".join(o)


# ================================================ 7/8. SITE WALLS (browser cards)
def screen_card(cx, cy, w, d, h, color, s, uid, title, sub, tsize=11, ssize=10.5,
                live=False, shine_dur=None, begin=0.0):
    """An isometric 'browser window' slab with a title bar, label and shine sweep."""
    P = lambda x, y, z=h: iso(x, y, z, s, cx, cy)
    top = [P(0, 0), P(w, 0), P(w, d), P(0, d)]
    bar = [P(0, 0), P(w, 0), P(w, 0.62), P(0, 0.62)]
    out = [box(0, 0, w, d, h, color, s, cx, cy, stroke=shade(color, 1.5))]
    out.append(poly(bar, shade(color, 0.55)))
    for k in range(3):
        dx, dy = iso(0.35 + k * 0.42, 0.3, h, s, cx, cy)
        out.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{s*0.055:.1f}" fill="{shade(color, 1.55)}" opacity=".85"/>')
    if shine_dur:
        band = [P(0, 0), P(0.9, 0), P(0.9, d), P(0, d)]
        bd = " ".join(f"{a:.1f},{b:.1f}" for a, b in band)
        td = " ".join(f"{a:.1f},{b:.1f}" for a, b in top)
        dx, dy = (w - 0.9) * KX * s, (w - 0.9) * KY * s
        out.append(f'<clipPath id="clip{uid}"><polygon points="{td}"/></clipPath>'
                   f'<g clip-path="url(#clip{uid})"><polygon points="{bd}" fill="#ffffff" opacity="0.16">'
                   f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx:.1f} {dy:.1f}" '
                   f'dur="{shine_dur}s" begin="{begin}s" repeatCount="indefinite"/></polygon></g>')
    tx, ty = iso(w / 2, d / 2 + 0.25, h, s, cx, cy)
    out.append(label(tx, ty + 4, title, tsize, "#f8fafc", font=MONO, weight="700"))
    by = iso(w / 2, d, 0, s, cx, cy)[1] + 24
    shift = 7 if live else 0
    out.append(label(cx + shift, by, sub, ssize, "#8c9bbd", font=MONO, weight="500"))
    if live:
        lx = cx - len(sub) * ssize * 0.3 - 6
        out.append(f'<circle cx="{lx:.1f}" cy="{by - 4:.1f}" r="3.6" fill="#34d399">'
                   f'<animate attributeName="opacity" values="1;.25;1" dur="2.2s" begin="{begin}s" repeatCount="indefinite"/>'
                   f'<animate attributeName="r" values="3.6;5.4;3.6" dur="2.2s" begin="{begin}s" repeatCount="indefinite"/></circle>')
    return "".join(out)


def clients():
    W, H = 1200, 520
    o = [svg_open(W, H), defs_common(), card(W, H, "glowGreen", "glowA"), stars(W, H, 40, seed=131)]
    o.append(label(600, 50, "LIVE CLIENT WORK — SHIPPED AND IN PRODUCTION", 17, "#bbf7d0", ls="3.5"))
    o.append(label(600, 76, "six businesses running on sites I built · travel, industrial, packaging, D2C", 12.5, "#8093b8", font=MONO))

    sites = [
        ("FindUrTrip", "travel · tours", "#8b5cf6"),
        ("SCE Boiler Spares", "boiler spares", "#22d3ee"),
        ("KBC Global", "private-label brands", "#f472b6"),
        ("BLS Packaging", "bottles · caps", "#38bdf8"),
        ("Shree Har Pkg.", "bag-closing machines", "#a855f7"),
        ("TT Marketing", "weighing systems", "#34d399"),
    ]
    s = 23.0
    for i, (name, sub, col) in enumerate(sites):
        cx = 300 + (i % 3) * 300
        cy = 172 + (i // 3) * 172
        o.append(f'<g>{float_anim(6, 4.4 + (i % 4) * 0.5, i * 0.35)}'
                 f'{screen_card(cx, cy, 4.8, 4.8, 1.2, col, s, f"c{i}", name, sub, tsize=11.5, live=True, shine_dur=5.5 + i * 0.4, begin=i * 0.6)}</g>')

    o.append(chip(340, 480, "REAL BUSINESSES · REAL TRAFFIC", "#34d399", dur=3.6))
    o.append(chip(680, 480, "DESIGN + BUILD + DEPLOY", "#8b5cf6", dur=4.1))
    o.append(chip(960, 480, "OWNED END TO END", "#22d3ee", dur=3.9))
    o.append('</svg>')
    return "".join(o)


def demos():
    W, H = 1200, 600
    o = [svg_open(W, H), defs_common(), card(W, H, "glowA", "glowB"), stars(W, H, 45, seed=173)]
    o.append(label(600, 50, "DEMO SITES — ONE PER INDUSTRY, BUILT TO SHOW CLIENTS", 17, "#e9d5ff", ls="3"))
    o.append(label(600, 76, "each one a full build: layout, copy, responsive pass, deploy", 12.5, "#8093b8", font=MONO))

    demos_list = [
        ("Healthcare", "Sanjeevani", "#f472b6"), ("Dental", "ARIA Studio", "#22d3ee"),
        ("Fitness", "Forge Gym", "#f59e0b"), ("Salon", "Lumiere", "#a855f7"),
        ("Legal", "Mehta + Kapadia", "#38bdf8"), ("Architecture", "Angan", "#8b5cf6"),
        ("Real Estate", "Aavas Realty", "#34d399"), ("Education", "Aakash Intl.", "#6366f1"),
        ("Restaurant", "Angan Kitchen", "#fb7185"), ("Events", "Mehr Events", "#c084fc"),
        ("E-commerce", "Apna Bazar", "#2dd4bf"),
    ]
    s = 18.0
    n = len(demos_list)
    cycle = n * 0.9
    rows = [(4, 168), (4, 316), (3, 464)]
    idx = 0
    for count, cy in rows:
        span = 250 if count == 4 else 250
        x0 = 600 - (count - 1) * span / 2
        for k in range(count):
            name, proj, col = demos_list[idx]
            cx = x0 + k * span
            a = idx / n
            pulse = (f'<animate attributeName="opacity" values="0;0;0.5;0;0" '
                     f'keyTimes="0;{a:.3f};{a+0.028:.3f};{a+0.075:.3f};1" dur="{cycle:.1f}s" repeatCount="indefinite"/>')
            glow = (f'<circle cx="{cx}" cy="{cy+16}" r="86" fill="{col}" opacity="0">{pulse}</circle>')
            o.append(glow)
            o.append(f'<g>{float_anim(5, 4.2 + (idx % 5) * 0.4, idx * 0.28)}'
                     f'{screen_card(cx, cy, 3.7, 3.7, 0.9, col, s, f"d{idx}", name, proj, tsize=10, ssize=9.5, shine_dur=6.0 + idx * 0.3, begin=idx * 0.5)}</g>')
            idx += 1

    o.append(chip(392, 556, "16 INDUSTRIES", "#8b5cf6", dur=3.7))
    o.append(chip(600, 556, "MOBILE-FIRST", "#22d3ee", dur=4.2))
    o.append(chip(818, 556, "SHIPPED LIVE", "#f472b6", dur=3.9))
    o.append('</svg>')
    return "".join(o)


files = {
    "clients-3d.svg": clients(),
    "demos-3d.svg": demos(),
    "dhanrakshak-3d.svg": dhanrakshak(),
    "driftlock-3d.svg": driftlock(),
    "hero-3d.svg": hero(),
    "architecture-3d.svg": architecture(),
    "stack-orbit-3d.svg": orbit(),
    "ship-loop-3d.svg": shiploop(),
}
for n, c in files.items():
    p = os.path.join(OUT, n)
    with open(p, "w") as f:
        f.write(c)
    print(n, len(c), "bytes")
