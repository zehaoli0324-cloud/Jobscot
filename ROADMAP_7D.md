# ROADMAP 7D — 循序渐进训练路径

> 默认每天 6–8 小时。若只有 3–4 小时，保留“核心学习 + 核心题 + 复盘”，删掉第二个变式，不删测试和复盘。

## 总体升级规则

每个能力都经历 4 层：

1. **理解**：能用自己的话说出模式、invariant、复杂度。
2. **模仿**：看过一次参考框架后，关掉答案重新写。
3. **迁移**：换医疗/评测语境后仍能识别同一模式。
4. **面试**：限时、无提示、可运行、能自测、能扛追问。

只有第 4 层 ≥8/10 才算“会”。

---

# Day 1 — Python 基础 + 数据处理基本功

## 今日目标

把“知道 Python”变成“现场不会因语法和容器卡住”。

## Learn（90 min）

只学：

- list / tuple / dict / set；
- membership、插入、查找的典型复杂度；
- `enumerate` / `zip` / `sorted(key=...)`；
- `Counter` / `defaultdict`；
- list/dict/set comprehension；
- 函数、异常、空输入；
- JSON / JSONL 基本读写；
- 去重、分组、排序、聚合。

不要学 class 花活、装饰器、metaclass。

## Closed-book Recall（30 min）

不查资料手写：

- 按 key 分组；
- tuple 作为 dict key；
- 去重但保序；
- 按字段排序；
- Counter 统计频次；
- 读取 JSONL 并逐行处理。

## Practice 1（45 min）

做 **A1 去重 + 最新记录**。

要求：
- 25 min 内完成；
- 自己写 3 个测试；
- 解释 O(n) 与最终排序的复杂度；
- 追问：数据不能一次进内存怎么办？

## Practice 2（60 min）

做 **B1 医疗问答 Evaluator**。

先只实现 micro precision / recall / F1，再补：
- empty pred；
- duplicate diagnosis；
- missing field；
- empty gold；
- malformed input 的明确策略。

## Exit Gate

必须满足：
- A1 ≥8/10；
- B1 ≥7/10；
- `dict/set/Counter/defaultdict/sorted` 不需要查语法。

未通过：Day 2 前先做同模式 1 个变式，不增加新知识。

---

# Day 2 — 高频算法模式，不刷题海

## 今日目标

建立“看到题 → 识别模式”的反射。

## Learn（120 min）

只学 5 个模式：

1. HashMap / Set；
2. Sliding Window；
3. Heap / Top-K；
4. Queue + BFS / Topological Sort；
5. LRU = HashMap + Doubly Linked List。

每个模式只回答 4 个问题：
- 什么时候用？
- invariant 是什么？
- 复杂度是什么？
- 最常见 bug 是什么？

## Practice（3–4 h）

依次：

- **A2 最长无重复窗口** — 30 min；
- **A3 Top-K 错误类型** — 25 min；
- **A4 任务依赖/拓扑排序** — 35 min；
- **A5 LRU Cache** — 45 min。

每题结束必须：
1. 自测至少 2 个 edge cases；
2. 解释复杂度；
3. 说出若数据规模扩大 1000 倍会发生什么；
4. 关掉代码 20 分钟后重写关键部分。

## Exit Gate

- A2/A3/A4 中至少 3 个 ≥8/10；
- A5 ≥7/10；
- 能在 30 秒内说出题目属于哪个模式以及原因。

不要因为 LRU 卡住就去刷 20 道链表题。

---

# Day 3 — Evaluator Coding：把它练成强项

## 今日目标

面试官一旦进入评测代码，你从“应付”转成“有工程判断”。

## Learn（90 min）

掌握：

- TP / FP / FN；
- micro vs macro；
- denominator 为 0 的定义；
- schema validation；
- missing / duplicate / malformed input；
- deterministic evaluator；
- unit test / regression test；
- aggregate score 为什么可能掩盖高风险 slice。

## Practice 1（60 min）

**B1 二刷**，换 schema，不看旧代码。

增加：
- 多样本；
- 诊断项大小写/别名是否标准化的策略说明；
- per-slice metric。

## Practice 2（75 min）

**B2 Judge Aggregation**。

至少实现：
- aggregate score；
- disagreement flag；
- missing judge；
- out-of-range score 报错；
- 4 个测试。

追问：
- mean / median / majority vote 各有什么假设？
- judge drift 怎么发现？
- judge 自身需要怎样校准？

## Mini Design（45 min）

回答：为什么医疗评测不能只给一个总平均分？

要求主动提：高风险 slice、安全红线、置信区间/不确定性、case mix。

## Exit Gate

B1、B2 **都 ≥8/10**。否则不进入 Day 4 的复杂工程题。

---

# Day 4 — Async + Retry + Resume：工程生存线

## 今日目标

能写一个“小而正确”的可恢复 batch evaluator，并解释为什么工业系统要这样设计。

## Learn（120 min）

只学：

- `async` / `await`；
- semaphore 控制并发；
- timeout；
- retry + exponential backoff；
- rate limit；
- sample-level status；
- checkpoint；
- cache；
- idempotency key；
- append-only result / upsert 的取舍；
- resume。

核心问题：**失败后能不能从断点恢复，而不是从头重跑？**

## Guided Build（60 min）

先自己写最小版本：

`evaluate_one -> bounded concurrency -> gather results`

然后逐层加入：

`timeout -> retry -> state -> resume -> cache`

每加一层都解释它解决哪种 failure mode。

## Timed Practice（90 min）

做 **B3 可恢复 Batch Evaluation**，从空白开始，限时 45–60 min。

必须能回答：
- worker/请求失败怎么办？
- retry 会不会重复收费？
- 如何做到 idempotent？
- 如何跳过成功样本？
- 怎样记录 error type？

## Exit Gate

B3 ≥8/10；能不用术语堆砌，画出 sample 从 pending → running → success/failed 的状态流。

---

# Day 5 — Eval / Benchmark：把已有优势变成标准面试答案

## 今日目标

不是讲很多概念，而是形成一个固定的“可信评测骨架”。

## Learn（90 min）

固定七步：

1. Task taxonomy / slice；
2. 独立 truth / evidence；
3. Metric / rubric；
4. Judge calibration + human adjudication；
5. Safety / high-risk errors；
6. Leakage / shortcut / naive baseline / perturbation；
7. Statistics + held-out regression。

## Practice 1（75 min）

**C1：模型 A vs B 谁更适合医疗问答？**

第一次 20 min 答；根据追问重构；第二次压到 12–15 min。

## Practice 2（75 min）

**C2：如何证明 Benchmark 没有 shortcut？**

必须区分：
- contamination = 测试内容被见过；
- shortcut = 即使没见过，也能利用非目标信号解题。

## Stress Questions（45 min）

连续回答：
- truth 如果来自 LLM judge，哪里循环了？
- 为什么平均分会掩盖医疗风险？
- judge 与专家不一致怎么办？
- benchmark 分数涨了，为什么不能立刻说模型变强？

## Exit Gate

C1、C2 均 ≥8/10，且每题可在 15 min 内完成主干。

---

# Day 6 — System Design：从单机 evaluator 到评测平台

## 今日目标

形成稳定的系统设计顺序，而不是随机报技术名词。

## Learn（90 min）

固定顺序：

**Requirements → Data model → Task flow → Concurrency → Failure recovery → Idempotency → Provenance → Observability → Cost → Trade-offs**

## Practice 1（90 min）

**D1：100 万回答 × 3 Judge**。

先画最小流：

`dataset -> task queue -> workers -> judge API -> result store -> aggregation/report`

然后逐个处理：rate limit、timeout、retry、cache、checkpoint、versioning、成本。

## Practice 2（90 min）

**D2：每周新模型，怎么判断真的变好？**

主动分成：
- frozen regression suite；
- dynamic challenge set；
- safety gate；
- slice metrics；
- significance / CI；
- failure registry；
- release gate / rollback。

## Coding Refresh（60 min）

随机抽 A2/A4/B2/B3 中一题，30 min 无提示写。

## Exit Gate

D1/D2 ≥8/10，随机 Coding ≥7.5/10。

---

# Day 7 — 全真模拟 + 最小修补

## 今日目标

停止学习新知识，只验证“面试状态”。

## Mock 1（60 min）

严格按 `MOCK_INTERVIEW.md`：
- 5 min 项目/背景；
- 30 min coding；
- 15 min eval/system deep dive；
- 10 min 追问。

结束后只记录：
- 1 个致命弱点；
- 1 个次要弱点；
- 1 个优势。

## Repair（90–120 min）

只补 Mock 1 暴露出的**最致命一个问题**。

不能因为错了一道滑窗题就去学动态规划。

## Mock 2（60 min）

换题面但不换能力模式。

## Final Gate

满足任意一个条件即可停止：

- Mock 2 总评 ≥8/10；或
- Coding ≥7.5、Evaluator/Eval/System 中至少两个 ≥8.5，且无致命 correctness/failure-recovery 问题。

如果某一项仍 <7：面试前只练这一项，不再横向扩展。

---

# 这一周明确不学

- LeetCode Hard；
- 复杂 DP；
- 红黑树、线段树等竞赛数据结构；
- 深入 C++/Go；
- 复杂分布式一致性理论；
- 医学百科背诵；
- 大模型训练公式大全。

除非真实面试反馈明确出现，否则不扩范围。