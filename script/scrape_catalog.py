import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

products = []

cards = soup.find_all("a")

for card in cards:
    href = card.get("href")

    if href and "/products/" in href:
        name = card.get_text(strip=True)

        if name:
            products.append({
                "name": name,
                "url": href if href.startswith("http") else "https://www.shl.com" + href
            })

# Remove duplicates
unique = {p["url"]: p for p in products}

with open("app/catalog.json", "w") as f:
    json.dump(list(unique.values()), f, indent=2)

print("Saved catalog")