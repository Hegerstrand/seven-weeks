# Extensions

Optional add-on modules for the base game. One subfolder per pack, each with its own README.
Two tracks, set by where the pack came from. Every pack README opens with a **Track:** line.

## Track A - extracted
Cut **out of** the base game after a playtest finding of "too complicated". The base rulebook
was stripped and carries one signpost. Needs a dated playtest entry (the evidence gate).

| Pack | Restores | Status |
|---|---|---|
| [feature-quality-uncertainty](feature-quality-uncertainty/README.md) | Hidden feature Quality, the Unclear flag, full Demo/Align, the Quality Torso's habitus pair | Rules text extracted (v0.21); components not re-cut |
| [performance-review](performance-review/README.md) | Individual Performance Review Capital penalty, Collective Bargaining | Extracted (2026-09-09) |
| [team-reflexivity](team-reflexivity/README.md) | Old pool-flip Team Reflexivity | History only; a new form is in base §18 |

## Track B - additive
New content **added on top of** the base game. The base rulebook is not stripped, and
needs no more than one signpost line when a rule is chosen. No evidence gate: each pack states a
hypothesis and the test that would confirm it. Status runs **idea -> drafted -> played**.

| Pack | Adds | Status |
|---|---|---|
| [saboteur](saboteur/README.md) | A character at 0 Motivation turns Saboteur instead of quitting | Drafted 2026-10-08, never played |
| [the-wolf](the-wolf/README.md) | THE WOLF returns, and stepping up costs more each time | Drafted 2026-10-09, never played |
| [the-sixth-seat](the-sixth-seat/README.md) | A sixth player as Estimator (forecast before week 1) and reserve, with alternatives to the Onboarding card | Ideas only, 2026-10-17 |

Rules for both tracks are in the `board-game-extension-packs` skill.

## Simulating a pack
`scripts/balance_sim.py` can run the base game with or without each pack. Every pack is one off-by-default
switch on `Rules`, so a plain run is still the base game.

```
python scripts/balance_sim.py --ext saboteur,wolf                 # these packs on
python scripts/balance_sim.py --compare all --reuse-optimal       # base, each pack alone, all together; policy held fixed
python scripts/balance_sim.py --ext sixth-seat --set sixth_replace=contractor
python scripts/balance_sim.py --ext sixth-seat --sweep sixth_replace=onboarding,bench,alumnus,contractor,short
```

Runs with a pack on write to `balance_sim_ext_results*` and `plots_ext/`, and never overwrite the saved optimal strategy.

| Pack | Switch | Modelled | Not modelled |
|---|---|---|---|
| the-wolf | `ext_wolf`, `wolf_escalate` | Shuffled back, escalating step-up cost, discarded when nobody has Capital | - |
| saboteur | `ext_saboteur`, `saboteur_*` | Turning, three hostile acts, win-back by Engagement + Celebrate + Trust, score and thresholds | Hero win-back; a Saboteur's Capital in Standing; the Saboteur's own win condition |
| the-sixth-seat | `ext_sixth_seat`, `sixth_*` | E1 forecast and Trust penalty, R1 to R5, handover, a sixth character joining in week n | The Estimator's own Capital; E2, E3 (no scoring to simulate) |
| feature-quality-uncertainty | `ext_feature_quality`, `fq_*` | Unclear flag and Plan lock, UNCLEAR REQUIREMENT, SURPRISE AUDIT, Quality-revealing Demo | The Quality Torso's block and Trust tendency; how Quality falls is a guess |
| performance-review | - | Refused: the pack has no card that takes Capital away yet | Everything |

Every number a pack leaves open is a guess behind a `Rules` field. The addenda of feature-quality-uncertainty and
saboteur predate rulebook v0.36 in places (card names, the quit penalty), so read the model's docstring first.
