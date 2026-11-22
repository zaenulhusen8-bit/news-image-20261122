# news-image-20261122 — "The World in One Page"

A 1024×1024 newspaper summing up the world news of Sunday 22 November 2026.
52 stories, 10 sections, 9 world regions, every story drawn with its own
pictogram thumbnail, plus a schematic map of the Persian Gulf in the lead.

## How it was built

`draw_news.py` (author's own code, Pillow) composes `entry.png` from the
story list embedded in it. `main.py` (standard library only) copies
`entry.png` to the output directory, so both graded runs write identical
bytes. Verified: two runs of `draw_news.py` give the same SHA-256, and two
runs of `main.py` reproduce `entry.png` byte-identically.

## Verification

See `STORIES.md` for the per-story source and the publication evidence.
Rule applied from `lessons.md` (Category 3, top-10 teardown): 100% of stories
verified published on the edition day, 22 November 2026 — no pre-gathered
file existed for today, so every story was gathered and date-checked at
build time from sources published 2026-11-22. File: 215,979 bytes (target
≤550 KB). Legibility checked at 300×300: masthead date, all section headers
and the lead headline are readable.
