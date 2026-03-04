import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Waffen-SS_units"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

# Download page
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")

# Sections to extract
sections = [
    "Waffen-SS_divisions",
    "SS_corps",
    "Other_units",
    "Foreign_legions"
]

# Dictionary to hold lists of units
units_dict = {}

for sec_id in sections:
    heading = soup.find("span", id=sec_id)
    if heading:
        ul = heading.find_next("ul")
        if ul:
            units_list = [li.get_text(strip=True) for li in ul.find_all("li")]
            units_dict[sec_id] = units_list

# Example: Access the lists
print("Waffen-SS Divisions:", units_dict.get("Waffen-SS_divisions", [])[:10])
print("SS Corps:", units_dict.get("SS_corps", [])[:10])
print("Other Units:", units_dict.get("Other_units", [])[:10])
print("Foreign Legions:", units_dict.get("Foreign_legions", [])[:10])

import matplotlib.pyplot as plt

# Suppose units_dict is your dictionary of lists
# Example structure:
# units_dict = {
#     "Waffen-SS_divisions": [...],
#     "SS_corps": [...],
#     "Other_units": [...],
#     "Foreign_legions": [...]
# }

# Count units per category
categories = list(units_dict.keys())
counts = [len(units_dict[cat]) for cat in categories]

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(categories, counts, color='skyblue')
plt.title("Number of Waffen-SS Units per Category")
plt.ylabel("Number of Units")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()