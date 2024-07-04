import json
import pandas as pd
from textblob import TextBlob

# Load the scraped data
with open("../beautifulsoup_scraper/output.json") as f:
    data_bs = json.load(f)

with open("../scrapy_scraper/output.json") as f:
    data_scrapy = json.load(f)

# Convert to DataFrame
df_bs = pd.DataFrame(data_bs)
df_scrapy = pd.DataFrame(data_scrapy)

# Combine the DataFrames
df = pd.concat([df_bs, df_scrapy], ignore_index=True)

# Sentiment Analysis
df["sentiment"] = df["review"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Save the analysis
df.to_csv("analysis.csv", index=False)

print(df.describe())
