# Examples · 示例

Five pairs, chosen to cover five different graphic languages. Left is the photograph,
right is the poster. Nothing was traced, cropped, or filtered — every poster is drawn
from scratch in HTML/CSS/SVG, with coordinates sampled from the original by script.

五对，各自代表一种不同的图形语言。左边原片，右边成品。
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

*Photographs © Yang Zhao. 照片版权归赵洋所有。*
