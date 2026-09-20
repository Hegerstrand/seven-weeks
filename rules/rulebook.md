# Rulebook - High-Performance Team (v0.27 draft)

Status: prototype draft, not yet playtested. Bump this version header whenever a playtest
changes a rule, and log the change in [../playtests/README.md](../playtests/README.md).

> **v0.27 - Capability and Adaptability can now fall.** Audit found Trust (`split`, `audit`,
> `CONFLICT`) and Shared Practice (`reorg`) each had at least one Event that moved their Ledger
> coin down, but Capability and Adaptability had none - two of four tracks only ever rose. Added
> two new Event cards (21\u219223 total): **SHAKY GROUND** (Environment, −1 Capability) and
> **ALWAYS REACTING** (Customer, −1 Adaptability). Both name the track directly in the effect
> line, distinct from the Torso reaction's personal Motivation loss underneath - per §18, this
> is the coin moving down, permanent until re-earned, never a one-week effect. Each card's HABIT
> is deliberately the one that track itself unlocks (Who Knows What / Team Reflexivity).

> **v0.26 - Item's axis renamed TOOL → SKILL.** Cosmetic, no rule change: every printed and
> written reference to the Item/Zone-column axis ("TOOL") now reads "SKILL" - the Zone board's
> column header, the Item habitus cards, the person board's caption, and this rulebook's own
> build-order and Zone (§8) text. Unrelated uses of the word "tool" (Vygotsky's "mediation by
> tools", the Internal Tools product parody, TOOLING OUTAGE) are untouched - they aren't this
> axis.

> **v0.25 - Take One For The Team.** A player asked for a Base habitus card that traded
> Motivation for Trust - refused as a habitus card (§5.2 confines Base to the character's own
> Motivation, never a shared track; see [../docs/habitus-model.md](../docs/habitus-model.md)'s
> "never two currencies" rule), but the underlying want was real: a way to nudge Trust in a week
> the team couldn't spare a Coordinate or Meet. Added as a new **standing action** (§7, alongside
> Overtime, not a card): any character may pay 1 Motivation for the week's +1 Trust, if Trust
> hasn't already risen that week. Shares Trust's existing "rises 1 a week, max" ceiling - it's an
> alternate route to that same point, spending Motivation instead of a card slot, never a stack.

> **v0.24 - Strict renamed to By The Book; habitus card wording cleanup.** The Strict card's
> two mechanic lines didn't hang together on the printed card ("the other" had no visible
> antecedent once "IGNORE 1 EVENT LOSS/WEEK" was trimmed to fit) and its flavour text read as
> generic. Renamed to **By The Book** (same rule, unchanged) and rewrote its card copy from
> scratch; Competitive's "-1 EXTRA" line now spells out what the extra is (Motivation), and
> every habitus part-card abbreviation (`MOTIV.`, `CAPAB.`, `SH.PRAC`, `ADAPT.`) was reverted to
> the full word, wrapped onto an extra line where it didn't fit - card-copy only, no rule change.

> **v0.23 - Performance Review cleanup.** v0.22 said Performance Review and Authorized Voice's
> Collective Bargaining use were extracted to `game/extensions/performance-review/`, but left
> the old dual-use wording sitting in §5.1's Losing Capital list and in the Habit discount
> table - both still described Authorized Voice shielding a Performance Review, contradicting
> "Authorized Voice now only cancels an Event." Removed; the extension's own README already
> carries the full restored mechanic.

> **v0.22 - Balance pass on the Event/Adapt escape valves.** Performance Review and
> Authorized Voice's Collective Bargaining use are extracted to `game/extensions/performance-review/`
> - Authorized Voice now only cancels an Event. A Habit always costs 1 less to cancel an Event,
> never fully removes it (minimum 1, was minimum 0). Every Event card's ADAPT cost below 3 is
> raised by 1 (four ADAPT-1 cards -> ADAPT-2, nine ADAPT-2 cards -> ADAPT-3). Motivation cost
> widened from 4 to 8 Event cards (added EQUIPMENT OUTAGE, THE TEAM SPLITS, EVERYTHING AT ONCE,
> THE AUDIT), to keep Motivation pressure real even as more Events get cancelled.
>
> **v0.21 - Feature Quality & Unclear extracted to an extension pack.** First playtest finding:
> too complicated. The Project feature system's hidden Quality (Low/Medium/High) attribute and
> the Unclear flag are cut from the base game - see `game/extensions/feature-quality-uncertainty/`.
> Align simplifies to unconditional +1 Adaptability; Demo keeps its Capital-gate and
> standing-concentration mechanic (§5.1) but is now an unconditional success (no hidden Quality
> roll); SURPRISE AUDIT and UNCLEAR REQUIREMENT move to the extension's Event deck. The Quality
> Torso's Need condition is simplified; its Strength/Tendency habitus pair and Vindication
> trigger have **no base-game replacement yet** - flagged as an open design gap in the
> extension's README.
>
> **v0.20 - Replacement replaces NEW TEAM MEMBER, and Brooks's Law gets a mechanic back.**
> Onboarding (§12) no longer waits on a random Event draw - it now triggers automatically and
> expensively whenever a character quits or is fired (§13): the seat sits empty for the rest
> of that week, then the replacement pays the usual 2-day onboarding cost with no shortcut.
> This also closes playability-assessment.md's M7 (Onboarding could go a whole game unseen).
> The freed Event card slot (was NEW TEAM MEMBER) now carries **REINFORCEMENTS ARRIVE**,
> giving Brooks's Law its first mechanic since the absorption cap was removed in v0.19 - see
> [Designer's Notes](../docs/04-designers-notes.md).

> **v0.19 - Both Work caps removed.** The per-feature "2 Work days a week" cap (§10) and the
> weekly output ceiling (§7) are both gone. If the team wants to pour every day into Work, they
> can - nothing is wasted just for landing on an already-busy feature, and stacked bonuses on
> one card are no longer capped. **The consequence moves from a rule to an opportunity cost:**
> every day on Work is a day not spent building Trust, Capability, Adaptability or Motivation,
> and a team with no Shared Practice already makes its 2nd+ Work card *worse*, not blocked
> (§4) - diminishing returns instead of a hard wall. This removes the last mechanical grounding
> **Brooks's Law** had in the game - see [Designer's Notes](../docs/04-designers-notes.md) for
> the honest accounting. The 55%-of-budget derivation in §3.2 is now flagged stale rather than
> silently wrong; nobody has re-derived it against an uncapped week yet.

> **v0.18 - Five-level documentation structure.** This document is now **Level 2 - the
> Rulebook** in a five-level reading order (Level 0 Overview, Level 1 Learn to Play, Level 2
> this document, Level 3 Rules Reference, Level 4 Designer's Notes) - see
> [../README.md](../README.md#reading-order). No rule changed. The Appendix moved out to its
> own Level 4 document, [Designer's Notes](../docs/04-designers-notes.md), and the full
> gameplay content here is now also indexed in [Rules Reference](../docs/03-rules-reference.md)
> for lookup. This document keeps its job: teach the game in playable order, start to finish.

> **v0.17 - Fixed a real contradiction in v0.16.** Saying Learn and Teach both get "up, down,
> left or right" directly contradicted Learn's own "in your own row" restriction - Learn can
> never actually move up/down, since that would leave the row. Split it correctly: **Learn is
> left/right only** (confined to your own row), **Teach is all four directions** (it can cross
> into any row, handing you a square you couldn't have reached alone). Board 4's LEARN/TEACH
> text and shared footnote rewritten to state this per-Activity instead of as one blanket rule.

> **v0.16 - Zone adjacency made explicitly the Zone of Proximal Development.** §8's "must touch one you already cover" was
> ambiguous about diagonals. Learn and Teach now require **orthogonal** adjacency only
> (up/down/left/right) - Vygotsky's zone of proximal development made physical: one step from
> what you can already do, never a diagonal leap. Board 4's "HOW YOU COVER" footnote updated
> to match. Also fixed board 3b's Capital highlight, which was sitting over the wrong word.

> **v0.15 - New Management Event: THE BARNUM EFFECT.** +1 Motivation to everyone, but no
> Trust/Capability/Shared Practice - a vague "personality profile" that feels personally true
> without the team having actually learned anything real about itself. §11's Management
> backlog is now 9 deep.

> **v0.14 - Complexity needed a real job back in Plan.** v0.13's flat +1-for-everyone fix
> stopped the exploit but made Medium and High identical under Plan - Complexity stopped
> mattering there at all. Restored a genuine High edge **without** reopening the one-card
> payoff: the per-card bonus stays flat at +1 (never big enough to outrun a feature's Work
> Cost alone), but **on a High-complexity feature the bonus now also applies the following
> week**. That rewards Complexity on the same axis it already costs on - High already takes a
> bigger rework hit from Events (§10) - so a hard feature that was Planned keeps paying off for
> as long as it's likely to still be open, instead of in one lump sum. Board 1's D/F callouts
> updated to "2 weeks." Still needs a playtest: does the 2-week window actually get used, or do
> most High features get finished or reworked before week 2 makes it matter?

> **v0.13 - Plan's High bonus was letting a feature finish too cheap.** D (Work Cost 3, High)
> could be fully banked in **2 days** (1 Plan + 1 Work, at +2 extra) against a 7-week/35-day
> project - way out of proportion. §7's Plan effect is now a flat **+1 extra per Work card**
> on Medium *and* High (still nothing on Low), matching the "roughly doubles" prose that the
> old +2-extra table entry already contradicted. Board 1's D/F callouts updated to match.
> Needs a playtest to confirm Plan is still worth taking on High features at the flat rate.

> **v0.12 - Two more Management Events.** **MANDATORY FUN (OFFSITE)** removes a card but
> raises Motivation anyway - the corporate ritual is bullshit *and* the free catering is
> nice, both at once. **PERFORMANCE REVIEW SEASON** neuters a Reflect into paperwork, no
> Adaptability or Shared Practice - bureaucracy standing in for genuine reflection. §11's
> Management backlog is now 8 deep, still short of the ~30-card target.

> **v0.11 - Software project reskinned to The Excel Workflow.** No mechanical change - Work
> Costs, Complexity and gates in §20 are untouched. Replaces Internal Tools (auth/CLI/SSO
> jokes about a team building for itself) with a client engagement joke instead: a customer who
> hands over a spreadsheet and can't explain it. B is reverse-engineering the macros, C is
> guessing the data model nobody wrote down, D automates "the button that fixes it," F
> reconciles three conflicting "final" sheets.

> **v0.10 - Corporate jargon purged outside the Event deck.** The game speaks plainly
> everywhere except Management-category Events, which are the one place the world is allowed
> to talk *at* the team like that (\u00a711 now says so explicitly). §7/§9's **Alignment
> Meeting** and **Status Meeting** Activity options are renamed **Working Meeting** and
> **Record Meeting** - same effects, same satire (a team can choose the ritual over the real
> thing), just without borrowing the Event deck's own vocabulary. Two new Management Events
> added for the deck, played straight-up corporate on purpose: **CORPORATE BUZZWORD BINGO**
> and **A NEW AI INITIATIVE**.

> **v0.9 - Sheltered, simplified.** Tying Sheltered to Celebrate timing needed a whole
> explainer paragraph just to say what it did - a bad sign for a five-word card. **Now it's
> two always-on lines, no conditions:** the weekly grind (§5) never touches your Motivation,
> and you never hold more than **3 Motivation** - the normal cap of 5 doesn't apply to you.
> Same trade as before (immune to the low, capped below the high), stated flat instead of
> riding on when Celebrate gets played. Log the first table's read on it in
> [../playtests/README.md](../playtests/README.md).

> **v0.8 - Project cards reskinned to three sectors.** No mechanical change - Work Costs,
> Complexity and gates in §20 are untouched. Healthcare (Patient Portal) and Finance (Loan
> Platform) are played straight; **Software (Internal Tools) is deliberately tongue-in-cheek** -
> the field study's wink at its own kind of team (auth rewritten a fourth time, SSO fronting the
> SSO, a CLI destined for a Rust rewrite). Replaces the old Customer Portal / Warehouse System /
> Migration flavour.

> **v0.7 - Unstable retired, Sheltered takes the slot.** Unstable's "gains and losses both hit
> harder" was a wash dressed up as a mechanic - it didn't give a team anything to actually
> decide, so it's gone. **Sheltered** replaces it: skip the weekly Motivation grind outright on
> any week the team plays Celebrate, but your own Celebrate is capped at +2 and never pays the
> +3 banked bonus. Same shape as every other Base option - a strength and a tendency, both on
> your own Motivation (§5.2) - but built around Celebrate and the weekly grind instead of
> Learn/Teach, so it doesn't overlap with Bookish or Hands-On. Log the first table's read on it
> in [../playtests/README.md](../playtests/README.md).

> **v0.6 - Base moved off Work entirely.** Two rounds of patching (v0.4's tendency, v0.5's
> Weekly Focus) were both attempts to make a Work-based Base bonus mean something, and both
> needed another rule bolted on just to make the tendency bite. **Base doesn't touch Work any
> more.** It governs a character's own **Motivation** (§5.2) instead - gains and losses on
> Learn, Teach, Overtime and Hero, nothing shared, nothing feature-shaped, nothing that a team
> can route around by working in parallel. Because patching Base's Work coupling was **Weekly
> Focus's only reason to exist, v0.5 is reverted**: Work can once again land on any feature,
> capped at 2 Work days per feature per week (§10), and phase 1 of the weekly turn no longer names
> a Focus (§6.1). This is a design correction made before any full-rulebook playtest; log the
> first table's read on Base in [../playtests/README.md](../playtests/README.md).

> **v0.5 - the team works on a feature, not on all of them.** v0.4 gave Base a tendency to
> pair with its strength, but that alone didn't fix anything: with every feature open to Work
> at once (§10's old "2 Work days per feature" cap, spread across up to three features a week), a team
> could always park its badly-fitted character on whichever feature they weren't penalised on,
> in parallel with everyone else. The tendency never actually fired. **Fixed at the root:** the
> team now names one **Focus** feature when it lays the week (§6.1), and Work cards can only
> ever target that one feature (§10). There is no "parallel" left to hide in - if the team
> needs Work done this week, it happens on the Focus, whoever that suits or doesn't. This is a
> design correction made before any full-rulebook playtest; it very likely changes how tight
> the 18-Work / 35-day budget (§3.2) actually is, and that needs re-deriving against real play,
> not assumed - log it in [../playtests/README.md](../playtests/README.md).

> **v0.4 - Base pays for itself.** Bookish, Hands-On and Competitive (§5.2, and the printed
> [habitus part-cards](../components/cards-habitus-parts-01-15-44x36mm-A4-landscape.svg)) were flat
> "+1 Work on two features" bonuses with no cost - a naked exception to the game's own design
> rule (never a flat bonus; see [habitus-model.md](../docs/habitus-model.md)) and, in practice,
> pointless: with no restriction on who works which feature, the team would simply always route
> that character's Work to their bonus features, so the +1 was guaranteed rather than a choice.
> Every Base option now pairs its strength with a tendency, the same pattern already used for
> Head - see the updated table below and the part-cards. This is a design correction made
> before any full-rulebook playtest, not a playtest-verified fix; log the first table's read on
> it in [../playtests/README.md](../playtests/README.md).

> **v0.3 - the week is five team-days.** The turn is the week, and the week is **five Activity
> cards for the whole team** - not five per player. Three players or six, the week is still
> five days, so the game doesn't change shape with the player count (§6.0). The five slots are
> a **set, not a sequence**: the week happens at once and resolution order never matters, which
> is why Adapt buys you *different cards*, not a reshuffle (§6.1).
>
> **All five blocking defects from the
> [playability assessment](../docs/playability-assessment.md) are closed:** the currency is
> settled (§6.0), every Activity has an exact number (§7), Capital converts in and its gate is
> relative to the team average (§5.1), and the work economy is bounded and derived - output
> capped at *Work cards + 2, +1 per Habit* (§7), features absorb 2 Work days a week (§10), Work
> totals **18** against a **35-day** budget (§3.2).
>
> The design models to the skill curve in [concept.md](../docs/concept.md): **~5% random,
> ~50% competent, ~95% perfect.** **Every number here is derived, not observed.** Play
> [rulebook-lite.md](./rulebook-lite.md) first and don't tune anything until a table has
> played it.

## 1. Overview
The game opens with every player physically building their character's habitus, out of five
parts - Base, Legs, Torso, Head, Item - before a single project rule gets explained (§3.1;
see [../docs/habitus-model.md](../docs/habitus-model.md)). Only then do you become a team
delivering a project with a fixed feature set, inside **7 weeks / 35 working days**. Every
day the team decides freely how to spend its time - no weekday spot has a fixed ritual or
effect (see §7 Activities). The goal is simple to say and hard to do well: **build the
project's features** (§3.2) before Day 35, without wrecking the team along the way. Your
choices change both the project's progress and the team's own state, shaped throughout by
the habitus you built at the start.

## 2. Components (v0.1 prototype)
- Character boards/cards (Name, Habitus, Skills, Knowledge, Motivation, Role, Capital/influence - see §5.1)
- Habitus cards/tiles (used at character creation)
- Feature Tower (completed features only - a feature is placed here once its Work counter
  reaches its Work Cost; see §10)
- Feature Work counters (a small track or token pile per feature, off the tower, tracking
  accumulated Work toward its Work Cost)
- Week board (5 weekday slots, Monday - Friday - where the week's five Activity cards are laid
  before Events are drawn, see §6.1)
- Week counter (1-7 - one turn per week)
- Event Deck (~30 cards for v0.1; 2 drawn per week)
- Motivation tokens (per character)
- Knowledge/Skill markers (individual and shared)
- Team State tracks: Trust, Capability, Shared Practice, Adaptability (scale 0-5)

## 3. Setup

### 3.0 The staged first game
A full board is a wall. So the game opens with most of it **covered**, and uncovers itself one
idea at a time. Nobody is taught a subsystem before the week they need it.

| From | What opens | Cards in play |
|---|---|---|
| **Week 1** | **The week.** The week strip and the six features. Your figure, your Knowledge, your Motivation. | Work · Coordinate · Celebrate |
| **Week 2** | **The team, and reality.** The Ledger - Trust, Capability, Shared Practice, Adaptability, and the Habits - and Shit Happens and Adapt, together. Adapt equals **[Adaptability]** from the first day it exists - no separate training-wheels stage. | + nothing new |
| **Week 3** | **Board 4b, then the person.** HOW YOU COVER / THE LEDGER READS THIS lift (plate 3b) - the Zone's grid was already live, this is just where it starts paying off - and the Specimen card: Capital, Need, Overtime and Flex. | + Learn · Align · Reflect · Meet · Plan · Demo |
| **Week 4** | **Standing.** The fifth Ledger track (plate 3b) - whoever holds the most Capital becomes the team's Standing. | + nothing new |

Weeks 5-7 are the whole game with nothing new opening, and by then the table has met
every rule *at the moment it mattered* rather than in a twenty-minute briefing.

**One idea per week, and each one is a sentence.** Week 1: a week is five days and you choose
them. Week 2: it was never only the project - it was landing on the team, and your plan was
made in ignorance, both at once. Week 3: and on you personally.

**Week 1 is deliberately almost trivial:** lay five cards, resolve them, close the
week. That's the entire lesson. A first-timer makes a real decision inside five minutes of
sitting down, which is the only onboarding that reliably works.

#### Weeks 2, 3 and 4 are reveals, and they're staged as reveals
For a week the table has played cards and watched only the features move. Make the
consequence *shown* rather than announced. Keep every card played so far face-up in a pile, and
when you uncover each panel, run its catch-up:

> **Week 2 - the team.** Move Trust up **1 for every two Coordinate cards** the team has
> played. Everything else starts where it always was, at 2.
>
> **Week 3 - the person.** Give each character **1 Capital for every two cards they played**
> in weeks 1-2, to a maximum of 2.
>
> **Week 4 - standing.** No catch-up to run - just reveal 3b and compare: whoever holds the
> most Capital right now is Standing.

Two small adjustments and one comparison, no hidden bookkeeping - and between them the
difference between being told these things matter and *seeing* that they were counting the
whole time.

Nothing has been lost by starting small. Everything sat at its starting value whether it was
visible or not. Week 2 doesn't *start* Trust; it starts you paying attention to it.

> **Playing with people who know the game?** Uncover everything at setup and deal the habitus
> as a draft (§3.1). The staged version costs about two weeks of depth; the full version costs
> about twenty minutes of teaching. Pick whichever the table can afford.

### 3.1 Build your habitus - this is how the game starts
Each player is **dealt five parts at random**, one from each row of
[the habitus deck](../components/cards-habitus-parts-01-15-44x36mm-A4-landscape.svg) (sheet 1 of 2;
Head and Item are on [sheet 2](../components/cards-habitus-parts-16-25-44x36mm-A4-landscape.svg)) - Base, Legs,
Torso, Head, Item - and physically assembles them into their figure, bottom to top, before a
single project rule is explained.

**You are dealt your habitus, not asked to choose it.** That is the point, and it's the more
honest reading of the theory: nobody selects their upbringing, their schooling, or what they do
by instinct when the pressure comes on. You are handed a person and you play them. It also
removes five decisions per player from a table that doesn't yet know what any of the words
mean - the single biggest setup cost in the game.

You still do the building. That matters and it stays: assembling something that becomes visibly
*yours* is what gets a newcomer's hands on the game before their head is ready, and it takes
about ninety seconds.

1. **Base** - upbringing. Nothing attaches to it; it's the foundation.
2. **Legs** - education & inclination, attached to the Base.
3. **Torso** - values, attached to the Legs. (Arms are sculpted in, not swappable.)
4. **Head** - pressure response, attached to the Torso.
5. **Item** - the skill you hold, into the Torso's hand.

Slot the five part-cards into your player board as you go. Nothing is written down. Then take
the matching [NEED and HERO tiles](../components/cards-need-hero-44x36mm-A4-landscape.svg) -
the one that names your Torso value, and the one that names your Head - and slot those too.
(Your **Need** is your **Torso**, read a second way - it just isn't *asked about* until week 3,
with the Specimen panel - §3.0. Weeks 1-2 are about who you are and what you know; what you
*need* from the team is the week-3 idea, and the tile that answers it has been on your board
the whole time.)

The build order - upbringing → education → values → instinct → skill - is on purpose: it mirrors
how a habitus actually forms, oldest layer first.

> **Variant, for players who know the game:** deal each player seven parts and let them keep
> five, one per row. You get the drafting decision back without the paralysis, because by then
> the words mean something.


### 3.2 Create the project
**Pick a Project card** (§20) - or deal one at random. Every project has the same six
feature slots, the same Work Costs, the same Complexity and the same dependencies; only the
names change. Nothing about the choice affects balance, so pick whichever one the table finds
funniest or most familiar.

What it *does* affect is whether the team can hold the project in its head. "We can't ship
self-service billing until the account API is done" is a sentence people reason with. "F
depends on C" is a lookup.

v0.1 prototype: 6 features, each with a Work Cost, a Complexity, and - for two of them - a
Dependency, meaning a feature that must be placed on the Tower first (§10).

   | Feature | Work Cost | Complexity | Depends on |
   |---|---|---|---|
   | A | 3 | Low | - |
   | B | 4 | Medium | - |
   | C | 4 | Medium | - |
   | D | 3 | High | B |
   | E | 2 | Low | - |
   | F | 2 | High | C |

   Total required work: **18**, against a budget of **35 days** (§6.0). Not every day produces
   direct work - that gap is the central strategic tension.

   These numbers are derived. Events destroy roughly 6 days across the project, leaving
   **29 usable**; at the bounded output rate of ~1.4 Work per Work day (§7), 18 base Work plus
   ~4 Event rework costs about **16 days - 55% of the usable budget**, leaving 13 for Celebrate
   and
   everything that makes the team better. They sit at the conservative end of the 55-65% band
   on purpose.

   > **Stale since §7's output cap was removed.** The ~1.4 Work/day rate above assumed the old
   > weekly output ceiling; there is no ceiling any more, so a well-invested team's real rate is
   > unknown until it's actually played. Log what an uncapped week does to this math in
   > [../playtests/README.md](../playtests/README.md) before trusting the 55% figure.

   Only **5 of the 18 Work (28%)** sits behind a dependency gate. Gated features unlock once
   their prerequisite (B or C) is banked (§3.2), so front-loading the Work is what keeps the
   endgame winnable - see B5 in the
   [playability assessment](../docs/playability-assessment.md).

### 3.3 Starting values
1. Set every character's starting **Motivation to 3** (scale 0-5).
2. Set all four **Team State** tracks to a neutral starting value (v0.1: 2 or 3 out of 5 - tune this in playtest).

## 4. Team State
Four tracks, each 0-5, describing the team rather than any one person.

| Track | Low | High |
|---|---|---|
| **Trust** | People hesitate to challenge each other; sharing knowledge is harder; mistakes get hidden. | People challenge ideas; problems surface earlier; learning is faster. |
| **Capability** | The team can't get much done together, no matter how skilled each person is. | Work is more efficient - this grows through learning, cross-training, experience, shared knowledge. |
| **Shared Practice** | No common language, routines, or patterns. | Familiar work goes faster - shared language, routines, procedures, mental models. |
| **Adaptability** | The team struggles to respond to change. | Changing requirements, surprise events, and staff changes hurt less. |

**These four interact - don't just try to max them all:**
- High Trust + high Capability → team members can genuinely help each other.
- High Capability + high Shared Practice → very efficient, but only at *familiar* work.
- High Shared Practice + low Adaptability → **risk of becoming rigid.**
- Low Trust + strong individual experts → **knowledge gets stuck in individuals.**
- High Adaptability + low Shared Practice → can handle change, but may be inefficient.

**Every track has a live, always-on effect.** These apply in ordinary play, not just when an
Event happens:

| Track | At 4-5 | At 0-1 |
|---|---|---|
| **Trust** | Once per week, cancel one Event effect completely. | **Learn does nothing.** Knowledge won't move through a team that doesn't trust each other. |
| **Capability** | Work produces **+1**. | Work produces **−1** (minimum 0). |
| **Shared Practice** | The **second and every later Work card** in a week produces **+1 extra**. The team has a routine for the thing it does most. | The **second and every later Work card** in a week produces **1 less** (minimum 0). No routines - every one is reinvented from scratch. |
| **Adaptability** | Four or five points a week - you can rebuild most of a week, or cancel the worst Event in the deck. | One point or none. You play the week you laid, whatever lands on it. |

Capability's bonus stacks with everything else on a Work card - there's no ceiling any more
(§7). A well-invested team is genuinely meant to run a different economy, not a marginally
faster one.

**Shared Practice counts Work cards, and only Work cards.** Lay three Work cards in a week and
the *first* is always plain: the 2nd and 3rd are the ones the track touches. At 4-5 that's
**+1 each**; at 0-1 it's **−1 each**, minimum 0. Everything in between does nothing.

Only Work, for an honest reason: the other tracks move **at most one step per week** (§18), so
a second Coordinate or a second Reflect in the same week already achieves nothing. A general
"any repeated Activity" rule would have read as broad while only ever firing on Work. This
says what it does.

**This is West's team reflexivity, not accidentally.** A second Reflect in the same week
buys nothing because reflexivity isn't about how many times a team looks at itself - it's
whether it paused and adjusted at all. One genuine Reflect a week is the whole mechanism;
playing it twice is volume, not insight.

The high end is still bounded by the weekly output cap (§7), so a routine makes the team faster
without letting it dump the whole week into one push - but because that cap now rises with each
Habit, Shared Practice actually gets paid instead of landing on a ceiling. And note the low
end is a **penalty, not a prohibition** - a team with no shared routines can still repeat
itself, it just wastes part of the effort every time, which is the actual failure mode.

**Adaptability is the re-planning budget, and it refreshes every week.** It is *not* a stockpile
you save up. Whatever the track reads when you reach phase 3, that is how many points you have
that week - spend them or lose them. Adaptability 0 means you play the week exactly as you laid
it, whatever just happened. Adaptability 5 means almost nothing can catch you out.

#### How you raise the track
Three Activities feed it, and - like every track - it rises **at most one step per week**,
resolved at week close (§6.1):

| Play | Gives |
|---|---|
| **Reflect** | +1 Adaptability, unconditionally |
| **Align** | +1 Adaptability, unconditionally |
| **Meet**, as a Working Meeting | +1 Adaptability (and +1 Trust) |

**You cannot spike it.** Three Reflects in one week still move the coin one step. It starts at
**2**, so reaching 5 takes three clean weeks of deliberate investment - which is why a team
that wants to be able to react has to start paying in week 2, not week 6. By the time you
*need* Adaptability, it is too late to buy it.

That's the trap the track exists to set: spending a day on Reflect costs you Work now, against
a week that hasn't gone wrong yet.

This is where §4's warning stops being prose: **Shared Practice pays you for repeating
yourself, and Adaptability pays you for not having to.** A team that pushes Shared Practice to
5 and leaves Adaptability at 1 is genuinely excellent at the work it already knows and
genuinely cannot change course - and it will have earned both.

These stack with any Skill-match bonus (§7) and Habitus/Capital bonus (§5.1) on the same
action.

The best teams keep a healthy balance across all four - not "max everything."

## 5. Motivation
Each character has their own pool of **Motivation tokens** (starts at 3, cap 5) instead of
just a number on a track. The physical count matters, because tokens move in three different
ways:
- **Gain** - Celebrate (§7), or a good Event/team condition, adds a token.
- **Lose** - an Event or team condition removes a token. Not the character's choice.
- **Spend** - the character's own choice: pay a token for a specific optional benefit (e.g.
  Overtime, §7 - which also puts you in debt a day). Spending should be worth it *sometimes* - that's the point.

That third mode is what makes Motivation the game's **second currency** (§6.0), not a health
bar. Days are shared, fixed and expire at the end of the week; Motivation is personal, bankable up to
5, and the only thing that buys a team more output than its calendar allows. Every Motivation
spend is therefore the Hero-Team path (§14) being offered to one player, one token at a time.

| Tokens | Effect |
|---|---|
| 4-5 | Highly engaged - no penalty. |
| 2-3 | Normal. |
| 1 | Reduced effectiveness. |
| **0** | **The character quits, right away** - see §13. Not "at risk": zero tokens *is* the quit trigger. |

**The weekly grind.** When a week closes (§6.1), **every character loses 1 Motivation**. Seven
weeks, seven grinds. The only thing that pushes back is **Celebrate** (§7) - a day spent
marking what the team got done. Starting at 3, a team that never celebrates loses its first
character early in week 3.

> **Resolve the week's Motivation as one number.** Total each character's change - **−1** for
> the grind, **+1** if their Need was met (**from week 3**, §5.1) - apply it, and *then*
> check for zero. Don't run the grind as a separate step first: a character on 1 Motivation
> whose Need was satisfied has had a week that balanced out, and shouldn't quit on a
> sequencing technicality.

That's the standing drain, and it's why a bigger team is harder to sustain: the grind hits
every character, but a Celebrate still costs the same single day however many people it lifts.

Exact thresholds and penalties: playtest and tune.

### Motivation depends on habitus
An Event doesn't cost everyone the same. Each **Torso** has one Event category that gets to it,
and one it doesn't feel at all:

| Torso | −1 Motivation whenever this lands | Immune to Motivation loss from | Vindicated by |
|---|---|---|---|
| **Autonomy** | Management | Environment | Shared Repertoire |
| **Hierarchy** | Environment | Management | Who Knows What |
| **Community** | People | Customer | Psychological Safety |
| **Quality** | Customer | People | Team Reflexivity |

**Recognition is the fifth Torso and sits outside this table on purpose** - no Event category
touches it, and none is immune to it either. It's the one that's purely about being *seen*,
not about how the four categories land, so it pays off differently: **+1 Capital whenever that
character's own Need is met** (§5.1), rather than off a Habit vindicating it.

**The −1 is not conditional on the card costing Motivation.** Eight Events in the deck now take
Motivation from everybody (widened from four after a balance pass - see the extension's
version note); the other ten cost Work, or days, or Trust. But an Autonomy
character loses a point of Motivation *every time a Management Event lands*, whatever else the
card does - because that category of thing wears them down personally. That is the whole claim:
the same week is more tiring for some people than others, and not because the week was worse.

The **immunity** column only ever does anything on the original four cards that carry a Torso
reaction alongside their Motivation cost - STATUS MEETING, BUDGET CUT, REORGANISED and A FLAT
WEEK. The four added later (EQUIPMENT OUTAGE, THE TEAM SPLITS, EVERYTHING AT ONCE, THE AUDIT)
hit everybody with no immunity exception - deliberately: not every Motivation cost needs to
be a habitus lesson. On every other card the immunity line would be an
exemption from a penalty that was never coming, so **the Event cards only print the immunity
line where it does something.** If a card shows one Torso line, that category costs somebody a
point and nobody is protected from anything.

Every category has exactly one Torso that suffers and one that shrugs, so no build is simply
better - a bad week for one character is a quiet week for another, at the same table, off the
same card. (Recognition, the fifth, sits outside this entirely - see above.)

**Vindication.** The last column is habitus reacting to **Habits** (§18). Each Torso is
protected, eventually, by exactly one of them - the one that discounts the category it suffers
from. **When the team acquires that Habit, that character gains +1 Capital.** The thing you
always said mattered has become how the team works, and your standing rises accordingly.
That's Bourdieu's whole argument about legitimacy in one token.

### Need gives bonus Motivation
Your **Need is your Torso** - the same card you were dealt at setup, read a second way.
From week 3, when the week closes (§6.1), check whether the week satisfied it. If so, you
**gain 1 Motivation** (cap 5) - which, conveniently, is exactly enough to cancel the weekly
grind.

Weeks 1-2 don't ask the question, so Motivation only ever falls and **Celebrate is the sole
relief**. That's the point: the grind is taught first, and the thing that answers it was on
your board from the start - the game just waits until week 3 to turn it over.

| Torso (= Need) | Satisfied when, during that week... |
|---|---|
| Autonomy | A card assigned to this character was **not replaced** in the Adapt phase - they finished the day they were given. |
| Hierarchy | They played a **Teach** card, or they spent their Hero. |
| Community | The team spent a Coordinate, Reflect or Celebrate, or Trust is currently 4 or higher. |
| Quality | The team spent an Align. |
| Recognition | A feature they Worked on was banked, or they led a successful Demo. |

Checking this once per week rather than once per day keeps it to one pass over four
characters at a natural stopping point - and it makes the Need question the right one:
*did we, across a whole week, pay any attention to what this person needs?*

> **Autonomy is the one that bites.** Adapt is how the team saves a week that Events have
> wrecked - and every replacement costs somebody their Autonomy. The team that re-plans hardest
> is the team that keeps overriding the person who most needs not to be overridden. That
> tension is deliberate, and it is the only Need the team can actively take away.

### 5.1 Capital (within the field)
In Bourdieu's terms, habitus only "pays off" when the field treats it as legitimate. **Here,
the field is the team itself** - small and temporary, but it still has its own emerging sense
of who's earned the right to take charge, be listened to, or be trusted with a judgment call.

Each character tracks **Capital** (0-5, next to Motivation on the character card): how much
the rest of the team currently trusts this character's standing. It's not the same as:
- **Item/Skill** - what they can actually do.
- **Habitus** (Base/Legs/Torso/Head) - how they tend to act.
- **Trust** - how much the team trusts each other in general.

Capital is about whether *this character's* actions land, specifically.

**Starting value:** 2 (scale 0-5) for everyone at setup - nobody's proven anything yet.

#### Capital is converted, never self-generated
Standing doesn't come from standing. It's **converted**, in public, out of something you
already hold - see the forms-of-capital model in
[../docs/habitus-model.md](../docs/habitus-model.md). Your **Knowledge and Skills** (built by
your Base and Legs) are one form; the team's **Trust** is another. Capital is what those turn
into once the team recognises them.

**Gaining Capital.** Maximum **+1 per character per week**, however many of these fire:

| Trigger | What converts |
|---|---|
| You played a **Learn** card this week as the **teacher**. | Knowledge → standing. You give the know-how away and get standing back. |
| A feature you played a **Work** card on was **banked** this week. | Delivered work → standing. |
| You led a **Demo**. | A public success → standing. |
| A **habitus strength** of yours visibly worked in front of the team - a Take Charge call that landed, calling out Knowledge Hoarding. | Disposition → standing. |
| **Cross-Trained** - you just covered your **3rd row** on the Zone board (§8), once per character, whenever it first happens. | Breadth → standing. Not the team's Capability, *yours* - the moment you stop being fixed to one fragment of the work. |
| You paid the Motivation for **Take One For The Team** (§6.1) this week. | Personal sacrifice → standing. You spent your own Motivation so the team's Trust could rise; the team saw it cost you something. |

All six require the team to **witness** it - no exceptions. Private competence earns nothing -
recognition is what makes standing exist at all. **Recognition (the Torso) leans into this
instead of opting out of it**: whenever one of their own six triggers fires, witnessed as
normal, they **name the teammate who witnessed it** - that teammate gains **+1 Motivation**.
Being seen is relational: crediting the person who saw it back is the one thing none of the
other five triggers ask for, and Recognition is the one habitus built to do it anyway.

**Losing Capital.** No weekly cap:
- A habitus **tendency** of yours fired publicly against the team's wishes: **−1**.

*(Extension: `game/extensions/performance-review/` restores a second, individualized Capital-loss
trigger - being the subject of a Performance Review - plus a way for the team to convert it into
a shared −1 Trust instead. Cut from the base game, see that pack's README for why.)*

> **This is what finally gives KNOWLEDGE HOARDING teeth (§11).** Hoarding protects your
> scarcity - you stay the only one who can do the thing. But teaching is the main route to
> standing, so the hoarder stays permanently **needed** and never becomes **respected**. That
> trade-off is the whole event, and it only exists once teaching pays Capital.

#### Standing doesn't update itself
**Standing** (the Ledger row that joins at week 4, §3.0) is not its own resource - it just
names whichever character currently holds the highest Capital, and it is **not live**: nobody
re-checks it every time a Capital box changes. It gets re-read at two points only - the week 4
reveal (its first reading), and whenever an Event explicitly says to (REORGANISED is the only
one that does, so far). Outside those two moments, the marker stays where it last landed even
if Capital has since moved past it - Standing is a snapshot of a moment, not a live mirror.

#### The habitus trigger pattern
Every habitus effect reads as: **when [X] happens, if a character's habitus is [Y], then [Z].**
Habitus shows up in four places, and between them they cover everything a character does:

| Part | Reacts to |
|---|---|
| **Legs** | **Activities** - your Skill gives +1 on one of them |
| **Torso** | **Events** (one category worse, one not at all) and **Habits** (+1 Capital when yours arrives) |
| **Head** | **Pressure** - a strength and the tendency that comes with it |
| **Base** | **Motivation** - a strength and tendency on your own Learn/Teach/Overtime/Hero, never on Work (§5.2) |
| **Head** | **The Hero move** - every part is one of your Pressure Response and Events name a Pressure Response you alone can cancel |

#### The Hero move
Every Event card names one of the five **Pressure Response** options (Take Charge / Analyze /
Support / Challenge / Withdraw). A character whose **Head** is that Pressure Response may,
**once per game**, spend their **Hero** to **cancel that Event outright** - no Adaptability
paid, nothing resolved. They gain **+2 Capital**, and **one other character of their choosing
gains +1 Motivation**: somebody saw it, and it mattered to them.

> **You must have at least 3 Motivation to play your Hero.** It costs you nothing - it is a
> threshold, not a price. People who are running on empty do not step up; that is the whole
> observation. Check it at the moment you play it.

This is the rule that makes **Celebrate** strategic rather than merely survival. The weekly
grind drags everyone toward the floor, so a team that only Celebrates enough to keep people
from quitting will find, somewhere around week 5, that nobody at the table is capable of a
Hero any more. The Events that only *you* could have answered arrive, and you watch them
land.

It also gives the Hero's own +1 Motivation a second job: hand it to the character sitting on
2, and you have just made *them* able to step up later.

All eighteen Event cards carry a Hero route except three, split evenly across the five Head
options (3 cards each), so **most characters can answer exactly 3 Events, whatever Head they
were dealt**. The three that name no Pressure Response at all save nobody.

This is the sharpest version of the whole thesis. Your habitus is not better or worse than
anyone else's; it is *tuned to a situation you did not choose*. When the field finally asks the
question you happen to be the answer to, you convert disposition straight into standing - and
someone else is moved by watching it. When it never asks, you carry a Hero you never spent.
Every habitus effect (see the design rule in
[../docs/habitus-model.md](../docs/habitus-model.md)) should read as: **when [Event X]
happens, if a character's habitus is [Y] and their Capital clears a threshold, then [Z].**
Capital decides whether the *same* habitus-driven action succeeds, or just costs the
tendency's price.

> **Elite Athlete, revisited:** when the team is under real pressure (X) and a character's
> Head is Take Charge (Y):
> - If **Capital ≥ the team average**: they get +1 immediate Work output - the team accepts
>   the lead.
> - If **below average**: no Work bonus. The team hesitates or pushes back, and the **−1
>   Trust** tendency still applies if no Knowledge holder was consulted.
>
> The habitus doesn't change. Whether it works depends on how the field currently reads that
> character - that's Capital.

#### The Capital threshold is relative, not absolute
Capital isn't a substance you accumulate; it's a **position in a distribution**. What matters
is how much you hold compared to everyone else in this particular field - and the field here
is this team.

> **Demo requires Capital ≥ the team's average Capital**, counting every character still on
> the team. Check it when the week is laid out (§6.1 phase 1).
>
> The same test replaces every other "Capital ≥ 3" in the game, including the Take Charge
> pattern above.

At setup everyone sits at 2, which *is* the average - so **everyone qualifies and nothing is
locked**. But the moment one character pulls ahead, they raise the average and start shutting
the others out. Nobody wrote that rule; it falls out of the threshold being relative.

That is the "face of the team" concentration this section used to only warn about. Demo grows
the Capital that Demo requires, so standing compounds into one character - the same Hero-team
risk flagged in §14, now an actual mechanism instead of a paragraph. Deliberately routing a
Demo to a lower-Capital character costs the team a safer success, but spreads standing to
where it's needed, especially after onboarding (§12). That's a real strategic choice, and now
it's a real rule.

> **Two readings of the same rule.** Bourdieu's is the one already cited above - capital as a
> position in a field, not a substance. But "compare against the average, not a fixed number"
> is also exactly Foucault's **normalization**: power doesn't need an external absolute
> standard, only a distribution to sit inside of. The two aren't competing explanations here -
> Bourdieu and Foucault were real intellectual neighbours arguing about this same phenomenon,
> and the rule holds up under both readings at once. **A third:** Elias's figurational
> sociology rejects the free-standing individual entirely - there is no Capital value that
> exists before or outside the team, only a position inside the *current* figuration. See
> [../docs/theoretical-sources.md](../docs/theoretical-sources.md).

> **Not yet in play - sponsorship.** A researched option, held back until a playtest shows
> Capital genuinely concentrating: *a character with Capital ≥ 4 may be named alongside the
> presenter to sponsor a lower-Capital character's Demo, which then ignores the threshold.
> Success gives the presenter +2 instead of +1; failure costs the **sponsor** −1 as well.* This is
> Bourdieu's **consecration** - the established lending legitimacy to a newcomer, and carrying
> some of the risk. See B4 in the [assessment](../docs/playability-assessment.md). Don't add
> it until the problem it solves has actually appeared at a table.

Other activities that might reasonably need Capital (e.g. representing the team in a
management-facing meeting): to be decided - playtest and tune.

### 5.2 Base - your Motivation, not your Work
Your Base never touches Work, a feature, or any Team State track. It answers a narrower,
personal question: what costs *you* energy, and what gives it back? Like every other habitus
part it pairs a strength with a tendency (see the design rule in
[../docs/habitus-model.md](../docs/habitus-model.md)) - but both halves move only your own
**Motivation** (§5), never a shared track, never a feature, and never anyone else's day. That's
the point: a team can dodge a bad *feature* fit by working in parallel, but it can't dodge one
character's own Motivation for them.

| Base | Strength | Tendency |
|---|---|---|
| **Bookish** | **+1 Motivation** when you play Learn | **−1 Motivation** when you play Teach |
| **Hands-On** | **+1 Motivation** when you play Teach | **−1 Motivation** when you play Learn |
| **Sheltered** | The weekly grind (§5) doesn't affect your Motivation | **You never rise above 3 Motivation** - insulated from the highs as much as the lows |
| **Strict** (now **By The Book**) | Ignore **one** Event's Motivation loss, each week (your choice which, of the two drawn) | **The other** costs you an *extra* **−1 Motivation** |
| **Competitive** | May spend **Hero** even below the usual 3-Motivation threshold | **Spending your own Hero costs an extra −1 Motivation** - it never comes free for you |

Each **Head/Pressure Response** pairs the same way, keyed to whichever Team State track (§4)
it reads as most under pressure - high, it lands as **+1 Motivation**; low, the same instinct
reads as overreach for **−1 Motivation**:

| Head | Track | Strength (track ≥ 4) | Tendency (track ≤ 1) |
|---|---|---|---|
| **Take Charge** | Trust | +1 Motivation - the team backs your call | −1 Motivation - it reads as overreach |
| **Analyze** | Capability | +1 Motivation - the question was worth asking | −1 Motivation - analysis paralysis |
| **Support** | Shared Practice | +1 Motivation - people leave the room feeling better | −1 Motivation - it reads as hollow |
| **Challenge** | Adaptability | +1 Motivation - the thing everyone was quietly worried about | −1 Motivation - it reads as obstruction |
| **Withdraw** | Capability | +1 Motivation - you'd rather be good at it than explain how | −1 Motivation - it reads as unavailable |

All five Base options are personal and apply only to your own Motivation pool. None of them
ever touch Work, a feature, or a Team State track directly - which is also why none of them
need a Focus, a target feature, or any restriction on who works what: there's nothing left to
route around.

Head reads a Team State track as its *trigger*, but the payoff is still only ever your own
Motivation - no Base or Head option ever changes Work, a feature, or a track's value.

They all matter for the same downstream reason: Motivation is what decides whether you can
still play your **Hero** (§5.1) and whether you **quit** (§13). A Bookish character endlessly
assigned to Teach and never allowed to Learn is being quietly run into the ground, and it will
show up on their own track - nobody else's.

## 6. The Working Week

### 6.0 The two currencies
The team spends exactly two things, and nothing else.

**Days - the team's time.** A week is **five days**, and that is the *whole team's* week - not
five days each. Three players or six, the week is still five days. Each day is **one Activity
card** (§7); the team names which character executes it **when the card resolves**, not when
it's laid out - that character's Skill, Knowledge, Habitus and Capital apply to it. A character
may take several of the week's days, or none at all.

> The project's budget is **7 weeks × 5 days = 35 days.** That is the number Work Costs get
> compared against, and it does not move.

**Why the team, not the person.** This game is about how a team spends its time, and that
shouldn't change because someone extra joined. Adding people gives you **more options, not
more actions** - a bigger team covers more Skills and holds more Knowledge, so you can pick a
better character for each day. It also gives you **more people to keep motivated**, and the
weekly grind (§5) hits every one of them while a Celebrate still costs the same single day.
Big
teams are more capable and harder to sustain. That's the trade, and it's the same trade real
teams make.

**Motivation - personal, and the only way to buy more.** Days are shared and fixed;
Motivation is per-character and genuinely spendable (§5). Spending it is the only way to push
a week past five days - see Overtime (§7).

### 6.1 The weekly turn
The game is **7 turns, one per week**. Each week runs in four phases:

**1 - Plan the week.** Lay out **five Activity cards**, one on each weekday slot Monday to
Friday. Nobody is assigned to a card yet - that's decided when it resolves (Phase 4), not now.
A slot may instead take a **Flex marker**, giving back a day someone worked as Overtime (§7).
Then stop. Nothing has resolved.

**2 - Shit happens.** Draw **2 Event cards** and turn them face up beside the week. Read them
out. **Do not resolve them yet** - they are threats, not yet facts. They are aimed at the week
you have *already committed*, which is the point.

**3 - Adapt.** You may spend **Adaptability equal to your Adaptability track** (§4). Spend
them in any mix you like, in any order:

| Spend | Cost | Effect |
|---|---|---|
| **Cancel an Event** | its printed **ADAPT** number | Discard it. It never happened. |
| **Replace a card** | **1 Adaptability** | Take one of the five cards off the week and put a different Activity in its place. Somebody is doing something else now. |

Cancelling is **all or nothing** - you cannot part-pay an ADAPT 3 with 2 and soften it.

> **Why you can't just shuffle the days around.** You can't, and it wouldn't help. The five
> slots are a **set, not a sequence** - Monday to Friday is flavour, and every card resolves as
> though the week happened at once. Moving a card from Tuesday to Thursday changes nothing, so
> it isn't an option. The only thing worth spending on is changing **what somebody does.**

Two things cancel an Event **without costing Adaptability at all**:
- a character's **Hero** (§5.1), if the Event names their Pressure Response - once per game;
- **Authorized Voice** (§18), once a week, if the team has it.

**Worked example.** Your Adaptability is **3**. You draw EQUIPMENT OUTAGE (`ADAPT 3`) and A FLAT
WEEK (`ADAPT 2`). You already hold **Who Knows What**, which discounts Environment Events, so
the Outage costs **2**, not 3. Now you choose:
- cancel the Outage (2) and spend your last point replacing a Work card with a **Celebrate**,
  letting A Flat Week land but blunting it; or
- cancel neither, and rebuild three of the five days instead.

If someone at the table has the **Support** Head, they could instead Hero the Outage for
free, keeping all 3 Adaptability - and take +2 Capital for it.

**Then resolve whatever survived.** Events you did not cancel happen now, before the week runs.

#### Two ways out of an Event, and a Habit that changes the price
Every Event card prints the same **HOW TO ADAPT** block, Torso reaction (if any) printed just
above it. Two of its lines remove the Event, joined by an "or" - it prints a bare number and
unit (no repeated "ADAPT" label, since the box header already says it):

| Route | Costs | Limit |
|---|---|---|
| **n ADAPTABILITY** | n Adaptability, that week's re-lay budget | Whatever the track allows |
| **HERO** | Nothing. A named Pressure Response (§5.1) | Once per game, per character |

**The third line, HABIT, changes the price - and the card tells you what to.** Each Event
names the Habit matching its category. If the team has acquired it (§18), the card's own HABIT
line states the result: an ADAPT 3 card reads *so it costs 2 instead*. **A Habit always
costs 1 less - it never fully removes the need to spend Adaptability.** No
one has to work out which, and neither board carries the rule: it is printed on the card in
front of you.

| Category | Habit that discounts it | Grown on |
|---|---|---|
| **People** | Psychological Safety | Trust |
| **Environment** | Who Knows What | Capability |
| **Management** | Shared Repertoire | Shared Practice |
| **Customer** | Team Reflexivity | Adaptability |
| *Any* | **Authorized Voice** - cancel one Event a week outright | Standing |

This is the difference between a team that copes and a team that has changed. Adapt is
scrambling: it costs you the same every single time. A Habit costs nothing forever, because it
isn't a resource - it's who you now are. Wenger's shared repertoire is exactly this: the
practices a community builds until the thing that used to be a crisis is just Tuesday.

**4 - The week runs.** Resolve the five cards. **Order does not matter** - the week happened at
once, and every Activity is written so that it doesn't care what was resolved before it. Work
out the total, move the counters, done.

The weekdays are there so the week *reads* like a week, and so five slots are obviously five
days of a team's time. They are not a sequencing puzzle.

**Then close the week**, in this order:
1. **Bank** any feature whose Work counter reached its Work Cost (§10) - lift the lock tile off
   anything it unlocks, and pay Capital to whoever worked on it.
2. **Walk the Ledger** coins, at most one step each, and flip any that reached its ring (§18).
3. **Motivation - as a single net number per character:** −1 grind, +1 if their Need was
   met (§5). Apply it, then any character at 0 leaves.
4. **Advance the week.**

Banking comes first because it pays the Capital that feeds the Ledger's Standing row. **The
project ends when Week 7 closes.**

> **Why weeks and not days.** You commit all five days *before* you know what's coming. Plans
> get made in ignorance and reality lands on them - which is both the honest version of
> project work and the reason Adaptability is worth paying for.

Wherever an Event or rule says *"the team spends a Coordinate/Align/Plan/Reflect/Meet day,"*
read it as **one of the week's five cards**, unless the card says otherwise.

## 7. Activities - one card, one of the week's five days

Every Activity has an exact effect. Nothing here is "may" or "improves" - if a number isn't
listed, nothing happens. **The team names which character executes each card when it
resolves** - there is no assignment step during Planning (§6.1) - and that character's Skill,
Knowledge, Habitus and Capital apply. Where a card's Capital gain has no single teacher or
presenter named on it (a collective effort, not a paired one), the team nominates **one**
character to receive it.

| Activity | Exact effect |
|---|---|
| **Work** | **+1** to one feature's Work counter (§10). Modified by Capability (§4), Skill match, Knowledge and Habitus. **Minimum 0.** Can't target a feature whose Dependency is unbanked. |
| **Plan** | Choose a feature with clear requirements: **every Work card played on it this week produces +1 extra** (Low: no bonus). **If High complexity, the bonus also applies next week.** |
| **Coordinate** | **+1 Trust.** |
| **Align** | +1 Adaptability, unconditionally. |
| **Learn** | Cover a free square **in your own row** of the Zone (§8), immediately **left or right** of one you already cover. No teacher, no Capital - an instrument can be got hold of alone. |
| **Teach** | Let **up to two different characters**, each already covering a square, each let another character cover it, **any row**, immediately **up, down, left or right** of one they already cover. **Both teachers +1 Capital.** **Does nothing while Trust ≤ 1.** |
| **Demo** | Needs **Capital ≥ the team average** (§5.1). **The whole team takes part**; the team then names **one** character to receive **+1 Capital**, and the feature ignores the next NEGATIVE FEEDBACK. |
| **Reflect** | **+1 Adaptability.** If a feature was banked *or* an Event resolved since the team's last Reflect, also **+1 Shared Practice**. |
| **Meet** | Resolve as §9. **Working Meeting:** +1 Trust, +1 Adaptability. **Record Meeting:** no effect at all, but it satisfies Events that demand one. |
| **Celebrate** | **+2 Motivation to every character** (cap 5) - **+3 instead if a feature was banked this week.** |

There are **ten** Activities, and none of them is "rest" - resting isn't something a team does
at work. **Celebrate** is what is: you mark what you got done, in work time, together. It is
the only thing that pushes back against the weekly grind (§5).

### Why Celebrate pays more when you've shipped
A celebration with nothing behind it still helps - the base +2 is unconditional, so a team in
trouble always has a lifeline and can't spiral. But **+3 when a feature was banked that same
week** builds the rhythm the game is really about: *deliver, then mark it*. It makes the
Feature Tower emotionally load-bearing rather than decorative, and it rewards timing rather
than just spending.

It's also the honest version of how teams actually sustain themselves across a hard project.
They don't rest in the middle of it. They ship something and say so.

### Overtime, and the hours you owe
> **Overtime.** Any week, **at most one character** may play a **sixth card**, matching their
> Item - there is only one Overtime slot on the board. They immediately **spend 1 Motivation**
> and take a **Flex marker** - a day the project now owes them. A character holding a Flex
> marker cannot take Overtime again until it's cleared.
>
> **Flexing back.** Place a **Flex marker into a weekday slot** instead of a card. That day
> produces nothing at all - it's the day being given back - and the marker is discarded.
>
> **At the end of the project, every Flex marker still held costs 2 Team Score** (§16). Hours
> nobody ever gave back.

**Overtime buys timing, not capacity.** Six days this week and four the next is still ten days - the extra card costs a Motivation and returns nothing net. What it buys is *when*: banking a
foundation a week early unlocks its gated feature a week early, and on the critical path that
can be worth more than the day itself.

The exception is the one everybody recognises. **In week 7 there is no "later" to flex back
into** - so crunching at the deadline genuinely does buy days, and the bill arrives as Team
Score instead. That's the whole Hero-Team path (§14) compressed into a single decision, made
at the exact moment real teams make it.

> **The week runs 4 to 6 days, and both ends cost you.** Under-fill and the project slips.
> Over-fill and you're borrowing from a week that hasn't happened yet.

### Take one for the team
> **Any character may pay 1 Motivation for the team's +1 Trust this week** - a standing action,
> not a card, usable even in a week with no free slot for Coordinate or a Working Meeting.
> Once per week: if Trust already rose this week (Coordinate, Meet, or this action, by anyone),
> nobody may do it again - see the shared ceiling below.

It's the personal-cost mirror of Overtime: Overtime borrows against the *project's* clock
(a day now, a Flex marker owed later); this borrows against a *character's* Motivation instead,
for a track the team couldn't otherwise afford to move that week. Same shape as every other
habitus/Base pairing - one resource, spent - just not printed on a card, because it belongs to
any character, not one build option.

**Two limits that apply to everything above:**
- Work output is never below **0**.
- Each Team State track rises by at most **1 per week**, however many cards - or standing
  actions, like Take One For The Team - push at it.

### There is no weekly output ceiling any more
> **Removed on purpose.** Work used to cap out at *(Work cards played) + 2 + (1 per Habit)*.
> It doesn't any more. If Capability, Skill, Knowledge and Habitus all stack on one card, it
> produces all of it - that's what three or four weeks of deliberate investment is *for*.

The old cap existed to stop a maximally-stacked team running "a completely different economy"
from a badly-built one. **That's now the point, not the problem.** A team that invested in
Capability, taught its Skills around, and kept Knowledge current genuinely does run a different
economy - and the cost of getting there was real: three-plus weeks of Learn, Coordinate and
Reflect days that weren't spent building. The consequence lives in the investment, not in a
ceiling on the payoff.

This removes the only mechanical grounding **Brooks's Law** had in this game (the per-feature
cap, just above, was the other one). Both are gone on purpose now - see
[Designer's Notes](../docs/04-designers-notes.md) for the honest accounting of what that costs
the theory, and log what an uncapped week actually does to the 18-Work / 35-day budget in
[../playtests/README.md](../playtests/README.md), because nobody has derived those numbers
against this version yet.

### Why Plan scales with Complexity, without letting one card finish the job
Every Work card gets the same **+1 extra** when Planned - the bonus itself never changes size,
so Planning can never let a single card outrun a feature's real Work Cost. What Complexity
changes is **how long the bonus lasts**: Low gets nothing, Medium gets it for the week it was
Planned, and **High keeps it into the following week too**. That rewards Complexity exactly
where it already costs something - High features already take a bigger rework hit from Events
(§10) - so Planning a hard feature pays off for as long as it's likely to still be open,
rather than in one lump sum that could finish it outright.

Note that Plan buys nothing unless Work follows it *in the same week*: a Plan card played on a
feature nobody then works on is a wasted day. That's the real decision, and it doesn't need a
sequencing rule to be sharp.

### Skills modify Activities
Item/Skills were chosen at creation but never actually did anything until now. Here's the
fix: if the character playing a card matches one of their Skills to it, add **+1** to that
Activity's **first listed numeric effect** in the table above - Work's counter gain, Plan's
Work bonus, Coordinate's Trust, Learn's transfer (a matching teacher may move **two**
Knowledge in the same action), Demo's Capital, Reflect's Adaptability.
No match, no bonus - the Activity just resolves at its normal effect.


| Skill | Matches |
|---|---|
| Technical | Work |
| Planning | Plan |
| Facilitation | Align, Coordinate |
| Communication | Coordinate, Demo |
| Leadership | Meet, and Take Charge (Head) calls |
| Analysis | Plan, Reflect |
| Customer | Demo, Align |
| Quality | Reflect |

Every non-Work activity above maps to a specific Wenger or Vygotsky mechanism, not generic
"team building" - see [../docs/team-learning-model.md](../docs/team-learning-model.md) for
why each one exists and what it's really doing, including why Trust stands in for
psychological safety in this game.

This is what finally pays off the "same skill, different person" idea from
[../docs/habitus-model.md](../docs/habitus-model.md) on the *capability* side. The skill
itself is a small, flat, reliable bonus. The habitus is still what decides whether the
character reaches for that Activity in the first place.

## 8. Knowledge & Learning - the Zone (board 4)
What a character knows isn't a private card any more - it's a square on the shared **Zone**
board (board 4), a 5x5 grid of **Education** (row: your Legs) by **Skill** (column: your Item).
Covering a square means you can do that row's work with that column's instrument; once every **row in play** in a column is covered - by anyone, not necessarily the same character - the card
named under that column gets **+1**, no matter how many people hold it. A column that is only
partly covered gives nothing yet; there is no partial credit for a square here or there.

> **A row only counts if a character starts on it.** At setup, a row with nobody's Legs on it
> has no way in - Learn only extends your own row, and Teach needs a teacher who already holds
> a square there, so an empty row can never be entered by either card. **At 4 players, exactly
> one of the 5 Legs values is missing (5 Legs cards, dealt without replacement, one per
> character) - so exactly one row sits permanently empty.** Check which row(s) have nobody on
> them the moment habitus is dealt (§3.1): those rows don't count toward "every row in a
> column" for the rest of the game. A column completes once every **occupied** row in it is
> covered - the empty row is simply not part of the count. (5 players fills all 5 rows exactly
> once; 6 players fills all 5 with one row doubled - neither has this problem.)

There are two ways to cover a new square, and neither is a diagonal leap - that's Vygotsky's
**Zone of Proximal Development** made physical, one step from what you can already do. **Learn** (§7) covers a free
square **left or right** of one you already cover, in your own row only, alone, no teacher
needed. **Teach** (§7) lets **up to two different characters**, each already covering a
square, each let one other character cover it, **up, down, left or right** of one *they*
already cover - in any row, since a teacher can hand someone a square they'd
never have reached alone. **Both teachers gain +1 Capital.** One card, one day, two pairs - a
second teacher doesn't cost a second day; a training has to be conferred
by somebody who holds it, a skill can be picked up alone - that difference is the whole reason
the two are separate cards.

The Ledger reads the same board two ways: **fill any whole row or column** and Capability
rises; **two characters covering the same square** (a stack) and Shared Practice rises. One
step a week, as ever - a column can only be filled by teaching, never by Learn alone.

### Teaching costs a day, and a day is the scarcest thing there is
**Learn and Teach happen as the card is played.** Each takes one of the week's five days and
that is its whole cost for Learn - no Motivation, no Capital, nothing owed afterwards. The
teacher on a Teach card is barred from
nothing; they simply spent a day on this instead of on the tower.

That day *is* the scaffolding cost. Five days a week for the whole team, against 18 Work and a
35-day budget (§3.2), means every day spent teaching is a day the tower does not rise.
Vygotsky's **more knowledgeable other** is priced here as **opportunity, not penalty**: nobody
is punished for teaching, they just cannot also have built something with that day.

Two harder versions were modelled and dropped. Charging **two** days outright - the literal
reading of "a specialist teaching someone is worth two person-days" - drops a well-played
invested game to ~16 Work against the 18 the project needs. Barring the teacher from Work for
the rest of the week landed at ~20, but it charged for teaching twice: once in the day, again
in the restriction, which made the best teacher the worst person to teach.

> **What this change is worth.** A team that plays four Learns across the project keeps roughly
> four Work days it used to forfeit - about **6 Work** at the bounded rate of ~1.4 per Work day
> (§3.2). That deliberately tilts the game toward the invested line, which is the thesis. It
> wants playtesting rather than further modelling.

### The zone - you can't teach what you only just learned
**A Knowledge received this week cannot be taught this week.** Turn the card sideways when it
arrives; straighten it when the week closes.

This is the **zone of proximal development** made physical. Before this rule, a Knowledge could
cross the whole team in a single week - A teaches B on Monday, B teaches C on Tuesday - which
says that being told a thing and being able to teach it are the same state. They are not. The
gap between them is exactly what Vygotsky named.

One teacher may still hold a workshop instead: A can teach B *and* C **using two separate
Teach cards**, because A has held the Knowledge all along. That costs **two of the week's
five days** - a genuinely different choice from the two-teachers-one-card version above (one
teacher reaching two learners, instead of two teachers reaching one each).

> **Marx's overcome division of labour, played out square by square.** A character who starts
> narrow - one row, one column - and ends the project covering half the board isn't just more
> Capable; they're closer to Marx's "fully developed individual" (*The German Ideology*, 1846),
> able to do more than one kind of work instead of being fixed to a single fragment of it.
> **Knowledge Hoarding** (§5.1, §11) is the same idea from the other side: treating what you
> know as private property, withheld rather than made social, is exactly the alienation this
> mechanic punishes - which is why only teaching, never hoarding, ever converts to Capital.

## 9. Meetings
Meetings aren't automatically bad - the game separates **useful coordination** from
**organisational overhead**.

- **Working Meeting** - one of the week's five days; builds shared understanding, may raise
  Trust.
- **Record Meeting** - one of the week's five days; produces a record of the week for whoever
  needs one, but **no real feature progress.**

> **Event: ANOTHER STATUS MEETING** - *"Just a quick 30-minute check-in."* Actually costs the
> team **one of its five days** this week. Effect: **−1 Motivation** (everyone). (The
> corporate name is deliberate here - this is an Event, the world imposing itself on the team;
> §9's own Record Meeting is the same shape without the jargon, because the team chose it.)

## 10. Feature System
Each feature has a Work Cost, Complexity, Dependencies, and a running
**Work counter** starting at 0. A Work card adds to that counter - usually +1;
Habitus/Capital effects can add more (§5.1), and Skill matches can add even more (§7).

> **Extension available:** a hidden per-feature **Quality** attribute and an **Unclear**
> flag were part of this system in early drafts and are now an optional add-on - see
> `game/extensions/feature-quality-uncertainty/`. The base game below doesn't need either.

**Dependencies gate Work.** A feature with an entry in the "Depends on" column (§3.2) can't
receive Work until its prerequisite feature is placed on the Feature Tower. Work spent on it
before that is wasted.

**And the blocks enforce it themselves.** **D and F have no flat bottom** - a cone and a wedge.
They cannot stand on the plinth, on the table, or on any other block. Each seats into a cradle
that exists on exactly one piece: D's cone into B's dish, F's keel into C's groove. So a
dependent feature is not merely *forbidden* before its prerequisite lands, it is physically
**unplaceable**, and the finished tower becomes a record of what got built on what.

**Nothing caps how many Work days a feature can absorb in a week.** If the team wants to put
all five days into one feature, they can - there's no rule stopping them, and no day is ever
wasted just for landing on a feature that already has Work on it this week.

**The consequence isn't a rule, it's an opportunity cost.** Five days is still five days -
every one spent on Work is a Coordinate, Align, Learn, Reflect or Celebrate that didn't happen.
A team that never builds **Shared Practice** also never gets its payoff: at 0-1, the **second
and every later Work card in a week produces 1 less** (§4) - stacking Work without ever having
built a routine for it genuinely gets worse per card, it just isn't blocked outright. That's
the brake now: diminishing returns and a stalled Ledger, not a hard ceiling.

**Once a feature's Work counter reaches its Work Cost, the team gets to place that feature's
block on the Feature Tower** at the end of that week (§6.1). That placement is how
progress actually becomes visible - there's no partial stacking before that point, and
nothing to show for a half-finished feature except a counter quietly filling up.

Reaching the Work Cost doesn't guarantee the feature stays placed. Events and feedback (via
Demo) can add rework, extra requirements, defects, or new dependencies, which raise the
effective Work Cost or knock Work back off the counter - a feature can get pulled back off
the tower if that happens after it was placed. This is what keeps the game from being a plain
worker-placement puzzle.

**Complexity scales rework.** Event cards that print a rework number (NEGATIVE FEEDBACK's
−2, TECH DEBT SURFACES' +1 Work needed, §11) assume a Medium-complexity feature. Adjust by
the feature's real Complexity: Low is **−1** off the printed number, High is **+1** - a High
feature genuinely has more that can go wrong.

The **Feature Tower** is a display of **what's actually been delivered**, not
work-in-progress. Each placed block is a small, permanent-feeling win, and the growing gap
between placed and required features builds pressure as the deadline gets closer.

> **No block carries a name.** Nobody privately owns a feature, and Team Score belongs to the
> team, not to whoever last touched a given block - closer to a worker-owned cooperative than
> a factory floor. See [../docs/theoretical-sources.md](../docs/theoretical-sources.md) for
> why that's worth saying out loud rather than assuming.

## 11. Events
Drawn throughout the project; these represent the unpredictable stuff outside the team's
control.

### Rhythm: two Events per week, drawn *after* the plan is committed
**Draw 2 Event cards every week, in phase 2 of the weekly turn (§6.1)** - after each character
has already laid out its five cards, and before any of them resolve. Fourteen Events
across the project.

This timing is the entire point, and it replaces v0.1's hidden-Event-day token. You commit
the week in ignorance; then reality lands on it. Events can:
- **take a day off the board** - remove one of the five cards; it never resolves;
- **invalidate what a card was pointed at** - e.g. the extension-pack UNCLEAR REQUIREMENT
  Event flags a feature, wasting a Plan card aimed at it this week (`game/extensions/feature-quality-uncertainty/`);
- **raise a cost you had planned around.**

A team that invested in **Adaptability** (§4) can replace that many cards in phase 3.
else in phase 3. A team that didn't, eats the week exactly as it planned it. That's what
Adaptability is *for* - it's not a discount on Event damage, it's the ability to change your
mind after the damage lands.

Categories:
- **Management** - micromanagement, status meetings, reorganisation, new reporting requirements.
- **Customer** - requirement changes, new priorities, feedback, unclear requirements.
- **Team** - conflict, burnout, new members, people leaving.
- **Environment** - technical problems, external dependencies, unexpected opportunities, crises.

> **House rule for anyone adding cards:** the rest of the game speaks plainly - see the design
> guide's three-voice system. **Corporate jargon and buzzwords live only in Management-category
> Events.** That's the one place the world is allowed to talk like that *at* the team; nowhere
> else earns it.

### Example event cards
> **ANOTHER STATUS MEETING** - remove one of this week's five cards. Everyone: −1
> Motivation, except Head = **Withdraw**: −2 instead. (Forced synchronous social time costs
> more when your instinct is to solve things alone.)

> **BOSS MICROMANAGES** - everyone: −1 Motivation, except Torso = **Autonomy**: −2 instead
> (this goes against what they value), and Torso = **Hierarchy**: no Motivation loss
> (deferring to authority feels natural to them). If Trust is low: −1 additional Trust.

> **CUSTOMER CHANGES PRIORITY** - move the highest-priority feature; the team must spend an
> extra day aligning. If Adaptability ≥ 4: skip the extra cost.

> **HERO MOMENT** - one character may take **Overtime** (§7) this week even if they already
> hold a Flex marker. They still spend the Motivation, and they take a **second** marker. If
> this becomes a habit, the team is running on one person's unpaid hours.

> **KNOWLEDGE HOARDING** - a specialist won't share critical Knowledge; nobody else can use
> it. If Trust ≥ 4, the team may call this out.

> **RETIRED: NEW TEAM MEMBER.** Onboarding is no longer triggered by drawing a card - see
> §13's Replacement rule. This card slot now carries **REINFORCEMENTS ARRIVE** (Brooks's Law).

> **KEY SPECIALIST LEAVES** - remove one character. Any Knowledge only they knew is lost. If
> it had already been shared, nothing is lost.

### More event cards (building toward the ~30-card deck)

**Management**
> **REORGANISATION** - Roles get reshuffled. Treat two characters (players' choice) as newly
> re-onboarding (§12) - they haven't left, but they're now working under a different
> structure.

> **NEW REPORTING REQUIREMENT** - the team must spend a Meet this week producing a status
> report, or take −1 Motivation (everyone) at the end of the week.

> **EXECUTIVE VISIT** - a Demo is expected within 2 days. If it doesn't happen: −1
> Motivation (everyone).

> **BUDGET CUT** - −1 Motivation (everyone), once. If Trust ≥ 4, the team may spend a
> Coordinate day to turn this into no effect instead.

> **MANAGEMENT PRAISE** - if a feature was completed this week: +1 Motivation (everyone).
> Otherwise, nothing happens.

> **CORPORATE BUZZWORD BINGO** - leadership announces a new "strategic initiative" that
> changes nothing about the actual work. Everyone: −1 Motivation. If the team already banked
> a feature this week, ignore this card entirely - shipped work is the one thing a buzzword
> can't argue with.

> **A NEW AI INITIATIVE** - leadership wants "AI in the roadmap" by Friday. Spend a Plan day
> proving there is nothing sensible to automate yet, or take −1 Motivation (everyone) and add
> a new feature (Work Cost 2, Low complexity) nobody asked for.

> **MANDATORY FUN (OFFSITE)** - the team spends one of this week's five days at a "culture"
> offsite. Remove that card - nothing gets built on it - but everyone still gets **+1
> Motivation**; free catering and a day off the treadmill counts for something, even when it
> isn't real work.

> **PERFORMANCE REVIEW SEASON** - the team's next Reflect this week produces no Adaptability
> and no Shared Practice - the day goes to self-assessment forms instead of an actual
> after-action review. If no Reflect is played this week, ignore this card.

> **THE BARNUM EFFECT** - management circulates a "team personality profile," vague enough
> to fit anyone: **+1 Motivation** (everyone) - it feels personally true. It does **not**
> raise Trust, Capability, or Shared Practice: nobody actually learned anything about anybody,
> and feeling seen is not the same as being known.

> **SURPRISE AUDIT** - see `game/extensions/feature-quality-uncertainty/` (requires the
> feature Quality/Unclear extension - not in the base Event deck).

**Customer**
> **UNCLEAR REQUIREMENT** - see `game/extensions/feature-quality-uncertainty/` (requires the
> feature Quality/Unclear extension - not in the base Event deck).

> **NEGATIVE FEEDBACK** - pick a completed feature: it loses 2 progress (rework).

> **SCOPE CREEP** - add a new feature to the project (Work Cost 2, Low complexity).

> **EARLY DELIVERY REQUEST** - name one incomplete feature. If it's finished 3+ days before
> Day 35: +1 Motivation (everyone). No penalty if not.

> **CUSTOMER CHAMPION LEAVES** - the team's best point of contact is gone. Align actions
> cost +1 day until the team spends a Reflect to rebuild the relationship.

> **ALWAYS REACTING** - the team stops planning ahead and only reacts; deadlines slip
> sideways: the team **loses 1 Adaptability** (the Ledger coin, permanently). Quality: also
> lose 1 Motivation. *(Closes the gap where Adaptability had no way down at all.)*

**Team**
> **CONFLICT** - name two characters with clashing Values (Torso): −1 Trust each, unless the
> team spends a Coordinate day this week.

> **BURNOUT WARNING** - a character at Motivation 1 quits at the end of next week unless the
> team plays a Celebrate.

> **OUT SICK** - one character is unavailable for 2 working days (still on the team, no
> actions, no Motivation change).

> **SOMETHING TO MARK** - the next Celebrate this week also gives **+1 Trust**. Marking a win
> together is how a team learns it is one.

> **MENTORSHIP OPPORTUNITY** - any Learn actions this week also count as Coordinate (+Trust
> on top of the normal Learn effect).

**Environment**
> **TECH DEBT SURFACES** - pick a completed feature: it needs 1 more Work to actually be done.

> **TOOLING OUTAGE** - every Work card played this week produces 1 less output.

> **EXTERNAL DEPENDENCY DELAYED** - pick a feature: it can't progress until the team spends
> a Plan or Align day resolving the dependency.

> **UNEXPECTED OPPORTUNITY** - if the team already laid a Plan card this week, gain +1
> free Work on any one feature.

> **INDUSTRY CRISIS** - if Adaptability < 3: lose progress equal to 1 day's Work (the team's
> distracted). If Adaptability ≥ 3: no effect.

> **SHAKY GROUND** - a demo crashed in front of the customer: the team **loses 1 Capability**
> (move the Ledger coin down one, permanent, not a one-week penalty). Hierarchy: also lose 1
> Motivation. *(Closes the gap where Capability had no way down at all.)*

Still short of 30 cards - add more per category during playtesting, once specific rules are
tuned. Prioritize Team and Customer cards, since those interact most directly with Habitus
and Capital (§5.1).

## 12. Onboarding
A new character brings new Skills, Knowledge, Habitus, and Motivation - but doesn't
automatically understand how the team works. The team has to spend time onboarding them:
explaining context, teaching procedures, sharing knowledge, pairing them with someone,
building relationships.

**Rushed onboarding:** the new character can work right away, but their Work output is
**−1** (minimum 0), and they gain **no Capital**, no matter what they do, until Onboarding is
paid off. **Onboarding costs 2 days** of Learn and/or Coordinate involving the new character.
The moment those 2 days are played, the penalty ends immediately, even mid-week. This
creates the real onboarding dilemma: *"we're already behind - can we afford to onboard
properly?"*

> **This is Elias's established-outsiders dynamic, not a competence penalty.** The new
> character can be the most skilled person at the table and it changes nothing - the block on
> Capital is positional, not a judgment on ability. A long-tenured group's cohesion is what's
> missing, and only time spent together (Learn/Coordinate) closes that gap. See
> [../docs/theoretical-sources.md](../docs/theoretical-sources.md).

> **Sponsorship.** A character with Capital ≥ 4 may spend one of the two onboarding days
> paired with the newcomer (as a Coordinate or Learn naming both of them). If they do,
> **Onboarding finishes in 1 day instead of 2** - an established member's own standing can
> vouch for an outsider and shorten the gap, the same concept parked for Demo in §5.1.

## 13. Leaving the Team
- **Quit** - happens the instant a character's Motivation tokens hit 0 (§5).
- **Fired** - under real organisational pressure, management may remove the character with
  the lowest current contribution, if the project is far enough behind schedule. This should
  be a **dangerous** mechanism - it can start a negative spiral.

### Replacement - deliberately expensive
No like-for-like swap. Whenever a character quits or is fired:
- **The seat sits empty for the rest of that week** - nobody plays it, not even at reduced
  effect. That week's plan runs one character short.
- **At the start of the following week**, a new character joins with a fresh Habitus,
  Skills, Knowledge, and Motivation, and goes straight into **Rushed Onboarding (§12)**,
  same 2-day cost as ever. No shortcut, no buy-out.

This is now the **only** way Onboarding gets triggered - the old **NEW TEAM MEMBER** Event
card is retired. It used to depend on a random draw, which meant a whole subsystem could go
unseen in a short game (see [playability-assessment.md](../docs/playability-assessment.md),
M7). Now it's guaranteed, and it costs more than it used to: a lost week on top of the usual
onboarding tax, because losing someone should hurt more than the Motivation math alone says
it does. See [Designer's Notes](../docs/04-designers-notes.md) - this is also where **Brooks's
Law** gets a mechanic back, via the Event that took NEW TEAM MEMBER's card slot.

## 14. Sustainable Performance - two paths
- **Path A - Hero Team:** work extremely hard, invest almost nothing in learning,
  reflection, rest, or coordination. Short-term: great output. Long-term: Motivation falls,
  Trust falls, the team gets fragile, people may leave.
- **Path B - Sustainable High Performance:** invest in capability, shared practice, trust,
  adaptability, motivation. Short-term: less direct output. Long-term: higher, more
  sustainable productivity.

## 15. Resilience
The key hidden question: *what happens when something goes wrong?* A resilient team survives
someone leaving, changing requirements, unexpected problems, pressure, or failure. A fragile
team falls apart when its key person or process gets disrupted.

## 16. End of Project & Victory Conditions
At the end of Week 7 / Day 35, first check whether the project was delivered, then work out
a **Team Score** to see *how* the team got there:

**Team Score** = (features placed on the Tower × 10) + (sum of the four Team State tracks,
max 20) + (sum of every remaining character's Motivation tokens) − (10 × characters who quit
or were fired) − (2 × **unrepaid Flex markers**, §7).

> **Note for player counts other than 4:** the Motivation term scales with the number of
> characters, so the threshold below has to as well. Use **60 + (5 × number of starting
> characters)** - which is 80 at four players. Everything else in the game is player-count
> independent (§6.0); this is the one place it isn't, and it needs a playtest before it's
> trusted.

- **Project Failure** - not enough features delivered (the Tower is short of what was
  required). The team loses, no matter the Team Score.
- **Heroic Success** - all required features delivered, but Team Score **under 80**. The
  project succeeded; the team didn't.
- **Sustainable High Performance** *(the ideal outcome)* - all required features delivered
  **and** Team Score **80 or higher**.

80 is a first guess at four players, against a rough max of about 100 (6 features × 10 = 60,
+20 Team State, +20 Motivation, −0 quits, −0 unrepaid Flex). Playtest and adjust once real
scores come in - in particular, check that −2 per unrepaid Flex marker is *just* worse than
the day it bought. If teams routinely crunch week 7 and never look back, raise it.

## 17. Replayability
Variety should come from: the Project card chosen (§20), different Habitus builds, different
Skills, different Knowledge, Event draws, player decisions, staff changes, and different paths
the team takes as it develops. No game should have one obvious best sequence of moves.

## 18. Habits
A **Habit** is something the team has become, not something it currently has. Each one requires
deliberately investing in a Team State track - spending real days on the Activity that grows it,
not just stumbling into it - and each pays off exactly when **shit happens**: it makes a whole
category of Event permanently less painful, for good, even if the track later drops back down.

### One coin, two jobs
Each row of the Ledger has **one coin**. Walk it along the six wells as the track moves. When
it reaches the ringed well, **turn it over** - the reverse face is the Habit.

The coin can walk back down afterwards. **It never turns back over.** That single physical act
carries the whole rule: the track is what you have *now*, the face is what you have *become*,
and becoming is permanent. A team that pushed hard early and acquired Psychological Safety
keeps it for the rest of the game even if Trust falls back to 2 - the investment already
changed them.

That's also why they're called Habits rather than achievements or bonuses. In Bourdieu's terms
a habitus is a *durable acquired disposition* - it doesn't evaporate because you had a bad
week. See [../docs/habitus-model.md](../docs/habitus-model.md).

Starting with 5, and all of them are **team** habits, not individual ones. Each is acquired by
the group's investment, even when the trigger is one character crossing a threshold, and each
benefit is available to the whole team.

Each Habit is a **named construct from the literature**, not a badge invented for the game. The
board prints the source under the name, because the whole point is that these are findings.

| Habit | Source | Acquired at | Permanent effect on Events |
|---|---|---|---|
| **Psychological Safety** | Edmondson 1999 | Trust reaches 4 (through deliberate Coordinate spending). | Every **People**-category Event costs **1 less** ADAPT to cancel (minimum 1). |
| **Who Knows What** | Wegner 1986; Lewis 2003 - *transactive memory* | Capability reaches 4 (through deliberate Learn spending). | Every **Environment**-category Event costs **1 less** ADAPT (minimum 1). |
| **Shared Repertoire** | Lave & Wenger 1991; Wenger 1998 | Shared Practice reaches 4 (through deliberate Reflect/Coordinate spending). | Every **Management**-category Event costs **1 less** ADAPT (minimum 1). |
| **Team Reflexivity** | West 1996 | Adaptability reaches 4 (through deliberate Align/Reflect spending). | Every **Customer**-category Event costs **1 less** ADAPT (minimum 1). |
| **Authorized Voice** | Bourdieu 1991, *Language and Symbolic Power* | Standing reaches 5 - any one character's Capital (§5.1). | Once per week, any character may **cancel one Event completely**. *(Extension: `game/extensions/performance-review/` restores a second use, Collective Bargaining, as an alternative.)* |

**Why these names.** *Who Knows What* is Wegner's transactive memory: a group that knows who
holds which expertise, which is exactly what a Knowledge reaching three holders produces. It
replaces "Full Capability," which was consultancy vocabulary describing nothing. *Team
Reflexivity* is West's finding that teams which overtly reflect on their objectives and
processes, and change them, outperform teams that don't - which is precisely what Reflect does
to the Adaptability track. It replaces "Battle-Tested," which was folklore. *Authorized Voice*
is Bourdieu's authorized speaker: an utterance carries force because of the position of the
person making it, not its content - which is why the Demo gate is relative to the team average.

v0.1 ships 5. Add more once these are playtested and clearly working - record which ones got
acquired, and when, in the session's [playtest log entry](../playtests/README.md).

## 19. Prototype scope (v0.1)
3-6 players · 6 features · 18 total Work · 7 weeks × 5 team-days = **35 days** · 4 Team State
tracks · Motivation starts at 3 · 5-part Habitus build · ~30 Event cards · ~8-10 skills · a
simple individual/shared Knowledge system · 6 Project cards (§20). Keep components ugly at
first (index cards, cubes, sticky notes) - see
[../components/README.md](../components/README.md).

## 20. Project cards
**Every project uses the identical slot structure below** - same Work Costs, same Complexity,
same dependencies - so no project is harder than another and none of them need balancing. Only
the names change.

| Slot | Work Cost | Complexity | Depends on | Narrative role |
|---|---|---|---|---|
| **A** | 3 | Low | - | Independent side piece |
| **B** | 4 | Medium | - | Foundation |
| **C** | 4 | Medium | - | Foundation |
| **D** | 3 | High | **B** | Built on top of B |
| **E** | 2 | Low | - | The bit nobody wants to do |
| **F** | 2 | High | **C** | Built on top of C |

**18 Work in total**, of which 5 sits behind a gate (§3.2).

Six sectors are printed on sheet 9. The dependency in each is **causal, not arbitrary** - a
team should be able to say *why* D can't start, without looking anything up. Healthcare,
Finance, Retail, Construction and Events are played straight; **Software is the
tongue-in-cheek one** - the classic software engagement, where the customer hands over a
spreadsheet and cannot explain what it does.

### I - Patient Portal (Healthcare)
> A: Appointment reminders *(3, Low)* · **B: Patient login** *(4, Med)* · **C: Medical records
> API** *(4, Med)* · D: Referral network SSO *(3, High, needs B)* · E: Consent form capture
> *(2, Low)* · F: Billing history *(2, High, needs C)*
>
> **Why the gates hold:** you cannot federate identity out to a referring practice before you
> own identity yourself. And billing history is a *view over* the records API - without it
> there is literally nothing to bill against.

### II - Loan Platform (Finance)
> A: Branch locator *(3, Low)* · **B: Account ledger** *(4, Med)* · **C: Application intake**
> *(4, Med)* · D: Real-time balance sync *(3, High, needs B)* · E: Statement PDFs *(2, Low)* ·
> F: Credit scoring *(2, High, needs C)*
>
> **Why the gates hold:** sync compares live activity against the ledger - with no ledger there
> is nothing to reconcile against. And a credit score is computed *from* the application data,
> so until applications arrive there is nothing to score.

### III - The Excel Workflow (Software - played for the joke)
> A: Turn the screenshot into a spec *(3, Low)* · **B: Reverse-engineer the macros** *(4, Med)*
> · **C: Guess the data model** *(4, Med)* · D: Automate "the button that fixes it" *(3, High,
> needs B)* · E: Rename all the tabs *(2, Low)* · F: Reconcile three "final" sheets *(2, High,
> needs C)*
>
> **Why the gates hold:** you cannot automate a button whose behaviour nobody has reverse-
> engineered yet - least of all the customer, who only knows it "fixes it." And reconciling the
> final, final-v2, and final-v2-ACTUALLY-final sheets needs a data model to reconcile them
> *against* - one the customer never wrote down, because in their head there was only ever one
> version. **The customer isn't being difficult. They genuinely do not know what they're
> asking for**, and the whole project is downstream of that.

### IV - The Mobile App (Retail)
> A: App store listing *(3, Low)* · **B: Offline sync engine** *(4, Med)* · **C: Push
> notification service** *(4, Med)* · D: Sync conflict resolution *(3, High, needs B)* ·
> E: Accessibility pass *(2, Low)* · F: Rich notification actions *(2, High, needs C)*
>
> **Why the gates hold:** you can't resolve a conflict in data that doesn't sync offline yet -
> conflict resolution needs the sync engine to exist first. And a rich notification is still
> just a notification: there's no delivery service to decorate until it exists.

### V - Home Renovation (Construction)
> A: Permit application *(3, Low)* · **B: Framing and foundation** *(4, Med)* · **C: Plumbing
> and electrical rough-in** *(4, Med)* · D: Drywall and interior finishing *(3, High, needs B)*
> · E: Landscaping *(2, Low)* · F: Fixture installation *(2, High, needs C)*
>
> **Why the gates hold:** you can't hang drywall on a frame that doesn't exist yet - the finish
> work needs the frame to attach to. And you can't install a sink or a light switch before the
> pipe or wire behind that wall has actually been roughed in.

### VI - The Wedding (Events)
> A: Guest list and invitations *(3, Low)* · **B: Venue booking** *(4, Med)* · **C: Catering
> contract** *(4, Med)* · D: Seating chart and table layout *(3, High, needs B)* · E: Music
> playlist *(2, Low)* · F: Final headcount and catering order *(2, High, needs C)*
>
> **Why the gates hold:** you can't lay out tables for a floor plan you don't have yet - the
> seating chart needs the venue. And the final catering order is a number derived from the
> signed contract; there's nothing to finalize until the contract exists.

### Why this isn't just decoration
It has no mechanical effect and it shouldn't have one - that's what keeps the projects
swappable and unbalanceable. But it does three things that matter:

1. **Dependencies stop being a lookup.** *"We can't do the backfill until the schema lands"* is
   a sentence a team reasons with. *"D depends on B"* is a table you check.
2. **Events land as stories.** UNCLEAR REQUIREMENT on *the reporting module* is a moment.
   UNCLEAR REQUIREMENT on *Feature C* is admin.
3. **It gives Knowledge something to be about.** §8's individual Knowledge is currently
   abstract - *"Anna knows customer requirement pattern A."* With a project on the table it
   becomes *"Anna has worked with this payment provider before,"* which the team can actually
   reason about when deciding whether to spend one of five precious days teaching it to
   someone else.

Write the chosen project's feature names straight onto the six feature cards. Everything else
in the rules keeps referring to A - F.

## Appendix
The thinking behind the game - Bourdieu, Vygotsky, Wenger & Lave, Edmondson, Brooks, West,
Foucault, Elias, Marx, and where each one does and doesn't land on these mechanics - moved to
its own document: **[Designer's Notes](../docs/04-designers-notes.md)** (Level 4 of the
[reading order](../README.md#reading-order)). Nothing in it changes a rule.

