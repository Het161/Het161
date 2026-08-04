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
<filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="soft2" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
{extra}</defs>'''


def card(w, h):
    return (f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20" fill="url(#bg)" stroke="#26304d" stroke-width="1.5"/>'
            f'<ellipse cx="{w*0.28:.0f}" cy="{h*0.25:.0f}" rx="{w*0.35:.0f}" ry="{h*0.5:.0f}" fill="url(#glowA)"/>'
            f'<ellipse cx="{w*0.78:.0f}" cy="{h*0.8:.0f}" rx="{w*0.3:.0f}" ry="{h*0.45:.0f}" fill="url(#glowB)"/>')


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


files = {
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
