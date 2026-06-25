"""5 步画像采集
交互式问答，生成 profile.yml"""

import os
import yaml
from datetime import datetime

QUESTIONS_FILE = "config/questions.yml"
PROFILE_FILE = "config/profile.yml"


def load_questions():
    with open(QUESTIONS_FILE, "r") as f:
        data = yaml.safe_load(f)
    return data.get("questions", [])


def ask_questions(questions: list) -> dict:
    """逐题提问，收集答案"""
    answers = {}
    print("\n" + "=" * 50)
    print("  JobScout — 求职画像（共 5 题）")
    print("=" * 50)
    print("我会问你几个问题，帮你建立求职画像。")
    print("按 Enter 继续...")
    input()

    for q in questions:
        print(f"\n--- 问题 {questions.index(q)+1}/{len(questions)} ---")
        print(f"📌 {q['question']}")
        print(f"  提示：{q['hint']}")
        if not q.get("required", True):
            print("  （选填，直接回车跳过）")

        answer = input("\n你的回答：").strip()
        while q.get("required", True) and not answer:
            print("这个问题必须回答。")
            answer = input("你的回答：").strip()

        answers[q["id"]] = answer

    return answers


def answers_to_profile(answers: dict) -> dict:
    """将问答结果转换为 profile.yml 格式"""
    profile = {
        "name": "",
        "target_title": answers.get("target_title", ""),
        "location": answers.get("location", ""),
        "salary": _parse_salary(answers.get("salary", "")),
        "experience": answers.get("experience", ""),
        "hard_requirements": [],
        "exclude_conditions": _parse_constraints(
            answers.get("constraints", "")),
        "keywords": _extract_keywords(answers),
        "created_at": datetime.now().isoformat(),
    }
    return profile


def _parse_salary(salary_str: str) -> dict:
    """从薪资描述中提取数字"""
    import re
    result = {"min": 0, "max": 0, "type": "monthly"}

    if "年" in salary_str:
        result["type"] = "yearly"
    if "万" in salary_str:
        nums = re.findall(r'(\d+\.?\d*)', salary_str)
        if len(nums) >= 2:
            if result["type"] == "yearly":
                result["min"] = int(float(nums[0]) * 10000 / 12)
                result["max"] = int(float(nums[1]) * 10000 / 12)
            else:
                result["min"] = int(float(nums[0]) * 10000)
                result["max"] = int(float(nums[1]) * 10000)
        elif len(nums) == 1:
            if result["type"] == "yearly":
                result["min"] = int(float(nums[0]) * 10000 / 12)
            else:
                result["min"] = int(float(nums[0]) * 10000)
    elif "K" in salary_str.upper() or "k" in salary_str:
        nums = re.findall(r'(\d+\.?\d*)', salary_str)
        if len(nums) >= 2:
            result["min"] = int(float(nums[0]) * 1000)
            result["max"] = int(float(nums[1]) * 1000)
        elif len(nums) == 1:
            result["min"] = int(float(nums[0]) * 1000)

    return result


def _parse_constraints(constraints_str: str) -> list:
    """解析限制条件为列表"""
    if not constraints_str:
        return []
    parts = [c.strip() for c in constraints_str.replace("，", ",").split(",")
             if c.strip()]
    return parts


def _extract_keywords(answers: dict) -> list:
    """从回答中提取搜索关键词"""
    keywords = set()
    for v in answers.values():
        for word in v.replace("，", ",").replace("、", ",").replace("/", ",").split(","):
            w = word.strip()
            if len(w) >= 2:
                keywords.add(w)
    return list(keywords)


def save_profile(profile: dict):
    dir_name = os.path.dirname(PROFILE_FILE)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(PROFILE_FILE, "w") as f:
        yaml.dump(profile, f, allow_unicode=True, default_flow_style=False)
    print(f"\n✅ 画像已保存到 {PROFILE_FILE}")


def main():
    questions = load_questions()
    answers = ask_questions(questions)
    profile = answers_to_profile(answers)
    save_profile(profile)

    print("\n" + "=" * 50)
    print("  画像完成！你现在可以运行搜索：")
    print(f"  python3 src/search.py --profile {PROFILE_FILE}")
    print("=" * 50)


if __name__ == "__main__":
    main()
