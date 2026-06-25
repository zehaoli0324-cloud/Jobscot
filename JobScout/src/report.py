"""报告生成器"""

import os
from datetime import datetime


def generate_report(jobs: list, profile: dict, output_dir: str = "output"):
    """生成 Markdown 格式的求职报告"""
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"{output_dir}/report-{today}.md"
    # Keep the newest file as report-latest.md too
    latest = f"{output_dir}/report-latest.md"

    lines = []
    lines.append(f"# 求职搜索报告 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append(f"**目标岗位**: {profile.get('target_title', '未设置')}")
    lines.append(f"**地点**: {profile.get('location', '不限')}")
    lines.append(f"**最低薪资**: {profile.get('salary', {}).get('min', 0)}/月")
    lines.append("")
    lines.append("---")
    lines.append("")

    if not jobs:
        lines.append("## 本次未找到匹配岗位")
        lines.append("")
        lines.append("建议调整搜索条件后重试。")
    else:
        lines.append(f"## 匹配岗位（共 {len(jobs)} 个，按匹配度排序）")
        lines.append("")

        for i, job in enumerate(jobs, 1):
            score = job.get("score", 0)
            stars = "⭐" * max(1, min(5, int(score)))

            lines.append(f"### {i}. {stars} {job.get('title', '未命名岗位')}")
            lines.append("")
            lines.append(f"- **来源**: {job.get('source', '未知')}")
            lines.append(f"- **匹配度**: {score:.1f}/5.0")
            if job.get("url"):
                lines.append(f"- **链接**: {job['url']}")
            lines.append("")
            lines.append(f"{job.get('snippet', '')[:400]}")
            lines.append("")
            lines.append("---")
            lines.append("")

    # 搜索建议
    lines.append("## 搜索建议")
    lines.append("")
    lines.append("如果结果不理想，可以尝试：")
    lines.append("- 换更具体的关键词（如 'AI审计' → '审计数字化'）")
    lines.append("- 放宽地点或薪资限制")
    lines.append("- 直接去目标公司官网的招聘页看")

    content = "\n".join(lines)

    with open(filename, "w") as f:
        f.write(content)
    with open(latest, "w") as f:
        f.write(content)

    print(f"\n📄 报告已生成: {filename}")
    print(f"📄 最新报告: {latest}")

    return filename
