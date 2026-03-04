import requests
from bs4 import BeautifulSoup
import csv

url ="https://en.wikipedia.org/wiki/List_of_aircraft_of_World_War_II"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_ = "wikitable")
print(f"has been found{len(tables)} tables")



selected_tables = tables[0:3]



all_rows = []

for table in selected_tables:
    rows = table.find_all("tr")

    for row in rows:
        cols = row.find_all(["td","th"])
        data = [c.text.strip() for c in cols] 

        if data:
            all_rows.append(data)


with open("ww2_aircraft.csv", "w", newline="", encoding= " utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(all_rows)

print(" file with the name ww2_aircraft.csv is ready")

