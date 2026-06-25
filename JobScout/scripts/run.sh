#!/bin/bash
# JobScout 一键搜索脚本
# Usage: bash scripts/run.sh

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

echo "=============================="
echo "  JobScout — 求职搜索"
echo "=============================="

# 检查配置文件
if [ ! -f config/profile.yml ]; then
    echo "❌ 未找到画像文件"
    echo "   请先运行: python3 src/interview.py"
    exit 1
fi

# 执行搜索
python3 src/search.py --profile config/profile.yml "$@"
