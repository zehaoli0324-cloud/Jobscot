# START DEEPSEEK — 复制这一段即可开始

把本仓库链接发给 DeepSeek，然后附上下面这段话：

```text
这是我的“小荷健康/字节医疗大模型评测与数据工程”技术面训练仓库。

请先读取仓库中的：
DEEPSEEK_TUTOR.md
LEETCODE_CORE_15.md
ROADMAP_7D.md
RUBRIC.md
PROGRESS.md
CORE_12.md

然后严格按照 DEEPSEEK_TUTOR.md 训练我。

要求：
1. 一次只出一道题；
2. 在我回答前不要告诉我 LeetCode 编号、题名、标签、算法模式或答案；
3. Coding 用 Python；
4. 我答完后严格评分，不要给鼓励分；
5. 如果我错了，先定位最致命的一个问题，再做最小教学，不要立刻贴完整答案；
6. 根据我的表现自动决定 RETRY / VARIANT / ADVANCE / MINI-LESSON；
7. 每完成 5 题做一次极简 checkpoint；
8. Coding 占约 75%，Eval/Data/System 占约 25%；
9. 不扩展成 Hot100 或大而全题库；
10. 现在直接开始第一题，不要先总结仓库，也不要展示完整题单。
```

## 后续怎么回复

正常情况下，你只需要：

- 直接回答题目；
- 如果代码没写完，说“还没写完”；
- 想要一级提示，说“提示 1”；
- 再卡住，说“提示 2”；
- 想看完整参考解法时明确说“看答案”；
- 每轮结束后说“继续”。

不要每轮重新贴启动 prompt。

## 建议

尽量在同一个 DeepSeek 对话里完成一整天训练，因为教练需要利用前几题的分数和错误类型做自适应选题。

如果换了新对话，把上一次的 5-question checkpoint 一起贴进去即可恢复大部分训练状态。