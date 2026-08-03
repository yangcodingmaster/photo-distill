# Run Log · 运行日志模板

**何时必填**：在非本机环境交付海报时（Codex、CI、他人机器——任何用户无法直接看到你
工作过程的场合），定稿时随成品附上这份 6 行日志。
本机 Claude Code 会话可豁免——git commit message 本身就是设计日志。

**为什么**：用户报告"出图不对"时，这 6 行能立刻判断问题出在哪一环
（看不见？没采样？没停？），而不是靠转述反推。

```text
RUN LOG
- env check   : render=OK/FAIL   vision=OK/FAIL(FAIL→已走盲画协议)   PIL=OK/FAIL
- harness     : <实际模型与运行环境；不确定就写"不确定"，不许编>
- elements    : <用户点名的两三个元素，原话>
- sampled     : <关键采样值：色 H/S/V、分界 y、位置——证明颜色不是编的>
- deliveries  : <交付了几版；自发迭代必须为 0（协议条款 1）>
- finalize    : <finalize_poster.py 的结果：DELIVERY PASS / WAIVED 了哪些（用户确认过的偏离）>
```

规则：

- **不许声称无法验证的模型名或工具名**——写不出真的，就写"不确定"
- `vision=FAIL` 却没走盲画协议、或 `deliveries` 里有自发迭代，都是协议违规，
  日志的作用就是让这类违规无处藏身
- 日志是给人读的诊断数据，6 行封顶，不许扩写成表格
