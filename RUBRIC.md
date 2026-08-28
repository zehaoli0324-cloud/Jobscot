# RUBRIC — 严格 10 分制

**8 分 = 面试中可信；7 分 = 边缘；6 分及以下 = 必须继续练。**

## Coding / Evaluator

| 维度 | 分值 | 标准 |
|---|---:|---|
| Correctness | 4 | 主逻辑正确，关键 edge case 正确 |
| Complexity | 1.5 | 时空复杂度正确，知道瓶颈 |
| Robustness | 1.5 | empty / duplicate / missing / malformed 有策略 |
| Code quality | 1 | 命名与结构清楚，无无谓复杂度 |
| Explanation + tests | 2 | 能解释 invariant，并主动测试 |

硬扣分：
- 主逻辑无法运行：最高 5；
- 复杂度差一个数量级且无意识：最高 6；
- evaluator 除零或静默吞异常：至少扣 1.5；
- 背过代码但说不清 invariant：最高 6。

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

## 总体判断

- **9–10**：强，能反向推动设计；
- **8–8.9**：稳定通过；
- **7–7.9**：边缘，再做一个变式；
- **6–6.9**：理解不完整；
- **<6**：核心能力未形成。

## Mock Interview 总评

60 分钟模拟按以下权重：

- Coding：40%
- Evaluator / Data Engineering：25%
- Eval / Benchmark reasoning：20%
- Communication / debugging：15%

若 Coding correctness <6，或出现 truth 循环依赖 / retry 无幂等 / 无失败恢复等致命问题，即使加权均分 ≥8，也不能判“稳定通过”。