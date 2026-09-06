# Designer's Notes

**Level 4** of the game's [reading order](../README.md#reading-order) - the thinking behind the
game. This is the standard slot for this kind of content: most published games that bother to
explain themselves (*Root*, *Twilight Struggle*, *Pandemic Legacy*, *Scythe*) put it in a
Designer's Notes section, separate from the rules a table actually needs to play. Nothing here
changes a rule, and nothing here is required reading to play a single turn.

## Why this exists at all

**No component ever names a theorist**, and a mechanic that needs a lecture to make sense is a
mechanic to fix, not a footnote to add (see [design-guide.md](./design-guide.md)). This document
is for the designers, and for any player curious enough to ask "wait, why does Onboarding work
like *that*?" after the fact.

## The eight thinkers, and what each one is actually doing here

The game draws on eight thinkers, not one grand theory. Three carry most of the weight, two are
borrowed as single named findings, and four were added later to pressure-test the design from
outside the original three.

**The three the game is built on:**
- **Pierre Bourdieu** - habitus, capital, field. Why the figure is built before a single project
  rule is read, why Capital is never an absolute number, why Demo needs Capital ≥ the team
  average rather than "≥ 3." Full detail: [habitus-model.md](./habitus-model.md).
- **Lev Vygotsky** - the zone of proximal development. Why Learn costs the teacher a day too,
  why a Knowledge you just received can't be taught again this week.
- **Etienne Wenger**, with **Lave** for legitimate peripheral participation - communities of
  practice. Why Coordinate, Align, Reflect, Demo and Celebrate all exist as separate cards
  instead of one generic "team-building" action. Both detailed in
  [team-learning-model.md](./team-learning-model.md).

**Two borrowed findings, named rather than passed off as balance decisions:**
- **Amy Edmondson** - psychological safety. What Trust actually stands for.
- **Fred Brooks** - adding people to a late project makes it later. Lost its mechanic when the
  feature absorption cap was removed in rulebook v0.19, then **got a different one back in
  v0.20**: retiring the NEW TEAM MEMBER Event card (Onboarding now triggers automatically off
  a quit or firing, §13) freed a card slot for **MORE HANDS**, which halves the Work on
  whichever feature got the most piled onto it that week. Detailed in
  [team-learning-model.md](./team-learning-model.md).

**Four added later, to check the design from outside the original three:**
- **Michael A. West** - what actually makes a group of people a *team* (shared objectives, task
  interdependence, stable membership), and *team reflexivity* - a team pausing to examine and
  adjust its own way of working. The closest thing this list has to "already fully implemented
  before we knew the name" - see the full research for why no new mechanic was needed.
- **Michel Foucault** - power that works through visibility rather than force. The Ledger,
  face-up on the table all game, is a small version of exactly this; **Collective Bargaining**
  (the second use of Authorized Voice, §18) is close to a named act of collective resistance to
  individualized discipline.
- **Norbert Elias** - no individual exists outside the web of relationships around them; a
  long-tenured group holds informal status over newcomers regardless of the newcomers' actual
  ability. Why Onboarding penalises position, not skill, and why sponsorship can shorten it.
- **Karl Marx** - alienation, and the division of labour. The Feature Tower is anonymous,
  collective work with nobody's name on it - but this game is honestly closer to a worker-owned
  cooperative than a factory floor, so Marx mostly reveals what this game *doesn't* do to a
  team, more than what it does. **Cross-Trained** (§5.1) is the one place his critique of
  fragmented labour turns into an actual reward.

**Full research, citations, and the honest tensions** (including which readings are a stretch
and which aren't): [theoretical-sources.md](./theoretical-sources.md).

## Three known gaps, and one honest tension

Left visible on purpose, not smoothed over:
- Bourdieu's **hysteresis** has no mechanic.
- Vygotsky's **mediation** is thin - the Item is thematically a mediating artifact but
  mechanically just a spare person-day.
- Foucault's suspicion of "the team gets better" as a story sits in real tension with the whole
  design's optimism about growth. Nothing resolves this on purpose - see
  [theoretical-sources.md](./theoretical-sources.md) for the full argument.

## Where a citation actually lives on a physical component

The rule against naming theorists on components has exactly two carve-outs, both deliberate:
the **Ledger** (board 3/3b) prints a source under each Habit's name, and **board 4 (the Zone)**
prints a citation line under the grid - because on those two boards, and only those two, the
point being made *is* that these are findings, not folklore. Nowhere else earns it.

## Changelog of this document

This document was assembled from the rulebook's own former Appendix (moved out in rulebook.md
v0.18) plus the standalone research already done in theoretical-sources.md. See
[../rules/rulebook.md](../rules/rulebook.md) for the version history of the rules themselves;
this file doesn't carry rule versioning, since it can't change a rule by definition.
