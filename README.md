# Web Scraper and Analyzer

This project includes web scraping scripts using BeautifulSoup and Scrapy to collect product prices and reviews from e-commerce websites. The collected data is then analyzed for comparative pricing and sentiment analysis.

## Project Structure

- **scrapy_scraper**: Contains the Scrapy spider to scrape product data.
- **beautifulsoup_scraper**: Contains the BeautifulSoup script to scrape product data.
- **analysis**: Contains the script to analyze the scraped data.

## Setup

1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`.

## Usage

### Scrapy Scraper

1. Navigate to the `scrapy_scraper` directory.
2. Run the spider: `scrapy crawl product_spider`.

### BeautifulSoup Scraper

1. Navigate to the `beautifulsoup_scraper` directory.
2. Run the scraper: `python scrape.py`.

### Data Analysis

1. Navigate to the `analysis` directory.
2. Run the analysis: `python analyze.py`.

## Results

The scraped data and analysis results are saved in `output.json` and `analysis.csv`, respectively.
