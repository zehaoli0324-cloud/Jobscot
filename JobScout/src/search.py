#!/usr/bin/env python3
"""JobScout 搜索入口
用法:
  python3 src/search.py --profile config/profile.yml
  python3 src/search.py --title "AI审计" --location "北京"
"""

import argparse
import sys
import os
import yaml

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from browser_search import CDPBrowser, WebSearch
from analyze import JobAnalyzer
from report import generate_report


def load_profile(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def build_search_terms(profile: dict) -> list:
    """根据画像生成搜索词"""
    terms = []
    title = profile.get("target_title", "")
    location = profile.get("location", "")
    keywords = profile.get("keywords", [])

    # 主搜索词
    base = f"{title} {location}" if location else title
    terms.append(base)

    # 附加关键词组合
    for kw in keywords[:3]:
        if kw not in base:
            terms.append(f"{title} {kw} {location}")

    return terms


def main():
    parser = argparse.ArgumentParser(description="JobScout 求职搜索")
    parser.add_argument("--profile", default="config/profile.yml",
                        help="画像配置文件路径")
    parser.add_argument("--title", help="目标岗位（覆盖 profile）")
    parser.add_argument("--location", help="地点（覆盖 profile）")
    parser.add_argument("--no-browser", action="store_true",
                        help="不使用浏览器引擎（仅 HTTP）")
    args = parser.parse_args()

    # 加载画像
    profile_path = args.profile
    if not os.path.exists(profile_path):
        print(f"❌ 找不到画像文件: {profile_path}")
        print("请先运行 python3 src/interview.py 建立画像")
        sys.exit(1)

    profile = load_profile(profile_path)
    if args.title:
        profile["target_title"] = args.title
    if args.location:
        profile["location"] = args.location

    title = profile.get("target_title", "")
    location = profile.get("location", "")
    print(f"\n🔍 搜索: {title} @ {location}")
    print("=" * 50)

    # 生成搜索词
    terms = build_search_terms(profile)
    print(f"📝 关键词: {terms}")

    all_jobs = []

    # 通道一：CDP 浏览器（如果可用）
    if not args.no_browser:
        print("\n🌐 尝试 CDP 浏览器引擎...")
        browser = CDPBrowser()
        if browser.connect():
            print("✅ CDP 浏览器已连接")
            for term in terms:
                print(f"  搜索: {term}")
                jobs = browser.search_boss(term, location)
                all_jobs.extend(jobs)
                import time
                time.sleep(2)
        else:
            print("⚠️  CDP 浏览器不可用，降级到 HTTP 引擎")
            print("   如需启用: 确保 Chrome 以 --remote-debugging-port=9222 启动")
            args.no_browser = True

    # 通道二：HTTP 搜索引擎
    print("\n🔎 HTTP 搜索引擎...")
    web = WebSearch()
    for term in terms:
        print(f"  搜索: {term}")
        jobs = web.search_job_sites(term, location)
        all_jobs.extend(jobs)
        import time
        time.sleep(1.5)

    print(f"\n📊 原始结果: {len(all_jobs)} 条")

    # 分析和过滤
    analyzer = JobAnalyzer(profile_path)
    filtered = analyzer.filter_and_sort(all_jobs)
    print(f"✅ 匹配岗位: {len(filtered)} 个")

    # 生成报告
    report_file = generate_report(filtered, profile)

    print(f"\n💡 提示: 用 cat {report_file} 查看详细报告")


if __name__ == "__main__":
    main()
