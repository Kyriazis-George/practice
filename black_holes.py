import requests
from bs4 import BeautifulSoup
import csv
import re

def clean(text):
    return re.sub(r"\[.*?\]", "", text).strip()

url ="https://en.wikipedia.org/wiki/List_of_most_massive_black_holes"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

responce = requests.get(url, headers= headers)
responce.raise_for_status()

soup = BeautifulSoup(responce.text, "html.parser")
# print(soup.title.text)

table = soup.find("table",class_ = "wikitable")
rows = table.find_all("tr")

with open("black_holes.csv",mode="w", newline="", encoding= "utf-8" )as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Mass", "Galacy"])

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 3:
            name = clean(cols[0].text)
            mass = clean(cols[1].text)
            galaxy = clean(cols[2].text)

        writer.writerow([name, mass, galaxy])

print("file black_holes.csv is ready ")


