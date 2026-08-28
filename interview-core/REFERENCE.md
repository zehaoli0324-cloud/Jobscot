# REFERENCE — 做完题再看

这里只给“面试级骨架”，不追求教科书展开。

## A1 去重 + 最新记录

- key = `(qid, model)`；单次扫描维护最大 `ts`。
- 最后按 `qid` 排序。
- 时间：`O(n + m log m)`；空间：`O(m)`。
- 超大数据：外部排序、按 key 分区、数据库 `GROUP BY` / window function，或流式状态存储。

## A2 最长无重复窗口

- `left` + `last_seen[item]`。
- 遇到重复时：`left = max(left, last_seen[item] + 1)`。
- 每个元素只进出窗口一次，`O(n)`。

## A3 Top-K

- 先 frequency map；若类别数为 `m`：排序 `O(m log m)`，heap `O(m log k)`。
- 若输入极大但类别有限，可 streaming count；若类别也极大，再讨论 approximate heavy hitters。

## A4 DAG

- Kahn topological sort：建 indegree + adjacency；从 indegree=0 队列开始。
- 最终处理节点数 < 总节点数 => 有环。

## A5 LRU

- HashMap 保证 key -> node O(1)。
- Doubly linked list 维护 recency，移动/删除 O(1)。
- Python 可用 `OrderedDict`，但面试要能解释底层组合。

## B1 Evaluator

- 先明确单位：每个样本中的 diagnosis 当集合。
- 全局累加 TP / FP / FN，再算 micro P/R/F1。
- 定义 zero denominator 行为；明确 missing field 是 invalid、empty 还是 skip，不能默默决定。
- 单测至少覆盖：perfect、all wrong、empty pred、empty gold、duplicates、missing/malformed。

## B2 Judge Aggregation

- 先 validate range；缺失 judge 显式记录 count。
- 聚合前区分 ordinal score 与 categorical vote。
- 分歧可用 range / std / MAD / pairwise disagreement。
- 高分歧样本进入 expert adjudication 或 secondary judge。
- Judge drift：固定 anchor set + periodic calibration + per-judge agreement/偏差监控。

## B3 Recoverable Batch Eval

最小架构：

`sample -> task state -> semaphore-controlled async worker -> timeout/retry(backoff) -> result store`

关键点：

- sample/task 有稳定 id；
- 状态 `PENDING/RUNNING/SUCCEEDED/FAILED`；
- 成功结果持久化后才视为完成；
- restart 时只读取非 SUCCEEDED；
- cache key 应包含 input hash + evaluator/model/prompt/version；
- retry 写入使用 upsert/唯一键保证幂等。

## C1 模型比较

推荐顺序：

`use case -> task/safety slices -> independent truth -> rubric -> calibrated judge + expert anchors -> metrics + uncertainty -> paired comparison -> error taxonomy -> frozen regression`

高风险医疗错误（错误用药、漏诊危险病征等）不能被普通回答的平均分稀释，应单列 rate / severity gate。

## C2 Shortcut Audit

- contamination：测试内容可能进入训练数据；
- shortcut：即便没见过原题，也可利用非目标信号做对。

检查组合：leakage audit、naive baselines、label/format perturbation、counterfactuals、ablation、OOD held-out、oracle–naive separation。Benchmark 应证明“目标能力增加确实带来额外可测收益”。

## D1 100 万 × 3 Judge

核心组件：

`dataset/version -> durable task queue -> rate-limited workers -> model API -> validated result store -> aggregation/report`

必须有：checkpoint、retry/backoff、dead-letter、cache、idempotent key、sample-level provenance、metrics/logging、cost budget。

不要把“多线程”当系统设计答案；面试官关心的是失败后如何恢复、如何不重复花钱、如何追溯。

## D2 持续评测

两套集合：

- frozen regression suite：跨版本可比较；
- dynamic challenge set：追踪最新 failure frontier。

每次 release 固定记录 model/data/prompt/judge/version；看 overall + slices + safety gates + paired delta + uncertainty。触发 regression gate 时阻止发布或 rollback，并把新 failure case 进入可审计的 case lifecycle。
