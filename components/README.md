# Components

v0.1 prototype - keep it ugly first: index cards, paper, cubes, sticky notes, printed
feature blocks, simple tracks. Don't spend time on graphic design until the mechanics are
fun - see [../rules/rulebook.md](../rules/rulebook.md) §19.

When graphic design does start, it follows [../docs/design-guide.md](../docs/design-guide.md)
("The Field Study" - corporate objects in scholarly materials, three typographic voices, earthy
palette for the team and accent colours for what happens *to* them).

## Editing a print sheet: specs drive the SVG

Every `*.svg` in this folder has a matching Markdown spec in [specs/](./specs/README.md) -
grouping, background colours, text, and the illustration, one file per SVG. **Edit the spec,
then ask for the SVG to be updated to match, then push** - see the
[board-game-component-specs skill](../../.github/skills/board-game-component-specs/SKILL.md)
for the full workflow and template.

| Component | Quantity | Material / method | Status |
|---|---|---|---|
| Character/player board | 1 per player | Printed board with figure socket + 5 Motivation wells | To design |
| Habitus miniature (modular: base/legs/torso/head/item) | 1 per character | 3D print, see `3d-models/` | Concept locked - see `../docs/habitus-model.md` |
| Habitus cards/tiles (Base, Legs, Torso, Head, Item options) | 1 deck | Printed cards | To design |
| Project cards | 6 | Printed cards - six themed projects over one identical slot structure, §20 | Written in rulebook §20 |
| **Activity cards** | 16 per sheet (9 designs) | **The week's five slots are filled from these** - print sheet in `print-5-activities.svg` | Drawn |
| **Flex markers** | 6 | Taken on Overtime; a day the project owes. Placed **into a weekday slot** to give the day back, or −5 Team Score each if never repaid (§7) | **Off-the-shelf token, not printed** |
| Character discs | 1 per player | Small coloured disc placed on an Activity card to say who takes that day | **Off-the-shelf token, not printed** |
| **Feature Tower blocks** | 6 | **3D print, wood-fill PLA - hex, height proportional to Work Cost. D and F have cone/wedge bottoms and can only stand on B and C** | Spec'd in `3d-models/` |
| Feature Work cubes | 6 | One cube walking each feature's track on the Project Rack | **Off-the-shelf cube, not printed** |
| **Quality chips** | 6 | **3D print - same blank body across all tiers, engraved reveal face** | Spec'd in `3d-models/` |
| **Unclear flag** | 1 | Placed on a feature's flag seat when UNCLEAR REQUIREMENT (or similar) flags it; lifted when Align/Demo/Meet clears it (§10) | **Off-the-shelf token, not printed** |
| Lock tiles | 2 | Physically cover features D and F until B / C bank | To design |
| **Habit coins** | 5 | **3D print, resin - double-sided 14 mm coins, one per Ledger row. Track marker on one face, the acquired Habit on the other (§18)** | Spec'd in `3d-models/` |
| Week board | 1 | 5 weekday slots + the 1-7 ladder to the deadline | On the main board |
| Event Deck | ~30 cards | Printed cards; 2 drawn per week | Drafted in rulebook §11 |
| **Motivation tokens** | 25 (5 per character × 5 characters) | Domed discs seating into player-board wells | **Off-the-shelf token, not printed** - fallback print spec in `3d-models/` |
| Knowledge cards | Per character | Cards, copied to whoever you teach | To design |
| Team State tracks (Trust, Capability, Shared Practice, Adaptability, Standing) | 1 board | The Ledger, on the main board | To design |

See `3d-models/` for anything that will be 3D printed.

---

## Print sheets

**Office-printer set.** White ground, line art, no solid fills - cheap on toner and legible on
a bad laser. Print at 100%, no scaling, no "fit to page." **The paper format is in every
filename.**

## The four shared boards

Four boards, each printed **front and back and glued to one piece of cardboard**. For boards
1-3 the back is that week's rules and the front is that week's board; all three start **text
side up**, and at the start of each week you **turn one over** - the rule arrives in the same
gesture that uncovers the board. That is §3.0's staged reveal as a physical object rather than
a paragraph. **Board 4 (the Zone) never flips** - its grid is live from week 1. What it pays
off (Learn/Teach, and what the Ledger reads off the grid) doesn't exist before week 3, so that
content isn't on board 4 at all - it lives on a separate insert, **sheet 4b**, which sits face
down beside board 4 from setup and turns over at the start of week 3, alongside the Ledger.
Board 4's own back still carries no rule reveal; it exists only so the board glues to cardboard
the same way the others do, and so it can carry the table-placement guide too.

**A3 is the ceiling, not the target.** Each board is only as big as its content needs.

| Board | Paper | Front | Back |
|---|---|---|---|
| **1** | **A3 landscape** | `board-1-FRONT-week-and-project-A3-landscape.svg` | `board-1-BACK-week-1-the-week-A3-landscape.svg` |
| **2** | A4 portrait | `board-2-FRONT-reality-A4-portrait.svg` | `board-2-BACK-week-2-reality-A4-portrait.svg` |
| **3** | A4 landscape | `board-3-FRONT-the-team-A4-landscape.svg` | `board-3-BACK-week-3-the-team-A4-landscape.svg` |
| **4** | A4 landscape | `board-4-FRONT-the-zone-A4-landscape.svg` | `board-4-BACK-the-zone-A4-landscape.svg` - never flips during play |
| **4b** | A4 landscape, both faces on one page | `board-4b-the-zone-payoff-127x104mm-A4-landscape.svg` (Face A) | same file (Face B) - waits face down until week 3 |

Only board 1 needs A3 - it carries five 65 × 90 card slots, six features and the tower
plinth. Boards 2, 3 and 4 fit A4 comfortably and printing them larger would only cost paper.

**Gluing.** Front and back of a board are always the *same paper size and orientation*, so one
cardboard rectangle takes both. **Flip about the long edge** - like turning a page, not like
turning a steering wheel - and both faces read the right way up. Trim the cardboard flush after
both sides are down, not before: paper creeps a millimetre when it is wet with glue.

## Per-player components - print one set per player

| Print | Paper | What it is |
|---|---|---|
| `board-person-170x141mm-A4-portrait` | A4 **landscape** (filename now stale - was 170x114mm portrait, now 244x128mm landscape so the habitus seats could be true 44x36mm, matching the printed part-cards) | **The person board.** One per sheet, one per player - Capital+Motivation+Zone Start share a row, Need+Hero+Flex share the row below |

**Week 3 has no shared board, and shouldn't.** Its reveal is the bottom panel of your own
person board - always physically there, but only worth reading from week 3 on. A light dashed
rule marks where it starts, so nobody is asked to care about it before the week that needs it.

## Cards and leaflets - A4, print at 100%

| Print | Paper | Used from | What it is |
|---|---|---|---|
| `cards-activity-63x88mm-A4-portrait` | A4 | Week 1 | Nine Activity cards - Work x3, Coordinate x2, Align x2, Celebrate x2. **Print once** |
| `cards-activity-5b-63x88mm-A4-portrait` | A4 | Week 1/3 | The other nine - Work x2 (five total), Teach x2, Plan, Demo, Reflect, Meet, Learn. **Print once** |
| `cards-event-01-09-63x88mm-A4-portrait` | A4 | Week 2 | Event cards 1-9 |
| `cards-event-10-18-63x88mm-A4-portrait` | A4 | Week 2 | Event cards 10-18 |
| `cards-event-19-21-63x88mm-A4-portrait` | A4, one row used | Week 2 | Event cards 19-21 (THE BIKESHED, LEADS FROM BEHIND, THE DASHBOARD). Shuffle all three sheets into one 21-card deck |
| `cards-project-63x88mm-A4-portrait` | A4 | Setup | Six projects. Choose one; it drops into the seat on board 1 |
| `cards-habitus-parts-01-15-44x36mm-A4-landscape` + `cards-habitus-parts-16-25-44x36mm-A4-landscape` | True A4 landscape (297 x 210 mm), split across two sheets so the 5-per-row cards print at true 44 x 36 mm, matching the person board's seats exactly - the board is master | Setup | 25 part-cards (15 + 10), dealt at random |
| `cards-need-hero-44x36mm-A4-landscape` | True A4 landscape (297 x 210 mm) - the board is master, same fix as the habitus part-cards | Setup | 10 tiles: 5 NEED (= Torso, one per value) + 5 HERO (= Head, one per Pressure Response) - HERO tiles use the same shape/pip-count code as the HOW TO ADAPT box on Event cards |
| `specs/leaflet-how-to-play.md` | A4 | - | Setup, Week 1, the weekly pulse from week 2 on, and how it ends - plain printable Markdown, not an SVG. Paginated into `game-print-all.pdf` by `scripts/build_print_pdf.py`, or print the Markdown directly |

**Everything that goes in a weekday slot is 63 × 88 mm** - Activity and Event cards alike - so
the two decks handle identically and either fits any 65 × 90 seat. **The Project card is the
exception**: 88 × 88 mm, into its own 90 × 90 seat, because it's read once at setup and left in
place all game - it never needs to shuffle with the other two decks. **Never scale a card
sheet**: the boards' slots are cut to these exact millimetres.

**The Specimen panel** lives on the bottom of the merged person board now: Capital, Need and
Flex. It's live from week 3 (§3.0) - the week the game admits the project has been landing on
people, not just on the team.

**The Hero box** sits *above the week-4 panel* on the player board, because Hero is live from
week 2 when
Events start. Cover the small dashed box when it is spent. It requires **3 Motivation or more** - a threshold, not a cost - which is what makes Celebrate strategic rather than merely a way to
stop people quitting.

**Three ways out of an Event.** Every card prints the same **HOW TO ADAPT** block. The first
line spends the team's re-planning budget, joined by an "or" to **HERO**, which names one
habitus part and is free, once per game, for +2 Capital and +1 Motivation to somebody else -
this was built around **sixteen** Base / Legs / Head / Item parts (four per row) naming
exactly one Event each, and **four** Torso parts on every card as the suffers/ignores
reaction. **HABIT** names the acquired Ledger Habit for that card's category; holding it takes
**1 off the Adaptability cost**, so an ADAPT-1 card stops happening at all.

**Now stale:** Base, Legs, Head, Item and Torso are all five-per-row (twenty-five parts total)
- the printed Event cards still only name the original sixteen/four, so the five newest parts
(Base's Corporate, Legs' Organisational, Head's Challenge, Item's Calendar, Torso's Recognition)
have no Hero trigger yet. Needs a pass across `cards-event-01-09` and `cards-event-10-18`
before this paragraph is true again.

**The cover plates.** Three pieces of cardboard hide the parts of the board that aren't in play
yet (§3.0). Each one carries its reveal card on the *underside*, so the rule arrives in the same
gesture that uncovers the board - nobody is read a subsystem before the week they need it.
Plate 2 covers sheet 2, plate 3 covers the Ledger, plate 4 covers the Standing row. The
Specimen panel along the bottom of each player board isn't a cover plate either - it's printed
there from setup and simply isn't read until week 3 (a light dashed rule marks where it
starts). Sheet 4b isn't a cover plate - it's a
separate two-faced insert (see the boards table, above) that turns over on its own at week 3.

### Two rules the sheets obey

**Cards are 63 × 88 mm - a standard playing card** - and the weekday slots on sheet 1 are
65 × 90, so a card drops in with 1 mm of play on each side. Sleeve them and they still fit.
Activities and Events are the same size, so the two decks shuffle and stack alike. **The
Project card breaks this on purpose** (88 × 88 mm, its own 90 × 90 seat) - see
`cards-project-63x88mm-A4-portrait.svg`'s own note for why; the filename is stale, the card
isn't 63 × 88 any more.

**The board is added to, never covered.** Sheet 1 is the whole of week 1. Sheets 2 and 3 go
down together at week 2, the week-3 panel at the bottom of every player board at week 3. That
is cheaper than printing cover
panels, it means nothing is wasted, and the table visibly grows as the game does.

### Production intent - flip-plates

In the finished game the staged reveal is **double-sided cardboard plates seated in recesses on
one board**, not separate sheets. Each plate is printed:

- **Face up at setup:** almost nothing - the region's name and **"FLIP AFTER WEEK 3"**.
- **Face down (revealed):** the actual Ledger / Reality / Standing artwork, registered to line
  up with the board around it.

Better than loose sheets for three reasons: the board footprint never changes, so the table
doesn't have to be re-tidied mid-game; nothing can be lost between sessions; and *flipping* is
a more satisfying physical act than laying down a new piece of paper - it makes the reveal feel
like something turning over rather than something being fetched.

**Requirements this puts on the board:** each plate needs a shallow recess so it seats flush
and doesn't slide, and the revealed face must be registered to the surrounding artwork within
about a millimetre. Plate thickness ~2 mm greyboard. The print sheets above are the prototype
stand-in for exactly this.

> **The print sheets and the plates carry the same content.** Prototype with paper; only cut
> plates once the reveal schedule has survived a playtest, because a wrongly-staged plate is
> expensive and a wrongly-staged sheet is a reprint.

> **Superseded** (delete when you're happy with the new set): `board-study-wall.svg`,
> `board-allocation-desk.svg`, `board-player.svg`, `print-2-ledger.svg`, `print-4-cards.svg`,
> `print-5-activities.svg`, `print-6-cover-panels.svg`.
>
> `board-player.svg` is superseded **and broken** - its Motivation panel (y 94-142) and Specimen
> card (y 96-144) are drawn on top of each other, so it cannot be printed as-is. Replaced by
> `sheet-8-player-board-A4.svg`.

## Board layout

**Editable artwork:**
[board-study-wall.svg](./board-study-wall.svg) - the whole board, 620 × 440 mm ·
[board-allocation-desk.svg](./board-allocation-desk.svg) - Activity card print sheet, A4 ·
[board-player.svg](./board-player.svg) - player board, 220 × 150 mm

Open them in VS Code's preview or any browser; edit in Inkscape, Illustrator or Figma, or
straight as text. **1 SVG unit = 1 mm**, so they're at print scale - every recess and well
matches the tolerances in [3d-models/](./3d-models/README.md). Colours and type follow the
[design guide](../docs/design-guide.md).

**One board, three regions.**

- **The Ledger** (left) - five rows of six identical wells, **one coin each**. Walk the coin as
  the track moves; at the ringed well, **turn it over** - the reverse face is the **Habit**
  (§18). The coin can walk back down; it never turns back over. One component carries the whole
  rule: the position is what you *have*, the face is what you've *become*. The fifth row is
  *Standing* (highest Capital at the table), which drives Authorized Voice.
- **The Project** (right) - the Project card on its plinth, the **tower footprint** beside it,
  and the **six features** below. Card, delivered stack and work-in-progress all in one
  region, because they're the same subject. The tower needs nothing but its 32 × 32 mm plinth;
  the stack itself is the component.
- **The Working Week** (bottom) - reads **left to right as the turn**: the week ladder counting
  down to **DEADLINE** → `1 · PLAN THE WEEK` (five shared day slots, Monday - Friday, each with a
  disc socket for *who* takes it) → `2 · SHIT HAPPENS` (which holds the Event deck and discard - they belong to that moment) → `3 · ADAPT` → `CLOSE THE WEEK`. A new player can be taught
  the whole turn by pointing along the strip.

> **Five days, not five per player.** The week belongs to the team. Three players or six, it's
> still five cards - so the board is the same at any player count. A character disc under each
> card says who takes that day.

### Nothing is ever written on
Not on the board, not on the player boards, not anywhere. Every value is a **token in a well,
a marker on a track, a card in a seat, or a tile in a slot**. This forces the whole game state
to be physical and readable across the table, and it means components survive a hundred plays
without a single pencil mark.

| Was going to be written | Is now |
|---|---|
| Character name | Nothing - **the assembled figure is the character**. Player boards are printed with a specimen numeral. |
| Base / Legs / Torso / Head / Item | Five **part-card seats** under the figure socket |
| What a character knows | **Squares covered on the shared Zone board** (board 4) - no private card |
| Need | **The Torso card itself**, read a second way from week 3 - no separate card |
| Feature names | The **Project card** on its plinth names all six (§20) |
| Work progress | A **cube walks the track** in each feature's track to a green target disc |
| Quality | A **face-down chip**, turned over by a Demo |
| Dependency | A **LOCK tile** across features D and F - lifted off when B / C bank. And the blocks themselves: D and F have no flat bottom, so they physically cannot be placed until their parent is on the tower. |
| The week's plan | Five **Activity cards** - or a **Flex marker** - in the weekday slots |
| Who takes a day | A **character disc** under the card |

Four things are physical 3D objects, and each needs a **designed seat** - a recess, plinth or
socket - not just a printed square to balance on. Loose objects slide, get knocked, and read as
an afterthought. Seated objects read as deliberate, and they hold the "specimen tray" feeling
the [design guide](../docs/design-guide.md) is after.

```
┌────────────────────────────────────────────────────────────────┐
│  THE LEDGER                    │  THE PROJECT                  │
│  Trust      ○○●○⓪○  Psych.     │  ┌────────┐   ┌────────────┐  │
│  Capability ○○●○⓪○  Full       │  │ PROJECT│   │ □ plinth   │  │
│  Sh.Prac.   ○○●○⓪○  Shared     │  │ CARD   │   │ (tower)    │  │
│  Adapt.     ○○●○⓪○  Battle     │  └────────┘   └────────────┘  │
│  Standing   ○○●○○⓪  Trusted    │  A ○○● 3 □    D ○○● 3 █LOCK█  │
│             ↑ coin walks       │  B ○○○● 4 □   E ○● 2 □        │
│             ⓪ flip here        │  C ○○○● 4 □   F ○● 2 █LOCK█   │
├────────────────────────────────┴───────────────────────────────┤
│ WEEK 1..7 │ MON TUE WED THU FRI │ SHIT   │ADAPT│ CLOSE THE WEEK│
│ ↓DEADLINE │  □   □   □   □   □  │ HAPPENS│     │ grind −1      │
│           │  who ○ under each   │ +deck  │     │ slack +2      │
└────────────────────────────────────────────────────────────────┘
```

- **The Ledger's wells are all the same size** - 14.6 mm, because the same coin walks the whole
  row. At the ringed well you flip it in place.
- **Feature Tower plinth** - the board owes the tower nothing but a 32 × 32 mm footprint with a
  lip. The stack itself is the component.
- **Motivation wells - five sockets, not a pile.** A pile has to be counted; five wells with
  gaps can be read across the table at a glance. Everyone can see who's running out, which is
  exactly the information the group needs when deciding whether to spend a day on Celebrate.
- **Habitus figure socket** - a shallow recess matching the Base footprint, so the figure
  stands upright and *belongs* to that player rather than wandering the table.

---

## Open proposal - give the Tower a rule (fixes M3)

The [assessment](../docs/playability-assessment.md) flags (M3) that the Feature Tower is
decorative: blocks stack, but nothing about the stack matters. The physical design suggests a
fix that costs one line:

> **Blocks are stacked in the order features were banked. If an Event knocks a banked feature
> back off, you must physically dismantle everything above it to get it out.**

Rework stops being a number on a counter and becomes an actual, annoying, public act of taking
your delivered work apart. It also means the tower is a readable timeline of the project.

**Not applied** - it's a rules change, and it should be tested for whether the fiddliness is
worth the drama.

