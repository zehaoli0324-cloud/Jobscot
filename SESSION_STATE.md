# SESSION STATE — DeepSeek 会话恢复模板

> 用途：DeepSeek 无法直接持久化训练状态时，每 5 题或每天结束生成一次。新对话把最近一份 YAML 一起发给它。

```yaml
session_state:
  date: ""
  questions_completed: 0
  current_phase: "Phase A"
  current_priority: ""

  mastered: []
  pass_retest_due: []
  borderline: []
  learning: []

  last_attempts:
    # - pattern: "sliding_window"
    #   anchor: "LC3-like"
    #   score: 8.5
    #   hints_used: 0
    #   primary_error: null
    #   retest_after_question: 0

  failure_counts:
    SYNTAX_API: 0
    PATTERN_RECOGNITION: 0
    INVARIANT: 0
    IMPLEMENTATION: 0
    BOUNDARY: 0
    COMPLEXITY: 0
    DEBUGGING: 0
    EXPLANATION: 0

  hint_counts:
    hint_1: 0
    hint_2: 0
    hint_3: 0
    full_answer: 0

  strongest_patterns: []
  highest_risk_patterns: []
  next_priority: ""
  next_action: ""
```

## 更新规则

- 一次 ≥8：进入 `pass_retest_due`，不能直接进 `mastered`。
- 延迟无提示变式再次 ≥8：才进入 `mastered`。
- `MASTERED` 后 Mock <7.5：移回 `pass_retest_due`。
- Hint 2/3 或完整答案完成的题不能直接提供 mastery 证据。
- `primary_error` 每题只记录一个最主要根因。

## 新对话恢复 Prompt

```text
这是我上一轮训练状态。请把它作为当前真实进度，并结合仓库中的 DEEPSEEK_TUTOR.md V2 继续训练。不要重头开始，也不要展示题单。先检查哪些 RETEST-DUE 已满足延迟条件，再决定下一道单题。

<粘贴 YAML>
```
