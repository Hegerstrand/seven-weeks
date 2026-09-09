# Addendum: Feature Quality & Uncertainty

Rules text below is extracted verbatim (or lightly adapted) from `rules/rulebook.md` \u00a710,
the Activity card table, and the Need table, as they stood before the 2026-09-09 extraction.
Section numbers (\u00a7) refer to the base rulebook's numbering at the time of extraction.

## Feature attributes (\u00a710)
Each feature also carries a hidden **Quality** attribute, alongside Work Cost, Complexity, and
Dependencies.

**Unclear requirements block Plan.** A feature flagged Unclear (its Uncertainty made real -
e.g. by the UNCLEAR REQUIREMENT event) can still receive Work, but any Plan spent on it does
nothing until an Align or Demo resolves the ambiguity. This forces an order: Unclear \u2192
Align/Demo \u2192 Plan \u2192 Work benefits. Skipping straight to Plan on an unclear feature is a
wasted day that looks productive - the same trap a real project falls into.

**Quality is hidden per feature**, tracked face-down, starting at Medium. A Demo can confirm
or raise it; skipping Demo/Reflect on a feature, or a bad NEGATIVE FEEDBACK, can drop it to
Low. A character whose Torso is **Quality** gets a habitus pair here:
> **Strength:** may block the team from placing a Low-Quality feature on the Tower until it's
> reworked - protects long-term Resilience.
> **Tendency:** doing this without the team's agreement costs **-1 Trust** - overriding the
> group's urgency alone reads as obstruction, not care.

## Activity card effects
With this pack in play, restore these printed effects in place of the base game's simplified
versions:

| Card | Base game (without this pack) | With this pack |
|---|---|---|
| **Plan** | Choose a feature with clear requirements: every Work card played on it this week produces +1 extra (Low: no bonus). If High complexity, the bonus also applies next week. | Same, plus: **also reveal its hidden Quality. No effect on a feature flagged Unclear.** |
| **Align** | +1 Adaptability, unconditionally. | +1 Adaptability, **but only if no feature is Unclear - otherwise it clears the flag instead.** |
| **Meet** (Working Meeting) | +1 Adaptability, +1 Trust. | +1 Adaptability, +1 Trust, **and clears one Unclear.** |
| **Demo** | Needs Capital \u2265 the team average. Presenter +1 Capital, and the feature ignores the next NEGATIVE FEEDBACK. *(Unconditional success - the Capital gate and standing-concentration mechanic stayed in the base game; only the hidden-Quality roll was removed.)* | Same gate, but reveal the target feature's Quality first. **Medium or High:** as base game. **Low:** the feature loses 1 Work and the presenter takes -1 Capital instead. Either way, clears Unclear. |

## Need table (Quality Torso)
| Torso (= Need) | Base game | With this pack |
|---|---|---|
| Quality | The team spent an Align. | The team spent an Align, **or a feature they're on moved from Unclear to Clear.** |

## Vindication (Habits table)
| Torso | Base game | With this pack |
|---|---|---|
| Quality | Reflect. | Reflect, **and refusing to place a Low-Quality feature.** |

## Standing & Capital (§5.1/§14)
| Row | Base game | With this pack |
|---|---|---|
| Standing-conversion trigger | You led a Demo. | Your Demo revealed Medium or High Quality. |
| Losing Capital | *(no Demo-failure line - Demo cannot fail without hidden Quality)* | Your Demo revealed Low Quality: -1. |
| Habitus strength example (\u00a714) | *(drop the Low-Quality example)* | "...blocking a Low-Quality feature with the team's agreement..." |

## Event cards
These two Event cards only make sense with this pack in play - pull them from the base-game
Event deck (14 base Events instead of the printed 16, until this pack restocks them):

> **SURPRISE AUDIT** - reveal Quality on every feature that hasn't been revealed yet, and
> clear Unclear wherever it's flagged. Any feature revealed **Low** loses **1 Work** (rework),
> adjusted by Complexity as usual. Nobody presented this, so no Capital changes hands
> either way - an audit makes things visible, it doesn't make anyone look good. If the team
> already has **Shared Repertoire**: ignore this card entirely - a team with real routines has
> nothing to hide.

> **UNCLEAR REQUIREMENT** - pick a feature; flag it **Unclear**. Its true Work Cost is +1
> higher than shown, and Plan does nothing on it, until the team spends an Align or Demo on
> it.

## Components affected
See the pack [README.md](../README.md)'s "Components this pack touches" section for the full
list of cards/boards that need re-cutting (not yet done - text-only extraction so far).
