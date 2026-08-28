# PROGRESS — DeepSeek 训练状态（V2）

> 只记录能影响下一题选择的信息。完整跨对话状态使用 `SESSION_STATE.md`。

## 当前状态

```yaml
current_day: 1
current_phase: A
current_pattern: LC1-pattern
status: NOT_STARTED
```

状态只使用：

`NOT_STARTED → LEARNING → BORDERLINE → PASS/RETEST-DUE → MASTERED`

---

# Core 15 Mastery Map

## Level 1 — 基础反射

- [ ] LC1 pattern — HashMap
- [ ] LC20 pattern — Stack
- [ ] LC165 pattern — String parsing
- [ ] LC206 pattern — Linked List reverse

## Level 2 — 高频 Medium

- [ ] LC3 pattern — Sliding Window
- [ ] LC56 pattern — Interval merge
- [ ] LC102 pattern — Tree BFS
- [ ] LC200 pattern — Grid DFS/BFS
- [ ] LC215 pattern — Heap / Top-K
- [ ] LC33 pattern — Binary Search
- [ ] LC146 pattern — LRU

## Level 3 — 强化

- [ ] LC221 pattern — Basic DP
- [ ] LC32 pattern — Parentheses / Stack
- [ ] sqrt pattern — Binary search + Newton
- [ ] LC25 pattern — K-group linked list

### MASTERED V2 标准

不是“连续刚做两题都对”。必须：

1. 至少一次正式无 Hint 2/3 作答 ≥8；
2. 进入 `PASS/RETEST-DUE`；
3. 隔至少 3 道其他题，或下一次 session；
4. 做同模式不同题面的**无提示延迟复测**；
5. 再次 ≥8 才勾选 `MASTERED`。

已 MASTERED 模式若 Mock 回测 <7.5，取消勾选并改回 `RETEST-DUE`。

---

# Retest Queue

| Pattern | First pass score | Hint level | Earliest retest | Retest score | Status |
|---|---:|---:|---|---:|---|
|  |  | 0 | after 3 other questions / next session |  |  |

---

# 岗位能力状态

每约 3 道 Coding 穿插一次，不替代算法主线。

- [ ] B1 evaluator metrics
- [ ] B2 judge aggregation
- [ ] B3 async / retry / resume
- [ ] C1 trustworthy medical model comparison
- [ ] C2 shortcut / leakage audit
- [ ] D1 million-scale judge system
- [ ] D2 continuous regression system

---

# Attempt Log

| Date | Problem/Pattern | Attempt | Score | Primary error | Fatal issue | Hint | Next |
|---|---|---:|---:|---|---|---:|---|
|  |  |  |  |  |  | 0 |  |

## Primary Error Types

每题只选一个：

- `SYNTAX_API`
- `PATTERN_RECOGNITION`
- `INVARIANT`
- `IMPLEMENTATION`
- `BOUNDARY`
- `COMPLEXITY`
- `DEBUGGING`
- `EXPLANATION`
- `EVAL_ENGINEERING`

---

# 5-Question Checkpoints

每完成 5 道正式题，保存：

```text
Mastered:
Pass / retest due:
Borderline:
Biggest risk:
Most common failure type:
Hints used:
Next priority:
```

随后同步一份 `SESSION_STATE.md` 格式 YAML，便于换新 DeepSeek 对话。

---

# 今日收尾

```text
Today mastered:
-

Retest due:
-

Still risky (max 2):
-
-

Tomorrow first task:
-

One invariant I must remember:
-
```

---

# 面试前最终检查

- [ ] Easy 题约 15–20 min 能独立完成
- [ ] 常见 Medium 25–35 min 内能形成正确主解
- [ ] LC3 / LC200 / LC215 / LC146 至少 PASS，关键模式完成延迟复测
- [ ] 链表不会因 pointer 更新顺序卡住
- [ ] Tree/Grid BFS/DFS 能闭卷写
- [ ] Binary Search 边界定义清楚
- [ ] 主动讲时间/空间复杂度
- [ ] 每道 Coding 主动测至少 2 个 edge cases
- [ ] 代码错时能用失败用例自己 trace，而不是等答案
- [ ] 遇到陌生题先给 brute force，再优化
- [ ] Evaluator 会处理 empty/missing/duplicate/malformed
- [ ] Eval 设计知道 independent truth / judge calibration
- [ ] System 设计知道 retry / idempotency / provenance
- [ ] 至少一次 60 min Mock 整体 ≥8/10