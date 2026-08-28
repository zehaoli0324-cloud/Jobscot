# Xiaohe LLM Eval Interview Bootcamp

> 7 天定向训练：把 Coding 从“可能否决项”练到“稳定不拖后腿”，同时把 LLM Eval / Benchmark / Data Engineering 变成可面试表达、可现场实现的能力。

## 目标岗位

医疗大模型评测 / 数据工程师（研发-算法方向），以及相近的 LLM Eval / Benchmark / Data Engineer 岗位。

## 原则：少而精

只练 4 类核心能力：

1. **Python + 高频数据结构**：dict/set、sliding window、heap、BFS/拓扑、LRU。
2. **Evaluator + 数据处理 Coding**：指标、异常输入、Judge 聚合、batch evaluation。
3. **LLM Eval / Benchmark 设计**：truth、rubric、judge calibration、shortcut/leakage、regression。
4. **评测系统工程**：async、retry、rate limit、cache、checkpoint、idempotency、provenance。

不追求题量。**同一模式连续两次 ≥8/10 就停止刷该模式。**

## 7 天路径

| Day | 重点 | 结果 |
|---|---|---|
| 1 | Python 容器 + 数据处理基本功 | 能稳定写 A1 / B1 |
| 2 | 高频算法模式 | 掌握 A2 / A3 / A4；A5 至少理解并能写 |
| 3 | Evaluator | B1 / B2 独立实现并写 edge cases |
| 4 | Async + 可恢复评测 | B3 独立完成；解释 retry/idempotency |
| 5 | Eval / Benchmark | C1 / C2 15 分钟内结构化回答 |
| 6 | System Design | D1 / D2 能从 flow → failure → provenance → cost 展开 |
| 7 | 全真模拟 | 2 次 60 分钟技术面，定位最后 1–2 个弱点 |

详见 [`ROADMAP_7D.md`](./ROADMAP_7D.md)。

## 每天怎么练

固定循环：

**Learn → Closed-book Recall → Timed Coding/Design → Tests/追问 → Rubric → Error Log → Variant → Stop/Advance**

详见 [`DAILY_LOOP.md`](./DAILY_LOOP.md)。

## 文件

- [`ROADMAP_7D.md`](./ROADMAP_7D.md)：7 天逐日训练表。
- [`DAILY_LOOP.md`](./DAILY_LOOP.md)：每天可复用的学习+练习模板。
- [`CORE_12.md`](./CORE_12.md)：12 个能力锚点，不无限扩题。
- [`QUESTION_ENGINE.md`](./QUESTION_ENGINE.md)：给 GPT / Claude / Codex 的自适应出题协议。
- [`RUBRIC.md`](./RUBRIC.md)：严格评分标准。
- [`LEARNING_NOTES.md`](./LEARNING_NOTES.md)：只保留面试必须掌握的知识骨架。
- [`PROGRESS.md`](./PROGRESS.md)：训练记录与升级门槛。
- [`MOCK_INTERVIEW.md`](./MOCK_INTERVIEW.md)：Day 7 全真模拟规则。

## 给 Agent 的启动语句

直接把仓库链接给 Agent，然后说：

> 读取 README、ROADMAP_7D、QUESTION_ENGINE 和 PROGRESS。按当前 Day 开始训练。一次只给一个学习块或一道题；不要提前给答案。我的答案完成后按 RUBRIC 严格评分，并更新我应该进入的下一步。

## 最终通过线

面试前至少达到：

- Coding：5 个核心模式中 ≥4 个可在 25–35 分钟独立完成；
- Evaluator：B1/B2/B3 全部 ≥8/10；
- Eval：C1/C2 均能在 15 分钟内 ≥8/10；
- System：D1/D2 均能在 15–20 分钟内 ≥8/10；
- Mock：至少 1 次 60 分钟模拟总评为“稳定通过”。

**目标不是成为算法竞赛选手，而是让正常 Coding 题不再淘汰你，让 Eval / Benchmark / 医疗科研判断力决定结果。**