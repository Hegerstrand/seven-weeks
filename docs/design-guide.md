# Design Guide - High-Performance Team

Status: **v1.0 - art direction locked, execution not started.**

This governs how the game *looks, feels and speaks*. For what the components physically are,
see [../components/README.md](../components/README.md); for print specs, see
[../components/3d-models/](../components/3d-models/).

---

## 1. The concept: **The Field Study**

> The game is presented as a sociologist's field study of one software team over seven weeks.

Not a corporate training kit. Not a satire of office life. **A researcher's field materials** - specimen cards, observation logs, a wall chart, annotated in the margins by someone who is
genuinely fond of the people being studied and quietly amused by their rituals.

This framing isn't decoration. It's the honest description of what the game already is:
Bourdieu did fieldwork, Wenger studied communities of practice, and this game is an observation
of a team under pressure. Everything below follows from taking that literally.

> **It also solves a real problem.** The assessment flagged (M4) that tracks named
> *Trust / Capability / Shared Practice* and an achievement titled *Psychological Safety* sit
> dangerously close to an HR deck - which the concept explicitly names as a non-goal. Under the
> Field Study framing, that vocabulary stops reading as corporate and starts reading as
> **a researcher's terminology**. Same words, opposite feeling. The framing is the fix.

---

## 2. The core tension

Every single component holds two things at once:

| The corporate object | Rendered in scholarly material |
|---|---|
| Status report | …typed on foxed paper, annotated in pencil |
| Sprint board | …a linen wall chart with brass pins |
| Org chart | …a taxonomic diagram, like a family of beetles |
| KPI dashboard | …a hand-ruled ledger |
| Employee badge | …a museum specimen label |
| Gantt chart | …a botanical growth study |

**If a component reads as purely corporate, it's wrong. If it reads as purely academic, it's
also wrong.** The friction between the two *is* the aesthetic.

---

## 3. Typography - three voices

This is the most important system in the guide. The game has three speakers, and they never
share a typeface.

| Voice | Typeface | Used for |
|---|---|---|
| **The scholar** | **EB Garamond** (serif, old-style) | Rules text, explanation, theory, anything the game says in its own voice. Warm, considered, unhurried. |
| **The corporation** | **IBM Plex Mono** | Feature names, Event card headers, status reports, quoted management speech, numbers on tracks. Institutional, a little cold, faintly dated. |
| **The researcher's margin** | **Caveat** (or a real scanned hand) | Marginalia, wry observations, the single line on a card that tells you what just *actually* happened. |

Both alternates are open-licence: **Crimson Pro** for the serif, **Courier Prime** for the
mono. Never more than these three families on one component.

**The rule that makes it sing:** the scholar's voice explains, the corporation's voice
*intrudes*, and the margin's voice sees through the intrusion. That's the whole game in a
typographic system.

### Worked example - one Event card

```
┌─────────────────────────────────────────┐
│  ANOTHER STATUS MEETING          [MGMT] │  ← IBM Plex Mono, small caps, tracked out
│                                         │
│  "Just a quick 30-minute check-in."     │  ← Plex Mono, italic - management speaking
│                                         │
│  Costs every character their            │  ← EB Garamond - the rule
│  person-day. Everyone: −1 Motivation.   │
│  Head = Withdraw: −2 instead.           │
│                                         │
│    the meeting is not about             │  ← Caveat, pencil grey, slightly askew
│    information. it is about being       │
│    seen to be informed.                 │
└─────────────────────────────────────────┘
```

---

## 4. Palette

Two palettes, and **which one a component uses is meaningful, not decorative.**

### The team's world - earthy, natural pigments
Everything the team owns and controls.

| Name | Hex | Use |
|---|---|---|
| Field Paper | `#E8DCC4` | Primary card and board stock tone |
| Bone | `#F2EDE0` | Highlights, the habitus figures |
| Oak Gall Ink | `#2A2620` | All body text - a brown-black, never pure black |
| Herbarium Green | `#5A6650` | Capability, growth, learning |
| Oxblood | `#7B3F35` | Trust, the box cloth, binding accents |
| Ochre | `#C08A3E` | Motivation, warmth, the human element |
| Slate | `#4A5259` | Shared Practice, structure, rules furniture |
| Timber | `#8B6F47` / `#5C4830` (finished) / `#EFE4D3` (card tint) | Work - the feature Work-counter pips (darker shade = reached Work Cost) and the highlight box on the Work Activity card |

### The intrusion - corporate accents
**Used only for things that happen *to* the team.** Events, management demands, rework,
deadlines. Never for the team's own tracks, characters, or Habits.

| Name | Hex | Use |
|---|---|---|
| Highlighter | `#E8C547` | Management-category Events. The colour of someone else's priority. |
| Redline | `#B03A2E` | Rework, defects, corrections, "as per my last email" |
| Ledger Blue | `#3B5B7A` | Customer-category Events, external dependencies |

> **The colour rule:** earthy = the team. Accent = the world acting on the team. A player
> should be able to feel, without being told, that the yellow things are not on their side.

No pure black (`#000`), no pure white (`#FFF`), no gradients, no drop shadows, no gloss.

---

## 5. Materials & finish

**Uncoated, always.** Gloss is the single thing that would destroy this aesthetic fastest.

| Component | Direction |
|---|---|
| Cards | 300gsm uncoated with visible tooth. Linen finish acceptable, gloss never. Slightly warm stock, not bright white. |
| Boards | Greyboard wrapped in uncoated paper, with the **grey board edge left visible** - like a bound monograph, not a game board. |
| Feature blocks | **Unfinished or oiled hardwood.** Not painted, not plastic. The tower should smell faintly of wood. |
| Tokens | Wood or thick chipboard. Motivation tokens ideally wooden discs, warm to hold. |
| Box | Cloth-texture wrap in Oxblood, **foil-blocked title** in the mono face. It should shelve like an academic monograph and look faintly out of place in a game collection. |
| Rulebook | Sewn or saddle-stitched, generous margins for the marginalia voice, no glossy cover. |

### The habitus figures
**Printed in a single bone-coloured material. No painting, no colour-coding.**

They should read as **plaster study models or natural-history specimens**, not as toys or
wargaming miniatures. Differentiation between characters comes entirely from *shape* - never
from colour. Shape includes **pose and sculpted clothing/props**, not just outline - a Base
can plant its feet differently, a Torso can wear a different collar or fold its sculpted arms
differently, an Item can be held at a different angle. **Not a Lego look** - avoid interchangeable
blocky proportions, peg hands, or the iconic minifig silhouette - but it can be **just as
simple**: plain surfaces, minimal detail, no fine ornamentation.

This is thematically exact: habitus is structure, not decoration. It's also dramatically
cheaper and removes the "my mini isn't painted" problem entirely. Print specs stay with the
`board-game-3d-printing` skill; this guide only fixes the look.

---

## 6. Iconography

**Woodcut and scientific-plate line art.** Think 19th-century engraving, hand-inked, slightly
irregular. Never flat vector, never rounded-corner app icons, never isometric.

Reference points: botanical plates, anatomical diagrams, patent drawings, ordnance survey
symbols, herbarium labels.

> **Every icon is paired with a word. No exceptions.**
>
> This is not a style preference. Icon-only systems assume board-game literacy - a form of
> cultural capital that hobbyists have and newcomers don't - and quietly reproduce the
> insider/outsider split the game is *about*. A game built on Bourdieu that alienates
> outsiders through its iconography would be embarrassing. Plain language over hobby jargon,
> everywhere.

---

## 7. Component direction

**Character card** - a **specimen label**. Ruled fields, a printed catalogue number, space to
write in pencil. The five habitus parts listed as a taxonomy (Base / Legs / Torso / Head /
Item), not as a stat block. It should look like something pinned in a drawer.

**Team State board** - a **hand-ruled ledger**. Four tracks as columns in an accounts book,
numbers in the mono face, headers in the serif. Trust/Capability/Shared Practice/Adaptability
labelled as if they were measured variables in a study.

**Weekly allocation board** - the **corporate object at its most corporate**: a timesheet.
Five slots per character, ruled and boxed, the one component that looks genuinely bureaucratic.
This is deliberate - it's where players commit their week before reality lands on it (§6.1),
and it should feel like filing a plan you'll regret.

**Feature Tower** - bare wood, no printing. It's the only component with no voice at all,
because it's the only thing that's simply, physically true: this much got built.

**Event cards** - corporate accent colours, mono headers, category tag top-right. The
marginalia line is mandatory on every card; it's what stops the deck reading as a list of
punishments.

**Habit coins** - double-sided, read as **museum accession tokens or wax seals**, not game
chips. The unacquired face is plain and institutional - track name, threshold, mono. The
acquired face is the reward: the Habit named in the serif voice, with a small engraved mark.
The flip should feel like a coin being turned in the hand, because that gesture *is* the rule
(§18). This is also the fix for M4: a habit acquired by a team is a researcher's observation,
not an HR badge.

---

## 8. Voice & tone

The professor's voice: **warm, precise, faintly amused, never cynical.**

They have watched a hundred teams do this. They are not surprised by anything. They are not
sneering - they *like* these people, and they think the rituals are worth understanding rather
than mocking.

| Do | Don't |
|---|---|
| "The meeting is not about information; it is about being seen to be informed." | "LOL another pointless meeting 🙄" |
| "Teaching someone converts what you know into what you're owed." | "Sharing knowledge is a best practice!" |
| "The team was efficient. It was efficient at the wrong thing." | "Oops, you got too rigid!" |
| Observe, then let the player draw the conclusion. | State the lesson. |

**Never explain the theory by name on a component.** No card says "Bourdieu" or "habitus
capital." If a mechanic needs a lecture to make sense, the mechanic is wrong - the concept
already says this, and it applies double to the graphic design.

**Sentence length:** the scholar's voice runs long and calm. The corporation's voice is clipped
and full of nouns. The margin is a fragment.

---

## 9. Anti-patterns - the fastest ways to ruin this

1. **Gloss or UV coating.** Instant death.
2. **Startup aesthetics** - gradients, rounded sans-serif, pastel, isometric people, "playful"
   illustration. This is the opposite of the target.
3. **Corporate satire** - ties, briefcases, angry-boss caricatures, Dilbert energy. The game
   is a study, not a joke.
4. **Painted miniatures.** Undermines the specimen framing and adds cost for nothing.
5. **Icon-only rules.** See §6.
6. **Pure black text.** Always Oak Gall.
7. **Naming a theorist on any component.** The theory stays under the hood.
8. **A fifth typeface.** Three voices, no more.

---

## 10. The one-line test

> **Does it look like a thoughtful person's field notes on a software team - or does it look
> like a game about business?**

If it's the second one, throw it out.
