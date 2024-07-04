BOT_NAME = "scrapy_scraper"

SPIDER_MODULES = ["scrapy_scraper.spiders"]
NEWSPIDER_MODULE = "scrapy_scraper.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "scrapy_scraper.pipelines.JsonWriterPipeline": 300,
}

FEED_FORMAT = "json"
FEED_URI = "output.json"
