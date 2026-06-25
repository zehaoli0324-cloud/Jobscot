# JobScout — 通用求职猎手

AI 驱动的智能求职搜索系统。不只搜招聘 App，而是**全网搜索**——公司官网、行业社区、社交平台、搜索引擎全覆盖。浏览器自动化基于 CDP (Chrome DevTools Protocol)，复用真实浏览器环境，不触发反爬。

## 功能

- **5 步画像** — 回答 5 个问题，系统了解你的需求
- **全网搜索** — Boss直聘 / LinkedIn / 公司官网 / 行业论坛 / 社交媒体 / 搜索引擎
- **稳键浏览器** — 基于 CDP 协议直连 Chrome，复用真实 Cookie 和登录态
- **智能过滤** — 自动排除不符合条件的岗位，按匹配度排序
- **报告输出** — Markdown 报告，一目了然
- **定时推送** — 可配置 cronjob 每日自动搜索推送（Hermes 环境）

## 快速开始

### 方式一：作为 Hermes Skill 使用（推荐）

```bash
# 1. 加载 skill
skill_view(name='job-scout')

# 2. 开始一次搜索
cd /mnt/d/JobScout
python3 src/interview.py  # 回答5个问题建立画像

# 3. 执行搜索
python3 src/search.py --profile config/profile.yml

# 4. 查看报告
cat output/report-*.md
```

### 方式二：独立 Python 脚本

```bash
pip install requests beautifulsoup4 pyyaml

# 直接传参搜索
python3 src/search.py \
  --title "AI审计" \
  --location "北京" \
  --salary_min 13000 \
  --exclude "事务所"
```

## 项目结构

```
JobScout/
├── README.md
├── config/
│   ├── profile.yml          # 用户画像（5个问题生成）
│   └── questions.yml        # 5个画像问题定义
├── src/
│   ├── interview.py         # 交互式画像采集
│   ├── search.py            # 搜索入口
│   ├── browser_search.py    # CDP 浏览器搜索引擎
│   ├── web_search.py        # HTTP 搜索引擎（备用）
│   ├── analyze.py           # 岗位匹配分析
│   └── report.py            # 报告生成
├── scripts/
│   └── run.sh               # 一键搜索脚本
└── output/                  # 搜索报告输出
```

## 5 个画像问题

系统会问你：

1. **目标岗位** — 你找什么工作？（如 AI审计师、财务BI分析师）
2. **工作地点** — 期望在哪儿？（如北京、上海、远程）
3. **薪资期望** — 月薪或年薪范围？
4. **经验背景** — 几年经验？做过什么？
5. **硬性条件** — 有什么绝对不能接受的吗？（如不要事务所、必须有双休）

## 搜索来源

| 来源 | 方式 | 反爬策略 |
|------|------|---------|
| Boss直聘 | Web 搜索 + 浏览器 | CDP 真实浏览器 |
| 猎聘 | 浏览器 | CDP 真实浏览器 |
| LinkedIn | Web 搜索 | HTTP 请求 |
| 公司官网招聘页 | Web 搜索 | HTTP 请求 |
| 知乎 / 小红书 | Web 搜索 | HTTP 请求 |
| Google / Bing | Web 搜索 | HTTP 请求 |
| 36氪 / 行业媒体 | Web 搜索 | HTTP 请求 |

## 浏览器引擎说明

本系统使用 **CDP (Chrome DevTools Protocol)** 直连用户的 Chrome 浏览器，而非 Playwright/Puppeteer 等自动化框架。

### 优势

- **真实浏览器环境** — 复用你的 Chrome 登录态、Cookie、扩展
- **不被反爬识别** — 无 WebDriver 特征，和真实用户一致
- **支持中文网站** — Boss直聘、猎聘等国内站点不拦截
- **低资源占用** — 不启动额外浏览器实例，直接连已运行的 Chrome

### 前置要求

1. **Chrome/Edge 已安装**（Windows）
2. **启动时开启 CDP 端口**：
   ```
   # Windows PowerShell（关闭所有 Chrome 后执行）
   Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" `
     -ArgumentList "--remote-debugging-port=9222"
   ```
   或用 Edge：
   ```
   Start-Process -FilePath "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" `
     -ArgumentList "--remote-debugging-port=9222"
   ```

### 备用引擎

如果 CDP 连接失败，自动降级为 HTTP 请求引擎（`web_search.py`），使用 requests + BeautifulSoup，带随机 UA 头和代理轮换。

## 配置文件

```yaml
# config/profile.yml
name: "你的名字"
target_title: "AI审计师"          # 目标岗位
location: "北京"                  # 期望地点
salary:
  min: 13000                     # 最低月薪
  max: 30000                     # 期望月薪
  type: "monthly"                # monthly / yearly
experience_years: 3
hard_requirements:
  - "双休"
  - "五险一金"
exclude_conditions:
  - "会计师事务所"
  - "单休"
  - "外包"
keywords: ["AI", "审计", "数据分析", "Python"]
```

## Hermes 定时推送（可选）

如果你在使用 Hermes Agent，可以配置 cronjob 每天自动搜索推送：

```bash
# 创建 cronjob（每天早8点搜索一次）
cronjob create \
  --name "每日岗位搜索" \
  --schedule "0 8 * * *" \
  --skills job-scout \
  --prompt "根据 /mnt/d/JobScout/config/profile.yml 的配置，执行一次全网搜索，筛选匹配岗位，生成报告推送到群聊。"
```

## 报告示例

```markdown
# 求职搜索报告 — 2026-06-25

## 匹配岗位（按匹配度排序）

### 1. ⭐ AI审计工程师 — 某互联网大厂（北京）
- **薪资**: 20K-35K × 14薪
- **要求**: 3年以上审计/数据分析经验
- **匹配**: 技能 ✅ 地点 ✅ 薪资 ✅
- **来源**: Boss直聘
- **链接**: https://...
- **推荐理由**: AI审计方向，大厂，薪资符合预期

### 2. 财务BI分析师 — 某科技公司（北京）
...
```

## 许可

MIT
