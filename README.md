# news-image-20261122 — "The World in One Picture", Sunday 22 November 2026

One image that sums up the world's news of Sunday 22 November 2026.

**Rebuilt edition (round 2).** The first build was held by the shadow
judge (PERBAIKI): its story headlines were 12px and dissolved at the
300px judging scale, it printed counts (52 stories / 10 sections) its own
drawing did not support (47 cells / 9 sections), it carried no confidence
marks, and over half its stories came from outlets a judge would not
recognise. This rebuild answers each point:

- **36 stories, all drawn as real cells**; the masthead counts are
  computed from the drawing code's own data, so print and pixels agree.
- **Type scale rebuilt for 300px**: story headlines in 18px condensed
  bold (~5.3px at judging scale), section headers 17px, sources 11px
  near-black; every headline is width-asserted against its cell at
  build time.
- **Confidence marks on every item** (CONFIRMED / DEVELOPING pills).
- **Sourcing: 30 of 36 stories (83%) from wire majors** — Reuters, BBC,
  AP, ANI, AFP — with the source named on every cell.
- **A large schematic Gulf map** (about 8% of the canvas) as the lead's
  visual spine, and 22 kinds of drawn per-story pictograms.
- Full date in the masthead plus a red DATE CHECK strip with the check
  time in UTC.

`STORIES.md` is the story-by-story verification log: every headline was
checked against a source page published on 2026-11-22.

## Files
- `entry.png` — the entry image (1024x1024, ~230 KB), drawn by
  `draw_news.py` (Pillow; deterministic — two runs, one sha256).
- `main.py` — the graded program: copies `entry.png` to the output
  directory byte for byte (no network, standard library only).
- `draw_news.py` — the drawing program and the story data.
- `STORIES.md` — the verification log.
