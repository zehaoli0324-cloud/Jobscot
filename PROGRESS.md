# PROGRESS — DeepSeek 训练状态

> 每次只记录分数、主要错误和下一步。DeepSeek 在同一对话里自行维护临时状态；每完成 5 题，把 checkpoint 复制到本文件即可。

## 当前状态

```yaml
current_day: 1
current_phase: A
current_pattern: LC1-pattern
status: NOT_STARTED
```

## Core 15 Mastery Map

### Level 1 — 基础反射

- [ ] LC1 pattern — HashMap
- [ ] LC20 pattern — Stack
- [ ] LC165 pattern — String parsing
- [ ] LC206 pattern — Linked List reverse

### Level 2 — 高频 Medium

- [ ] LC3 pattern — Sliding Window
- [ ] LC56 pattern — Interval merge
- [ ] LC102 pattern — Tree BFS
- [ ] LC200 pattern — Grid DFS/BFS
- [ ] LC215 pattern — Heap / Top-K
- [ ] LC33 pattern — Binary Search
- [ ] LC146 pattern — LRU

### Level 3 — 强化

- [ ] LC221 pattern — Basic DP
- [ ] LC32 pattern — Parentheses / Stack
- [ ] sqrt pattern — Binary search + Newton
- [ ] LC25 pattern — K-group linked list

`MASTERED` = 同一模式连续两次 ≥8/10，且没有依赖 Hint 2/3。

---

# 岗位能力状态

每 3 道 Coding 穿插一次，不替代算法主线。

- [ ] B1 evaluator metrics
- [ ] B2 judge aggregation
- [ ] B3 async / retry / resume
- [ ] C1 trustworthy medical model comparison
- [ ] C2 shortcut / leakage audit
- [ ] D1 million-scale judge system
- [ ] D2 continuous regression system

---

# Attempt Log

| Date | Problem/Pattern | Attempt | Score | Main failure type | Fatal issue | Hint level | Next |
|---|---|---:|---:|---|---|---:|---|
|  |  |  |  |  |  | 0 |  |

## Error Types

只用一个主要标签：

- `SYNTAX`
- `PATTERN_RECOGNITION`
- `INVARIANT`
- `IMPLEMENTATION`
- `BOUNDARY`
- `COMPLEXITY`
- `EXPLANATION`
- `EVAL_ENGINEERING`

不要一次给一道题贴多个根因标签。

---

# 5-Question Checkpoints

每完成 5 题，把 DeepSeek 的 checkpoint 贴到这里。

## Checkpoint 1

```text
Mastered:
Needs work:
Biggest risk:
Recommendation:
```

## Checkpoint 2

```text
Mastered:
Needs work:
Biggest risk:
Recommendation:
```

## Checkpoint 3

```text
Mastered:
Needs work:
Biggest risk:
Recommendation:
```

---

# 今日收尾

```text
Today mastered:
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

- [ ] Easy 题 15 min 左右能独立完成
- [ ] 常见 Medium 25–35 min 内能形成正确主解
- [ ] LC3 / LC200 / LC215 / LC146 都达到 PASS
- [ ] 链表不会因 pointer 更新顺序卡住
- [ ] 树/Grid BFS/DFS 能闭卷写
- [ ] Binary Search 边界定义清楚
- [ ] 能主动讲时间/空间复杂度
- [ ] 每道 Coding 会自己测至少 2 个 edge cases
- [ ] 遇到陌生题先给 brute force，不直接沉默
- [ ] Evaluator 会处理 empty/missing/duplicate/malformed
- [ ] Eval 设计知道 independent truth / judge calibration
- [ ] System 设计知道 retry / idempotency / provenance
- [ ] 至少一次 60 min Mock 整体 ≥8/10