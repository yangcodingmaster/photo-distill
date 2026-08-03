# 生产管线 · Pipeline

从一张原片到一张 2x 成品 PNG。每个环节给两条路径：macOS 自带工具，和跨平台的 Python/PIL——
在 Codex 等非 macOS 环境里用后者。开工前先做 SKILL.md 的「开工自检」。

---

## 1. 读原片的事实

### 尺寸与比例（决定画布）

macOS 路径：

```bash
sips -g pixelWidth -g pixelHeight "原始照片/DSC00844.heic"
```

跨平台路径（PIL，Codex 等 Linux 沙箱用这个）：

```python
from PIL import Image
im = Image.open("photo.jpg")
print(im.size)          # (宽, 高)
```

画布按原片比例定，取一个方便的宽度（1200 / 1400），高度按比例算，**用脚本算**：

```bash
python3 -c "print(round(1400 * 2048 / 3089))"   # → 928
```

### EXIF

macOS 路径：

```bash
mdls -name kMDItemContentCreationDate \
     -name kMDItemLatitude -name kMDItemLongitude \
     -name kMDItemAcquisitionModel \
     -name kMDItemExposureTimeSeconds -name kMDItemFNumber -name kMDItemISOSpeed \
     "原始照片/DSC00844.heic"
```

跨平台路径（PIL）：

```python
from PIL import Image, ExifTags
ex = Image.open("photo.jpg").getexif()
for k, v in ex.items():
    print(ExifTags.TAGS.get(k, k), v)   # DateTime / Make / Model / ExposureTime…
# GPS 在 ex.get_ifd(ExifTags.IFD.GPSInfo) 里；没有就老实写 GPS —
```

⚠️ **时区**：`kMDItemContentCreationDate` 通常是 UTC。换算成拍摄地当地时间——
伦敦的夏令时（BST）只在 3 月最后一个周日至 10 月最后一个周日之间，
此区间内 +1 小时，区间外是 GMT，**不加**。别无脑 +1。

胶片扫描件没有这些——标扫描仪和扫描日期，GPS 写 `GPS —`。

---

## 2. 转格式（仅当需要采样像素时）

HEIC / HIF → JPG（macOS 路径）：

```bash
sips -s format jpeg "原始照片/IMG_3122.HEIC" --out "assets/IMG_3122.jpg"
```

非 macOS：装得上 `pillow-heif` 就用它读；装不上**别硬转**，直接请用户给一张 JPG。

### ⚠️ iPhone / HEIC 方向标签坑

`sips` 全程在"显示坐标系"工作、**汇报的尺寸不可信**；
Chrome 又会按 EXIF / eXIf 标签再转一次。两者叠加，采样坐标会整体错位或转 90°。

凡涉及裁剪 / 采样，先做**净化母图**：

1. 转 PNG
2. 用 Python 在 PNG chunk 级删掉 `eXIf` 块
3. 无头 Chrome 渲染，验证 `naturalWidth` / `naturalHeight` 与内容方向
4. 再据此裁剪

**别信 sips 的尺寸汇报。**

### 量透视用的裁窗对比

```bash
sips -c 400 600 --cropOffset 1800 200  "assets/x.jpg" --out "/tmp/left.jpg"
sips -c 400 600 --cropOffset 1800 2400 "assets/x.jpg" --out "/tmp/right.jpg"
```

两块**等高等宽**的窗口并排看，比在整图上目测准得多。

---

## 3. 采样脚本的约定

坐标、尺寸、亮度、面积——凡是进成品的数字，一律脚本算，绝不手写。

- 坐标保留**一位小数**
- 行尾挂溯源注释：`<!-- src y=1145 -->`
- 脚本把结果 **inline 进 HTML**（成品是纯静态 HTML，**不留 `<script>` 标签**）
- 脚本本身不必入库，但计算过程要在会话里展示出来

典型采样任务：亮度场网格降采样、色相突变行、亮团中心坐标、密度梯度、色锚面积统计。

### 采样原则：只采选中元素的关系量，一个脚本一次跑完

速度第一。采样范围由用户点名的两三个元素决定，**别把整张照片摸一遍**。
两次实测教训：① 一张海报写了 9 个探测脚本、一个脚本问一件事，拖掉十几分钟；
② 采了树梢轮廓的 141 个起伏点，结果把"一道横痕"画成了一座山——
**采样清单本身就是绘制清单**，多采的东西一定会多画。

每次只跑一个脚本，内容是：

- 尺寸、比例、画布高度（脚本算，别估）+ EXIF 全套，日期换算当地时间——永远要
- 每个选中元素的**关系量**：中心位置、聚类半径、逐格密度、一条分界 y、
  H/S/V 与高饱和占比（色锚预算用）
- **不采轮廓剖面**：一道边界只需要一个 y 值，不需要 141 个起伏点；
  物体的形状不进采样脚本
- 分段斜率（透视反推）只在选中元素含地面线/结构时才量

> **硬规则：色值必须来自采样像素。** 采样环境跑不通（没有 PIL、读不了图）时，
> 把 design-system 的默认色板拿给用户选，或请用户直接报颜色——**绝不凭印象编**。
> 实测教训：编出来的颜色第一版氛围必错，之后怎么改都是在错的基础上猜。

后面只在出意外时补测，不预防性采样。

色锚面积实测（定稿必做）：统计 `sat > 0.35` 的像素占比，与 0.8–2.5% 对照。

---

## 4. 自查与导出

海报源文件是纯本地 HTML，双击可开。自查用无头 Chrome 截图，**亲眼看**
（看不见就走 SKILL.md 的盲画协议，别装）。

macOS 路径：

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --screenshot="/tmp/check.png" --window-size=1400,928 \
  "file:///绝对路径/海报源文件/poster-24-name.html"
```

Linux / 沙箱路径（Codex 等；二进制名可能是 `chromium`、`chromium-browser` 或 `google-chrome`）：

```bash
chromium --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --screenshot=/tmp/check.png --window-size=1400,928 \
  "file:///绝对路径/poster-24-name.html"
```

哪个浏览器都找不到 → 别卡住：把 HTML 文件本体交给用户，请他双击打开、截图给你。

定稿导出 2 倍：

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 \
  --screenshot="输出成品/poster-24-name.png" --window-size=1400,928 \
  "file:///绝对路径/海报源文件/poster-24-name.html"
```

`--window-size` 必须与 `.poster` 的 width/height 完全一致，否则会截到桌面底色或裁掉边。

---

## 5. 目录与提交

```
原始照片/       用户原片（勿动）
海报源文件/     poster-*.html 全部源文件
assets/         转格式后的工作 JPG/PNG（纯绘制海报不需要）
输出成品/       2x 成品 PNG（与源文件一一对应）
CLAUDE.md       项目记忆
```

根目录只留 CLAUDE.md 和这几个文件夹，别往根目录散落 HTML。

**每张定稿即 git commit**，commit message 写这张的图形语法：

```
NO. 023 七姐妹外海：密度梯度，线自己出现
```

git log 于是成了一份设计日志——记录每张的语言，以及被否决的版本。

重制旧作时**新开 `-b` 后缀文件**（`poster-04-two-kids-b.html`），旧版一律保留，
海报上的编号沿用原编号。
