# Extension: Performance Review

**Requires:** the base game. **Adds back:** the individualized **Performance Review** Capital
penalty, and the **Collective Bargaining** alternate use of the Authorized Voice Habit that
shields a teammate from it. Cut from the base game on 2026-09-09 as part of tuning down how
many free/near-free ways a team has to shrug off Events (see the balance discussion in
`game/playtests/README.md` and `rules/rulebook.md`'s v0.21/v0.22 change notes).

## What this pack restores
- **Losing Capital \u2192 Performance Review:** a named character loses **1 Capital**, no weekly
  cap. If Trust \u2265 4, the team may spend a Coordinate to take this as **-1 Trust, shared**,
  instead of -1 Capital for the named character alone.
- **Authorized Voice** gains its second use: instead of cancelling an Event outright, the team
  may spend it as **Collective Bargaining** - convert a named character's Performance Review
  into a shared -1 Trust. Base game Authorized Voice only cancels an Event; this pack restores
  the choice between the two.
- The **"Fired"** leaving-the-team trigger (\u00a713) can cite a Performance Review event as its
  example trigger again once this pack defines one.

## Why this was cut (not just "too complicated")
Authorized Voice already gives a team a free, no-cost escape valve once a week (on top of a
growing Adaptability budget and Habit discounts - see the balance discussion this extraction
came out of). Giving that same free action **two** different uses to choose between adds a
decision that doesn't change the underlying problem (the team still has one fewer thing to
worry about that week) - it's complexity without a meaningfully different choice, the kind
Eurogame design principles say to cut. The base game now trusts Authorized Voice to just do
one thing: cancel an Event.

## Components affected
No physical card currently prints "PERFORMANCE REVIEW" as its own title (it was a named
mechanic in rulebook prose, not yet a cut card) - restoring this pack means designing that
event card, or wiring the mechanic into an existing one. Not yet done.

- `board-3b-standing` - the FRONT face's Authorized Voice text ("...or Collective Bargaining -
  shield a teammate's Performance Review instead") is simplified in the base-game sheet; this
  pack's version should restore the second line.
