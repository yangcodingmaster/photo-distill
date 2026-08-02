# Photo Distill · 照片蒸馏

[English](README.md) | **简体中文**

一个 Claude Code skill（Codex 用户经 [AGENTS.md](AGENTS.md) 同样可用）：
把你拍的照片蒸馏成极简 zine 纸质海报——手写 HTML/CSS/SVG、无头 Chrome 渲染。
不用图像生成模型，成品里没有一个照片像素。

## 视觉设计

海报保留的：

- 米白平面，画幅与原片同比例，或者自定义比例
- 整张 70–90% 读作纸；墨只落在配得上的地方
- 两三个印刷符号，蒸馏自**你**点名的元素——其余全部丢掉
- 一个高饱和色锚，占画布 0.8–2.5%，脚本实测把关
- 手撕柔边、套印错位、印刷颗粒——油墨吃进纸里的样子
- 一行真实拍摄参数（文件名、机身、曝光、日期、GPS）

避开的：full-bleed 场景铺满、cinematic 打光、3D、厚投影、装饰纹理、
干净的数字 UI，以及任何可读的口号或文案。

## 示例

左边是照片，右边是生成的海报。每对的蒸馏说明见 [examples/](examples/)。

| 原片 | 海报 |
|---|---|
| ![](examples/04b-two-kids-original.jpg) | ![](examples/04b-two-kids-poster.jpg) |
| ![](examples/09-lamp-original.jpg) | ![](examples/09-lamp-poster.jpg) |
| ![](examples/20-blossoms-original.jpg) | ![](examples/20-blossoms-poster.jpg) |
| ![](examples/22-aircraft-original.jpg) | ![](examples/22-aircraft-poster.jpg) |
| ![](examples/23-sevensisters-original.jpg) | ![](examples/23-sevensisters-poster.jpg) |
| ![](examples/24-shard-original.jpg) | ![](examples/24-shard-poster.jpg) |
| ![](examples/25-primrose-original.jpg) | ![](examples/25-primrose-poster.jpg) |
| ![](examples/26-window-original.jpg) | ![](examples/26-window-poster.jpg) |

## 安装

```bash
git clone https://github.com/yangcodingmaster/photo-distill.git
ln -s "$(pwd)/photo-distill" ~/.claude/skills/photo-distill
```

软链接之后，每个 Claude Code 会话都能触发这个 skill。
**Codex 用户**：把 agent 指到这个文件夹即可——它会读根目录的
[AGENTS.md](AGENTS.md) 自己找到路，无需其他配置。

## 怎么用

**第一步——丢进一张照片，点名两三个你最在意的元素。** 这句话就是完整的需求：

> 把这张照片做成海报。我想突出窗户的轮廓、外面的绿，和浅浅的渐变光。

你没点名的东西一律不采样、不绘制——点得少，海报更抽象；点得多，海报更具象。
不想选的话直说，skill 会只问你一个问题，或者替你挑。

**第二步——大约五分钟后第一张图就到你手上。** 用大白话反馈就行：

> 黑的那块太重了，读起来像山。

每处修改约 30 秒重新出图。你全程不用碰代码。

**第三步——你说行了。** 这时 skill 才用脚本核验四项印刷指标
（色锚面积、着墨率、缩略图可见性、色相集中度），导出 2 倍 PNG，提交存档。

想换默认值时开口即可，六个槽位可自定义——画幅、字体、纸色、色锚色板、
档案微字、编号。细节见 [references/design-system.md](references/design-system.md)。

## 产出

- `poster-XX-name.html`——自足的本地文件，双击即开，零依赖
- 定稿海报的 2 倍 PNG
- 纸面上一行你照片的真实参数——绝不编造

## 仓库结构

```
SKILL.md              方法论、工作流、硬性规则
AGENTS.md             Codex 及其他 agent 的入口
references/           设计系统 · SVG 滤镜库 · 手艺铁律 · 生产管线
assets/template.html  每张新海报的起步骨架
examples/             八对原片与成品对照
```

## 许可

方法与代码随意使用。照片版权归作者所有——请勿转用图片。
