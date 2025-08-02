import requests
from bs4 import BeautifulSoup
from regex_scanner import scan_text
from config import PASTEBIN_ARCHIVE_URL, USER_AGENT

def scrape_pastebin():
    headers = {'User-Agent': USER_AGENT}
    res = requests.get(PASTEBIN_ARCHIVE_URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    paste_links = []
    for a in soup.select('table tr a[href^="/"]'):
        paste_links.append('https://pastebin.com' + a['href'])

    for url in paste_links[:20]:  # Limit to first 20 to be nice
        try:
            paste_res = requests.get(url, headers=headers)
            if paste_res.status_code == 200:
                content = paste_res.text
                hits = scan_text(content)
                if hits:
                    print(f"[Pastebin Hit] {url}")
                    for hit in hits:
                        print(f"  >> {hit}")
        except Exception as e:
            print(f"[Error scraping {url}] {e}")