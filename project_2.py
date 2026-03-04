# # Given the birthdate and name of the person, you want to create a Python program to determine the corresponding Zodiac sign based on the date.



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