# Habitus Model

Status: **v0.1 - core character-creation model.**

Habitus, in Bourdieu's sense, isn't a personality trait or a list of stats. It's a tendency
to act and see the world in certain ways, shaped by your upbringing and experience. It
decides what feels natural to you, what you notice, and what you think you're capable of. In
this game, habitus has to actually change how a character plays - not just change a number.

## The core split
The character is built from five physical parts. The first four build the habitus. The fifth
is capability, and it's kept separate on purpose:

| Part | Represents | Bourdieu connection | Mechanical effect |
|---|---|---|---|
| **Base** | Upbringing / family background | Social conditions, incorporated history | Starting assumptions, social capital, what feels familiar |
| **Legs** | Education & inclination | Cultural capital, dispositions | What kinds of problems the character is naturally good at |
| **Torso** | Values | Durable preferences | What feels *right* to do, and what causes tension |
| **Head** | Perception & how they react under pressure | Schemes of perception, bodily hexis | How the character reads a situation and reacts on instinct. This is where **Pressure Response** (Take Charge / Analyze / Support / Challenge / Withdraw) becomes something physical instead of a line on a card - and it's what the **Hero** move (rulebook §5.1) keys off: every Event names one Pressure Response, and only a character with that Head can cancel it. |
| **Item** | Skills & tools (held) | Capability, not habitus | What the character can actually *do* |

Arms are sculpted into the Torso, not a separate swappable piece. A loose arm is fragile to
print and to peg reliably. A small held Item does the same job - showing capability - without
the risk of breaking.

**Same skill, different person:** two characters can both have "Facilitation." One grew up in
a hierarchical family, studied business, and values status - they'll run a meeting well, but
they'll also defer to seniority without thinking. The other grew up in a collaborative
family, studied psychology, and values autonomy - they'll run the same meeting, but push back
on the boss. Same skill, different habitus, different behaviour. That difference - not the
skill itself - is where habitus turns into a game mechanic. For example, when an Event puts a
micromanaging boss in the room.

## Build options (character creation)
- **Base - Opvækst (upbringing):** Bookish, Hands-On, Sheltered, Strict, Competitive - exactly
  five, and every one names a condition of the home you grew up in (what was normal there, how
  it ran, what it valued), never a parent's job. That's deliberate: Bourdieu's incorporated
  history is about the practices and conditions a childhood installs, not an occupation label.
- **Legs - Uddannelse & tilbøjelighed (education & inclination):** e.g. technical, academic,
  practical, creative, commercial, social, analytical, organisational.
- **Torso - Værdier (values, pick one):** Autonomy, Hierarchy, Community, Quality, Recognition -
  exactly five, because Torso is also **Need** (see below): whichever value you're dealt
  is both how Events land on you and what you need from the team from week 3 on.
- **Head - Pressure Response (pick one):** Take Charge / Analyze / Support / Challenge /
  Withdraw - sculpted as its own expression or pose. Also what Event cards name for the
  **Hero** move (rulebook §5.1) - exactly one of these five, once per game, cancels an Event.
- **Item - Værktøjer & færdigheder (skills, 2-3):** e.g. technical, planning, facilitation,
  communication, leadership, analysis, customer, quality - shown as a small held prop (laptop,
  phone, clipboard, coffee cup, wrench, etc.).

## Other character traits (not physical parts, tracked on the character card)
- **Need** is not a separate deal - **it is your Torso**, read a second way from week 3 on
  (see [../rules/rulebook.md](../rules/rulebook.md) §5.1). Nothing extra to print, deal or write
  down: the five Torso values (Autonomy, Hierarchy, Community, Quality, Recognition) double as
  the five Need conditions. It was never a *team* need - it's personal, same as Motivation.
- **Individual Knowledge** doesn't exist any more - what a character knows is which squares
  they cover on the shared **Zone** board (board 4), set by their **Legs** (row) and **Item**
  (column) at setup and grown by Learn/Teach from there. See
  [../rules/rulebook.md](../rules/rulebook.md) §8.

## Design rule: habitus is a trade-off, never a flat bonus
Never write a habitus effect as "+1 to X." Always pair a **strength** (habitus pays off) with
a **tendency** (habitus taken too far costs something) - **on the same currency, opposite
condition**, mirroring Base's Learn/Teach pattern. One card, one mechanic, viewed from two
sides - never two unrelated mechanics bolted together, and never two different currencies.

> **Base used to be the one exception** - Bookish/Hands-On/Competitive were printed as flat
> "+1 Work on two features," which is exactly the mistake this rule warns against: with
> nothing restricting who works which feature, the team would just always route that
> character's Work to the bonus features, so the +1 fired for free every time. Pairing it with
> a Work tendency didn't fix that either - a team can always dodge a bad *feature* fit by
> working in parallel. **Fixed by moving Base off Work entirely**, in
> [../rules/rulebook.md](../rules/rulebook.md) §5.2: every Base option now pairs a strength and
> tendency on the character's own **Motivation** (Learn, Teach, Overtime, Hero) - personal, so
> there's nothing left to route around. **This single-currency pattern is now the rule for
> every row, not just Base's exception** - Head, Torso and any future row pair strength and
> tendency on one currency, opposite condition, same as Learn/Teach.

> **Elite Athlete - Strength:** when the team is under real pressure and **Trust ≥ 4**, you
> take charge and it lands: **+1 Motivation**.
> **Elite Athlete - Tendency:** take the same charge with **Trust ≤ 1**, and it reads
> as overreach instead: **−1 Motivation**.

This pairs with the Head/Pressure Response choice - "Elite Athlete" naturally reads as Take
Charge, so match the strength/tendency to whichever Head the player picked.

The same rule applies to **Motivation**, not just to strengths and tendencies. An Event or
Activity that touches a character's Values (Torso) or Pressure Response (Head) shouldn't cost
or reward every character the same number of tokens. "Everyone: −1 Motivation" is a fine
default - but check first whether a specific Torso or Head would read the moment
differently. See [../rules/rulebook.md](../rules/rulebook.md) §5 for two worked examples
(BOSS MICROMANAGES, ANOTHER STATUS MEETING).

## Capital & field: why habitus doesn't always pay off
Habitus is only part of Bourdieu's picture. The other two pieces are **capital** and
**field**. The same habitus can land differently depending on how much capital you hold
*within a specific field* - because every field has its own rules about whose behaviour
counts as legitimate. A Take Charge instinct reads as leadership from someone with standing,
and as overreach from someone without it. Same habitus, different position, different
result.

**Here, the field is the team itself.** It's small and temporary, but it still has its own
sense of who's earned the right to take charge, be listened to, or be trusted with a
judgment call. That standing is tracked as **Capital** (0-5, starting at 2 for everyone - nobody's proven anything yet). It's defined mechanically in
[../rules/rulebook.md](../rules/rulebook.md) §5.1.

### Capital has forms, and they convert
The piece v0.1 originally left out - and the reason §5.1 deadlocked (see **B4** in the
[playability assessment](./playability-assessment.md)). In *The Forms of Capital* (1986)
Bourdieu's point is that capital isn't one substance but several, and that the interesting
action is them **converting into each other**:

| Form | What it is | In this game |
|---|---|---|
| **Cultural** | Education, credentials, embodied know-how | **Knowledge** and **Skills** - i.e. **Base** (upbringing) and **Legs** (education) |
| **Social** | Networks, relationships, obligations | **Trust**, and the relationships Coordinate builds |
| **Symbolic** | Prestige, standing, the right to be listened to | **Capital** (§5.1) |

Symbolic capital is what the other forms *become* once the field **recognises** them as
legitimate. So standing is never self-generating - it's converted, in public, out of something
you already hold. Two consequences the rules have to respect:

- **Teaching converts cultural → symbolic.** Giving your knowledge away is how it becomes
  standing. Hoarding it keeps you *needed* but never makes you *respected* - which is what
  finally gives the KNOWLEDGE HOARDING event some teeth.
- **Capital is relational, not absolute.** Its value is set by how much you hold *relative to
  everyone else in the field*. A fixed threshold ("you need 3") is un-Bourdieusian; a moving
  one ("you need more than the room's average") is the theory working.

And newcomers with no standing get it by **consecration** - being sponsored by someone the
field already recognises, who lends their legitimacy and carries some of the risk
(*The Rules of Art*; *Homo Academicus*).

This is also why **Base and Legs must have mechanical effects**: in Bourdieu's account they
are precisely where inherited cultural capital comes from. Leaving them inert isn't a missing
bonus, it's the theory going unimplemented.

## The rest of Bourdieu

Habitus, capital and field are the famous three, but the model is incomplete without four
more. Three of them are **already in the game** and were simply never named - which is worth
knowing, because an unnamed mechanic drifts.

### Illusio - why anyone plays at all
*Illusio* is the investment in the game: believing the stakes of this particular field are
worth pursuing. It isn't enthusiasm, it's being *taken in* by the game enough to compete in
it. Lose your illusio and you don't play badly - you leave.

> **This is Motivation.** And it's why the quit rule is right: at zero Motivation the
> character doesn't work at −5 efficiency, they *walk out of the field*. A character with no
> illusio isn't a bad employee; they're no longer playing.

It also justifies Motivation being a **currency you can spend** (§6.0): burning illusio for
one more push is exactly what the Hero path does, and it's why it runs out.

### Doxa - what goes without saying
*Doxa* is the field's unquestioned common sense: the rules so taken for granted nobody thinks
to challenge them.

> **This is why Events are mandatory.** Nobody at the table gets to say "we simply decline
> the status meeting." The team can absorb it, plan around it, or spend Trust to cancel it - > but the option to refuse the field's demands is not on the board. That absence *is* the
> mechanic. Do not add a "refuse the Event" action without understanding that it would delete
> doxa from the game.

### Symbolic violence and misrecognition - the gate nobody has to enforce
Bourdieu's *symbolic violence* is domination that works because the dominated accept it as
natural rather than arbitrary - *méconnaissance*, misrecognition.

> **This is the relative Capital threshold** (§5.1). No rule says "the low-Capital character
> must stay quiet." The team works out for itself that they shouldn't be the one to Demo, and
> then enforces it on themselves in the name of playing well. A player *choosing* to sideline
> their own character because it's optimal is symbolic violence reproduced at the table - and
> it happens without a single line of rules text instructing it.
>
> Worth watching for in playtest: does anyone notice they did this?

### Hysteresis - when the habitus stops fitting the field
The *hysteresis effect* (Bourdieu's "Don Quixote effect"): habitus is durable and slow, so
when a field changes suddenly, dispositions that used to pay off keep firing and now misfire.
People carry on doing the thing that used to work.

> **Not currently in the game.** The nearest thing is the REORGANISATION event, which only
> re-onboards people. A proper hysteresis event would be:
>
> **THE GROUND SHIFTS** - *until the end of the project, one named Head's **strength** no
> longer applies; its **tendency** still does.* The disposition hasn't changed. The field has.
>
> That is the single sharpest expression of Bourdieu available to this game, it costs one
> card, and it would make the Head choice genuinely load-bearing late on. **Flagged, not
> applied** - it's harsh, and it should be tested only after the Head strengths are known to
> work at all.

### Coverage

| Concept | Status |
|---|---|
| **Habitus** | ✅ The five-part figure |
| **Field** | ✅ The team itself (§5.1) |
| **Capital - forms and convertibility** | ✅ Knowledge/Trust → Capital, teaching and delivering |
| **Capital as relational position** | ✅ Demo needs ≥ the team average |
| **Consecration** | ⏸ Sponsorship, written but deliberately inactive (§5.1) |
| **Illusio** | ✅ Motivation, incl. quitting at 0 - now named |
| **Doxa** | ✅ Events cannot be refused - now named |
| **Symbolic violence / misrecognition** | ✅ The relative Capital gate - now named |
| **Hysteresis** | ❌ **The one real gap.** Proposal above. |


This turns the trigger pattern into three parts, not two: **when [Event X] happens, if a
character's habitus is [Y] and their Capital clears a threshold, then [Z].** The
strength/tendency pairing above still applies - Capital just decides whether the *strength*
half actually lands.

## The physical piece
The miniature is a **modular office-worker figure with five interchangeable parts** - base,
legs, torso, head, item - so the four habitus layers and the one capability layer are all
visible at the table, not just written on a card. See
[../components/3d-models/README.md](../components/3d-models/README.md) for the print design.

## This is the game's opening move
Character creation is not a pre-game admin step done off to the side - it **is** turn zero.
Each player is **dealt** five parts at random and assembles their own Base → Legs → Torso →
Head → Item figure, in that order, before any project rule is explained (see
[../rules/rulebook.md](../rules/rulebook.md) §3.1).

**Dealt, not chosen - and that is the more faithful reading.** Choosing your own habitus was
always slightly against the grain of the theory. Nobody selects their upbringing, their
schooling, or what they do by instinct when the pressure comes on. You are handed a person and
have to play them; the interesting question is what you do with what you were given, which is
Bourdieu's question rather than a character-builder's.

It doubles as onboarding: a new player is already doing something concrete and irreversible
(building a little figure that is visibly *theirs*) before they need to understand a single
rule - a direct application of the situated-learning implication in the
`board-game-playtesting` skill (participate first, comprehend fully later). Dealing the parts
rather than choosing them removes five decisions per player from a table that doesn't yet know
what the words mean, while keeping the part that matters: their hands are on the game.
