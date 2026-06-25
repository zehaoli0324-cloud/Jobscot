"""CDP (Chrome DevTools Protocol) 浏览器搜索引擎
复用用户真实 Chrome 浏览器，不触发反爬，支持复杂页面交互。
备用降级到 HTTP 搜索引擎。"""

import json
import time
import random
import requests
import urllib.parse
from typing import Optional

class CDPBrowser:
    """通过 CDP 直连 Chrome/Edge 控制浏览器"""

    def __init__(self, host="127.0.0.1", port=9222, timeout=15):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.ws_url = None
        self._session_id = None

    def connect(self) -> bool:
        """尝试连接本地 Chrome CDP"""
        try:
            r = requests.get(f"http://{self.host}:{self.port}/json/version",
                             timeout=3)
            if r.status_code == 200:
                data = r.json()
                self.ws_url = data.get("webSocketDebuggerUrl")
                return True
        except:
            pass
        return False

    def list_tabs(self):
        """列出所有打开的标签页"""
        r = requests.get(f"http://{self.host}:{self.port}/json",
                         timeout=3)
        return r.json() if r.status_code == 200 else []

    def search_boss(self, keyword: str, city: str = "") -> list:
        """在 Boss 直聘搜索岗位"""
        encoded = urllib.parse.quote(keyword)
        city_param = f"&city={urllib.parse.quote(city)}" if city else ""
        url = f"https://www.zhipin.com/web/geek/job?query={encoded}{city_param}"
        return self._search_web(url, f"Boss直聘 {keyword} {city}")

    def search_generic(self, keyword: str, site: str = "") -> list:
        """通用网页搜索"""
        site_q = f"site:{site} " if site else ""
        query = urllib.parse.quote(f"{site_q}{keyword} 招聘")
        url = f"https://www.google.com/search?q={query}"
        return self._search_web(url, f"Web {keyword}")

    def _search_web(self, url: str, label: str) -> list:
        """通过 CDP 打开页面并提取内容"""
        tabs = self.list_tabs()
        if not tabs:
            return []

        target = tabs[0]
        ws_url = target.get("webSocketDebuggerUrl")
        if not ws_url:
            return []

        import websocket
        try:
            ws = websocket.create_connection(ws_url, timeout=self.timeout)

            # 导航到目标 URL
            self._cdp_send(ws, "Page.navigate", {"url": url})
            time.sleep(random.uniform(2, 4))

            # 获取页面内容
            result = self._cdp_send(ws, "Runtime.evaluate",
                                     {"expression": "document.body.innerText"})
            ws.close()

            text = ""
            if result and "result" in result:
                text = result["result"].get("result", {}).get("value", "")

            return self._parse_results(text, label)

        except Exception as e:
            return [{"title": f"[CDP 错误] {label}", "url": url,
                     "snippet": str(e), "source": label, "score": 0}]

    def _cdp_send(self, ws, method: str, params: dict) -> dict:
        """发送 CDP 命令"""
        msg = json.dumps({"id": 1, "method": method, "params": params})
        ws.send(msg)
        resp = ws.recv()
        return json.loads(resp)

    def _parse_results(self, text: str, label: str) -> list:
        """从页面文本中提取岗位信息"""
        results = []
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        # 简单启发式提取含薪资/岗位关键词的行
        salary_keywords = ["K", "k", "万", "千", "薪资", "工资", "面议", "薪"]
        job_keywords = ["招聘", "岗位", "职位", "任职", "要求", "职责", "经验"]

        job_blocks = []
        current = []
        for line in lines:
            if any(k in line for k in salary_keywords) and any(k in line for k in job_keywords):
                if current:
                    job_blocks.append("\n".join(current))
                    current = []
            current.append(line)
        if current:
            job_blocks.append("\n".join(current))

        for i, block in enumerate(job_blocks[:20]):
            results.append({
                "title": f"{label} — 岗位 {i+1}",
                "snippet": block[:300],
                "source": label,
                "score": 1.0,
                "url": ""
            })

        return results


class WebSearch:
    """HTTP 请求搜索引擎（备用 / 免浏览器场景）"""

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/125.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    SEARCH_URLS = {
        "google": "https://www.google.com/search?q={q}&hl=zh-CN",
        "bing": "https://www.bing.com/search?q={q}&setlang=zh-CN",
        "baidu": "https://www.baidu.com/s?wd={q}",
        "zhihu": "https://www.zhihu.com/search?type=content&q={q}",
        "xhs": "https://www.xiaohongshu.com/search_result?keyword={q}&type=1",
    }

    def __init__(self, proxy: Optional[str] = None):
        self.proxy = proxy
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}

    def search(self, keyword: str, sources: list = None) -> list:
        """多来源并行搜索"""
        if sources is None:
            sources = ["bing", "google", "zhihu"]

        all_results = []
        q = urllib.parse.quote(keyword)

        for src in sources:
            if src not in self.SEARCH_URLS:
                continue
            url = self.SEARCH_URLS[src].format(q=q)
            try:
                r = self.session.get(url, timeout=10)
                if r.status_code == 200:
                    results = self._parse_html(r.text, src)
                    all_results.extend(results)
                time.sleep(random.uniform(1, 2))
            except:
                continue

        return all_results

    def _parse_html(self, html: str, source: str) -> list:
        """简单从 HTML 中提取文本段落"""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        texts = soup.get_text(separator="\n", strip=True)
        lines = [l for l in texts.split("\n") if len(l) > 30]
        results = []
        for line in lines[:30]:
            results.append({
                "title": f"[{source}] {line[:60]}",
                "snippet": line[:300],
                "source": source,
                "score": 0.5,
                "url": ""
            })
        return results

    def search_job_sites(self, keyword: str, location: str = "") -> list:
        """专门搜索招聘平台"""
        queries = [
            f"{keyword} 招聘 {location}",
            f"{keyword} 岗位 {location} 薪资",
            f"site:zhipin.com {keyword} {location}",
            f"site:liepin.com {keyword} {location}",
            f"site:linkedin.com {keyword} {location} 招聘",
        ]
        all_results = []
        for q in queries:
            results = self.search(q, sources=["bing", "google"])
            all_results.extend(results)
            time.sleep(random.uniform(1, 2))
        return self._dedup(all_results)

    def _dedup(self, results: list) -> list:
        """简单去重"""
        seen = set()
        unique = []
        for r in results:
            key = r["snippet"][:80]
            if key not in seen:
                seen.add(key)
                unique.append(r)
        return unique
