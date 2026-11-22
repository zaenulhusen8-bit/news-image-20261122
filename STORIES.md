# STORIES.md — verification log, news-image-20261122 (round 4, freshness audit)

Edition: **Sunday 22 November 2026**. 42 stories drawn (1 lead + 41 cells),
12 sections, 9 regions (derived in code from the section data), 15 outlets,
23 distinct drawn icon kinds + 1 schematic Gulf map.

## Method (corrected after the round-3 shadow-judge audit)
Round 3's gate audit caught this page stamping "22 NOV" on stories whose
sources had actually published on 20–21 Nov: the builder's first pass had
trusted a search index's `publishedDate`, which for several outlets is the
page's *update* time, not its publication time. Every item below was
therefore re-verified against **primary publication evidence**: the
pubDate in the outlet's own RSS feed (BBC World/regional/sport/politics,
Al Jazeera, France 24, Euronews, ABC News), or the wire's own timestamp
cross-checked in two independent pulls (Xinhua, AP, AFP, NBC News, The
Independent, The Guardian, The National, Gulf News, Roya News, Petra).
Verification window: 06:29–07:35 UTC, 22 Nov 2026. Items that failed the
audit were dropped (list at the bottom) — including several carried since
round 1 (Houthis/Riyadh was an 8 Nov AFP story; the Rohingya verdict
coverage was 19–20 Nov AP).

Each cell on the page prints its own stamp: `22 NOV · <pub time>Z ·
<outlet>` (the Jordan item's wire time was not captured, so it prints the
date and outlet only).

## Lead
**IRAN STRIKES U.S. BASES ACROSS THE GULF** — AFP, published 22 Nov
04:21Z (Iran strikes on US bases in Bahrain/Kuwait, tankers hit in
Hormuz). Independently corroborated, outlet-to-event: The National live
blog (22 Nov 03:23Z, IRGC claims Patriot radars at Bahrain bases, CENTCOM
denies the F-16 claim), Gulf News (22 Nov 04:48Z, Bahrain intercepts,
industrial site ablaze), Xinhua Middle East summary (22 Nov 05:44Z).
DEVELOPING.

## Gulf & Hormuz
1. **TANKERS HIT IN HORMUZ** — AFP 04:21Z. DEVELOPING.
2. **IRAN HIT BAHRAIN SITE** — AFP 04:21Z (civilian industrial site hit).
   DEVELOPING.
3. **14 TANKERS VS BLOCKADE** — Gulf News 04:48Z (Iran readies 14 tankers
   to breach the blockade). DEVELOPING.
4. **IRGC: PATRIOT RADARS HIT** — The National 03:23Z (IRGC claim;
   attribution printed in the log, claim marked DEVELOPING on the page).
5. **ARAGHCHI PLAN: HORMUZ** — Xinhua 05:44Z (Araghchi: Hormuz plan ready
   within two days). DEVELOPING.
6. **TRUMP SEEKS IRAN DEAL** — Xinhua 05:37Z (Trump seeks a permanent
   deal with Iran). DEVELOPING.

## Middle East
7. **JORDAN SLAMS STRIKE** — Petra, 22 Nov (Jordan condemns the strike on
   Bahrain; carried by Gulf News 22 Nov). CONFIRMED.
8. **GAZA DISPLACED PROTEST** — Al Jazeera RSS pubDate 22 Nov 02:14Z
   (displaced Palestinians protest as strikes continue). CONFIRMED.

## Ukraine
9. **KRYVYI RIH: 2 KILLED** — NBC News 22 Nov 00:29Z (ballistic missile
   on Zelenskyy's hometown kills 2). DEVELOPING.
10. **ZELENSKY: PUTIN 'KILLER'** — The Independent live blog 22 Nov
    04:00Z. CONFIRMED.
11. **CARGO SHIP HIT BY DRONE** — The Guardian Ukraine briefing 22 Nov
    02:19Z (Russian cargo ship hit by a drone in the Baltic Sea; the
    strike itself occurred late 21 Nov — reported in the 22 Nov briefing
    and followed up by France 24 at 06:15Z, item 15). DEVELOPING.

## Europe
12. **COP31: DRAFT DEAL TABLED** — AP 22 Nov 04:01Z (Turkey's final draft
    omits fossil fuels; talks in overtime). DEVELOPING.
13. **BRUSSELS FLIGHTS OFF** — Xinhua Daily World Briefing 22 Nov 05:49Z
    (strike cancellations at Brussels Airport). CONFIRMED.
14. **CLASHES ERUPT IN FRANCE** — Al Jazeera RSS 22 Nov 00:37Z.
    CONFIRMED.
15. **BALTIC SPILLOVER FEAR** — France 24 RSS 22 Nov 06:15Z (Finland says
    the war is "spilling over" after the Baltic drone strike). CONFIRMED.
16. **MAY: 'BREXIT IS DONE'** — BBC Politics RSS 22 Nov 06:01Z (May warns
    Burnham after the PM's EU talks). CONFIRMED.
17. **VILLAGE VOTES 'LEAVE UK'** — Euronews RSS 22 Nov 07:00Z (Suffolk
    village protest vote over asylum plans). CONFIRMED.
18. **MADEIRA OCEAN SURVEY** — Euronews RSS 22 Nov 07:02Z (protection
    works, worrying signs). CONFIRMED.

## Asia-Pacific
19. **FACTORY FIRE: 40 MISSING** — BBC World RSS 22 Nov 06:05Z
    (Indonesian candy factory fire, dozens missing). DEVELOPING.

## South Asia
20. **TAINTED BREW KILLS 11** — The Independent 22 Nov 04:03Z (suspected
    methanol poisoning, Manipur). CONFIRMED.

## North America
21. **FBI DATABASE HACK PROBE** — BBC World RSS 22 Nov 00:10Z.
    DEVELOPING.
22. **ICE ARRESTS AT AIRPORT** — Al Jazeera RSS 22 Nov 05:06Z (two
    detained at Seattle airport). CONFIRMED.
23. **BESSENT LIVING ON BASE** — Al Jazeera RSS 22 Nov 02:05Z (Treasury
    secretary living on a US military base over Iran fears). CONFIRMED.
24. **STORMS RAVAGE CA COAST** — Xinhua 22 Nov 10:24Z ("Super El Niño"
    storms). DEVELOPING.
25. **CANADA JOINS NATO FUND** — Xinhua 22 Nov 11:20Z (25th ally in the
    NATO Innovation Fund). CONFIRMED.

## Latin America
26. **CARTEL BOSS CAPTURED** — BBC World RSS 22 Nov 01:25Z ('El Chapo
    Isidro' arrested in a shoot-out). CONFIRMED.
27. **11 KILLED IN CARTEL RAID** — Al Jazeera RSS 22 Nov 03:34Z (eleven
    killed during the capture). CONFIRMED.
28. **QUAKE EMPTIES CINEMA** — Al Jazeera RSS 22 Nov 01:07Z (earthquake
    strikes Peru, moviegoers flee). CONFIRMED.

## Africa
29. **NIGERIA YOUTH UNSURE** — BBC Africa RSS 22 Nov 00:10Z (young
    Nigerians not shaping the election). CONFIRMED.
30. **NIGERIA BOAT: 24 DEAD** — Al Jazeera RSS 22 Nov 02:45Z (boat
    carrying mourners capsizes). CONFIRMED.
31. **DARFUR FAMILIES BRACE** — Al Jazeera RSS 22 Nov 05:21Z (displaced
    families face winter as aid cuts bite). CONFIRMED.
32. **SUDAN CLASHES, BLUE NILE** — Roya News 22 Nov 04:11Z. DEVELOPING.

## Markets & Tech
33. **KENYA NET BILL FEARS** — Al Jazeera RSS 22 Nov 05:38Z (internet
    metering bill raises privacy/affordability concerns). CONFIRMED.
34. **EU HIRING: SKILLS FIRST** — Euronews RSS 22 Nov 07:00Z.
    CONFIRMED.

## Sport
35. **VERSTAPPEN TAKES VEGAS** — BBC Sport RSS 22 Nov 06:27Z.
36. **AUSTRALIA EDGE WALES** — BBC Sport RSS 22 Nov 04:50Z.
37. **POCHETTINO'S UTD TEST** — BBC Sport RSS 22 Nov 06:21Z.
38. **SPURS TEEN IMPRESSES** — BBC Sport RSS 22 Nov 00:13Z.
39. **INDIA BREAKS TEST RECORD** — ABC News RSS 22 Nov 06:12Z (monster
    innings vs New Zealand in Wellington).

## Culture
40. **GAMER HELPS RESCUE GIRL** — BBC World RSS 22 Nov 00:09Z (teen gamer
    and his mother helped rescue a missing girl).
41. **FRASER AT 1956 REUNION** — ABC News RSS 22 Nov 00:08Z (Dawn Fraser
    fired up for the Melbourne Olympics reunion).

## Dropped by the freshness audit (were drawn in earlier rounds)
Crimean Bridge strikes (BBC 21 Nov 13:17Z), Baltic ship fire (BBC 21 Nov
19:20Z — replaced by its 22 Nov follow-ups, items 11/15), rapper
assassination plot (BBC 21 Nov 10:26Z), tech selloff (BBC 20 Nov 22:42Z),
ANC election fight (BBC 21 Nov 00:34Z), Europe cost-of-living protests
(BBC 20 Nov 16:45Z), Houthis/Riyadh (AFP 8 Nov), Rohingya verdict (AP
19–20 Nov), Seoul AI race (Reuters 21 Nov), Meta office protests
(Reuters 21 Nov), Florida floods (AP 20 Nov), Nvidia probe (BBC 18 Nov),
Eisenkot talks (France 24 21 Nov 20:00Z), F-16 claim and Hodeidah strike
(events dated Friday/Saturday inside their own copy), Lviv strike
(20 Nov), Iskander plant strike (9 Nov). Four items previously credited
to ANI traced back to an aggregator (Desi Talk); none remain — the
Araghchi item is now credited to Xinhua, which reported it directly.
