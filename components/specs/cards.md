# Cards - all sheets, one spec

Consolidated Markdown spec for every card sheet in `game/components/`. This file replaces the
separate per-sheet spec files (`cards-activity.md`, `cards-event.md`,
`cards-habitus-parts-44x36mm-A4-portrait.md`, `cards-need-hero-44x36mm-A4-portrait.md`,
`cards-project-63x88mm-A4-portrait.md`), which are now redirect stubs pointing here. See the
[board-game-component-specs skill](../../../.github/skills/board-game-component-specs/SKILL.md)
for the editing workflow (md first, then SVG) and `board-game-cards` for the geometry canon
(WAYS OUT/HOW TO ADAPT anatomy, tint derivation, print margins) this file doesn't restate.

## Index

| Section | Source SVG(s) |
|---|---|
| [Activity cards](#activity-cards-63x88mm-a4) | `../cards-activity-63x88mm-A4-portrait.svg`, `../cards-activity-5b-63x88mm-A4-portrait.svg` |
| [Event cards](#event-cards-63x88mm-a4) | `../cards-event-01-09-63x88mm-A4-portrait.svg`, `../cards-event-10-18-63x88mm-A4-portrait.svg`, `../cards-event-19-21-63x88mm-A4-portrait.svg` |
| [Habitus part-cards](#habitus-part-cards-44x36mm-a4-landscape) | `../cards-habitus-parts-01-15-44x36mm-A4-landscape.svg`, `../cards-habitus-parts-16-25-44x36mm-A4-landscape.svg` |
| [NEED and HERO tiles](#need-and-hero-tiles-44x36mm-a4-landscape) | `../cards-need-hero-44x36mm-A4-landscape.svg` |
| [Project cards](#project-cards-88x88mm-a4) | `../cards-project-63x88mm-A4-portrait.svg` |

---

# Activity cards (63x88mm, A4)

## Sheets

| Sheet | Source SVG | Contains |
|---|---|---|
| 1 | `../cards-activity-63x88mm-A4-portrait.svg` | Work x3, Coordinate x2, Workshop, Align, Celebrate x2 |
| 2 | `../cards-activity-5b-63x88mm-A4-portrait.svg` | Work x2 (five total with Sheet 1), Teach x2, Plan, Demo, Reflect, Workshop, Learn |

Eighteen Activity cards, the week 1/3 core loop, split across two A4 sheets (nine per sheet,
each printed once - no reprinting). Card size 63x88mm, text column x=5..58 (53mm). All cards
share the same skeleton: `63x88` border rect (`.c`), title (mono, 6.6-7.5pt, letter-spacing
1.2-1.5), a `.h` rule at y=17, then the card's own body. No category tint band (that's an
Event-card feature, not Activity) - the **effect** itself gets the tinted rounded rect instead,
directly behind its headline number. Both sheets use the same `scale(.95238095,1)` outer-`<g>`
squeeze on every card def - a horizontal compensation kept from an earlier sheet layout so the
*drawn* card stays 63mm authored width while the printed result reads exactly 63x88 against the
board's 65x90 slot; do not remove without checking the printed card still fits.

## Sheet 1

### Grouping

| `<g id>` (in `<defs>`) | Header band | Header colour text class |
|---|---|---|
| `work` | `#EFE4D3` band behind "+1 to one feature" | plain `.q` |
| `coordinate` | `#D3CEDF` band behind "+1 Trust" | `.trust` |
| `workshop` | `#B5C7CF` band behind "+1 Adaptability" | `.adapt` |
| `align` | `#B5C7CF` band behind "+3 Adaptability"; `#D3B1B1` chip behind "Every character pays 1 Motivation" | `.adapt` |
| `celebrate` | `#D3B1B1` band behind "+1 Motivation" | plain |

### Text

| Card | Title | Big effect (in tinted chip) | Body / conditions | Footer italic |
|---|---|---|---|---|
| `work` | WORK | "+1 to one feature" (`#EFE4D3`) | "Adjust total Work for Capability and Shared Practice." | "The only card that moves the project. Hence the trap." |
| `coordinate` | COORDINATE | "+1 Trust" (`#D3CEDF`, 9pt) | "Trust 1 or less: Teach is dead." + "TRUST RISE 1 A WEEK, MAX" | "Check in. Ask for help. Admit the small mistakes." |
| `workshop` | WORKSHOP | "+1 Adaptability" (`#B5C7CF`) | "Unconditionally - no gate, no second mode." + "TOKEN ARRIVES AT WEEK CLOSE, SPENDABLE FROM NEXT WEEK." (mono) | "A meeting that changes the plan, not just records it." |
| `align` | ALIGN | "+3 Adaptability" (`#B5C7CF`) and "Every character pays 1 Motivation" (`#D3B1B1`) | "NOTHING IF ANYONE IS ON 1." + "ONE WAY ONLY. NEVER BACK." (mono) | "A meeting nobody wants. Everybody sits through it." |
| `celebrate` | CELEBRATE | "+1 Motivation" (`#D3B1B1`, 6.6pt) and "to anyone on 3 or less" (5pt) | "Only works if there is something to celebrate: a feature banked, or every Event cancelled this week." (4.4pt) + "AT WEEK CLOSE, WITH THE GRIND." (mono). The old "NO CELEBRATE: LOSE 1 MOTIVATION" chip and "AT 0, A CHARACTER LEAVES" line are gone: they named the weekly grind and the quit rule in week 1, before the table has met either (2026-09-25 playtest) | "Nobody rests at work. You ship something and say so." |

Sheet placement (top-left corner of each `<use>`): Work at (10,12)/(76,12), Coordinate at
(142,12)/(10,104), Workshop at (76,104), Align at (142,104), Celebrate at (10,196)/(76,196), Work again at
(142,196).

**Timing lines (2026-10-10).** Each card that produces something says when it arrives, in 2.9 mono:
Work "BANKS WHEN THE WEEK CLOSES."; Coordinate "TRUST RISES AT WEEK CLOSE, WORKS FROM NEXT WEEK. 1 RISE A
WEEK, MAX."; Celebrate "LANDS AT WEEK CLOSE, WITH THE GRIND. CAPS AT 5."; Align "TOKENS ARRIVE AT WEEK
CLOSE, SPEND THEM FROM NEXT WEEK."; Workshop and Reflect "TOKEN ARRIVES AT WEEK CLOSE, SPENDABLE FROM
NEXT WEEK."

### Illustration

Paint order per card: border, title, rule, effect chip (if any) then effect text, second rule,
body/condition text, footer italic - identical order across all four, which is what lets them
share one mental template.

### Layout diagram

```mermaid
graph TD
  A["63x88 border"] --> B["title (mono, letter-spaced)"]
  B --> C["rule at y=17"]
  C --> D["effect chip (tinted) + big effect text"]
  D --> E["rule (card-specific y)"]
  E --> F["body / condition text"]
  F --> G["footer italic line"]
```

## Sheet 2

### Grouping

| `<g id>` (in `<defs>`) | Header band(s) | Header colour text class |
|---|---|---|
| `work` | `#EFE4D3` behind "+1 to one feature" | plain |
| `teach` | none (plain body); `#D9D3C4` chip behind "EACH TEACHER GAINS +1 CAPITAL" | `.trust` on "DEAD IF TRUST 1 OR LESS" |
| `plan` | `#EFE4D3` behind "+1 EXTRA WORK" | plain |
| `demo` | `#D9D3C4` chip behind "+1 Capital" | plain |
| `reflect` | `#B5C7CF` behind "+1 Adaptability"; `#F7D7A1` behind "+1 Shared Practice" | `.adapt` |
| `workshop` | `#B5C7CF` behind "+1 Adaptability" | `.adapt` |
| `learn` | `#D9D3C4` chip behind "NO CAPITAL FOR THIS ONE" | plain |

### Text

| Card | Title | Effect | Key conditions | Footer italic |
|---|---|---|---|---|
| `work` | WORK | "+1 to one feature" | "Adjust total Work for Capability and Shared Practice." | "The only card that moves the project. Hence the trap." |
| `teach` | TEACH | "Up to 2 characters may each teach 1 partner" | "Partner marks a square up, down, left or right of one you cover - any row."; "DEAD IF TRUST 1 OR LESS"; "EACH TEACHER GAINS +1 CAPITAL"; icon row "ZONE: [one-person tile] PUT DOWN [stacked tile] OR FLIP" | "Scaffolding: give it away and it becomes standing." |
| `plan` | PLAN | "+1 EXTRA WORK" (every Work card on that feature this week) | "HIGH COMPLEXITY: ALSO NEXT WEEK"; "PAYS AS THE WORK RESOLVES" | "Planning pays on hard problems. Only on those." |
| `demo` | DEMO | "+1 Capital to one named team member" | "CAPITAL AT OR ABOVE AVERAGE"; "feature ignores the next NEGATIVE FEEDBACK" | "The field decides who speaks." |
| `reflect` | REFLECT | "Trust 3 or more"; "+1 Adaptability"; "LAST WEEK GAVE EVIDENCE?" with the three well symbols (target: a feature was banked; route: you adapted to 2 Events; cycle: a Hero or a token was played, or an Event cost a Ledger track); "Yes: +1 Shared Practice" (`#F7D7A1`) and "and +1 Motivation to anyone on 3 or less"; "ALSO FILLS A WELL. TOKEN AT CLOSE." | "Ask what's not working - you can only reflect on it." |
| `workshop` | WORKSHOP | "+1 Adaptability" | - (unconditional, no gate) | "A meeting that changes the plan, not just records it." |
| `learn` | LEARN | "Everyone marks a free square each" | "Left or right of one they cover, in their own row."; "No teacher needed."; "COSTS THE DAY, NOTHING ELSE"; "NO CAPITAL FOR THIS ONE"; icon row "ZONE: [one-person tile] PUT DOWN [stacked tile] OR FLIP" | "Nobody taught you. It shows, and it holds." |

Sheet placement: Work (10,12), Work (76,12), Teach (142,12); Teach (10,104), Plan (76,104), Demo
(142,104); Reflect (10,196), Workshop (76,196), Learn (142,196).

### Illustration

Same `scale(.95238095,1)` squeeze and shared skeleton as Sheet 1 (border, title, rule, body,
rule, footer). Every card on this sheet carries at most one tinted chip, drawn immediately
before its own text line - same template as Sheet 1. Paint order otherwise identical to Sheet
1's card template.

### Layout diagram

```mermaid
graph TD
  A["63x88 border"] --> B["title"]
  B --> C["rule at y=17"]
  C --> D["body text, with 0-2 tinted chips inline before their text"]
  D --> E["second rule (card-specific)"]
  E --> F["condition/mono callouts"]
  F --> G["footer italic line"]
```

---

# Event cards (63x88mm, A4)

## Sheets

| Sheet | Source SVG | Contains |
|---|---|---|
| 1 | `../cards-event-01-09-63x88mm-A4-portrait.svg` | Events 1-9 |
| 2 | `../cards-event-10-18-63x88mm-A4-portrait.svg` | Events 10-18 |
| 3 | `../cards-event-19-21-63x88mm-A4-portrait.svg` | Events 19-25 (THE BIKESHED, LEADS FROM BEHIND, THE DASHBOARD, SHAKY GROUND, ALWAYS REACTING, EVERYONE IS EQUAL, THE WOLF) - three rows on the sheet, rest blank |

Twenty-five "shit happens" cards, same size as Activity cards, split across three A4 sheets.
Draw two every week. See `board-game-cards` for the full WAYS OUT / HOW TO ADAPT anatomy and
tint-derivation rule every sheet follows. Icon defs (`i-base/i-head/i-item/i-torso`, `i-head` is the HERO glyph and now draws the Legs triangle,
`q1`-`q5`) are shared shapes but each sheet defines its own copy - they don't share `<defs>`
across files. Sheet 3 names an organisational-behaviour pattern from
[../../docs/theoretical-sources.md](../../docs/theoretical-sources.md) on each card without
ever printing the theorist's name, per the house rule; it uses only one row of three, the rest
of the page is intentionally blank (see `board-game-component-specs` for why a sheet doesn't
need to be filled to be valid).

## Sheet 1

### Grouping

| `<g id>` (in `<defs>`) | Category | Header tint (hex) |
|---|---|---|
| `status` | Management | `#F7D7A1` (`.cat-mgmt`) |
| `budget` | Management | `#F7D7A1` |
| `requirements` | Customer | `#B5C7CF` (`.cat-cust`) |
| `feedback` | Customer | `#B5C7CF` |
| `scope` | Customer | `#B5C7CF` |
| `priority` | Customer | `#B5C7CF` |
| `hoarding` | People | `#D3CEDF` (`.cat-ppl`) |
| `burnout` | People | `#D3CEDF` |
| `outage` | Environment | `#C7CFB5` (`.cat-env`) |

### Text

Every card follows: CATEGORY label -> title (1-2 lines) -> rule -> effect body (with 0-2 tinted
chips) -> optional Torso-reaction line (icon + pip + chip + mono caption) -> HOW TO ADAPT box
(ADAPT n, HERO icon+text, HABIT name, "SO IT COSTS n INSTEAD" or "SO IT NEVER HAPPENS") ->
footer italic line.

| Card | Title | Effect | Torso reaction | ADAPT | HERO | HABIT | Footer italic |
|---|---|---|---|---|---|---|---|
| `status` | STATUS MEETING | remove one card, never happens; everyone loses 1 Motivation | Autonomy: lose 1 Motivation / Hierarchy: no loss | 3 | Take Charge (1 pip) | Shared Repertoire, costs 2 instead | "Not information - it's about being seen." |
| `budget` | BUDGET CUT | everyone loses 1 Motivation | Autonomy: lose 1 / Hierarchy: no loss | 2 | Take Charge (1 pip) | Shared Repertoire, costs 1 instead | "Nobody explains the reasoning to you." |
| `requirements` | REQUIREMENTS CHANGE | The unbanked feature with the most Work left loses 1 Work it already has | Quality: lose 1 Motivation | 2 | Take Charge (1 pip) | Team Reflexivity, costs 1 instead | none |
| `feedback` | NEGATIVE FEEDBACK | one banked feature loses 2 Work, comes off the tower | Quality: lose 1 Motivation | 3 | Analyze (2 pips) | Team Reflexivity, costs 2 instead | "A feature that passed a Demo is safe." |
| `scope` | SCOPE CREEP | unbanked feature closest to done gains +2 Work Cost | Quality: lose 1 Motiv. | 3 | Analyze (2 pips) | Team Reflexivity, costs 2 instead | "Everybody called it a small addition." |
| `priority` | PRIORITY CHANGES | remove one card this week | Quality: lose 1 Motivation | 2 | Analyze (2 pips) | Team Reflexivity, costs 1 instead | "Last week was the wrong thing." |
| `hoarding` | KNOWLEDGE HOARDING | Remove all TEACH cards | Community: lose 1 Motivation | 2 | Support (3 pips) | Psychological Safety, costs 1 instead | "Nobody wanted to be the one to ask." |
| `burnout` | BURNOUT WARNING | anyone on 1 Motivation leaves next week unless a Celebrate is played | Community: lose 1 Motivation | 2 | Support (3 pips) | Psychological Safety, costs 1 instead | "Everyone saw it coming." |
| `outage` | EQUIPMENT OUTAGE | Remove one WORK card; everyone loses 1 Motivation | Hierarchy: lose 1 Motivation | 3 | Support (3 pips) | Who Knows What, costs 2 instead | "Nobody's fault, and it costs a week." |

Sheet placement (assumed 3x3 top-left corners, verify against live SVG if reordering):
`status`(10,12) `budget`(76,12) `requirements`(142,12) / `feedback`(10,104) `scope`(76,104)
`priority`(142,104) / `hoarding`(10,196) `burnout`(76,196) `outage`(142,196).

### Illustration

Paint order per card (identical across all 9, see `board-game-cards` for the canonical
version): category tint band (`.6,.6` inset, `61.8x22.4`, rx 1.4) drawn **before** the border so
the border stays on top -> border rect -> category label + title -> rule (y=23) -> body text,
each colour-coded chip drawn immediately before its own text -> optional Torso-reaction row
(icon `<use>`, pip `<use>`, small chip, mono caption) -> WAYS OUT box (`.w` outline,
`5,54,53,22`) with "HOW TO ADAPT" label, ADAPT number, **one empty rounded square per adapt
token of the cost** (4.8 mm, `rx` .8, x 34/40/46, y 59 - the same shape as the pool wells on
board 2, so tokens are placed on the card as they are paid; `#cost1` / `#cost2` / `#cost3` in each sheet's
defs), "or", tint strip (`5.4,68.6,52.2,7.2`,
same category colour) with HERO icon/text on top of it, HABIT label/name below, cost line.
**Cost follows size (2026-10-07):** cost 1 = a nuisance, 2 = a real hit, 3 = lasting or
whole-week damage (8 / 12 / 4 cards, average 1.8). Habit takes 1 off, minimum 0, so a cost-1
card's cost line reads "SO IT IS FREE" in place of "SO IT COSTS n INSTEAD" (rulebook §6.1).
**Flavour text leads the card (2026-10-07):** the old italic footer at y=84 is gone on every
63x88 card, and the flavour now comes first. On Event cards it is plain serif 4.2 (lines 4.8 mm
apart, 2 lines max) at y 28-32.8, and the rule text, Torso rows, WAYS OUT box and cost squares
sit in a `translate(0,9.5)` group below it, so the box spans y 63.5-85.5. Where it reads as one
sentence the flavour is folded into the rule text instead (requirements, feedback, scope, priority,
hoarding, reinforcements, legacy, false start, deadline, bikeshed), 4.2 serif, same group shift.
A citation goes at the bottom of the card (Reinforcements: `BROOKS 1975`, mono 2.6 at y 86.2, box
shifted only 6). On Activity cards the flavour leads at y 23.5-28.3 (plain serif 4-4.2) and the rule
content sits in a translate group (6-15.5 mm) below it; no divider. On Project cards it sits in
the header, right of the title (x 46, serif 3.4); the footer rule is gone.

**Torso loss on top of "Everyone loses 1" reads "LOSE 1 EXTRA"** (Status Meeting, Budget Cut,
Equipment Outage, The Team Splits, Reorganised, Everything At Once, A Flat Week, The Audit): the
chip sits behind "1 EXTRA" only. On cards with no all-character loss the row still reads
"LOSE 1 MOTIVATION". Every one of those eight cards also prints the immune Torso ("X: NO LOSS",
plain mono 2.7) under the extra-loss row; the pairs follow rulebook section 5 (Environment:
Hierarchy loses, Autonomy immune; People: Community loses, Quality immune; Management: Autonomy
loses, Hierarchy immune). Cards with no HERO route (none on this sheet) would drop the icon and print "No
hero can save this." in its place - `status` through `outage` all have a HERO option here.

### Layout diagram

```mermaid
graph TD
  A["63x88 border"] --> B["category tint band (drawn before border)"]
  B --> C["category label + title"]
  C --> D["rule y=23"]
  D --> E["body text + colour chips"]
  E --> F["optional Torso-reaction row"]
  F --> G["WAYS OUT box: ADAPT n / HERO icon+text / HABIT name / cost line"]
  G --> H["footer italic line"]
```

## Sheet 2

The second half of the Event deck. HERO now keys off all 5 Legs/Pressure-Response options
(Take Charge/Analyze/Support/Engage/Challenge). `build` (False Start), `audit` (The Audit)
and `deadline` (The Date Moves Up) have **no HERO route** - "No hero can save this."

### Grouping

| `<g id>` (in `<defs>`) | Category | Header tint (hex) |
|---|---|---|
| `reinforcements` | People | `#D3CEDF` |
| `legacy` | Environment | `#C7CFB5` |
| `build` (title "FALSE START") | Environment | `#C7CFB5` |
| `split` (title "THE TEAM SPLITS") | People | `#D3CEDF` |
| `reorg` (title "REORGANISED") | Management | `#F7D7A1` |
| `crunch` (title "EVERYTHING AT ONCE") | Environment | `#C7CFB5` |
| `morale` (title "A FLAT WEEK") | People | `#D3CEDF` |
| `audit` (title "THE AUDIT") | Management | `#F7D7A1` |
| `deadline` (title "THE DATE MOVES UP") | Customer | `#B5C7CF` |

### Text

| Card | Effect | Torso reaction | ADAPT | HERO | HABIT | Footer italic |
|---|---|---|---|---|---|---|
| `reinforcements` (MORE HANDS) | feature with most Work this week: halve that Work (round down) | none | 2 | Engage (4 pips) | Shared Repertoire, costs 1 instead | "More hands, more talk. BROOKS 1975" |
| `legacy` (OLD FOUNDATIONS) | feature with most Work already banked gains +2 Work Cost | Hierarchy: lose 1 Motiv. | 2 | Engage (4 pips) | Who Knows What, costs 1 instead | "Built years ago. Nobody wrote down why." |
| `build` (FALSE START) | first Work card this week produces nothing | Hierarchy: lose 1 Motiv. | 2 | none - "No hero can save this." | Who Knows What, costs 1 instead | "It worked yesterday." |
| `split` (THE TEAM SPLITS) | two characters may not take the same feature; lose 1 Trust; everyone loses 1 Motivation | Community: lose 1 Motiv. | 2 | Challenge (5 pips) | Psychological Safety, costs 1 instead | "Nobody said anything out loud." |
| `reorg` (REORGANISED) | everyone loses 1 Motivation; lose 1 Shared Practice | Autonomy: lose 1 / Hierarchy: no loss | 2 | Engage (4 pips) | Shared Repertoire, costs 1 instead | "Only the chart changed, not the work." |
| `crunch` (EVERYTHING AT ONCE) | no feature may take more than 1 Work this week; everyone loses 1 Motivation | Hierarchy: lose 1 Motiv. | 3 | Challenge (5 pips) | Who Knows What, costs 2 instead | "All of it is the top priority." |
| `morale` (A FLAT WEEK) | everyone loses 1 Motivation; a feature banked this week is no reason to Celebrate | Community: lose 1 / Quality: no loss | 1 | Challenge (5 pips) | Psychological Safety, free | "Nothing happened. That is it." |
| `audit` (THE AUDIT) | one card this week must be Workshop or lose a card + 1 Trust + 1 Motivation | Autonomy: lose 1 Motivation | 2 | none - "No hero can save this." | Shared Repertoire, costs 1 instead | "No one person can be the answer." |
| `deadline` (THE DATE MOVES UP) | every Work card this week produces 1 less (never below 0) | Quality: lose 1 Motiv. | 3 | none - "No hero can save this." | Team Reflexivity, costs 2 instead | "This one is not about any of you." |

Sheet placement: `reinforcements`(10,12) `legacy`(76,12) `build`(142,12) / `split`(10,104)
`reorg`(76,104) `crunch`(142,104) / `morale`(10,196) `audit`(76,196) `deadline`(142,196).

### Illustration

Same shared anatomy as Sheet 1 - see that sheet's illustration section and `board-game-cards`.
The three no-HERO cards (`build`, `audit`, `deadline`) replace the icon+HERO-text line with a
single italic "No hero can save this." at the same y-position (y=66), so the HABIT line below
it does not shift - **never let the HERO-less state change the HABIT/cost line positions**,
that would break cross-card alignment.

### Layout diagram

```mermaid
graph TD
  A["63x88 border"] --> B["category tint band"]
  B --> C["category label + title"]
  C --> D["rule y=23"]
  D --> E["body text + colour chips"]
  E --> F["optional Torso-reaction row"]
  F --> G["WAYS OUT box: ADAPT n / HERO icon+text OR 'No hero can save this.' / HABIT name / cost line"]
  G --> H["footer italic line"]
```

## Sheet 3

A third Event sheet, extending the deck from 18 to 21 cards. Only one row of three is used; the
rest of the page is intentionally blank.

### Grouping

| `<g id>` (in `<defs>`) | Category | Header tint (hex) |
|---|---|---|
| `bikeshed` | Management | `#F7D7A1` (`.cat-mgmt`) |
| `leadsbehind` | Management | `#F7D7A1` |
| `dashboard` | Customer | `#B5C7CF` (`.cat-cust`) |
| `confidence` | Environment | `#C7CFB5` (`.cat-env`) |
| `reacting` | Customer | `#B5C7CF` |
| `equal` (title "EVERYONE IS EQUAL") | Management | `#F7D7A1` |
| `wolf` (title "THE WOLF") | Management | `#F7D7A1` |

### Text

| Card | Title | Effect | Torso reaction | ADAPT | HERO | HABIT | Footer italic |
|---|---|---|---|---|---|---|---|
| `bikeshed` (THE BIKESHED) | one line | The easiest unbanked feature gets +1 Work; the hardest gets nothing this week | Quality: lose 1 Motivation | 1 | Take Charge (1 pip) | Shared Repertoire, free | "Somebody had a strong opinion about the paint." |
| `leadsbehind` (LEADS FROM BEHIND) | two lines | Everyone loses 1 Motivation, except whoever has the highest Capital - they wrote it, they're exempt | none (the Capital exemption *is* the card; no Torso layer added on top) | 1 | Challenge (5 pips) | Shared Repertoire, free | "Everyone felt it. Almost everyone." |
| `dashboard` (THE DASHBOARD) | one line | Work only counts this week if it's on a Low feature; Medium/High Work happens but changes nothing | Quality: lose 1 Motivation | 3 | Analyze (2 pips) | Team Reflexivity, costs 2 instead | "The number went up. Nothing else did." |
| `confidence` (SHAKY GROUND) | one line | A demo crashed in front of the customer - **the team loses 1 Capability** (move the Ledger coin down one, permanently, not a one-week penalty) | Hierarchy: lose 1 Motivation | 3 | Engage (4 pips) | Who Knows What, costs 2 instead | "Confidence is earned in public - and lost there too." |
| `reacting` (ALWAYS REACTING) | one line | The team stops planning ahead and only reacts; deadlines slip sideways - **the team's Adaptability pool loses 1 token** (shared pool, cap 6; rulebook §4) | Quality: lose 1 Motivation | 1 | Challenge (5 pips) | Team Reflexivity, free | "There was a plan. Nobody remembers it now." |
| `equal` (EVERYONE IS EQUAL) | two lines | No Hero and no Authorized Voice this week, nobody gains Capital; everyone loses 1 Motivation | Autonomy: lose 1 extra / Hierarchy: no loss | 2 | none - "No hero can save this." | Shared Repertoire, costs 1 instead | "No titles. No one to ask, so nobody does." |
| `wolf` (THE WOLF) | one line | **The Wolf is the boss, the manager** (named on the card). Management targets the character with the most Capital (**the shepherd**, named on the card as "TARGET: THE SHEPHERD" with a target glyph), who **stays on the team**. **Cannot be cancelled.** Team steps up to shield them (+1 Capital to that character, every character loses 1 Motivation) or that character's Capital is erased (goes to 0) | none (the cost is flat and falls on everybody) | **none - no ADAPT number** | **none - no HERO line** (stepping up is not a Hero play) | none | "" (no flavour line: the rule text fills the space) |

Sheet placement: `bikeshed`(10,12) `leadsbehind`(76,12) `dashboard`(142,12) / `confidence`(10,104)
`reacting`(76,104) `equal`(142,104) / `wolf`(10,196) - three rows, the last two slots of row 3 left blank.

**THE WOLF breaks the WAYS OUT anatomy on purpose.** The "HOW TO ADAPT" box becomes "HOW TO RESIST": a large "STEP UP" (mono 4) with "+1 CAPITAL", an italic "by the one with most Capital", a tinted strip carrying "COST: ALL LOSE 1 MOTIVATION" and "IF NOT: THEIR CAPITAL → 0", and "NO ADAPT. NO HERO.". There are no cost squares, no Torso row, no HERO icon and no HABIT line. Its border is `stroke-width .9`, the same marker the no-HERO cards use for "this one is different".

**Why these two exist.** Every Team State track needs a way down as well as up, or the Ledger's
own rule (§18: "the coin can walk back down afterwards") has nothing to point at for two of the
four tracks. Before these cards, Trust could fall (`split`, `audit`, the rulebook's `CONFLICT`)
and Shared Practice could fall (`reorg`), but **Capability and Adaptability never had a single
card that touched them downward** - `confidence` and `reacting` close that gap, one each. Both
read as a track-level change, not a one-week/one-character Motivation hit: the effect line names
the track directly ("the team loses 1 Capability/Adaptability"), distinct from the Torso
reaction's personal, one-character Motivation loss underneath it - and each card's HABIT is
deliberately the one that track itself unlocks (Who Knows What for Capability, Team Reflexivity
for Adaptability), so a team that already invested in the track being hit gets it cheaper to
cancel.

### Illustration

Same shared anatomy as Sheets 1/2 - see those sheets and `board-game-cards` for the canonical
WAYS OUT/HOW TO ADAPT layout. `leadsbehind` deliberately carries **no Torso reaction row**: the
card's mechanic already *is* an exemption (highest Capital is spared the flat Motivation loss),
and adding a second, Torso-keyed exemption on top would double the "who's exempt" logic on one
card - `reinforcements` and `build` (Sheet 2) are the existing precedent for a card with zero
Torso reaction. `bikeshed` and `dashboard` both react on **Quality** (`i-torso` + `q4`), reusing
the identical chip/rect snippet already used on `requirements`/`feedback`/`scope`/`priority`
(Sheet 1) verbatim - `dashboard`'s copy is shifted down 5mm (`y=46.9`/`48` instead of
`41.9`/`43`) because its effect text runs one line longer than theirs. `confidence` reuses
`bikeshed`'s exact geometry (3 body lines, Torso row at `41.9`/`43`) with a Hierarchy reaction
(`q2`) instead of Quality; `reacting` reuses `dashboard`'s exact geometry (4 body lines, Torso
row at `46.9`/`48`) with the same Quality reaction. Reusing known-good coordinates rather than
re-deriving new ones keeps every card's WAYS OUT box aligned at the same `y=54`.

### Layout diagram

```mermaid
graph TD
  A["63x88 border"] --> B["category tint band (drawn before border)"]
  B --> C["category label + title"]
  C --> D["rule y=23"]
  D --> E["body text + colour chips"]
  E --> F["Torso-reaction row (all but leadsbehind)"]
  F --> G["WAYS OUT box: ADAPT n / HERO icon+text / HABIT name / cost line"]
  G --> H["footer italic line"]
```

---

# Habitus part-cards (44x36mm, A4 landscape)

Source: `../cards-habitus-parts-01-15-44x36mm-A4-landscape.svg` (sheet 1 of 2 - Base, Head, Torso)
and `../cards-habitus-parts-16-25-44x36mm-A4-landscape.svg` (sheet 2 of 2 - Legs, Item)
Page: 297x210mm each - **true A4 landscape**, so both sheets print at 100% with no
print-driver "fit to page" auto-scaling. Card size 44x36mm, 5-per-row, unchanged.

**Filename/history note:** this sheet used to be one file at a custom 272x297mm page size,
which fit neither A4 orientation. Print drivers silently auto-scaled it down to fit real A4
paper, so the printed cards no longer matched the true 44x36mm seats on the person board (the
board, already true A4 landscape at 297x210mm, always printed correctly - "the board is
master"). Fixed by splitting the 25 cards across two true-A4-landscape files, one 15-card
sheet (Base/Head/Torso) and one 10-card sheet (Legs/Item). The old single-file SVG
(`cards-habitus-parts-44x36mm-A4-portrait.svg`) is deprecated in place with a redirect notice
and should be deleted from the folder. All card content, layout constants, and conventions
documented below are unchanged and apply identically to both new sheets.

Twenty-five part-cards (5 rows x 5 options: Base, Legs, Torso, Head, Item), dealt at random,
one per row, and assembled bottom to top into the figure on the person board's HABITUS row.
Every card carries the habitus card tint `#F0E3D1` (lightened 2026-10-07 from `#E8D4B8`; the person-board seats and the Shit Happens HERO panel were lightened to match). **No hand-written (Caveat) aside on any card** -
removed for print readability; all body/mechanic text lives at `2.6px` or larger, one size up
from the previous `2.0-2.1px` tier that was too small to read at true print scale.

Each card is a plain positioned group (no `<defs>`/`<use>` reuse for the card body - all 25 are
drawn inline, each `44x36`, `rx 1.5`, class `.cut` = fill `#F0E3D1`, stroke `#2A2620`). Every row
is laid out as one base card at a literal `x`, plus four more each wrapped in a cumulative
`<g transform="translate(Nx13.5,0)">` (13.5, 27, 40.5, 54mm) - **when editing a single card in a
row, edit inside its own transform group, don't recompute the absolute x.** A thin `.hair`
divider (`#4A5259`, opacity .7) sits under each card's name. The corner icon (shape = row,
pip count = element, defined once in `<defs>` and placed via `<use>` at the end of the file) is
unaffected by any of the text/font changes below.

There are two per-row card templates:
- **Mechanic template** (BASE, TORSO, LEGS): name, hairline, then two mono mechanic lines, each
  with a coloured background chip highlighting the changed number/keyword. BASE additionally
  has two short serif flavour lines between its two mechanic lines. **Never abbreviate a full
  word (Motivation, Capability, Shared Practice, Adaptability) - if it doesn't fit on one mono
  line, wrap it onto an extra line instead**, using the card's own bottom slack (the template
  baselines below already include the wrap lines where a card needs one).
  Text baselines (absolute y, mechanic template): name `+7` from card top, hairline `+10`.
  BASE: mono line 1 `+15`, flavour line 1 `+19.5`, flavour line 2 `+24`, mono line 2 `+29`
  (plus a wrapped `+33` line on By The Book and Competitive, see below).
  TORSO: mono line 1 `+16` (chip line only), wrapped `+20` ("-1 MOTIVATION", own chip
  `#D3B1B1`), mono line 2 `+27`. LEGS: mono line 1 `+16` (label only, no chip), wrapped `+20` (chip line),
  mono line 2 `+27` (label only), wrapped `+31` (chip line).
- **Flavour template** (HEAD, ITEM): name, hairline, then four serif body lines in two
  sentence-pairs. Baselines: name `+7`, hairline `+10`, line 1 `+16`, line 2 `+20`, line 3 `+26`,
  line 4 `+30`.

## BASE row - "UPBRINGING → COST AND REPAYMENT" · aside: "your own Motivation, never Work"

| Card | Name | Mono line 1 (chip) | Flavour (2 lines) | Mono line 2 (chip) |
|---|---|---|---|---|
| 1 | Bookish | `LEARN: +2 MOTIVATION` (chip on "+2 MOTIVATION") | "Theory first, then" / "hands, eventually." | `TEACH: -1 MOTIVATION` (chip on "-1 MOTIVATION") |
| 2 | Hands-On | `TEACH: +2 MOTIVATION` (chip on "+2 MOTIVATION") | "You fix it, then" / "explain it - maybe." | `LEARN: -1 MOTIVATION` (chip on "-1 MOTIVATION") |
| 3 | Sheltered | `GRIND DOESN'T TOUCH YOU` (no chip) | "The highs and lows" / "never quite reached you." | `MOTIVATION NEVER OVER 3` (chip on "MOTIVATION" only, `#D3B1B1`; "NEVER OVER 3" un-chipped) |
| 4 | Dependable | `TAKE ONE FOR THE TEAM` (no chip) | "Somebody has to hold it together." / "It might as well be you." | `SPEND 3 MOTIVATION` (chip, `#D3B1B1`) + wrapped `+1 TRUST +1 CAPITAL` (two chips on the same line: `#D3CEDF` on "+1 TRUST", `#D9D3C4` on "+1 CAPITAL") |
| 5 | Competitive | `HERO IS REUSABLE` (no chip) | "Still needs 3 Motivation." / "You needed this win." | `ANOTHER PLAYS HERO:` (no chip) + wrapped `-1 MOTIVATION` (chip) |

All chips fill `#D3B1B1` (the standing Motivation-cost tint), **except** Dependable's
`+1 TRUST +1 CAPITAL` line, which carries two chips instead: the Trust category tint
`#D3CEDF` (the same lavender used for People/Trust on the TORSO row) and the Capital tint
`#D9D3C4` (Bone, the same colour used for Capital chips elsewhere on this sheet) - it's a stat
gain, not a Motivation cost, so it doesn't share the Motivation chip's colour even though it
sits directly under one on the same card. The Capital half matches the rulebook's new §5.1
trigger: paying Motivation for Take One For The Team now earns Capital too, so the card that
prints that action needed to say so - fitted onto the existing line since the card has no room
for a new one.

**Dependable** (was By The Book, was Strict) replaces the old "ignore 1 Event loss" card with a
printed version of the rulebook's Take One For The Team standing action (§ "Take one for the
team"), at a steeper cost specific to this build: **3** Motivation for **+1 Trust and +1
Capital**, versus the generic standing action's 1-for-1 (also now worth +1 Capital, per §5.1).
Same shared-ceiling rule still applies (Trust rises at most once per week, however many sources
push it).

## HEAD row - "EDUCATION → WHERE YOU START" · aside: "the row you begin in on the Zone"

> **Swapped 2026-10-07 (no rule change):** this row was the LEGS row (triangle icon) and the old
> HEAD row below is now LEGS (hexagon swapped for the triangle). Education is now the **Head**
> (hexagon icon, sheet 1, middle row); instinct / Pressure Response is now the **Legs**
> (triangle icon, sheet 2, first row). Card contents are unchanged; only the part name, the
> icon and the row header moved.

| Card | Name | Line 1 | Line 2 |
|---|---|---|---|
| 1 | Technical | "Your row on the Zone is" | "where the work happens." |
| 2 | Social | "Your row on the Zone is" | "where people talk while they work." |
| 3 | Commercial | "Your row on the Zone faces" | "outward, toward the customer." |
| 4 | Analytical | "Your row on the Zone is" | "where things get written down." |
| 5 | Organisational | "Your row on the Zone is" | "where the schedule lives." |

No mechanic lines or chips on this row - pure flavour. The row is your row on your SKILLS grid
(rulebook §8).

## TORSO row - "VALUES → HOW EVENTS LAND" · aside: "your Torso is also your Need, from week 2"

| Card | Name | Mono line 1 (chip, category tint) | Mono line 2 (chip, category tint) |
|---|---|---|---|
| 1 | Autonomy | `MANAGEMENT:` (chip on "MANAGEMENT", `#F7D7A1`) + wrapped `-1 MOTIVATION` (own chip, `#D3B1B1`) | `IMMUNE TO ENVIRONMENT` (chip on "ENVIRONMENT", `#C7CFB5`) |
| 2 | Hierarchy | `ENVIRONMENT:` (chip on "ENVIRONMENT", `#C7CFB5`) + wrapped `-1 MOTIVATION` (own chip, `#D3B1B1`) | `IMMUNE TO MANAGEMENT` (chip on "MANAGEMENT", `#F7D7A1`) |
| 3 | Community | `PEOPLE:` (chip on "PEOPLE", `#D3CEDF`) + wrapped `-1 MOTIVATION` (own chip, `#D3B1B1`) | `IMMUNE TO CUSTOMER` (chip on "CUSTOMER", `#B5C7CF`) |
| 4 | Quality | `CUSTOMER:` (chip on "CUSTOMER", `#B5C7CF`) + wrapped `-1 MOTIVATION` (own chip, `#D3B1B1`) | `IMMUNE TO PEOPLE` (chip on "PEOPLE", `#D3CEDF`) |
| 5 | Recognition | `SOMEONE GAINS CAPITAL:` (no chip, 2.8pt) + wrapped `NAME A TEAMMATE` (no chip) | `+1 MOTIVATION TO THEM` (chip on "+1 MOTIVATION", `#D3B1B1`) |

"-1 MOTIVATION" is never abbreviated - it now wraps onto its own line under the chipped
category label instead of being squeezed onto one line as "-1 MOTIV." (all four category
lines used to read that way; Community's used to spell the word out while the other three
abbreviated it - now all four spell it out the same way). Its wrap line now carries its own
`#D3B1B1` cost-chip (the same fill used for every Motivation cost elsewhere on this sheet),
distinct from the category-tint chip above it (e.g. People/Trust's `#D3CEDF`) - two
differently-coloured chips stacked on one card, each sized to fit its own line.

**Recognition payout widened (2026-10-11).** The trigger is now "someone gains Capital" (anyone, not only
the Recognition character): each Recognition character then names a teammate, who gains **+1 Motivation**.
The earlier version below fired only on their own gains.

**Recognition was emptied and rebuilt a third time.** It went through "EITHER WAY", then a
rejected "NEED MET: +1 CAPITAL", then a rejected "SEEN: +1 CAPITAL" (both smuggled in a
different rulebook section's rule), then a **witnessing exception** ("its own Capital gains
count even unwitnessed") - that version read backwards on inspection: a value called
Recognition should be the one that cares *most* about being seen, not the one that's exempt
from needing to be. It was also nearly unobservable at a physical table, where almost nothing
is ever unwitnessed. This version keeps the witness requirement **universal** (no exception
for anyone) and gives Recognition a payoff for it instead: whenever one of their own six
Capital triggers fires, witnessed as normal (§5.1), they **name the teammate who witnessed
it** - that teammate gains **+1 Motivation**. Recognition's whole disposition is that being
seen is relational - crediting the person who saw it is the one thing none of the other
Capital triggers ask for, and it's the one habitus built to do it anyway. Self-contained - it
only adds a payout on top of Recognition's own existing Capital gains; it changes nothing
about anyone else's Capital, the team average, or the Need/Motivation swap (§ "Motivation
depends on habitus") that already makes Recognition different in a separate, unrelated way.

## LEGS row - "INSTINCT · PRESSURE RESPONSE → STRENGTH, COST" · aside: "every part is a Hero trigger somewhere"

| Card | Name | Mono line 1 (category chip + wrapped amount chip) | Mono line 2 (category chip + wrapped amount chip) |
|---|---|---|---|
| 1 | Take Charge | `TRUST` (chip, `#D3CEDF`) `3 OR MORE:` + `+1 MOTIVATION` (chip, `#D3B1B1`) | `TRUST` (chip, `#D3CEDF`) `1 OR LESS:` + `-1 MOTIVATION` (chip, `#D3B1B1`) |
| 2 | Analyze | `CAPABILITY` (chip, `#C7CFB5`) `3 OR MORE:` + `+1 MOTIVATION` (chip, `#D3B1B1`) | `CAPABILITY` (chip, `#C7CFB5`) `1 OR LESS:` + `-1 MOTIVATION` (chip, `#D3B1B1`) |
| 3 | Support | `SHARED PRACTICE` (chip, `#F7D7A1`) `3 OR MORE:` + `+1 MOTIVATION` (chip, `#D3B1B1`) | `SHARED PRACTICE` (chip, `#F7D7A1`) `1 OR LESS:` + `-1 MOTIVATION` (chip, `#D3B1B1`) |
| 4 | Challenge | `ADAPTABILITY` (chip, `#B5C7CF`) `3 OR MORE:` + `+1 MOTIVATION` (chip, `#D3B1B1`) | `ADAPTABILITY` (chip, `#B5C7CF`) `1 OR LESS:` + `-1 MOTIVATION` (chip, `#D3B1B1`) |
| 5 | Engage | `FIRST 3 WEEKS:` + `+1 MOTIVATION` (chip, `#D3B1B1`) | `AFTER THAT:` + `-1 MOTIVATION` (chip, `#D3B1B1`) |

Every label line now carries its own category-tint chip on just the stat word (matching the
same People=Trust `#D3CEDF` / Environment=Capability `#C7CFB5` / Management=Shared Practice
`#F7D7A1` / Customer=Adaptability `#B5C7CF` canon used on the TORSO row), on top of the existing
`#D3B1B1` Motivation-cost chip on the wrapped amount line below it - two differently-coloured
chips per line-pair, same as TORSO. **Abbreviations reverted:** `CAPAB.` →
`CAPABILITY`, `SH.PRAC` → `SHARED PRACTICE`, `ADAPT.` → `ADAPTABILITY`, and every `MOTIV.` →
`MOTIVATION` - each label line now stands alone ("TRUST" with "3 OR MORE:" under it) with the signed amount on
the line below. This also fixes a real bug: Support's low line used to read `SH.PRAC 1 or less:
-1` with no unit at all (the rulebook's Support/Shared Practice row (§5.1) is "−1 Motivation -
it reads as hollow", same as every other Head) - it now reads `SHARED PRACTICE` / `1 OR LESS:` /
`-1 MOTIVATION` like its siblings.

**Engage (formerly Withdraw) was emptied (it used to be an exact duplicate of Analyze) and rebuilt from theory,
not guessed.** habitus-model.md's Bourdieu coverage table flagged exactly one unbuilt gap:
**Hysteresis** - "habitus is durable and slow, so when a field changes suddenly, dispositions
that used to pay off keep firing and now misfire." The doc's own proposed fix, THE GROUND
SHIFTS, was written as an Event card ("one named Head's strength no longer applies; its
tendency still does") but never built. Engage (formerly Withdraw) - an instinct tied to the project's own pace - is the natural home for it as a **self-contained** card effect instead of
a new Event: no category-tint chip (there's no Team State track called "week"), just the
week-number threshold in place of a track value, same **±1 MOTIVATION** payout shape as every
other Head. Early instinct pays off; the same instinct, unchanged, costs you once the field
(the project's own timeline) has moved on without it. habitus-model.md's coverage table now
marks Hysteresis ✅.

## ITEM row - "THE SKILL YOU HOLD → TEAM'S OVERTIME SLOT" · aside: "also the column you begin in on the Zone"

| Card | Name | Line 1 | Line 2 | Line 3 | Line 4 |
|---|---|---|---|---|---|
| 1 | Laptop | "Your Zone column is" | "built with this skill." | "Teach someone to hold it," | "and the column grows." |
| 2 | Coffee cup | "Your Zone column runs" | "on this skill." | "Teach someone to hold it," | "and the column grows." |
| 3 | Clipboard | "Your Zone column is" | "checked with this skill." | "Teach someone to hold it," | "and the column grows." |
| 4 | Wrench | "Your Zone column is" | "fixed with this skill." | "Teach someone to hold it," | "and the column grows." |
| 5 | Calendar | "Your Zone column is" | "scheduled with this skill." | "Teach someone to hold it," | "and the column grows." |

No mechanic lines or chips on this row - pure flavour.

## Sheet chrome (outside the five rows)

| Text | Class / size | Notes |
|---|---|---|
| "1 · HABITUS" | `.mono`, 6, ls 2 | sheet title, top-left |
| "Deal one card from each row, at random, and build the figure bottom to top. Nobody picks their upbringing." | `.serif` italic, 3.6 | top-left, under the title |
| "CUT ALONG THE GAPS · DEAL, DON'T CHOOSE" | `.mono`, 3, text-anchor end | top-right |
| Row header (e.g. "BASE · UPBRINGING → COST AND REPAYMENT") | `.mono.rl`, 3.3, ls 1.2 | left-aligned, one per row |
| Row-level aside (e.g. "your own Motivation, never Work") | `.serif` italic, 2.8, text-anchor end | right-aligned, same baseline as the row header |
| Card name (e.g. "Bookish") | `.serif`, 3.5 | not part of the "small font" bump - already readable |
| Mechanic/mono line | `.mono`, 2.6 | bumped from 2.0-2.1 |
| Flavour/serif body line | `.serif`, 2.6 | bumped from 2.1 |
| Footer line 1: "Same skill, different person: two characters can both hold the clipboard. One defers to the boss without thinking; one doesn't." | `.serif` italic, 3.2 | bottom, under the hairline rule at y=282 |
| Footer line 2: "That difference is the whole point - it is what the Torso and Legs are for." | `.serif` italic, 3.2 | bottom |

## Illustration

**Paint order per card:** border rect, name, hairline, then (mechanic template) chip-then-mono
pairs with the BASE row's two flavour lines sandwiched between them, or (flavour template) four
plain serif lines. Chips are always drawn **before** the text that sits on them. Every chip
highlights a specific word or phrase within its line (the changed keyword or the sign+number),
not the whole line - chip `x`/`width` are computed as `charsBeforeHighlight * fontSize * 0.6`
offset from the line's own text-start `x`, and `highlightedChars * fontSize * 0.6 + ~0.5mm`
padding for the width. These are approximate (mono character width varies slightly by glyph) -
verify against a real print and nudge a chip individually if it doesn't fully cover its word.

**Removing the hand-written aside** freed up the card's bottom margin rather than being
replaced by new content: TORSO and HEAD cards in particular now have a visibly larger blank
strip under their two mechanic lines (10-12mm) - that's intentional breathing room, not a bug;
don't feel obliged to fill it with more copy.

**Row Y-position summary** (all values absolute, add nothing - these already include the row's
own vertical offset): BASE row top=40, LEGS=90, TORSO=140, HEAD=190, ITEM=240; each row's
baselines are `top + the offsets listed in the per-template summary above`.

**Card X-positions** (literal, before each card's own cumulative `translate`): card 1 `x=14`
(text `x=17`), card 2 `x=50.5` (text `x=53.5`), card 3 `x=87` (text `x=90`), card 4 `x=123.5`
(text `x=126.5`), card 5 `x=160` (text `x=163`) - identical across all five rows.

## Layout diagram

```mermaid
graph TD
  A["page background #FFFFFF"] --> B["sheet header + rule"]
  B --> C["BASE row (5 cards, mechanic+flavour template, #F0E3D1)"]
  C --> D["HEAD row (5 cards, flavour-only template, #F0E3D1)"]
  D --> E["TORSO row (5 cards, mechanic template, category-tint chips, #F0E3D1)"]
  E --> F["LEGS row (5 cards, mechanic template, #F0E3D1)"]
  F --> G["ITEM row (5 cards, flavour-only template, #F0E3D1)"]
  G --> H["footer: 2-line closing note"]
  H --> I["icons layer: one shape+pip glyph per card, top-right"]
```

---

# NEED and HERO tiles (44x36mm, A4 landscape)

Source: `../cards-need-hero-44x36mm-A4-landscape.svg`
Page: 297x210mm - **true A4 landscape**, so it prints at 100% with no print-driver "fit to
page" auto-scaling. Card size 44x36mm, matching cards-habitus-parts, unchanged.

**Filename/history note:** this sheet used to be a 272x140mm custom page that fit neither A4
orientation, causing the same print-driver auto-scale bug as cards-habitus-parts - the tiles
no longer matched the person board's true 44x36mm seats. Fixed by enlarging the page to true
A4 landscape (no content needed to move; 10 tiles already fit well inside 297x210mm). The old
file (`cards-need-hero-44x36mm-A4-portrait.svg`) is deprecated in place with a redirect notice
and should be deleted from the folder.

Ten tiles: 5 NEED (mirrors Torso, one per value) + 5 HERO (mirrors Legs/Pressure Response, one
per option). HERO tiles use the same hexagon shape + pip-count code as the HOW TO ADAPT box on
Event cards, so a tile and its matching card show the same glyph.

## Grouping

| Row | 5 tiles | Shape used | Shared def |
|---|---|---|---|
| NEED | Autonomy(1 pip), Hierarchy(2), Community(3), Quality(4), Recognition(5) | `sh-torso-red` (filled red pentagon) | `p1`-`p5` pip glyphs, white `#FFFFFF` (`.pip`) for contrast on the `#905151` red |
| HERO | Take Charge(1), Analyze(2), Support(3), Engage (4), Challenge(5) | `sh-legs-red` (filled red triangle) | `p1`-`p5` pip glyphs, white `#FFFFFF` (`.pip`) for contrast on the `#905151` red |

All ten tiles are drawn inline (no `<defs>`/`<use>` for the card body itself, only the shape
and pip glyphs are shared defs). Each tile: `44x36`, `rx 1.5`, class `.cut` (`#F0E3D1` fill,
`#2A2620` stroke).

## Text

| Field | Class | Size | Colour | Background chip (hex) |
|---|---|---|---|---|
| Row header ("NEED · SAME 5 VALUES AS TORSO", "HERO · SAME 5 OPTIONS AS LEGS") | `.mono.rl` | 3.3 | `#000000` | - |
| Row-level italic hint | `.serif` | 2.8 | `#000000` | - |
| Tile name (e.g. "Autonomy", "Take Charge") | `.serif` | 3.5 | `#000000` | - |
| NEED condition (2-3 lines, centred) | `.serif` | 2.6 | `#000000` | - |
| NEED reward ("+1 Motivation.", own line, centred) | `.serif` | 2.6 | `#000000` | `#D3B1B1` |
| NEED row footnote ("FROM WEEK 2") | `.serif` italic | 2.8 | `#000000` | - |
| HERO threshold line ("NEEDS 3 MOTIVATION OR HIGHER") | `.mono` | 2.6 | `#000000` | - |
| HERO effect (2 lines, centred) | `.serif` | 2.6 | `#000000` | - |
| HERO payout (2 lines) | `.mono` | 2.6 | `#000000` | - |

Each NEED tile used to carry two visually different runs - a `.serif` condition (2 lines) and
a separate `.mono` "FROM WEEK 2: +1 MOTIVATION" reward line - with the week-2 timing repeated
five times. That's now one unified `.serif` 2.6 style throughout: the condition (2-3 lines)
followed by "+1 Motivation." on its own line with a `#D3B1B1` background chip (the standard
Motivation-reward tint used elsewhere on this sheet), and "FROM WEEK 2" moves out to a single
row-level footnote under the NEED row instead of repeating on every tile.

**Autonomy's Need was rebuilt after the 2026-09-25 playtest, and again when Activity cards became
the team's.** It used to read "Finished the week you planned, unreplaced", which only made sense
while Adapt could swap a laid card (rulebook v0.30), then "You executed at least one card". With
no executor the tile read "No Event landed on the team, or it has Shared Repertoire"; simulation
(2000 games) showed that left Autonomy characters quitting at 1.6-1.9 times the average, since two
Events are drawn every week from week 2. It now reads **"At most 1 Event landed on the team, or it
has Shared Repertoire: +1
Motivation."** Every Need tile except Recognition now ends with its vindicating Habit as an
alternative (Hierarchy: Who Knows What, Community: Psychological Safety, Quality: Team
Reflexivity), replacing Community's old "Trust is 4+".
(rulebook.md, "Need gives bonus Motivation"). Hierarchy reads "Team played a Teach, or team has
Who Knows What" and Recognition "A feature was banked this week, or you spent Hero".
**The condition text sits on a tint (2026-10-07)**, a rounded rect behind the condition lines
(38 mm wide, `rx` .4) in the colour of the Event category that gets to that Torso (rulebook §5):
Autonomy `#F7D7A1` (Management), Hierarchy `#C7CFB5` (Environment), Community `#D3CEDF` (People),
Quality `#B5C7CF` (Customer; the "No Work added to feature:" line sits on the Work colour `#EFE4D3`), Recognition `#D9D3C4` (no category; the
Capital chip tint). The "+1 Motivation" chip stays `#D3B1B1`.
**Tile headlines (2026-10-07):** all ten tiles now carry the headline `NEED` or `HERO` (`.mono` 3.4,
letter-spacing 1, x+3, y 47 / 97). The value name (Autonomy... / Take Charge...) stays as a small
italic serif 3 caption, right-aligned at x+33, so a tile can still be matched to its Torso or Legs card.

**Quality's Need was rebuilt after the 2026-09-25 playtest.** It first dropped its "or a feature
cleared Unclear" clause (Unclear went to the `feature-quality-uncertainty` extension, rulebook
v0.21), leaving "The team spent an Align." Players then spent weeks 1-3 on everything but Work,
so the Need now reads **"Work added to a feature this week: +1 Motivation. No Work added to feature: -1
Motivation."** (two lines each with a `#D3B1B1` chip; rulebook.md, "Need gives bonus
Motivation"). It counts Work that really moved a feature's counter, not just a Work card laid
down. It is the only Need that can cost you.

**Text sizes were raised after the 2026-09-25 playtest ("still too small").** On the habitus
sheets mono is now 3.0 and serif body 3.2 (was 2.6 for both); on the NEED and HERO tiles serif is
3.2 and mono 3.0. Copy was re-wrapped and shortened to fit (Item and Legs cards lost a line,
Dependable lost its second flavour line, HERO tiles read "NEEDS 3+ MOTIVATION" and "+1
MOTIVATION TO A TEAMMATE" over two lines). Chip rectangles were re-measured at 1.8 mm per mono
character. Any size in this file that still says 2.6 is the old value.

**Recognition drops "successful" from its Demo clause** - Demo is now an unconditional success
(no hidden Quality roll, same v0.21 change), so qualifying it as "successful" is redundant:
**"A feature you Worked banked, or you led a Demo: +1 Motivation."**

Every HERO tile has **identical mechanics** ("NEEDS 3 MOTIVATION OR HIGHER", "Once per game:
cancel an Event card.", "+2 CAPITAL TO YOU, +1 MOTIVATION TO A TEAM MATE") - only the name and
shape/pip-count differ. This is intentional: HERO's power is choosing *which* Event it can
cancel (whichever names that part), not a mechanical difference between the five. The one
exception lives on a different card: a **Competitive** Base makes its owner's Hero reusable
("HERO IS REUSABLE", Base row above), and every reuse still needs 3 Motivation. The sheet's
subtitle states this ("once per game (a Competitive Base: every time)"); the tiles themselves
stay generic.

## Illustration

Each tile places its shape glyph (`sh-torso-red` or `sh-legs-red`) with a matching pip glyph
(`<use href="#p1".."p5">`) at the tile's top-right corner (offset `x=39/89/139/189/239, y=6`
relative to each tile's own origin) - **the pip count must always match the row position** (1st
tile = 1 pip, 5th = 5 pips) since this is the code Event cards use to point at a HERO option.
Layout is two rows of 5, each tile 44mm wide with a 6mm gap (14, 64, 114, 164, 214 for NEED;
same x positions at y=90 for HERO).

## Layout diagram

```mermaid
graph TD
  A["page background #FFFFFF"] --> B["sheet header + rule"]
  B --> C["NEED row: 5 tiles (sh-torso-red + pips 1-5)"]
  C --> D["HERO row: 5 tiles (sh-legs-red + pips 1-5)"]
  D --> E["closing note: deal both at random with habitus deck"]
```

---

# Project cards (88x88mm, A4)

Source: `../cards-project-63x88mm-A4-portrait.svg`
Page: 210x297mm portrait · card size **88x88mm** (deliberately not 63x88 - see below), text
starts x=5, right edge x=83

Six sectors (Healthcare, Finance, Software, Retail, Construction, Events), each naming features
A-F with the same slot structure - only names/flavour change. Chosen once at setup, dropped
into board 1's 90x90 Project seat, never shuffled with the other decks.

## Grouping

| `<g id>` (in `<defs>`) | Contents | Background (hex) |
|---|---|---|
| `frame` | shared skeleton: 88x88 border, "PROJECT" label, roman-numeral circle (top right), header rule (y=29), footer rule (y=81) | none, `.c` outline only |

Each project is its own `<g transform="translate(x,y)">` instance re-using `<use href="#frame"/>`
plus its own text - not a `<defs>` id, since each is placed exactly once (no repeats).

## Text

| Project | Numeral | Sector tag | Features A-F (name · complexity/gate · cost) | Footer italic |
|---|---|---|---|---|
| I - Patient Portal | I | HEALTH | Appointment reminders·LOW·3; Patient login·MEDIUM·BASE·4; Medical records API·MEDIUM·BASE·4; Referral network SSO·HIGH·NEEDS B·3; Consent form capture·LOW·2; Billing history·HIGH·NEEDS C·2 | "No identity, no chart to open." |
| II - Loan Platform | II | FINANCE | Branch locator·LOW·3; Account ledger·MEDIUM·BASE·4; Application intake·MEDIUM·BASE·4; Real-time balance sync·HIGH·NEEDS B·3; Statement PDFs·LOW·2; Credit scoring·HIGH·NEEDS C·2 | "No ledger, nothing to reconcile." |
| III - Excel Workflow | III | SOFTWARE (tongue-in-cheek) | Screenshot → spec·LOW·3; Decode the macros·MEDIUM·BASE·4; Guess the data model·MEDIUM·BASE·4; The "fixes it" button·HIGH·NEEDS B·3; Rename all the tabs·LOW·2; Reconcile the finals·HIGH·NEEDS C·2 | "Not even the customer can explain the macro." |
| IV - Mobile App | IV | RETAIL | App store listing·LOW·3; Offline sync engine·MEDIUM·BASE·4; Push notification service·MEDIUM·BASE·4; Sync conflict resolution·HIGH·NEEDS B·3; Accessibility pass·LOW·2; Rich notification actions·HIGH·NEEDS C·2 | "No sync engine, nothing to send notifications about." |
| V - Home Renovation | V | CONSTRUCTION | Permit application·LOW·3; Framing and foundation·MEDIUM·BASE·4; Plumbing and electrical rough-in·MEDIUM·BASE·4; Drywall and interior finishing·HIGH·NEEDS B·3; Landscaping·LOW·2; Fixture installation·HIGH·NEEDS C·2 | "No frame, nothing to finish." |
| VI - The Wedding | VI | EVENTS | Guest list and invitations·LOW·3; Venue booking·MEDIUM·BASE·4; Catering contract·MEDIUM·BASE·4; Seating chart and table layout·HIGH·NEEDS B·3; Music playlist·LOW·2; Final headcount and catering order·HIGH·NEEDS C·2 | "No venue booked, nowhere to seat anyone." |

Sheet placement (2 columns x 3 rows, each card `translate(x,y)`): I (10,14), II (102,14); III
(10,106), IV (102,106); V (10,198), VI (102,198).

All six share the identical Work-cost profile (3,4,4,3,2,2) and gate structure (D needs B, F
needs C) - only sector, names and flavour text change, by design (see the file's own `<desc>`).

## Illustration

Each card reuses the shared `frame` (border + PROJECT label + numeral circle + two rules)
via `<use>`, then adds its own six feature lines between the rules - one `<text>` per column
(letter, name, complexity/gate tag, cost number right-aligned) rather than per-feature groups,
since there's no per-feature icon here (unlike board 1's feature rows). Gated rows (D needs B,
F needs C) print their complexity tag in plain black without the `.q` grey, functioning as a
"pay attention" cue consistent with board 1's red-bordered gated rows - though here it's a
colour-weight cue, not a coloured border (the card has no room for a full red outline). Sheet
is a 2-column x 3-row grid of these 88x88 cards with 2mm gaps.

## Layout diagram

```mermaid
graph TD
  A["88x88 border (frame)"] --> B["PROJECT label + roman numeral circle"]
  B --> C["rule at y=29"]
  C --> D["title (2 lines) + sector tag"]
  D --> E["6 feature rows: letter, name, complexity/gate, cost"]
  E --> F["rule at y=81"]
  F --> G["footer italic line"]
```
