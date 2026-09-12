# 3D models

Drop STL/3MF/STEP files here, one subfolder per component.

For each printable part, write down next to the file:
- Which process it assumes (FDM or resin/SLA)
- Which way it's printed, and whether it needs supports
- The minimum wall thickness used
- Any tight-fit clearance used, in mm

## Habitus miniature (the main piece)
The core piece is a **modular office-worker miniature** built from five interchangeable
parts, matching the habitus model in
[../../docs/habitus-model.md](../../docs/habitus-model.md):

| Part | Represents | Interchange point |
|---|---|---|
| Base | Upbringing/background | Peg/socket into legs |
| Legs | Education & inclination | Socket into torso |
| Torso (arms sculpted in) | Values | Socket for head; molded hand slot for item |
| Head | Perception / Pressure Response | Swappable head, its own expression or pose per response |
| Item | Skill (capability) | Small prop that pegs into the torso's molded hand |

Goal: you should be able to glance at another player's miniature and read their
Base/Legs/Torso/Head/Item straight away - not have to check a card.

### Every variant needs its name engraved on the part

Each part type has **4 named variants - 20 sculpts total** at full scope, matching
[print-1-habitus.svg](../print-1-habitus.svg). **Phase 1 (this round): 2 of the 4 per part - 10 sculpts.** The other 2 per part are Phase 2, added once Phase 1 has been printed and
handled. Which 2 ship first is an arbitrary placeholder below - swap freely.

| Part | Phase 1 (now) | Phase 2 (later) |
|---|---|---|
| Base | Academic · Trade | Entrepreneurial · Public sector |
| Legs | Technical · Social | Commercial · Analytical |
| Torso | Autonomy · Hierarchy | Community · Quality |
| Head | Take Charge · Analyze | Support · Withdraw |
| Item | Laptop · Clipboard | Coffee cup · Wrench |

With up to 20 variants at full scope, silhouette alone won't stay readable across the table - **every part must have its own name engraved (recessed) into the sculpt**, same convention as
the Habit coins and Quality chips (recessed, never raised text). This applies from Phase 1 - don't defer the engraving just because the variant count is smaller for now.

### Print notes (fill in once modeled)
- **Process:** FDM for the first prototype set - cheaper, faster to iterate. Consider
  resin/SLA later for a polished set where the face and props need more detail.
- **Interchange:** peg-and-socket between each part, with a clearance tolerance so parts
  swap easily by hand without being loose. Start around 0.15-0.2 mm clearance per side on
  FDM and adjust from there. Arms are sculpted into the Torso, not a separate part - a thin
  arm pegged at the shoulder is fragile and snaps easily. A small Item prop shows capability
  just as well, without that risk.
- **Orientation/supports:** check each part once it's modeled. The Head's expression and the
  Item's shape are the most likely to need supports, or a redesign that avoids them. Keep
  the Item's peg short and thick so it doesn't snap.
- **Scale:** use one peg/socket size across every Base/Legs/Torso/Head/Item variant, so any
  combination fits together - that's the whole point of the piece.

## Other printable components

Three more parts are physical 3D objects, each with a designed seat on a board - see the board
layout in [../README.md](../README.md). Specs below are the intended "as-built" record; confirm
and correct them against the first real print.

### Feature Tower blocks (×6)

The centrepiece. **Block height is proportional to the feature's Work Cost**, so the finished
tower's *height* physically shows how much was delivered, not just how many features. At
7 mm per Work:

| Feature | Work Cost | Block height |
|---|---|---|
| A | 3 | 21 mm |
| B | 4 | 28 mm |
| C | 4 | 28 mm |
| D | 3 | 21 mm |
| E | 2 | 14 mm |
| F | 2 | 14 mm |
| | | **126 mm** full tower |

- **Process:** FDM in **wood-fill PLA.** The [design guide](../../docs/design-guide.md) calls
  for unfinished or oiled hardwood; wood-fill sands to a genuinely woody finish and smells
  right. ⚠️ It needs a **0.5-0.6 mm nozzle** - the fibres block 0.4 mm - and is mildly
  abrasive, so use a hardened nozzle.
- **Footprint:** **hexagonal, 40 mm across flats**, identical on every block so any stacking
  order is stable. Hexagons read better than squares on the table, seat into the plinth at any
  of six rotations, and don't need aligning.
- **Stacking joint (A and E, the plain blocks):** 6 mm dia × 3 mm boss on the top face;
  6.3 mm dia × 3.4 mm recess in the underside. **0.15 mm clearance per side.**
- **Orientation:** flat face on the bed, boss pointing up. **No supports** - the recess ceiling
  is a 6.3 mm bridge, trivial for FDM.
- **Min wall:** 2 mm. Infill 15%. Layer 0.2 mm.
- **Letter engraving:** each block has its feature letter (**A - F**) engraved (recessed, never
  raised) on a visible side face, same convention as the Habit coins and Quality chips - so a
  block is identifiable on sight, on or off the tower.
- **Seat:** a **hexagonal recess 46 mm across flats, 2 mm deep** in the Project region of the
  board - 3 mm clearance per side, with a lip so a 126 mm stack can't be knocked over. Sized
  generously on purpose: the tower is the one component people reach for while looking
  somewhere else.

### The dependency, built into the geometry

D depends on B and F depends on C - and that shouldn't only live on a lock tile. **D and F have
no flat bottom. They cannot stand on the plinth, on the table, or on any other block.** They
seat into a cradle that exists on exactly one other piece.

| Block | Bottom | Top |
|---|---|---|
| **A, E** | flat + 6.3 mm socket | flat + 6 mm boss |
| **B** | flat + 6.3 mm socket | **conical dish, 28 mm dia × 5 mm deep**, centred (no boss) |
| **D** | **cone, 28 mm dia × 5 mm tall, 60° included** | flat + 6 mm boss |
| **C** | flat + 6.3 mm socket | **V-groove, 34 mm corner-to-corner × 8 mm deep** (no boss) |
| **F** | **matching keel, 34 mm × 8 mm, 60° wedge** | flat + 6 mm boss |

**The cradles nest, so they add no height.** D's cone sinks fully into B's dish; F's keel fills
C's groove. A finished tower is still exactly `total Work × 7 mm` tall, and the height gauge
stays honest.

**Round vs. linear is the key.** D is a cone, F is a wedge, and they don't cross-fit: a cone
dropped in C's V-groove slides along it and tips whatever sits above; a keel laid in B's round
dish contacts at two points and rocks. Neither is *impossible* to balance for a second, but
neither will hold a tower - which is the right kind of enforcement for a tabletop game. It
corrects itself, loudly, without anyone having to be the rules police.

> **What this buys.** The finished tower is no longer just a height - it's a **record of what
> was built on what**. D sitting in B's dish is visible from across the room. And a team that
> banks D's prerequisite late can see the consequence physically: a wedge-bottomed block
> sitting on the table beside the tower, unable to go anywhere.

**Print notes for the four shaped blocks:**
- **B** - dish up. A concave bowl prints clean, no supports.
- **C** - groove up. The V opens upward so both walls slope outward; no supports.
- **D** - **print inverted**, cone pointing up, flat top on the bed. A 60° cone is
  self-supporting.
- **F** - **print inverted**, keel pointing up. Same 60° rule.

**If you want it hard-blocked** rather than merely unstable, add peg keying: **two** 4 mm pegs
20 mm apart in B's dish (two sockets in D's cone), and **three** 4 mm pegs in a 14 mm triangle
in C's groove (three sockets in F's keel). No pair in the triangle is 20 mm apart, so neither
child can seat on the wrong parent at all. Costs four extra features to model; only worth it if
a playtest shows people actually trying to cheat the stack.

### Habit coins (×5) - one per Ledger row

**Double-sided, and they do two jobs.** The coin is the track marker *and* the Habit (§18): walk
it along the six wells as the track moves, and turn it over when it reaches the ringed well.
The coin can walk back down afterwards; it never turns back over.

- **One generic coin body, modeled once, reused for all 5.** Same blank disc for every row - only the engraved text differs between the 5 copies. No need for 5 separate body sculpts.
- **Front = the Track face, back = the Habit face.** **Track face (front, unacquired):** the
  track's name and the threshold. **Habit face (back, acquired):** the Habit - *Psychological
  Safety*, *Who Knows What*, *Shared Repertoire*, *Team Reflexivity*, *Authorized Voice*.
- **Text is engraved (recessed) on both faces, on every coin - never embossed.** Recessed text
  prints cleanly on a top surface at this size and takes an ink wash better than raised text
  would.
- **Process:** **resin/SLA** for the final set - small parts with sharp engraved text on both
  faces are exactly what resin is for. For an FDM prototype, print each face separately
  (engraved face up, so it prints clean) and glue the two halves back-to-back, or use a
  mid-print filament change.
- **Size:** **14 mm dia × 3 mm** - sized to the Ledger wells, not to a display shelf. Every
  well on the board is the same diameter so the coin drops into any of them.
- **Orientation:** FDM - flat, no supports, one face per print, engraved face up. Resin - tilt
  ~20° with supports on the rim only, never on an engraved face.
- **Min wall:** 1.5 mm.
- **Seat:** every Ledger well is **14.6 mm dia × 2 mm deep** - **0.3 mm clearance per side**, and
  shallow enough to flip a coin in place with a fingernail. That last point matters: the flip
  happens *on the track*, not in a separate shelf.

### Quality chips (×6) - one per feature

**Face-down until a Demo reveals it** (rulebook §10): Low / Medium / High, one chip per feature,
placed face-down when Standing arrives in Week 4.

- **All three tiers are identical, full stop** - same geometry, same body colour, same blank
  reverse face. Tier is never encoded in the shape or colour of the body, only in the printed
  reveal face. Pick a chip up face-down and there is no way to tell which tier it is.
- **Reveal face: engraved (recessed), never embossed** - pips (● / ●● / ●●●) or the word
  Low/Medium/High, matching the Habit coins' engraving convention.
- **Process:** FDM prototype - one filament colour for all six chips regardless of tier;
  engrave the reveal face, blank face down on the bed (flat, no supports). Resin for the final
  set - same reveal-face-up engraving rule as the Habit coins.
- **Size:** 16 mm dia × 3 mm - one size step up from the 14 mm Habit coin/Motivation token so it
  doesn't get confused with either by feel alone.
- **Min wall:** 1.5 mm.
- **Seat:** a dashed-circle placement mark now sits in every feature slot on
  [board-1-FRONT-week-and-project-A3-landscape.svg](../board-1-FRONT-week-and-project-A3-landscape.svg),
  but it's a print guide, not a physical recess yet. Needs a **16.6 mm dia × 2 mm** well cut at
  that mark per feature, 0.3 mm clearance per side, matching the Ledger wells, before this is
  printed.

### Simple generic tokens - off-the-shelf for now

No unique geometry or engraving on any of these - buy a generic part instead of modeling one:

| Component | Off-the-shelf option |
|---|---|
| Motivation tokens | 14 mm gem/token, ochre or clear-ochre |
| Flex markers | Small disc or cube in a 6th colour, distinct from the character discs |
| Character discs | Small coloured disc/pawn, 1 per player |
| Feature Work cubes | Plain 10-12 mm wooden or acrylic cube, 1 per feature |

The fallback spec below (Motivation tokens) is kept in case the right size/finish can't be
sourced off-the-shelf later - not currently being printed.

### Motivation tokens (Quantity: 25-5 per character × 5 characters) - fallback spec, not currently printed

- **Process:** FDM, ochre filament (the [design guide](../../docs/design-guide.md) assigns
  Ochre `#C08A3E` to Motivation).
- **Size:** 14 mm dia × 5 mm, with a **2 mm domed top** so they lift out of a well easily.
  Flat discs in a recess are miserable to pick up.
- **Orientation:** flat, dome up. **No supports** - a 2 mm crown over 14 mm is a shallow enough
  curve to print unsupported.
- **Seat:** five 14.4 mm dia × 3 mm wells in a row on each **player** board, not the main
  board. **0.2 mm clearance per side.**
- **Why wells and not a pile:** a pile has to be counted; five wells with gaps can be read
  across the table instantly. Everyone can see who's running out of Motivation, which is the
  information the team needs to decide whether Rest is worth a person-day.

### Habitus figure socket
A shallow recess on the player board matching the **Base** part's footprint, +0.3 mm per side.
Keeps the figure upright and anchored to its owner.

---

## Outsourcing brief (Fiverr) - bespoke parts only

Only the parts with unique geometry or per-part engraving are worth paying a modeler for.
Generic tokens (above) are bought off-the-shelf instead. Priority order:

1. **Habitus miniature** - **Phase 1: 10 sculpts** (2 each of Base/Legs/Torso/Head/Item, see
   table above), peg-and-socket interchange common to all variants, each part's name engraved
   into the sculpt. Phase 2 adds the remaining 10 later. The core piece and the most complex
   modeling job - highest priority.
2. **Feature Tower blocks (×6)** - hex-footprint blocks with interlocking cradle geometry
   (cone/dish on B - D, wedge/groove on C - F), wood-fill PLA.
3. **Habit coins (×5)** - individually modeled, double-sided engraved text on every coin.
4. **Quality chips (×6)** - shared blank body across all tiers, engraved reveal face. Simpler
   than the above - lower priority.
5. **Lock tiles (×2)** - lowest priority; may not need a paid modeler at all.

Each numbered item above already has a full spec in this file (process, orientation, supports,
tolerances) - link or paste the relevant section into the job listing rather than re-describing
it from scratch.

### Fiverr job post (copy-paste)

**Title:** 3D modeling for a modular tabletop miniature + interlocking game pieces (editable CAD + STL)

**Category:** 3D Modeling & Design > Game Assets / Miniatures

**Description:**

> I'm making a board game prototype and need help designing three sets of small 3D-printable
> pieces. I don't need anything printed or shipped, just the design files.
>
> **1. Two sets of modular little figurine in 5 parts. Think of a simple office-worker.**
> (10 pieces total):
> - 1a. Two Bases should look clearly different from the other Base
> - 1b. Two different sets of legs
> - 1c. Two different torsos. Arms can be part of the torso, no separate arm pieces please
> - 1d. Two different heads
> - 1e. Two different items
>
> Every part should plug into the next, so any Base fits any Legs, any Legs fit any Torso, and
> so on. Each piece needs its name carved into the surface, or raised up. I'll send you the 10
> names.
>
> **2. Six blocks that stack into a little tower:**
> - 2a. A hexagon base that can hold 2b, 2c and 2d
> - 2b. A something that fits on top of 2a
> - 2c. A shape on top of 2a with room for a spear (2e)
> - 2d. A shape on top of 2a that can hold 2f
> - 2e. A spear that only fits in 2c
> - 2f. A ball like thing that only fits on 2d
>
> Each block also needs a letter (A - F, I'll tell you which one goes where) carved into a side
> face, same as the figure parts.
>
> **Style for the tower pieces:** bare, unpainted wood look - no printing, no colour, no
> labels beyond the carved letter. Closest reference: unpainted geometric wooden
> building-block sets - plain, precision-fit, no branding. The fit itself should work like a
> basic shape-sorter toy: the spear (2e) only sits in 2c, the ball (2f) only sits on 2d - the
> wrong piece should simply not go in, no instructions needed to enforce it.
>
> **3. One generic coin, engraved 5 different ways.** Same blank double-sided coin body,
> modeled once - only the text changes between the 5 copies. Each coin shows a track name on
> the front (the Track face) and a different word on the back (the Habit face), revealed by
> flipping it over later. All text carved into the coin, on both sides. The five front/back
> pairs:
> - Trust → Psychological Safety
> - Capability → Who Knows What
> - Shared Practice → Shared Repertoire
> - Adaptability → Team Reflexivity
> - Standing → Authorized Voice
>
> **What I need delivered, for every piece:**
> The file you made it in (we will keep adding more pieces over time)
> A ready-to-print STL and 3MF.
>
> **Measurements:**
> Figure (Part 1): roughly 25-35 mm tall once stacked. Peg-and-socket joints need a small gap,
> about 0.15-0.2 mm, so parts fit snugly but aren't glued stuck.
> Tower blocks (Part 2): 40 mm across each hexagon.
> Coins (Part 3): 14 mm across, about 3 mm thick.

**Attachments to prepare before posting:** export the relevant sections of this file
([3d-models/README.md](.)) - the Habitus table + Print notes, and the Feature Tower blocks +
"The dependency, built into the geometry" sections - as a PDF or plain-text spec sheet.

**Rough price estimate** (typical Fiverr range, varies a lot by seller level - get 3-4 quotes
and compare rather than pre-committing): Part 1 figures $25-50/piece (**$250-500** for 10) - Part 2 tower blocks $15-30/piece (**$90-180** for 6) - Part 3 coins: one body ($15-25) + 5
text variants ($5-10 each) (**$40-75** total). **Total ~$380-755 (roughly €350-695 at ~0.92
USD/EUR - set a hard budget cap around €700 and treat quotes above that as needing
negotiation, not a like-for-like comparison).**

## Print order

Don't print any of this yet. The mechanics aren't proven - see the
[playability assessment](../../docs/playability-assessment.md), Stage 10. Cardboard, coins and
sticky notes until a table has played it. The whole advantage of printing is that a redesign
costs a file edit; that advantage disappears if you print before the numbers are real.

