# Theoretical Sources - the full list, and the research behind the new ones

Status: **research reference.** The three core theorists (Bourdieu, Vygotsky, Wenger) already
have dedicated model docs - this file doesn't repeat that work. It exists to do the same
thorough treatment for the sources added after the fact: **Michael A. West, Michel Foucault,
Norbert Elias, Karl Marx, Charles Goodhart, C. Northcote Parkinson, Derek de Solla Price, and
Melvin Conway** - what each one actually argues, why it's relevant to teamwork in general, and
where (if anywhere) it lands on this game's actual mechanics. **Lave** is confirmed as a
pairing with Wenger (legitimate peripheral participation) - see
[team-learning-model.md](./team-learning-model.md) §"Wenger - the basics"; no separate entry
needed here. **Dogfooding and Cunningham's Law** are covered too, right after Parkinson and
Conway respectively, but deliberately kept off the thinker roster - both are practitioner
aphorisms, not named theorists' findings, and this document draws that line honestly rather
than blurring it.

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
| **Charles Goodhart** | Economics - measurement and control | **This document** |
| **C. Northcote Parkinson** | Public administration - committee behaviour | **This document** |
| **Derek de Solla Price** | Bibliometrics/history of science - productivity distribution | **This document** |
| **Melvin Conway** | Software engineering - organizational design | **This document** |

**Not on this roster on purpose:** *dogfooding* (see the short note after Parkinson) and
*Cunningham's Law* (see the short note after Conway) aren't named theorists' findings - they're
practitioner aphorisms, and this document is honest about that distinction rather than
dressing them up as two more thinkers.

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

## Charles Goodhart - when the measure becomes the target

**The theory.** Goodhart's original 1975 point was narrow and monetary - a statistical
regularity used as a policy target stops behaving like the regularity that made it worth
targeting in the first place, because people and institutions change their behaviour in
response to being measured. The version everyone actually quotes is anthropologist Marilyn
Strathern's 1997 paraphrase: **"When a measure becomes a target, it ceases to be a good
measure."** The mechanism is simple - a proxy is chosen because the real goal is hard to
observe directly; once the proxy is rewarded, people optimize the proxy, and the gap between
proxy and goal is exactly where the damage accumulates.

**Relevance to teamwork generally.** Velocity, story points, lines of code, ticket-closure
counts, OKR scorecards - every one of these exists because "is the team actually effective" is
hard to measure directly. The moment any one of them becomes *the* target, teams learn to pad
estimates, split tickets for count, or close what's easy instead of what matters - not through
bad faith, but because the target is doing exactly what a target does. It sits close to
Foucault's normalizing gaze (above): both describe a measurement regime reshaping the behaviour
it was meant to only observe, from two different centuries and two different disciplines.

**Relevance to this game.**
- **§16's Team Score / victory-condition split is Goodhart's Law built as a win condition**,
  not just illustrated by one: **Team Score** is the proxy (features banked × 10, the four
  Team State tracks, remaining Motivation), and it is *always* possible to over-fit it - bank
  conservatively, avoid every risky Reflect or Celebrate, hoard Motivation instead of spending
  it on the team. That's exactly why **Heroic Success** (all features delivered, Team Score
  under 80) exists as its own named outcome, distinct from **Sustainable High Performance**:
  the rulebook was already worried about a team that optimizes the number instead of the thing
  the number was supposed to stand for, before anyone reached for Goodhart's name for it - "The
  project succeeded; the team didn't."
- **§16's own honesty about the scoring threshold** - "this is the one place [scoring] isn't
  [player-count independent], and it needs a playtest before it's trusted" - is itself a
  Goodhart-shaped worry: a fixed numeric line is exactly the kind of target that gets gamed
  once players learn precisely where it sits, and the rulebook is right to flag it as unproven
  rather than load-bearing.
- **THE AUDIT (§11)** is a small, self-contained Goodhart's Law event: it demands proof of a
  *proxy activity* - one card played as a **Workshop** - rather than measuring whether
  coordination actually improved, and its own footer already says the quiet part out loud:
  "No one person can be the answer." Measuring *that a meeting happened* is not the same as
  measuring *that anything got better*, and the card's whole bite is that the team can satisfy
  the letter of the requirement while missing the point.
- **No new mechanic is needed here.** Unlike West's reflexivity (which was "already fully
  implemented before we knew the name"), this is closer to *the design's own stated risk*
  finally getting its name - the victory-condition split already does the work.

**Key works.** Goodhart, C.A.E., "Problems of Monetary Management: The U.K. Experience" (1975);
Strathern, M., "'Improving ratings': audit in the British university system" (1997) - the
paraphrase most people actually quote.

---

## C. Northcote Parkinson - the law of triviality ("bikeshedding")

**The theory.** Parkinson's *Parkinson's Law: The Pursuit of Progress* (1957) includes the **law
of triviality**: a committee's time spent debating any agenda item is inversely proportional to
the sum of money (or stakes) involved. His illustration is a finance committee that waves
through a multi-million-pound nuclear reactor in minutes, then spends an hour arguing over the
cost of the staff bicycle shed roof - because everyone understands roofing and can hold an
opinion on it, while almost nobody feels qualified (or willing to be blamed later) to challenge
the reactor. Poul-Henning Kamp's 1999 FreeBSD mailing-list post popularized **"bikeshedding"**
as the verb for this specifically in software/engineering culture.

**Relevance to teamwork generally.** Big, consequential, genuinely hard decisions get
rubber-stamped precisely *because* they're hard to have a defensible opinion on, while small,
visible, easy-to-have-an-opinion-about decisions eat disproportionate meeting time - not
because they matter, but because everyone can participate without risk.

**Relevance to this game - no longer a gap.** **THE BIKESHED** (Event 19, sheet 8 - see
[../components/specs/cards-event-19-21-63x88mm-A4-portrait.md](../components/specs/cards-event-19-21-63x88mm-A4-portrait.md))
is a direct mechanic for this: the easiest unbanked feature gets +1 Work for free, while the
hardest one gets nothing that week - triviality rewarded, consequence starved, without ever
naming Parkinson on the card. Before this card existed, the closest material was:
- **STATUS MEETING and THE AUDIT** (§11, Management category), which dramatize "a day spent on
  process instead of the work" but don't specifically reward trivial-but-visible engagement
  over hard-but-consequential engagement - they're closer to Foucault's disciplinary
  examination (already cited above) than to Parkinson's triviality trap specifically.
- **UNCLEAR REQUIREMENT and SCOPE CREEP** (§11), which put a hard, ambiguous feature in front of
  the team without letting them dodge it for something easier - the problem bikeshedding would
  strike at, without the temptation itself being modelled.

Those two stay in the document as the *adjacent* material THE BIKESHED sits next to, not as a
replacement for it.

**Key works.** Parkinson, C.N., *Parkinson's Law: The Pursuit of Progress* (1957), ch. "High
Finance, or the Point of a Pyramid"; Kamp, P-H., "A Bike Shed (Any Colour Will Do)" (FreeBSD
mailing list, 1999).

---

## Dogfooding - a practitioner heuristic, not a listed thinker

Unlike everything else in this document, "dogfooding" (eat your own dog food) isn't a named
theorist's finding - it's an engineering aphorism, commonly traced to Microsoft in the late
1980s, for the idea that whoever makes a decision should also live with its consequences, or
they'll keep making the same bad call without ever feeling why it's bad. It's included here,
separately from the roster table above, because the honesty standard this document holds itself
to (naming the gaps, not smoothing them over) applies to *how a source is categorized* too, not
just to how well it fits.

**Relevance to teamwork generally.** A decision-maker insulated from the downstream effects of
their own call - a manager who never has to live inside the process they mandated - loses the
feedback loop that would otherwise correct them, and keeps making the same call.

**Relevance to this game - already present, not yet named.** The **Torso/Values row already
encodes exactly this asymmetry**, without the game ever using the word: **Autonomy** ("let me
get on with it") takes the Management-category Event hit directly and is immune to Environment,
while **Hierarchy** ("they must have a reason") takes the Environment hit and is immune to
Management - a Hierarchy-valued character is mechanically insulated from bad top-down decisions
precisely *because* they defer to them rather than owning them, while an Autonomy-valued
character feels every Management misstep directly, because they're the one making their own
calls. Dogfooding's failure mode and its cure are sitting on the same card already.

**A seam worth flagging, not touching.** The **Plan → Work** split is the one place the game
currently lets a decision (Plan) and its consequence (the Work it improves) land on two
different characters, with nothing requiring they be the same person - the literal opposite of
dogfooding. That's probably fine as-is (division of labour is part of the design - see Marx,
above), but if a future Event wanted to dramatize "the planner never does the work," that's the
existing seam to use. Plan's balance is already tuned, so treat this as a flag, not a change.

---

## Derek de Solla Price - productivity is a power law, not a bell curve

**The theory.** Price's *Little Science, Big Science* (1963) found that scientific output isn't
spread evenly across contributors - it clusters. His rough rule of thumb: **the square root of
the number of contributors produces about half the total output.** Ten contributors, roughly
three or four do half the work; a hundred, roughly ten. This builds on Alfred Lotka's earlier
bibliometric finding (1926) that publication counts follow a power-law-shaped distribution, not
a normal one. The popular software-culture version is "10x engineer" folklore, and the same
shape shows up in open-source commit histories, StackOverflow answer counts, and internal bug
triage logs.

**Relevance to teamwork generally.** Price's Law predicts that raw output concentration among a
few people is the *default* shape of any productive group, not a symptom of unfairness or a
fluke of this particular team. That raises a real design question for any organization: do you
protect and lean into that concentration (accept the bus-factor risk, let the core few carry
weight), or actively flatten it (mentorship, pairing, documentation) so the team survives losing
any one person? Both are legitimate responses; pretending the distribution is flat is not.

**Relevance to this game.**
- **KNOWLEDGE HOARDING** (§5.1, §11) already assumes a Price-shaped world: the card targets
  "whoever holds the most Knowledge," which presumes a concentrated holder exists in the first
  place, not an even spread. The card doesn't create the inequality - Price's Law says it was
  always going to be there - it just makes the team pay for tolerating it instead of converting
  it via Teach (§8).
- **MORE HANDS** (§11, Brooks - see [team-learning-model.md](./team-learning-model.md)) keys off
  "the feature with the most Work played on it this week," which only means anything because
  effort piles up unevenly across features and people in the first place - another place the
  design already assumes Price's shape rather than an even one.
- **Skill match bonuses (§7) and Habitus/Capital effects (§5.1)** deliberately let some
  characters produce more Work on features that fit their Skill - the game doesn't pretend
  everyone contributes equally; it prices the unevenness directly into the Work formula.
- **The honest tension.** The win condition's own framing pulls the other way: **Team Score
  belongs to the team, not to whoever last touched a block** (§10), and nothing on the Feature
  Tower carries a name. Price's Law says a small core probably produced most of the actual
  progress; the scoring and thematic framing insist on flattening credit back to the whole
  table regardless. Both can be true at once - the mechanics quietly assume concentration while
  the scoring and theme insist on collective credit - and this document isn't resolving that
  tension, only naming it, the same way it names Foucault's.

**Key works.** de Solla Price, D.J., *Little Science, Big Science* (1963); Lotka, A.J., "The
frequency distribution of scientific productivity" (1926) - the earlier bibliometric law
Price's argument builds on.

---

## Melvin Conway - organizations ship their org chart (and the Reverse Conway Maneuver)

**The theory.** Conway's 1968 paper "How Do Committees Invent?" argues that any organization
designing a system is constrained to produce a design that mirrors its own communication
structure - if four groups build a compiler, expect a four-pass compiler, because the system's
internal interfaces will trace the interfaces between the people who built it. The modern
corollary, the **Reverse (or Inverse) Conway Maneuver** - named and popularized by Matthew
Skelton and Manuel Pais in *Team Topologies* (2019), building on discussion going back to the
2000s DevOps community - flips the causality on purpose: instead of discovering your
architecture is whatever shape your org chart accidentally produced, you **design the team's
communication structure first**, deliberately, to induce the system architecture you actually
want.

**Relevance to teamwork generally.** Architecture and org chart are the same fact seen from two
sides. A team that wants a modular, loosely-coupled system needs modular, loosely-coupled
communication (or a small number of people who deliberately cross every boundary); a team that
wants one seamless, integrated product needs integrated communication. Trying to get one shape
of system out of the other shape of team is fighting the law, not using it - which is exactly
why the Reverse Conway Maneuver treats team topology as a design lever, not an afterthought.

**Relevance to this game - an unusually clean fit.**
- **The Zone board (§8) is a literal communication-structure matrix**, not a metaphor for one:
  rows are Education (Legs), columns are Skill (Item), and a covered square is a real,
  named link between a person's training and an instrument. The **Feature Tower - the "system"
  being designed - is built entirely out of Work produced through those exact links** (Skill
  match, §7). Conway's Law isn't being borrowed here; the team's covered squares on the Zone
  board *are* its communication structure, and the tower *is* the system that structure produces.
- **The dependency gates (§10)** - a feature physically unplaceable until its prerequisite lands
  - are the system's architecture (a strict build order) mirroring whatever the team's own
  attention happened to cover that week. If the team's de facto communication structure never
  reaches the Zone squares that would smooth the path to a gated feature, the system inherits
  that gap, exactly as Conway predicts.
- **Learn and Teach (§8) are the Reverse Conway Maneuver, played as a turn-by-turn choice.** A
  team that looks at which features gate which (§20, at setup) and *then* deliberately chooses
  its Learn/Teach targets to cover the rows/columns a gated feature will need - before the week
  that needs it, not after discovering the gap - is restructuring its own communication graph on
  purpose to get the system it wants, rather than accepting whatever shape its Work happened to
  fall into.
- **Cross-Trained** (§5.1) rewards exactly the capability the maneuver requires: a character who
  has covered three rows has deliberately reshaped their own place in the team's communication
  graph, ahead of need, not in response to a gap already discovered.

**Key works.** Conway, M.E., "How Do Committees Invent?" (*Datamation*, 1968); Skelton, M. &
Pais, M., *Team Topologies: Organizing Business and Technology Teams for Fast Flow* (2019) - the
standard modern reference for the Reverse/Inverse Conway Maneuver.

---

## Cunningham's Law - a practitioner heuristic, not a listed thinker

Like dogfooding, this one doesn't belong on the roster table above: **"the best way to get the
right answer on the Internet is not to ask a question, it's to post the wrong answer"** is
attributed to wiki inventor Ward Cunningham via a 2010 recollection from Steven McGeady;
Cunningham himself has said he doesn't recall coining it. It's internet folklore with a name
attached, not a citable finding - and it's kept separate here for the same honesty reason
dogfooding is.

**Relevance to teamwork generally.** Committing to a visible, falsifiable draft - even a wrong
one - reliably extracts more and better feedback than an open-ended question, because *correcting*
something has a lower social cost than *originating* something. It's the mechanism behind "rough
draft," "straw-man proposal," and "show, don't ask" review cultures.

**Relevance to this game.** **Demo** (§7, "Reveal a feature's Quality") is structurally this
exact move: instead of debating a feature's quality in the abstract, the team commits it
publicly to the field's judgment (Capital ≥ the table average, §5.1), and the correction - a bad
review costing Work and Capital, or a good one paying out - **is** the feedback, produced by
showing rather than asking. Nobody has to raise the question of whether the feature is good;
committing it wrong (or right) produces the answer directly. **Align**, by contrast, resolves
uncertainty the other way - by direct discussion, not by committing a guess and eating the
correction - so the game already models both routes to resolving ambiguity, under two different
cards, without either one ever needing this name.

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
- **Goodhart** is the second-cleanest addition after West - not because a mechanic was built for
  it, but because the victory-condition split (§16) was already worrying about exactly this
  before the name existed. Low risk, high fit, zero new rules required.
- **Parkinson** started as the honest miss of this batch, and no longer is: **THE BIKESHED**
  (Event 19, sheet 8) rewards trivial engagement and starves consequential engagement directly,
  closing the gap this document originally flagged.
- **Conway** is the other cleanest addition - the Zone board and Feature Tower already are a
  communication-structure-produces-system relationship, not a metaphor for one, and Learn/Teach
  already give the team a Reverse Conway lever it can choose to use or ignore.
- **Price** fits the mechanics (Knowledge concentration, Skill-match unevenness) but sits in the
  same kind of honest tension as Foucault: the collectivist scoring and "no block carries a
  name" framing quietly disagrees with what Price's Law predicts actually happened at the table.
- **Dogfooding and Cunningham's Law** are both practitioner aphorisms rather than theorists'
  findings; dogfooding also picked up a dedicated card (**LEADS FROM BEHIND**, Event 20, sheet 8)
  alongside the Autonomy/Hierarchy mirrored immunities it was already encoded in. Cunningham's
  Law is still just Demo's public-commitment structure, and doesn't need more than that.

None of this changes a rule. It's a record of where the theory was checked against the
mechanics, and what was found - in keeping with the same honesty the model docs already apply
to Bourdieu and Vygotsky's own gaps.
