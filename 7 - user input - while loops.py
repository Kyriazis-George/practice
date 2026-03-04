# rental_car = input("name a car")
# print(f"\n Let me find you a {rental_car}")

#  ------

# number = input("Enter a number of guests")
# number = int(number)

# if number >= 6:
#     print(f"we don't have table for {number}")
# else:
#     print(f"you are {number}, we have an availabe table for you")
# ----

message = "Let me see if the number is a multiple of 10 or not"
number = int(input(message))

if number % 10 == 0:
    print (f"number {number} if multiple of 10"
           f"number {number} is the result of  {number//10} * 10")
else:
    print(f"number {number} it is not") 