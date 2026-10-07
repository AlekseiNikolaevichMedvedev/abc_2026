import json
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
quotes = [
    {
        "text": q.select_one("span.text").get_text(strip=True),
        "author": q.select_one("small.author").get_text(strip=True),
    }
    for q in soup.select("div.quote")
]

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

print(f"Спарсено {len(quotes)} цитат")
