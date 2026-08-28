# MOCK INTERVIEW — Day 7 全真模拟

> 目标：复刻 60 分钟技术面，不再学习新知识。

## 规则

- 全程 60 分钟；
- 不查资料；
- Agent 不提前提示；
- Coding 必须现场写完整代码；
- 面试官至少追问 2 个 failure / edge cases；
- 结束后按 `RUBRIC.md` 总评；
- Mock 1 与 Mock 2 换题面，但不换能力范围。

---

# 标准 60 分钟结构

## 0–5 min：项目热身

随机选一个你熟悉的 Eval / Benchmark 项目，要求 3 分钟讲清：

1. problem；
2. 你做了什么；
3. 最难的技术/方法问题；
4. 如何验证结果可信；
5. 一个失败或迭代。

面试官只追一个最深问题，不展开成完整项目面。

---

## 5–35 min：Coding

从以下能力随机抽 1 个：

- A1 / A2 / A3 / A4；
- B1 / B2；
- 若前六天状态很好，可抽 B3 的简化版。

要求：

1. 先复述需求与边界；
2. 写代码；
3. 主动测试；
4. 复杂度；
5. 面试官改变一个 constraint 后口头调整方案。

### Coding 追问池

只抽 1–2 个：

- 输入扩大 1000 倍？
- 输入是 stream？
- 空输入/重复/缺字段？
- 为什么这个数据结构比另一种好？
- 如果不能依赖标准库怎么办？

---

## 35–50 min：Eval / Data / System Deep Dive

随机抽 1 个：

- B3；
- C1；
- C2；
- D1；
- D2。

候选人先用 2 分钟给结构，再展开。

面试官必须追问两个 failure mode，例如：

- truth 是否循环依赖？
- judge 为什么可信？
- retry 重复收费怎么办？
- worker 挂了怎么办？
- 高风险错误为何不会被平均掉？
- benchmark 涨分是不是 contamination？

---

## 50–57 min：快速基础追问

从下面随机选 3 个，每题 1–2 分钟：

- dict / set / list lookup 复杂度；
- heap top-k 复杂度；
- micro vs macro；
- precision vs recall；
- timeout vs retry；
- idempotency；
- cache 与 checkpoint 区别；
- contamination vs shortcut；
- frozen regression vs dynamic challenge set；
- provenance 至少记录哪些 version。

---

## 57–60 min：候选人反问

准备 2 个真正像研发候选人的问题，例如：

- 团队当前医疗大模型评测中，最难自动化、仍依赖专家 adjudication 的环节是什么？
- 这个岗位更偏 evaluator/data pipeline 的工程建设，还是会直接参与 benchmark definition 和模型 failure analysis？
- 新模型版本的 release gate 目前主要由哪些指标和高风险 slices 决定？

不要在技术面优先问福利和加班。

---

# Mock 总评模板

```text
Coding: __/10
Evaluator/Data Engineering: __/10
Eval/Benchmark reasoning: __/10
Communication/Debugging: __/10

Weighted score: __/10
Fatal issue: __________________
Strongest signal: ______________
Verdict: FAIL / BORDERLINE / STABLE PASS
```

## 稳定通过条件

建议同时满足：

- Coding ≥7.5；
- 加权总分 ≥8；
- 没有 correctness 致命错误；
- 没有 truth 循环依赖；
- 没有“失败后从头重跑”的系统设计；
- 能主动提至少一个 edge case / failure mode，而不是全靠面试官提醒。

---

# Mock 后修补规则

只选一个：

> 如果明天就面试，我最可能因为哪一个问题挂？

只补它 60–120 分钟，然后进行第二次 Mock。

禁止：Mock 结束后因为焦虑新增十几个知识点。