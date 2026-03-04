#project_1 
# You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.


import random

score_1 = 0
score_2 = 0

while True:
    player_1 = input("rock - paper or scissors ?").lower()
    player_2 = random.choice(["rock","paper","scissors"])
    print(f"computer is {player_2}")

    if player_1 == "scissors" and player_2 == "paper":
        print("player_1 wins")
        score_1 +=10
    
    elif player_1 == "rock" and player_2 == "scissors":
        print("player_1 wins")
        score_1 += 10

    elif player_1 == "paper" and player_2 == "rock":
        print("player_1 wins")
        score_1 +=10

    elif player_1 == player_2:
        print("you are even")

    else:
        print("player 2 wins") 
        score_2 +=10

    cont = input("play again?yes/no").lower()
    if cont != "yes":
        print(f"player 1 ,your final score is {score_1} and for player_2 is {score_2}")
        if score_1 > score_2:
            print("player_1 won the game")
        elif score_1 < score_2:
            print("computer won") 
        else:
            print("you are even")
        break                              

# 2nd way


import random

score_1 = score_2 = 0

while True:
    player_1 = input("rock - paper or scissors ?").lower()
    player_2 = random.choice(["rock","paper","scissors"])
    print(f"computer is {player_2}")

    a = player_1 == "rock" and player_2 == "scissors"
    b = player_1 == "paper" and player_2 == "rock"
    c = player_1 == "scissors" and player_2 == "paper"
    d = player_1 == player_2

    if a or b or c:
        print("player_1 wins")
        score_1 +=10
    elif d:
        print("you are even")

    else:
        print("player_2 wins")
        score_2 +=10

    cont = input("play again?yes/no").lower()
    if cont != "yes":
        print(f"player 1 ,your final score is {score_1} and for player_2 is {score_2}")
        if score_1 > score_2:
            print("player_1 won the game")
        elif score_1 < score_2:
            print("computer won") 
        else:
            print("you are even")
        break      


#project_2
# You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.
# How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?   


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

low = 0
high = len(numbers)-1
while low<= high: 
    mid = (low + high)//2


    if numbers[mid] < target:
        low = mid+1
    elif numbers[mid] > target:
        high = mid -1
    elif numbers[mid] == target:
        print(f"your found the number, {target} was in  {mid}")
    else:
        print(f" found the {target}m is here {numbers}")
        break


# Project_3
# Problem Statement:
# You want to write a Python program that can send emails to one or multiple recipients using an email account.

# Question:
# How can I write a Python program that can send emails to one or multiple recipients using an email account?

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "kyriazis_1987@hotmail.gr"
password = "XXXXXXXXX"

subject = "Email test"
body = "This is my message"

recipients = recipients = {
    "Ali": "ali@example.com",
    "Fatima": "fatima@example.com",
    "Usman": "usman@example.com"
}

msg = MIMEMultipart()
msg['']= sender_email
msg[""] = ",".join(recipients)
msg['']= subject

msg.attach(MIMEText(body))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, password)

    print("email has been sent")

except Exception as e:
    print(f"Error: {e}") 
finally:
    server.quit()       




# project_4

# Given the birthdate and name of the person, you want to create a Python program to determine the corresponding Zodiac sign based on the date.

import pandas as pd


df = pd.DataFrame(columns=["Month", "Day", "Zodiac"])

def zodiac_sign(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Invalid date"

while True:
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    zodiac = zodiac_sign(month, day)
    print(f"Your zodiac sign is {zodiac}")

   
    df = pd.concat([df, pd.DataFrame({"Month": [month], "Day": [day], "Zodiac": [zodiac]})], ignore_index=True)

    
    cont = input("Do you want to add another? (y/n): ")
    if cont.lower() != 'y':
        break


df.to_csv("zodiac_data.csv", index=False)
print("All entries saved to zodiac_data.csv")

# project_5


import os
import glob

directory = input("Enter directory path: ").strip()
pattern = input("Enter file pattern (e.g. *.jpg): ").strip()
new_base_name = input("Enter new base name (e.g. photo_): ").strip()

files = glob.glob(os.path.join(directory, pattern))
print("\nFound files:")
print(files)

if not files:
    print("\n No files found. Check your pattern and directory path.")
else:
    for i, old_path in enumerate(files, start=1):
        ext = os.path.splitext(old_path)[1]
        new_name = f"{new_base_name}{i}{ext}"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {os.path.basename(old_path)} → {new_name}")

# project_6


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

    print(f" Saved {len(data)-1} data rows (plus header) to CSV.")


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

#here I added extra option to watch the graphs.

import matplotlib.pyplot as plt

top10 = top_revenue.head(10)
plt.barh(top10['Name'], top10['Revenue(USD millions)'])
plt.gca().invert_yaxis()
plt.title("Top 10 U.S. Companies by Revenue")
plt.xlabel("Revenue(USD millions)")
plt.tight_layout()
plt.show()