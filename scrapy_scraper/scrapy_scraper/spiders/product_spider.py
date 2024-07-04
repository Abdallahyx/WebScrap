import scrapy
import pandas as pd
from scrapy_scraper.items import Product


class ProductSpider(scrapy.Spider):
    name = "product_spider"

    def start_requests(self):
        urls_df = pd.read_excel("../../urls.xlsx")
        urls = urls_df["URL"].tolist()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css("div.product"):
            item = Product()
            item["name"] = product.css("a.product-title::text").get()
            item["price"] = product.css("span.product-price::text").get()
            item["review"] = product.css("div.product-review::text").get()
            yield item
