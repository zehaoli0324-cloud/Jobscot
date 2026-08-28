# RUBRIC — 严格评分，不做鼓励分

统一 10 分制。**8 分 = 面试中可信；7 分 = 边缘；6 分及以下 = 需要继续练。**

## Coding / Evaluator 题

| 维度 | 分值 | 通过标准 |
|---|---:|---|
| Correctness | 4 | 主逻辑正确，关键 edge case 不错 |
| Complexity | 1.5 | 能给出正确时空复杂度，并知道瓶颈 |
| Robustness | 1.5 | 处理空输入、重复、缺失、异常等 |
| Code quality | 1 | 命名清楚、结构合理、无无谓复杂度 |
| Explanation + tests | 2 | 能解释思路并主动覆盖关键测试 |

### 硬扣分

- 代码主逻辑无法运行：最高 5/10。
- 算法复杂度比目标差一个数量级且无意识：最高 6/10。
- Evaluator 对空集合发生除零 / 静默吞掉 malformed input：至少扣 1.5。
- 只背答案但不能解释 invariant：最高 6/10。

## Eval / Benchmark 设计题

| 维度 | 分值 |
|---|---:|
| Task / slice 定义清楚 | 1.5 |
| Truth / evidence 独立可靠 | 2 |
| Metric / rubric 合理 | 1.5 |
| Judge calibration / human validation | 1.5 |
| Failure / shortcut / leakage 分析 | 1.5 |
| Statistics / uncertainty / regression | 1 |
| 可执行性 | 1 |

### 硬扣分

- Truth 与被评模型或 judge 循环依赖：最高 5/10。
- 只报一个平均总分、不做高风险 slice：最高 6/10。
- LLM-as-Judge 未校准就当 gold：最高 6/10。
- 不区分 contamination 与 shortcut：扣 1。

## System Design 题

| 维度 | 分值 |
|---|---:|
| Data / task flow | 1.5 |
| Concurrency / throughput | 1.5 |
| Failure recovery | 2 |
| Idempotency / consistency | 1.5 |
| Observability / provenance | 1.5 |
| Cost / scalability | 1 |
| Trade-off 表达 | 1 |

### 硬扣分

- 任务失败后只能“从头重跑”：最高 6/10。
- retry 可能造成重复写入/重复收费但没有意识：最高 6/10。
- 没有 sample-level 状态或 checkpoint：扣 1.5。
- 无版本追踪，无法知道某个分数由哪个模型/prompt/judge 产生：扣 1.5。

## 面试通过判断

- **9–10**：明显强，能反向推动设计。
- **8–8.9**：稳定通过该能力面。
- **7–7.9**：有基础但容易被追问打穿，再做 1 个变式。
- **6–6.9**：理解不完整，必须补。
- **<6**：核心概念或 coding 尚未形成可用能力。
