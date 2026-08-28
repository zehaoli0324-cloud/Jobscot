# RUBRIC — 严格 10 分制（V2）

**8 分 = 面试中可信；7 分 = 边缘；6 分及以下 = 必须继续练。**

## Coding / Evaluator

| 维度 | 分值 | 标准 |
|---|---:|---|
| Correctness | 5.0 | 主逻辑正确，关键 edge case 正确 |
| Complexity | 1.5 | 时空复杂度正确，知道瓶颈 |
| Edge cases / robustness | 1.5 | empty / duplicate / boundary / malformed 等有策略 |
| Explanation / invariant | 1.0 | 能解释为什么正确，不只是背模板 |
| Code clarity / self-test | 1.0 | 命名清楚，主动给测试并能调试 |

### 硬扣分

- 主逻辑无法运行或错误：最高 5.5；
- 复杂度明显差一个数量级且无意识：最高 6.5；
- evaluator 除零或静默吞异常：至少扣 1.5；
- 代码背对但说不清 invariant：最高 7；
- 面试官明确指出核心算法后才完成：最高 6.5；
- 看过完整答案后的立即重写：不提供 mastery 证据。

### 提示上限

| 提示使用 | 本题最高分 | 是否可 MASTERED |
|---|---:|---|
| 无提示 | 10 | 仍需延迟复测 |
| Hint 1：苏格拉底式问题 | 9.0 | 否 |
| Hint 2：模式方向 | 8.0 | 否 |
| Hint 3：局部伪代码/invariant | 7.0 | 否 |
| 完整答案 | 不作为 mastery evidence | 否 |

> 提示不是惩罚，而是为了区分“独立面试能力”和“教学后能力”。

## 正确性验证原则

如果候选人代码有 bug：

1. 优先给**最小失败输入**；
2. 让候选人自己 trace；
3. 再决定是否提示；
4. 不要第一时间贴标准答案。

如果模型没有真实代码执行环境，只能说“静态检查/手工测试”，不能声称已经真实运行。

---

## Eval / Benchmark

| 维度 | 分值 |
|---|---:|
| Task / slice | 1.5 |
| Truth / evidence 独立可靠 | 2 |
| Metric / rubric | 1.5 |
| Judge calibration / human validation | 1.5 |
| Failure / shortcut / leakage | 1.5 |
| Statistics / uncertainty / regression | 1 |
| 可执行性 | 1 |

硬扣分：

- truth 与被评模型/judge 循环依赖：最高 5；
- 只报平均总分，不看高风险 slice：最高 6；
- LLM judge 未校准直接当 gold：最高 6；
- 不区分 contamination 和 shortcut：扣 1。

---

## System Design

| 维度 | 分值 |
|---|---:|
| Data / task flow | 1.5 |
| Concurrency / throughput | 1.5 |
| Failure recovery | 2 |
| Idempotency / consistency | 1.5 |
| Observability / provenance | 1.5 |
| Cost / scalability | 1 |
| Trade-off | 1 |

硬扣分：

- 失败后只能从头重跑：最高 6；
- retry 可能重复收费/写入且没意识：最高 6；
- 无 sample-level 状态/checkpoint：扣 1.5；
- 无版本追踪，分数不可追溯：扣 1.5。

---

## 状态判定

- **9–10**：强；本次 PASS，等待延迟复测；
- **8–8.9**：稳定通过本次，状态 `PASS / RETEST-DUE`；
- **7–7.9**：`BORDERLINE`，需要同模式变式；
- **6–6.9**：`LEARNING`；
- **<6**：核心能力未形成。

### MASTERED 的额外条件

不能只看一次分数。

必须：

1. 至少一次无 Hint 2/3 的正式题 ≥8；
2. 隔至少 3 道其他题，或下一次 session；
3. 做同模式不同题面的无提示变式；
4. 延迟复测再次 ≥8。

满足后才允许标记 `MASTERED`。

已 MASTERED 模式若在后续 Mock 回测 <7.5，则降级为 `RETEST-DUE`。

---

## Mock Interview 总评

60 分钟模拟按：

- Coding：50%
- Evaluator / Data Engineering：20%
- Eval / Benchmark / System reasoning：15%
- Communication / debugging：15%

若 Coding correctness <6，或出现 truth 循环依赖 / retry 无幂等 / 无失败恢复等致命问题，即使加权均分 ≥8，也不能判“稳定通过”。