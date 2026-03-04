# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. 
# The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

# Question:
# What is the process to extract data from the wikipedia website using Beautiful Soup in Python? 
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth, Headquarters for the top US companies by Revenue?


import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
response.raise_for_status()
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table", {"class": "wikitable"})

if not table:
    print("Could not find the table on the page. Please inspect page structure.")
else:
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all(["th", "td"])
        cols_text = [col.get_text(strip=True).replace("\u00a0", " ") for col in cols]
        data.append(cols_text)

    with open("largest_us_companies_by_revenue.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

    print(f"✅ Saved {len(data)-1} data rows (plus header) to CSV.")


df = pd.read_csv("largest_us_companies_by_revenue.csv")


df.columns = [col.strip().replace('\n', ' ') for col in df.columns]
print("Columns found:", df.columns)

if 'Revenue(USD millions)' in df.columns:
    df['Revenue(USD millions)'] = (
        df['Revenue(USD millions)']
        .replace(r'[\$,]', '', regex=True)
        .astype(float)
    )


top_revenue = df.sort_values(by='Revenue(USD millions)', ascending=False)
print("\n Top 10 U.S. Companies by Revenue:\n")
print(top_revenue[['Name', 'Revenue(USD millions)']].head(10))



import matplotlib.pyplot as plt

top10 = top_revenue.head(10)
plt.barh(top10['Name'], top10['Revenue(USD millions)'])
plt.gca().invert_yaxis()
plt.title("Top 10 U.S. Companies by Revenue")
plt.xlabel("Revenue(USD millions)")
plt.tight_layout()
plt.show()