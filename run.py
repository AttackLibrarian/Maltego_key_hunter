from pastebin_scraper import scrape_pastebin
from crawler import crawl_urls

print("[*] Starting Maltego License Key Hunter...\n")

scrape_pastebin()
crawl_urls()

print("\n[*] Done scanning.")