# DAILY LOOP — 每天可复用的学习 + 练习模板

> 目标：避免“看懂了 = 会了”。每个知识点必须经过闭卷、限时、测试和变式。

## 一个标准训练单元（约 90–120 min）

### Step 1 — Learn（20–30 min）

只回答 5 个问题：

1. 这个模式解决什么问题？
2. 核心数据结构 / invariant 是什么？
3. 时间和空间复杂度？
4. 最常见 failure / bug？
5. 在医疗评测或数据工程里会在哪里出现？

学习阶段允许看资料，但禁止复制整段答案代码。

---

### Step 2 — Closed-book Recall（10 min）

关掉资料，用自己的话写：

- 3–5 行核心思路；
- 必要 API / 数据结构；
- 复杂度；
- 2 个 edge cases。

如果连这一步都写不出，说明还没有形成可调用知识。

---

### Step 3 — Timed Attempt（25–45 min）

模拟面试：

- 不查答案；
- 不让 Agent 提示；
- 先复述题意；
- 写完整可运行代码或完整设计；
- Coding 必须主动写测试；
- 设计题必须主动讲 failure mode。

Coding 推荐时间：
- Easy / data processing：20–25 min；
- Medium pattern：25–35 min；
- async/evaluator 工程题：35–45 min。

---

### Step 4 — Self-test / Interviewer Pressure（10–15 min）

Coding 自问：

- 空输入？
- 重复值？
- malformed input？
- 数据扩大 1000 倍？
- stream 输入？
- 有没有 off-by-one / denominator=0？

System / Eval 自问：

- truth 独立吗？
- worker 挂了怎么办？
- retry 会重复写/重复收费吗？
- 高风险错误会不会被平均分掩盖？
- 某个分数能追溯到 model/prompt/judge/version 吗？

---

### Step 5 — Rubric Score（5 min）

按 `RUBRIC.md` 评分，不打鼓励分。

记录：

```text
Score: __ / 10
Fatal issue: __________________
Best part: ____________________
```

**<7：未掌握。7–7.9：边缘。≥8：可信。**

---

### Step 6 — Error Log（10 min）

错误只能归到以下 6 类之一：

1. `SYNTAX/API` — Python 写法不熟；
2. `PATTERN` — 没识别出 hashmap/window/heap/BFS 等；
3. `CORRECTNESS` — invariant 或边界错误；
4. `ROBUSTNESS` — empty/missing/malformed 没处理；
5. `ENGINEERING` — retry/state/idempotency/provenance 缺失；
6. `EVAL_REASONING` — truth/judge/shortcut/slice/statistics 有漏洞。

不要写“粗心”。必须写可修复原因。

示例：

```text
错误：滑窗左指针只移动一次，重复元素仍留在窗口。
类别：CORRECTNESS
根因：没有明确 window invariant。
修复句：循环结束后 window 内必须不存在重复元素。
```

---

### Step 7 — Variant（20–30 min）

只有两种情况需要做变式：

- 得分 <8；
- 得分 ≥8 但这是该模式第一次通过。

变式只能改：
- schema；
- edge case；
- 数据规模；
- 医疗语境；
- performance / failure constraint。

**不新增算法知识点。**

---

## 停止规则

同一能力：

- 第一次 ≥8：再做 1 个变式；
- 连续两次 ≥8：标记 `MASTERED`，停止练这类题；
- 连续两次 <7：回到 Learn，但只重学最小缺口；
- 第三次仍 <7：记录为 `INTERVIEW_RISK`，后续每天用 20 min 复测。

---

## 每日收尾（15 min）

更新 `PROGRESS.md`：

```text
Today mastered:
- ...

Still risky:
- ...

Tomorrow first task:
- ...

One sentence I must remember:
- ...
```

每天只允许保留 **1–2 个主要弱点**。不要制造一个 20 项待办清单。

---

# 给 Agent 的每日指令模板

复制：

> 读取 ROADMAP_7D、DAILY_LOOP、CORE_12、RUBRIC 和 PROGRESS。今天是 Day __。严格按当天顺序训练我。学习块只讲最少必要知识；然后闭卷抽问；接着一次只出一道限时题，不给提示。我完成后严格评分、指出唯一最致命问题，并决定是同模式变式还是升级。不要提前扩展新的知识点。