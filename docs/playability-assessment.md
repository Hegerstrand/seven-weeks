# Playability Assessment - High-Performance Team v0.1

Status: **assessment of the v0.1 paper design, before first playtest.**
Assessed against [concept.md](./concept.md), [../rules/rulebook.md](../rules/rulebook.md),
[habitus-model.md](./habitus-model.md), and [../components/README.md](../components/README.md).

> **Headline verdict (original): v0.1 is not playable as written.** Not because the ideas are
> bad - the premise and the opening build ritual are genuinely strong - but because four
> specific defects stop a table from resolving a single day without house-ruling.
>
> **All are now closed.** B1 (§7 has exact numbers) · B2 (the currency is settled) · B3 (output
> bounded, absorption capped, Work totals derived) · B3b (**the week is the turn** - 7 turns,
> ~85 min) · B4 (Capital converts in; the Demo gate is relative to the team average) ·
> B5 (the schedule has slack).
>
> ⚠️ **v0.3 recalibration - read this before trusting any number above.** The designer
> clarified that **the week's five days belong to the team, not to each player**. My B2/B3
> analysis assumed per-character person-days and was wrong: the budget is **35 days**, not 140,
> and the original v0.1 Work Costs (26 total) were roughly right all along. My "×2.4 raise" to
> 66 was an artefact of the misreading. Everything has been re-derived below at team scale;
> where an older paragraph still says "person-days," read "days" and divide by four.
>
> Knock-on closures: **S1, S2, S5, M1, M2, M4, M6.** **S3 (Base and Legs) and S4 (the
> alpha-player problem) are the open items** - neither blocks a playtest.

---

## 0. v0.3 - the team-day recalibration

**The clarification.** A week is **five Activity cards for the whole team**, each played by a
named character. Not five per player. Feature Work Costs count **team days**, not person-days.

**Why this is the better model**, beyond being what was meant:
- **The game is player-count independent.** 3 players or 6, it's the same length, the same
  budget, the same difficulty. That removes an entire class of balance problem I'd have had to
  solve separately for each count.
- **"35 working days" becomes literally true.** The fiction and the budget are the same number.
  The thing I flagged as an arithmetic error in §3.2 was never an error - it was a different,
  and better, model.
- **Scaling is expressed the right way.** More players = **more options, not more actions**
  (wider Skill/Knowledge coverage to pick from) and **more people to keep motivated** (the
  grind hits everyone; a Rest still costs one of five days). Bigger teams are more capable and
  harder to sustain. That's self-balancing, and it's true to life.

**The second clarification: phase 4 was wrong.** Plan and Demo are cards you play *during* the
week, so a separate "resolve" phase listing activities made no sense. Cards now resolve
**Monday → Friday in the order they were laid**, which deletes the fixed resolution order
entirely and turns sequencing into a player decision - put Align on Monday if you want the
requirements cleared before Wednesday's Plan. Strictly fewer rules, strictly more decisions.

### Re-derived economy

| Step | v0.3 |
|---|---|
| Budget | **35 days** (7 weeks × 5) |
| − destroyed by Events (14 events, ~0.4 days each) | −6 |
| = **usable** | **29** |
| × 55% | **16 days on Work** |
| × bounded output ~1.4 | ≈ **22 Work delivered** |
| − Event rework | −4 |
| **= base Work total** | **18** |

**Features:** A 3, B 4, C 4, D 3, E 2, F 2 = **18**. Gated (D + F) = 5 = **28%**, which keeps
B5's endgame lesson intact.

**Absorption cap → 2 per feature per week.** At this scale a cap of 3 wouldn't bind at all;
with five days in the week, a cap of 2 guarantees **at least three days go elsewhere**. The
endgame release is deleted - unnecessary now, so that's one rule fewer.

**Recovery is Celebrate, not Rest.** Nobody rests *at* work. Teams sustain themselves across a
hard project by shipping something and marking it \u2014 so the ninth Activity is **Celebrate**:
+2 Motivation to everyone, **+3 if a feature was banked that week**. The base is unconditional
so a struggling team always has a lifeline and can't spiral; the bonus builds the rhythm the
game is about (*deliver, then mark it*) and makes the Feature Tower emotionally load-bearing
rather than decorative. Same budget as the old Rest card (~4 across the game, 11%), so no
recalibration.

**And Motivation resolves as one net number.** Running the grind as a separate step before Team
Need meant a character on 1 Motivation whose need had been met would quit on a sequencing
technicality \u2014 while \u00a75 simultaneously claimed the +1 was "exactly enough to cancel the grind."
Now: total \u22121 grind and +1 Team Need, apply, *then* check for zero.

**Overtime is a debt, not a bonus.** A sixth card costs 1 Motivation *and* a **Flex marker** \u2014
a day the project owes back, repaid by placing that marker into a weekday slot, which then
produces nothing. So overtime is **capacity-neutral** (6 + 4 = 5 + 5) and the 35-day budget
needs no recalibration; what it buys is *timing*, which on the dependency-gated critical path
can be worth more than the day.

The exception is the interesting one: **in week 7 there is no later to flex into**, so
deadline crunch genuinely does buy days - and the bill arrives as **−5 Team Score per unrepaid
marker**. That's design goal 10 ("working sustainably is different from working like a hero")
reduced to one decision, made at the moment real teams make it. **The dial to watch:** −5 must
be *just* worse than the ~4 points a day is worth. If teams crunch week 7 and never regret it,
raise it.

### Budget check

| | Days |
|---|---|
| Work (18 base + 4 rework, at ~1.4) | 16 |
| Celebrate (~4 across 7 weeks) | 4 |
| Destroyed by Events | 6 |
| **Left for Learn / Coordinate / Align / Plan / Demo / Reflect / Meet** | **9** |

Nine days to build four tracks and move Knowledge across a whole project. That is genuinely
scarce, and it's where the game now lives.

### Against the skill curve

| Play | Need | vs. 29 usable | Chance |
|---|---|---|---|
| **Random** | - | Collapses first: no Rest means the team loses a character in **week 3** | **~5%** ✅ |
| **Competent** (output ~1.2, some waste) | 18+4 ÷ 1.2 ≈ 18 days + 4 Rest = 22 | 22 vs 29 | **~50%** ✅ |
| **Perfect** (output ~1.6, right sequencing) | 22 ÷ 1.6 ≈ 14 + 4 Rest = 18 | 18 vs 29 | **~95%** ✅ |

Same curve as before, at a quarter of the numbers. **Still to verify at a table:** the real
output rate, and whether the cap of 2 ever actually binds.

---

## 1. What's working (don't break these)

| Strength | Why it matters |
|---|---|
| **The opening habitus build (§3.1)** | Best thing in the design. Players do something concrete and irreversible before a rule is read - textbook participate-first onboarding. Keep this even in the lightest cut. |
| **Strength/tendency design rule** | "Never write a habitus effect as +1 to X" is a real discipline that will keep the game from turning into a stat-bonus salad. Hold the line on it. |
| **Dependencies + the Unclear → Align → Plan ordering (§10)** | A genuine puzzle with a real trap: skipping to Plan on an Unclear feature is a wasted day that *looks* productive. That's the design goal working. |
| **Habits as permanent unlocks (§18)** | Correctly avoids the "your bonus evaporates when the track drops" trap. Rewards *reaching*, not *hovering* - and the double-sided coin carries the whole rule physically: position is what you have, face is what you've become. |
| **Hidden Event day ↔ Adaptability (§11)** | Clean coupling: an abstract track buys a concrete, felt benefit. More couplings should look like this one. |
| **Documentation discipline** | Cross-referenced, versioned, honest about what's untuned. Unusually good for a v0.1. |

---

## 2. Blocking defects - the game cannot be played until these are fixed

### B1. ~~Seven of nine Activities have no number~~ - **RESOLVED**

§7 is rewritten as an exact table: every Activity now states a cost in person-days and a
numeric effect, with no "may," "can," or "improves" anywhere. Two blanket limits added (Work
never below 0; each track rises at most 1 per day), and the Skill bonus now points at a
determinate target ("the first listed numeric effect") instead of the vague "main numeric
effect."

The one genuinely new design decision made while closing this: **Plan scales with
Complexity** - High −2, Medium −1, **Low −0**. Plan is deliberately *worse than Work* on easy
features and twice as good on hard ones. That gives Complexity a job beyond scaling rework,
and it turns Plan from a vague efficiency buff into a real read-the-problem decision. Watch it
in playtest: if teams never Plan, the High −2 is too weak.

Other effects settled the same way - Coordinate → Trust (+Shared Practice when two people do
it together), Align → clears Unclear or +1 Adaptability, Learn → Knowledge becomes **Shared**
at 3 holders for +1 Capability and +1 Shared Practice, Reflect → +1 Adaptability (+1 Shared
Practice only if there's experience to reflect on), Demo → a real gamble on hidden Quality.

### B2. ~~The currency is ambiguous~~ - **RESOLVED**

**Decision (locked): the currencies are person-days and Motivation.** Weeks are the accounting
period, not a third currency.

- **Person-days** - one per character per day. Never saved, never carried over, never given
  away; unspent is wasted. An Activity involving N characters costs **N person-days** (a Learn
  costs 2 - the teacher's day *and* the learner's).
- **Budget: 4 × 35 = 140 person-days.** *35 days* is the calendar; *140 person-days* is the
  budget. Work Costs get compared against 140, never 35.
- **Motivation** - personal, bankable to 5, and genuinely **spendable**. It is the only way to
  buy more output than the calendar holds (HERO MOMENT, the Item one-shot). Person-days are
  shared and expire nightly; Motivation is individual and can be hoarded or burned.

That asymmetry does real thematic work: the team can always buy speed, but only out of the
people. Every Motivation spend is the Hero-Team path (§14) being offered to one player, one
token at a time.

**Applied to:** rulebook §6.0 (the rule), §3.2, §5, §6.1, §7, §9, §11, §12, and Lite §5/§6.
A blanket clause in §6.0 now covers every Event card that says *"the team spends a
Coordinate/Align/Plan/Reflect day"* - one character, one person-day - so those cards didn't
each need rewriting.

> **Knock-on:** Onboarding (§12) was "2 combined days," which under the settled rule is a
> single Learn. Raised to **4 person-days** so the onboarding dilemma still has teeth.

> **Open, for Stage 3:** if Motivation is a currency, it needs more than one thing to buy.
> Today there are two purchases in the whole game (HERO MOMENT, the Lite Item one-shot), both
> "buy a person-day." Watch the playtest count of tokens *spent* vs. *lost* - if it's near
> zero, Motivation is still a health bar wearing a currency's clothes.

### B3. ~~The work budget is not close to balanced~~ - **RESOLVED**
§3.2 originally reasoned *"26 work required, against 35 available days"* - comparing work to
the **calendar** rather than the **budget**. Against the real 140 person-days, the project
consumed **under 20%**: no deadline pressure, and therefore no Hero-vs-Sustainable choice
(§14), because a team could trivially do both.

Even generously assuming rework, events, and dependency stalls double the cost, the team has
roughly a hundred spare person-days. There is no deadline pressure, and therefore no Hero-vs-
Sustainable choice (§14), because you can trivially do both.

**Severity: was blocking.** Fixed by bounding output first and deriving the costs from the
bound - see below.

#### How to fix it - the arithmetic

Work the ratio, not the feel. Target: **required Work + expected rework should consume 55-65%
of the *usable* budget.** Below 50% there's no pressure; above 75% the non-Work activities
become unaffordable, which deletes the point of the game.

#### First, the diagnosis has changed - B3 is a multiplier problem, not a Work Cost problem

The obvious fix is "raise the Work Costs." That fix is wrong, and v0.2 makes it clearly wrong.

**Output per person-day is unbounded.** One Work person-day produces: base 1, **+1** if
Capability ≥ 4, **+1** on a Skill match, **+1** on a Knowledge/Domain match. A Technical
character with matching Knowledge on a Capability-4 team produces **4 Work from one day** - four times the character sitting next to them.

So "140 person-days against 26 Work" doesn't describe anything. Two teams spending the same
140 person-days deliver wildly different amounts, and the gap widens every week:

| Path | Avg output per Work day | Person-days to deliver 63 Work |
|---|---|---|
| **No investment** (Hero) | ~1.0 | **63** |
| **Full investment** (Sustainable) | ~2.0 by week 3 | **~35**, plus ~15 invested = **50** |

Raising Work Costs to squeeze the second team makes the first team's game *impossible* - and
the first team is the one already suffering. **You cannot set a Work Cost until output per
person-day is bounded.** Fix that first.

#### Fix A - the Feature Absorption Cap *(the one I'd actually do)*

> **A feature can absorb at most 3 Work person-days per week.** Person-days allocated beyond
> that are wasted.

This is **Brooks's Law** - adding people to a late project makes it later - and it's the most
thematically exact rule the game could possibly have. It fixes B3 from the *demand* side
instead of by inflating any number:

- Week 1 has four features available (A, B, C, E - D and F are dependency-gated). Absorption
  ceiling is **4 × 3 = 12** person-days, against **20** available.
- **Eight person-days per week physically cannot go into Work.** Non-Work activities stop
  being a virtuous choice and become structurally mandatory.
- It punishes panic-dumping specifically, not normal play - at a normal pace (~8 Work
  person-days/week) the cap never binds. It bites exactly when the team is behind and wants to
  throw bodies at the problem, which is when it *should* bite.
- It makes the dependency chain matter: you can't rush D by piling on, you have to bank B first.

This single rule does more for B3 than any Work Cost change, and it costs one line.

#### Fix B - make the bonuses per-week, not per-person-day

> **Capability ≥ 4 and a Skill match each give +1 Work per character per week**, not per
> person-day.

A character putting 4 days into Work gets 5 Work, not 8. Average output settles around
**1.2-1.4** instead of 1.0-4.0, so the person-day budget finally means something. Investment
still pays about **25-30%** across the project - worth it, but no longer a different economy.

This replaces the earlier "make Capability decay" idea. Decay is a maintenance tax that adds
bookkeeping every week; a per-week cap just stops the runaway at the source.

#### Fix C - *now* set the Work Costs

With A and B in place, the arithmetic finally holds still:

| Step | v0.2 (4 players × 7 weekly turns) |
|---|---|
| Raw budget | **140** person-days |
| − destroyed by Events (14 events × ~2) | −28 |
| = **usable budget** | **112** |
| × 60% target | **67** person-days on Work |
| × avg output ~1.2 | ≈ **80** Work delivered |
| − expected rework/scope from 14 Events | −14 |
| **= base Work total should be** | **≈ 66** |

| Feature | Work Cost | was | Complexity | Depends on |
|---|---|---|---|---|
| A | **7** | 3 | Low | - |
| B | **11** | 4 | Medium | - |
| C | **13** | 5 | Medium | - |
| D | **16** | 6 | High | B |
| E | **7** | 3 | Low | - |
| F | **12** | 5 | High | C |
| | **66** | 26 | | |

**Sanity checks:** 55 Work person-days + 12 for rework = 67 of 112 usable (**60%** ✓). The
remaining 45 cover 7 weekly grinds' worth of Rest (~18 person-days) plus ~27 for everything
else - tight, and every one of them a real decision. Average Work demand is ~8 person-days per
week against Fix A's ceiling of 12, so the cap binds only when panicking ✓.

#### Fix D - make it visible
**Withdrawn.** This originally added a pace line (**S5**): the Work total you should have banked
by the end of each week. It was cut from the design - it turned a cooperative game into a
progress audit, and the deadline plus the shrinking week ladder already carry the pressure.
S5 is therefore **open again**: the team can still only feel it is losing, not see it.

---

> **✅ Applied - bounds first, costs derived from them.**
>
> **The bound (§7):** *a character can never produce more than (their Work person-days that
> week) + 2 Work.* Resolve normally, then check the cap. This is what pins output to ~1.0-1.4
> per person-day instead of 1.0-4.0. Chosen over per-week bonuses because it's a single
> ceiling checked once, rather than a rewrite of every bonus in the game.
>
> **The absorption cap (§10):** *a feature absorbs at most 3 Work person-days per week.*
>
> **Derived costs (§3.2):** total **66** (A 7, B 11, C 13, D 16, E 7, F 12).

#### Why 66 is the conservative number
Not "66 is right" - **66 is the number that survives the model being wrong.** The output rate
is the one figure nobody can know before a playtest, so the costs were chosen to stay sane
across the whole plausible range of it:

| If real output turns out to be | Work consumes | Verdict |
|---|---|---|
| 1.1 / person-day | 65% of usable budget | Top of band - tight but playable |
| **1.3 (modelled)** | **55%** | Bottom of band, as intended |
| 1.5 / person-day | 47% | Loose - too easy, but not broken |

A number tuned to be exactly right at 1.3 would break at 1.1. This one doesn't.

#### The two paths now land where §14 says they should
This is the check that actually matters - B3 existed because both paths were trivially
achievable at once:

| Path | Output rate | Person-days on Work | % of 112 usable | Result |
|---|---|---|---|---|
| **Hero** (no investment) | 1.0 | 80 | **71%** | Survivable and miserable. ~18 must still go to Rest against 7 grinds, leaving 14 for everything else. Expect burnout and quits. |
| **Sustainable** (~15 invested) | 1.4 | 57 + 15 = 72 | **64%** | 40 person-days left for Rest and the rest. Comfortable, not free. |

A 7-point gap: investment clearly pays, and neglecting it clearly hurts, but neither path is
automatic. That's §14 finally being a real decision instead of a description.

#### Checked while deriving: Plan isn't degenerate
Plan reduces High −2 / Medium −1 / Low −0, floored at half the printed cost. At output 1.3,
planning both High features (D 16→8, F 12→6) costs 7 Plan person-days to save ~10.8 - a net
gain of about **3.8 person-days across the whole project, ~3%**. Worth doing, not worth
building a strategy around. On Medium it's a net loss and on Low it does nothing, exactly as
§7 intends. **No extra rule needed** - which is the point of a conservative pass.

---

### B5. ~~The absorption cap starves the endgame~~ - **RESOLVED**

Found by scheduling the project rather than budgeting it. B3 checked whether the team has
enough *person-days*; it never checked whether those person-days can be **absorbed in the
weeks they're available**. They couldn't.

#### The critical path

Fix A caps each feature at 3 Work person-days per week. So the team's Work capacity in any
week is `(unbanked available features) × 3` - and the dependency structure collapses that
number exactly when the deadline gets close.

| Week | Features available | Work capacity (person-days) |
|---|---|---|
| 1 | A, B, C, E | 12 |
| 2 | A, B, C, E | 12 |
| 3 | B, C, E | 9 |
| 4 | C, **D** | 6 |
| 5 | D, F | 6 |
| 6 | D, F | 6 |
| 7 | D, F | 6 |
| | | **≈ 57 total** |

Required: **80 Work** (66 base + ~14 Event rework) ÷ ~1.4 output for a well-invested team =
**57 person-days**.

> **57 available against 57 needed \u2014 zero slack**, assuming perfect scheduling, no
> misallocation, and events that never touch the critical path. In Work terms it's ~82
> capacity against 80 required.

#### Why it fails
1. **42% of all Work is behind a dependency gate.** D (16) and F (12) total 28 Work, and
   neither can start until B and C are banked. They're forced into exactly the weeks when only
   two features exist to absorb effort.
2. **D and F individually just miss.** D can start week 4 at the earliest and needs 16 Work
   from 12 person-days; F starts week 5 and needs 12 from 9. Both require near-maximum output
   every remaining week with no Event interference.
3. **Weeks 5-7 have 14 idle person-days a week.** Only 6 of 20 can go to Work. The cap that
   correctly forces investment in the early game becomes forced idleness in the late game - and by then there's nothing left worth investing in.
4. **Any late rework is fatal.** A NEGATIVE FEEDBACK or TECH DEBT on D in week 6 cannot be
   recovered: there is no spare absorption anywhere.

#### Estimated chance of delivering all six features

| Table | Chance |
|---|---|
| Perfect play, average luck | **~30-40%** |
| Competent play, average luck | **~10-15%** |
| First-time players | **under 5%** |

For a cooperative game that's too harsh - and worse, it fails for a reason players can't see
or plan around. They'll lose to a scheduling constraint that only shows up in week 5.

#### The fix - **APPLIED**

Two changes, neither touching the 66 total or the derivation behind it.

**1 - Move Work off the gated features.** Gated Work drops from **28 to 19** (42% → 29%):

| Feature | Work Cost | was | Complexity | Depends on |
|---|---|---|---|---|
| A | **10** | 7 | Low | - |
| B | **13** | 11 | Medium | - |
| C | **14** | 13 | Medium | - |
| D | **10** | 16 | High | B |
| E | **10** | 7 | Low | - |
| F | **9** | 12 | High | C |
| | **66** | 66 | | |

**2 - Release the absorption cap at the end.** *A feature absorbs at most 3 Work person-days
per week, rising to **5 once only two features remain unbanked**.*

Redistribution alone wasn't enough. The deeper problem is that **absorption shrinks as you
succeed** - every banked feature is one less place to put people, so a flat cap makes the
final stretch a bottleneck no matter how the Work is distributed. Recomputed with only the
redistribution, capacity was 60 person-days against 57 needed: still under 5% slack. The
endgame release is what actually fixes it, and it keeps the Brooks's Law squeeze in the middle
of the game where the decisions are interesting, rather than at the end where it's arithmetic.

#### Does it hit the target curve?

Checked against the skill-expression target now recorded in [concept.md](./concept.md) - random ~5%, competent ~50%, perfect ~95%.

Total capacity after the fix: **~78 Work person-days** (48 across weeks 1-4 at 4 features × 3,
plus 30 across weeks 5-7 at 2 features × 5).

| Play | Effective need | vs. 78 capacity | Chance |
|---|---|---|---|
| **Random** - no investment (output 1.0), heavy misallocation, no Rest | Collapses before the schedule matters: characters hit Motivation 0 in **week 3** and quit | - | **~5%** ✅ |
| **Competent** - output ~1.2, ~15% of allocations wasted | 80 ÷ 1.2 = 67, × 1.15 = **77** | 77 vs 78 | **~50%** ✅ |
| **Perfect** - output ~1.4, no waste, correct sequencing | 80 ÷ 1.4 = **57** | 57 vs 78 (37% slack) | **~95%** ✅ |

The curve works because **the two ends fail for different reasons**: random play dies to the
Motivation grind long before the deadline is the issue, while skilled play is bounded by the
schedule. Neither mechanism alone would produce a 90-point spread; together they do.

**The one number to verify first:** competent play sits at 77 against 78 - a one-person-day
margin. That's fine as a design intent (a coin-flip in the middle is exactly right) but it
means the ~1.2 competent output rate and the ~15% waste estimate are the two figures a
playtest most needs to confirm.

---

### B3b. ~~The 35-day calendar cannot coexist with a 90-minute playtime~~ - **RESOLVED**

This is the same defect seen from the other end, and it's the one that actually binds.

**Time model** (4 players, first play, with a teacher). Fixed overhead: habitus build 12 min +
rules teach 8 min + wrap-up/scoring 5 min = **25 min**. Per in-game day: ~5 min while learning
(days 1-3), ~3.5 min while the teacher tapers (days 4-8), ~2.5 min once the table runs itself.

| Calendar | Play time | + overhead | Verdict |
|---|---|---|---|
| 10 days | 37.5 min | **62 min** | Fits, but too short to feel the arc |
| **15 days** | 50 min | **75 min** | ✅ **Fits 90 with real buffer** |
| 20 days | 62.5 min | 87.5 min | Ceiling. No buffer, no debrief |
| **35 days** | 100 min | **125 min** | ❌ And that assumes zero friction |

Even for a table that already knows the game and plays flat-out at 2 min/day, 35 days is
70 min of play + 25 overhead = 95 min. **The full game only ever approaches 90 minutes for
experienced players who don't argue.** A first playthrough at 35 days is 2.5-3 hours.

#### Three ways out, ranked - **DECIDED: option 1**

**1. Make the week the turn, not the day** - ✅ **adopted.** Each character allocates **5
person-days per weekly turn**, committing *before* that week's Events are drawn. Turn count
drops 35 → 7; the budget stays exactly 140 person-days; **the locked fiction of "7 weeks / 35
working days" survives untouched.** Modelled at 7 turns × ~8.5 min + 25 min overhead ≈
**85 min**. Applied in rulebook §6.1 and [concept.md](./concept.md).

The commit-then-disrupt ordering turned out to be worth more than the time saving:
- **Adaptability finally has a job** - it's the number of person-days you may re-point after
  Events land (§4). That's an always-on numeric effect, which is most of **S2** fixed as a
  side effect. All four tracks now have live effects; Shared Practice makes Learn cost 1
  person-day instead of 2.
- **The hidden-Event-day token is gone.** Drawing Events *after* commitment achieves the same
  "you can't plan around it" goal with fewer components and more tension.
- **Wasted days become visible.** An Event that invalidates what a day was pointed at destroys
  a decision you already made - which is the actual feeling the game is chasing.
- **M1 and M2 close too.** Team Need moves to a weekly check (one pass at a natural stopping
  point), and the Pulse track - which explicitly did nothing - is replaced by the weekly
  allocation board.

**Watch in playtest:** turn 1 allocation is the risk. Twenty person-days across nine
Activities with four people discussing is the heaviest single decision in the game. If turn 1
runs past ~12 minutes, cut to 5 or 6 weeks rather than trimming the allocation.

**2. Shorten the calendar** to 3-4 weeks (15-20 days). Keeps daily decisions; changes the
fiction. This is what Lite still does - Lite stays daily on purpose, so the first playtest
tests the *activity economy* without also testing a novel turn structure.

**3. Accept a longer game** and move the playtime target to ~2.5 hours. Rejected.

### B4. ~~Capital deadlocks on turn one~~ - **RESOLVED** (Fixes 1 and 2 applied; Fix 3 held)

Everyone starts at Capital 2. The named ways to *gain* Capital are:
- a Demo going well - but **Demo requires Capital ≥ 3**;
- a Take Charge call landing - but that **requires Capital ≥ 3** to land;
- calling out Knowledge Hoarding - requires that specific Event *and* Trust ≥ 4.

So at setup nobody can Demo, nobody's Take Charge works, and there is **no defined route from
2 to 3**. An entire subsystem - and with it the Bourdieu thesis the game is built on - is
locked shut for the whole game.

**Severity: blocking.**

#### The deadlock is a theory error, not an arithmetic one

v0.1 models Capital as **self-generating**: standing is the only thing that produces standing.
Bourdieu says close to the opposite, and the game gets stuck precisely because it dropped the
part of the theory that makes capital *move*.

Three pieces of the theory are missing, and each supplies one fix.

---

**1. Capital is convertible between forms.** *(Bourdieu, "The Forms of Capital", 1986.)*
Bourdieu's central claim is that capital exists in several forms - **economic**, **cultural**
(education, credentials, embodied know-how), and **social** (networks, relationships,
obligations) - and that these are **convertible into one another**. **Symbolic capital** - prestige, standing, the right to be listened to - is what any of the other forms becomes when
the field *recognises* it as legitimate.

The game's Capital is symbolic capital. But the game never lets anything convert *into* it, so
it can't be created. Meanwhile the characters are already holding the other forms and the
rules don't notice:

| Bourdieu's form | Already in the game as | Currently converts to Capital? |
|---|---|---|
| Cultural capital | **Knowledge** and **Skills** - literally Base (upbringing) and Legs (education) | No |
| Social capital | **Trust**, and the team relationships built by Coordinate | No |
| Symbolic capital | **Capital** (§5.1) | - |

> **Fix 1 - open the conversions.** Two new Capital sources, both available at Capital 0:
> - **Teach (Learn, as the teacher): +1 Capital.** Cultural → symbolic. You convert private
>   know-how into public standing by giving it away.
> - **A feature you contributed Work to is banked: +1 Capital** to each contributing character.
>   Labour → symbolic, and it's *witnessed* - see Fix 1b.
>
> Cap Capital gain at **1 per character per week** so it can't spiral.

This also quietly fixes the KNOWLEDGE HOARDING event, which currently has no teeth. Once
teaching pays standing, hoarding becomes a genuine dilemma straight out of the theory:
monopolising cultural capital preserves your scarcity and your indispensability, but forfeits
its conversion into symbolic capital. The hoarder stays *needed* and never becomes
*respected*.

**1b. Recognition is what makes it symbolic.** Bourdieu insists symbolic capital only exists
through **recognition** by the field (and its *méconnaissance* - the field's habit of
mistaking earned advantage for natural authority). So the gain must be public: Capital is
awarded only for things that happen **in front of the team** - teaching someone, a banked
feature, a call that visibly landed. Private competence earns nothing. That's not a
restriction bolted on, it's the definition.

---

**2. Capital is a position in a distribution, not a substance.** Bourdieu treats capital as
**relational** - its value is set by how much of it you hold *relative to other agents in the
same field*. An absolute threshold of "3" is un-Bourdieusian on its face, and it's exactly
what creates the deadlock.

> **Fix 2 - make the gate relative.** **Demo requires Capital ≥ the team's average Capital.**
>
> At setup everyone sits at 2, which *is* the average - so everyone qualifies and the deadlock
> evaporates without a single special case. But the moment one character pulls ahead, they
> raise the average and start locking the others out.

That's the "Hero-team / face of the team" concentration §5.1 says it wants - and here it
*emerges from the theory* instead of being a warning paragraph. It also makes a low-Capital
character's Demo a live cooperative decision every single time, rather than a fixed
early-game lockout.

---

**3. Newcomers gain legitimacy through consecration.** In Bourdieu's studies of cultural
fields (*The Rules of Art*; *Homo Academicus*), agents who lack standing acquire it by being
**consecrated** - sponsored, vouched for, co-signed by someone the field already recognises.
The incumbent lends their legitimacy, and takes on some of the risk of doing so.

> **Fix 3 - sponsorship.** A character with **Capital ≥ 4** may sponsor a lower-Capital
> character's Demo, spending their own person-day to do it. The presenter runs the Demo
> regardless of the threshold in Fix 2.
> - Demo succeeds → presenter **+2 Capital** (instead of +1). The sponsor gains nothing.
> - Demo fails → presenter −1 as normal, and the **sponsor −1 Capital** too. Vouching for
>   someone costs you when it goes wrong.

This is the deliberate counter-move to Fix 2's concentration: the team can spend its
established member's standing to build someone else's. It's the mechanical form of the thing
§5.1 already asks for - *"deliberately letting a lower-Capital character Demo is riskier, but
it spreads standing to where the team needs it"* - except now it costs the right person
something.

---

#### What this does to the design

| Before | After |
|---|---|
| Capital is self-generating, so it can't start | Capital is **converted** from Knowledge, teaching, and delivered work |
| Absolute threshold of 3, deadlocked at 2 | **Relative** threshold - no deadlock possible, by construction |
| Concentration warned about in prose | Concentration **emerges**, and sponsorship is the counter-play |
| Knowledge Hoarding is a flavourless event | Hoarding is a real strategic trade-off: needed vs. respected |
| Base and Legs are inert (**S3**) | They supply the cultural capital that converts into standing |

Note the last row: this proposal partly closes **S3** as a side effect. Base (upbringing) and
Legs (education) are, in Bourdieu's terms, *precisely* where a person's inherited cultural
capital comes from - so wiring them to Capital isn't a patch, it's the theory finally being
implemented.

#### Open questions to settle before applying
1. **Does "average" round?** Recommend comparing against the raw average and using **≥**, so
   everyone at equal standing qualifies. Confirm at the table that it isn't fiddly to compute
   with 4-6 characters.
2. **Is +1 Capital per banked feature too generous** when a feature can have 4 contributors?
   Possibly restrict to the character who added the *final* Work - but that rewards
   vulture-play. Test the generous version first.
3. **Does the weekly cap of +1 make Capital too slow** across a 7-week game? Max reachable is
   then 2 + 7 = 9, well over the 0-5 scale, so the cap is probably safe - but it means Capital
   5 is achievable by week 3, which turns on the **Authorized Voice** habit (§18) early.
4. **Sponsorship at Capital ≥ 4 may be unreachable** if Fix 2 makes the average climb fast.
   Consider "≥ 4, *or* the highest Capital at the table."

**Recommendation:** apply Fixes 1 and 2 together - they're each one line and they're what
actually unblocks the subsystem. Hold Fix 3 (sponsorship) until a playtest shows Capital
genuinely concentrating; if it doesn't concentrate, sponsorship is solving a problem the game
doesn't have.

> ✅ **Applied.** §5.1 is rewritten: four conversion routes into Capital (teaching, delivering,
> a successful Demo, a habitus strength that visibly worked), capped at +1 per character per
> week, all requiring the team to witness it. The Demo gate and the Take Charge pattern both
> now read **≥ the team average**. Sponsorship is written into §5.1 as an explicitly inactive
> module. The forms-of-capital theory went into
> [habitus-model.md](./habitus-model.md), which had no account of it at all.

---

## 3. Serious design problems - playable once B1 - B4 are fixed, but the game won't deliver its promise

### S1. Nothing degrades the team, so the team-under-pressure premise never fires
Motivation only moves on Events and Team Need. Team Need pays **+1 per day** with a cap of 5,
against **7 Events across 35 days**. Net drift is strongly positive: most characters sit
pinned at 5 Motivation all game.

Consequences: Rest is never worth a day; Burnout Warning can't trigger; quitting at 0 (§13)
essentially cannot happen; and §14's Hero Team path has no downside, so it isn't a path, it's
just the correct play.

**Fix:** add a standing drain - an automatic Motivation cost per week (or per Work-heavy day)
that Rest and Team Need have to actively counteract. Pressure must be *systemic*, not
event-driven. This is the single highest-value change in the whole assessment.

### S2. ~~Only one of four Team State tracks does anything~~ - **RESOLVED**
v0.1 was explicit: *"Capability is the one track with a direct number effect."* The optimal
play was therefore *"max Capability, ignore the rest"* - the exact opposite of §4's *"the best
teams keep a healthy balance."*

The week-turn change (B3b) supplied the missing effect. §4 now gives all four a live,
always-on job:

| Track | Live effect |
|---|---|
| **Trust** | ≤ 1: **Learn does nothing.** ≥ 4: cancel one Event effect per week. |
| **Capability** | ≥ 4: Work +1. ≤ 1: Work −1. |
| **Shared Practice** | ≥ 4: **Learn costs 1 person-day instead of 2.** ≤ 1: multi-character Activities cost one extra. |
| **Adaptability** | **The re-planning budget** - person-days you may re-point after Events land on your committed week. |

Adaptability's version is the important one: it's a number the team uses every single turn.
And it makes §4's stated interaction real - **high Shared Practice with low Adaptability is
now mechanically a team that is excellent at familiar work and cannot change course.**

**Still to test:** whether Shared Practice's Learn discount and Trust's Learn lockout stack
into a runaway (cheap teaching → Capability → more Work → more of everything).

### S3. Two of the five habitus parts are mechanically inert
**Base (upbringing)** and **Legs (education)** have zero rules effect anywhere in the
rulebook. They are the first two parts the player picks, in the ritual the whole design is
anchored on. Torso and Head have exactly **two** worked examples between them.

Players will notice by week two that 40% of the figure they lovingly built is decoration - and the Bourdieu argument ("upbringing shapes what feels natural") collapses to a costume.

**Fix:** every part must pay for its place on the figure. Base → starting Knowledge. Legs →
the Skill that grants the activity bonus. That's two lines of rules and it saves the thesis.

### S4. Fully open information + collective decisions = the alpha player problem
This is a co-op with no hidden hands, no communication limits, and ~140 collective decisions.
One confident player will drive the table. The game about building a high-performing team will
reliably reproduce the single worst team dynamic - and it has no mechanism to stop it.

Team Need and Habitus are the natural hooks (they're per-character agendas), but neither
currently *constrains* anyone; both are group-resolved. **Fix:** make at least one habitus
effect a thing only that player may declare, and consider a soft rule that each player chooses
their own character's action.

### S5. Scores don't discriminate, and you only find out on Day 35
Team Score's threshold is 70 of ~100. Given B3's slack, a competent table maxes features (60),
maxes tracks (20), and holds Motivation near cap (~20) - scoring ~95-100 almost every game.
"Sustainable High Performance" becomes the default outcome rather than an achievement.

Separately: there is no mid-game feedback. A co-op needs a visible losing clock - you should
be able to *see* you're falling behind in week 3, not learn it on day 35. A printed pace line
was tried and **cut** - it read as a progress audit and flattened the mood of every week it
touched. **Still open.** Whatever replaces it has to come from something the team already
handles: unbanked bays visible against a shrinking week ladder, most likely.

### S6. ~~Rules mass vs. the 60-90 minute target~~ - **ADDRESSED by staged setup**

A POC sanity test confirmed the diagnosis from the other end: the game reads as good - *for
experienced board-game players*. Setup and initialisation are too heavy for everyone else.
That's the Bourdieu problem the playtesting skill warns about, arriving exactly on schedule:
the design was being validated by people who already hold the cultural capital.

**Two fixes, both in §3.0-3.1:**

**1. Habitus is dealt, not chosen.** Five random parts, one per row, and you still physically
assemble the figure. This removes five decisions per player from a table that doesn't yet know
what the words mean - the single largest setup cost - while keeping the tactile ritual that
makes §3.1 worth having.

> **And it is theoretically better.** Choosing your habitus was always slightly against the
> grain of the theory: nobody selects their upbringing, their schooling, or what they do by
> instinct under pressure. Being *handed* a person and having to play them is Bourdieu's actual
> claim. Drafting returns as an explicit variant for players who know the game.

**2. The board uncovers itself.** A cover panel sits over the Ledger and comes off at the
start of week 2, together with Reality/Shit Happens/Adapt - both at once. **Week 1 is only "plan a week"** - lay five cards, resolve left to right, close it. Three card types.

| From | Opens - **one idea a week** | Cards added |
|---|---|---|
| Week 1 | **The week.** Week strip, Project bays, your figure, Knowledge, Motivation | Work · Coordinate · Celebrate |
| Week 2 | **The team, and reality.** The whole Ledger, plus Habits - and Shit Happens and Adapt, together. Adapt equals [Adaptability] immediately | - |
| Week 3 | **Board 4b, then the person.** HOW YOU COVER/THE LEDGER READS THIS lift, and the Specimen card - Capital, Team Need, Overtime/Flex. Quality | Learn · Align · Reflect · Meet · Plan · Demo |
| Week 4 | **Standing.** The Ledger's fifth track - whoever holds the most Capital | - |

Each week's lesson is one sentence: *a week is five days and you choose them · it was never
only the project - it was landing on the team, and your plan was made in ignorance, both at
once · and it was never only the team - it was landing on you.*

**Weeks 2, 3 and 4 are staged as reveals.** For a week the table watches only the features
move. To make the consequence *shown* rather than announced, the discard pile stays face up and
each panel runs a one-line catch-up on reveal: **week 2, Trust +1 per two Coordinates played;
week 3, each character takes 1 Capital per two cards they played, max 2; week 4, no catch-up -
just compare who holds the most Capital.** No hidden bookkeeping - but it's the difference
between being told these things matter and seeing that they were counting all along.

Everything sat at its starting value whether visible or not. Week 2 doesn't *start* Trust, it
starts you paying attention to it. Nothing is lost, and the table meets each rule at the moment it matters
instead of in a twenty-minute briefing.

This is legitimate peripheral participation applied to the rulebook rather than to a character:
a newcomer makes a real decision inside five minutes, and the scaffolding tapers on a schedule
instead of all at once.

**Still to verify:** whether week 1 is *too* thin - three card types and no Events may feel
inert rather than gentle. If it does, move Events to week 1 and push everything else back one.

---

## 4. Smaller issues, worth noting

| # | Issue |
|---|---|
| ~~M1~~ | ✅ **Closed by the week-turn.** Team Need is now checked once per week, at the week's close - one pass over four characters at a natural stopping point. |
| ~~M2~~ | ✅ **Closed by the week-turn.** The Pulse track (which explicitly did nothing) is gone, replaced by the weekly allocation board where the committed plan physically lives. |
| M3 | **The Feature Tower is decorative.** Blocks stack, but nothing about the tower's *shape* or *stability* matters. If it's going to be the game's visual centrepiece, its physicality should carry a rule. |
| M4 | ✅ **Addressed by art direction and naming.** The "Field Study" framing in [design-guide.md](./design-guide.md) recasts Trust/Capability/Shared Practice as a *researcher's* terminology rather than an HR deck. Achievements are now **Habits** - plain language, and in a game built on *habitus* the strongest available word for a durable acquired disposition. Confirm at playtest that it lands. |
| M5 | **KEY SPECIALIST LEAVES is player elimination** in a 4-player game (§11). Removing someone's character mid-game with nothing to do is a hard no for playtesting. Make it a temporary absence. |
| ~~M6~~ | ✅ **Closed.** Events went from 7 to **14** (2 per week), and each one now lands on a committed plan rather than on an open decision - so they bite far harder per card. |
| M7 | ~~**Onboarding (§12) can't be reached** - it depends on NEW TEAM MEMBER being drawn from a 30-card deck.~~ ✅ **Closed in v0.20.** NEW TEAM MEMBER is retired; Onboarding now triggers automatically whenever a character quits or is fired (§13's Replacement rule), so it can no longer go a whole game unseen. |

---

## 5. Verdict

| Dimension | Rating | Note |
|---|---|---|
| **Concept originality** | Strong | The premise and the build ritual are the real assets. |
| **Rules completeness** | Resolvable | B1 and B2 closed. §7 has exact numbers; the currency is settled. |
| **Economy / balance** | Derived, untested | Budget *and* schedule both check out: output bounded at days+2, absorption 3/week (5 at the endgame), Work totals 66 with only 29% behind gates. |
| **Difficulty** | On target | Models to ~5% random / ~50% competent / ~95% perfect - the curve stated in [concept.md](./concept.md). |
| **Meaningful choice** | Structural | The absorption cap makes 8 person-days a week *unable* to go into Work. Non-Work activities are now mandatory, not virtuous. |
| **Pressure / tension** | Designed in | Weekly grind + committing the week before Events land. |
| **Theme delivery** | Good | B4 fixed - Capital converts and the gate is relative. **S3 (inert Base/Legs) is the last theme gap.** |
| **Onboarding** | Excellent, then a shorter cliff | §3.1 is great; the wall after it is lower now that the turn structure is 7 steps, not 35. |
| **Playtime realism** | On target | ~85 min modelled at 7 weekly turns (**B3b**). |

**Recommendation: do not playtest v0.1 as written.** Play the cut-down
[rulebook-lite.md](../rules/rulebook-lite.md) instead - it exists to answer three questions
cheaply, and everything it removes is listed there as deliberately deferred, not deleted.

---

## 6. Step-by-step improvement plan

Ordered so each stage is testable on its own and nothing later depends on a guess made
earlier. **Do not skip ahead** - stages 4+ are tuning, and tuning a broken economy wastes
sessions.

### Stage 0 - Decide the currency ✅ **DONE**
Fixed **B2**. The currencies are **person-days** (one per character per day; an N-character
Activity costs N) and **Motivation** (personal, spendable). Budget is **140 person-days**, not
35 days. Written into rulebook §6.0 with a blanket clause covering the Event cards, and into
Lite §5. Onboarding raised to 4 person-days as a knock-on.

**Still open from this stage:** Motivation has only two things to buy. Carried into Stage 3.

---

### Stage 1 - Give every Activity a number ✅ **DONE**
Fixed **B1**. §7 is now an exact table - cost in person-days, numeric effect, no hedging
verbs. Plan scales with Complexity (High −2 / Medium −1 / Low −0), which was the only real
design call needed to close it.

**Not yet balanced, and deliberately so** - these numbers exist to be *resolvable*, not
correct. Balancing is Stage 4, after a playtest.

---

### Stage 2 - Cut to the light version and run the first playtest
Fixes **S6**, sidesteps **B4**, partially fixes **B3** and **S1**.
1. Play [rulebook-lite.md](../rules/rulebook-lite.md) - 15 days, 5 Activities, 2 tracks, no
   Capital, no Quality, no Demo/Plan/Reflect/Meet, paper habitus parts, nothing 3D-printed.
2. It answers three questions and only three (see Lite §1).
3. Log it against the template in [../playtests/README.md](../playtests/README.md), recording
   **quotes**, not just outcomes.

**Done when:** you have one logged session and an answer to Lite's Q1/Q2/Q3.

> **Gate:** if Lite's Q2 comes back *"Work was always obviously right"*, stop and fix the
> action economy before touching anything below. That answer invalidates the whole design.

---

### Stage 3 - Make pressure systemic ✅ **DONE**
Fixed **S1** and **S5**.
1. The **weekly grind** (§5): every character loses 1 Motivation when the week closes, unless
   they allocated a Rest that week. Seven weeks, seven grinds - a standing drain that Rest and
   Team Need have to actively counteract.
2. Committing the week *before* Events are drawn (§6.1) turned out to be the larger pressure
   source than the grind.

**Still open from Stage 0:** Motivation has only two things to buy. If a playtest shows tokens
being lost but never *spent*, it's still a health bar - build it a shop or stop calling it a
currency.

**Target outcome to check:** at least one character gets within 1 of quitting in a normal
game, and Rest gets allocated without prompting.

---

### Stage 4 - Rebuild the work economy ✅ **DONE**
Fixed **B3**, bound-first: the weekly output bound (§7) and the feature absorption cap (§10)
were set *before* any cost was chosen, then Work Costs were derived from them - **66 total**,
sitting at the conservative bottom of the 55-65% band so the model can be wrong in either
direction without breaking.

**What a playtest still has to confirm:**
1. **The real output rate.** Everything above hangs off ~1.3 Work per Work person-day. Count
   it directly: total Work delivered ÷ person-days spent on Work.
2. **Whether the absorption cap of 3 is right.** Too low and the team is idle; too high and it
   never binds. Watch whether anyone ever *wants* a 4th day on a feature.
3. **Team Score thresholds** re-derived from observed scores, not the guess at 70.

---

### Stage 5 - Make all four Team State tracks load-bearing ✅ **DONE**
Fixed **S2**, as a side effect of the week-turn. §4 now gives each track a live effect: Trust
gates Learn, Capability modifies Work, Shared Practice halves Learn's cost, and Adaptability
is the per-turn re-planning budget. Achievement discounts (§18) sit on top as the bonus, not
as the reason the track exists.

**Still to test:** whether a table now invests in more than one track, and whether cheap
teaching → Capability → more Work runs away.

---

### Stage 6 - Pay off Base and Legs
Fixes **S3**.
1. **Base → starting Knowledge** (unique, teachable, so losing that person hurts).
2. **Legs → the Skill** that grants the activity bonus.
3. Then write strength/tendency pairs for **all six** Heads and **all** Torso values - not two
   worked examples. This is a content grind, not a design problem; budget a session for it.

**Done when:** every part of the figure is referenced by at least one rule.

---

### Stage 7 - Unlock Capital ✅ **DONE** (except sponsorship)
Fixed **B4**. Applied to §5.1: four conversion routes into Capital (teach, deliver, successful
Demo, a habitus strength that visibly landed), capped at +1 per character per week, all
requiring the team to witness it - and the Demo gate plus the Take Charge pattern now read
**≥ the team average** instead of ≥ 3.

**Held deliberately:** Fix 3 (sponsorship / consecration) is written into §5.1 as an inactive
module. Turn it on only if a playtest shows Capital genuinely concentrating in one character.
If it doesn't concentrate, sponsorship is solving a problem the game doesn't have.

---

### Stage 8 - Raise Event pressure and volume
Fixes **M6**, part of **S1**. (M7 closed separately in v0.20 - see above.)
1. Move to roughly 2 Events per week so the deck and its habitus exceptions actually get seen.
2. Fix **M5** - no player elimination.

---

### Stage 9 - Reintroduce the deferred subsystems, one per playtest
Plan, Demo, Reflect, Meet, Quality, Shared Practice, Adaptability, Team Need, Onboarding,
Achievements, Team Score.

**Rule for this stage:** add **one** back per session, and if it doesn't change a decision
somebody actually makes at the table, cut it permanently. This is where the game gets elegant - by things failing to earn their way back in.

---

### Stage 10 - Only now, 3D print
Fixes nothing; it's the reward. Do not print a 5-part modular miniature until the habitus
options are frozen (Stage 6) - the part count is roughly *(bases + legs + torsos + heads +
items) × players*, and every option change is a reprint. Hand this stage to the
`board-game-3d-printing` skill when Stage 6 closes.

---

## 7. Two things flagged, not changed

Per advisory-first: these contradict the **locked** v0.1 concept, so they're raised here rather
than edited into [concept.md](./concept.md).

1. **The 60-90 minute play-time target is not achievable at 35 days** - now quantified in
   **B3b**: a first playthrough is 125+ minutes, and even experienced players hit ~95. The
   recommended fix (**make the week the turn**, 7 turns of 5 person-days each) lands at ~81
   minutes and preserves "7 weeks / 35 working days" exactly - but it contradicts the concept's
   stated core fantasy, *"Every day you choose what the team spends its time on."* That's a
   concept edit and needs a deliberate answer before Stage 4.
2. **§3.2's "26 work against 35 available days" was arithmetically wrong** as a statement of
   tension (**B3**) - it compared work to the calendar while the game spends person-days. The
   rulebook now says 140 person-days, but the same framing is echoed in the concept's
   description of the core mechanic, so [concept.md](./concept.md) still needs the matching
   correction. Flagged, not edited.
