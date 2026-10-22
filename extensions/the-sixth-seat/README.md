# Extension: The Sixth Seat

**Track:** B - additive (new content, not cut from the base game). **Requires:** the base game
(rulebook v0.36 or later). **Status: ideas only, drafted 2026-10-17. No rules text yet, never
played.** Every number below is a first guess.

## What this pack is for
The base game already allows 3-6 players (concept.md), and the week stays five team-days at any
size (§6.0). A sixth player in the base game is just a sixth copy of a character. This pack gives
the sixth chair **a role of its own**: the **Estimator**, who works before week 1 and then
doubles as the team's reserve, so a quit has more than one possible answer.

## Hypotheses and the test that would confirm each
There is no playtest finding that asks for this pack, so it does not go through the evidence
gate that Track A packs do. Each idea starts from something already on record:

| Idea | Grounded in | Test that would confirm it |
|---|---|---|
| A job before week 1 | Week 1 is the most over-loaded week (2026-09-25: lots of text that makes no sense yet). A sixth player who is busy elsewhere until week 2 fits the staged reveal (§3.0). | Six players, one is the Estimator. Does week 1 get faster for the other five, and is the Estimator bored or engaged? |
| Forecasting delivery | "Should there be deadlines on features?" (2026-09-25, open). | Compare the forecast with what actually banked. Is the gap interesting or just noise? |
| Alternatives to Onboarding | "Should there be consequences if someone quits?" (2026-09-25, open); §13: the seat sits empty and the Onboarding card costs a day. | Force a quit in week 3 and try one alternative. Does losing someone still hurt more than the Motivation maths says (§13)? |

## Part 1 - Starting by estimating, before week 1
A **Week 0** of about five minutes, before the staged week 1 (§3.0). The sixth player has no
figure yet. Their job is the estimate, and week 1 is the only week they watch before joining.

Work Cost (§3.2) is measured in Work, but the team pays in **days**, and the number of days a
feature takes depends on Capability, Shared Practice and Events (§4, §10). So the thing to
estimate is not "how big is it" but **"which week will it be banked?"**. That is a real forecast,
it works with the fixed Work Costs, and it needs no hidden information.

**E1 - Forecast (recommended first test).** The Estimator places one **week marker** (1-7) on each
of the six features, in public, before anyone plays a card.
- Banked **on or before** its week: +1 Capital to the Estimator (once per feature, cap 3 for the game).
- Banked **after** its week: Trust -1 once, at the week it was due (a missed date is felt by everyone).
- The forecast is never changed. It is read again at the end of week 7 as the debrief
  question: where were we wrong, and why?

**E2 - Planning poker, whole team.** Same markers, but all six players estimate with cards
and the Estimator only facilitates and writes down the median. Lowest-risk version: no scoring, it only
gives the table something to talk about before they have a figure to hide behind. Weakest on its own.

**E3 - Pressure to pad.** Management (the box, or a player) tells the Estimator the date they
want. The Estimator announces any forecast, but secretly writes their own true guess. At the end
the gap between the two is read aloud. This is closer to real estimation (sandbagging, bowing to a
deadline) but it adds a hidden-information layer to a game that is deliberately cooperative, so
test it last.

> **Costs are the same in every project (§3.2).** Hiding them would only work once for a group.
> If a later test wants a hidden cost, it needs variant feature cards (each cost +/-1), which is a
> bigger change than this pack.

## Part 2 - Alternatives to the Onboarding card
Base rule (§12, §13): when a character quits or is fired the team pays 40 Team Score and everyone
loses 1 Motivation, the seat stays empty until the team lays the **Onboarding** card (costs a day),
and the replacement arrives with a fresh habitus, Motivation 5, Capital 0.

In every option below **the -40 and the -1 Motivation for everyone stay**. The quit still hurts;
only the *replacement step* changes.

| | Option | Replaces | Cost to the team | Risk |
|---|---|---|---|---|
| **R1** | **Bench step-in.** The Estimator joins the plan at once: no Onboarding card, no day. They draw a fresh figure and start on **Motivation 3** and Capital 0. | Onboarding card | One day saved, but 2 Motivation lower than a base replacement | Makes a quit cheaper. -40 should still dominate, but the sim has not seen it. |
| **R2** | **The quitter becomes the Estimator.** The player who quit keeps their chair and takes the Estimator role (forecasts and watches; no figure, no Need). They can step in as R1 if a later character quits. The seat they left stays empty as in base, or is filled by another option. | Nobody leaves the table | None extra | The player who burned out first is still engaged, which is the point. Overlaps in spirit with **Saboteur** (`../saboteur/`); do not use both. Works at five players, where there is no sixth. |
| **R3** | **Handover.** Before they go, the quitter hands over: **one free square** on their Zone row is copied to a teammate who has a free adjacent square (no Teach card, no day, Zone rules otherwise as §8). | Only adds to base, or to R1/R2/R4 | None | Softens the Knowledge loss of KEY SPECIALIST LEAVES. May make quitting too friendly. |
| **R4** | **Contractor.** Instead of Onboarding, the team spends **2 adapt tokens**. A temporary character fills the seat for **2 weeks**: Motivation 5, no Capital, does not count toward Habits, and then leaves without a -40. | Onboarding card | 2 adapt tokens (the same currency as cancelling an Event) | A way to pay your way out of a quit. Adaptability is already contested (§4). Probably too cheap. |
| **R5** | **Run short.** Decline the replacement. The seat closes for good: no card, no day. The team loses a Motivation term and a Zone row, and the thresholds drop (§16). | Onboarding card | The seat itself | The honest answer to "do we need them back?" Already possible in base by never laying the card. This option only makes it a stated choice. |

## Where I would start
**E1 + R1 + R3** at a six-player table, with one quit forced in week 3. It uses the most of
what the sixth player brings (a job from minute one, a reserve when someone leaves) without
adding any hidden information. Then try **R2** at a five-player table.

## Components (not designed)
- **Estimator board:** week markers 1-7 and the six feature rows. A forecast strip on THE TEAM
  would be cleaner than a new board, but that is a design question.
- **Week markers x6** and a **BENCH** marker.
- **Spare habitus parts** (a sixth Base, Legs, Torso, Head and Item, plus a Need and a Hero tile),
  because the habitus deck holds five of each row. Base-game replacements already need a fresh
  figure, so this may exist anyway.
- Nothing 3D-printed yet. If the BENCH marker is a figure it needs an orientation and a
  supports call before it is printed (`board-game-3d-printing`).

## What this pack touches in the base game
Nothing is removed. When a rule is chosen, the base game needs **one signpost** only (and a
rulebook version bump) next to §12. Until then, the rulebook is untouched.

## Scoring
§16's thresholds read **5 x starting characters + 75 and + 125**. With a sixth character
(R1, or any sixth player who joins the plan) that is **105 and 155**. That note already says it
needs a playtest. The Estimator counts as a starting character only from the week they
join the plan.

## Open questions
- Does the Estimator have a hand on the Zone and a Need before joining the plan? As written,
  no: they have a forecast and nothing else.
- Does a sixth player who **never** has someone quit get enough to do after week 1? If not,
  give the Estimator a standing job in the weekly checklist (§6.1), for example reading the
  forecast out at the close.
- Is a missed forecast date a Trust hit (E1) or a Capital hit to the Estimator alone? The
  first spreads the blame to the whole team; the second punishes the one person who is not
  doing the work.
