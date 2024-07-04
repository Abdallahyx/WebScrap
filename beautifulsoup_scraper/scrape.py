import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

urls_df = pd.read_excel("../urls.xlsx")
urls = urls_df["URL"].tolist()

products = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for product in soup.select("div.product"):
        name = product.select_one("a.product-title").text
        price = product.select_one("span.product-price").text
        review = product.select_one("div.product-review").text
        products.append({"name": name, "price": price, "review": review})

with open("output.json", "w") as f:
    json.dump(products, f, indent=4)
