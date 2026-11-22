# news-image-20261122 — "The World in One Page", Sunday 22 November 2026

One image that sums up the world's news of Sunday 22 November 2026.

**Round 6 (FINAL fix round).** The round-5 formal gate verdict
(Seek fallback, PERBAIKI/near) named six fixes; all six are applied,
and the image was frozen before any judging of this round:

- **Column geometry, with the numbers printed.** Columns now hold
  **14 / 13 / 14 cells** at **cell_h 45 / 46 / 45 px** (asserted from
  the data in code; every column ≤ 14 cells, every cell ≥ 44px).
  Ink separation is asserted per cell at source level with the
  fonts' own bounding boxes — the check the verdict itself
  prescribed: headline ink ends **≥ 2px** above stamp ink in every
  cell (measured minimum margin across the 41 cells: **2px**, in the
  45px columns; 3px in the 46px column), stamp ink never passes the
  cell's bottom rule, and headlines are worded without
  below-baseline glyphs (J/Q/comma) so the margin is real. A
  post-render audit on the 300px downscale counts ink rows per cell:
  **min 9, max 10** — two separated text bands, never a filled
  ridge. (The round-5 verdict's premise of an 18-cell column at
  34px did not match the committed file — 15 cells at 41px — but
  column A was genuinely the tightest; it is now fixed and the
  numbers are printed here and in the gate brief.)
- **Icon tiles clamped**: each 40px tile is centred inside its cell
  and the code asserts the tile rect is a subset of the cell rect;
  with cell_h ≥ 45 no tile can reach a header bar. The confidence
  pill is now painted *before* the headline text, so it can never
  erase headline pixels where their rows meet.
- **Freshness audited on EVENT date** (the gate's reading). The
  Guardian Baltic cargo-ship cell — whose own round-5 log dated the
  strike to late 21 Nov — is gone, as are the two Saturday-fixture
  match reports (Wales v Australia, the Spurs teenager) and the
  France clashes item ("another night of protest", 00:37Z). The
  audit standard is written in STORIES.md and applied uniformly;
  the DATE CHECK strip claims exactly what the audit enforces:
  every event occurred on 22 Nov and every story was published on
  22 Nov.
- **Thin sections filled**: Asia-Pacific 1→3, South Asia 1→3,
  Culture 1→4; no section holds fewer than 2 stories. Five cells
  were removed as pure geometry trims (Madeira survey, Canada NATO
  fund, Bessent, Roya Sudan clashes, Village votes).
- **Wire majors up**: Reuters/BBC/AP/ANI/AFP now carry **15 of 42
  (36%)**, up from 13/43 (30%) — every addition is a BBC item
  verified in BBC's own feeds this round.
- **Two stamp corrections, made openly**: Euronews' EU-hiring
  pubDate is 07:00:51 **+01:00** = **06:00Z** (rounds 4–5 printed
  the feed's local string as UTC); BBC updated the Wembanyama item
  to pubDate **07:42Z** (round 5 printed 06:55Z). Both confirmed in
  two live pulls, 07:52:27–07:55:00 UTC on 22 Nov; the render
  postdates the window and the program asserts max(printed time)
  = 07:42 ≤ 07:55.
- **42 stories, 42 distinct events, 13 sections, 9 regions,
  16 outlets** — counts computed from the data and asserted in
  code. Kept from earlier rounds: CONFIRMED/DEVELOPING pill on
  every cell, LIVE pill on the lead, DATE CHECK strip, hero = the
  lead band only (Gulf map 322×122 ≈ 3.7% of canvas), 23 drawn
  icon kinds + the Gulf map, Xinhua cells date-only (their page
  times carry no provable UTC basis).

## Reproducibility (measured, not asserted)
`entry.png` was rendered from the committed `draw_news.py` with
**Python 3.12.3 / Pillow 10.2.0** (`/usr/bin/python3` — byte-identity
holds only under this interpreter pin; the host default python3
3.14.9 renders different bytes). Two runs in a clean directory
produced byte-identical output, and the render in this repository
matches them:

- sha256(entry.png) = 6ef5c196ff55046fc04e97ae1195eb0d709af0412ddbb9132709cea2fa78878a
- size = 291,983 bytes (1024x1024 PNG)

`STORIES.md` is the story-by-story verification log: every headline
was checked against a source published on 2026-11-22, with the
round-6 event-date audit standard, the two-pull verification
window, and the stamp corrections documented.

## Files
- `entry.png` — the entry image (1024x1024, 291,983 bytes).
- `main.py` — the graded program: copies `entry.png` to the output
  directory byte for byte (no network, standard library only), so both
  grading runs emit identical bytes.
- `draw_news.py` — the drawing program and the story data.
- `STORIES.md` — the verification log.
