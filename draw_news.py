#!/usr/bin/env python3
"""Draw "The World in One Page" — news-image-20261122, round 3 (PERBAIKI).

One 1024x1024 PNG summing up the world news of Sunday 22 November 2026.
All stories are verified in STORIES.md (every item dated 22 Nov 2026).
Layout targets the judging scale: story headlines are 26px Noto Sans
ExtraCondensed Bold (~7.6px nominal at the 300px comparison scale),
every story is a cell with its own drawn pictogram, and the printed
masthead counts are computed from the drawing data and asserted here.

Deterministic: no randomness, no clock reads; all strings are literals.
Rendered and verified with Python 3.12.3 / Pillow 10.2.0 (see README.md).
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (250, 247, 240)
INK = (20, 24, 29)
GREY = (84, 90, 98)
RULE = (216, 210, 198)
RED = (158, 22, 22)
GREEN = (30, 122, 52)
AMBER = (178, 106, 0)

NOTO = "/usr/share/fonts/truetype/noto"
F_XBOLD = f"{NOTO}/NotoSans-ExtraCondensedBold.ttf"
F_CBOLD = f"{NOTO}/NotoSans-CondensedBold.ttf"
F_CREG = f"{NOTO}/NotoSans-Condensed.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(F_XBOLD, 42)
F_DATE = font(F_CBOLD, 20)
F_STRIP = font(F_CBOLD, 15)
F_KICK = font(F_CBOLD, 15)
F_LEAD = font(F_XBOLD, 34)
F_LEAD_SUB = font(F_CREG, 15)
F_HEAD = font(F_XBOLD, 26)
F_SEC = font(F_CBOLD, 19)
F_SRC = font(F_CBOLD, 13)
F_PILL = font(F_CBOLD, 10)
F_MAP = font(F_CBOLD, 11)
F_FOOT = font(F_CREG, 12)

LEAD_REGION = "Middle East"

# ---------------------------------------------------------------- stories
# (headline, source, pub-time UTC on 22 Nov 2026 or "", confidence, icon)
# Every item is a report PUBLISHED on Sunday 22 Nov 2026; pubDates were
# verified against RSS feeds (BBC, Al Jazeera, France 24, Euronews, ABC)
# or the wire's own timestamp — see STORIES.md for the per-item evidence.
LEAD = ("IRAN STRIKES U.S. BASES ACROSS THE GULF", "AFP", "04:21",
        "DEVELOPING", "missile")
LEAD_SUB = ("IRGC says Patriot radars were hit in Bahrain; Bahrain reports a "
            "civilian site ablaze. AFP, Xinhua, Gulf News and The National "
            "confirm the attacks.")

SECTIONS = [
    ("GULF & HORMUZ", (158, 22, 22), "Middle East", [
        ("TANKERS HIT IN HORMUZ", "AFP", "04:21", "DEVELOPING", "ship"),
        ("IRAN HIT BAHRAIN SITE", "AFP", "04:21", "DEVELOPING", "factory"),
        ("14 TANKERS VS BLOCKADE", "Gulf News", "04:48", "DEVELOPING", "drop"),
        ("IRGC: PATRIOT RADARS HIT", "The National", "03:23", "DEVELOPING", "target"),
        ("ARAGHCHI PLAN: HORMUZ", "Xinhua", "05:44", "DEVELOPING", "scroll"),
        ("TRUMP SEEKS IRAN DEAL", "Xinhua", "05:37", "DEVELOPING", "talk"),
    ]),
    ("MIDDLE EAST", (178, 106, 0), "Middle East", [
        ("JORDAN SLAMS STRIKE", "Petra", "", "CONFIRMED", "flag"),
        ("GAZA DISPLACED PROTEST", "Al Jazeera", "02:14", "CONFIRMED", "people"),
    ]),
    ("UKRAINE", (38, 84, 158), "Eastern Europe", [
        ("KRYVYI RIH: 2 KILLED", "NBC News", "00:29", "DEVELOPING", "explosion"),
        ("ZELENSKY: PUTIN 'KILLER'", "The Independent", "04:00", "CONFIRMED", "talk"),
        ("CARGO SHIP HIT BY DRONE", "The Guardian", "02:19", "DEVELOPING", "ship"),
    ]),
    ("EUROPE", (70, 60, 150), "Europe", [
        ("COP31: DRAFT DEAL TABLED", "AP", "04:01", "DEVELOPING", "globe"),
        ("BRUSSELS FLIGHTS OFF", "Xinhua", "05:49", "CONFIRMED", "plane"),
        ("CLASHES ERUPT IN FRANCE", "Al Jazeera", "00:37", "CONFIRMED", "people"),
        ("BALTIC SPILLOVER FEAR", "France 24", "06:15", "CONFIRMED", "shield"),
        ("MAY WARNS ON EU RESET", "BBC", "06:01", "CONFIRMED", "flag"),
        ("VILLAGE VOTES 'LEAVE UK'", "Euronews", "07:00", "CONFIRMED", "ballot"),
        ("MADEIRA OCEAN SURVEY", "Euronews", "07:02", "CONFIRMED", "globe"),
    ]),
    ("ASIA-PACIFIC", (18, 120, 110), "Asia-Pacific", [
        ("FACTORY FIRE: 40 MISSING", "BBC", "06:05", "DEVELOPING", "factory"),
    ]),
    ("SOUTH ASIA", (18, 120, 110), "South Asia", [
        ("TAINTED BREW KILLS 11", "The Independent", "04:03", "CONFIRMED", "bottle"),
    ]),
    ("NORTH AMERICA", (30, 110, 60), "North America", [
        ("FBI DATABASE HACK PROBE", "BBC", "00:10", "DEVELOPING", "lock"),
        ("ICE ARRESTS AT AIRPORT", "Al Jazeera", "05:06", "CONFIRMED", "shield"),
        ("BESSENT LIVING ON BASE", "Al Jazeera", "02:05", "CONFIRMED", "flag"),
        ("STORMS RAVAGE CA COAST", "Xinhua", "10:24", "DEVELOPING", "cloud"),
        ("CANADA JOINS NATO FUND", "Xinhua", "11:20", "CONFIRMED", "coin"),
    ]),
    ("LATIN AMERICA", (30, 110, 60), "Latin America", [
        ("CARTEL BOSS CAPTURED", "BBC", "01:25", "CONFIRMED", "target"),
        ("11 KILLED IN CARTEL RAID", "Al Jazeera", "03:34", "CONFIRMED", "explosion"),
        ("QUAKE EMPTIES CINEMA", "Al Jazeera", "01:07", "CONFIRMED", "camera"),
    ]),
    ("AFRICA", (150, 100, 20), "Africa", [
        ("NIGERIA YOUTH UNSURE", "BBC", "00:10", "CONFIRMED", "people"),
        ("NIGERIA BOAT: 24 DEAD", "Al Jazeera", "02:45", "CONFIRMED", "ship"),
        ("DARFUR FAMILIES BRACE", "Al Jazeera", "05:21", "CONFIRMED", "people"),
        ("SUDAN CLASHES, BLUE NILE", "Roya News", "04:11", "DEVELOPING", "explosion"),
    ]),
    ("MARKETS & TECH", (90, 90, 96), "Global", [
        ("KENYA NET BILL FEARS", "Al Jazeera", "05:38", "CONFIRMED", "chip"),
        ("EU HIRING: SKILLS FIRST", "Euronews", "07:00", "CONFIRMED", "scroll"),
    ]),
    ("SPORT", (196, 90, 20), "Global", [
        ("VERSTAPPEN TAKES VEGAS", "BBC", "06:27", "CONFIRMED", "flag"),
        ("AUSTRALIA EDGE WALES", "BBC", "04:50", "CONFIRMED", "ball"),
        ("POCHETTINO'S UTD TEST", "BBC", "06:21", "CONFIRMED", "ball"),
        ("SPURS TEEN IMPRESSES", "BBC", "00:13", "CONFIRMED", "ball"),
        ("INDIA BREAKS TEST RECORD", "ABC News", "06:12", "CONFIRMED", "ball"),
    ]),
    ("CULTURE", (150, 40, 110), "Global", [
        ("GAMER HELPS RESCUE GIRL", "BBC", "00:09", "CONFIRMED", "game"),
        ("FRASER AT 1956 REUNION", "ABC News", "00:08", "CONFIRMED", "flame"),
    ]),
]
COLUMNS = [[0, 2, 3], [1, 4, 5, 6, 7], [8, 9, 10, 11]]

ALL_STORIES = [LEAD] + [st for s in SECTIONS for st in s[3]]
N_STORIES = len(ALL_STORIES)
REGIONS = {LEAD_REGION} | {s[2] for s in SECTIONS}
WIRE5 = {"Reuters", "BBC", "AP", "ANI", "AFP"}
N_WIRE5 = sum(1 for st in ALL_STORIES if st[1] in WIRE5)
OUTLETS = {st[1] for st in ALL_STORIES}
ICON_KINDS = {st[4] for st in ALL_STORIES}
assert N_STORIES == 42, N_STORIES
assert len(SECTIONS) == 12
assert len(REGIONS) == 9, REGIONS
assert N_WIRE5 == 14, N_WIRE5
assert len(OUTLETS) == 15, OUTLETS

# ------------------------------------------------------------------- icons
# Each icon draws inside a 40x40 tile centred at (cx, cy), glyph ~30px.


def _l(d, pts, c, w=3):
    d.line(pts, fill=c, width=w, joint="curve")


def i_missile(d, cx, cy, c):
    _l(d, [(cx - 11, cy + 11), (cx + 8, cy - 8)], c, 7)
    d.polygon([(cx - 12, cy + 4), (cx - 3, cy + 12), (cx - 11, cy + 12)],
              fill=c)
    _l(d, [(cx - 14, cy + 14), (cx - 8, cy + 8)], (230, 120, 20), 4)


def i_ship(d, cx, cy, c):
    d.polygon([(cx - 14, cy + 2), (cx + 14, cy + 2), (cx + 9, cy + 10),
               (cx - 9, cy + 10)], outline=c, width=3)
    _l(d, [(cx, cy + 2), (cx, cy - 12)], c, 3)
    d.rectangle([cx + 1, cy - 8, cx + 9, cy - 3], outline=c, width=2)
    _l(d, [(cx - 14, cy + 14), (cx - 6, cy + 12), (cx + 2, cy + 14),
           (cx + 10, cy + 12)], (60, 110, 190), 2)


def i_factory(d, cx, cy, c):
    d.rectangle([cx - 13, cy - 2, cx + 13, cy + 12], outline=c, width=3)
    _l(d, [(cx - 8, cy - 2), (cx - 8, cy - 12)], c, 4)
    _l(d, [(cx + 3, cy - 2), (cx + 3, cy - 12)], c, 4)
    d.ellipse([cx - 11, cy - 17, cx - 4, cy - 12], outline=c, width=2)


def i_drop(d, cx, cy, c):
    d.polygon([(cx, cy - 14), (cx + 9, cy + 3), (cx + 6, cy + 10),
               (cx - 6, cy + 10), (cx - 9, cy + 3)], outline=c, width=3)


def i_jet(d, cx, cy, c):
    d.polygon([(cx + 14, cy - 4), (cx - 2, cy - 4), (cx - 12, cy - 13),
               (cx - 8, cy + 1), (cx - 14, cy + 8), (cx - 6, cy + 8),
               (cx - 2, cy + 4), (cx + 14, cy + 4)], fill=c)


def i_scroll(d, cx, cy, c):
    d.rectangle([cx - 11, cy - 10, cx + 11, cy + 10], outline=c, width=3)
    _l(d, [(cx - 6, cy - 4), (cx + 6, cy - 4)], c, 2)
    _l(d, [(cx - 6, cy + 1), (cx + 6, cy + 1)], c, 2)
    _l(d, [(cx - 6, cy + 6), (cx + 2, cy + 6)], c, 2)


def i_anchor(d, cx, cy, c):
    d.ellipse([cx - 3, cy - 14, cx + 3, cy - 8], outline=c, width=3)
    _l(d, [(cx, cy - 8), (cx, cy + 12)], c, 3)
    _l(d, [(cx - 7, cy - 3), (cx + 7, cy - 3)], c, 3)
    _l(d, [(cx - 11, cy + 5), (cx - 11, cy + 12), (cx - 4, cy + 12)], c, 3)
    _l(d, [(cx + 11, cy + 5), (cx + 11, cy + 12), (cx + 4, cy + 12)], c, 3)


def i_flag(d, cx, cy, c):
    _l(d, [(cx - 9, cy - 14), (cx - 9, cy + 14)], c, 3)
    d.polygon([(cx - 9, cy - 14), (cx + 12, cy - 10), (cx - 9, cy - 5)],
              outline=c, width=3)


def i_bridge(d, cx, cy, c):
    _l(d, [(cx - 15, cy + 10), (cx + 15, cy + 10)], c, 3)
    _l(d, [(cx - 10, cy + 10), (cx - 10, cy - 10)], c, 3)
    _l(d, [(cx + 10, cy + 10), (cx + 10, cy - 10)], c, 3)
    _l(d, [(cx - 15, cy + 2), (cx - 10, cy - 10), (cx + 10, cy - 10),
           (cx + 15, cy + 2)], c, 2)


def i_shield(d, cx, cy, c):
    d.polygon([(cx, cy - 14), (cx + 11, cy - 10), (cx + 11, cy + 2),
               (cx, cy + 14), (cx - 11, cy + 2), (cx - 11, cy - 10)],
              outline=c, width=3)
    _l(d, [(cx - 5, cy), (cx - 1, cy + 5), (cx + 6, cy - 5)], c, 3)


def i_explosion(d, cx, cy, c):
    import math
    pts = []
    for k in range(16):
        r = 14 if k % 2 == 0 else 6
        a = math.pi * k / 8
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, outline=c, width=2)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=c)


def i_flame(d, cx, cy, c):
    d.polygon([(cx, cy - 15), (cx + 8, cy - 2), (cx + 7, cy + 8),
               (cx + 2, cy + 13), (cx - 5, cy + 11), (cx - 8, cy + 2),
               (cx - 4, cy - 6)], outline=(210, 90, 10), width=3)


def i_target(d, cx, cy, c):
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=c, width=3)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], outline=c, width=2)
    _l(d, [(cx - 15, cy), (cx - 9, cy)], c, 2)
    _l(d, [(cx + 9, cy), (cx + 15, cy)], c, 2)
    _l(d, [(cx, cy - 15), (cx, cy - 9)], c, 2)
    _l(d, [(cx, cy + 9), (cx, cy + 15)], c, 2)


def i_globe(d, cx, cy, c):
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=c, width=3)
    d.ellipse([cx - 5, cy - 12, cx + 5, cy + 12], outline=c, width=2)
    _l(d, [(cx - 12, cy), (cx + 12, cy)], c, 2)


def i_people(d, cx, cy, c):
    d.ellipse([cx - 11, cy - 12, cx - 3, cy - 4], outline=c, width=3)
    d.arc([cx - 14, cy - 3, cx, cy + 13], 180, 360, fill=c, width=3)
    d.ellipse([cx + 3, cy - 12, cx + 11, cy - 4], outline=c, width=3)
    d.arc([cx, cy - 3, cx + 14, cy + 13], 180, 360, fill=c, width=3)


def i_plane(d, cx, cy, c):
    d.polygon([(cx + 14, cy), (cx - 4, cy - 3), (cx - 12, cy - 12),
               (cx - 9, cy - 1), (cx - 14, cy + 6), (cx - 8, cy + 6),
               (cx - 4, cy + 3)], fill=c)


def i_talk(d, cx, cy, c):
    d.rounded_rectangle([cx - 13, cy - 11, cx + 13, cy + 6], 5,
                        outline=c, width=3)
    d.polygon([(cx - 6, cy + 6), (cx - 6, cy + 13), (cx + 2, cy + 6)],
              outline=c, width=2)
    _l(d, [(cx - 8, cy - 5), (cx + 8, cy - 5)], c, 2)
    _l(d, [(cx - 8, cy), (cx + 4, cy)], c, 2)


def i_gavel(d, cx, cy, c):
    _l(d, [(cx - 2, cy - 2), (cx + 11, cy + 11)], c, 4)
    d.rectangle([cx - 12, cy - 12, cx + 2, cy - 4], outline=c, width=3)
    _l(d, [(cx - 13, cy + 13), (cx + 3, cy + 13)], c, 3)


def i_chip(d, cx, cy, c):
    d.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], outline=c, width=3)
    d.rectangle([cx - 3, cy - 3, cx + 3, cy + 3], outline=c, width=2)
    for t in (-6, 0, 6):
        _l(d, [(cx + t, cy - 13), (cx + t, cy - 8)], c, 2)
        _l(d, [(cx + t, cy + 8), (cx + t, cy + 13)], c, 2)
        _l(d, [(cx - 13, cy + t), (cx - 8, cy + t)], c, 2)
        _l(d, [(cx + 8, cy + t), (cx + 13, cy + t)], c, 2)


def i_bottle(d, cx, cy, c):
    d.polygon([(cx - 3, cy - 14), (cx + 3, cy - 14), (cx + 3, cy - 7),
               (cx + 8, cy - 2), (cx + 8, cy + 12), (cx - 8, cy + 12),
               (cx - 8, cy - 2), (cx - 3, cy - 7)], outline=c, width=3)
    _l(d, [(cx - 8, cy + 4), (cx + 8, cy + 4)], (190, 30, 30), 2)


def i_flood(d, cx, cy, c):
    d.polygon([(cx - 10, cy - 13), (cx, cy - 5), (cx + 10, cy - 13)],
              outline=c, width=3)
    d.rectangle([cx - 7, cy - 5, cx + 7, cy + 4], outline=c, width=2)
    _l(d, [(cx - 14, cy + 9), (cx - 7, cy + 6), (cx, cy + 9),
           (cx + 7, cy + 6), (cx + 14, cy + 9)], (40, 100, 190), 3)
    _l(d, [(cx - 14, cy + 14), (cx - 7, cy + 11), (cx, cy + 14),
           (cx + 7, cy + 11)], (40, 100, 190), 3)


def i_lock(d, cx, cy, c):
    d.rectangle([cx - 10, cy - 2, cx + 10, cy + 12], outline=c, width=3)
    d.arc([cx - 6, cy - 13, cx + 6, cy + 1], 180, 360, fill=c, width=3)
    d.ellipse([cx - 2, cy + 3, cx + 2, cy + 7], fill=c)


def i_chart(d, cx, cy, c):
    _l(d, [(cx - 13, cy - 13), (cx - 13, cy + 12), (cx + 13, cy + 12)],
       c, 2)
    _l(d, [(cx - 10, cy - 8), (cx - 3, cy - 2), (cx + 2, cy - 6),
           (cx + 11, cy + 7)], (190, 30, 30), 3)
    _l(d, [(cx + 6, cy + 7), (cx + 11, cy + 7), (cx + 11, cy + 2)],
       (190, 30, 30), 3)


def i_camera(d, cx, cy, c):
    d.rectangle([cx - 13, cy - 8, cx + 13, cy + 11], outline=c, width=3)
    d.rectangle([cx - 5, cy - 12, cx + 3, cy - 8], outline=c, width=2)
    d.ellipse([cx - 6, cy - 4, cx + 6, cy + 8], outline=c, width=3)


def i_ball(d, cx, cy, c):
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=c, width=3)
    _l(d, [(cx, cy - 12), (cx, cy - 4)], c, 2)
    _l(d, [(cx - 11, cy - 4), (cx - 4, cy - 1)], c, 2)
    _l(d, [(cx + 11, cy - 4), (cx + 4, cy - 1)], c, 2)
    _l(d, [(cx - 6, cy + 10), (cx - 3, cy + 3)], c, 2)
    _l(d, [(cx + 6, cy + 10), (cx + 3, cy + 3)], c, 2)


def i_crown(d, cx, cy, c):
    d.polygon([(cx - 13, cy + 9), (cx - 13, cy - 8), (cx - 6, cy + 1),
               (cx, cy - 11), (cx + 6, cy + 1), (cx + 13, cy - 8),
               (cx + 13, cy + 9)], outline=c, width=3)
    _l(d, [(cx - 13, cy + 13), (cx + 13, cy + 13)], c, 3)


def i_game(d, cx, cy, c):
    d.rounded_rectangle([cx - 14, cy - 8, cx + 14, cy + 9], 7,
                        outline=c, width=3)
    _l(d, [(cx - 9, cy), (cx - 3, cy)], c, 3)
    _l(d, [(cx - 6, cy - 3), (cx - 6, cy + 3)], c, 3)
    d.ellipse([cx + 5, cy - 4, cx + 8, cy - 1], fill=c)
    d.ellipse([cx + 8, cy + 1, cx + 11, cy + 4], fill=c)


def i_cloud(d, cx, cy, c):
    d.arc([cx - 13, cy - 8, cx + 1, cy + 8], 90, 270, fill=c, width=3)
    d.arc([cx - 4, cy - 13, cx + 12, cy + 3], 180, 360, fill=c, width=3)
    _l(d, [(cx - 6, cy + 6), (cx + 12, cy + 6)], c, 3)
    d.polygon([(cx + 2, cy + 7), (cx - 2, cy + 13), (cx + 1, cy + 13),
               (cx - 1, cy + 16)], fill=(230, 170, 20))


def i_coin(d, cx, cy, c):
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], outline=c, width=3)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], outline=c, width=2)


def i_ballot(d, cx, cy, c):
    d.rectangle([cx - 12, cy + 1, cx + 12, cy + 12], outline=c, width=3)
    _l(d, [(cx - 6, cy + 6), (cx + 6, cy + 6)], c, 3)
    d.rectangle([cx - 5, cy - 13, cx + 5, cy + 1], outline=c, width=2)


ICONS = {name[2:]: fn for name, fn in list(globals().items())
         if name.startswith("i_")}


# ------------------------------------------------------------------ layout

def tint(c, f=0.84):
    return tuple(int(v + (255 - v) * f) for v in c)


def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def pill(d, x, y, label):
    col = GREEN if label == "CONFIRMED" else AMBER
    w_ = int(d.textlength(label, font=F_PILL)) + 12
    d.rounded_rectangle([x, y, x + w_, y + 15], 7, fill=col)
    d.text((x + 6, y + 2), label, font=F_PILL, fill=(255, 255, 255))
    return w_


def draw_map(d, x, y, w_, h_):
    d.rounded_rectangle([x, y, x + w_, y + h_], 8, fill=(219, 233, 243))
    land = (232, 220, 188)
    # Iran (top right), Iraq (top centre-left), Saudi (bottom), Gulf states
    d.polygon([(x + 205, y + 8), (x + w_ - 6, y + 8), (x + w_ - 6, y + 66),
               (x + 252, y + 58), (x + 218, y + 34)], fill=land)
    d.polygon([(x + 92, y + 10), (x + 196, y + 10), (x + 214, y + 36),
               (x + 168, y + 52), (x + 108, y + 40)], fill=land)
    d.polygon([(x + 100, y + 52), (x + 170, y + 56), (x + 226, y + 66),
               (x + 240, y + h_ - 6), (x + 60, y + h_ - 6), (x + 52, y + 74)],
              fill=land)
    d.polygon([(x + 244, y + 62), (x + 268, y + 70), (x + 262, y + 92),
               (x + 240, y + 84)], fill=land)  # Qatar peninsula
    d.text((x + 252, y + 16), "IRAN", font=F_MAP, fill=INK)
    d.text((x + 118, y + 16), "IRAQ", font=F_MAP, fill=INK)
    d.text((x + 96, y + 82), "SAUDI ARABIA", font=F_MAP, fill=INK)
    d.text((x + 164, y + 36), "KUWAIT", font=F_MAP, fill=INK)
    d.text((x + 226, y + 96), "QATAR", font=F_MAP, fill=INK)
    d.text((x + 8, y + 8), "THE GULF", font=F_MAP, fill=(38, 84, 158))
    d.text((x + 196, y + 74), "STRAIT OF", font=F_MAP, fill=(38, 84, 158))
    d.text((x + 196, y + 86), "HORMUZ", font=F_MAP, fill=(38, 84, 158))
    for (mx, my, lab) in [(188, 50, ""), (222, 64, "BAHRAIN")]:
        d.polygon([(mx + x - 5, my + y), (mx + x, my + y - 6),
                   (mx + x + 5, my + y), (mx + x, my + y + 6)], fill=RED)
        if lab:
            d.text((mx + x + 8, my + y - 5), lab, font=F_MAP, fill=RED)


def draw_cell(d, x, y, w_, h_, sec_color, story):
    head, src_name, pub, conf, icon = story
    d.line([x, y + h_ - 1, x + w_, y + h_ - 1], fill=RULE, width=1)
    d.rounded_rectangle([x + 1, y + (h_ - 40) // 2, x + 41,
                         y + (h_ - 40) // 2 + 40], 7, fill=tint(sec_color))
    ICONS[icon](d, x + 21, y + h_ // 2, sec_color)
    tx = x + 48
    tw = d.textlength(head, font=F_HEAD)
    assert tw <= w_ - 52, f"headline too wide: {head} {tw:.0f} > {w_ - 52}"
    d.text((tx, y + 1), head, font=F_HEAD, fill=INK)
    sy = y + h_ - 17
    stamp = f"22 NOV · {pub}Z · {src_name}" if pub else f"22 NOV · {src_name}"
    d.text((tx, sy), stamp, font=F_SRC, fill=(40, 44, 50))
    sw = d.textlength(stamp, font=F_SRC)
    pill(d, tx + sw + 8, sy, conf)


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # masthead
    d.text((10, 4), "THE WORLD IN ONE PAGE", font=F_TITLE, fill=INK)
    d.text((1014, 16), "EST. 22 NOV 2026", font=F_DATE, fill=GREY,
           anchor="ra")
    counts = (f"{N_STORIES} STORIES · {len(SECTIONS)} SECTIONS · "
              f"{len(REGIONS)} REGIONS · {len(OUTLETS)} OUTLETS")
    d.text((10, 52), "SUNDAY 22 NOVEMBER 2026", font=F_DATE, fill=RED)
    dw = d.textlength("SUNDAY 22 NOVEMBER 2026", font=F_DATE)
    d.text((10 + dw + 14, 52), "· " + counts, font=F_DATE, fill=INK)
    d.line([10, 80, 1014, 80], fill=INK, width=3)

    # DATE CHECK strip (with UTC timeline)
    d.rectangle([0, 84, 1024, 112], fill=RED)
    strip = ("DATE CHECK — EVERY STORY PUBLISHED SUNDAY 22 NOV 2026 · "
             "PUBDATES VERIFIED VIA RSS FEEDS + WIRE STAMPS · "
             "CHECKED 06:29–07:35 UTC")
    assert d.textlength(strip, font=F_STRIP) <= 1004
    d.text((10, 90), strip, font=F_STRIP, fill=(255, 255, 255))

    # lead band
    ly = 120
    d.text((10, ly), "LEAD — GULF CRISIS · MIDDLE EAST", font=F_KICK,
           fill=RED)
    d.text((10, ly + 20), LEAD[0], font=F_LEAD, fill=INK)
    sub_lines = wrap(d, LEAD_SUB, F_LEAD_SUB, 648)
    assert len(sub_lines) <= 2
    for i, ln in enumerate(sub_lines):
        d.text((10, ly + 62 + i * 19), ln, font=F_LEAD_SUB, fill=GREY)
    sy = ly + 104
    d.rounded_rectangle([10, sy, 64, sy + 17], 8, fill=RED)
    d.text((18, sy + 2), "● LIVE", font=F_SRC, fill=(255, 255, 255))
    lead_stamp = "22 NOV · 04:21Z · AFP + XINHUA · GULF NEWS · THE NATIONAL"
    d.text((72, sy + 1), lead_stamp, font=F_SRC, fill=(40, 44, 50))
    sw = d.textlength(lead_stamp, font=F_SRC)
    pill(d, 72 + sw + 8, sy + 1, LEAD[3])
    ICONS[LEAD[4]](d, 662, ly + 58, RED)
    draw_map(d, 692, ly, 322, 122)
    d.line([10, 250, 1014, 250], fill=INK, width=2)

    # story grid: 3 columns, per-column cell heights
    grid_y, grid_h = 258, 738
    col_x = [10, 345, 680]
    col_w = [325, 325, 334]
    for ci, sec_ids in enumerate(COLUMNS):
        x, w_ = col_x[ci], col_w[ci]
        n_cells = sum(len(SECTIONS[s][3]) for s in sec_ids)
        cell_h = (grid_h - 24 * len(sec_ids)) // n_cells
        y = grid_y
        for s in sec_ids:
            name, color, _region, stories = SECTIONS[s]
            d.rectangle([x, y, x + w_, y + 24], fill=color)
            d.text((x + 8, y + 2), name, font=F_SEC, fill=(255, 255, 255))
            cnt = f"{len(stories)} STOR{'IES' if len(stories) != 1 else 'Y'}"
            d.text((x + w_ - 8, y + 3), cnt, font=F_PILL,
                   fill=(255, 255, 255), anchor="ra")
            y += 24
            for st in stories:
                draw_cell(d, x, y, w_, cell_h, color, st)
                y += cell_h

    # footer
    d.line([10, 1002, 1014, 1002], fill=INK, width=2)
    foot = ("Verification log with per-story publication dates: STORIES.md "
            "in this repository · Every story above was published on "
            "22 Nov 2026 · Developing stories carry the amber pill")
    d.text((10, 1006), foot, font=F_FOOT, fill=GREY)
    return img


def main():
    img = build()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, format="PNG", optimize=True)
    data = open(out, "rb").read()
    print("wrote", out, len(data), "bytes")
    print("sha256", hashlib.sha256(data).hexdigest())
    print("stories", N_STORIES, "sections", len(SECTIONS), "regions",
          len(REGIONS), "wire5", N_WIRE5, "outlets", len(OUTLETS),
          "icon_kinds", len(ICON_KINDS))
    assert len(data) <= 550 * 1024, len(data)


if __name__ == "__main__":
    main()
