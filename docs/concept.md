# Concept

Status: **v0.1 - locked for prototyping.**

- **Working title:** High-Performance Team
- **Player count:** 3-6 - and the game does **not** change shape with the count. The week is
  five team-days whatever the size of the team.
- **Play time target:** 60-90 minutes
- **Game type:** Cooperative strategy / simulation
- **In-fiction duration:** 7 weeks / 35 working days - played as **7 weekly turns of five
  team-days each** (**35 days** total budget, regardless of player count)
- **Core theme:** A team delivers a project against a hard deadline. Along the way, they
  either become a real high-performing team, or they don't.
- **Core fantasy:** Every week you commit the team's five days - build, plan, coordinate,
  align, teach, demo, reflect, rest, or sit through a meeting - **before you find out what's
  coming.** Then reality lands on the plan you already made. Each character's habitus turns
  the same choice into different behaviour.
- **Core mechanic(s):** The game opens with every player physically building their
  character's habitus out of five parts (Base → Legs → Torso → Head → Item - see
  [habitus-model.md](./habitus-model.md)). Then it's **7 weekly turns**: lay five Activity
  cards across Monday - Friday → draw the Events → adapt what you still can → the week runs
  left to right. Backed by four Team State tracks (Trust, Capability, Shared Practice,
  Adaptability) plus personal Motivation and Knowledge - all shaped by the habitus built at
  the start.
- **Target audience:** Cooperative-strategy hobbyists. It has to work as a good coop game
  first, and a "team simulation" second - see Non-goal below.
- **Comparable games:** Sits next to cooperative pressure games like Pandemic - a race
  against a clock - but here the resource under pressure is the team itself, not an outside
  threat.

## The dials (stated explicitly, not left to feel)

**Skill expression - the target curve.** This is the number every balance decision gets
checked against:

| How the table plays | Chance of delivering all six features |
|---|---|
| Randomly | **~5%** |
| Competently | **~50%** |
| Perfectly | **~95%** |

A 90-point spread between random and perfect play is a deliberate choice: **this is a
skill game, not a luck game.** Events supply variance and pressure, but they must never be
the main determinant of the outcome. If a playtest shows good play losing to a bad draw, the
Events are too strong - not the team too weak.

The two ends fail for *different reasons*, and that's what makes the curve work:
- **Random play dies to Motivation.** Never resting means quits by week 3, and the team
  collapses before the schedule ever becomes the problem.
- **Skilled play is constrained by the schedule** - the absorption cap, the dependency gates,
  and the 140 person-day budget.

**Luck vs. skill:** strongly skill-weighted. **Length:** one evening (~85 minutes), 7 turns.
**Complexity:** medium-heavy, but front-loaded into a build ritual rather than a rules
lecture.

## Design goals
The game should make players **feel** these things, not read about them:
1. Time is finite.
2. Working hard right now isn't always the smart move.
3. Teams get better through social learning.
4. Shared habits make a team faster.
5. A strong team can get too rigid.
6. Trust is what lets people challenge, learn, and adapt.
7. The environment affects motivation.
8. Knowledge stuck in one person's head makes a team fragile.
9. Losing a person can really hurt a team.
10. Working sustainably is different from working like a hero.

## Non-goal
This shouldn't feel like a corporate training exercise. It should feel like a good
cooperative strategy game that just happens to model teams unusually well.

## Theoretical grounding (kept under the hood)
- **Bourdieu** - habitus, capital, field, illusio, doxa, symbolic violence.
- **Vygotsky** - the zone of proximal development, mediation by tools, social learning, the
  move from between-people to inside-the-person.
- **Wenger** - community of practice, shared repertoire, participation and reification,
  legitimate peripheral participation.

Players should learn this by playing, not by being told about it. If a mechanic needs a
lecture to make sense, fix the mechanic - don't add a footnote to the rulebook. **No component
ever names a theorist.**

### Where each idea actually lives
Full detail in [habitus-model.md](./habitus-model.md) (Bourdieu) and
[team-learning-model.md](./team-learning-model.md) (Vygotsky, Wenger). In brief:

| Idea | Mechanic |
|---|---|
| Habitus | The five-part figure you build before any rule is read |
| Field | The team itself |
| Capital, and its convertibility | Teaching and delivering convert Knowledge into standing |
| Capital as *position*, not substance | Demo needs Capital ≥ the team average |
| **Illusio** | **Motivation - and why zero means you leave, not that you work badly** |
| **Doxa** | **Events cannot be refused. The absence of that option is the mechanic.** |
| **Symbolic violence** | **The team sidelines its own low-Capital character, unprompted** |
| Zone of Proximal Development, scaffolding, the MKO | Learn - and it costs the teacher their day too |
| Mediation by tools | The Item (the weakest link - see the open question in the model doc) |
| Between-people → inside-the-person | Knowledge becomes Shared Practice at three holders |
| Mutual engagement / joint enterprise / shared repertoire | Coordinate / Align / the Shared Practice track |
| Participation ↔ reification | Work and Coordinate vs. Reflect, Demo, and the Tower itself |
| Legitimate peripheral participation | Onboarding: a newcomer does real work from day one, at reduced effect |
| Identity - learning as becoming | Capital and the figure, running on one track |

Two ideas are borrowed from outside the three: **psychological safety** (Edmondson) is what
Trust stands for. **Brooks's Law** (Brooks) was the other - it used to be the feature
absorption cap, until that cap was removed (rulebook v0.19) so a team can pile every day into
Work if it wants to. It has a mechanic again as of v0.20 - the **MORE HANDS** Event card; see
[Designer's Notes](./04-designers-notes.md) for the full story.

**Two known gaps**, both flagged in the model docs and neither blocking a playtest:
Bourdieu's **hysteresis** has no mechanic, and Vygotsky's **mediation** is thin - the Item is
thematically a mediating artifact but mechanically just a spare person-day.

### Four more sources, checked against the design after the fact
**Michael A. West** (team effectiveness, team reflexivity), **Michel Foucault** (power and
visibility), **Norbert Elias** (figurations, established-outsiders), and **Karl Marx**
(alienation, division of labour) were each researched against the existing mechanics - full
findings, including the honest tensions and the one thinker (Marx) who mostly reveals what this
game *doesn't* do, in [theoretical-sources.md](./theoretical-sources.md). A short, readable
version lives in the rulebook's own Appendix.

## The core question
> "If you only had 35 working days, how would you spend them?"

And underneath that:
> "How do you turn a group of individuals into a real high-performing team before the
> deadline arrives?"

The game works if a playtester says something like *"we actually had enough time, we just
spent it badly"* or *"we delivered everything, but that team is completely burned out"* - without anyone telling them that was the point.

## Changelog
- **v0.2 → v0.3 (the week is five team-days).** The week's five days belong to the **team**,
  not to each player. Three players or six, the week is still five Activity cards - so the
  budget is a flat **35 days** and the game is player-count independent. Adding people gives
  **more options, not more actions** (wider Skill and Knowledge coverage), and **more people to
  keep motivated**, since the weekly grind hits everyone while a Rest still costs one of five
  days. Work totals recalibrated 66 → **18**.
  Cards now resolve **Monday to Friday in the order you laid them**, which deleted the fixed
  resolution order and turned sequencing into a player decision.
- **v0.1 → v0.2 (turn structure).** The turn became the **week**, not the day: you commit the
  whole week *before* the Events are drawn, then reality lands on the committed plan. The
  fiction (7 weeks / 35 working days) is unchanged - only the grain of decision-making moved.
  Two reasons: 35 turns could not fit a 90-minute session (**B3b** in the
  [playability assessment](./playability-assessment.md)), and committing before knowing is a
  far better expression of design goals 1, 2 and 5 than choosing one day at a time with full
  information. Adaptability got a real job: the number of cards you may re-lay after the Events
  land.
