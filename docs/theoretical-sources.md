# Theoretical Sources - the full list, and the research behind the new ones

Status: **research reference.** The three core theorists (Bourdieu, Vygotsky, Wenger) already
have dedicated model docs - this file doesn't repeat that work. It exists to do the same
thorough treatment for the sources added after the fact: **Michael A. West, Michel Foucault,
Norbert Elias, and Karl Marx** - what each one actually argues, why it's relevant to teamwork
in general, and where (if anywhere) it lands on this game's actual mechanics. **Lave** is
confirmed as a pairing with Wenger (legitimate peripheral participation) - see
[team-learning-model.md](./team-learning-model.md) §"Wenger - the basics"; no separate entry
needed here.

As with the rest of the design: **no component ever names a theorist**, and a mechanic that
needs a lecture to make sense is a mechanic to fix, not a footnote to add. This document is for
the designers, not the table.

## The full roster, at a glance

| Thinker | Field | Already covered in |
|---|---|---|
| Pierre Bourdieu | Sociology - practice theory | [habitus-model.md](./habitus-model.md) |
| Lev Vygotsky | Developmental psychology | [team-learning-model.md](./team-learning-model.md) |
| Etienne Wenger (with Lave) | Learning theory - communities of practice | [team-learning-model.md](./team-learning-model.md) |
| Amy Edmondson | Organizational behaviour - psychological safety | [team-learning-model.md](./team-learning-model.md) |
| Fred Brooks | Software engineering management | [team-learning-model.md](./team-learning-model.md) |
| **Michael A. West** | Organizational psychology - team effectiveness | **This document** |
| **Michel Foucault** | Philosophy/history - power and discipline | **This document** |
| **Norbert Elias** | Sociology - figurational/process sociology | **This document** |
| **Karl Marx** | Political economy - labour and alienation | **This document** |

---

## Michael A. West - team effectiveness and team reflexivity

**The theory.** West is an organizational psychologist whose work (much of it NHS- and
healthcare-focused) asks a blunt question: when is a group of people actually a *team*, rather
than a set of individuals who happen to share a manager? His answer rests on three conditions -
**shared objectives**, **task interdependence**, and **team boundedness** (a stable,
identifiable membership over time). Miss any of these and you have a "pseudo-team" - people
call it a team, but it doesn't function like one, and West's research repeatedly finds
pseudo-teams underperform even individuals working alone.

His second major contribution is **team reflexivity**: the extent to which a team stops,
looks at its own objectives, strategies and processes, and deliberately adjusts them, rather
than just ploughing on. Reflexivity is one of the best-evidenced predictors of team innovation
and adaptability in the organizational literature - a team that never reflects can be full of
skilled individuals and still fail to adapt.

**Relevance to teamwork generally.** West's "real team" test is a useful diagnostic for a lot of
corporate theatre - "my team" often means "my reporting line," not a bounded group with a
shared goal and real interdependence. Team reflexivity, meanwhile, is the empirical backbone of
why retrospectives, after-action reviews, and "lessons learned" sessions correlate with better
outcomes when they're taken seriously, and why they're theatre when they're not.

**Relevance to this game.**
- **§6.0's whole argument** - "the week belongs to the team, not the player," five days
  regardless of headcount - is West's *task interdependence* and *team boundedness* criteria
  turned into a hard rule rather than left as an aspiration. A bigger team gives **more options,
  not more actions**, precisely because West's model says realness doesn't scale with headcount.
- **Reflect** (§7) is close to a direct implementation of team reflexivity: a day spent
  explicitly examining how the team is working, banked as +1 Adaptability (and +1 Shared
  Practice if something changed since the last one). The existing citation for Reflect leans on
  Wenger's *reification* and Vygotsky's *internalization* (see
  [team-learning-model.md](./team-learning-model.md)) - West's reflexivity is arguably the more
  precise fit for *this specific card*, since reification is about turning experience into
  something shareable in general, while reflexivity is specifically about a team pausing to
  audit and adjust its own way of working. Worth holding in mind as a second, teamwork-specific
  lens on the same mechanic, not a replacement for the existing one.
- The **Project card's shared feature set** (§20) is West's *shared objectives* condition made
  physical - everyone at the table is working toward the same six named things, not five
  private agendas.

**Key works.** West, M.A., *Effective Teamwork: Practical Lessons from Organizational Research*
(various editions, Blackwell/BPS); West, M.A., "Reflexivity and Work Group Effectiveness" and
related team reflexivity literature with J. Lyubovnikova and colleagues.

---

## Michel Foucault - power, discipline, and the normalizing gaze

**The theory.** Foucault's *Discipline and Punish* (1975) argues that modern institutions
(prisons, schools, hospitals, factories) exercise power less through force and more through
**disciplinary techniques**: hierarchical observation (being watched), normalizing judgment
(being measured against others), and examination (the two combined - a visible, recorded
comparison against a norm). The **Panopticon** is his emblem of this: a design where subjects
know they *might* be watched at any moment, and so start watching - and disciplining -
themselves. Later work (his lectures on **governmentality**) extends this to how populations,
not just individuals, get managed through diffuse, distributed techniques rather than a single
ruler's command.

**Relevance to teamwork generally.** Performance dashboards, always-on status indicators, ticket
trackers, 360 reviews, OKR scorecards - these are disciplinary technologies in Foucault's exact
sense. They don't need a supervisor watching every second; they make performance perpetually
*legible*, and workers learn to self-monitor because the record is always there. This is not
automatically sinister (visibility can also build trust and fairness), but Foucault's point is
that it is never neutral either - visibility is a form of power, whoever's watching.

**Relevance to this game.**
- **The Ledger itself is a small panopticon.** Every Team State track, and every character's
  Capital, sits face-up on the table for the whole game. Nobody needs to *ask* how someone else
  is doing - standing is continuously, publicly legible. That's exactly the disciplinary
  visibility Foucault describes, running as a board mechanic rather than a metaphor.
- **PERFORMANCE REVIEW** (§11) is close to a named disciplinary examination: a single character
  singled out, measured, and docked Capital for it. It is Foucault's "examination" - hierarchical
  observation plus normalizing judgment - almost without translation.
- **Capital ≥ the team average**, not an absolute threshold (§5.1), can be read two ways at
  once, and it's worth naming both. Bourdieu's own account (relational capital, a position in a
  field) is the primary citation already used here. But Foucault's *normalization* makes the
  same point from a different angle: power doesn't need an external absolute standard, only a
  distribution to sit inside of - "the average" is itself a disciplinary instrument, not a
  neutral statistic. Bourdieu and Foucault were contemporaries in real tension with each other
  on exactly this point, so seeing both readings land on the same rule isn't a coincidence; it's
  the two of them arguing about the same phenomenon.
- **The honest limit.** Foucault is fundamentally suspicious of the "team gets better, people
  grow" narrative that Vygotsky and this game's design goals openly celebrate. A strict
  Foucauldian reading would say the Ledger's growth tracks are themselves a normalizing
  discourse that produces compliant, self-monitoring workers who *want* to be watched improving.
  The game doesn't mechanize that critique, and probably shouldn't - but it's the honest cost of
  using Foucault at all, and it belongs in this document rather than being smoothed over.

**Key works.** Foucault, M., *Discipline and Punish: The Birth of the Prison* (1975); his later
1970s lecture courses at the Collège de France on governmentality (published posthumously as
*Security, Territory, Population* and *The Birth of Biopolitics*).

---

## Norbert Elias - figurations, interdependence, and the established-outsiders dynamic

**The theory.** Elias's figurational (or "process") sociology rejects the standard split
between "the individual" and "society" as separate things in tension. For Elias there is no
free-standing individual prior to the group - people exist only within **figurations**: webs of
interdependence, chains of interlocking actions and intentions, in which power is always
relational and unevenly distributed but never held absolutely by one side (even the least
powerful person is still a link in the chain). *The Civilizing Process* (1939) traces how
self-restraint became internalized as interdependence intensified across European history. His
later, more directly team-relevant study - *The Established and the Outsiders* (with John
Scotson, 1965) - looked at a single town and found that a long-tenured resident group
("established") maintained informal status and gossip-based control over newer arrivals
("outsiders"), regardless of the outsiders' actual individual character or conduct. Cohesion and
tenure, not merit, produced the hierarchy.

**Relevance to teamwork generally.** Elias explains something every long-lived team already
knows and rarely names: a new hire can be more competent than half the room and still sit at
the bottom of the informal pecking order for months, purely because they haven't been part of
the group's shared history yet. It also explains why no team member's contribution can be
assessed in isolation - everyone's action is shaped by, and reshapes, the web of relationships
they sit inside.

**Relevance to this game.**
- **Onboarding** (§12) - a new character contributing at reduced effect until they're
  "onboarded," regardless of their actual Skills or Habitus - is Elias's established-outsiders
  dynamic turned into a rule. The penalty isn't a competence penalty; it's a *positional* one,
  exactly as Elias found: the group's cohesion, not the newcomer's ability, is what's missing.
- **Capital as always relative to the team, never absolute** (§5.1) is readable through Elias as
  much as through Bourdieu: there is no such thing as a free-standing individual Capital value,
  only a position inside the *current* figuration. Elias's rejection of "the individual" as a
  unit that exists before the group is arguably the deeper reason Capital was never allowed to
  be an absolute number in the first place.
- **Team State tracks belonging to the team, not to any one character**, is Elias's central
  claim made physical: Trust, Capability, Shared Practice and Adaptability are properties of the
  *interdependence itself*, not of any single node in it. No character "owns" a fraction of
  Trust; the web does.
- **KEY SPECIALIST LEAVES** (§11) is a clean demonstration of interdependence chains: remove one
  link, and see what the whole web actually loses (or doesn't, if the Knowledge was already
  shared) - the event only makes sense because nobody's contribution was ever really separable
  from everyone else's to begin with.

**Key works.** Elias, N., *The Civilizing Process* (1939, trans. 1969); Elias, N. & Scotson, J.,
*The Established and the Outsiders* (1965).

---

## Karl Marx - alienation, division of labour, and the honest limits of the fit

**The theory.** Marx's account of **alienation** (*Economic and Philosophic Manuscripts of
1844*) holds that under capitalist production the worker is estranged in four ways: from the
**product** of their labour (owned and controlled by someone else), from the **act** of labour
itself (coerced by necessity, not freely chosen), from their own **species-being** (creative,
deliberate capacity, reduced to bare survival), and from **other workers** (competition
replacing solidarity). Later work (*Capital*, Vol. 1, 1867) develops the **division of
labour** - fragmenting a worker's activity into narrow, repetitive tasks - and **commodity
fetishism**, where social relations between people come to appear as relations between things
(the product, the price). The *German Ideology* (with Engels, 1846) sketches the opposite ideal:
a "fully developed individual," not fragmented into one narrow trade, able to move between kinds
of work across a day.

**Relevance to teamwork generally.** Alienation is the direct ancestor of most modern
disengagement and burnout research - lack of autonomy, lack of visible ownership over outcomes,
and fragmented, meaningless task-slices are exactly the conditions Marx described a century and
a half earlier, minus the vocabulary. Marx's division-of-labour critique also underlies job-
design theory (autonomy, mastery, task variety) as a direct response to Taylorist task-splitting.

**Relevance to this game - and where it's actually a contrast, not a mirror.**
- **The Feature Tower is a striking image of the product of labour separating from the
  labourer**: no Work card carries a name, no block says who built it - the tower is anonymous,
  collective, "delivered work" walking distance from the hands that made it. That's the
  alienation-from-the-product image almost drawn to scale.
- **But this game is not a capitalist relation in Marx's sense, and that matters more than the
  resemblance above.** There is no owning class extracting surplus value from the team; the
  Tower's value - Team Score, the win condition - belongs to the team itself, collectively.
  Structurally this is closer to a worker-managed cooperative than a factory floor. Read
  honestly, a Marxist lens mostly reveals what's **absent** here - the alienation that comes from
  *someone else* owning what you built - rather than confirming what's present. That's a more
  useful and more honest finding than forcing a 1:1 mechanical map.
- **Division of labour is genuinely present**, though, in Skill-to-Activity matching, Domain
  expertise on named features, and starting Zone position (Legs × Item) - the team's early
  efficiency depends on narrow specialization. The game's own counter to this is **Learn/Teach**:
  covering more of the Zone board over time is structurally the same arc as Marx's "fully
  developed individual" overcoming fragmentation - a character who can do more kinds of work
  across the week, not fewer - even though the game never uses that language.
- **KNOWLEDGE HOARDING** (§11), and the rule that hoarding keeps you *needed* but never
  *respected* because only teaching converts to Capital, is close to an anti-alienation
  mechanic: it explicitly punishes treating your own labour-capacity as private property to be
  withheld, and rewards making it social instead - the opposite of alienation-from-other-workers.

**Key works.** Marx, K., *Economic and Philosophic Manuscripts of 1844* (the alienation
chapters); Marx, K., *Capital*, Vol. 1 (1867) (division of labour, commodity fetishism); Marx, K.
& Engels, F., *The German Ideology* (1846) (the "fully developed individual" passage).

---

## What this expanded roster actually buys the design

Being honest about the whole set, not just the flattering parts:

- **West** is the cleanest addition - a genuine teamwork researcher (not a general social
  theorist reused for teamwork) whose criteria already match design decisions the game made for
  other reasons. Low risk, high fit.
- **Elias** slots in almost as cleanly, and productively complicates the Bourdieu reading of
  Capital and onboarding rather than competing with it - the two were real intellectual
  neighbours (Elias significantly influenced Bourdieu), so this isn't force-fitting two
  incompatible traditions together.
- **Foucault** fits several mechanics well (the Ledger, PERFORMANCE REVIEW, the relative
  threshold) but sits in genuine tension with the game's own optimism about growth and capability
  - a tension worth keeping visible, not resolving.
- **Marx** is the biggest stretch, and the most interesting for exactly that reason: the honest
  finding is that this game depicts a **post-alienation** version of teamwork (the team owns
  what it builds), which makes Marx more useful as a *contrast case* than as a source of
  mechanics. That's a legitimate research result, not a failure to find a fit.

None of this changes a rule. It's a record of where the theory was checked against the
mechanics, and what was found - in keeping with the same honesty the model docs already apply
to Bourdieu and Vygotsky's own gaps.
