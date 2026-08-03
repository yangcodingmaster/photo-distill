# Photo Distill

**English** | [简体中文](README.md)

A skill for Claude Code (and Codex, via [AGENTS.md](AGENTS.md)) that distils your
photograph into a minimal zine-style paper poster — hand-written HTML/CSS/SVG rendered
by headless Chrome. No image-generation model. No photo pixels in the output.

## Before You Start

This skill is not a machine for mindlessly stamping out posters in this style.
It needs your ideas folded into it. AI has no feelings — a work holds together only
because **you** are expressing something through it: which two or three elements you
name, what you say is wrong, when you decide it is done. Those choices are what the
poster actually shows. So don't just drop a photo on the AI and walk away — your
participation is not optional; it is part of the method.

## Visual Design

The poster keeps:

- an aged off-white plain, at the photograph's own aspect ratio
- 70–90% of the sheet reading as paper; ink only where it earns its place
- two or three printed marks distilled from elements **you** name — the rest is dropped
- one high-saturation colour anchor, 0.8–2.5% of the canvas, verified by script
- torn-paper soft edges, off-register doubles, print grain — ink pressed into paper
- an archive line of real shooting parameters (file, camera, exposure, date, GPS)

and avoids: full-bleed scenes, cinematic lighting, 3D, drop shadows, decorative texture,
clean digital UI, and any readable slogan or caption.

## Examples

Photograph on the left, generated poster on the right.
Notes on each pair: [examples/](examples/)

| Original | Poster |
|---|---|
| ![](examples/04b-two-kids-original.jpg) | ![](examples/04b-two-kids-poster.jpg) |
| ![](examples/09-lamp-original.jpg) | ![](examples/09-lamp-poster.jpg) |
| ![](examples/20-blossoms-original.jpg) | ![](examples/20-blossoms-poster.jpg) |
| ![](examples/22-aircraft-original.jpg) | ![](examples/22-aircraft-poster.jpg) |
| ![](examples/23-sevensisters-original.jpg) | ![](examples/23-sevensisters-poster.jpg) |
| ![](examples/24-shard-original.jpg) | ![](examples/24-shard-poster.jpg) |
| ![](examples/25-primrose-original.jpg) | ![](examples/25-primrose-poster.jpg) |
| ![](examples/26-window-original.jpg) | ![](examples/26-window-poster.jpg) |

## Installation

```bash
git clone https://github.com/yangcodingmaster/photo-distill.git
ln -s "$(pwd)/photo-distill" ~/.claude/skills/photo-distill
```

The symlink makes the skill available in every Claude Code session.
**Codex users**: point the agent at this folder — it reads [AGENTS.md](AGENTS.md) at the
root and finds its way in. No other setup.

## Usage

**Step 1 — drop in a photo and name the two or three elements that matter to you.**
That sentence is the whole brief:

> 把这张照片做成海报。我想突出窗户的轮廓、外面的绿，和浅浅的渐变光。
>
> *Make a poster from this photo. I want the window's outline, the green outside,
> and the soft gradient of light.*

Everything you didn't name is neither sampled nor drawn — naming fewer elements gives a
more abstract poster, naming more gives a more literal one. If you'd rather not choose,
say so and the skill will ask one question or pick for you.

**Step 2 — the first image arrives in about five minutes.** React in plain words:

> 黑的那块太重了，读起来像山。 · *The black band is too heavy — it reads like a mountain.*

Each fix re-renders in about 30 seconds. You never touch the code.

Before starting, the agent self-checks its capabilities — can it render? can it *see* its
own render? can it sample pixels? If it cannot see (true of some Codex setups), it
switches to a **blind protocol**: the first version is delivered immediately, every later
change is driven only by your feedback, and it never silently self-iterates — you become
its eyes. Colours always come from sampled pixels, never from vibes.

**Step 3 — say it's right.** Only then does the skill verify the four print metrics by
script (colour-anchor area, ink coverage, thumbnail visibility, hue concentration),
export at 2×, and commit.

Six slots are customizable when you ask — aspect ratio, typeface, paper colour, colour
anchor palette, archive line, numbering. Details in
[references/design-system.md](references/design-system.md).

## Output

- `poster-XX-name.html` — self-contained, double-click to open, no dependencies
- a 2× PNG export of the finished poster
- an archive line on the sheet with your photo's real parameters — nothing invented

## Repository Structure

```
SKILL.md              The method, the workflow, the hard rules
AGENTS.md             Entry point for Codex and other agents (numbered protocol)
CLAUDE.md             Entry point when the repo is opened as a Claude Code project
references/           Design system · SVG filter library · craft rules · pipeline
scripts/              finalize_poster.py — fail-closed sign-off (render 2× + four metrics)
assets/template.html  Skeleton every new poster starts from
examples/             Eight original-to-poster pairs with notes
```

## License

Method and code free to use. Photographs © the author — please don't reuse the images.
