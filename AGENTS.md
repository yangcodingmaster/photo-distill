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

## Protocol — hard rules, in order / 协议——按序号执行的硬约束

**0. Capability check — TEST, don't assume. 开工自检——实测，别"以为"。**
Before any poster work, verify three things:
(a) you can render HTML → PNG (try it; macOS & Linux commands in
[references/pipeline.md](references/pipeline.md) §4 — no browser at all → hand the user
the HTML file itself);
(b) **you can actually SEE the rendered PNG** — the test: after rendering, name three
concrete things visible in the image. Can't do it = you are blind = switch to the blind
protocol below. Pretending to see is worse than not seeing;
(c) you can run Python + PIL (`python3 -c "from PIL import Image"`).
开工前实测三件事：能渲染吗；**能看见渲染结果吗**（检验：说出画面里三个东西，
说不出＝盲＝走盲画协议，不许装）；能跑 Python + PIL 吗。

**Blind protocol / 盲画协议** — when (b) fails: build v1 from sampled numbers, deliver it
**immediately**, and say plainly "I cannot see my own render — please look and tell me
what's wrong." After that, every single change must be driven by user feedback: one
comment → one fix → deliver again. **Zero self-initiated iterations.** A blind revision
is a wasted revision.
(b) 不成立时：第一版按采样数据画完**立刻交付**，明说"我看不到渲染结果，请你看图反馈"；
此后一条反馈 → 一处修改 → 立刻再交，**自发迭代次数为零**。

**1. One self-fix round, then STOP. 一轮自查，然后必须停。**
After the first render you get **exactly one** round of self-fixes (only defects visible
at thumbnail size). Then you MUST hand the image to the user. Making two consecutive
revisions without user input is a protocol violation. Every delivery carries three
things: the image, one sentence on what changed, one concrete question ("what should I
adjust?"). The user's one-line reaction outguides five rounds of your own polishing.
首版渲染后你**有且只有一轮**自查（只修缩略图上看得见的错误），然后必须把图交给用户；
未经用户输入连改两版＝违反协议。每次交付带三样：图、一句话说明改了什么、一个明确的问题。

**2. Never sample contours. 绝不采轮廓。**
The sampling list becomes the drawing list — sample a treetop's outline and you will end
up drawing a mountain. A boundary needs one y value, not 141 profile points. Sample only
relation quantities: positions, densities, one dividing line, hue/saturation.
采样清单就是绘制清单——采了树梢的起伏，就会画出一座山。只采关系量：
位置、密度、一条分界线、色相/饱和度。

**3. Every number from a script; every colour from a sampled pixel. 数字必须脚本算，颜色必须采出来。**
Coordinates, geometry, colour values — computed, shown, never eyeballed. If sampling is
impossible in your environment, offer the default palette in
[references/design-system.md](references/design-system.md) or ask the user to name
colours — **never invent them from vibes**: an invented palette gets the mood wrong on
v1 and every later fix guesses on top of the error. The four sign-off metrics are
**factory inspection, not creative targets**: run them once, only after the user approves
the look, via `scripts/finalize_poster.py` (renders 2×, checks, deletes on FAIL;
user-approved deviations recorded with `--waive`). Never tweak the artwork to chase
percentages. When delivering from a non-local environment, attach the 6-line run log
from [references/run-log-template.md](references/run-log-template.md).
坐标、几何、色值——脚本算、亮出来，绝不目测。环境跑不了采样就给默认色板或请用户报色，
**绝不凭印象编**。四项定稿指标是**出厂检验不是创作目标**：只在用户说行之后经
`scripts/finalize_poster.py` 跑一次（FAIL 即删；用户确认的偏离用 `--waive` 记录），
禁止为凑百分比改画面。非本机环境交付时附 6 行运行日志（run-log-template.md）。

## Then, as needed / 然后按需读

| File | Load when |
|---|---|
| [references/pipeline.md](references/pipeline.md) | Starting out: EXIF, minimal sampling, HEIC trap, render/export commands for macOS & Linux · 开工第一步与导出时 |
| [references/craft-rules.md](references/craft-rules.md) | Before drawing and before sign-off: perspective, material grammar, failure cases, checklist · 动手前和定稿前 |
| [references/filters.md](references/filters.md) | Deciding how to draw a symbol: copy-paste SVG filter library, mask patterns · 决定符号怎么画时 |
| [references/design-system.md](references/design-system.md) | Building the skeleton or checking constraints: paper, ink, colour anchor, archive type, hard avoids, slots · 搭骨架与定稿对表时 |
| [assets/template.html](assets/template.html) | Copy this to start a new poster · 每张海报的起步骨架 |
| [examples/structural-index.md](examples/structural-index.md) | Picking a graphic language for a new photo — structure type → move, read this first · 选语言前先认结构 |
| [examples/](examples/) | Eight original-to-poster pairs with notes · 八对原片与成品对照 |
| [scripts/finalize_poster.py](scripts/finalize_poster.py) | Sign-off only: render 2× + four metrics, fail-closed · 定稿专用 |
