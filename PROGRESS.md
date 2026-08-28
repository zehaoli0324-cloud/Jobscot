# PROGRESS — 训练状态

> 每次训练后只更新分数、错误类型和下一步。不要写成长篇日记。

## 当前状态

```yaml
current_day: 1
current_stage: A1
status: NOT_STARTED
```

## 评分记录

| Day | Skill | Attempt | Score | Fatal issue | Error type | Next |
|---|---|---:|---:|---|---|---|
| 1 | A1 | 1 |  |  |  |  |
| 1 | B1 | 1 |  |  |  |  |
| 2 | A2 | 1 |  |  |  |  |
| 2 | A3 | 1 |  |  |  |  |
| 2 | A4 | 1 |  |  |  |  |
| 2 | A5 | 1 |  |  |  |  |
| 3 | B1 variant | 2 |  |  |  |  |
| 3 | B2 | 1 |  |  |  |  |
| 4 | B3 | 1 |  |  |  |  |
| 5 | C1 | 1 |  |  |  |  |
| 5 | C2 | 1 |  |  |  |  |
| 6 | D1 | 1 |  |  |  |  |
| 6 | D2 | 1 |  |  |  |  |
| 7 | Mock 1 | 1 |  |  |  |  |
| 7 | Mock 2 | 1 |  |  |  |  |

## Mastery Map

- [ ] A1 dict / dedup / sort
- [ ] A2 sliding window
- [ ] A3 top-k / heap
- [ ] A4 BFS / topological sort
- [ ] A5 LRU
- [ ] B1 evaluator metrics
- [ ] B2 judge aggregation
- [ ] B3 async / retry / resume
- [ ] C1 trustworthy model comparison
- [ ] C2 shortcut / leakage audit
- [ ] D1 million-scale judge system
- [ ] D2 continuous regression system

`MASTERED` 标准：同一能力连续两次 ≥8/10；B1/B2/B3 不允许仅靠口头理解标记。

## Error Log

只允许以下标签：

- `SYNTAX/API`
- `PATTERN`
- `CORRECTNESS`
- `ROBUSTNESS`
- `ENGINEERING`
- `EVAL_REASONING`

| Date | Skill | Error type | One-line root cause | Repair |
|---|---|---|---|---|
|  |  |  |  |  |

## 今日收尾模板

```text
Today mastered:
- 

Still risky (max 2):
- 
- 

Tomorrow first task:
- 

One sentence I must remember:
- 
```

## 面试前最终检查

- [ ] 常用 Python 容器/API 不查资料即可写
- [ ] 30 分钟内能完成随机核心 Coding
- [ ] evaluator 会主动处理 empty/missing/duplicate/malformed
- [ ] async batch 会 timeout/retry/checkpoint/resume
- [ ] 能解释 idempotency 和重复计费风险
- [ ] Eval 设计先定义 task + independent truth
- [ ] LLM-as-Judge 会做 calibration，不当 gold
- [ ] 会区分 contamination 与 shortcut
- [ ] System design 主动讲 failure recovery + provenance
- [ ] 至少 1 次 Mock 达到稳定通过