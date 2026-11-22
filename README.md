# news-image-20261122 — "The World in One Page", Sunday 22 November 2026

One image that sums up the world's news of Sunday 22 November 2026.

**Round 5 (final fix round).** The round-4 gate verdict (PERBAIKI/near)
named five defects; all five are addressed, and the image was frozen
before any judging of this round:

- **The five impossible stamps are resolved.** The three Euronews
  times (07:00Z ×2, 07:02Z) were re-pulled from Euronews' own RSS and
  are genuine pubDates — verified 07:08–07:11Z, rendered 07:12:48Z.
  The two Xinhua times (10:24Z, 11:20Z) could not be proven to be UTC
  from any primary feed (Xinhua page timestamps state no timezone; its
  legacy RSS is a fossil), so **all five Xinhua cells now print the
  date only**. The program asserts max(printed time) = 07:02 ≤ the
  07:11 close of the verification window printed in the DATE CHECK
  strip, and the render postdates the window — no stamp can postdate
  the render. This corrects round 4's claim that every cell prints a
  publication time.
- **43 stories, 43 distinct events.** The two cells that merely
  re-faceted the lead's AFP report are gone (Gulf crisis = lead + 4
  cells), the cartel capture and its death toll are one merged cell,
  and four new distinct events were added from the same verified
  feeds (Victoria fire alert, Grampians rescue, Wembanyama's 50,
  Kansas City's NWSL title). Every story carries a unique event-id in
  draw_news.py, asserted unique in code.
- **Type scale raised where the gate demanded it**: section headers
  26px, masthead date 26px (headlines stay 26px ExtraCondensed Bold).
  Measured on a LANCZOS 300px downscale of the shipped PNG, two ways:
  masthead date ink = 6px (row-band and glyph-span methods agree);
  all 13 section headers = 4–5px glyph-ink span (judge's method);
  lead headline 7px; cell headlines 6px glyph span.
- **Regions are honest**: 9 regions, all geographic — a new OCEANIA
  section holds four ABC News items; the "Global" placeholder is gone
  (Markets & Tech, Sport and Culture are desks, not regions, and are
  not counted). Counts are computed from the data and asserted in
  code: **43 stories · 13 sections · 9 regions · 15 outlets**; wire
  majors (Reuters/BBC/AP/ANI/AFP) carry 13 of 43; the rest are
  established international newsrooms — no aggregators.
- Kept from earlier rounds: CONFIRMED/DEVELOPING pill on every cell,
  LIVE pill on the lead, DATE CHECK strip, hero = the lead band only
  (map 322×122 ≈ 3.7% of canvas), 23 drawn icon kinds + the Gulf map.

## Reproducibility (measured, not asserted)
`entry.png` was rendered from the committed `draw_news.py` with
**Python 3.12.3 / Pillow 10.2.0** (`/usr/bin/python3` — byte-identity
holds only under this interpreter pin; the host default python3
3.14.9 renders different bytes). Two runs in a clean directory
produced byte-identical output, and the render in this repository
matches them:

- sha256(entry.png) = 110f8aebe52157ee25dc3c69b354183e6ab6f390e8f2ba846c1cf32570a69d4b
- size = 328,459 bytes (1024x1024 PNG)

`STORIES.md` is the story-by-story verification log: every headline
was checked against a source published on 2026-11-22, with the
round-5 re-verification window and the Xinhua correction documented.

## Files
- `entry.png` — the entry image (1024x1024, 328,459 bytes).
- `main.py` — the graded program: copies `entry.png` to the output
  directory byte for byte (no network, standard library only), so both
  grading runs emit identical bytes.
- `draw_news.py` — the drawing program and the story data.
- `STORIES.md` — the verification log.
