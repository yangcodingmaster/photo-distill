# CLAUDE.md

本仓库是一个 **skill**：把一张照片蒸馏成极简 zine 纸质海报——手写 HTML/CSS/SVG 绘制、
无头 Chrome 导出 PNG。不用图像生成模型，成品里没有照片像素。

This repository is a **skill** for distilling a photograph into a minimal zine-style
paper poster — hand-written HTML/CSS/SVG, no image-generation model.

## 先读这个 / Read this first

**[SKILL.md](SKILL.md)** —— 方法论、工作流、硬性规则。接到任何海报任务前先完整读一遍；
其余文件按 SKILL.md §五 的索引按需加载。若本仓库已作为 skill 安装
（`~/.claude/skills/photo-distill`），触发时会自动加载 SKILL.md，无需重复读。

## 四条硬约束（完整版在 [AGENTS.md](AGENTS.md)，两处同义）

0. **开工自检，实测别"以为"**：能渲染吗？**能看见渲染结果吗**（检验：说出画面里三个
   东西）？能跑 Python + PIL 吗？看不见 → 走 SKILL.md 的**盲画协议**：
   首版立刻交付，此后只按用户反馈改，自发迭代次数为零
1. **一轮自查，然后必须停**：首版后有且只有一轮自查，未经用户输入连改两版＝违反协议；
   每次交付带图、一句话说明、一个明确的问题
2. **绝不采轮廓**：采样清单就是绘制清单；一道边界只要一个 y 值
3. **数字脚本算、颜色采出来**：色值绝不凭印象编；四项定稿指标是出厂检验不是创作目标，
   用户说行之后才跑

## 本仓库的日常约定

- 改手艺规则 → 改 `references/`，SKILL.md 只留主流程；三个入口
  （SKILL.md / AGENTS.md / CLAUDE.md）不复制正文
- `examples/` 的图片是作者的摄影作品，版权归作者，勿转用
- 中英 README 逐节对齐，改一份必须同步另一份
