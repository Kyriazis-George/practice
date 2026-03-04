# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. 
# The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

# Question:
# What is the process to extract data from the wikipedia website using Beautiful Soup in Python? 
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth, Headquarters for the top US companies by Revenue?

import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Amazon_(company)"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

intro_paragraph = soup.find("p").get_text().strip()
print("Introduction:")
print(intro_paragraph)


headings = soup.find_all(["h2", "h3"])
for heading in headings:
    text = heading.get_text().replace("[edit]", "").strip()
    print(text)


infobox = soup.find("table", {"class": "infobox vcard"})
infobox_data = []

if infobox:
    for row in infobox.find_all("tr"):
        header = row.find("th")
        value = row.find("td")
        if header and value:
            infobox_data.append([header.get_text(strip=True), value.get_text(strip=True)])
    
    for item in infobox_data:
        print(item)
else:
    print("Infobox not found. Check the page structure or headers.")


if infobox_data:
    with open("amazon_info.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Field", "Value"])
        writer.writerows(infobox_data)
        