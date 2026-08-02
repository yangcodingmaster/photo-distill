# Photo Distill

**Distil a photograph into three or four printed marks — one block of ink, one line,
one point of colour, one row of small type. When the meaning is there, stop.**

A skill for turning your own photographs into minimal zine-style paper posters.
No image generation model. No photo pixels in the output. Every poster is hand-written
HTML/CSS/SVG, drawn from coordinates sampled out of the original by script, and exported
to PNG through headless Chrome.

[中文版 →](README.zh-CN.md)

![](examples/23-sevensisters-poster.jpg)

---

## What this is

Most "turn my photo into art" tools work by transformation: filter the pixels, restyle
them, generate a lookalike. This works the other way round. The photograph is read, measured,
and then **abandoned** — what gets printed is a small set of abstract marks that carry the
same relationship the photograph carried.

The output is a single self-contained HTML file (double-click to open) plus a 2× PNG.
Nothing to install, nothing to render, no API calls.

## The method

Three routes were tried. The first two failed, and the failures are the useful part:

1. ❌ **Collage** — cut pixels from the photo, age them, paste them on paper.
   Reads as a cut-out, not a poster.
2. ❌ **Literal redrawing** — draw the whole scene: night sky, glowing lamp, misty tree line.
   Too literal; it becomes an illustration of the photograph.
3. ✅ **Abstract redrawing** — print abstract symbols on paper.
   A street lamp at night = one tall indigo block (night) + a thin black line through it
   (the pole) + an amber dot with an off-register double (the lamp) + an amber bar
   below (the lit road).

### Then one layer deeper: the reverse-semantic move

The end of distillation isn't "draw the object more simply." It's **strip the photograph
down until only a relationship is left, then draw only that relationship.**

Forward semantics: *look at the image → recognise blossoms and asphalt.*
Reverse: *extract the relationship (a uniform field with three anomalies) → draw the field
and the anomalies.*

> **The test: if the viewer is still counting petals, you are still drawing the object.**

The objects may disappear. The facts may not — those three gaps still sit at the measured
centres of the three bright clusters in the original file.

## Examples

Eight original-to-poster pairs, each a different graphic language, with notes on what became
what: **[examples/](examples/)**

| | |
|---|---|
| ![](examples/20-blossoms-poster.jpg) | ![](examples/22-aircraft-poster.jpg) |
| ![](examples/09-lamp-poster.jpg) | ![](examples/04b-two-kids-poster.jpg) |

## Install

```bash
git clone <this repo> ~/code/photo-distill
ln -s ~/code/photo-distill ~/.claude/skills/photo-distill
```

The symlink makes it available in every Claude Code session; edit the source repo and both
stay in sync. **Codex and other agents** read [AGENTS.md](AGENTS.md) at the repository
root — point them at the folder and they'll find their way in.

Then just say what you want:

> 把这张照片做成海报 — *make a poster from this photo*

## How it runs

One photograph at a time, and speed is the first metric: **the first image reaches you in
about five minutes.**

1. **You name the two or three elements that matter** — "the window's outline, the green
   outside, the soft light". That sentence is the plan; drawing starts immediately.
   Anything you didn't name is neither sampled nor drawn
2. Facts are read off the original (aspect ratio, EXIF), then one script samples only the
   relation quantities those elements need — positions, densities, one dividing line, hue.
   Contours are never sampled: sample a treetop's outline and you end up drawing a mountain
3. Drawn at full texture in one pass, screenshotted, delivered
4. You react ("the black reads like a mountain"), each fix re-renders in ~30 seconds
5. When you say it's right: four metrics are verified by script, then exported at 2× and
   committed

## What you can change

Six slots are open. The defaults are the origin of the visual language; the table in
[references/design-system.md](references/design-system.md#6-自定义槽位) says what to
respect when changing each.

| Slot | Default |
|---|---|
| **Aspect ratio** | Same as the original photograph, portrait or landscape |
| **Typeface** | Courier / Songti stack — one stack site-wide, italics disabled |
| **Paper colour** | Warm off-white `#e9e3d5` |
| **Colour anchor** | Rotates by photograph — cobalt, signal red, amber, mint… |
| **Archive type** | Three lines of real shooting parameters |
| **Numbering** | `NO. XXX` plus a registration mark |

Some things are not open: the paper grain parameters, `multiply` ink-on-paper, the ban on
material simulation, the four hard metrics for the colour anchor, and the list of hard
avoids. Change those and it stops being this language.

## Contents

```
SKILL.md                     The method, the workflow, the hard rules — read first
AGENTS.md                    Entry point for Codex and other agents
references/
  design-system.md           Paper, ink, colour anchor, archive type, hard avoids, slots
  filters.md                 Copy-paste SVG filter library and mask patterns
  craft-rules.md             Perspective, material grammar, failure cases, final checklist
  pipeline.md                EXIF, the HEIC orientation trap, sampling, export commands
assets/template.html         Skeleton to copy when starting a new poster
examples/                    Eight original-to-poster pairs with notes
```

## Notes

The filter parameters in here are not defaults anyone chose — they were calibrated one
poster at a time, usually after two or three versions that looked fine and were wrong.
The comments recording *how* each one failed are worth more than the values themselves.
When something in here looks arbitrary, that's usually where a hard-won number is hiding.

---

*Distilled from the Photo Minimal series (NO. 001–026). Photographs © Yang Zhao.*
