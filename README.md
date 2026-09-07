# Game

## Folder structure

- `docs/` - design docs: concept, habitus model, playability assessment, design guide.
- `rules/` - the rulebook as it grows (draft → playtested → polished), plus the cut-down
  `rulebook-lite.md` used for the first playtest.
- `components/` - physical component specs: cards, boards, tokens, box.
- `components/3d-models/` - 3D-printable files (STL/3MF/STEP) and print notes (material, supports, orientation).
- `playtests/` - dated playtest logs: what we tested, what worked, what changed.

## Working agent & skills

Use the **Board Game Designer** agent (`.github/agents/board-game-designer.agent.md`) for
this project. It draws on four skills:

- **board-game-mechanics** - concept, mechanics, rulebook, meaningful-choice design.
- **board-game-3d-printing** - how to design and spec 3D-printed components.
- **board-game-playtesting** - learning theory (situated learning, zone of proximal
  development, Bourdieu's habitus and field) applied to onboarding and playtests.
- **board-game-team-dynamics** - running the design team itself well (Tuckman's stages).

## Status

**Concept locked: v0.1 - "High-Performance Team."** A cooperative strategy game where a
4-6 person team has 35 working days to deliver a project, while becoming (or failing to
become) a real high-performing team. See [docs/concept.md](./docs/concept.md) for the pitch
and [docs/habitus-model.md](./docs/habitus-model.md) for how characters get built.

**Rulebook is at v0.2: the turn is the week.** Each character allocates 5 person-days at once,
*before* that week's Events are drawn - 7 turns, not 35, and ~85 minutes. **All five blocking
defects** in the [playability assessment](./docs/playability-assessment.md) are now closed;
the open items are S3 (Base and Legs are still mechanically inert) and S4 (no defence against
the alpha-player problem).

The design targets an explicit skill curve - **~5% random, ~50% competent, ~95% perfect**
(see [docs/concept.md](./docs/concept.md)) - and currently models to it.

**Art direction is locked: "The Field Study"** - the game presented as a sociologist's field
study of one software team. Corporate objects rendered in scholarly materials. See
[docs/design-guide.md](./docs/design-guide.md). Nothing gets designed or printed until the
mechanics are proven at a table.

**Not playtested yet, and every number in it is derived rather than observed.** First session
runs the cut-down [rules/rulebook-lite.md](./rules/rulebook-lite.md) - 15 days, 5 activities,
all paper, ~75 minutes - which stays deliberately *daily*, so the first test measures the
activity economy without also testing a new turn structure. Nothing gets 3D printed until the
habitus options freeze (assessment Stage 10).
