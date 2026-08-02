# 设计系统 · Design System

海报的"物质基础"：纸、墨、色锚、档案微字。这一层在所有作品之间**保持不变**——
变的是印在纸上的符号（那是每张自己的图形语言）。
末尾的「自定义槽位」列出哪些常量允许被换掉、换的时候要守什么。

---

## 1. 变量层：三个常量 + 一个槽

```css
:root {
  --paper: #e9e3d5;      /* 米白纸 */
  --ink: #57524a;        /* 主墨 */
  --ink-faint: #8d867a;  /* 档案微字墨 */
  --accent: #2f66b8;     /* ← 色锚：唯一按张变化的槽，按内容改名改值 */
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  background: #b8b0a0;   /* 桌面底色，衬托纸边 */
  font-family: "Courier New", "Courier", "Songti SC", "STSong", serif;
}
```

色锚槽在各张里按内容取名：`--sky #2f66b8`、`--wheat #cf9a33`、`--signal #9e3b28`、
`--lake #3878a8`、`--amber #e8a72e`。取名本身是设计动作——它逼你说清这块色是什么。

**字体栈全站一个，禁用斜体。** 微字 9px / letter-spacing .16em / line-height 2.1。

---

## 2. 纸：受光 + 噪点 + 斑驳

纸是三层叠出来的，缺一层就假。

```css
.poster {
  position: relative;
  width: 1400px; height: 928px;   /* ← 画幅：与原片同比例 */
  margin: 0 auto;
  overflow: hidden;
  background:
    radial-gradient(110% 90% at 26% 20%, rgba(255,252,240,0.42), transparent 62%),  /* 主光 */
    radial-gradient(70% 60% at 88% 78%, rgba(190,178,152,0.28), transparent 70%),   /* 暗角 */
    radial-gradient(45% 45% at 10% 92%, rgba(196,186,162,0.24), transparent 70%),
    var(--paper);
}
```

**噪点层**——逐字节照抄，别调参数（bf 0.9 / 2 octaves / opacity .07 / multiply / 压在最上层）：

```css
.poster::before {
  content: ""; position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E");
  opacity: 0.07;
  mix-blend-mode: multiply;
  pointer-events: none;
  z-index: 9;
}
```

**斑驳层**——三团低透明暖灰，位置每张微调，结构不变：

```css
.mottle {
  position: absolute; inset: 0; z-index: 1;
  background:
    radial-gradient(200px 130px at 68% 22%, rgba(184,170,140,0.12), transparent 70%),
    radial-gradient(240px 160px at 18% 66%, rgba(184,170,140,0.10), transparent 70%),
    radial-gradient(130px 100px at 86% 88%, rgba(170,155,125,0.09), transparent 70%);
}
```

**暗角（可选）**——只在原片本身有暗角语义时加（如隔着车窗拍）：

```css
.vignette {
  position: absolute; inset: 0; z-index: 6;
  background:
    radial-gradient(58% 52% at 0% 0%,     rgba(88,82,72,0.16), transparent 72%),
    radial-gradient(58% 52% at 100% 0%,   rgba(88,82,72,0.15), transparent 72%),
    radial-gradient(58% 52% at 0% 100%,   rgba(88,82,72,0.13), transparent 72%),
    radial-gradient(58% 52% at 100% 100%, rgba(88,82,72,0.14), transparent 72%);
  mix-blend-mode: multiply; pointer-events: none;
}
```

**纸就是纸。** 照片的氛围通过纸上印的符号表达，不要把整张纸染成场景色
（深蓝夜纸试过，被否）。纸也可以直接充当留白的"场地"——尘土广场、天空，都是纸本身。

### 分层顺序（数字可调，顺序不可乱）

```
1   mottle 斑驳
2-5 内容层（远→近，每层一个独立 <svg>，各自 mix-blend-mode: multiply）
6   vignette 暗角（可选）
7   档案微字
9   噪点（永远在最上）
```

---

## 3. 色锚

一张海报**一个**高饱和色。它是全张唯一的"事件"。

### 四条硬指标（定稿前脚本实测，别靠眼估）

1. **占画布 0.8–2.5%**
2. **缩略图下必须可见**——必须是实在的色块，不能只是几个小点
3. **绝不用 pale / muted / faded / pastel / low-saturation / near-monochrome 的做法削弱它**。
   纸、灰度影像、次级墨可以压，色锚不行。
   （multiply 上纸是印刷语言，不算削弱：`#cf9a33` multiply 后实测仍是 S=73%）
4. **只能有一个主色相**。次色相仅在支撑主体、且不让整张变商业彩色时才允许。
   用户明确点名两个色彩元素时可以破例双色。

色锚可以直接**是主体**（有色的树/果/剪影/几何切块/窗/图版），
这优于"灰主体 + 一个彩色套准点"的做法。

### 两条实测教训（几何面积会骗人）

- **渗边会把面积撑大**：几何算出实色 2.0%，成品实测 3.18%——渐变 stop 0.70–0.87 那段
  也保住了高饱和，turbulence 位移还把形状撑大了。
  **别信几何面积，信 `sat>0.35` 的像素统计**，按实测反推系数重算。
- **细线做色锚，饱和度会被抗锯齿稀释**：本色 S=75% 的红，画成 2–4px 半透明细线后
  成品实测只剩 S=52%（边缘像素混进纸色）。加粗到 3.4–6.4px、opacity 提到 0.66–0.98
  才回到 61%。**色锚是细碎符号时，必须留出被稀释的余量。**

### 常用色板（按照片轮换）

钴蓝 `#2a4d9b` / 天蓝 `#2f66b8` / 信号红 `#d93a25` / 陶红 `#9e3b28` /
琥珀 `#f59e1d` / 麦金 `#cf9a33` / 薄荷绿 `#2aa87a` / 湖蓝 `#3878a8`

---

## 4. 档案系统

海报**不带任何文案短句**。只带真实拍摄参数——这是这套语言与文艺海报的分界线。

```css
.archive {
  position: absolute; left: 116px; bottom: 76px;
  font-size: 9px; line-height: 2.1; letter-spacing: 0.16em;
  color: var(--ink-faint); z-index: 7;
}
.index-no {
  position: absolute; right: 116px; top: 84px;
  font-size: 9px; letter-spacing: 0.3em; color: var(--ink-faint); z-index: 7;
}
.reg-mark {
  position: absolute; left: 118px; top: 84px;
  font-size: 11px; color: var(--ink-faint); opacity: 0.7; z-index: 7;
}
```

**数码机身模板：**

```html
<div class="archive">
  DSC00844 · SONY ILCE-6700<br>
  22 JUN 2026 · 13:09 · f/11 · 1/640 · ISO 200<br>
  50.7401° N / 0.2058° E · SEVEN SISTERS
</div>
<div class="index-no">NO. 023</div>
<div class="reg-mark">+</div>
```

**胶片扫描件模板：**

```html
<div class="archive">
  IMG_5222 · 35MM COLOUR NEGATIVE<br>
  SCANNED 10 JUL 2026 · NORITSU EZ CONTROLLER<br>
  GPS —
</div>
```

规则：

- 分隔符恒为 ` · `，全大写，无句号
- 无 GPS 写 `GPS —`
- **地名只写可从照片或用户陈述确证的**（TOWER BRIDGE、HYDE PARK、SEVEN SISTERS），不猜
- 编号三位补零，与作品序号一致；重制版沿用原编号
- 特殊符号用 HTML 实体：`&#916; 378 PX`
- **时区**：换算成拍摄地当地时间。以伦敦为例，夏令时（BST）只在
  **3 月最后一个周日 – 10 月最后一个周日**之间，此区间内 EXIF UTC +1 小时；
  区间外是 GMT，与 UTC 相同、**不加**

---

## 5. 反向约束（Hard Avoids，定稿前逐条对表）

- full-bleed 场景铺满
- 商业标题层级
- 产品广告版式 · logo · CTA
- 干净数字 UI 白底
- 光泽纸 mockup 与厚投影
- 3D · cinematic lighting · 硬阴影 · 景深 · 霓虹 · 赛博朋克
- 可爱卡通 · 二次元 · 时尚大片戏剧感
- 过多物件 · 贴纸 · 颜色 · 说明文字 · 装饰纹理
- 高清商业写实
- 长段干净可读的文字块

**量化线**：纸读作 70–90%，主体团块 8–25%。横版全幅地景类按外框算会超标
（实测某张外框 32%），按**实际着墨**算才准（同张实际 12.7%，纸约 87%）。
判据以实际着墨为准，但外框超标时要回头确认稀疏度够、纸感还在。

---

## 6. 自定义槽位

默认值是这套语言的原点。要换，先读"换的时候守什么"。

| 槽位 | 默认 | 可换成 | 换的时候守什么 |
|---|---|---|---|
| **画幅** | 与原片同比例（横竖都跟原片） | 任意比例；zine 原版偏爱竖版 3:5 | 一旦不跟原片，就要重新决定裁掉什么——裁切本身是蒸馏动作，要说明理由 |
| **字体** | `"Courier New","Courier","Songti SC","STSong",serif` | 任何等宽或衬线栈；档案感来自等宽 | **全站一个字体栈、禁用斜体**。这两条不放开——多字体会立刻读成商业版式 |
| **纸色** | 米白 `#e9e3d5` | 其他纸感底色（牛皮、灰蓝、旧绿） | 氛围优先进符号，不进纸。整张染成场景色 = 回到"再现" |
| **色锚色板** | 按照片轮换（见 §3） | 用户指定的品牌色或固定色板 | 四条硬指标一条都不放宽，尤其第 3 条（绝不削弱） |
| **档案微字** | 三行真实拍摄参数 | 其他元信息格式；或加一句短诗（回到 zine 原版做法） | 若保留"档案"路线，**参数必须真实**，宁可写 `GPS —` 也不编 |
| **编号系统** | `NO. XXX` + 左上 `+` 套准符 | 换前缀（`PL. 07`、`FIG. 12`）、改位置、或整个关掉 | 关掉套准符会掉一层印刷感；改前缀时保持三位补零的节奏 |

**不可自定义的**（换掉就不是这套语言了）：噪点层参数、multiply 上纸、
"不做材质模拟"这条铁律、色锚的四条硬指标、反向约束清单。
