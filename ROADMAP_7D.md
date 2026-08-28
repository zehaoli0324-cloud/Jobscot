# ROADMAP 7D — 牛客 / LeetCode 风格冲刺版

> 面试官已明确说明 Coding 类似牛客 / 力扣，因此本路线调整为：**Coding 约 75%，Eval/Data/System 约 25%。**
>
> 每天默认 6–8 小时；如果只有 3–4 小时，只做标记为 P0 的内容。

## 总原则

每个算法模式都必须经历：

**Learn → 小例子手推 → Closed-book → Timed Problem → 自测 → 评分 → Variant**

只有：

- 不看答案；
- 不依赖 Hint 2/3；
- 代码主逻辑正确；
- 能说清复杂度和 invariant；
- 同模式连续两次 ≥8/10；

才记为 `MASTERED`。

题库以 `LEETCODE_CORE_15.md` 为准。不要擅自扩 Hot100。

---

# Day 1 — Python 现场 Coding + 四道基础反射

## Learn（60–90 min）

只补面试直接需要的 Python：

- list / dict / set / tuple；
- `enumerate / zip / sorted`；
- `Counter / defaultdict / deque`；
- 函数、循环、条件、异常；
- 链表节点的基本写法；
- 时间/空间复杂度怎么口述。

## P0 Practice

按顺序做：

1. LC1 模式 — HashMap；
2. LC20 模式 — Stack；
3. LC165 模式 — String parsing；
4. LC206 模式 — Linked List。

前两题 15 min，后两题 15–20 min。

## 每题固定动作

- 先用 2–3 句话讲思路；
- 写完整 Python；
- 自己给 2 个测试；
- 说复杂度；
- 说明最容易错的边界。

## Exit Gate

4 题至少 3 题 ≥8，且 LC206 必须能独立写。

---

# Day 2 — 高频数组：Sliding Window / Interval / Binary Search

## Learn（90 min）

只学三个 invariant：

### Sliding Window
- 当前窗口代表什么；
- 何时移动 left；
- 为什么 left 不回退。

### Interval
- 为什么先排序；
- 当前 merged interval 代表什么。

### Binary Search
- 搜索区间定义；
- 循环条件；
- 每次为什么一定缩小。

## P0 Practice

1. LC3 模式 — 25 min；
2. LC56 模式 — 25 min；
3. LC33 模式 — 30 min。

## Variant

只从下面选 1 道迁移验证：

- LC153 模式；或
- LC121 模式。

不要两道都刷。

## Exit Gate

LC3 必须 ≥8；LC56/LC33 至少一题 ≥8，另一题 ≥7。

---

# Day 3 — Tree / Grid / BFS-DFS

## Learn（60–90 min）

掌握：

- queue BFS；
- recursion / explicit stack DFS；
- visited 的时机；
- 二叉树 level boundary；
- grid 四方向遍历。

## P0 Practice

1. LC102 模式 — 20 min；
2. LC200 模式 — 30 min。

LC200 完成后必须口述另一种 BFS/DFS 实现。

## Variant

二选一：

- LC112 路径总和；
- 岛屿面积类 grid variant。

## Eval 插针（45 min）

做 `CORE_12.md` 中 B1 evaluator coding。

目的不是抢算法时间，而是保持岗位相关 coding 优势。

## Exit Gate

LC200 ≥8；树/图遍历不能再因模板语法卡住；B1 ≥7。

---

# Day 4 — Heap + LRU + 链表实现能力

## Learn（90 min）

### Heap
- min-heap 为什么适合保留 Top-K；
- O(n log k)；
- Python `heapq` 基本 API。

### LRU
- 为什么需要 HashMap + Doubly Linked List；
- head/tail sentinel；
- move-to-front / remove / insert 的职责。

## P0 Practice

1. LC215 模式 — 30 min；
2. LC146 模式 — 40–45 min。

## 链表强化

根据 Day1 LC206 表现：

- 如果 LC206 已 MASTERED：尝试 LC25 的分段框架；
- 如果 LC206 仍不稳：不碰 LC25，先做同模式链表变式。

## Eval 插针（60 min）

做 B2 Judge Aggregation 或 B3 batch evaluator 二选一。

## Exit Gate

LC215 ≥8；LC146 ≥7.5；能清楚解释 LRU 的 O(1) 从哪里来。

---

# Day 5 — 字节公开面经强化题

这一天才引入少量更难模式，不提前学一堆 DP。

## Practice 1 — LC221 最大正方形

Learn 20–30 min：只理解这个 DP 状态，不系统学 DP 大全。

Timed：30 min。

## Practice 2 — LC32 最长有效括号

先尝试 30 min；失败后再进入 Stack mini-lesson。

## Practice 3 — sqrt(x)

分别实现：

- binary search；
- Newton iteration。

目标不是背公式，而是能解释停止条件和精度。

## 岗位设计题（60–90 min）

做 C1：如何可信比较两个医疗 LLM。

## Exit Gate

三道 Coding 强化题至少 2 道 ≥7.5；C1 ≥8。

---

# Day 6 — Mixed Interview：陌生题面迁移

停止按专题顺序刷。

## Mock Coding A（45 min）

DeepSeek 从已学模式中随机出 1 道变式，隐藏 LeetCode 编号/标签。

## Mock Coding B（45 min）

再随机 1 道不同模式。

## Stretch（45 min）

如果基础链表稳定，做 LC25；否则随机回测最弱模式。

## Eval/System（90 min）

二选一主练，另一题只做 10 min 框架：

- C2 Benchmark shortcut/leakage；
- D1 100 万回答 × 3 Judge。

## Exit Gate

两道陌生题面 Coding 平均 ≥7.5，且至少一题 ≥8。

如果模式识别仍不稳定，Day7 不学新题，只回测弱项。

---

# Day 7 — 两轮真实 60 分钟技术面

今天不学习新算法。

## Mock 1

- 5 min：项目/自我介绍；
- 35 min：一题牛客/LeetCode 风格 Coding；
- 15 min：Eval/Data/System 追问；
- 5 min：代码复杂度和边界追问。

结束只记录：

- 最大 Coding 风险 1 个；
- 最大表达风险 1 个。

## Repair（90 min）

只补最大 Coding 风险。

## Mock 2

同结构，再来一轮不同题面。

## 最终通过线

- Easy：基本 15 min 内完成；
- 常见 Medium：25–35 min 内有正确主解；
- 15 个核心中 Level1 全会、Level2 至少 6/7 PASS；
- 近期字节强化模式至少 2 个能完成；
- Eval/System 不成为短板；
- Mock 2 Coding ≥7.5，整体 ≥8。

---

# 明确不做

一周内不系统刷：

- Hot100 全套；
- DP 大全；
- 图最短路大全；
- 线段树 / 红黑树；
- 冷门数学竞赛；
- 大量 LeetCode Hard。

LC25 是唯一保留的 Hard 级 stretch，因为它是字节长期代表性高频链表题；如果时间不够，可以放弃它而不影响整体计划。

**原则始终是：少而精，先把正常 Medium 做稳。**