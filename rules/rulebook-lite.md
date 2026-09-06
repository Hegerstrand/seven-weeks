# Rulebook - High-Performance Team **LITE** (v0.1-lite)

Status: **first-playtest cut. Not a replacement for [rulebook.md](./rulebook.md)** - it is a
deliberately reduced version built to answer three questions cheaply, per Stage 2 of the
[playability assessment](../docs/playability-assessment.md).

Target: **75 minutes inside a 90-minute slot** (§11), 4 players, **nothing 3D-printed**,
everything on paper.

---

## 1. What this version is for

Lite exists to answer exactly three questions. Everything else is noise for now.

- **Q1 - Pace.** Is the Decide → Execute → Update loop fast enough? *Target: under 3 minutes
  per in-game day.*
- **Q2 - Meaningful choice.** Is **Work** ever *not* the obvious action? Do Coordinate, Learn,
  Align and Rest earn their day?
- **Q3 - Habitus.** Does the figure you built actually change how you behave, or is it a
  costume?

Record the answer to each in the [playtest log](../playtests/README.md). If Q2 comes back
*"Work was always right"*, stop - that invalidates the action economy and nothing below is
worth tuning.

### Deliberately deferred (cut, not deleted)
Capital · Demo · Plan · Reflect · Meet · hidden Quality · Shared Practice · Adaptability ·
Team Need · Onboarding · Achievements · Team Score · the ~30-card Event deck · 3D-printed
miniatures. All of these stay in the full [rulebook.md](./rulebook.md) and come back one at a
time from Stage 9 of the assessment.

---

## 2. Components (all paper - build in about 20 minutes)

| Component | Qty | Make it from |
|---|---|---|
| Habitus part cards (Base / Legs / Torso / Head / Item - 4 options each) | 20 | Index cards, cut in half |
| Character card | 4 | Index card: name, Motivation boxes, Knowledge, Item-used box |
| Motivation tokens | 20 (5 per player) | Cubes, beans, coins |
| Feature cards A - D | 4 | Index cards: name, Work Cost, dependency, Work counter |
| Feature blocks (banked features only) | 4 | Wooden blocks / dice / anything stackable |
| Trust track (0-5) | 1 | Drawn line + a marker |
| Capability track (0-5) | 1 | Drawn line + a marker |
| Day track (1-15) | 1 | Drawn line + a marker |
| Event cards | 12 | Index cards, text copied from §8 |

**Do not 3D print anything yet.** The habitus "figure" in Lite is five part-cards laid in a
vertical column in front of the player - Base at the bottom, Item at the top. It reads at a
glance and costs nothing to change between sessions. That's the point.

---

## 3. Setup - build your habitus first (this is still turn zero)

Same principle as the full rulebook §3.1: **players build characters before a single project
rule is explained.** Lay the four options for each part face-up in five rows. Each player, in
order, takes one card from each row and stacks their column bottom-to-top:

**Base → Legs → Torso → Head → Item.**

Then - and only then - read §4 onward.

### Base - upbringing → your starting **Knowledge**
You alone hold this until you teach it (§6, Learn).

| Base | Knowledge | Effect while you hold it |
|---|---|---|
| Academic | *Domain Insight* | Your Work on **C** or **D** produces +1. |
| Trade / working-class | *Craft* | Your Work on **A** or **B** produces +1. |
| Entrepreneurial | *Customer Sense* | Your Align also banks +1 Work on the feature you cleared. |
| Public sector | *Process* | Ignore the first Work loss from an Event each week. |

### Legs - education → your **Skill**
Take that Activity, get **+1** to its effect. That's it.

| Legs | Skill | Bonus on |
|---|---|---|
| Technical | Technical | Work |
| Social | Facilitation | Coordinate |
| Commercial | Communication | Align |
| Academic | Teaching | Learn |

### Torso - value → how **Events** land on you
Event cards are tagged **MGMT**, **PEOPLE**, or **WORK** (§8).

| Torso | Effect |
|---|---|
| Autonomy | **MGMT** Events cost you 1 extra Motivation. |
| Hierarchy | **MGMT** Events cost you no Motivation at all. |
| Community | **PEOPLE** Events cost you 1 extra Motivation - but you gain +1 Motivation every time any character Coordinates. |
| Quality | **WORK** Events cost you 1 extra Motivation - but once per game you may cancel one Work loss entirely. |

### Head - pressure response → your **strength & tendency**
Never a flat bonus. Every one of these costs you something.

| Head | Strength | Tendency |
|---|---|---|
| **Take Charge** | Your Work produces +1 while your Capital is the highest at the table. | Each time you use it, **−1 Trust** unless another character also Worked that same feature today. |
| **Analyze** | Your Align clears an Unclear feature **and** gives +1 Trust. | Your Work on an **Unclear** feature produces **−1** (min 0). You can't stop questioning it. |
| **Support** | Your Coordinate gives **+1 Motivation to every character**, on top of the Trust. | Your Work always produces exactly 1 - no Skill, Knowledge or Capability bonus ever applies to it. |
| **Withdraw** | Your Work produces +1 on any day when **no character** took Coordinate or Align. | **−1 Trust** at the end of any week in which you never took Coordinate or Align. |

### Item - the **hero moment** (one-shot)
Once per game: **spend 1 Motivation to buy yourself a second person-day today.** The second
action must match your item. This is the two-currency system in one line - you can't make more
time, but you can buy it out of a person.

| Item | Second action must be |
|---|---|
| Laptop | Work |
| Clipboard | Align |
| Coffee cup | Coordinate |
| Wrench | Learn |

Tick the box on your character card when it's spent. It does not come back.

### Starting values
- Every character: **3 Motivation** (cap 5).
- **Trust: 2.** **Capability: 2.** (Both 0-5.)
- Day marker on **Day 1**.

---

## 4. The project

| Feature | Work Cost | Depends on |
|---|---|---|
| **A** | 4 | - |
| **B** | 6 | - |
| **C** | 7 | A banked |
| **D** | 9 | B banked |

Total **26 Work**, against a budget of **60 person-days** (4 characters × 15 days) - of which
Events will destroy roughly 4 or 5. That puts Work at about **51% of the usable budget**:
deliberately a shade loose for a first session. §10 has the tightened numbers for session 2.

Each feature card has a **Work counter** starting at 0. A feature can't receive Work until its
dependency is **banked**. When a feature's counter reaches its Work Cost, **bank it**: put its
block on the stack in the middle of the table. That stack is the only visible record of what
you've actually delivered.

---

## 5. The working day

Fifteen days. Each one:

1. **Event** - on days **2, 5, 8, 11, 14** only: flip the top Event card and resolve it.
2. **Decide & Execute** - **each character has exactly one person-day** and spends it on an
   Activity (§6). Resolve them in any order the team likes. *Each player chooses their own
   character's action* - advise, but don't take someone else's turn for them.
3. **Update** - adjust Work counters, Trust, Capability, Motivation. Bank any completed
   feature.
4. **Advance** - move the day marker. At the end of **Day 5** and **Day 10**, resolve the
   weekly grind (§7).

> **The currency rule, stated once.** The team spends **person-days**: one per character per
> day, never saved, never carried over, never given away. An Activity involving N characters
> costs **N person-days** - so a **Learn costs 2**, the teacher's day and the learner's.
> There is no separate "team day."
>
> The second currency is **Motivation** - personal, and the only way to buy more out of a day
> than it holds (the Item hero moment, §3). Weeks are just the accounting period for the
> grind (§7) - not a third thing you spend.

---

## 6. Activities - five, each with an exact number

All cost the acting character their person-day. **Learn costs two** - see the note below.

| Activity | Cost | Effect |
|---|---|---|
| **Work** | 1 person-day | Add **+1** to one feature's Work counter. Modified by: Capability (§7), your Knowledge (§3), your Head (§3), Technical skill (+1), and Unclear (−1). Minimum 0. |
| **Align** | 1 person-day | Clear the **Unclear** flag from one feature. If no feature is Unclear: **+1 Trust** instead. |
| **Coordinate** | 1 person-day each | **+1 Trust.** If **two or more** characters Coordinate on the same day, also **+1 Capability**. |
| **Learn** | **2 person-days** | Name one Knowledge you hold and one other character - **both of you spend your day**, and they now hold it too. The **third** time a given Knowledge is taught to someone new, **+1 Capability** (once per Knowledge). **Learn does nothing while Trust ≤ 1.** |
| **Rest** | 1 person-day | **+2 Motivation** to yourself (cap 5), and you take no weekly grind loss this week (§7). |

Learn costing both people is deliberate: teaching is the most expensive thing in the game, and
spreading Knowledge is what stops one person leaving from wrecking you. Watch whether the team
ever thinks it's worth two days - that's half of Q2.

Each track may rise by at most **1 per day**, no matter how many person-days push at it.

---

## 7. Team State, Motivation, and the grind

### Capability (0-5, starts 2)
- **≥ 4** → every Work action produces **+1**.
- **≤ 1** → every Work action produces **−1** (min 0).

### Trust (0-5, starts 2)
- **≥ 4** → once per week, cancel one negative Event effect entirely.
- **≤ 1** → **Learn does nothing.** Knowledge won't move through a team that doesn't trust
  each other.

### Motivation (0-5, starts 3) - and the weekly grind
At the end of **Day 5** and **Day 10**, **every character loses 1 Motivation** - unless they
took **Rest** during that week.

| Tokens | Effect |
|---|---|
| 2-5 | Normal. |
| 1 | Your Work produces −1 (min 0). |
| **0** | **You quit.** Your character is out for the rest of the game. Any Knowledge only you held is lost. |

This grind is the whole point of Lite. It's what makes Rest cost a real day and pay a real
return - and it's what B3/S1 in the [assessment](../docs/playability-assessment.md) says v0.1
was missing.

---

## 8. Event deck - 12 cards, 5 get drawn

Shuffle all 12. Draw on days 2, 5, 8, 11, 14. Tags drive the Torso effects in §3.

**MGMT**
> **STATUS MEETING** - everyone is in a meeting. Only **one** character (team's choice) keeps
> their person-day. Everyone else's is lost.

> **BUDGET CUT** - every character: **−1 Motivation**.

> **NEW REPORT DUE** - one character (team's choice) spends their person-day writing a report.
> No other effect.

> **MANAGEMENT PRAISE** - if a feature was banked in the last 3 days, every character: **+1
> Motivation**. Otherwise nothing happens.

**PEOPLE**
> **CONFLICT** - **−1 Trust**. If Trust is now 1 or lower, also **−1 Motivation** to everyone.

> **OUT SICK** - the character holding the most Knowledge loses their person-day for the next
> **2 days**.

> **BORROWED BY ANOTHER PROJECT** - the character with the **most** Motivation is loaned out
> and loses their person-day for the next **3 days**.

> **MENTORSHIP** - the next **Learn** taken this week also gives **+1 Trust**.

**WORK**
> **UNCLEAR REQUIREMENT** - flag the unbanked feature with the **highest remaining** Work Cost
> as **Unclear**. Work on it produces −1 (min 0) until an Align clears it.

> **REWORK** - one feature (team's choice, banked or not) loses **2** Work. If that drops a
> banked feature below its Work Cost, take its block **off** the stack.

> **TOOLING OUTAGE** - all Work actions today produce **0**.

> **SCOPE CREEP** - the unbanked feature **closest to completion** gains **+3** Work Cost.

---

## 9. Ending and outcome

The game ends after Day 15 resolves. Three outcomes:

- **Failure** - fewer than four features banked, **or** any character quit.
- **Delivered, team damaged** - all four banked, but **Trust + Capability is 6 or lower**.
  You shipped it. Look at what it cost.
- **High-performing team** - all four banked, nobody quit, and **Trust + Capability is 7 or
  higher**.

Both thresholds are first guesses. Write the actual final numbers in the playtest log so
Stage 4 has real data to tune against.

---

## 10. How to run the session

Following [board-game-playtesting](../playtests/README.md) practice:

- **4 players.** At least one person from outside the board-game hobby - testing only with
  hobbyists systematically hides onboarding problems.
- **A named teacher.** Whoever knows the rules sits at the table and actively coaches
  **Week 1** (days 1-5), then deliberately steps back and shuts up for days 6-15. Note the
  exact moment you stopped needing to help.
- **Build the habitus columns before explaining anything.** No exceptions. That ritual is the
  onboarding, and Lite is partly a test of whether it survives contact with a first-timer.
- **Time the days.** Write down how long day 1, day 5 and day 12 each took. That's Q1's
  answer.
- **Write down what people say**, not what they scored. The quotes are the data.

### The three things to watch for
| Question | What a good answer looks like |
|---|---|
| **Q1 Pace** | Days settling to under 3 minutes by week 2, without the teacher. |
| **Q2 Choice** | Someone visibly agonises over Work vs. Rest/Learn - and at least once, chooses not to Work and is right. Watch Learn especially: at 2 person-days it's the priciest thing on the board. |
| **Q3 Habitus** | A player says *"I can't do that, I'm a Withdraw"* - or refuses a sensible play because it's out of character. |

**Also record, every session:** how many of the 60 person-days went to Work vs. everything
else, and how many Motivation tokens were *spent* (as opposed to lost). Those two numbers are
what Stage 4 tunes against.

### The dials to turn afterwards

Lite session 1 is deliberately set **slightly loose** - Work + expected rework is about **51%**
of the usable budget, just under the 55-65% target band. A first playthrough that's a little
generous teaches you more than one that crushes the table in week 2. Tighten in session 2:

| Variant | A | B | C | D | Total Work | ≈ % of usable budget | Use when |
|---|---|---|---|---|---|---|---|
| **Easier** | 3 | 5 | 6 | 8 | 22 | ~44% | Session 1 was a bloodbath, or you have first-timers |
| **Session 1 (calibration)** | **4** | **6** | **7** | **9** | **26** | **~51%** | Default. Start here. |
| **Tightened** | 5 | 7 | 9 | 11 | 32 | ~62% | Session 1 was comfortable - most likely outcome |

*(Usable budget = 60 person-days − ~4.5 destroyed by Events ≈ 55.5.)*

**Other dials, in the order worth trying:**
- **Too easy on Motivation?** Make the weekly grind hit **even if you Rested** (Rest then only
  buys back the +2). This is the strongest single squeeze in the game.
- **Too easy on time?** Move Events to days 3, 6, 9, 12, 15 - one extra draw's worth of damage.
- **Too hard?** Push Events to days 3, 7, 11 (three draws instead of five).
- **Running long?** Cut to 10 days with the Easier column. Don't cut players - the discussion,
  not the arithmetic, is what makes the habitus visible.

---

## 11. Time budget - how this fits in 90 minutes

| Phase | Minutes |
|---|---|
| Habitus build (§3) - five part-cards each, explained as you go | 12 |
| Rules teach - 5 activities, 2 tracks, features, the grind | 8 |
| **Play - 15 days** (~5 min/day for days 1-3, ~3.5 for 4-8, ~2.5 from day 9) | **50** |
| Wrap-up and outcome | 5 |
| **Total** | **75 min** |

That leaves ~15 minutes of buffer inside 90 for the debrief, which you should actually use.

**Why 15 days and not 35:** at the same per-day rates, the full 35-day calendar is 100 minutes
of play plus 25 of overhead - **125 minutes**, and that assumes nothing goes wrong. See B3b in
the [assessment](../docs/playability-assessment.md). 20 days is the absolute ceiling for a
90-minute session and leaves no room to debrief.

**Watch the clock and write it down.** Time day 1, day 5 and day 12 with a phone. If day 12 is
still over 3 minutes, that's Q1 failing, and it matters more than anything else you learn - the full game is 2.3× longer, so a 3.5-minute day here is a 2-hour game there.

---

## Changelog
- **v0.1-lite** - first cut, derived from [rulebook.md](./rulebook.md) v0.1 in response to the
  [playability assessment](../docs/playability-assessment.md). Closes B1 (every Activity has a
  number), B2 (currency settled: **person-days + Motivation**, §5), B3 (26 Work against 60
  person-days ≈ 51% of usable budget, vs. 19% in the full game), B3b (15 days models to 75
  minutes - §11), and S1 (the weekly grind gives Motivation a systemic drain). Sidesteps B4 by
  cutting Capital entirely. Fixes S3 by making all five habitus parts mechanically live. Learn
  costs **2** person-days under the settled currency rule - teaching is two people's time. Not yet playtested.
- **v0.2-lite** - pace line removed throughout. Take Charge no longer keys off "Behind"; it now
  triggers on holding the highest Capital at the table.
