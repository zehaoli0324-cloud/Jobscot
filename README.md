# Xiaohe LLM Eval Interview Bootcamp

> 7 天定向训练：**牛客 / LeetCode 风格 Coding 为主，LLM Eval / Data Engineering 为辅。**
>
> 目标不是刷很多题，而是让正常 Easy / Medium 不再淘汰你，再用 Eval / Benchmark / 医疗领域能力拉开差距。

## 为什么这样改

面试方已明确说明技术面需要线上写代码，题型会比较类似牛客 / 力扣。因此训练权重调整为：

- **Algorithm Coding：约 75%**
- **Evaluator / Eval / Data / System：约 25%**

题目选择参考近期字节大模型/算法公开面经、小荷健康实习面经，以及 CodeTop/LeetcodeTop 字节长期高频统计。

## 最小核心范围

算法只保留 `LEETCODE_CORE_15.md` 中 15 个锚点：

- HashMap / Stack / String parsing；
- Linked List；
- Sliding Window；
- Interval；
- Tree BFS；
- Grid DFS/BFS；
- Heap / Top-K；
- Binary Search；
- LRU；
- 少量 DP / 括号栈 / 数值二分；
- 1 道字节代表性链表 stretch。

**不刷 Hot100 全套。** 同一模式连续两次 ≥8/10 就停止日常刷该模式。

岗位能力题仍保留在 `CORE_12.md`，用于每 3 道 Coding 穿插一次 Evaluator / Eval / System 训练。

---

# 最推荐的使用方式：把仓库交给 DeepSeek

先看：[`START_DEEPSEEK.md`](./START_DEEPSEEK.md)

你只需要把本仓库链接 + 里面那段启动 prompt 发给 DeepSeek。

DeepSeek 将按 [`DEEPSEEK_TUTOR.md`](./DEEPSEEK_TUTOR.md) 执行：

**一次一道题 → 你回答 → 严格评分 → 定位最致命错误 → 最小教学 → RETRY / VARIANT / ADVANCE。**

在你提交答案前，它不会告诉你：

- LeetCode 编号；
- 原题名称；
- 算法标签；
- 关键数据结构；
- 标准答案。

这样更接近真实面试。

---

# 7 天路径

| Day | 主线 | 目标 |
|---|---|---|
| 1 | Python + HashMap/Stack/String/链表 | 基础题不因语法和指针挂掉 |
| 2 | Sliding Window / Interval / Binary Search | 建立高频数组题模式识别 |
| 3 | Tree + Grid BFS/DFS | 掌握树和二维遍历 |
| 4 | Heap / LRU / 链表实现 | 提升数据结构现场实现能力 |
| 5 | 字节公开面经强化 + Eval | 最大正方形、最长有效括号、sqrt 等 |
| 6 | Mixed Coding + Eval/System | 陌生题面迁移 |
| 7 | 两轮 60 分钟全真模拟 | 只补最后一个最大风险 |

详见 [`ROADMAP_7D.md`](./ROADMAP_7D.md)。

---

# 文件导航

- [`START_DEEPSEEK.md`](./START_DEEPSEEK.md)：**最先看。** 复制一段话即可启动 DeepSeek 教练。
- [`DEEPSEEK_TUTOR.md`](./DEEPSEEK_TUTOR.md)：单题循环、评分、教学、自适应选题协议。
- [`LEETCODE_CORE_15.md`](./LEETCODE_CORE_15.md)：15 道最小核心算法锚点。
- [`ROADMAP_7D.md`](./ROADMAP_7D.md)：7 天循序渐进训练表。
- [`DAILY_LOOP.md`](./DAILY_LOOP.md)：每天固定 Learn → Practice → Review 模板。
- [`PROGRESS.md`](./PROGRESS.md)：训练状态和错误记录。
- [`RUBRIC.md`](./RUBRIC.md)：严格评分标准。
- [`CORE_12.md`](./CORE_12.md)：Evaluator / Eval / System 岗位能力题。
- [`LEARNING_NOTES.md`](./LEARNING_NOTES.md)：最小知识骨架。
- [`MOCK_INTERVIEW.md`](./MOCK_INTERVIEW.md)：Day 7 模拟协议。
- [`QUESTION_ENGINE.md`](./QUESTION_ENGINE.md)：旧版通用 Agent 出题协议；DeepSeek 训练优先以 `DEEPSEEK_TUTOR.md` 为准。

---

# 最终通过线

面试前希望达到：

- Level 1 四个基础模式全部稳定；
- Level 2 七个高频 Medium 至少 6 个 PASS；
- 任意陌生常见 Medium 能先给 brute force，再逐步优化，而不是空白；
- Evaluator Coding 不成为短板；
- Eval/System 设计能在 15–20 分钟内形成结构；
- 至少一轮 60 分钟 Mock 达到整体 ≥8/10。

**目标不是成为算法竞赛选手，而是让 Coding 不再拥有一票否决权。**