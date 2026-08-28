# CORE 12 — 只保留这些题

这 12 题不是“题库”，而是 12 个**能力锚点**。每题代表一类模式；训练时优先做变式，而不是继续加新知识点。

---

## A. Python / 数据结构现场 Coding（5 题）

### A1. 去重 + 保序 + 最新记录

给定医疗模型评测记录：

```python
records = [
    {"qid": "q1", "model": "A", "score": 0.8, "ts": 3},
    {"qid": "q1", "model": "A", "score": 0.6, "ts": 1},
    {"qid": "q2", "model": "A", "score": 0.9, "ts": 2},
]
```

实现：对 `(qid, model)` 去重，仅保留 `ts` 最大的一条；最终按 `qid` 排序返回。

追问：时间复杂度？如果数据不能一次放进内存怎么办？

**核心模式：** dict / tuple key / sorting / streaming thinking。

---

### A2. 最长无重复窗口

实现 `longest_unique_span(items)`：返回一个序列中最长“不含重复元素”的连续区间长度。

例：

```python
["A", "B", "A", "C", "D"] -> 4
```

追问：为什么不能每次重新构造 set？

**核心模式：** sliding window + hashmap。

---

### A3. Top-K 错误类型

输入大量错误标签字符串，例如：

```python
["hallucination", "unsafe", "hallucination", "guideline_mismatch", ...]
```

返回出现频率最高的 K 类及其次数。要求考虑输入非常大。

追问：`Counter.most_common`、排序和 heap 的复杂度区别？

**核心模式：** frequency map + heap。

---

### A4. 依赖任务是否可执行

有一批评测任务，每个任务可能依赖其他任务：

```python
{
    "parse": [],
    "judge": ["parse"],
    "report": ["judge"]
}
```

判断是否存在循环依赖；若无，给出一个可执行顺序。

**核心模式：** graph + indegree + BFS / topological sort。

---

### A5. LRU Cache

实现一个固定容量的 LRU Cache，支持：

```python
get(key)
put(key, value)
```

平均 O(1)。

追问：为什么只用普通 dict 不够？Python `OrderedDict` 怎么实现？如果要求手写数据结构怎么办？

**核心模式：** hashmap + doubly linked list / cache systems。

---

## B. 数据处理 + Evaluator Coding（3 题）

### B1. 医疗问答 Evaluator

输入：

```python
samples = [
    {
        "id": "1",
        "gold": {"diagnosis": ["A", "B"]},
        "pred": {"diagnosis": ["A", "C"]}
    }
]
```

实现 micro precision / recall / F1。

要求：

- 空预测不能报错；
- 重复 diagnosis 要去重；
- 缺字段要有明确策略；
- 写至少 4 个 edge cases。

追问：为什么医疗任务可能不能只看 micro-F1？

---

### B2. Judge Aggregation

每个回答由 3 个 judge 打分：

```python
{
    "sample_id": "q1",
    "scores": [4, 4, 1]
}
```

设计并实现一个聚合器：

- 输出最终分；
- 标记高分歧样本；
- judge 缺失时仍可运行；
- 不允许静默吞掉异常值。

追问：什么时候应该 majority vote，什么时候用平均分？怎样发现 judge drift？

---

### B3. 可恢复的 Batch Evaluation

实现函数框架：

```python
async def evaluate_batch(samples, evaluator, concurrency=10):
    ...
```

要求：

- 最大并发受控；
- 单样本失败不导致整批失败；
- timeout + retry；
- 保存每个 sample 的状态；
- 重新运行时跳过已经成功的 sample。

追问：怎样做到 idempotent？怎样避免 retry 导致 API 重复计费？

---

## C. LLM Eval / Benchmark 设计（2 题）

### C1. 模型 A 和 B，谁更适合医疗问答？

你有 10,000 条医疗问答和两个模型。设计一次可信比较。

必须讲清：

1. task taxonomy；
2. ground truth / evidence source；
3. scoring rubric；
4. LLM-as-Judge 如何校准；
5. 医疗高风险错误如何单独处理；
6. 统计比较；
7. error taxonomy；
8. held-out regression set。

**红线：**只说“让 GPT-5 当 judge 打平均分”视为不通过。

---

### C2. 如何证明一个 Benchmark 没有被 shortcut？

你设计了一个医疗推理 Benchmark，模型分数很高。怎么判断它是真的会推理，而不是利用题面、答案分布、长度、模板或数据泄露？

必须覆盖：

- leakage audit；
- naive baseline；
- adversarial / counterfactual perturbation；
- oracle–naive separation；
- ablation；
- held-out construction；
- contamination 与 shortcut 的区别。

---

## D. 评测系统工程设计（2 题）

### D1. 100 万条回答 × 3 个 Judge

设计一个系统，对 100 万条医疗模型回答调用 3 个 LLM judge。

约束：

- API 有 rate limit；
- 单次调用可能超时；
- 成本昂贵；
- 任务可能运行数小时甚至更久；
- 运行中机器可能挂；
- 最终结果必须可追溯、可复现。

必须讲：

`queue / batch / async / retry / backoff / cache / checkpoint / idempotency / schema / observability / cost control`

---

### D2. 模型升级后怎么判断“真的变好了”？

团队每周发布一个新医疗模型版本。设计持续评测系统。

必须讲：

- frozen regression suite；
- dynamic challenge set；
- slice metrics；
- safety guardrails；
- significance / uncertainty；
- failure case tracking；
- data / prompt / model / judge versioning；
- release gate 与 rollback。

---

# 停止规则

不要继续无限加题。

当你满足：

- A 类任意变式连续 2 题 ≥8/10；
- B 类 3 题全部 ≥8/10；
- C、D 类能在 15 分钟内独立回答到 ≥8/10；

就停止刷题，转去做模拟面试和项目深挖。
