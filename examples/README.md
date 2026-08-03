# Examples · 示例

Eight pairs, each a different graphic language. Left is the photograph, right is the
poster. Nothing was traced, cropped, or filtered — every poster is drawn from scratch
in HTML/CSS/SVG, with coordinates sampled from the original by script.
Picking a language for a new photo? Start from the one-line map in
[structural-index.md](structural-index.md).

八对，各自代表一种不同的图形语言。左边原片，右边成品。
给新照片选语言，先看一行式索引 [structural-index.md](structural-index.md)。
没有描摹、没有裁贴、没有套滤镜——每张海报都是从零手写的 HTML/CSS/SVG，
坐标由脚本从原片采样得到。

---

## NO. 009 — 夜的墨块 / The Block of Night

| 原片 Original | 成品 Poster |
|---|---|
| ![](09-lamp-original.jpg) | ![](09-lamp-poster.jpg) |

The founding piece — the first poster with zero photo pixels, and the one that settled
the method. A street lamp at night becomes: one tall indigo block (the night),
a thin black line through it (the pole), an amber dot with an off-register double at the
top (the lamp), an amber bar below (the lit road). Four marks. That's the whole poster.

奠基之作——第一张零照片像素的海报，也是定下方法论的那张。
夜里的一盏路灯变成：一块竖长靛蓝墨块（夜）+ 一根细黑线穿过（灯柱）
+ 线顶一个带套印错位的琥珀圆点（灯）+ 下方一道琥珀横条（被照亮的路）。
四个记号，整张就完了。

---

## NO. 020 — 均质点场 + 三处异常 / A Uniform Field, Three Anomalies

| 原片 Original | 成品 Poster |
|---|---|
| ![](20-blossoms-original.jpg) | ![](20-blossoms-poster.jpg) |

The clearest demonstration of the reverse-semantic move. Forward semantics says
"blossoms on asphalt." Reverse says: *a uniform field with three anomalies* — so tarmac
and flowers become **the same symbol**. 2,500 near-identical ink dots make the field;
the flowers are where the dots step aside. The field's edge thins out on its own rather
than being drawn.

Three earlier versions failed: printing black and cutting out flower shapes (still objects);
removing the asphalt texture simulation (still objects). Only unifying both into one symbol
worked. The three gaps sit at the measured centres of the three bright clusters in the original.

反向语义最清楚的一次示范。正向语义说"柏油上的花"，反向说：
**一片均质的场 + 三个异常点**——于是柏油和花统一成**同一种符号**。
2500 颗几乎一样的墨点构成场，花是点阵让开的空处，场的边界自己稀疏掉，不画。

前三版全废：印一块黑挖出花形（仍是物体）、撤掉沥青质感模拟（仍是物体）。
只有把两者统一成一种符号才成立。三处空处的坐标是原片三个亮团中心的实测值。

---

## NO. 022 — 无边界墨气 + 全张唯一的硬边 / One Hard Edge

| 原片 Original | 成品 Poster |
|---|---|
| ![](22-aircraft-original.jpg) | ![](22-aircraft-poster.jpg) |

Clouds have no shape, so they are not drawn as shapes. The original's brightness field is
downsampled onto a grid of ellipses, then dissolved past any edge
(`feGaussianBlur 46` + `feDisplacementMap 56`). The aeroplane is the only thing in the
frame with a precise outline.

**Self-check for this grammar: cover the one hard-edged symbol, and the poster should
read as no shape at all.** The ink density here took several attempts — ×0.62 turned the
paper dirty, ×0.34 still pressed out a grey cloud; ×0.17 is where paper stays paper.

云没有形状，所以不画成形状。原片亮度场降采样成一片椭圆，
再用 `feGaussianBlur 46 + feDisplacementMap 56` 化到没有一条边。
飞机是全张唯一有精确轮廓的东西。

**这套语法的自查判据：盖住那个硬边符号，整张应该读不出任何形状。**
浓度试了几轮——×0.62 糊成脏纸，×0.34 仍压出一团灰云，×0.17 才是"纸还是纸"。

---

## NO. 023 — 密度梯度场 / The Line Appears By Itself

| 原片 Original | 成品 Poster |
|---|---|
| ![](23-sevensisters-original.jpg) | ![](23-sevensisters-poster.jpg) |

No horizon is drawn. Thousands of short marks vary only in stroke width and opacity,
monotonically with distance — and the line appears on its own.

Two calibrations worth stealing: the colour anchor is not a band laid over the field but
**those rows' own marks turned red**, coexisting with the ink ones (replace them and it
reads as a separate ribbon floating above the sea). And the anchor sits at the *start of the
marks*, not at the steepest brightness gradient — the eye reads the boundary where the
symbol begins, not where the physics peaks.

海平线一根没画。几千道短痕只在 stroke-width 和 opacity 上随距离单调变化，
线就自己出现了。

两条值得偷师的校准：色锚不是盖在场上的一条带，而是**把那几行的痕换成红的**、
与墨痕共存（替换那一段会读作悬在海上方的另一条带）。
色锚落在**痕的起点**而不是亮度最陡处——人眼认边界是认符号从哪开始，不是认物理量的极值。

---

## NO. 004-B — 油画棒 + 测距图 / Crayon Drag & Measurement

| 原片 Original | 成品 Poster |
|---|---|
| ![](04b-two-kids-original.jpg) | ![](04b-two-kids-poster.jpg) |

A remake of an earlier collage-era poster under the distillation grammar (kept as a `-b`
file; the original was never deleted, and the poster number stays). Two children in a lake
become two ink dots with trembling reflections; the lake becomes five crayon drags.

The crayon effect is anisotropic turbulence (`baseFrequency="0.010 0.16"` — low across,
high down, giving horizontal drag), displaced for a ragged edge, then punched through by
*the same noise* converted to alpha (`A = 2.4R − 0.62`) so the paper's tooth doesn't take
the wax. The `Δ 378 PX` annotation is a measured distance, not decoration.

早期拼贴时代作品按蒸馏语法的重制版（新开 `-b` 文件，旧版保留，编号沿用）。
水里的两个孩子变成两个墨点人加颤抖的倒影，湖变成五道油画棒横拖。

油画棒的做法：各向异性湍流（`baseFrequency="0.010 0.16"`，横低纵高 ⇒ 横向拖痕）
→ 推毛边 → 再用**同一套噪声**换算成 alpha（`A = 2.4R − 0.62`）挖洞，
纸的凹处没吃到蜡。`Δ 378 PX` 是实测距离，不是装饰。

---

## NO. 024 — 一方冷，亮从里面让开 / A Cold Rectangle, and the Light That Steps Aside

| 原片 Original | 成品 Poster |
|---|---|
| ![](24-shard-original.jpg) | ![](24-shard-poster.jpg) |

Made with this skill from scratch, as a live test of it. A room at dusk, a window, the Shard
two kilometres away. The first attempt drew the window — frame, mullion, transom — and read
as an icon of a window. That is the "still counting petals" failure.

What the photograph actually is: **one warm field with a cold rectangle cut into it, and
everything visible is light stepping aside from that cold.** So the mullion is not drawn at
all — only the difference it causes (left pane has sky and tower, measured L≈65; right pane
is all tree shadow, L≈45) survives, as a gradient across the blue. The tower is drawn only
for the length it actually glows: contrast measured +145 at its brightest, decaying to +15
by y=383, so that is exactly where the shape stops. The beacon sits below it, alone in the
dark stretch — because in the original it does too.

The other fact the poster keeps: **near is blurred, far is sharp.** The window frame is out
of focus in the photograph, the tower two kilometres away is not. So the tower is the only
edge in the whole sheet, and every other boundary is eaten back into the paper.

用这个 skill 从零做的一张，作为对 skill 本身的实测。黄昏的房间、一扇窗、两公里外的碎片大厦。
第一版把窗画了出来——窗框、竖棂、横档——结果读作"一扇窗的图标"。
这就是"还在数花瓣"的那种失败。

照片真正的样子：**一整片暖里开了一方冷，而所有能被看见的东西，都是从那片冷里让开的亮。**
所以竖棂完全不画，只留它造成的差异（左格有天有塔，实测 L≈65；右格全是树影，L≈45），
变成蓝里的一道浓度梯度。塔只画它真的在发光的那一段：实测对比度最亮处 +145，
衰减到 y=383 时只剩 +15，形状就正好停在那里。红灯孤零零在下面那段暗里——因为原片里它就是这样。

海报保住的另一个事实：**近的糊、远的清。** 照片里窗框是失焦的，两公里外的塔却是清晰的。
于是塔成了全张唯一的边，其余所有边界都被纸吃了回去。

Measured on the finished file: colour anchor 1.93% of canvas (target 0.8–2.5%), ink 17.0%
(target 8–25%), paper 83.0%, hue 211° with 5–95 percentile 206–212° — a single hue.

成品实测：色锚占画布 1.93%（目标 0.8–2.5%），实际着墨 17.0%（目标 8–25%），纸 83.0%，
色相 211°、5–95 分位 206–212°——单一主色相。

---

## NO. 025 — 内透的光与投射的光 / Light From Within, Light Cast Down

| 原片 Original | 成品 Poster |
|---|---|
| ![](25-primrose-original.jpg) | ![](25-primrose-poster.jpg) |

The first poster made under the revised workflow: three written options first, then a
low-fidelity sketch, then texture. The brief that shaped it came from one sentence — the
park's yellow lamps, and their relationship to the city's lit windows behind.

That word, *from within*, decided the whole grammar. **The two kinds of light had to be
drawn as two different symbols**: the distant windows glow but illuminate nothing, so they
are hard-edged little blocks with no halo at all; the lamps cast light, so each has a small
bright core and a wide smear of warm ink pooled on the ground beneath it.

The skyline is not drawn. The measured density of lit windows (per-cell counts, adaptive
threshold per row) is kept, then **the positions are re-scattered at random within each
cell** — density survives, building silhouettes do not. An earlier draft sampled positions
directly and you could pick out the Shard; that is drawing the object again.

Paper does double duty here: it is the dusk sky above, and it is the unlit grass below.
Ink can't print light on cream paper, so darkness is simply where nothing was printed, and
the tree line — one narrow band dissolving downward — is the only solid ink in the sheet.

用改版后流程做的第一张：先给三个文字方案，再出低保真草图，最后才上质感。
定调的是用户的一句话——公园里那些黄色的路灯光点，与它们背后城市灯光内透的关系。

"内透"这个词决定了整套语法。**两种光必须画成两种符号**：远处的窗光自身发亮却不照亮任何
东西，所以是**没有一点晕**的硬边小方块；路灯是投射光，所以每盏都是一个小亮核 + 下方
一摊洒开的暖墨。

天际线不画。实测的窗光密度（逐格计数、逐行自适应阈值）保留下来，
但**位置在每个格子内重新随机撒过**——密度留下，建筑轮廓丢弃。
早先一版直接照位置采样，结果能认出碎片大厦的尖顶：那又是在画物体了。

纸在这张里身兼两职：既是上方的暮色天空，也是下方没被照亮的草地。
米白纸上印不出光，所以"暗"就是没印东西的地方，而树线——一条往下化开的窄带——
是全张唯一的实墨。

Measured on the finished file: colour anchor 1.72%, ink 17.9%, paper 82.1%, hue 36° with
5–95 percentile spanning just 36–38°.

成品实测：色锚 1.72%，着墨 17.9%，纸 82.1%，色相 36°、5–95 分位只跨 36–38°。

---

## NO. 026 — 窗格线、一格绿、洒地的光 / A Grid, One Green Pane, Light on the Floor

| 原片 Original | 成品 Poster |
|---|---|
| ![](26-window-original.jpg) | ![](26-window-poster.jpg) |

The first poster under the speed-first workflow: the user named three elements — the
window's outline, the green outside, the soft gradient of light — and that sentence *was*
the plan. From receiving the photo to the first delivered image: about four minutes.

Three elements, three treatments. The window is an outer frame plus three mullions and
three transoms, every position measured from luminance valleys in the original. The green
lives only in the bottom row of panes, exactly where the lawn sits in the photograph
(measured H=50°, S=64%), with the glazing bars pressing over it. The light is a patch of
warm tone on the floor with no edge at all. The dark room itself is not drawn — nothing
else was named, and the paper does the darkness.

速度版流程的第一张：用户点名三个元素——窗户的轮廓、外面的绿、浅浅的渐变光——
这句话本身就是方案。从拿到照片到交出第一版，约四分钟。

三个元素三种处理。窗是外框加三竖棂三横棂，每个位置都从原片的亮度谷实测；
绿只住在最下面一排窗格里，正是照片里草坪所在的位置（实测 H=50°、S=64%），
窗棂从它上面压过去；光是地板上一片没有边的暖。房间的暗不画——
用户没点名别的东西，纸就是那片暗。

Measured at sign-off: colour anchor 2.41%, ink 10.5%, paper 89.5%, hue 56° (54–57°).

定稿实测：色锚 2.41%，着墨 10.5%，纸 89.5%，色相 56°（54–57°）。

---

*Photographs © the author. 照片版权归作者所有。*
