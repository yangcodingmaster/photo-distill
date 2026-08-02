# AGENTS.md

This repository is a **skill**: a method for distilling a photograph into a minimal
zine-style paper poster — hand-written HTML/CSS/SVG, exported via headless Chrome.
No image generation model is involved. No photo pixels end up in the poster.

本仓库是一个 **skill**：把一张照片蒸馏成极简 zine 纸质海报的方法——
手写 HTML/CSS/SVG 绘制、无头 Chrome 导出。不用图像生成模型，成品里没有照片像素。

## Read this first / 先读这个

**[SKILL.md](SKILL.md)** — the method, the workflow, the hard rules.
Read it in full before starting any poster task. Everything else is loaded on demand.

**[SKILL.md](SKILL.md)** —— 方法论、工作流、硬性规则。
接到任何海报任务前先完整读一遍，其余按需加载。

## Then, as needed / 然后按需读

| File | Load when |
|---|---|
| [references/pipeline.md](references/pipeline.md) | Starting out: EXIF, HEIC orientation trap, sampling, Chrome export commands · 开工第一步与导出时 |
| [references/craft-rules.md](references/craft-rules.md) | Before drawing and before finalizing: perspective, material grammar, failure cases, checklist · 动手前和定稿前 |
| [references/filters.md](references/filters.md) | Deciding how to draw a symbol: copy-paste SVG filter library, mask patterns · 决定符号怎么画时 |
| [references/design-system.md](references/design-system.md) | Building the skeleton or checking against constraints: paper, ink, colour anchor, archive type, hard avoids, customization slots · 搭骨架与定稿对表时 |
| [assets/template.html](assets/template.html) | Copy this to start a new poster · 每张海报的起步骨架 |
| [examples/](examples/) | Five original-to-poster pairs with notes · 五对原片与成品对照 |

## Non-negotiables / 不可协商

Two rules matter more than the rest, and both are easy to violate while feeling productive:

有两条比其他都重要，而且违反的时候手感通常还很好：

1. **Wait for the user to approve the distillation plan before drawing.**
   One photo at a time. Never batch, never decide for them.
   **给出蒸馏方案后等用户确认再动手。** 一张一张做，不批量、不自作主张。

2. **Every number that reaches the artwork must be computed by a script** — coordinates,
   geometry, perspective landings, colour-anchor area. Show the computation. Never eyeball.
   **进成品的每个数字必须脚本算**——坐标、几何、透视落点、色锚面积。展示计算过程，绝不目测。
