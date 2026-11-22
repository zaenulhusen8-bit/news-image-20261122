# STORIES.md — verification log, news-image-20261122 (round 5, final fix round)

Edition: **Sunday 22 November 2026**. 43 stories drawn (1 lead + 42
cells), **43 distinct events** (each story carries a unique event-id in
draw_news.py, asserted in code), 13 sections, 9 regions — all nine are
real geographic regions; the round-4 "Global" placeholder is gone (the
Markets & Tech, Sport and Culture desks carry no region and are not
counted). 15 outlets, 23 distinct drawn icon kinds + 1 schematic Gulf
map.

## Method (round 5)
Every item was re-verified against **primary publication evidence**
during the window **07:08–07:11 UTC, 22 Nov 2026**: the pubDate in the
outlet's own RSS feed (BBC World/Africa/Sport/Politics, Al Jazeera,
France 24, Euronews, ABC News — all pulled live twice in the window,
identical results), or the wire's own timestamp cross-checked in two
independent pulls (AFP, AP, NBC News, The Independent, The Guardian,
The National, Gulf News, Roya News, Petra). The final render was made
after the window closed (07:12:48Z); the program asserts
max(publication time) = 07:02 ≤ window close 07:11, so no cell can
carry a stamp later than the render.

## The five disputed stamps — resolved
Round 4's gate held the build because five printed times postdated the
06:40Z render. Round 5 re-pulled each from its primary feed:
- **VILLAGE VOTES 'LEAVE UK' — Euronews 07:00Z: GENUINE.** Euronews'
  own RSS gives pubDate 22 Nov 07:00Z (confirmed in both pulls). The
  round-4 defect was procedural (the item was drawn before it could
  have been verified), not a false time; in this build it was verified
  at 07:08–07:11Z and rendered at 07:12:48Z.
- **EU HIRING: SKILLS FIRST — Euronews 07:00Z: GENUINE** (same feed,
  same confirmation).
- **MADEIRA OCEAN SURVEY — Euronews 07:02Z: GENUINE** (same feed).
- **STORMS RAVAGE CA COAST — printed "10:24Z": NOT PROVABLE, TIME
  DROPPED.** Xinhua page timestamps state no timezone, and Xinhua's
  legacy world RSS endpoint is a fossil (its top item is a 2017 Pence
  story), so no primary feed can prove the UTC basis. The cell now
  prints the date only.
- **CANADA JOINS NATO FUND — printed "11:20Z": NOT PROVABLE, TIME
  DROPPED** (same reason).
For methodological consistency the same treatment was applied to the
three remaining Xinhua times (05:37/05:44/05:49): all five Xinhua cells
print `22 NOV · Xinhua`. Their **dates** stand on round 4's dated
briefing verification (Xinhua Daily World Briefing and Middle East
summary, both dated 22 Nov, cross-checked in two pulls); only the
unprovable clock times were withdrawn. This corrects the round-4
README/STORIES claim that every cell prints its publication time.

## Deduplication (round 5)
- Removed **TANKERS HIT IN HORMUZ** and **IRAN HIT BAHRAIN SITE** —
  both were facets of the lead's single AFP 04:21Z report. The Gulf
  crisis now occupies the lead + 4 cells (5 items, 5 distinct angles:
  blockade preparations, the IRGC's radar claim, Araghchi's plan,
  Trump's deal push, plus Jordan's condemnation in Middle East).
- Merged the cartel pair into one cell: **BOSS TAKEN, 11 KILLED**
  (BBC World RSS 01:25Z for the capture; Al Jazeera RSS 03:34Z for the
  eleven killed during it; Al Jazeera 04:42Z carried the first images
  after the arrest — one event, three reports).
- Added four new distinct events from the same verified feeds:
  Victoria fire alert (ABC 06:04Z), Grampians missing man found alive
  (ABC 04:34Z), Wembanyama's 50-point game (BBC Sport 06:55Z), Kansas
  City's NWSL title (Al Jazeera 06:40Z). A new OCEANIA section gathers
  the two ABC Australia items previously filed under Sport/Culture
  (Wellington Test record, Fraser reunion) with the two new ones.

## Lead
**IRAN STRIKES U.S. BASES ACROSS THE GULF** — AFP, published 22 Nov
04:21Z (Iran strikes on US bases in Bahrain/Kuwait, tankers hit in
Hormuz). Independently corroborated, outlet-to-event: The National
live blog (22 Nov 03:23Z, IRGC claims Patriot radars at Bahrain bases,
CENTCOM denies the F-16 claim), Gulf News (22 Nov 04:48Z, Bahrain
intercepts, industrial site ablaze), Xinhua Middle East summary
(22 Nov). DEVELOPING.

## Gulf & Hormuz
1. **14 TANKERS VS BLOCKADE** — Gulf News 04:48Z (Iran readies 14
   tankers to breach the blockade). DEVELOPING.
2. **IRGC: PATRIOT RADARS HIT** — The National 03:23Z (IRGC claim;
   attribution printed, claim marked DEVELOPING on the page).
3. **ARAGHCHI PLAN: HORMUZ** — Xinhua, 22 Nov (date only, see above;
   Araghchi: Hormuz plan ready within two days). DEVELOPING.
4. **TRUMP SEEKS IRAN DEAL** — Xinhua, 22 Nov (date only). DEVELOPING.

## Middle East
5. **JORDAN SLAMS STRIKE** — Petra, 22 Nov (Jordan condemns the strike
   on Bahrain; carried by Gulf News 22 Nov). CONFIRMED.
6. **GAZA DISPLACED PROTEST** — Al Jazeera RSS pubDate 22 Nov 02:14Z
   (re-confirmed in this round's pull). CONFIRMED.

## Ukraine
7. **KRYVYI RIH: 2 KILLED** — NBC News 22 Nov 00:29Z (ballistic missile
   on Zelenskyy's hometown kills 2). DEVELOPING.
8. **ZELENSKY: PUTIN 'KILLER'** — The Independent live blog 22 Nov
   04:00Z. CONFIRMED.
9. **CARGO SHIP HIT BY DRONE** — The Guardian Ukraine briefing 22 Nov
   02:19Z (Russian cargo ship hit by a drone in the Baltic Sea; the
   strike itself occurred late 21 Nov — reported in the 22 Nov briefing
   and followed up by France 24 at 06:15Z, item 13). DEVELOPING.

## Europe
10. **COP31: DRAFT DEAL TABLED** — AP 22 Nov 04:01Z (Turkey's final
    draft omits fossil fuels; talks in overtime). DEVELOPING.
11. **BRUSSELS FLIGHTS OFF** — Xinhua, 22 Nov (date only; strike
    cancellations at Brussels Airport). CONFIRMED.
12. **CLASHES ERUPT IN FRANCE** — Al Jazeera RSS 22 Nov 00:37Z
    (re-confirmed). CONFIRMED.
13. **BALTIC SPILLOVER FEAR** — France 24 RSS 22 Nov 06:15Z
    (re-confirmed; Finland says the war is "spilling over" after the
    Baltic drone strike — the follow-up report to item 9, drawn as its
    own cell because it is a distinct report of a government's
    reaction). CONFIRMED.
14. **MAY WARNS ON EU RESET** — BBC Politics RSS 22 Nov 06:01Z
    (re-confirmed). CONFIRMED.
15. **VILLAGE VOTES 'LEAVE UK'** — Euronews RSS 22 Nov 07:00Z
    (re-confirmed twice; Suffolk village protest vote over asylum
    plans). CONFIRMED.
16. **MADEIRA OCEAN SURVEY** — Euronews RSS 22 Nov 07:02Z
    (re-confirmed twice; protection works, worrying signs). CONFIRMED.

## Asia-Pacific
17. **FACTORY FIRE: 40 MISSING** — BBC World RSS 22 Nov 06:05Z
    (re-confirmed; Indonesian candy factory fire, dozens missing).
    DEVELOPING.

## South Asia
18. **TAINTED BREW KILLS 11** — The Independent 22 Nov 04:03Z
    (suspected methanol poisoning, Manipur). CONFIRMED.

## North America
19. **FBI DATABASE HACK PROBE** — BBC World RSS 22 Nov 00:10Z
    (re-confirmed). DEVELOPING.
20. **ICE ARRESTS AT AIRPORT** — Al Jazeera RSS 22 Nov 05:06Z
    (re-confirmed; two detained at Seattle airport). CONFIRMED.
21. **BESSENT LIVING ON BASE** — Al Jazeera RSS 22 Nov 02:05Z
    (re-confirmed; Treasury secretary living on a US military base
    over Iran fears). CONFIRMED.
22. **STORMS RAVAGE CA COAST** — Xinhua, 22 Nov (date only — time
    withdrawn, see above; "Super El Niño" storms). DEVELOPING.
23. **CANADA JOINS NATO FUND** — Xinhua, 22 Nov (date only — time
    withdrawn; 25th ally in the NATO Innovation Fund). CONFIRMED.

## Latin America
24. **BOSS TAKEN, 11 KILLED** — BBC World RSS 22 Nov 01:25Z
    (re-confirmed; 'El Chapo Isidro' arrested in a shoot-out; the
    eleven killed during the capture are Al Jazeera RSS 03:34Z — one
    merged cell, see Deduplication). CONFIRMED.
25. **QUAKE EMPTIES CINEMA** — Al Jazeera RSS 22 Nov 01:07Z
    (re-confirmed; earthquake strikes Peru, moviegoers flee).
    CONFIRMED.

## Africa
26. **NIGERIA YOUTH UNSURE** — BBC Africa RSS 22 Nov 00:10Z
    (re-confirmed). CONFIRMED.
27. **NIGERIA BOAT: 24 DEAD** — Al Jazeera RSS 22 Nov 02:45Z
    (re-confirmed; boat carrying mourners capsizes). CONFIRMED.
28. **DARFUR FAMILIES BRACE** — Al Jazeera RSS 22 Nov 05:21Z
    (re-confirmed; displaced families face winter as aid cuts bite).
    CONFIRMED.
29. **SUDAN CLASHES, BLUE NILE** — Roya News 22 Nov 04:11Z.
    DEVELOPING.

## Markets & Tech
30. **KENYA NET BILL FEARS** — Al Jazeera RSS 22 Nov 05:38Z
    (re-confirmed; internet metering bill raises privacy/affordability
    concerns). CONFIRMED.
31. **EU HIRING: SKILLS FIRST** — Euronews RSS 22 Nov 07:00Z
    (re-confirmed twice). CONFIRMED.

## Sport
32. **VERSTAPPEN TAKES VEGAS** — BBC Sport RSS 22 Nov 06:27Z
    (re-confirmed).
33. **AUSTRALIA EDGE WALES** — BBC Sport RSS 22 Nov 04:50Z
    (re-confirmed).
34. **POCHETTINO'S UTD TEST** — BBC Sport RSS 22 Nov 06:21Z
    (re-confirmed).
35. **SPURS TEEN IMPRESSES** — BBC Sport RSS 22 Nov 00:13Z
    (re-confirmed).
36. **WEMBANYAMA SCORES 50** — BBC Sport RSS 22 Nov 06:55Z (new this
    round; 50 points in the Spurs' win).
37. **KANSAS CITY TAKES NWSL** — Al Jazeera RSS 22 Nov 06:40Z (new
    this round; Kansas City Current beat Washington Spirit 2-1 to lift
    their first NWSL title).

## Culture
38. **GAMER HELPS RESCUE GIRL** — BBC World RSS 22 Nov 00:09Z
    (re-confirmed; teen gamer and his mother helped rescue a missing
    girl).

## Oceania
39. **VICTORIA FIRE ALERT EASES** — ABC News RSS 22 Nov 06:04Z (new
    this round; emergency fire warning downgraded in Victoria's
    north-west). CONFIRMED.
40. **FOUND ALIVE AFTER 5 DAYS** — ABC News RSS 22 Nov 04:34Z (new
    this round; man, 55, found alive after going missing in the
    Grampians for five days). CONFIRMED.
41. **INDIA SETS TEST RECORD** — ABC News RSS 22 Nov 06:12Z
    (re-confirmed; monster innings vs New Zealand in Wellington —
    moved from Sport: the event's region is Oceania).
42. **FRASER AT 1956 REUNION** — ABC News RSS 22 Nov 00:08Z
    (re-confirmed; Dawn Fraser fired up for the Melbourne Olympics
    reunion — moved from Culture).

## Dropped by earlier rounds' freshness audits (not drawn)
Crimean Bridge strikes (BBC 21 Nov), Baltic ship fire (BBC 21 Nov —
replaced by its 22 Nov follow-ups, items 9/13), rapper assassination
plot (BBC 21 Nov), tech selloff (BBC 20 Nov), ANC election fight
(BBC 21 Nov), Europe cost-of-living protests (BBC 20 Nov), Houthis/
Riyadh (AFP 8 Nov), Rohingya verdict (AP 19–20 Nov), Seoul AI race
(Reuters 21 Nov), Meta office protests (Reuters 21 Nov), Florida
floods (AP 20 Nov), Nvidia probe (BBC 18 Nov), Eisenkot talks
(France 24 21 Nov), F-16 claim and Hodeidah strike (events dated
Friday/Saturday inside their own copy), Lviv strike (20 Nov),
Iskander plant strike (9 Nov). Four items previously credited to ANI
traced back to an aggregator (Desi Talk); none remain.
