# STORIES.md — verification log, news-image-20261122 (round 6, FINAL fix round)

Edition: **Sunday 22 November 2026**. 42 stories drawn (1 lead + 41
cells), **42 distinct events** (each story carries a unique event-id
in draw_news.py, asserted unique in code), 13 sections, 9 regions —
all nine are real geographic regions (the Markets & Tech, Sport and
Culture desks carry no region and are not counted). 16 outlets, 23
distinct drawn icon kinds + 1 schematic Gulf map. Wire majors
(Reuters/BBC/AP/ANI/AFP) carry 15 of 42 stories (36%).

## Method (round 6)
Every printed item was re-verified against **primary publication
evidence** in two live pulls on 22 Nov 2026 — pull A **07:52:27–
07:52:42 UTC** and pull B **07:54:47–07:55:00 UTC** — with identical
results: the pubDate in the outlet's own RSS feed (BBC World/Sport/
Politics/Entertainment, Al Jazeera, France 24, Euronews, ABC News
feeds 2942460 and 51120, The Guardian, CNA, The Hindu). Feed-local
times were converted to UTC from the offsets printed in the feeds
themselves: CNA is SGT (UTC+8), The Hindu is IST (UTC+5:30),
Euronews is CET (UTC+1). Items whose outlets expose no usable RSS
subset (AFP lead, AP, NBC News, The Independent, The National, Gulf
News, Petra, Xinhua) stand on the rounds 4–5 two-pull wire-stamp
verification, unchanged this round. The final render was made after
the window closed (08:03Z); the program asserts
max(printed time) = 07:42 ≤ window close 07:55, so no cell can carry
a stamp later than the render. Xinhua cells print the date only
(Xinhua page times carry no stated timezone and two of five captured
times were provably not UTC — rounds 4–5 finding, kept).

## Event-date audit (round 6 — the gate's reading of freshness)
The round-5 gate read the freshness hard check as **event date**, not
publication date, and its one genuine fatal was a story whose own
round-5 log dated its event to late 21 Nov while the DATE CHECK
strip claimed otherwise. Round 6 audits every cell under that
reading, with this standard, applied uniformly: **a cell is dropped
if (a) our own prior log or the item's own text/feed metadata dates
its principal event to 21 Nov or earlier, or (b) it reports a
scheduled fixture known to have been played on 21 Nov. Everything
else published on 22 Nov stands.** Dropped under the standard:

- **CARGO SHIP HIT BY DRONE** (Guardian, was Ukraine) — the round-5
  log itself records "the strike itself occurred late 21 Nov". This
  was the gate's genuine fatal; disclosure in the log did not cure
  the strip's claim.
- **AUSTRALIA EDGE WALES** (BBC Sport) — a Saturday (21 Nov) fixture.
- **SPURS TEEN IMPRESSES** (BBC Sport) — a Saturday (21 Nov) fixture.
- **CLASHES ERUPT IN FRANCE** (Al Jazeera 00:37Z) — the item's own
  framing ("another night of protest") dates the principal event to
  the night of 21 Nov.

Kept despite early-hour stamps, because no evidence dates their
events before 22 Nov: Kryvyi Rih strike (00:29Z), FBI probe (00:10Z),
Gaza displaced protest (02:14Z), gamer rescue (00:09Z), Nigeria
youth survey (00:10Z), Fraser reunion (00:08Z). Five further cells
were removed as pure geometry trims (the column rebalance), not for
freshness: Madeira ocean survey, Canada NATO fund, Bessent living
on base, Roya Sudan clashes, Village votes 'leave UK'.

The DATE CHECK strip now claims exactly what this audit enforces:
**every event occurred on 22 Nov and every story was published on
22 Nov.**

## Corrections made openly this round
- **EU HIRING: SKILLS FIRST — printed time corrected 07:00Z →
  06:00Z.** Euronews' feed gives pubDate "22 Nov 07:00:51 +0100";
  rounds 4–5 printed the feed's local string as if it were UTC. The
  true UTC time is 06:00Z, confirmed in both round-6 pulls.
- **WEMBANYAMA SCORES 50 — printed time updated 06:55Z → 07:42Z.**
  BBC Sport's feed now carries pubDate 07:42Z for this item (the
  item was updated by BBC after round 5's pull); 07:42Z is what both
  round-6 pulls show, and it is the latest stamp on the page.
- **Oceania sources pinned down:** the Victoria fire and Grampians
  items are not in ABC's 2942460 feed; they are verified in ABC feed
  51120 (06:04Z and 04:34Z respectively), confirmed in both pulls.
- Five headlines reworded to remove below-baseline glyphs (J, Q,
  comma) whose ink would reach the stamp row — wording only, same
  stories: AMMAN SLAMS STRIKE (was JORDAN…), SEOUL ED MINISTER OUT
  (was …QUITS), INDIA CRASH KILLS 9 (was RAJASTHAN…), TREMOR EMPTIES
  CINEMA (was QUAKE…), BOSS TAKEN: 11 KILLED (was BOSS TAKEN, 11…).

## Lead
**IRAN STRIKES U.S. BASES ACROSS THE GULF** — AFP, published 22 Nov
04:21Z (wire stamp, rounds 4–5 two-pull verification; corroborated
by The National 03:23Z, Gulf News 04:48Z and Xinhua's 22 Nov Middle
East summary, all drawn as cells below). DEVELOPING, LIVE pill.

## Gulf & Hormuz
1. **14 TANKERS VS BLOCKADE** — Gulf News 04:48Z (wire stamp). DEVELOPING.
2. **IRGC: PATRIOT RADARS HIT** — The National 03:23Z (wire stamp; claim attributed). DEVELOPING.
3. **ARAGHCHI PLAN: HORMUZ** — Xinhua, 22 Nov (date only). DEVELOPING.
4. **TRUMP SEEKS IRAN DEAL** — Xinhua, 22 Nov (date only). DEVELOPING.

## Middle East
5. **AMMAN SLAMS STRIKE** — Petra, 22 Nov (date only; Jordan condemns the strike on Bahrain). CONFIRMED.
6. **GAZA DISPLACED PROTEST** — Al Jazeera RSS 02:14Z. CONFIRMED.

## Ukraine
7. **KRYVYI RIH: 2 KILLED** — NBC News 00:29Z (wire stamp). DEVELOPING.
8. **ZELENSKY: PUTIN 'KILLER'** — The Independent 04:00Z (wire stamp). CONFIRMED.

## Europe
9. **COP31: DRAFT DEAL TABLED** — AP 04:01Z (wire stamp). DEVELOPING.
10. **BRUSSELS FLIGHTS OFF** — Xinhua, 22 Nov (date only). CONFIRMED.
11. **BALTIC SPILLOVER FEAR** — France 24 RSS 06:15Z (Finland's reaction, a 22 Nov government statement). CONFIRMED.
12. **MAY WARNS ON EU RESET** — BBC Politics RSS 06:01Z. CONFIRMED.

## Asia-Pacific
13. **FACTORY FIRE: 40 MISSING** — BBC World RSS 06:05Z. DEVELOPING.
14. **SEOUL ED MINISTER OUT** — The Guardian RSS 05:04Z (education minister resigns, 22 Nov). CONFIRMED.
15. **NK MARATHON DELAYED** — CNA RSS 15:06 SGT = 07:06Z (North Korea delays its international marathon). CONFIRMED.

## South Asia
16. **TAINTED BREW KILLS 11** — The Independent 04:03Z (wire stamp; Manipur). CONFIRMED.
17. **DELHI AIR TURNS 'POOR'** — The Hindu RSS 10:45 IST = 05:15Z (Delhi AQI recorded 22 Nov). CONFIRMED.
18. **INDIA CRASH KILLS 9** — The Hindu RSS 12:49 IST = 07:19Z (road crash in Rajasthan, 22 Nov). CONFIRMED.

## North America
19. **FBI DATABASE HACK PROBE** — BBC World RSS 00:10Z. DEVELOPING.
20. **ICE ARRESTS AT AIRPORT** — Al Jazeera RSS 05:06Z. CONFIRMED.
21. **STORMS RAVAGE CA COAST** — Xinhua, 22 Nov (date only). DEVELOPING.

## Latin America
22. **BOSS TAKEN: 11 KILLED** — BBC World RSS 01:25Z (cartel capture; the eleven killed during it are Al Jazeera RSS 03:34Z — one event, merged cell since round 5). CONFIRMED.
23. **TREMOR EMPTIES CINEMA** — Al Jazeera RSS 01:07Z (Peru earthquake, moviegoers flee). CONFIRMED.

## Africa
24. **NIGERIA YOUTH UNSURE** — BBC RSS 00:10Z. CONFIRMED.
25. **NIGERIA BOAT: 24 DEAD** — Al Jazeera RSS 02:45Z. CONFIRMED.
26. **DARFUR FAMILIES BRACE** — Al Jazeera RSS 05:21Z. CONFIRMED.

## Markets & Tech
27. **KENYA NET BILL FEARS** — Al Jazeera RSS 05:38Z. CONFIRMED.
28. **EU HIRING: SKILLS FIRST** — Euronews RSS 07:00:51+01:00 = **06:00Z** (corrected, see above). CONFIRMED.

## Sport
29. **VERSTAPPEN TAKES VEGAS** — BBC Sport RSS 06:27Z (Las Vegas GP, raced 22 Nov). CONFIRMED.
30. **POCHETTINO'S UTD TEST** — BBC Sport RSS 06:21Z. CONFIRMED.
31. **WEMBANYAMA SCORES 50** — BBC Sport RSS **07:42Z** (updated by BBC, see above). CONFIRMED.
32. **KANSAS CITY TAKES NWSL** — Al Jazeera RSS 06:40Z (NWSL final, played 22 Nov). CONFIRMED.
33. **ARSENAL'S EUROPEAN LAG** — BBC Sport RSS 07:17Z. CONFIRMED.

## Culture
34. **GAMER HELPS RESCUE GIRL** — BBC World RSS 00:09Z. CONFIRMED.
35. **DU MAURIER PHOTOS OUT** — BBC Entertainment RSS 07:20Z. CONFIRMED.
36. **INMATE TO WEST END** — BBC Entertainment RSS 07:32Z. CONFIRMED.
37. **HARRY STYLES' STAR PATH** — BBC Entertainment RSS 07:14Z. CONFIRMED.

## Oceania
38. **VICTORIA FIRE ALERT EASES** — ABC feed 51120 RSS 06:04Z (warning downgraded 22 Nov). CONFIRMED.
39. **FOUND ALIVE AFTER 5 DAYS** — ABC feed 51120 RSS 04:34Z (man found alive in the Grampians, 22 Nov). CONFIRMED.
40. **INDIA SETS TEST RECORD** — ABC News RSS 06:12Z. CONFIRMED.
41. **FRASER AT 1956 REUNION** — ABC News RSS 00:08Z. CONFIRMED.

(Lead + cells 1–41 = 42 stories.)

## Dropped by earlier rounds' freshness audits (not drawn)
Crimean Bridge strikes (BBC 21 Nov), Baltic ship fire (BBC 21 Nov —
its 22 Nov follow-up, Finland's reaction, is drawn as item 11),
rapper assassination plot (BBC 21 Nov), tech selloff (BBC 20 Nov),
ANC election fight (BBC 21 Nov), Europe cost-of-living protests
(BBC 20 Nov), Houthis/Riyadh (AFP 8 Nov), Rohingya verdict (AP
19–20 Nov), Seoul AI race (Reuters 21 Nov), Meta office protests
(21 Nov), Florida floods (AP 20 Nov), Nvidia probe (BBC 18 Nov),
Eisenkot talks (France 24 21 Nov), F-16 claim and Hodeidah strike
(events dated Friday/Saturday inside their own copy), Lviv strike
(20 Nov), Iskander plant strike (9 Nov). Four items previously
credited to ANI traced back to an aggregator (Desi Talk); none
remain.
