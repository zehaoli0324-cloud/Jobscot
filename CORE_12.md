# CORE 12 — 12 个能力锚点

这不是题海。每题代表一个核心模式；训练时优先做变式，不继续横向加题。

## A. Python / 数据结构 Coding（5）

### A1. 去重 + 最新记录

给定：

```python
records = [
    {"qid": "q1", "model": "A", "score": 0.8, "ts": 3},
    {"qid": "q1", "model": "A", "score": 0.6, "ts": 1},
    {"qid": "q2", "model": "A", "score": 0.9, "ts": 2},
]
```

对 `(qid, model)` 去重，仅保留 `ts` 最大的一条；最终按 `qid` 排序。

追问：复杂度？数据不能一次放进内存怎么办？

**模式：dict / tuple key / sorting / streaming thinking。**

### A2. 最长无重复窗口

实现 `longest_unique_span(items)`，返回最长不含重复元素的连续区间长度。

```text
[A, B, A, C, D] -> 4
```

追问：为什么不能每次重新构造 set？

**模式：sliding window + hashmap。**

### A3. Top-K 错误类型

输入大量错误标签，返回出现频率最高的 K 类及次数，并考虑输入很大。

追问：`Counter.most_common`、全排序、heap 的复杂度区别？

**模式：frequency map + heap。**

### A4. 依赖任务是否可执行

```python
{
    "parse": [],
    "judge": ["parse"],
    "report": ["judge"]
}
```

判断是否有循环依赖；若无，给出一个执行顺序。

**模式：graph + indegree + BFS / topological sort。**

### A5. LRU Cache

实现固定容量 LRU Cache：

```python
get(key)
put(key, value)
```

平均 O(1)。

追问：为什么普通 dict 不够？`OrderedDict` 怎么做？如果要求手写怎么办？

**模式：hashmap + doubly linked list。**

---

## B. 数据处理 + Evaluator Coding（3）

### B1. 医疗问答 Evaluator

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
- 重复 diagnosis 去重；
- 缺字段有明确策略；
- 写至少 4 个 edge cases。

追问：为什么医疗任务不能只看 micro-F1？

### B2. Judge Aggregation

```python
{
    "sample_id": "q1",
    "scores": [4, 4, 1]
}
```

实现聚合器：
- 输出最终分；
- 标记高分歧样本；
- judge 缺失仍可运行；
- 异常值不能静默吞掉。

追问：什么时候 mean / median / majority vote？怎样发现 judge drift？

### B3. 可恢复 Batch Evaluation

实现：

```python
async def evaluate_batch(samples, evaluator, concurrency=10):
    ...
```

要求：
- 并发受控；
- 单样本失败不拖垮整批；
- timeout + retry；
- sample-level 状态；
- rerun 时跳过成功样本。

追问：怎样 idempotent？怎样避免 retry 重复计费？

---

## C. LLM Eval / Benchmark 设计（2）

### C1. 模型 A 与 B，谁更适合医疗问答？

有 10,000 条医疗问答和两个模型，设计可信比较。

必须覆盖：
1. task taxonomy / slices；
2. ground truth / evidence；
3. metric / rubric；
4. LLM-as-Judge calibration；
5. 医疗高风险错误；
6. statistics / uncertainty；
7. error taxonomy；
8. held-out regression set。

**红线：只说“让一个强模型当 judge 打平均分”视为不通过。**

### C2. 如何证明 Benchmark 没有 shortcut？

模型分数很高，如何判断它是真的完成目标能力，而不是利用题面、答案分布、模板、长度或泄露？

必须覆盖：
- leakage audit；
- naive baseline；
- adversarial / counterfactual perturbation；
- oracle–naive separation；
- ablation；
- held-out construction；
- contamination 与 shortcut 的区别。

---

## D. 评测系统工程设计（2）

### D1. 100 万条回答 × 3 个 Judge

约束：rate limit、timeout、成本昂贵、长时间运行、机器可能挂、结果必须可追溯可复现。

必须讲：

`queue / batch / async / retry / backoff / cache / checkpoint / idempotency / schema / observability / provenance / cost control`

### D2. 模型升级后如何判断“真的变好”？

团队每周发布一个新医疗模型版本，设计持续评测系统。

必须讲：
- frozen regression suite；
- dynamic challenge set；
- slice metrics；
- safety guardrails；
- significance / uncertainty；
- failure case tracking；
- data / prompt / model / judge versioning；
- release gate / rollback。

---

# 停止规则

- A 类同模式变式连续 2 题 ≥8/10：停止刷该模式；
- B1/B2/B3 全部 ≥8/10：Evaluator 通过；
- C1/C2 15 分钟内均 ≥8/10：Eval 通过；
- D1/D2 20 分钟内均 ≥8/10：System 通过。

达到后转模拟面试和项目深挖，不继续堆题。