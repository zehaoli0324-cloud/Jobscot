# Xiaohe Medical LLM Eval — Interview Core

> 目标：只练最可能决定技术面是否通过的能力。**少而精，不做百科全书式准备。**

适用岗位：大模型评测 / 数据工程师（医疗方向），以及相近的 LLM Eval / Benchmark / Data Engineer 岗位。

## 只练 4 个能力

| 优先级 | 能力 | 面试中要达到的状态 |
|---|---|---|
| P0 | Python + 数据结构现场 Coding | 25–35 分钟独立写出正确代码，能讲复杂度和边界条件 |
| P0 | 数据处理 + Evaluator Coding | 能把 JSONL/模型输出变成可靠、可复跑的评测程序 |
| P0 | LLM Eval / Benchmark 设计 | 能定义 truth、rubric、judge calibration、error taxonomy、held-out regression |
| P1 | 评测系统工程设计 | 能讲并写出 batch、async、retry、rate limit、cache、idempotency、resume |

**暂时不单独刷：**大而全的算法题、深度学习公式推导、医学百科、复杂分布式系统。除非面试反馈明确要求，再扩。

## 训练材料

- [`CORE_12.md`](./CORE_12.md)：12 道核心题。覆盖整个面试面，不继续无上限加题。
- [`QUESTION_ENGINE.md`](./QUESTION_ENGINE.md)：给 GPT / Claude / Codex 的出题协议。每次只出 1 题，并针对弱点生成变式。
- [`RUBRIC.md`](./RUBRIC.md)：统一评分标准。避免“感觉会了”。
- [`REFERENCE.md`](./REFERENCE.md)：参考思路。**做完题再看。**

## 推荐使用方式

把这个目录或仓库链接给任意 Agent，然后说：

> 按 `interview-core/QUESTION_ENGINE.md` 开始面试训练。一次只问一道，不给提示。我回答后按 rubric 严格打分，再决定下一题。

训练循环只有四步：

1. **限时作答**：Coding 30 分钟；设计题 15 分钟。
2. **严格评分**：低于 7/10 就算没掌握。
3. **只补失败点**：同一能力再做 1 个变式，不横向扩题库。
4. **通过即停止**：同一能力连续 2 题 ≥8/10，就转下一能力。

## 面试前最低通过线

- 5 道 Coding 核心模式：至少 4 道可独立完成。
- 3 道 Evaluator/Data 题：必须全部可独立完成。
- 2 道 Eval 设计题：能在 10–15 分钟内形成结构化方案。
- 2 道系统设计题：能讲清 failure recovery、成本、可复现性和扩展性。

不是追求“刷过很多题”，而是追求：**面试官换一下题面，你仍然能从底层模式重新构造答案。**
