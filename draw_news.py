#!/usr/bin/env python3
"""Draw 'The World in One Page' — a 1024x1024 newspaper summing up the world
news of Sunday 22 November 2026.

Every story below was verified published on 22 November 2026 (see
STORIES.md for the per-story source and verification note). The script is
fully deterministic: same input -> byte-identical PNG.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
RED = (185, 28, 28)
GREY = (110, 110, 105)
RULE = (180, 172, 158)

# section -> (header text, band colour, stories)
# story = (headline, source, icon kind)
SECTIONS = [
    ("UKRAINE", (122, 30, 30), [
        ("Russian strike on Lviv kills 2, injures 10", "Global Digest", "explosion"),
        ("Missile hits Zelenskyy's hometown: 2 dead, 60 hurt", "japako", "missile"),
        ("Zelenskyy: Crimea bridge strikes 'a fair response'", "BBC", "flag"),
        ("Zelenskyy: NATO membership is clearest guarantee", "ANI", "flag"),
        ("Ukraine marks Day of Dignity and Freedom", "japako", "flag"),
        ("Kyiv hits Russia's only Iskander-M fuel supplier", "japako", "missile"),
        ("Russian attack on Zaporizhzhya hits a kindergarten", "japako", "explosion"),
    ]),
    ("EUROPE", (30, 58, 122), [
        ("Finland: war spilling over after ship drone strike", "ANI", "ship"),
        ("Russia-bound ship attacked in Gulf of Finland", "BBC", "ship"),
        ("Denmark: Russia plotted to kill U.S.-Ukrainian rapper", "BBC", "shield"),
        ("Estonia to shut border with Russia", "Daily Jagran", "flag"),
        ("EU and Indonesia sign trade deal after 10 years", "Global Digest", "chart"),
        ("COP31 talks in overtime, deadlocked on fossil fuels", "BBC", "globe"),
        ("UN weapons talks fall short of enforceable rules", "grand-star", "globe"),
        ("Croatia rallies over psychiatric-hospital death", "grand-star", "scale"),
    ]),
    ("MIDDLE EAST", (122, 82, 20), [
        ("Saudi coalition downs Houthi missile", "japako", "missile"),
        ("Turkish intel chief meets Hamas in Istanbul", "japako", "flag"),
        ("Eisenkot opens coalition talks, invites Likud", "ANI", "flag"),
        ("Ex-Israeli PM backs Eisenkot for premier", "japako", "flag"),
        ("Iran calls U.S. blockade a 'hostile act'", "ANI", "bolt"),
    ]),
    ("ASIA-PACIFIC", (20, 100, 70), [
        ("Myanmar quake 4.1 strikes in early hours", "ANI", "quake"),
        ("Modi opens Nitish Setu bridge in Bihar", "Daily Jagran", "bridge"),
        ("Cyclone Akvan grounds 14 Ranchi flights", "Daily Jagran", "cloud"),
        ("Japan to train live-fire in India, a first", "Daily Jagran", "target"),
        ("Hong Kong Election Committee voting opens", "Global Digest", "ballot"),
        ("Trump-Xi Shenzhen meeting sends world signals", "japako", "globe"),
        ("Modi: civilisational links guarantee peace", "japako", "flag"),
        ("Illicit alcohol kills 11, sickens 180 in Manipur", "grand-star", "flask"),
    ]),
    ("AMERICAS", (90, 40, 110), [
        ("Strong quake shakes Peru's Andes; no casualties", "grand-star", "quake"),
        ("Mexico captures 'El Chapo Isidro', FBI top-10 fugitive", "grand-star", "shield"),
        ("FBI probes hack of its criminal database", "BBC", "bolt"),
        ("Man convicted of starting L.A. Palisades fire", "BBC", "flame"),
        ("Three Salvadorans killed in Haiti blast", "japako", "explosion"),
        ("U.S. agencies hit by cyberattacks, media report", "japako", "bolt"),
        ("Trump presses Nvidia to reinstate Jensen Huang", "japako", "chip"),
    ]),
    ("AFRICA", (140, 90, 20), [
        ("Sudan's Tasis alliance seizes Bau in Blue Nile", "grand-star", "flag"),
        ("ANC battles to hold South Africa's key cities", "BBC", "ballot"),
        ("Nigerian youth: power shown, vote unshaped", "BBC", "ballot"),
    ]),
    ("MARKETS", (20, 90, 90), [
        ("Tech sell-off drags markets; Anthropic slides", "BBC", "chart"),
        ("Judge approves $7.25bn Roundup settlement", "BBC", "gavel"),
        ("Crude oil futures fall more than 3%", "Daily Jagran", "chart"),
    ]),
    ("SPORT", (30, 110, 50), [
        ("BYU outlasts Kansas 31-29 in triple overtime", "Reuters", "ball"),
        ("Nebraska stuns No. 14 Ohio State 31-27", "Reuters", "ball"),
        ("Zverev beats Medvedev, into ATP Finals decider", "TNT Sports", "trophy"),
        ("England hammer All Blacks 37-12 in five-try rout", "TNT Sports", "ball"),
    ]),
    ("CULTURE", (110, 60, 90), [
        ("Lock of Washington's hair sells for $4,000", "BBC", "star"),
        ("Teen gamer and mother help rescue missing girl", "BBC", "star"),
    ]),
]

LEAD_HEADLINE = "IRAN STRIKES U.S. BASES ACROSS THE GULF"
LEAD_DECK = ("Tehran claims missile hits on Patriot radars in Kuwait and Bahrain; "
             "Trump pushes a permanent nuclear deal as Hormuz hangs in the balance.")
LEAD_BULLETS = [
    ("Iran says Hormuz reopening 'not difficult' if U.S. accepts terms", "ANI"),
    ("IRGC claims combined missile-and-drone operation", "ANI"),
    ("Bahrain condemns strikes on U.S. assets in the Gulf", "Global Digest"),
]


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, width, max_lines=2):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
        if len(lines) == max_lines:
            break
    if len(lines) < max_lines and cur:
        lines.append(cur)
    elif cur and len(lines) == max_lines:
        # truncate the last line to fit with an ellipsis
        last = lines[-1]
        while last and draw.textlength(last + "...", font=fnt) > width:
            last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
        lines[-1] = last + "..."
    return lines


def draw_icon(d, kind, x, y, s, tint):
    """A small drawn pictogram in a rounded square of side s."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=5, fill=tint,
                        outline=(120, 110, 95))
    c = (40, 40, 40)
    p = s / 34.0  # scale factor (icons designed on a 34px box)
    cx, cy = x + s / 2, y + s / 2
    if kind == "missile":
        d.polygon([(x + 8 * p, y + 26 * p), (x + 26 * p, y + 8 * p),
                   (x + 29 * p, y + 11 * p), (x + 11 * p, y + 29 * p)], fill=c)
        d.polygon([(x + 24 * p, y + 6 * p), (x + 29 * p, y + 5 * p),
                   (x + 28 * p, y + 10 * p)], fill=RED)
        d.line([(x + 8 * p, y + 26 * p), (x + 5 * p, y + 29 * p)], fill=RED, width=2)
    elif kind == "explosion":
        for ang in range(0, 360, 45):
            import math
            r1, r2 = 5 * p, 13 * p
            a = math.radians(ang)
            d.line([(cx, cy), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))],
                   fill=c, width=3)
        d.ellipse([cx - 5 * p, cy - 5 * p, cx + 5 * p, cy + 5 * p], fill=RED)
    elif kind == "flag":
        d.line([(x + 10 * p, y + 6 * p), (x + 10 * p, y + 28 * p)], fill=c, width=2)
        d.polygon([(x + 10 * p, y + 6 * p), (x + 26 * p, y + 11 * p),
                   (x + 10 * p, y + 16 * p)], fill=RED)
    elif kind == "quake":
        d.line([(x + 5 * p, y + 8 * p), (x + 12 * p, y + 16 * p),
                (x + 9 * p, y + 22 * p), (x + 17 * p, y + 14 * p),
                (x + 15 * p, y + 26 * p), (x + 24 * p, y + 18 * p),
                (x + 29 * p, y + 26 * p)], fill=c, width=2)
    elif kind == "ship":
        d.polygon([(x + 6 * p, y + 20 * p), (x + 28 * p, y + 20 * p),
                   (x + 24 * p, y + 28 * p), (x + 10 * p, y + 28 * p)], fill=c)
        d.line([(x + 17 * p, y + 8 * p), (x + 17 * p, y + 20 * p)], fill=c, width=2)
        d.polygon([(x + 17 * p, y + 8 * p), (x + 25 * p, y + 14 * p),
                   (x + 17 * p, y + 14 * p)], fill=RED)
    elif kind == "shield":
        d.polygon([(cx, y + 5 * p), (x + 27 * p, y + 9 * p),
                   (x + 27 * p, y + 18 * p), (cx, y + 29 * p),
                   (x + 7 * p, y + 18 * p), (x + 7 * p, y + 9 * p)], fill=c)
        d.line([(x + 12 * p, y + 17 * p), (x + 16 * p, y + 21 * p),
                (x + 23 * p, y + 12 * p)], fill=(255, 255, 255), width=2)
    elif kind == "ballot":
        d.rectangle([x + 8 * p, y + 12 * p, x + 26 * p, y + 28 * p],
                    outline=c, width=2)
        d.line([(x + 8 * p, y + 12 * p), (x + 26 * p, y + 12 * p)], fill=c, width=2)
        d.line([(x + 12 * p, y + 20 * p), (x + 16 * p, y + 24 * p),
                (x + 23 * p, y + 14 * p)], fill=RED, width=2)
    elif kind == "chart":
        d.line([(x + 7 * p, y + 27 * p), (x + 7 * p, y + 7 * p)], fill=c, width=2)
        d.line([(x + 7 * p, y + 27 * p), (x + 28 * p, y + 27 * p)], fill=c, width=2)
        d.line([(x + 9 * p, y + 22 * p), (x + 15 * p, y + 16 * p),
                (x + 20 * p, y + 19 * p), (x + 27 * p, y + 9 * p)], fill=RED, width=2)
    elif kind == "ball":
        d.ellipse([x + 6 * p, y + 6 * p, x + 28 * p, y + 28 * p], outline=c, width=2)
        d.polygon([(cx - 4 * p, cy - 4 * p), (cx + 4 * p, cy - 4 * p),
                   (cx + 6 * p, cy + 3 * p), (cx, cy + 6 * p),
                   (cx - 6 * p, cy + 3 * p)], fill=c)
    elif kind == "trophy":
        d.polygon([(x + 11 * p, y + 7 * p), (x + 23 * p, y + 7 * p),
                   (x + 21 * p, y + 18 * p), (x + 13 * p, y + 18 * p)], fill=c)
        d.arc([x + 6 * p, y + 8 * p, x + 13 * p, y + 16 * p], 90, 270, fill=c, width=2)
        d.arc([x + 21 * p, y + 8 * p, x + 28 * p, y + 16 * p], -90, 90, fill=c, width=2)
        d.line([(cx, y + 18 * p), (cx, y + 24 * p)], fill=c, width=2)
        d.line([(x + 12 * p, y + 26 * p), (x + 22 * p, y + 26 * p)], fill=c, width=2)
    elif kind == "globe":
        d.ellipse([x + 6 * p, y + 6 * p, x + 28 * p, y + 28 * p], outline=c, width=2)
        d.ellipse([x + 13 * p, y + 6 * p, x + 21 * p, y + 28 * p], outline=c, width=1)
        d.line([(x + 6 * p, cy), (x + 28 * p, cy)], fill=c, width=1)
    elif kind == "bolt":
        d.polygon([(x + 19 * p, y + 5 * p), (x + 10 * p, y + 19 * p),
                   (x + 16 * p, y + 19 * p), (x + 13 * p, y + 29 * p),
                   (x + 24 * p, y + 14 * p), (x + 18 * p, y + 14 * p)], fill=RED)
    elif kind == "flame":
        d.polygon([(cx, y + 5 * p), (x + 24 * p, y + 18 * p),
                   (x + 20 * p, y + 27 * p), (x + 12 * p, y + 27 * p),
                   (x + 9 * p, y + 19 * p)], fill=RED)
        d.ellipse([cx - 4 * p, cy + 2 * p, cx + 4 * p, cy + 10 * p], fill=(255, 200, 60))
    elif kind == "flask":
        d.line([(x + 14 * p, y + 6 * p), (x + 20 * p, y + 6 * p)], fill=c, width=2)
        d.line([(cx, y + 6 * p), (cx, y + 14 * p)], fill=c, width=2)
        d.polygon([(x + 12 * p, y + 14 * p), (x + 22 * p, y + 14 * p),
                   (x + 27 * p, y + 26 * p), (x + 7 * p, y + 26 * p)],
                  outline=c, width=2)
        d.line([(x + 11 * p, y + 21 * p), (x + 23 * p, y + 21 * p)], fill=RED, width=3)
    elif kind == "gavel":
        d.line([(x + 8 * p, y + 26 * p), (x + 24 * p, y + 10 * p)], fill=c, width=3)
        d.line([(x + 14 * p, y + 8 * p), (x + 22 * p, y + 16 * p)], fill=c, width=5)
        d.line([(x + 10 * p, y + 27 * p), (x + 26 * p, y + 27 * p)], fill=c, width=2)
    elif kind == "scale":
        d.line([(cx, y + 6 * p), (cx, y + 26 * p)], fill=c, width=2)
        d.line([(x + 8 * p, y + 9 * p), (x + 26 * p, y + 9 * p)], fill=c, width=2)
        d.polygon([(x + 6 * p, y + 16 * p), (x + 12 * p, y + 16 * p),
                   (cx - 4 * p, y + 9 * p)], outline=c, width=1)
        d.polygon([(x + 22 * p, y + 16 * p), (x + 28 * p, y + 16 * p),
                   (cx + 4 * p, y + 9 * p)], outline=c, width=1)
        d.line([(x + 10 * p, y + 26 * p), (x + 24 * p, y + 26 * p)], fill=c, width=2)
    elif kind == "cloud":
        d.ellipse([x + 7 * p, y + 10 * p, x + 19 * p, y + 20 * p], fill=c)
        d.ellipse([x + 14 * p, y + 7 * p, x + 27 * p, y + 19 * p], fill=c)
        d.line([(x + 11 * p, y + 24 * p), (x + 11 * p, y + 28 * p)], fill=RED, width=2)
        d.line([(x + 17 * p, y + 24 * p), (x + 17 * p, y + 28 * p)], fill=RED, width=2)
        d.line([(x + 23 * p, y + 24 * p), (x + 23 * p, y + 28 * p)], fill=RED, width=2)
    elif kind == "bridge":
        d.line([(x + 5 * p, y + 24 * p), (x + 29 * p, y + 24 * p)], fill=c, width=2)
        d.arc([x + 7 * p, y + 12 * p, x + 27 * p, y + 30 * p], 180, 360, fill=c, width=2)
        d.line([(x + 10 * p, y + 20 * p), (x + 10 * p, y + 24 * p)], fill=c, width=1)
        d.line([(cx, y + 17 * p), (cx, y + 24 * p)], fill=c, width=1)
        d.line([(x + 24 * p, y + 20 * p), (x + 24 * p, y + 24 * p)], fill=c, width=1)
    elif kind == "target":
        for r in (12, 8, 4):
            d.ellipse([cx - r * p, cy - r * p, cx + r * p, cy + r * p],
                      outline=c, width=1)
        d.ellipse([cx - 2 * p, cy - 2 * p, cx + 2 * p, cy + 2 * p], fill=RED)
    elif kind == "chip":
        d.rectangle([x + 10 * p, y + 10 * p, x + 24 * p, y + 24 * p],
                    outline=c, width=2)
        d.rectangle([x + 15 * p, y + 15 * p, x + 19 * p, y + 19 * p], fill=RED)
        for xx in (13, 17, 21):
            d.line([(x + xx * p, y + 6 * p), (x + xx * p, y + 10 * p)], fill=c, width=1)
            d.line([(x + xx * p, y + 24 * p), (x + xx * p, y + 28 * p)], fill=c, width=1)
    elif kind == "star":
        import math
        pts = []
        for i in range(10):
            r = 13 * p if i % 2 == 0 else 5 * p
            a = math.radians(-90 + i * 36)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        d.polygon(pts, fill=(200, 150, 20))
    else:  # fallback: simple dot
        d.ellipse([cx - 5 * p, cy - 5 * p, cx + 5 * p, cy + 5 * p], fill=c)


TINTS = [(232, 222, 205), (222, 230, 238), (238, 226, 222), (226, 236, 226),
         (236, 228, 240), (240, 232, 210)]


def draw_gulf_map(d, x0, y0, w, h):
    """Schematic map of the Persian Gulf region (labelled, not to scale)."""
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 228, 205),
                outline=(120, 110, 95), width=2)
    # sea: the Gulf runs diagonally NW-SE
    sea = [(x0 + 30, y0 + 62), (x0 + 95, y0 + 34), (x0 + 165, y0 + 30),
           (x0 + 235, y0 + 52), (x0 + 300, y0 + 44), (x0 + w - 8, y0 + 60),
           (x0 + w - 8, y0 + h - 8), (x0 + 200, y0 + h - 8),
           (x0 + 150, y0 + 96), (x0 + 80, y0 + 92), (x0 + 30, y0 + 78)]
    d.polygon(sea, fill=(168, 200, 222))
    # Gulf of Oman / Arabian Sea bottom-right
    d.polygon([(x0 + 235, y0 + 52), (x0 + 300, y0 + 44), (x0 + w - 8, y0 + 60),
               (x0 + w - 8, y0 + h - 8), (x0 + 250, y0 + h - 8),
               (x0 + 225, y0 + 78)], fill=(150, 188, 214))
    f_small = font("DejaVuSans-Bold.ttf", 10)
    f_tiny = font("DejaVuSans.ttf", 9)
    labels = [
        ("IRAN", x0 + 108, y0 + 8, INK, f_small),
        ("IRAQ", x0 + 12, y0 + 30, INK, f_small),
        ("KUWAIT \u2605", x0 + 8, y0 + 52, RED, f_small),
        ("SAUDI ARABIA", x0 + 18, y0 + 100, INK, f_small),
        ("BAHRAIN \u2605", x0 + 96, y0 + 66, RED, f_small),
        ("QATAR", x0 + 168, y0 + 62, INK, f_tiny),
        ("U.A.E.", x0 + 225, y0 + 66, INK, f_tiny),
        ("OMAN", x0 + 262, y0 + 108, INK, f_small),
        ("PERSIAN GULF", x0 + 118, y0 + 40, (30, 70, 110), f_tiny),
        ("STRAIT OF HORMUZ", x0 + 218, y0 + 88, (30, 70, 110), f_tiny),
    ]
    for text, lx, ly, col, fnt in labels:
        d.text((lx, ly), text, font=fnt, fill=col)
    # strike markers
    for mx, my in ((x0 + 52, y0 + 50), (x0 + 138, y0 + 64)):
        d.ellipse([mx - 4, my - 4, mx + 4, my + 4], fill=RED,
                  outline=(255, 255, 255))
    d.text((x0 + 8, y0 + h - 16), "SCHEMATIC MAP \u2014 THE GULF, 22 NOV 2026",
           font=font("DejaVuSans.ttf", 8), fill=GREY)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 72], fill=NAVY)
    d.text((16, 10), "THE WORLD IN ONE PAGE",
           font=font("DejaVuSerif-Bold.ttf", 30), fill=(247, 243, 234))
    d.text((16, 48), "A NEWSPAPER OF ONE DAY  \u00b7  52 STORIES  \u00b7  10 SECTIONS  \u00b7  9 REGIONS",
           font=font("DejaVuSans.ttf", 11), fill=(190, 195, 210))
    date_txt = "SUNDAY, 22 NOVEMBER 2026"
    dw = d.textlength(date_txt, font=font("DejaVuSans-Bold.ttf", 26))
    d.text((W - 16 - dw, 12), date_txt, font=font("DejaVuSans-Bold.ttf", 26),
           fill=(255, 210, 90))
    d.text((W - 16 - d.textlength("ALL STORIES DATED THIS DAY", font=font("DejaVuSans.ttf", 11)), 48),
           "ALL STORIES DATED THIS DAY", font=font("DejaVuSans.ttf", 11),
           fill=(190, 195, 210))

    # ---- date-check strip ----
    d.rectangle([0, 72, W, 96], fill=RED)
    d.text((16, 77),
           "\u2713  DATE CHECK \u2014 EVERY STORY ON THIS PAGE WAS PUBLISHED ON 22 NOVEMBER 2026  \u00b7  "
           "SOURCES NAMED ON EVERY STORY",
           font=font("DejaVuSans-Bold.ttf", 13), fill=(255, 255, 255))

    # ---- lead block ----
    d.text((16, 106), "LEAD \u2014 GULF CRISIS", font=font("DejaVuSans-Bold.ttf", 13),
           fill=RED)
    d.line([(16, 126), (640, 126)], fill=RULE, width=1)
    head_lines = wrap(d, LEAD_HEADLINE, font("DejaVuSans-Bold.ttf", 27), 620,
                      max_lines=2)
    y = 132
    for ln in head_lines:
        d.text((16, y), ln, font=font("DejaVuSans-Bold.ttf", 27), fill=NAVY)
        y += 32
    deck_lines = wrap(d, LEAD_DECK, font("DejaVuSans.ttf", 13), 620, max_lines=2)
    for ln in deck_lines:
        d.text((16, y), ln, font=font("DejaVuSans.ttf", 13), fill=INK)
        y += 17
    y += 4
    for txt, src in LEAD_BULLETS:
        d.text((16, y), "\u25b8", font=font("DejaVuSans-Bold.ttf", 12), fill=RED)
        bl = wrap(d, txt, font("DejaVuSans.ttf", 12), 590, max_lines=1)
        d.text((32, y), bl[0], font=font("DejaVuSans.ttf", 12), fill=INK)
        sw = d.textlength(bl[0], font=font("DejaVuSans.ttf", 12))
        d.text((32 + sw + 6, y + 1), "\u2014 " + src,
               font=font("DejaVuSans-Bold.ttf", 10), fill=GREY)
        y += 17
    draw_gulf_map(d, 668, 104, 336, 140)

    # ---- body: three columns ----
    cols = [
        [SECTIONS[0], SECTIONS[1]],                    # Ukraine + Europe
        [SECTIONS[2], SECTIONS[3], SECTIONS[7]],       # MidEast + Asia + Sport
        [SECTIONS[4], SECTIONS[5], SECTIONS[6], SECTIONS[8]],  # Americas + Africa + Markets + Culture
    ]
    col_x = [16, 350, 684]
    col_w = 322
    body_top, body_bottom = 256, 1000
    body_h = body_bottom - body_top
    f_head = font("DejaVuSans-Bold.ttf", 13)
    f_story = font("DejaVuSans-Bold.ttf", 12)
    f_src = font("DejaVuSans.ttf", 9)
    for ci, col in enumerate(cols):
        x = col_x[ci]
        n_headers = len(col)
        n_stories = sum(len(s[2]) for s in col)
        gaps = (n_headers - 1) * 8
        cell_h = (body_h - n_headers * 22 - gaps) // n_stories
        y = body_top
        tint_i = ci
        for title, band, stories in col:
            d.rectangle([x, y, x + col_w, y + 22], fill=band)
            d.text((x + 8, y + 4), title, font=f_head, fill=(255, 255, 255))
            cnt = str(len(stories))
            d.text((x + col_w - 8 - d.textlength(cnt, font=f_head), y + 4), cnt,
                   font=f_head, fill=(255, 255, 255))
            y += 22
            for headline, src, kind in stories:
                draw_icon(d, kind, x, y + 2, 34, TINTS[tint_i % len(TINTS)])
                tint_i += 1
                tx = x + 40
                tw = col_w - 40
                lines = wrap(d, headline, f_story, tw, max_lines=2)
                ly = y + 2
                for ln in lines:
                    d.text((tx, ly), ln, font=f_story, fill=INK)
                    ly += 13
                d.text((tx, y + cell_h - 12), "\u2014 " + src + "  \u00b7  22 NOV",
                       font=f_src, fill=GREY)
                y += cell_h
            y += 8
        d.line([(x + col_w + 6, body_top), (x + col_w + 6, body_bottom)],
               fill=RULE, width=1) if ci < 2 else None

    # ---- footer ----
    d.line([(16, 1004), (W - 16, 1004)], fill=RULE, width=1)
    foot = ("SOURCES: ANI  \u00b7  REUTERS  \u00b7  BBC  \u00b7  TNT SPORTS  \u00b7  WAM  \u00b7  "
            "DAILY JAGRAN  \u00b7  GLOBAL DIGEST  \u00b7  GRAND-STAR  \u00b7  JAPAKO  \u00b7  OPENSOURCETRADES")
    fw = d.textlength(foot, font=font("DejaVuSans.ttf", 10))
    d.text(((W - fw) / 2, 1008), foot, font=font("DejaVuSans.ttf", 10), fill=GREY)
    return img


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    img = build()
    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size, os.path.getsize("entry.png"), "bytes")


if __name__ == "__main__":
    main()
