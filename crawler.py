import requests
from regex_scanner import scan_text
from config import TARGET_URLS, USER_AGENT

def crawl_urls():
    headers = {'User-Agent': USER_AGENT}
    for url in TARGET_URLS:
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                content = res.text
                hits = scan_text(content)
                if hits:
                    print(f"[URL Hit] {url}")
                    for hit in hits:
                        print(f"  >> {hit}")
        except Exception as e:
            print(f"[Error fetching {url}] {e}")