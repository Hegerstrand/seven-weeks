# Post-sim report

Games per mode: balanced [work_cost_mult=1.0] 2000, invested [work_cost_mult=1.0] 2000, optimal [work_cost_mult=1.0] 2000, balanced [work_cost_mult=1.2] 2000, invested [work_cost_mult=1.2] 2000, optimal [work_cost_mult=1.2] 2000, balanced [work_cost_mult=1.3] 2000, invested [work_cost_mult=1.3] 2000, optimal [work_cost_mult=1.3] 2000, balanced [work_cost_mult=1.5] 2000, invested [work_cost_mult=1.5] 2000, optimal [work_cost_mult=1.5] 2000. Players: 5. Thresholds: lower 100, upper 150.

## 1. Targets by mode

| Target | balanced [work_cost_mult=1.0] | invested [work_cost_mult=1.0] | optimal [work_cost_mult=1.0] | balanced [work_cost_mult=1.2] | invested [work_cost_mult=1.2] | optimal [work_cost_mult=1.2] | balanced [work_cost_mult=1.3] | invested [work_cost_mult=1.3] | optimal [work_cost_mult=1.3] | balanced [work_cost_mult=1.5] | invested [work_cost_mult=1.5] | optimal [work_cost_mult=1.5] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reach UPPER threshold (goal: optimal 80% or more) | 46% | 40% | 80% **PASS** | 67% | 43% | 74% **MISS** | 69% | 43% | 73% **MISS** | 59% | 40% | 23% **MISS** |
| Reach LOWER threshold (goal: balanced and invested 50% or more) | 79% **PASS** | 76% **PASS** | 92% | 90% **PASS** | 78% **PASS** | 85% | 91% **PASS** | 78% **PASS** | 84% | 84% **PASS** | 63% **PASS** | 43% |
| All but 1 action cards played in every game (goal: 95% of games) | 27% **MISS** | 2% **MISS** | 98% **PASS** | 2% **MISS** | 3% **MISS** | 97% **PASS** | 2% **MISS** | 3% **MISS** | 96% **PASS** | 5% **MISS** | 3% **MISS** | 79% **MISS** |
| Every action card played in more than 50% of games (goal in optimal) | fewest: Demo 4% | fewest: Workshop 0% | fewest: Demo 95% **PASS** | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Teach 93% **PASS** | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Demo 90% **PASS** | fewest: Workshop 0% | fewest: Workshop 0% | fewest: Demo 52% **PASS** |
| Plan plays a game (goal: 1.0 to 2.5) | 3.1 **MISS** | 3.3 **MISS** | 1.7 **PASS** | 3.3 **MISS** | 3.3 **MISS** | 2.6 **MISS** | 3.3 **MISS** | 3.3 **MISS** | 2.6 **MISS** | 4.1 **MISS** | 4.3 **MISS** | 4.3 **MISS** |
| Workshop plays a game (goal: 1.0 to 2.5) | 0.9 **MISS** | 0.0 **MISS** | 1.9 **PASS** | 0.0 **MISS** | 0.0 **MISS** | 1.4 **PASS** | 0.0 **MISS** | 0.0 **MISS** | 1.3 **PASS** | 0.0 **MISS** | 0.0 **MISS** | 0.9 **MISS** |
| Celebrate plays a game (goal: 4 or fewer) | 0.3 **PASS** | 2.2 **PASS** | 3.5 **PASS** | 0.2 **PASS** | 2.1 **PASS** | 3.5 **PASS** | 0.2 **PASS** | 2.1 **PASS** | 3.4 **PASS** | 0.3 **PASS** | 2.1 **PASS** | 3.5 **PASS** |
| Team Reflexivity held at the end (goal: reachable in optimal, 50% or more) | 95% | 78% | 98% **PASS** | 98% | 94% | 100% **PASS** | 97% | 94% | 98% **PASS** | 94% | 55% | 26% **MISS** |
| Psychological Safety held at the end (goal: reachable in optimal, 50% or more) | 100% | 100% | 100% **PASS** | 100% | 100% | 100% **PASS** | 100% | 100% | 100% **PASS** | 100% | 100% | 100% **PASS** |
| Quits per 100 character-weeks (HARD goal in optimal: 5 or less) | 1.95 (0.77 a game, 0 quits in 48% of games) | 1.98 (0.78 a game, 0 quits in 50% of games) | 0.38 (0.15 a game, 0 quits in 89% of games) **PASS** | 1.00 (0.40 a game, 0 quits in 72% of games) | 1.87 (0.74 a game, 0 quits in 52% of games) | 0.20 (0.08 a game, 0 quits in 94% of games) **PASS** | 0.91 (0.36 a game, 0 quits in 74% of games) | 1.83 (0.72 a game, 0 quits in 53% of games) | 0.16 (0.06 a game, 0 quits in 95% of games) **PASS** | 1.00 (0.39 a game, 0 quits in 74% of games) | 0.98 (0.38 a game, 0 quits in 81% of games) | 0.35 (0.14 a game, 0 quits in 93% of games) **PASS** |
| Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none) | 3 of 15 | 2 of 15 | 6 of 15 **MISS** | 3 of 15 | 1 of 15 | 11 of 15 **MISS** | 3 of 15 | 1 of 15 | 13 of 15 **MISS** | 1 of 15 | 0 of 15 | 4 of 15 **MISS** |
| Most Flex markers held at once (goal: 1 or fewer) | 0 **PASS** | 0 **PASS** | 1 **PASS** | 0 **PASS** | 0 **PASS** | 1 **PASS** | 0 **PASS** | 0 **PASS** | 1 **PASS** | 0 **PASS** | 0 **PASS** | 1 **PASS** |
| Quality quits after a week without Work (goal in optimal: 0.05 or less) | 0.685 | 0.683 | 0.138 **MISS** | 0.300 | 0.625 | 0.061 **MISS** | 0.263 | 0.611 | 0.049 **PASS** | 0.193 | 0.046 | 0.026 **PASS** |
| Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card) | 0.22 | 0.21 | 0.02 **PASS** | 0.08 | 0.18 | 0.01 **PASS** | 0.07 | 0.18 | 0.01 **PASS** | 0.14 | 0.21 | 0.08 **PASS** |
| Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%) | 1.4% **PASS** | 2.2% **PASS** | 5.8% **MISS** | 2.0% **PASS** | 2.8% **PASS** | 13.1% **MISS** | 2.5% **PASS** | 3.1% **PASS** | 14.3% **MISS** | 10.2% **PASS** | 34.1% **PASS** | 56.5% **MISS** |
| Autonomy Need met (soft goal: 75% to 100%) | 99% | 98% | 100% **PASS** | 100% | 99% | 100% **PASS** | 100% | 99% | 100% **PASS** | 99% | 96% | 98% **PASS** |
| Hierarchy Need met (soft goal: 75% to 100%) | 94% | 63% | 88% **PASS** | 81% | 66% | 71% **MISS** | 80% | 66% | 71% **MISS** | 59% | 27% | 57% **MISS** |
| Community Need met (soft goal: 75% to 100%) | 96% | 95% | 99% **PASS** | 94% | 93% | 97% **PASS** | 94% | 93% | 97% **PASS** | 93% | 91% | 95% **PASS** |
| Quality Need met (no goal) | 78% | 78% | 91% | 87% | 79% | 96% | 88% | 79% | 96% | 92% | 99% | 99% |
| Recognition Need met (soft goal: 75% to 95%) | 63% | 62% | 79% **PASS** | 84% | 77% | 86% **PASS** | 85% | 77% | 87% **PASS** | 79% | 79% | 76% **PASS** |

PASS/MISS is only shown where the goal applies to that mode.

## 2. Summary by mode

| Measure | balanced [work_cost_mult=1.0] | invested [work_cost_mult=1.0] | optimal [work_cost_mult=1.0] | balanced [work_cost_mult=1.2] | invested [work_cost_mult=1.2] | optimal [work_cost_mult=1.2] | balanced [work_cost_mult=1.3] | invested [work_cost_mult=1.3] | optimal [work_cost_mult=1.3] | balanced [work_cost_mult=1.5] | invested [work_cost_mult=1.5] | optimal [work_cost_mult=1.5] |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Failure / heroic / sustainable / high performance | 1 / 20 / 34 / 46 % | 1 / 23 / 36 / 40 % | 6 / 3 / 11 / 80 % | 1 / 8 / 23 / 67 % | 2 / 20 / 35 / 43 % | 13 / 2 / 12 / 74 % | 2 / 7 / 22 / 69 % | 2 / 20 / 35 / 43 % | 14 / 2 / 11 / 73 % | 10 / 6 / 25 / 59 % | 34 / 2 / 24 / 40 % | 56 / 1 / 20 / 23 % |
| Mean score (p10 / p90) | 129.2 (73 / 170) | 121.2 (59 / 167) | 149.3 (109 / 173) | 143.2 (100 / 169) | 124.1 (61 / 168) | 133.7 (0 / 169) | 144.2 (105 / 169) | 124.2 (61 / 168) | 132.1 (0 / 169) | 130.7 (0 / 168) | 95.5 (0 / 156) | 63.9 (0 / 157) |
| Features banked, all six | 5.99, 99% | 5.99, 99% | 5.94, 94% | 5.98, 99% | 5.98, 98% | 5.86, 87% | 5.97, 98% | 5.97, 98% | 5.84, 86% | 5.87, 90% | 5.51, 66% | 5.19, 44% |
| Habits held at the end | 4.8 | 4.3 | 4.7 | 4.8 | 4.5 | 4.1 | 4.8 | 4.4 | 4.1 | 4.4 | 3.2 | 3.1 |
| Events cancelled | 10.4 of 11.8 | 9.4 of 11.8 | 10.9 of 11.8 | 10.0 of 11.8 | 9.9 of 11.8 | 10.8 of 11.7 | 10.0 of 11.8 | 9.8 of 11.8 | 10.7 of 11.7 | 9.7 of 11.8 | 8.7 of 11.7 | 9.8 of 11.7 |
| Mean Motivation at week 8 (lowest) | 3.21 (1.93) | 3.19 (1.96) | 3.95 (2.73) | 3.32 (1.98) | 3.13 (1.86) | 4.01 (2.88) | 3.35 (2.00) | 3.14 (1.88) | 4.05 (2.93) | 3.40 (2.10) | 3.62 (2.55) | 4.00 (3.03) |
| Quits a game, games with a quit | 0.77, 52% | 0.78, 50% | 0.15, 11% | 0.40, 28% | 0.74, 48% | 0.08, 6% | 0.36, 26% | 0.72, 47% | 0.06, 5% | 0.39, 26% | 0.38, 19% | 0.14, 7% |
| Capability / Trust / Shared Practice at the end | 4.2 / 4.0 / 5.0 | 3.6 / 4.0 / 4.9 | 4.0 / 4.5 / 5.0 | 4.2 / 4.0 / 5.0 | 3.6 / 4.0 / 5.0 | 2.9 / 4.5 / 5.0 | 4.2 / 4.0 / 5.0 | 3.6 / 4.0 / 5.0 | 2.9 / 4.5 / 5.0 | 3.5 / 4.0 / 4.9 | 2.3 / 4.0 / 4.5 | 2.3 / 4.5 / 4.4 |

## 3. Optimal play only: optimal [work_cost_mult=1.0]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 80% **PASS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 92%
- All but 1 action cards played in every game (goal: 95% of games): 98% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Demo 95% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 1.7 **PASS**
- Workshop plays a game (goal: 1.0 to 2.5): 1.9 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 3.5 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 98% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.38 (0.15 a game, 0 quits in 89% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 6 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.138 **MISS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.02 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 5.8% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 88% **PASS**
- Community Need met (soft goal: 75% to 100%): 99% **PASS**
- Quality Need met (no goal): 91%
- Recognition Need met (soft goal: 75% to 95%): 79% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.37 | 2.96 | 3.22 | 3.04 | 3.05 | 3.11 | 2.73 |
| Mean | 4.59 | 4.40 | 3.80 | 4.32 | 3.96 | 4.05 | 4.18 | 3.95 |
| Median | 4.89 | 4.65 | 3.72 | 4.57 | 3.97 | 4.13 | 4.34 | 4.12 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.13 |

Quit causes per game (biggest Motivation loss in the week): a week without Work (Quality Need) 0.14, the weekly grind 0.01, Events 0.00, another character's Hero 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| THE DATE MOVES UP | say no | 0.160 | 0.066 | 41% |
| FALSE START | 2 | 0.161 | 0.014 | 9% |
| BUDGET CUT | 2 | 0.165 | 0.013 | 8% |
| THE AUDIT | 2 | 0.151 | 0.011 | 8% |
| REORGANISED | 2 | 0.161 | 0.011 | 7% |
| STATUS MEETING | 3 | 0.158 | 0.009 | 5% |
| PRIORITY CHANGES | 2 | 0.159 | 0.007 | 4% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.007 | 4% |
| SCOPE CREEP | 3 | 0.179 | 0.006 | 3% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.006 | 4% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.006 | 4% |
| THE TEAM SPLITS | 2 | 0.170 | 0.005 | 3% |
| THE BIKESHED | 1 | 0.158 | 0.005 | 3% |
| SHAKY GROUND | 3 | 0.165 | 0.005 | 3% |
| MORE HANDS | 2 | 0.147 | 0.004 | 3% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.004 | 2% |
| BURNOUT WARNING | 2 | 0.151 | 0.004 | 3% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.003 | 2% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.003 | 2% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.002 | 1% |
| ALWAYS REACTING | 1 | 0.151 | 0.002 | 1% |
| THE DASHBOARD | 3 | 0.159 | 0.002 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.002 | 1% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| EVERYONE IS EQUAL | 0.001 | 0.01 | 18.2 |
| STATUS MEETING | 0.001 | 0.02 | 2.6 |
| REQUIREMENTS CHANGE | 0.001 | 0.01 | 3.7 |
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE TEAM SPLITS | 0.000 | 0.01 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.11 | 0.0 |
| THE DASHBOARD | 0.000 | 0.01 | 0.0 |
| THE BIKESHED | 0.000 | 0.01 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | EVERYONE IS EQUAL 0.001, REORGANISED 0.000, STATUS MEETING 0.000 |
| torso Hierarchy | OLD FOUNDATIONS 0.001, EVERYTHING AT ONCE 0.001, THE WOLF 0.000 |
| torso Community | THE TEAM SPLITS 0.000, EVERYONE IS EQUAL 0.000, THE WOLF 0.000 |
| torso Quality | THE DATE MOVES UP 0.005, THE DASHBOARD 0.003, PRIORITY CHANGES 0.001 |
| torso Recognition | THE WOLF 0.000, THE TEAM SPLITS 0.000, THE DATE MOVES UP 0.000 |
| legs OwnIt | THE DATE MOVES UP 0.002, STATUS MEETING 0.000, REORGANISED 0.000 |
| legs Analyze | THE DATE MOVES UP 0.001, EVERYTHING AT ONCE 0.001, REQUIREMENTS CHANGE 0.000 |
| legs Support | THE DATE MOVES UP 0.001, THE DASHBOARD 0.001, OLD FOUNDATIONS 0.001 |
| legs Engage | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, THE TEAM SPLITS 0.001 |
| legs SpeakUp | THE DASHBOARD 0.001, EVERYONE IS EQUAL 0.000, PRIORITY CHANGES 0.000 |
| base Bookish | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, EVERYONE IS EQUAL 0.000 |
| base HandsOn | EVERYTHING AT ONCE 0.001, THE DATE MOVES UP 0.001, OLD FOUNDATIONS 0.000 |
| base Sheltered | THE DASHBOARD 0.002, PRIORITY CHANGES 0.001, THE DATE MOVES UP 0.001 |
| base Dependable | THE DATE MOVES UP 0.001, THE DASHBOARD 0.001, PRIORITY CHANGES 0.001 |
| base Competitive | THE DATE MOVES UP 0.002, OLD FOUNDATIONS 0.001, EVERYONE IS EQUAL 0.000 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 19.38 |
| Celebrate | 100% | 3.46 |
| Engagement | 100% | 3.49 |
| Workshop | 100% | 1.94 |
| Learn | 100% | 2.33 |
| Teach | 97% | 2.68 |
| Reflect | 100% | 3.61 |
| Plan | 96% | 1.75 |
| Demo | 95% | 1.67 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 1.7 | 4.01 |
| legs Engage | 0.6 | 3.99 |
| legs SpeakUp | 0.6 | 4.04 |
| base Competitive | 0.5 | 4.28 |
| legs OwnIt | 0.5 | 4.06 |
| base HandsOn | 0.4 | 4.38 |
| base Dependable | 0.4 | 4.55 |
| base Sheltered | 0.3 | 2.97 |

Lowest mean Motivation: base Sheltered 2.97, legs Engage 3.99, torso Quality 4.01, legs SpeakUp 4.04.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Quality + instinct SpeakUp | 2.8 | 7.3x | 86 | 3103 |
| values Quality + instinct Engage | 2.7 | 7.1x | 86 | 3200 |
| values Quality + upbringing Competitive | 2.4 | 6.3x | 73 | 3094 |
| values Quality + instinct OwnIt | 2.3 | 6.0x | 68 | 2979 |
| values Quality + upbringing Dependable | 1.7 | 4.6x | 59 | 3373 |
| values Quality + upbringing HandsOn | 1.7 | 4.6x | 58 | 3319 |
| values Quality + upbringing Sheltered | 1.4 | 3.7x | 47 | 3324 |
| values Quality + upbringing Bookish | 1.4 | 3.6x | 42 | 3052 |
| instinct OwnIt + upbringing Competitive | 0.8 | 2.1x | 25 | 3161 |
| instinct Engage + upbringing Competitive | 0.7 | 1.8x | 22 | 3236 |
| instinct SpeakUp + upbringing HandsOn | 0.6 | 1.7x | 20 | 3174 |
| values Quality + instinct Analyze | 0.6 | 1.6x | 21 | 3410 |

## 3. Optimal play only: optimal [work_cost_mult=1.2]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 74% **MISS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 85%
- All but 1 action cards played in every game (goal: 95% of games): 97% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Teach 93% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 2.6 **MISS**
- Workshop plays a game (goal: 1.0 to 2.5): 1.4 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 3.5 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.20 (0.08 a game, 0 quits in 94% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 11 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.061 **MISS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.01 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 13.1% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 71% **MISS**
- Community Need met (soft goal: 75% to 100%): 97% **PASS**
- Quality Need met (no goal): 96%
- Recognition Need met (soft goal: 75% to 95%): 86% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.51 | 3.12 | 3.23 | 3.08 | 2.94 | 3.02 | 2.88 |
| Mean | 4.59 | 4.51 | 3.98 | 4.21 | 4.03 | 3.97 | 4.06 | 4.01 |
| Median | 4.89 | 4.81 | 4.02 | 4.36 | 4.08 | 4.06 | 4.17 | 4.17 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.06 |

Quit causes per game (biggest Motivation loss in the week): a week without Work (Quality Need) 0.06, the weekly grind 0.01, Events 0.00, another character's Hero 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| THE DATE MOVES UP | say no | 0.160 | 0.064 | 40% |
| FALSE START | 2 | 0.161 | 0.011 | 7% |
| REORGANISED | 2 | 0.161 | 0.010 | 6% |
| BUDGET CUT | 2 | 0.165 | 0.010 | 6% |
| THE AUDIT | 2 | 0.151 | 0.008 | 5% |
| STATUS MEETING | 3 | 0.158 | 0.008 | 5% |
| PRIORITY CHANGES | 2 | 0.159 | 0.007 | 4% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.005 | 3% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.005 | 3% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.004 | 3% |
| THE BIKESHED | 1 | 0.158 | 0.004 | 3% |
| SCOPE CREEP | 3 | 0.179 | 0.004 | 2% |
| BURNOUT WARNING | 2 | 0.151 | 0.004 | 3% |
| SHAKY GROUND | 3 | 0.165 | 0.004 | 2% |
| THE TEAM SPLITS | 2 | 0.170 | 0.003 | 1% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.003 | 2% |
| MORE HANDS | 2 | 0.147 | 0.003 | 2% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.003 | 2% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.002 | 1% |
| THE DASHBOARD | 3 | 0.159 | 0.002 | 1% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.002 | 1% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| ALWAYS REACTING | 1 | 0.151 | 0.001 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.000 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| THE TEAM SPLITS | 0.001 | 0.01 | 10.5 |
| SHAKY GROUND | 0.001 | 0.03 | 2.9 |
| EVERYONE IS EQUAL | 0.001 | 0.01 | 20.0 |
| PRIORITY CHANGES | 0.001 | 0.01 | 3.4 |
| BUDGET CUT | 0.001 | 0.01 | 3.4 |
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.14 | 0.0 |
| THE DASHBOARD | 0.000 | 0.01 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | BUDGET CUT 0.001, THE AUDIT 0.000, EVERYONE IS EQUAL 0.000 |
| torso Hierarchy | SHAKY GROUND 0.003, EQUIPMENT OUTAGE 0.002, FALSE START 0.001 |
| torso Community | THE TEAM SPLITS 0.001, KNOWLEDGE HOARDING 0.001, EVERYONE IS EQUAL 0.000 |
| torso Quality | THE DATE MOVES UP 0.004, THE DASHBOARD 0.003, PRIORITY CHANGES 0.002 |
| torso Recognition | EVERYONE IS EQUAL 0.000, BUDGET CUT 0.000, THE WOLF 0.000 |
| legs OwnIt | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, THE TEAM SPLITS 0.001 |
| legs Analyze | SHAKY GROUND 0.001, PRIORITY CHANGES 0.001, EQUIPMENT OUTAGE 0.001 |
| legs Support | THE DATE MOVES UP 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| legs Engage | THE DATE MOVES UP 0.002, FALSE START 0.001, EQUIPMENT OUTAGE 0.001 |
| legs SpeakUp | SHAKY GROUND 0.001, THE DASHBOARD 0.001, THE WOLF 0.000 |
| base Bookish | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, PRIORITY CHANGES 0.001 |
| base HandsOn | SHAKY GROUND 0.002, THE TEAM SPLITS 0.001, THE DATE MOVES UP 0.001 |
| base Sheltered | THE DASHBOARD 0.001, PRIORITY CHANGES 0.001, THE AUDIT 0.001 |
| base Dependable | THE DASHBOARD 0.001, BUDGET CUT 0.001, EVERYTHING AT ONCE 0.001 |
| base Competitive | THE DATE MOVES UP 0.002, SHAKY GROUND 0.001, EQUIPMENT OUTAGE 0.001 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 20.55 |
| Celebrate | 100% | 3.46 |
| Engagement | 100% | 3.29 |
| Workshop | 99% | 1.41 |
| Learn | 99% | 1.91 |
| Teach | 93% | 1.57 |
| Reflect | 100% | 3.76 |
| Plan | 99% | 2.59 |
| Demo | 93% | 1.62 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 0.8 | 4.14 |
| legs Engage | 0.4 | 4.02 |
| base Competitive | 0.3 | 4.27 |
| legs SpeakUp | 0.3 | 4.11 |
| base HandsOn | 0.2 | 4.42 |
| legs OwnIt | 0.2 | 4.12 |
| base Sheltered | 0.2 | 2.98 |
| legs Analyze | 0.1 | 4.14 |

Lowest mean Motivation: base Sheltered 2.98, legs Engage 4.02, torso Hierarchy 4.07, legs SpeakUp 4.11.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Quality + instinct SpeakUp | 1.4 | 6.9x | 42 | 3093 |
| values Quality + instinct Engage | 1.3 | 6.6x | 42 | 3209 |
| values Quality + upbringing Competitive | 1.1 | 5.5x | 34 | 3096 |
| values Quality + instinct OwnIt | 0.9 | 4.4x | 26 | 2971 |
| values Quality + upbringing Sheltered | 0.8 | 4.1x | 27 | 3307 |
| values Quality + upbringing Bookish | 0.7 | 3.7x | 22 | 3038 |
| values Quality + upbringing HandsOn | 0.7 | 3.6x | 24 | 3321 |
| values Quality + upbringing Dependable | 0.6 | 3.0x | 20 | 3368 |
| instinct Engage + upbringing Competitive | 0.5 | 2.5x | 16 | 3220 |
| instinct OwnIt + upbringing Competitive | 0.4 | 2.1x | 13 | 3149 |
| instinct Engage + upbringing HandsOn | 0.4 | 2.1x | 12 | 2949 |
| instinct Engage + upbringing Sheltered | 0.4 | 1.8x | 11 | 3087 |

## 3. Optimal play only: optimal [work_cost_mult=1.3]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 73% **MISS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 84%
- All but 1 action cards played in every game (goal: 95% of games): 96% **PASS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Demo 90% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 2.6 **MISS**
- Workshop plays a game (goal: 1.0 to 2.5): 1.3 **PASS**
- Celebrate plays a game (goal: 4 or fewer): 3.4 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 98% **PASS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.16 (0.06 a game, 0 quits in 95% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 13 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.049 **PASS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.01 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 14.3% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 100% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 71% **MISS**
- Community Need met (soft goal: 75% to 100%): 97% **PASS**
- Quality Need met (no goal): 96%
- Recognition Need met (soft goal: 75% to 95%): 87% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.51 | 3.12 | 3.23 | 3.08 | 3.02 | 3.02 | 2.93 |
| Mean | 4.59 | 4.51 | 3.98 | 4.21 | 4.03 | 4.03 | 4.06 | 4.05 |
| Median | 4.89 | 4.81 | 4.02 | 4.35 | 4.08 | 4.12 | 4.16 | 4.21 |
| Quits | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.05 |

Quit causes per game (biggest Motivation loss in the week): a week without Work (Quality Need) 0.05, the weekly grind 0.01, Events 0.00, another character's Hero 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| THE DATE MOVES UP | say no | 0.160 | 0.064 | 40% |
| FALSE START | 2 | 0.161 | 0.011 | 7% |
| REORGANISED | 2 | 0.161 | 0.010 | 6% |
| BUDGET CUT | 2 | 0.165 | 0.010 | 6% |
| THE AUDIT | 2 | 0.151 | 0.008 | 5% |
| STATUS MEETING | 3 | 0.158 | 0.008 | 5% |
| PRIORITY CHANGES | 2 | 0.159 | 0.007 | 4% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.005 | 3% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.005 | 3% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.004 | 3% |
| THE BIKESHED | 1 | 0.158 | 0.004 | 3% |
| SCOPE CREEP | 3 | 0.179 | 0.004 | 2% |
| BURNOUT WARNING | 2 | 0.151 | 0.004 | 3% |
| SHAKY GROUND | 3 | 0.165 | 0.004 | 2% |
| THE TEAM SPLITS | 2 | 0.170 | 0.003 | 1% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.003 | 2% |
| MORE HANDS | 2 | 0.147 | 0.003 | 2% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.003 | 2% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.002 | 1% |
| THE DASHBOARD | 3 | 0.159 | 0.002 | 1% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.002 | 1% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| ALWAYS REACTING | 1 | 0.151 | 0.001 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.000 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| SHAKY GROUND | 0.001 | 0.04 | 2.5 |
| THE TEAM SPLITS | 0.001 | 0.01 | 4.3 |
| PRIORITY CHANGES | 0.001 | 0.02 | 2.9 |
| EVERYONE IS EQUAL | 0.001 | 0.01 | 10.0 |
| BUDGET CUT | 0.001 | 0.02 | 3.2 |
| THE WOLF | 0.000 | 0.49 | 0.0 |
| THE DATE MOVES UP | 0.000 | 0.14 | 0.0 |
| THE DASHBOARD | 0.000 | 0.01 | 0.0 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | BUDGET CUT 0.001, THE AUDIT 0.000, EVERYONE IS EQUAL 0.000 |
| torso Hierarchy | SHAKY GROUND 0.002, EQUIPMENT OUTAGE 0.002, FALSE START 0.001 |
| torso Community | THE TEAM SPLITS 0.001, KNOWLEDGE HOARDING 0.001, THE WOLF 0.000 |
| torso Quality | THE DATE MOVES UP 0.004, THE DASHBOARD 0.003, PRIORITY CHANGES 0.002 |
| torso Recognition | EVERYONE IS EQUAL 0.000, BUDGET CUT 0.000, THE WOLF 0.000 |
| legs OwnIt | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, PRIORITY CHANGES 0.001 |
| legs Analyze | PRIORITY CHANGES 0.001, EQUIPMENT OUTAGE 0.001, THE DATE MOVES UP 0.001 |
| legs Support | THE DATE MOVES UP 0.001, THE WOLF 0.000, THE TEAM SPLITS 0.000 |
| legs Engage | THE DATE MOVES UP 0.002, FALSE START 0.001, EQUIPMENT OUTAGE 0.001 |
| legs SpeakUp | SHAKY GROUND 0.001, THE DASHBOARD 0.001, THE WOLF 0.000 |
| base Bookish | THE DATE MOVES UP 0.002, THE DASHBOARD 0.001, PRIORITY CHANGES 0.001 |
| base HandsOn | THE TEAM SPLITS 0.001, SHAKY GROUND 0.001, PRIORITY CHANGES 0.001 |
| base Sheltered | THE DASHBOARD 0.001, PRIORITY CHANGES 0.001, THE DATE MOVES UP 0.001 |
| base Dependable | BUDGET CUT 0.001, THE DASHBOARD 0.001, EVERYTHING AT ONCE 0.001 |
| base Competitive | THE DATE MOVES UP 0.002, EQUIPMENT OUTAGE 0.001, THE AUDIT 0.001 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 20.76 |
| Celebrate | 100% | 3.45 |
| Engagement | 100% | 3.31 |
| Workshop | 99% | 1.33 |
| Learn | 100% | 1.91 |
| Teach | 92% | 1.57 |
| Reflect | 100% | 3.62 |
| Plan | 99% | 2.61 |
| Demo | 90% | 1.59 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| torso Quality | 0.6 | 4.17 |
| legs Engage | 0.3 | 4.03 |
| base Competitive | 0.2 | 4.28 |
| legs SpeakUp | 0.2 | 4.13 |
| base HandsOn | 0.2 | 4.43 |
| base Sheltered | 0.2 | 2.98 |
| legs OwnIt | 0.1 | 4.13 |
| legs Analyze | 0.1 | 4.14 |

Lowest mean Motivation: base Sheltered 2.98, legs Engage 4.03, torso Hierarchy 4.07, legs SpeakUp 4.13.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Quality + instinct Engage | 1.1 | 6.7x | 35 | 3209 |
| values Quality + instinct SpeakUp | 1.1 | 6.6x | 33 | 3094 |
| values Quality + upbringing Competitive | 1.0 | 6.0x | 30 | 3096 |
| values Quality + upbringing Sheltered | 0.8 | 4.8x | 26 | 3307 |
| values Quality + instinct OwnIt | 0.7 | 4.1x | 20 | 2971 |
| values Quality + upbringing Bookish | 0.6 | 3.8x | 19 | 3038 |
| values Quality + upbringing HandsOn | 0.5 | 3.3x | 18 | 3321 |
| instinct Engage + upbringing Competitive | 0.4 | 2.7x | 14 | 3221 |
| instinct Engage + upbringing Sheltered | 0.4 | 2.2x | 11 | 3086 |
| values Quality + instinct Analyze | 0.3 | 2.0x | 11 | 3397 |
| instinct OwnIt + upbringing Competitive | 0.3 | 2.0x | 10 | 3149 |
| instinct SpeakUp + upbringing Competitive | 0.3 | 1.9x | 9 | 2852 |

## 3. Optimal play only: optimal [work_cost_mult=1.5]

### Targets

- Reach UPPER threshold (goal: optimal 80% or more): 23% **MISS**
- Reach LOWER threshold (goal: balanced and invested 50% or more): 43%
- All but 1 action cards played in every game (goal: 95% of games): 79% **MISS**
- Every action card played in more than 50% of games (goal in optimal): fewest: Demo 52% **PASS**
- Plan plays a game (goal: 1.0 to 2.5): 4.3 **MISS**
- Workshop plays a game (goal: 1.0 to 2.5): 0.9 **MISS**
- Celebrate plays a game (goal: 4 or fewer): 3.5 **PASS**
- Team Reflexivity held at the end (goal: reachable in optimal, 50% or more): 26% **MISS**
- Psychological Safety held at the end (goal: reachable in optimal, 50% or more): 100% **PASS**
- Quits per 100 character-weeks (HARD goal in optimal: 5 or less): 0.35 (0.14 a game, 0 quits in 93% of games) **PASS**
- Habitus cards under 0.25 quit per 100 character-weeks (soft goal: none): 4 of 15 **MISS**
- Most Flex markers held at once (goal: 1 or fewer): 1 **PASS**
- Quality quits after a week without Work (goal in optimal: 0.05 or less): 0.026 **PASS**
- Onboarding plays a game (goal in optimal: 0.15 or less, follows the quits; not an action card): 0.08 **PASS**
- Games that end on 0 points (goal: optimal 2% or less, balanced and invested more than 1%): 56.5% **MISS**
- Autonomy Need met (soft goal: 75% to 100%): 98% **PASS**
- Hierarchy Need met (soft goal: 75% to 100%): 57% **MISS**
- Community Need met (soft goal: 75% to 100%): 95% **PASS**
- Quality Need met (no goal): 99%
- Recognition Need met (soft goal: 75% to 95%): 76% **PASS**

### Motivation and quits by week

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Lowest | 3.63 | 3.50 | 3.23 | 3.20 | 2.92 | 2.84 | 2.83 | 3.03 |
| Mean | 4.59 | 4.44 | 3.94 | 4.13 | 3.89 | 3.88 | 3.87 | 4.00 |
| Median | 4.89 | 4.67 | 3.93 | 4.23 | 3.90 | 3.96 | 3.92 | 4.09 |
| Quits | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.05 | 0.04 | 0.03 |

Quit causes per game (biggest Motivation loss in the week): the weekly grind 0.08, Events 0.03, a week without Work (Quality Need) 0.03, a track in the low band (instinct) 0.00, another character's Hero 0.00, spent it on Workshop, Overtime or Take One 0.00.

### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)

| Event | cost to cancel | drawn a game | landed a game | share that landed |
|---|---|---|---|---|
| THE WOLF | cannot | 0.170 | 0.170 | 100% |
| THE DATE MOVES UP | say no | 0.160 | 0.064 | 40% |
| FALSE START | 2 | 0.161 | 0.020 | 12% |
| BUDGET CUT | 2 | 0.165 | 0.015 | 9% |
| REORGANISED | 2 | 0.161 | 0.012 | 7% |
| STATUS MEETING | 3 | 0.158 | 0.011 | 7% |
| PRIORITY CHANGES | 2 | 0.159 | 0.011 | 7% |
| THE AUDIT | 2 | 0.151 | 0.010 | 7% |
| SCOPE CREEP | 3 | 0.179 | 0.009 | 5% |
| NEGATIVE FEEDBACK | 3 | 0.158 | 0.009 | 6% |
| KNOWLEDGE HOARDING | 2 | 0.173 | 0.009 | 5% |
| THE BIKESHED | 1 | 0.158 | 0.008 | 5% |
| SHAKY GROUND | 3 | 0.165 | 0.008 | 5% |
| REQUIREMENTS CHANGE | 2 | 0.165 | 0.008 | 5% |
| EVERYTHING AT ONCE | 3 | 0.162 | 0.007 | 5% |
| EQUIPMENT OUTAGE | 3 | 0.154 | 0.006 | 4% |
| THE DASHBOARD | 3 | 0.159 | 0.006 | 4% |
| BURNOUT WARNING | 2 | 0.151 | 0.006 | 4% |
| THE TEAM SPLITS | 2 | 0.170 | 0.005 | 3% |
| MORE HANDS | 2 | 0.147 | 0.005 | 3% |
| LEADS FROM BEHIND | 1 | 0.166 | 0.004 | 3% |
| OLD FOUNDATIONS | 2 | 0.155 | 0.004 | 3% |
| ALWAYS REACTING | 1 | 0.151 | 0.003 | 2% |
| A FLAT WEEK | 1 | 0.150 | 0.002 | 1% |
| EVERYONE IS EQUAL | 2 | 0.153 | 0.000 | 0% |

### Event cards behind quits

| Event | quits a game | lands a game | quits per 100 landings |
|---|---|---|---|
| BUDGET CUT | 0.009 | 0.06 | 16.2 |
| THE AUDIT | 0.007 | 0.06 | 11.9 |
| EVERYONE IS EQUAL | 0.006 | 0.05 | 13.0 |
| THE TEAM SPLITS | 0.003 | 0.03 | 9.4 |
| SHAKY GROUND | 0.002 | 0.10 | 2.0 |
| PRIORITY CHANGES | 0.002 | 0.06 | 3.6 |
| EVERYTHING AT ONCE | 0.001 | 0.10 | 1.0 |
| STATUS MEETING | 0.001 | 0.08 | 0.6 |

### Event cards behind each habitus card's quits (the quit week and the week before)

| Habitus card | Event cards (quits a game) |
|---|---|
| torso Autonomy | THE AUDIT 0.007, EVERYONE IS EQUAL 0.005, BUDGET CUT 0.004 |
| torso Hierarchy | EVERYTHING AT ONCE 0.009, SHAKY GROUND 0.005, EQUIPMENT OUTAGE 0.005 |
| torso Community | THE AUDIT 0.004, EVERYONE IS EQUAL 0.003, BUDGET CUT 0.003 |
| torso Quality | THE DASHBOARD 0.019, PRIORITY CHANGES 0.004, SCOPE CREEP 0.004 |
| torso Recognition | THE AUDIT 0.003, BUDGET CUT 0.003, EVERYONE IS EQUAL 0.002 |
| legs OwnIt | THE DASHBOARD 0.005, THE AUDIT 0.003, EVERYONE IS EQUAL 0.003 |
| legs Analyze | THE AUDIT 0.004, EVERYONE IS EQUAL 0.003, THE DASHBOARD 0.003 |
| legs Support | THE DASHBOARD 0.003, THE AUDIT 0.003, BUDGET CUT 0.002 |
| legs Engage | EVERYONE IS EQUAL 0.006, EVERYTHING AT ONCE 0.005, THE AUDIT 0.005 |
| legs SpeakUp | THE DASHBOARD 0.004, THE AUDIT 0.002, BUDGET CUT 0.001 |
| base Bookish | THE DASHBOARD 0.005, THE AUDIT 0.002, EVERYONE IS EQUAL 0.002 |
| base HandsOn | EVERYTHING AT ONCE 0.004, THE DASHBOARD 0.004, EVERYONE IS EQUAL 0.003 |
| base Sheltered | THE DASHBOARD 0.004, THE AUDIT 0.003, EVERYONE IS EQUAL 0.003 |
| base Dependable | BUDGET CUT 0.004, THE DASHBOARD 0.004, THE AUDIT 0.003 |
| base Competitive | THE AUDIT 0.005, EVERYONE IS EQUAL 0.003, THE DASHBOARD 0.002 |

### Cards (share of games playing each, plays a game)

| Card | share | per game |
|---|---|---|
| Work | 100% | 21.57 |
| Celebrate | 100% | 3.47 |
| Engagement | 100% | 3.38 |
| Workshop | 83% | 0.88 |
| Learn | 79% | 1.62 |
| Teach | 90% | 1.04 |
| Reflect | 99% | 2.29 |
| Plan | 99% | 4.33 |
| Demo | 52% | 1.20 |

### Habitus parts by quits (per 100 character-weeks)

| Part | quits/100 | mean Motivation |
|---|---|---|
| legs Engage | 0.6 | 3.97 |
| torso Quality | 0.5 | 4.18 |
| base HandsOn | 0.5 | 4.32 |
| legs Analyze | 0.5 | 4.05 |
| torso Hierarchy | 0.5 | 3.92 |
| base Competitive | 0.4 | 4.19 |
| base Dependable | 0.3 | 4.49 |
| torso Autonomy | 0.3 | 4.18 |

Lowest mean Motivation: base Sheltered 2.97, torso Hierarchy 3.92, legs Engage 3.97, legs Analyze 4.05.

### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)

| Pair | quits/100 | vs all | quits | character-weeks |
|---|---|---|---|---|
| values Hierarchy + instinct Engage | 1.1 | 3.2x | 37 | 3239 |
| values Hierarchy + upbringing HandsOn | 1.0 | 2.8x | 29 | 2995 |
| instinct Engage + upbringing HandsOn | 1.0 | 2.7x | 28 | 2911 |
| instinct Engage + upbringing Dependable | 0.8 | 2.3x | 25 | 3074 |
| values Quality + instinct Engage | 0.8 | 2.2x | 25 | 3180 |
| instinct Engage + upbringing Competitive | 0.8 | 2.1x | 24 | 3185 |
| values Quality + upbringing Bookish | 0.7 | 2.1x | 22 | 3028 |
| instinct Analyze + upbringing HandsOn | 0.7 | 2.0x | 23 | 3213 |
| values Community + instinct Analyze | 0.7 | 1.9x | 21 | 3107 |
| values Hierarchy + instinct Analyze | 0.7 | 1.9x | 20 | 3064 |
| values Quality + instinct OwnIt | 0.6 | 1.6x | 17 | 2956 |
| values Hierarchy + upbringing Competitive | 0.6 | 1.6x | 18 | 3193 |
