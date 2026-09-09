# Extension: Feature Quality & Uncertainty

**Requires:** the base game. **Adds back:** the Project feature system's hidden **Quality**
(Low/Medium/High) attribute and the **Unclear** flag, both cut from the base game after the
2026-09-09 playtest finding that the full feature system was too complicated (see
`game/playtests/README.md`).

## What this pack restores
- Every feature also carries a **hidden Quality** (Low/Medium/High, starts Medium, tracked
  face-down) alongside its Work Cost/Complexity/Dependencies.
- Features can be flagged **Unclear**; an Unclear feature can still take Work, but Plan spent
  on it is wasted until an Align/Demo/Working Meeting clears the flag.
- **Demo** becomes a full card again: it reveals a feature's Quality and pays off or punishes
  the team depending on what's revealed.
- **Align** regains its conditional effect (clear Unclear *or* +1 Adaptability, instead of
  always +1 Adaptability).
- **Quality** (the Torso) regains its full habitus pair: blocking the team from placing a
  Low-Quality feature without agreement.

See [rules/addendum.md](rules/addendum.md) for the exact rules text, verbatim from the
rulebook section it was cut from.

## Components this pack touches
- `cards-activity` / `cards-activity-5b` - the Align and Demo cards need their Unclear/Quality
  clauses restored (base-game versions of these two cards currently print the simplified
  effect - see addendum for the printed difference). Demo stays in the base deck either way.
- `cards-event-01-09` / `cards-event-10-18` - the **UNCLEAR REQUIREMENT** and **SURPRISE
  AUDIT** event cards only make sense with this pack in play; base-game games should pull them
  from the Event deck.
- `cards-habitus-parts` - one printed strength/tendency references Work-on-Unclear; only
  applies with this pack.
- `cards-need-hero` - the Quality-Torso Need tile's "a feature cleared Unclear" clause only
  applies with this pack (base-game tile prints the simplified condition - see addendum).
- `board-1-FRONT` - the Unclear flag seat and Quality chip seat printed next to each feature
  slot are only used with this pack in play; without it, leave those seats empty.
- `board-3b-standing` - drop the "ALSO NOW: A FACE-DOWN QUALITY CHIP GOES ON EACH FEATURE"
  line from the base-game sheet; it belongs here instead.

None of the above SVG files have been re-cut yet - this pack currently only contains the
rules text. Re-cutting the physical components (marking them extension-only vs. producing
simplified base-game replacements, per the `board-game-extension-packs` skill's "skip vs.
mark" choice) is tracked as open work below.

## Open design questions this extraction raised
Removing Unclear/Quality left Align's conditional effect with nothing to be conditional on,
which needed a provisional redesign rather than a silent gap. **Flagging this for
confirmation:**

1. **Align (base game).** Its only base-game effect was "+1 Adaptability, but only if no
   feature is Unclear - otherwise clears the flag." With Unclear gone, it's been simplified to
   **"+1 Adaptability, unconditionally"** (its own stated fallback). Low-risk, matches what
   already happened whenever no feature was flagged.
2. **Demo (base game) stays in the base game.** Its Capital-average gate and the
   standing-concentration mechanic it drives (§5.1's "Hero-Team path") are independent of
   feature Quality and were not touched. Only its **outcome** was Quality-dependent, so the
   base game now reads: **"Needs Capital ≥ the team average. Presenter +1 Capital, and the
   feature ignores the next NEGATIVE FEEDBACK."** - i.e. every base-game Demo is an
   unconditional success (there's no hidden Quality roll left to fail against). This pack
   restores the Medium/High-success-vs-Low-failure branch and the Unclear-clearing clause.
3. **The Quality Torso's habitus pair.** Its Strength ("may block a Low-Quality feature")
   and Tendency (-1 Trust for doing so without agreement) are entirely about feature Quality.
   Its Need condition ("spent an Align, or a feature moved Unclear→Clear") and its Vindication
   trigger ("Reflect, and refusing to place a Low-Quality feature") are too. Provisionally:
   - Need simplified to "the team spent an Align" (Align still exists in the base game).
   - The Strength/Tendency pair and Vindication trigger are left **without a base-game
     replacement** - rulebook.md now says plainly that Quality's full habitus pair requires
     this extension. **This is a real gap in the base game's habitus balance (one Torso out
     of five has no unique ability without the pack) and needs a design decision**, not an
     invented placeholder.
