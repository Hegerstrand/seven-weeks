# Post-sim report

Games per mode: balanced [feature_costs=3-4-4-3-2-2] 2000, invested [feature_costs=3-4-4-3-2-2] 2000, optimal [feature_costs=3-4-4-3-2-2] 2000, balanced [feature_costs=4-5-5-4-2-2] 2000, invested [feature_costs=4-5-5-4-2-2] 2000, optimal [feature_costs=4-5-5-4-2-2] 2000, balanced [feature_costs=4-5-5-4-3-3] 2000, invested [feature_costs=4-5-5-4-3-3] 2000, optimal [feature_costs=4-5-5-4-3-3] 2000. Players: 5. Thresholds: lower 100, upper 150.

## 1. Targets by mode

| Target | balanced [feature_costs=3-4-4-3-2-2] | invested [feature_costs=3-4-4-3-2-2] | optimal [feature_costs=3-4-4-3-2-2] | balanced [feature_costs=4-5-5-4-2-2] | invested [feature_costs=4-5-5-4-2-2] | optimal [feature_costs=4-5-5-4-2-2] | balanced [feature_costs=4-5-5-4-3-3] | invested [feature_costs=4-5-5-4-3-3] | optimal [feature_costs=4-5-5-4-3-3] |
|---|---|---|---|---|---|---|---|---|---|
| Reach UPPER threshold (goal: optimal 80% or more) | 46% | 38% | 89% **PASS** | 70% | 67% | 96% **PASS** | 70% | 65% | 94% **PASS** |
| Reach LOWER threshold (goal: balanced and invested 50% or more) | 79% **PASS** | 74% **PASS** | 94% | 91% **PASS** | 90% **PASS** | 98% | 90% **PASS** | 86% **PASS** | 97% |
| All but 1 action cards played in every game (goal: 95% of games) | 4% **MISS** | 3% **MISS** | 99% **PASS** | 3% **MISS** | 1% **MISS** | 100% **PASS** | 3% **MISS** | 1% **MISS** | 96% **PASS** |
| Every action card played in more than 50% of games (goal in optimal) | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Plan 73% **PASS** | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Celebrate 60% **PASS** | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Celebrate 44% **MISS** |
| Plan plays a game (goal: 1.0 to 2.5) | 3.2 **MISS** | 3.2 **MISS** | 1.0 **MISS** | 4.1 **MISS** | 4.2 **MISS** | 2.1 **PASS** | 4.2 **MISS** | 4.3 **MISS** | 2.9 **MISS** |
| Workshop plays a game (goal: 1.0 to 2.5) | 0.0 **MISS** | 0.0 **MISS** | 1.6 **PASS** | 0.0 **MISS** | 0.0 **MISS** | 2.3 **PASS** | 0.0 **MISS** | 0.0 **MISS** | 1.8 **PASS** |
| Celebrate plays a game (goal: 4 or fewer) | 0.3 **PASS** | 2.2 **PASS** | 3.1 **PASS** | 0.2 **PASS** | 2.0 **PASS** | 0.9 **PASS** | 0.2 **PASS** | 2.1 **PASS** | 0.6 **PASS** |
| Team Reflexivity held at the end (goal: reachable in optimal, 50% or more) | 98% | 94% | 100% **PASS** | 98% | 82% | 98% **PASS** | 98% | 78% | 99% **PASS** |
| Psychological Safety held at the end (goal: reachable in optimal, 50% or more) | 100% | 100% | 100% **PASS** | 100% | 100% | 100% **PASS** | 100% | 100% | 100% **PASS** |
| Quits per 100 character-weeks (HARD goal in optimal: 5 or less) | 1.96 (0.77 a game, 0 quits in 49% of games) | 2.16 (0.85 a game, 0 quits in 45% of games) | 0.18 (0.07 a game, 0 quits in 95% of games) **PASS** | 0.89 (0.35 a game, 0 quits in 74% of games) | 0.70 (0.28 a game, 0 quits in 81% of games) | 0.04 (0.02 a game, 0 quits in 99% of games) **PASS** | 0.84 (0.33 a game, 0 quits in 76% of games) | 0.66 (0.26 a game, 0 quits in 83% of games) | 0.09 (0.04 a game, 0 quits in 97% of games) **PASS** |
| Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none) | 1 of 15 | 1 of 15 | 12 of 15 **MISS** | 3 of 15 | 4 of 15 | 15 of 15 **MISS** | 3 of 15 | 4 of 15 | 14 of 15 **MISS** |
| Most Flex markers held at once (goal: 1 or fewer) | 0 **PASS** | 0 **PASS** | 1 **PASS** | 0 **PASS** | 0 **PASS** | 1 **PASS** | 0 **PASS** | 0 **PASS** | 1 **PASS** |
| Quality quits after a week without Work (goal in optimal: 0.05 or less) | 0.660 | 0.743 | 0.062 **MISS** | 0.259 | 0.204 | 0.006 **PASS** | 0.231 | 0.165 | 0.024 **PASS** |
| Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card) | 0.22 | 0.21 | 0.01 **PASS** | 0.07 | 0.06 | 0.01 **PASS** | 0.07 | 0.07 | 0.01 **PASS** |
| Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%) | 1.9% **PASS** | 2.4% **PASS** | 4.9% **MISS** | 2.8% **PASS** | 4.7% **PASS** | 2.3% **MISS** | 4.8% **PASS** | 9.9% **PASS** | 2.0% **PASS** |
| Autonomy Need met (soft goal: 75% to 100%) | 100% | 99% | 100% **PASS** | 100% | 98% | 100% **PASS** | 100% | 98% | 100% **PASS** |
| Hierarchy Need met (soft goal: 75% to 100%) | 81% | 66% | 93% **PASS** | 82% | 64% | 96% **PASS** | 80% | 61% | 81% **PASS** |
| Community Need met (soft goal: 75% to 100%) | 94% | 93% | 98% **PASS** | 94% | 95% | 98% **PASS** | 94% | 95% | 96% **PASS** |
| Quality Need met (no goal) | 78% | 76% | 93% | 88% | 89% | 100% | 89% | 90% | 99% |
| Recognition Need met (soft goal: 75% to 95%) | 78% | 76% | 84% **PASS** | 76% | 72% | 92% **PASS** | 77% | 74% | 86% **PASS** |

PASS/MISS is only shown where the goal applies to that mode.

## 2. Summary by mode

| Measure | balanced [feature_costs=3-4-4-3-2-2] | invested [feature_costs=3-4-4-3-2-2] | optimal [feature_costs=3-4-4-3-2-2] | balanced [feature_costs=4-5-5-4-2-2] | invested [feature_costs=4-5-5-4-2-2] | optimal [feature_costs=4-5-5-4-2-2] | balanced [feature_costs=4-5-5-4-3-3] | invested [feature_costs=4-5-5-4-3-3] | optimal [feature_costs=4-5-5-4-3-3] |
|---|---|---|---|---|---|---|---|---|---|
| Failure / heroic / sustainable / high performance | 1 / 20 / 33 / 46 % | 1 / 25 / 36 / 38 % | 5 / 1 / 5 / 89 % | 2 / 6 / 21 / 70 % | 4 / 6 / 23 / 67 % | 2 / 0 / 2 / 96 % | 5 / 5 / 20 / 70 % | 10 / 4 / 21 / 65 % | 2 / 1 / 4 / 94 % |
| Mean score (p10 / p90) | 127.6 (70 / 168) | 119.5 (58 / 167) | 158.4 (133 / 176) | 144.6 (106 / 169) | 141.3 (100 / 169) | 164.2 (155 / 174) | 142.7 (98 / 169) | 135.0 (18 / 169) | 162.6 (154 / 173) |
| Features banked, all six | 5.99, 99% | 5.99, 99% | 5.95, 95% | 5.97, 98% | 5.94, 96% | 5.98, 98% | 5.95, 95% | 5.87, 90% | 5.98, 98% |
| Habits held at the end | 4.8 | 4.5 | 4.8 | 4.8 | 4.4 | 4.8 | 4.8 | 4.3 | 4.8 |
| Events cancelled | 10.0 of 11.8 | 9.9 of 11.8 | 10.8 of 11.8 | 10.1 of 11.8 | 9.6 of 11.8 | 11.0 of 11.8 | 10.1 of 11.8 | 9.5 of 11.8 | 10.7 of 11.8 |
| Mean Motivation at week 8 (lowest) | 3.15 (1.85) | 3.05 (1.82) | 4.15 (2.95) | 3.36 (2.01) | 3.54 (2.23) | 4.07 (3.08) | 3.42 (2.09) | 3.61 (2.35) | 3.97 (2.88) |
| Quits a game, games with a quit | 0.77, 51% | 0.85, 55% | 0.07, 5% | 0.35, 26% | 0.28, 19% | 0.02, 1% | 0.33, 24% | 0.26, 17% | 0.04, 3% |
| Capability / Trust / Shared Practice at the end | 4.2 / 4.0 / 5.0 | 3.6 / 4.0 / 5.0 | 4.2 / 4.8 / 5.0 | 4.2 / 4.0 / 5.0 | 3.7 / 4.0 / 4.9 | 4.2 / 4.0 / 5.0 | 4.2 / 4.0 / 5.0 | 3.6 / 4.0 / 4.9 | 4.0 / 4.0 / 5.0 |

## 3. Optimal play only: optimal [feature_costs=3-4-4-3-2-2]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 89% **PASS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 94%
- All but 1 action cards played in every game (goal: 95% of games): 99% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Plan 73% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 1.0 **MISS**
- Workshop plays a game (goal: 1.0 to 2.5): 1.6 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 3.1 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.18 (0.07 a game, 0 quits in 95% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 12 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.062 **MISS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.01 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 4.9% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 93% **PASS**
- Community Need met (soft goal: 75% to 100%): 98% **PASS**
- Quality Need met (no goal): 93%
- Recognition Need met (soft goal: 75% to 95%): 84% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.55 | 3.28 | 3.15 | 2.99 | 3.08 | 3.24 | 2.95 |
| Mean | 4.59 | 4.52 | 4.30 | 4.15 | 3.84 | 4.08 | 4.26 | 4.15 |
| Median | 4.89 | 4.81 | 4.48 | 4.30 | 3.81 | 4.17 | 4.44 | 4.38 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 |

Quit causes per game (biggest Motivation loss in the week): a week without Work (Quality Need) 0.06, the weekly grind 0.01, another character's Hero 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| BUDGET CUT | 2 | 0.165 | 0.066 | 40% |
| THE DATE MOVES UP | say no | 0.160 | 0.064 | 40% |
| STATUS MEETING | 3 | 0.158 | 0.061 | 39% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.028 | 16% |
| FALSE START | 2 | 0.161 | 0.025 | 16% |
| SCOPE CREEP | 3 | 0.179 | 0.018 | 10% |
| REORGANISED | 2 | 0.161 | 0.016 | 10% |
| PRIORITY CHANGES | 2 | 0.159 | 0.016 | 10% |
| SHAKY GROUND | 3 | 0.165 | 0.013 | 8% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.013 | 9% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.012 | 8% |
| THE DASHBOARD | 3 | 0.159 | 0.010 | 6% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.010 | 6% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.009 | 5% |
| THE AUDIT | 2 | 0.151 | 0.008 | 5% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.006 | 4% |
| BURNOUT WARNING | 2 | 0.151 | 0.006 | 4% |
| THE BIKESHED | 1 | 0.158 | 0.004 | 3% |
| THE TEAM SPLITS | 2 | 0.170 | 0.004 | 2% |
| MORE HANDS | 2 | 0.147 | 0.004 | 3% |
| ALWAYS REACTING | 1 | 0.151 | 0.004 | 3% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.003 | 2% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.000 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE TEAM SPLITS | 0.000 | 0.01 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.12 | 0.0 |
| THE DASHBOARD | 0.000 | 0.01 | 0.0 |
| THE BIKESHED | 0.000 | 0.00 | 0.0 |
| THE AUDIT | 0.000 | 0.01 | 0.0 |
| STATUS MEETING | 0.000 | 0.06 | 0.0 |
| SHAKY GROUND | 0.000 | 0.02 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | BUDGET CUT 0.000, STATUS MEETING 0.000, THE WOLF 0.000 |
| torso Hierarchy | FALSE START 0.001, EQUIPMENT OUTAGE 0.001, EVERYTHING AT ONCE 0.000 |
| torso Community | BUDGET CUT 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| torso Quality | THE DATE MOVES UP 0.001, SCOPE CREEP 0.001, REQUIREMENTS CHANGE 0.000 |
| torso Recognition | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs OwnIt | THE DATE MOVES UP 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| legs Analyze | EQUIPMENT OUTAGE 0.001, BUDGET CUT 0.000, FALSE START 0.000 |
| legs Support | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs Engage | THE DATE MOVES UP 0.001, SCOPE CREEP 0.001, FALSE START 0.001 |
| legs SpeakUp | BUDGET CUT 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| base Bookish | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| base HandsOn | SCOPE CREEP 0.001, REQUIREMENTS CHANGE 0.000, FALSE START 0.000 |
| base Sheltered | THE DATE MOVES UP 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| base Dependable | FALSE START 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| base Competitive | BUDGET CUT 0.001, THE DATE MOVES UP 0.001, EQUIPMENT OUTAGE 0.001 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 17.99 |
| Celebrate | 98% | 3.14 |
| Engagement | 100% | 3.39 |
| Workshop | 98% | 1.56 |
| Learn | 100% | 2.43 |
| Teach | 100% | 3.14 |
| Reflect | 100% | 4.04 |
| Plan | 73% | 0.96 |
| Demo | 100% | 2.74 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 0.8 | 4.12 |
| legs SpeakUp | 0.3 | 4.14 |
| legs Engage | 0.3 | 4.02 |
| base Competitive | 0.2 | 4.40 |
| base HandsOn | 0.2 | 4.54 |
| legs OwnIt | 0.2 | 4.17 |
| base Dependable | 0.2 | 4.64 |
| base Sheltered | 0.2 | 2.98 |

Lowest mean Motivation: base Sheltered 2.98, legs Engage 4.02, torso Quality 4.12, legs SpeakUp 4.14.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Quality + instinct SpeakUp | 1.6 | 9.2x | 50 | 3096 |
| values Quality + instinct Engage | 1.3 | 7.3x | 41 | 3201 |
| values Quality + instinct OwnIt | 1.1 | 6.1x | 32 | 2976 |
| values Quality + upbringing Competitive | 1.0 | 5.9x | 32 | 3091 |
| values Quality + upbringing HandsOn | 0.9 | 5.0x | 29 | 3316 |
| values Quality + upbringing Dependable | 0.8 | 4.5x | 27 | 3371 |
| values Quality + upbringing Sheltered | 0.8 | 4.3x | 25 | 3313 |
| instinct SpeakUp + upbringing Competitive | 0.6 | 3.2x | 16 | 2843 |
| values Quality + upbringing Bookish | 0.5 | 3.0x | 16 | 3047 |
| instinct SpeakUp + upbringing HandsOn | 0.4 | 2.1x | 12 | 3175 |
| instinct SpeakUp + upbringing Dependable | 0.4 | 2.0x | 12 | 3426 |
| instinct Engage + upbringing Competitive | 0.3 | 1.9x | 11 | 3231 |

## 3. Optimal play only: optimal [feature_costs=4-5-5-4-2-2]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 96% **PASS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 98%
- All but 1 action cards played in every game (goal: 95% of games): 100% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Celebrate 60% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 2.1 **PASS**
- Workshop plays a game (goal: 1.0 to 2.5): 2.3 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 0.9 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 98% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.04 (0.02 a game, 0 quits in 99% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 15 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.006 **PASS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.01 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 2.3% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 96% **PASS**
- Community Need met (soft goal: 75% to 100%): 98% **PASS**
- Quality Need met (no goal): 100%
- Recognition Need met (soft goal: 75% to 95%): 92% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.55 | 3.00 | 3.12 | 3.10 | 3.12 | 2.81 | 3.08 |
| Mean | 4.59 | 4.54 | 3.86 | 4.06 | 4.11 | 4.08 | 3.77 | 4.07 |
| Median | 4.89 | 4.84 | 3.82 | 4.15 | 4.20 | 4.16 | 3.74 | 4.15 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 |

Quit causes per game (biggest Motivation loss in the week): the weekly grind 0.01, a week without Work (Quality Need) 0.01, another character's Hero 0.00, Events 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| THE DATE MOVES UP | say no | 0.160 | 0.065 | 41% |
| FALSE START | 2 | 0.161 | 0.015 | 9% |
| BUDGET CUT | 2 | 0.165 | 0.012 | 7% |
| REORGANISED | 2 | 0.161 | 0.011 | 7% |
| THE AUDIT | 2 | 0.151 | 0.009 | 6% |
| STATUS MEETING | 3 | 0.158 | 0.009 | 5% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.007 | 4% |
| THE BIKESHED | 1 | 0.158 | 0.006 | 4% |
| PRIORITY CHANGES | 2 | 0.159 | 0.006 | 4% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.006 | 4% |
| SCOPE CREEP | 3 | 0.179 | 0.005 | 3% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.005 | 3% |
| THE TEAM SPLITS | 2 | 0.170 | 0.005 | 3% |
| SHAKY GROUND | 3 | 0.165 | 0.004 | 3% |
| MORE HANDS | 2 | 0.147 | 0.004 | 3% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.004 | 3% |
| BURNOUT WARNING | 2 | 0.151 | 0.004 | 3% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.003 | 2% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.003 | 2% |
| ALWAYS REACTING | 1 | 0.151 | 0.003 | 2% |
| THE DASHBOARD | 3 | 0.159 | 0.002 | 1% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.002 | 1% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.000 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| STATUS MEETING | 0.001 | 0.01 | 4.2 |
| REQUIREMENTS CHANGE | 0.001 | 0.01 | 5.0 |
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE TEAM SPLITS | 0.000 | 0.01 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.10 | 0.0 |
| THE DASHBOARD | 0.000 | 0.01 | 0.0 |
| THE BIKESHED | 0.000 | 0.01 | 0.0 |
| THE AUDIT | 0.000 | 0.01 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | STATUS MEETING 0.000, REORGANISED 0.000, THE WOLF 0.000 |
| torso Hierarchy | EVERYTHING AT ONCE 0.001, SHAKY GROUND 0.001, FALSE START 0.001 |
| torso Community | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| torso Quality | THE DASHBOARD 0.002, PRIORITY CHANGES 0.001, THE DATE MOVES UP 0.001 |
| torso Recognition | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs OwnIt | NEGATIVE FEEDBACK 0.001, EVERYTHING AT ONCE 0.001, THE DASHBOARD 0.000 |
| legs Analyze | THE DATE MOVES UP 0.001, SHAKY GROUND 0.001, FALSE START 0.001 |
| legs Support | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs Engage | THE DASHBOARD 0.001, PRIORITY CHANGES 0.001, BUDGET CUT 0.001 |
| legs SpeakUp | THE DASHBOARD 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| base Bookish | THE DASHBOARD 0.001, NEGATIVE FEEDBACK 0.001, THE WOLF 0.000 |
| base HandsOn | EVERYTHING AT ONCE 0.001, THE DATE MOVES UP 0.001, BUDGET CUT 0.001 |
| base Sheltered | THE DASHBOARD 0.001, REQUIREMENTS CHANGE 0.000, PRIORITY CHANGES 0.000 |
| base Dependable | PRIORITY CHANGES 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| base Competitive | THE DASHBOARD 0.001, SHAKY GROUND 0.001, SCOPE CREEP 0.001 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 20.80 |
| Celebrate | 60% | 0.89 |
| Engagement | 100% | 3.00 |
| Workshop | 100% | 2.33 |
| Learn | 100% | 2.04 |
| Teach | 99% | 3.28 |
| Reflect | 100% | 2.99 |
| Plan | 100% | 2.05 |
| Demo | 100% | 2.17 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 0.1 | 4.16 |
| base Competitive | 0.1 | 4.22 |
| legs Analyze | 0.1 | 4.37 |
| legs OwnIt | 0.1 | 4.01 |
| base HandsOn | 0.1 | 4.40 |
| torso Hierarchy | 0.1 | 4.14 |
| torso Community | 0.0 | 4.15 |
| base Sheltered | 0.0 | 2.99 |

Lowest mean Motivation: base Sheltered 2.99, legs Engage 3.87, legs SpeakUp 3.99, legs OwnIt 4.01.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| instinct Analyze + upbringing Competitive | 0.2 | 5.8x | 8 | 3328 |
| values Community + instinct Analyze | 0.2 | 4.6x | 6 | 3127 |
| values Quality + upbringing Sheltered | 0.2 | 4.3x | 6 | 3333 |
| values Quality + instinct OwnIt | 0.2 | 4.0x | 5 | 2989 |
| values Hierarchy + upbringing Competitive | 0.2 | 3.7x | 5 | 3227 |
| values Community + upbringing Competitive | 0.1 | 3.1x | 4 | 3059 |
| values Hierarchy + instinct Analyze | 0.1 | 3.1x | 4 | 3102 |
| values Quality + upbringing Competitive | 0.1 | 3.1x | 4 | 3106 |
| values Quality + instinct Engage | 0.1 | 3.0x | 4 | 3220 |
| instinct Analyze + upbringing HandsOn | 0.1 | 3.0x | 4 | 3245 |
| values Quality + instinct Analyze | 0.1 | 2.8x | 4 | 3418 |
| values Hierarchy + upbringing HandsOn | 0.1 | 2.4x | 3 | 3033 |

## 3. Optimal play only: optimal [feature_costs=4-5-5-4-3-3]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 94% **PASS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 97%
- All but 1 action cards played in every game (goal: 95% of games): 96% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Celebrate 44% **MISS**
- Plan plays a game (goal: 1.0 to 2.5): 2.9 **MISS**
- Workshop plays a game (goal: 1.0 to 2.5): 1.8 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 0.6 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 99% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.09 (0.04 a game, 0 quits in 97% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 14 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.024 **PASS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.01 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 2.0% **PASS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 81% **PASS**
- Community Need met (soft goal: 75% to 100%): 96% **PASS**
- Quality Need met (no goal): 99%
- Recognition Need met (soft goal: 75% to 95%): 86% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.51 | 3.23 | 3.09 | 3.07 | 2.97 | 2.71 | 2.88 |
| Mean | 4.59 | 4.51 | 4.23 | 3.98 | 4.10 | 4.02 | 3.75 | 3.97 |
| Median | 4.89 | 4.81 | 4.37 | 3.98 | 4.21 | 4.12 | 3.73 | 4.06 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.02 |

Quit causes per game (biggest Motivation loss in the week): a week without Work (Quality Need) 0.02, the weekly grind 0.01, another character's Hero 0.00, Events 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| BUDGET CUT | 2 | 0.165 | 0.066 | 40% |
| THE DATE MOVES UP | say no | 0.160 | 0.065 | 40% |
| STATUS MEETING | 3 | 0.158 | 0.062 | 40% |
| FALSE START | 2 | 0.161 | 0.030 | 19% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.029 | 16% |
| SCOPE CREEP | 3 | 0.179 | 0.021 | 12% |
| REORGANISED | 2 | 0.161 | 0.019 | 12% |
| PRIORITY CHANGES | 2 | 0.159 | 0.018 | 11% |
| SHAKY GROUND | 3 | 0.165 | 0.017 | 10% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.015 | 9% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.014 | 9% |
| THE DASHBOARD | 3 | 0.159 | 0.012 | 8% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.012 | 7% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.011 | 7% |
| THE BIKESHED | 1 | 0.158 | 0.009 | 6% |
| THE AUDIT | 2 | 0.151 | 0.009 | 6% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.008 | 5% |
| THE TEAM SPLITS | 2 | 0.170 | 0.005 | 3% |
| BURNOUT WARNING | 2 | 0.151 | 0.005 | 4% |
| MORE HANDS | 2 | 0.147 | 0.005 | 3% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.004 | 3% |
| ALWAYS REACTING | 1 | 0.151 | 0.004 | 3% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.001 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| EVERYONE IS EQUAL | 0.001 | 0.01 | 9.1 |
| BUDGET CUT | 0.001 | 0.07 | 0.7 |
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE TEAM SPLITS | 0.000 | 0.01 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.11 | 0.0 |
| THE DASHBOARD | 0.000 | 0.02 | 0.0 |
| THE BIKESHED | 0.000 | 0.01 | 0.0 |
| THE AUDIT | 0.000 | 0.01 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | STATUS MEETING 0.001, BUDGET CUT 0.001, EVERYONE IS EQUAL 0.000 |
| torso Hierarchy | EQUIPMENT OUTAGE 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| torso Community | EVERYONE IS EQUAL 0.000, BUDGET CUT 0.000, THE WOLF 0.000 |
| torso Quality | THE DASHBOARD 0.002, NEGATIVE FEEDBACK 0.001, THE DATE MOVES UP 0.001 |
| torso Recognition | BUDGET CUT 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| legs OwnIt | NEGATIVE FEEDBACK 0.001, THE DASHBOARD 0.000, EVERYONE IS EQUAL 0.000 |
| legs Analyze | BUDGET CUT 0.001, STATUS MEETING 0.000, THE WOLF 0.000 |
| legs Support | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs Engage | THE DASHBOARD 0.001, THE DATE MOVES UP 0.001, EQUIPMENT OUTAGE 0.001 |
| legs SpeakUp | THE DASHBOARD 0.001, EVERYONE IS EQUAL 0.001, STATUS MEETING 0.001 |
| base Bookish | THE DASHBOARD 0.001, NEGATIVE FEEDBACK 0.001, EVERYONE IS EQUAL 0.000 |
| base HandsOn | THE DATE MOVES UP 0.001, EQUIPMENT OUTAGE 0.001, THE WOLF 0.000 |
| base Sheltered | THE DASHBOARD 0.002, EVERYONE IS EQUAL 0.000, BUDGET CUT 0.000 |
| base Dependable | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| base Competitive | BUDGET CUT 0.001, STATUS MEETING 0.001, EVERYONE IS EQUAL 0.000 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 21.75 |
| Celebrate | 44% | 0.60 |
| Engagement | 100% | 3.01 |
| Workshop | 98% | 1.77 |
| Learn | 100% | 1.18 |
| Teach | 99% | 3.44 |
| Reflect | 100% | 3.06 |
| Plan | 100% | 2.92 |
| Demo | 89% | 1.73 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 0.3 | 4.16 |
| legs Engage | 0.2 | 3.83 |
| base Competitive | 0.1 | 4.22 |
| base HandsOn | 0.1 | 4.53 |
| base Bookish | 0.1 | 4.51 |
| legs OwnIt | 0.1 | 4.02 |
| legs SpeakUp | 0.1 | 4.00 |
| legs Analyze | 0.1 | 4.39 |

Lowest mean Motivation: base Sheltered 2.99, legs Engage 3.83, legs SpeakUp 4.00, legs OwnIt 4.02.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Quality + instinct Engage | 0.7 | 7.5x | 23 | 3214 |
| values Quality + upbringing Bookish | 0.6 | 5.9x | 17 | 3056 |
| values Quality + instinct OwnIt | 0.5 | 5.3x | 15 | 2988 |
| values Quality + instinct SpeakUp | 0.4 | 3.7x | 11 | 3105 |
| values Quality + upbringing Sheltered | 0.3 | 3.2x | 10 | 3323 |
| values Quality + upbringing Competitive | 0.3 | 2.7x | 8 | 3100 |
| instinct Analyze + upbringing Competitive | 0.2 | 2.5x | 8 | 3319 |
| values Quality + upbringing HandsOn | 0.2 | 2.5x | 8 | 3333 |
| instinct Engage + upbringing Competitive | 0.2 | 2.3x | 7 | 3233 |
| instinct SpeakUp + upbringing Bookish | 0.2 | 2.2x | 6 | 2882 |
| values Quality + upbringing Dependable | 0.2 | 2.2x | 7 | 3380 |
| instinct Engage + upbringing Bookish | 0.2 | 2.1x | 6 | 3013 |
