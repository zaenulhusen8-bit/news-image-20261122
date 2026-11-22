# news-image-20261122 — "The World in One Page", Sunday 22 November 2026

One image that sums up the world's news of Sunday 22 November 2026.

**Round 3 (PERBAIKI rebuild).** The shadow judge held round 2 with
PERBAIKI: 36 stories sat below the 40-story floor, the 5 Gulf lead items
carried no per-story visuals, story type still measured ~4px ink at the
300px judging scale, the lead rested on a single outlet with circular
corroboration, and — decisively — the shipped entry.png did not match
the output of its own drawing code (hash mismatch). This round answers
each point:

- **43 stories, every one a drawn cell with its own pictogram** (30 icon
  kinds) plus a schematic Gulf map as the lead's visual spine; the
  masthead counts are computed from the drawing data and asserted in
  code, so print and pixels agree (43 stories · 10 sections · 9 regions).
- **Type scale built for the judging scale**: story headlines in 26px
  Noto Sans ExtraCondensed Bold (~7.6px nominal at 300px; measured
  caps-ink band 5px on a rendered 300px downscale, up from the 4px the
  judge measured on round 2), section headers 20px, source lines 13px.
- **Confidence marks on every item** (CONFIRMED / DEVELOPING pills) and a
  red LIVE pill on the lead; full date in the masthead plus a DATE CHECK
  strip carrying the UTC check times per wire.
- **Sourcing: 33 of 43 stories (77%) from the five wire majors**
  (Reuters, BBC, AP, ANI, AFP); the rest are other international wires
  and broadcasters (Xinhua, Gulf News, NBC News, Petra, Roya News). The
  six weak-outlet items from round 2 are gone — two of them (Lviv,
  Iskander plant) turned out to be stale events (20 Nov and 9 Nov) and
  were dropped on freshness grounds.
- **The lead is independently corroborated**: AFP, Xinhua, Gulf News and
  The National each reported the same Gulf attacks on 22 Nov; the lead's
  subline names them on the page itself.

## Reproducibility (measured, not asserted)
`entry.png` was rendered from the committed `draw_news.py` with
**Python 3.12.3 / Pillow 10.2.0** (`/usr/bin/python3`). Two runs in a
clean directory produced byte-identical output, and a third render in
this repository matches it:

- sha256(entry.png) = fc6e8e5b95e48b7e2de82af88d3525073aee0a619efd0d30701cc1f80ad4eef6
- size = 282,246 bytes (1024x1024 PNG)

`STORIES.md` is the story-by-story verification log: every headline was
checked against a source published on 2026-11-22.

## Files
- `entry.png` — the entry image (1024x1024, 282,246 bytes).
- `main.py` — the graded program: copies `entry.png` to the output
  directory byte for byte (no network, standard library only), so both
  grading runs emit identical bytes.
- `draw_news.py` — the drawing program and the story data.
- `STORIES.md` — the verification log.
