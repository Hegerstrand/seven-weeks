# Component specs

Three consolidated Markdown files describe every print sheet in `game/components/` -
grouping, background colours, text, and the illustration - used to drive SVG edits:

- **[cards.md](./cards.md)** - every card sheet (Activity, Event, Habitus parts, NEED/HERO
  tiles, Project).
- **[boards.md](./boards.md)** - every board and table-insert sheet (Person/Specimen board,
  Standing strip, THE DEVELOPMENT, THE PROJECT, THE TEAM, THE ZONE, SHIT HAPPENS).
- **[leaflet-how-to-play.md](./leaflet-how-to-play.md)** - the printable how-to-play leaflet
  (plain Markdown, no matching SVG) - read this one last.

See the
[board-game-component-specs skill](../../../.github/skills/board-game-component-specs/SKILL.md)
for the full workflow and the exact template each section follows.

**Workflow:** edit the relevant section in `cards.md`/`boards.md` → tell the agent to update
the matching SVG → push.

`_check-table-layout.svg` is a dev check (leading underscore), not a print sheet, and has no
spec.

Every filename that used to hold one sheet's spec (`cards-activity.md`, `cards-event.md`,
`cards-habitus-parts-44x36mm-A4-portrait.md`, `cards-need-hero-44x36mm-A4-portrait.md`,
`cards-project-63x88mm-A4-portrait.md`, `board-person-170x141mm-A4-portrait.md`,
`standing-281x34mm-A4-landscape.md`, `the-development-127x104mm-A4-landscape.md`,
`the-project.md`, `the-team.md`, `the-zone.md`, `shit-happens.md`) is now a short redirect
stub with its old content commented out below the notice - safe to delete once you've
confirmed `cards.md`/`boards.md` cover everything.

## Index

| File | Covers |
|---|---|
| [cards.md](./cards.md) | `../cards-activity-63x88mm-A4-portrait.svg`, `../cards-activity-5b-63x88mm-A4-portrait.svg`, `../cards-event-01-09-63x88mm-A4-portrait.svg`, `../cards-event-10-18-63x88mm-A4-portrait.svg`, `../cards-event-19-21-63x88mm-A4-portrait.svg`, `../cards-habitus-parts-01-15-44x36mm-A4-landscape.svg`, `../cards-habitus-parts-16-25-44x36mm-A4-landscape.svg`, `../cards-need-hero-44x36mm-A4-landscape.svg`, `../cards-project-63x88mm-A4-portrait.svg` |
| [boards.md](./boards.md) | `../board-person-170x141mm-A4-portrait.svg`, `../standing-281x34mm-A4-landscape.svg`, `../the-development-127x104mm-A4-landscape.svg`, `../the-project-FRONT-A3-landscape.svg` + BACK, `../the-team-FRONT-A4-landscape.svg` + BACK, `../the-zone-FRONT-A4-landscape.svg` + BACK, `../shit-happens-FRONT-A4-portrait.svg` + BACK |
| [leaflet-how-to-play.md](./leaflet-how-to-play.md) | plain printable Markdown, no matching SVG |

## Template (copy for a new SVG)

```markdown
# <Title from the SVG's <title>>

Source: `../<filename>.svg`
Page: <width>x<height>mm <orientation>

## Grouping

| Group id | Contents | Background (hex) |
|---|---|---|
| ... | ... | ... |

## Text

| Text | Class / font | Size | Colour | Background chip (hex) |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Illustration

Prose: shapes, paint order (top to bottom = back to front), orientation, sizes not already
covered by the piece-size canon.

## Layout diagram

\`\`\`mermaid
graph TD
  A["..."] --> B["..."]
\`\`\`
```
