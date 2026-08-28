# Xiaohe LLM Eval Interview Bootcamp

> 7 天定向训练：**牛客 / LeetCode 风格 Coding 为主，LLM Eval / Data Engineering 为辅。**
>
> 目标不是刷很多题，而是让正常 Easy / Medium 不再淘汰你，再用 Eval / Benchmark / 医疗领域能力拉开差距。

## 训练权重

- **Algorithm Coding：约 75%**
- **Evaluator / Eval / Data / System：约 25%**

面试方已明确说明技术面需要线上写代码，题型比较类似牛客 / 力扣。因此算法主线优先级高于岗位场景题。

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
- 1 道代表性链表 stretch。

**不刷 Hot100 全套。**

岗位能力题保留在 `CORE_12.md`，每约 3 道 Coding 穿插 1 道 Evaluator / Eval / System。

---

# 最推荐的使用方式：DeepSeek V2 单题教练

先看：[`START_DEEPSEEK.md`](./START_DEEPSEEK.md)

把仓库链接 + 启动 Prompt 发给 DeepSeek，它必须按 [`DEEPSEEK_TUTOR.md`](./DEEPSEEK_TUTOR.md) V2 执行：

**一次一道题 → 你提交 → 判代码 → 最小反例 → 你自己 debug → 严格评分 → 最小教学 → 变式/延迟复测。**

在你提交前，它不会告诉你：

- LeetCode 编号；
- 原题名称；
- 算法标签；
- 关键数据结构；
- 标准答案。

### V2 的关键升级

1. **Counterexample-first**：代码错了先给最小失败输入，不直接贴修法。
2. **Hint ladder**：提示 1/2/3 分级，越强的提示越不能证明独立能力。
3. **Delayed mastery**：刚做对不算 MASTERED；隔至少 3 道题或下一次 session，无提示变式再 ≥8 才算掌握。
4. **Interleaving**：不连续刷同模式制造虚假熟练度。
5. **Retention retest**：已掌握模式会在后续 Mock 随机回测。
6. **Session state**：用 `SESSION_STATE.md` 在新对话恢复训练进度。

---

# 7 天路径

| Day | 主线 | 目标 |
|---|---|---|
| 1 | Python + HashMap/Stack/String/链表 | 基础题不因语法和指针挂掉 |
| 2 | Sliding Window / Interval / Binary Search | 建立高频数组题模式识别 |
| 3 | Tree + Grid BFS/DFS | 掌握树和二维遍历 |
| 4 | Heap / LRU / 链表实现 | 提升数据结构现场实现能力 |
| 5 | 字节风格强化 + Eval | DP/括号/sqrt + 岗位题 |
| 6 | Mixed Coding + Eval/System | 陌生题面迁移 |
| 7 | 两轮 60 分钟全真模拟 | 只补最后一个最大风险 |

详见 [`ROADMAP_7D.md`](./ROADMAP_7D.md)。

---

# 文件导航

- [`START_DEEPSEEK.md`](./START_DEEPSEEK.md)：**最先看。** 一段 Prompt 启动 DeepSeek。
- [`DEEPSEEK_TUTOR.md`](./DEEPSEEK_TUTOR.md)：V2 单题循环、调试、教学、延迟复测协议。
- [`SESSION_STATE.md`](./SESSION_STATE.md)：跨对话恢复训练状态。
- [`LEETCODE_CORE_15.md`](./LEETCODE_CORE_15.md)：15 道最小核心算法锚点。
- [`ROADMAP_7D.md`](./ROADMAP_7D.md)：7 天循序渐进训练表。
- [`DAILY_LOOP.md`](./DAILY_LOOP.md)：每天固定 Learn → Practice → Review 模板。
- [`PROGRESS.md`](./PROGRESS.md)：训练状态和错误记录。
- [`RUBRIC.md`](./RUBRIC.md)：严格评分 + 提示分数上限 + mastery 判据。
- [`CORE_12.md`](./CORE_12.md)：Evaluator / Eval / System 岗位能力题。
- [`LEARNING_NOTES.md`](./LEARNING_NOTES.md)：最小知识骨架。
- [`MOCK_INTERVIEW.md`](./MOCK_INTERVIEW.md)：Day 7 模拟协议。

---

# 最终通过线

面试前希望达到：

- Level 1 基础模式稳定；
- Level 2 高频 Medium 大部分至少 PASS；
- 关键模式经过**延迟无提示复测**后 MASTERED；
- 任意陌生常见 Medium 能先给 brute force，再逐步优化，而不是空白；
- Evaluator Coding 不成为短板；
- Eval/System 能在 15–20 分钟内形成结构；
- 至少一轮 60 分钟 Mock 达到整体 ≥8/10。

**目标不是成为算法竞赛选手，而是让 Coding 不再拥有一票否决权。**