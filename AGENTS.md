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
| [references/pipeline.md](references/pipeline.md) | Starting out: EXIF, the minimal-sampling rule, HEIC orientation trap, Chrome export commands · 开工第一步与导出时 |
| [references/craft-rules.md](references/craft-rules.md) | Before drawing and before sign-off: perspective, material grammar, failure cases, checklist · 动手前和定稿前 |
| [references/filters.md](references/filters.md) | Deciding how to draw a symbol: copy-paste SVG filter library, mask patterns · 决定符号怎么画时 |
| [references/design-system.md](references/design-system.md) | Building the skeleton or checking against constraints: paper, ink, colour anchor, archive type, hard avoids, customization slots · 搭骨架与定稿对表时 |
| [assets/template.html](assets/template.html) | Copy this to start a new poster · 每张海报的起步骨架 |
| [examples/](examples/) | Eight original-to-poster pairs with notes · 八对原片与成品对照 |

## Non-negotiables / 不可协商

Three rules matter more than the rest, and all are easy to violate while feeling productive:

有三条比其他都重要，而且违反的时候手感通常还很好：

1. **Speed is the first metric: first image in front of the user within ~5 minutes.**
   The user names the two or three elements that matter — that sentence IS the plan; start
   drawing immediately. Everything they did not name: don't sample it, don't draw it.
   Deliver after one screenshot; the user's one-line feedback beats five rounds of your
   own polishing.
   **速度是第一指标：约 5 分钟内让用户看到第一张图。** 用户点名的两三个元素就是方案，
   直接开画；没点名的东西一律不采样、不绘制。截一张图就交出去——
   用户一句话反馈顶你自己打磨五轮。

2. **Never sample contours.** The sampling list becomes the drawing list — sample a
   treetop's outline and you will end up drawing a mountain. A boundary needs one y value,
   not 141 profile points. Sample only relation quantities: positions, densities, one
   dividing line, hue/saturation.
   **绝不采轮廓。** 采样清单就是绘制清单——采了树梢的起伏，就会画出一座山。
   一道边界只需要一个 y 值。只采关系量：位置、密度、一条分界线、色相/饱和度。

3. **Every number that reaches the artwork must be computed by a script** — coordinates,
   geometry, colour-anchor area. Show the computation. Never eyeball. The four sign-off
   metrics run once, only after the user approves.
   **进成品的每个数字必须脚本算**——坐标、几何、色锚面积。展示计算过程，绝不目测。
   四项定稿实测只在用户说行之后跑一次。
