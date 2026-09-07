# Design Guide - High-Performance Team

Status: **v2.0 - art direction locked, execution not started.**

> **What changed from v1.0:** the iconography (§6) and the habitus-figure sculpting direction
> (§5) move from hand-inked woodcut engraving to **low-poly, faceted geometry** - flat-shaded
> planes with hard edges, no smoothing, no gradients. The earthy palette (§4) and the Field
> Study/academic framing (§1-2) are unchanged and still govern everything below.

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

> **v3 override: all text is pure black (`#000`).** The Oak Gall Ink convention below described
> a warm brown-black for body text; the client has since directed **black text only, everywhere,
> with no exceptions** - no Oak Gall, no Slate, no track-coloured keywords (Trust/Capability/
> Shared Practice/Adaptability), no Redline alert text. Colour now lives **only** in backgrounds,
> washes, and outline strokes (see §4) - never in a text fill. The one accepted exception is
> light text set directly on a dark shape fill for contrast (e.g. the Bone numerals on the
> Feature Tower's Timber work-counter dots), which is a legibility requirement, not a stylistic
> choice.

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
| Ivory | `#F2EDE0` | Highlights, the habitus figures |
| Oak Gall Ink | `#2A2620` | All body text - a brown-black, never pure black |
| Herbarium Green | `#5A6650` | Capability, growth, learning |
| Smoky Rose | `#905151` | Trust, binding/registration guide lines, **and** Redline (rework, defects, locked/red borders) - one color now covers both; see the note below. |
| ~~Oxblood~~ | ~~`#7B3F35`~~ | Retired - merged into Smoky Rose above. |
| Motivation | `#D3B1B1` | Dusty rose - the Motivation box, every "Lose 1 Motivation" highlight on cards. Supersedes "Ochre" below, which was never actually built - this is the color the whole project converged on instead. |
| ~~Ochre~~ | ~~`#C08A3E`~~ | Retired - documented for Motivation but never used anywhere; see Motivation above. |
| Slate | `#4A5259` | Shared Practice, structure, rules furniture |
| Timber | `#8B6F47` / `#5C4830` (finished) / `#EFE4D3` (card tint) | Work - the feature Work-counter pips (darker shade = reached Work Cost) and the highlight box on the Work Activity card |

### The intrusion - corporate accents
**Used only for things that happen *to* the team.** Events, management demands, rework,
deadlines. Never for the team's own tracks, characters, or Habits.

| Name | Hex | Use |
|---|---|---|
| Highlighter | `#E8C547` | Management-category Events. The colour of someone else's priority. |
| ~~Redline~~ | ~~`#B03A2E`~~ | Retired - merged into Smoky Rose (team's world palette, above). |
| Ledger Blue | `#3B5B7A` | Customer-category Events, external dependencies |

> **The colour rule:** earthy = the team. Accent = the world acting on the team. A player
> should be able to feel, without being told, that the yellow things are not on their side.
> **Smoky Rose is the one deliberate exception** - Trust/binding (team) and Redline (intrusion)
> now share a single color, collapsing that split for this pair only. Highlighter and Ledger
> Blue still hold the line for everything else.

### The palette gaps - filled

Four concepts had no colour at all and were borrowing someone else's (Capital sat on an
unrelated purple; the Adaptability track and the Event categories People/Environment were
quietly reusing Trust/Capability's earthy tints or Customer's accent blue). Trust's own
sentence-level highlights had the same problem the other way round - reusing its pale *tint*
as if it were a wash. Filled with a **dusty, muted fourth family** - lighter and greyer than
the earthy tier, distinct from the saturated corporate accents - each with a wash (area fills,
bands, highlights) and, where it's read as text, a darker ink:

| Concept | Wash (fills, bands) | Ink (text, icons, strokes) | Use |
|---|---|---|---|
| Trust | `#D3CEDF` Lavender | *(no separate ink - text is pure black per §3)* | The Ledger's Trust band, the "+1/Lose 1 Trust" highlights on cards - seam-32 keeps the Oxblood ink until re-derived from Lavender |
| Capital | `#D9D3C4` Bone | `#6E6249` Bone Ink | Personal standing/recognition - the "+2 Capital" highlight, the Capital box on the person board; the seam-12 placement line |
| People | `#F5CE89` Apricot Cream | `#9C7A32` Apricot Cream Ink | Event category header (`cat-ppl`); also board 3's Standing slot (shared colour, different concept); the seam-31 placement line |
| Environment | `#B8C1A1` Dry Sage | `#6E7A54` Dry Sage Ink | Event category header (`cat-env`); the seam-43 placement line |
| Adaptability | `#B5C7CF` Pale Sky | `#3F5B66` Pale Sky Ink | The team's re-lay track - the Ledger's 4th band, the "+1 Adaptability" highlight/keyword; the seam-41 placement line |

The five **inks** above also double as the **board-to-board seam placement guide** (see
`_check-table-layout.svg` and the matching edge lines on each printed board) - one seam per
colour, so the same five names cover every stroke on the table, not just the cards.

No pure black (`#000`), no pure white (`#FFF`), no gradients, no drop shadows, no gloss.

> **Print-reality rule for the POC:** these prototypes come off cheap home/office
> inkjet/laser printers with no colour profiling - a full-saturation palette hex used as a
> **field behind text** will run dark and murky and take the Oak Gall contrast with it. Every
> named colour above is for **outlines, icons, small fills, and text itself only.** Any
> background sitting behind text must be a **pale tint of that hue at roughly 90%+ lightness**
> - the existing card/board tints (`#D3CEDF` Lavender/Trust, `#DFF0DB` Capability, `#DDE1E2`
> Shared Practice, `#FAECBE` Highlighter, `#DCE7F2` Ledger Blue, `#EFE4D3` Timber, `#E8D4B8`
> habitus) are the calibrated examples; derive new ones the same way rather than lightening
> by eye.

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

**Sculpted low-poly - flat, faceted planes with hard edges, no smoothing, no organic
curvature.** They should read as **faceted plaster casts or geological specimen models**, not
as toys, wargaming miniatures, or smooth-shaded renders. Differentiation between characters
comes entirely from *shape* - never from colour. Shape includes **pose and sculpted
clothing/props**, not just outline - a Base can plant its feet differently, a Torso can wear a
different collar or fold its sculpted arms differently, an Item can be held at a different
angle. **Not a Lego look** - avoid interchangeable blocky proportions, peg hands, or the
iconic minifig silhouette - but it can be **just as simple**: flat facets, minimal detail, no
fine ornamentation.

This is thematically exact: habitus is structure, not decoration, and low-poly facets *are*
visible structure. It's also practically useful for FDM printing - faceted planes need far
fewer supports than organic curves - and removes the "my mini isn't painted" problem
entirely. Print specs stay with the `board-game-3d-printing` skill; this guide only fixes the
look.

---

## 6. Iconography

**Low-poly, faceted geometric illustration.** Every icon, diagrammatic figure, and printed
motif is built from flat-shaded polygonal facets with visible hard edges - never smooth
curves, never gradients, never rounded blends. This is a direct extension of the "no
gradients, no gloss" material rule in §5: low-poly facets are *definitionally* flat-shaded, so
the two rules reinforce each other rather than compete.

Each facet fills from the earthy palette (§4) only - **never** the corporate accent colours,
which stay reserved for card fields and rules furniture, not iconography. A hard, 1pt Oak Gall
outline traces every facet edge, so the line work still reads as field-notes material -
surveyed and drafted by hand - rather than a rendered video-game asset.

Reference points: faceted mineral/crystal specimens, low-poly terrain and contour surveys,
geodesic-dome diagrams, herbarium presses redrawn as flat triangulated planes.

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
2. **Startup aesthetics** - gradients, rounded sans-serif, pastel, cartoon SaaS-marketing
   mascots, "playful" illustration. This is the opposite of the target.
3. **Corporate satire** - ties, briefcases, angry-boss caricatures, Dilbert energy. The game
   is a study, not a joke.
4. **Painted miniatures.** Undermines the specimen framing and adds cost for nothing.
5. **Smoothed or subdivided low-poly.** If the facets get smoothed into curves or hidden with
   a subdivision pass, the whole point evaporates. Edges stay hard and visible, always.
6. **Icon-only rules.** See §6.
7. **Pure black text.** Always Oak Gall.
8. **Naming a theorist on any component.** The theory stays under the hood.
9. **A fifth typeface.** Three voices, no more.

---

## 10. The one-line test

> **Does it look like a thoughtful person's field notes on a software team - or does it look
> like a game about business?**

If it's the second one, throw it out.
