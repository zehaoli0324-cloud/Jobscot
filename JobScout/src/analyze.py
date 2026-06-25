"""岗位匹配分析引擎
根据用户画像对搜到的岗位进行评分和过滤。"""

import re
import yaml
from typing import Optional

class JobAnalyzer:
    def __init__(self, profile_path: str = "config/profile.yml"):
        with open(profile_path, "r") as f:
            self.profile = yaml.safe_load(f)
        self._compile_patterns()

    def _compile_patterns(self):
        p = self.profile

        # 最低薪资数字提取
        self.min_salary = 0
        sal = p.get("salary", {})
        if isinstance(sal, dict):
            self.min_salary = sal.get("min", 0)
        elif isinstance(sal, (int, float)):
            self.min_salary = sal

        # 排除关键词
        self.exclude_keywords = []
        for c in p.get("exclude_conditions", []):
            self.exclude_keywords.append(c.lower())

        # 匹配关键词
        self.match_keywords = []
        title = p.get("target_title", "")
        self.match_keywords.append(title.lower())
        for kw in p.get("keywords", []):
            self.match_keywords.append(kw.lower())

        # 地点
        self.location = p.get("location", "").lower()

    def score_job(self, job: dict) -> float:
        """对单个岗位评分，返回 0.0-5.0"""
        text = f"{job.get('title', '')} {job.get('snippet', '')}".lower()
        score = 2.5  # 基础分

        # 排除检查
        for ek in self.exclude_keywords:
            if ek and ek in text:
                return 0.0  # 一票否决

        # 地点匹配
        if self.location and self.location not in ["不限", "远程", "全国"]:
            locs = [self.location, self._city_aliases(self.location)]
            if not any(loc in text for loc in locs):
                score -= 1.0

        # 关键词匹配
        matched = sum(1 for kw in self.match_keywords if kw and kw in text)
        score += matched * 0.5

        # 薪资匹配
        salary_match = re.search(r'(\d+\.?\d*)\s*[Kk千]', text)
        if salary_match:
            sal = float(salary_match.group(1)) * 1000
            if self.min_salary > 0 and sal >= self.min_salary * 0.8:
                score += 1.0
            elif self.min_salary > 0:
                score -= 0.5

        salary_match2 = re.search(r'(\d+\.?\d*)\s*万', text)
        if salary_match2:
            sal = float(salary_match2.group(1)) * 10000 / 12
            if self.min_salary > 0 and sal >= self.min_salary * 0.8:
                score += 1.0

        return max(0.0, min(5.0, score))

    def _city_aliases(self, city: str) -> str:
        alias = {"北京": "bj", "上海": "shanghai", "深圳": "sz",
                 "杭州": "hangzhou", "广州": "gz"}
        return alias.get(city, city)

    def filter_and_sort(self, jobs: list) -> list:
        """过滤并排序"""
        scored = []
        for j in jobs:
            j["score"] = self.score_job(j)
            if j["score"] > 0:
                scored.append(j)
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored
