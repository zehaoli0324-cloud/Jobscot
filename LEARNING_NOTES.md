# LEARNING NOTES — 只记这些

> 不是教程，只是面试前必须能闭卷调用的知识骨架。不会的再查；会的不要继续扩展。

---

# 1. Python / 数据结构

## dict / set

典型用途：
- 去重；
- O(1) 平均查找；
- frequency map；
- key → state；
- tuple 作为复合 key。

必须知道：
- dict/set lookup / insert 平均 O(1)；
- list membership O(n)；
- `sorted(...)` O(n log n)。

## Counter / defaultdict

- `Counter`：计数；
- `defaultdict(list)`：分组；
- 面试时可以用标准库，但要知道底层仍是 hashmap 思维。

## Sliding Window

使用条件：
- 连续区间；
- 需要满足某个局部约束；
- 右指针扩张，左指针在约束破坏时收缩。

最重要的是说清 window invariant。

## Heap / Top-K

- 若需要所有元素排序：O(n log n)；
- 若只要 top-k，维护大小 k 的 heap：常见 O(n log k)。

## BFS / Topological Sort

拓扑排序核心：
- 建图；
- indegree；
- indegree=0 入队；
- 每弹一个节点降低后继 indegree；
- 最后处理节点数 < 总数 → 有环。

## LRU

O(1) `get/put` 的典型结构：

`hashmap + doubly linked list`

hashmap 找节点；双向链表 O(1) 移动/删除；头尾表示新旧。

---

# 2. Evaluator

## Precision / Recall / F1

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 = 2PR / (P + R)

必须先定义 denominator=0 时的策略，不要让代码意外除零。

## Micro vs Macro

- Micro：先聚合所有 TP/FP/FN，再算；大 slice 权重大。
- Macro：各 slice/类别先算，再平均；更关注小类别，但对稀疏类别敏感。

医疗评测通常不能只有一个 overall score：要单列高风险、安全、专科、难度等 slices。

## Robust evaluator

必须明确：
- duplicates；
- missing fields；
- malformed input；
- normalization；
- empty prediction/gold；
- deterministic behavior；
- unit/regression tests。

---

# 3. Judge Aggregation

不要先问“平均还是投票”，先问 score 的语义。

- 连续/近似区间量表：mean/median 可考虑；
- 离散标签：majority vote 更自然；
- outlier judge：median 更稳健，但可能掩盖系统性偏差。

必须关注：
- inter-judge disagreement；
- judge missing；
- invalid score；
- judge drift；
- judge vs expert agreement；
- versioning。

LLM-as-Judge 不是 gold，需要用专家/高质量人工集校准。

---

# 4. Async Batch Evaluation

最小结构：

`sample -> bounded worker -> evaluator/API -> result/state store`

## 必会概念

### bounded concurrency

用 semaphore 或 worker pool 限制同时请求数量，避免 rate limit / resource exhaustion。

### timeout

单次请求不能无限挂住。

### retry

只对可重试失败；指数退避 + jitter 常见。

### idempotency

同一个 logical task 重跑，不应产生重复逻辑效果。

常见做法：稳定 task/sample key + unique constraint/upsert + cache/result lookup。

### checkpoint / resume

记录 sample-level 状态：

`PENDING -> RUNNING -> SUCCESS / RETRYABLE_FAILED / FATAL_FAILED`

重启后从未成功任务继续。

### retry 与成本

如果外部 API 已执行成功但本地写入前崩溃，retry 可能重复收费。

面试中要主动承认：外部 API 不支持 idempotency key 时无法绝对避免重复调用，只能通过 request/result ledger、缓存、写入顺序和 reconciliation 降低风险。

---

# 5. Eval / Benchmark 固定骨架

每次设计都按这个顺序：

1. **Capability / task taxonomy**：到底测什么；
2. **Truth**：独立、可审计、非循环；
3. **Rubric / metrics**：和目标能力对齐；
4. **Judge validation**：人工专家锚点、agreement、偏差分析；
5. **Slices / safety**：高风险不能被均值掩盖；
6. **Shortcut / leakage audit**：确认模型不是靠非目标信号；
7. **Statistics / regression**：CI、paired comparison、held-out regression。

## contamination vs shortcut

- contamination：测试内容或高度相似内容进入训练/检索上下文；
- shortcut：不需要目标能力，也能利用非目标特征获得高分。

两者可以同时存在，但不是一回事。

## oracle–naive separation

一个好任务至少应表现为：

- 合法利用目标信息/方法的 oracle 能解；
- 简单 heuristic / leakage / superficial baseline 明显较差。

否则可能是不可解，或过于容易 shortcut。

---

# 6. System Design 固定顺序

不要随机报 Kafka/Redis。先按：

1. Requirements / scale / SLO；
2. Data schema；
3. Task flow；
4. Concurrency / queue；
5. Failure recovery；
6. Idempotency / consistency；
7. Provenance / versioning；
8. Observability；
9. Cost；
10. Trade-offs。

## Provenance 最少记录

每条结果至少能追溯：

- sample/data version；
- tested model version；
- model output；
- evaluator/judge model version；
- judge prompt/rubric version；
- code version；
- timestamp / run_id；
- raw judge response + parsed score（视隐私策略）。

---

# 7. 每道题最后必须说出的 4 句话

Coding：

1. “核心 invariant 是……”
2. “时间复杂度是……，空间复杂度是……”
3. “我会测试空输入、重复/边界以及一个正常 case。”
4. “如果数据扩大/流式输入，我会……”

Eval/System：

1. “先把 truth / data flow 定义清楚。”
2. “这里最大的 failure mode 是……”
3. “我不会让整体平均分掩盖高风险 slice。”
4. “结果必须可以追溯到 data/model/prompt/judge/code version。”