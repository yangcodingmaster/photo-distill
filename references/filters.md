# 滤镜与符号词汇 · Filters & Vocabulary

全部可直接复制。参数是逐张校准出来的，不是随手填的——改之前先看"何时用"和"坑"。

**seed 用质数轮换**（3 / 5 / 7 / 11 / 13 / 17 / 21 / 23 / 31），
避免同一张里不同滤镜的噪声重合出现可见的规律。

---

## 1. 揉边 rough1–4：手撕手贴的柔

这是全系列的基础质感——元素边缘不是矢量的硬边，而是被纸和手揉过一遍。
结构永远是 `feTurbulence → feDisplacementMap` 两步。

```xml
<filter id="rough1" x="-15%" y="-15%" width="130%" height="130%">
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="3" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.5" xChannelSelector="R" yChannelSelector="G"/>
</filter>

<filter id="rough2" x="-8%" y="-8%" width="116%" height="116%">
  <feTurbulence type="fractalNoise" baseFrequency="0.013" numOctaves="3" seed="11" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/>
</filter>

<filter id="rough3" x="-6%" y="-30%" width="112%" height="160%">
  <feTurbulence type="fractalNoise" baseFrequency="0.008" numOctaves="2" seed="17" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
</filter>

<filter id="rough4" x="-12%" y="-40%" width="124%" height="180%">
  <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="31" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/>
</filter>
```

| id | baseFrequency | scale | 用在 |
|---|---|---|---|
| rough1 | 0.05 | 2.5 | 小元素（人、点、灯） |
| rough2 | 0.013 | 5 | 色块 |
| rough3 | 0.008 | 3.5 | 线条（注意滤镜框上下放宽到 160%） |
| rough4 | 0.02 | 6 | 大色块 |

**变体 `press`**——只揉出印刷压痕，几乎不动形状。给"全张唯一的硬边"那个符号用，
它要保住轮廓，但不能是矢量的干净边：

```xml
<filter id="press" x="-30%" y="-30%" width="160%" height="160%">
  <feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="0.8" xChannelSelector="R" yChannelSelector="G"/>
</filter>
```

**滤镜框要留够**：`x/y/width/height` 不放宽的话，位移会被裁掉，边缘出现直的切口。
位移越大，框放得越宽。

**滤镜可以放两个地方**：内容 SVG 自己的 `<defs>` 里（多数情况）；
或者当 CSS `filter: url(#rough1)` 用在 HTML 元素上时，放在 body 顶部一个零尺寸 SVG：

```html
<svg width="0" height="0" style="position:absolute"><defs>
  <filter id="rough1" ...>...</filter>
</defs></svg>
```

---

## 2. 标准颗粒 grain：唯一被允许的"质感"

```xml
<filter id="grain" x="0%" y="0%" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="23" result="g"/>
  <feColorMatrix in="g" type="saturate" values="0"/>
</filter>
```

**用法固定**：把同一个形状再画一遍，套 grain，`screen` 混合、opacity 0.12：

```xml
<path d="…" fill="#cf9a33" filter="url(#rough4)"/>
<path d="…" filter="url(#grain)" opacity="0.12" style="mix-blend-mode:screen"/>
```

**这是唯一允许的材质层。** 沥青碎石、木纹、水波、布纹——任何**材质模拟**都是再现，不是蒸馏。
（曾叠三层骨料滤镜做柏油，像是很像，整张就废了。）

分界线：
- 模拟"画的东西长什么样" = **再现** ❌
- 模拟"笔怎么走、墨怎么上纸" = **印刷语言** ✅（grain 和下面的 pastel 都属于这类）

---

## 3. dissolve：无边界的墨气

给云、雾、水汽这类**本来就没有形状**的东西用。不画形状，只留浓度。

```xml
<filter id="dissolve" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur in="SourceGraphic" stdDeviation="46" result="b"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.004" numOctaves="3" seed="9" result="n"/>
  <feDisplacementMap in="b" in2="n" scale="56" xChannelSelector="R" yChannelSelector="G"/>
</filter>
```

喂给它的是**原片亮度场的网格降采样**——一排椭圆，opacity 来自实测亮度：

```xml
<g fill="#57524a" filter="url(#dissolve)">
  <ellipse cx="87.5" cy="77.3" rx="301.0" ry="266.0" opacity="0.018"/>
  <ellipse cx="262.5" cy="77.3" rx="301.0" ry="266.0" opacity="0.037"/>
  …
</g>
```

两个坑：

1. **椭圆半径要给到单元格的 1.7 倍**，否则会露出方块状的网格残影。
2. **浓度极难拿捏**：`亮度 × 0.62` 糊成脏纸，`× 0.34` 仍压出一团灰云，
   **`× 0.17` 才是"纸还是纸"**。

---

## 4. bleed：双级渗边

粗形变定大形，细毛边收边缘，最后一点模糊收口。给需要"渗进纸里"的色斑用。

```xml
<filter id="bleed" x="-25%" y="-25%" width="150%" height="150%">
  <feTurbulence type="fractalNoise" baseFrequency="0.006 0.009" numOctaves="4" seed="21" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="34" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="7" result="n2"/>
  <feDisplacementMap in="d" in2="n2" scale="5" xChannelSelector="R" yChannelSelector="G"/>
  <feGaussianBlur stdDeviation="1.4"/>
</filter>
```

⚠️ 这个滤镜会把形状**撑大**。色锚面积必须按成品实测回缩，见 design-system §3。

---

## 5. pastel：油画棒

最精巧的一个。三步：各向异性湍流做拖痕 → 推毛边 → 用**同一套噪声**当"纸的凹凸"挖洞
（纸的凹处没吃到蜡）。

```xml
<filter id="pastelA" x="-10%" y="-40%" width="120%" height="180%">
  <!-- 各向异性：横向低频、纵向高频 ⇒ 横向拖痕 -->
  <feTurbulence type="fractalNoise" baseFrequency="0.010 0.16" numOctaves="3" seed="5" result="s"/>
  <feDisplacementMap in="SourceGraphic" in2="s" scale="7"
                     xChannelSelector="R" yChannelSelector="G" result="p"/>
  <!-- 同一套噪声 → alpha：A = 2.4R − 0.62 -->
  <feColorMatrix in="s" type="matrix"
    values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  2.4 0 0 0 -0.62" result="tooth"/>
  <feComposite in="p" in2="tooth" operator="in"/>
</filter>
```

三档变体只改四个数（多道笔画叠加时错开，避免重复纹理）：

| id | baseFrequency | scale | alpha 系数 | seed |
|---|---|---|---|---|
| pastelA | 0.010 0.16 | 7 | 2.4, −0.62 | 5 |
| pastelB | 0.013 0.19 | 6 | 2.2, −0.55 | 17 |
| pastelC | 0.008 0.14 | 8 | 2.6, −0.7 | 31 |

**笔画本体**是圆角矩形，填一份共享的 `objectBoundingBox` 渐变收两端：

```xml
<linearGradient id="lakeDrag">
  <stop offset="0"    stop-color="#3878a8" stop-opacity="0"/>
  <stop offset="0.13" stop-color="#3878a8" stop-opacity="0.85"/>
  <stop offset="0.46" stop-color="#3878a8" stop-opacity="1"/>
  <stop offset="0.80" stop-color="#3878a8" stop-opacity="0.88"/>
  <stop offset="1"    stop-color="#3878a8" stop-opacity="0"/>
</linearGradient>

<g fill="url(#lakeDrag)">
  <rect x="300" y="306" width="416" height="80" rx="30" opacity="0.52"
        filter="url(#pastelA)" transform="rotate(-0.6 508 346)"/>
  <rect x="418" y="352" width="330" height="44" rx="20" opacity="0.30"
        filter="url(#pastelC)" transform="rotate(-0.3 583 374)"/>
</g>
```

想要纵向笔触就把 baseFrequency 的两个数**对调**（高频在横、低频在纵）。
多道叠加时用 multiply，自然加深。

---

## 6. mask 的四种用法

### ① 雾 = 把油墨吃掉（不是涂白）

白＝留墨，黑＝没印上。四道方向不同的 linearGradient 叠在同一个 mask 里，
整组元素 `<g mask="url(#fog)">`：

```xml
<linearGradient id="fogV" x1="0" y1="240" x2="0" y2="560" gradientUnits="userSpaceOnUse">
  <stop offset="0"    stop-color="#2a2a2a"/>
  <stop offset="0.34" stop-color="#8a8a8a"/>
  <stop offset="0.72" stop-color="#dcdcdc"/>
  <stop offset="1"    stop-color="#ffffff"/>
</linearGradient>
<linearGradient id="fogL" x1="60" y1="0" x2="440" y2="0" gradientUnits="userSpaceOnUse">
  <stop offset="0"   stop-color="#000000" stop-opacity="1"/>
  <stop offset="0.5" stop-color="#000000" stop-opacity="0.55"/>
  <stop offset="1"   stop-color="#000000" stop-opacity="0"/>
</linearGradient>
<!-- fogR / fogB 同理，收右边缘与下边缘 -->

<mask id="fog">
  <rect x="0" y="0" width="1200" height="900" fill="url(#fogV)"/>
  <rect x="0" y="0" width="1200" height="900" fill="url(#fogL)"/>
  <rect x="0" y="0" width="1200" height="900" fill="url(#fogR)"/>
  <rect x="0" y="0" width="1200" height="900" fill="url(#fogB)"/>
</mask>
```

配合**按距离分级的不透明度**（近 0.5 → 远 0.06，远的再加 1.3px 模糊）。
**纸就是雾**——白色补丁在有渐变的纸上一定露馅。

### ② 线端渐隐

白底上画"黑→透明"的 radialGradient 圆。停点固定用 `0 白 / 0.70 白 / 0.87 #8a8a8a / 1 黑`，
椭圆化靠 gradientTransform：

```xml
<radialGradient id="fade0" cx="1176.1" cy="633.9" r="84.8" gradientUnits="userSpaceOnUse"
                gradientTransform="translate(0,633.9) scale(1,1.442) translate(0,-633.9)">
  <stop offset="0"    stop-color="#ffffff"/>
  <stop offset="0.70" stop-color="#ffffff"/>
  <stop offset="0.87" stop-color="#8a8a8a"/>
  <stop offset="1"    stop-color="#000000"/>
</radialGradient>
<mask id="edge0"><rect x="0" y="0" width="1400" height="928" fill="url(#fade0)"/></mask>
```

**别用纸色补丁盖**，**别对高弯曲的弧用弦轴 linearGradient**（会吃掉半条弧）。

CSS 侧的等价写法（细线、雨帘）：

```css
-webkit-mask-image: linear-gradient(90deg, transparent 0, #000 25%, #000 75%, transparent 100%);
        mask-image: linear-gradient(90deg, transparent 0, #000 25%, #000 75%, transparent 100%);
```

### ③ 局部让开 / 两端收边

一个全幅 `fadeX` 收两端，再叠一个"要让开的形状"，形状自己也可以带滤镜：

```xml
<linearGradient id="fadeX" x1="100" y1="0" x2="1300" y2="0" gradientUnits="userSpaceOnUse">
  <stop offset="0"     stop-color="#000000"/>
  <stop offset="0.045" stop-color="#ffffff"/>
  <stop offset="0.955" stop-color="#ffffff"/>
  <stop offset="1"     stop-color="#000000"/>
</linearGradient>
<mask id="landMask">
  <rect x="0" y="0" width="1400" height="928" fill="url(#fadeX)"/>
  <path d="M …" fill="url(#gullyV)" filter="url(#rough2) blur(3px)"/>   <!-- 滤镜链 + CSS blur 混写 -->
</mask>
```

给档案微字挖出空位：mask 里放白底矩形 + 一个黑色圆角矩形 `style="filter:blur(13px)"`。

### ④ 色斑软边

见 ②，每个色斑一份 radialGradient + mask。注意渗边那段（stop 0.70–0.87）
仍是高饱和，会算进色锚面积。

---

## 7. 三条手法通则

**套印错位**——同形状低透明副本，先画，偏移 2–3px：

```xml
<g fill="#3c3830" opacity="0.30" filter="url(#press)" transform="translate(2.6,-2.0)"> … </g>
<g fill="#3c3830" opacity="1.00" filter="url(#press)" transform="translate(0,0)">     … </g>
```

**每元素微旋转 ±0.3–0.8°**：`transform="rotate(-0.6 508 346)"`。手贴的东西不会正。

**multiply 上纸**：每个内容层 `mix-blend-mode: multiply`，圆角 3–5px。
这是油墨吃进纸里的样子；不加就是贴上去的塑料片。

---

## 8. 常用符号词汇

- **低语线**：opacity .15–.2 的 1.5px 细线
- **渐隐竖痕**：mask 下端淡出
- **吊线 + 圆盘**
- **微缩人**：头点 + 身笔（圆 + 圆角矩形，各 6–17px）
- **回声残影**：低透明度副本
- **点场**：几千个几乎一样的点＝均质的场；让开的空处＝异常
- **密度梯度**：stroke-width 与 opacity 随距离单调变化，线自己出现，不画边界
