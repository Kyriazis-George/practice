# my_tupple = ("George", "Theodore", "Georgantas")


# my_tupple.count("Georgantas")
# print(my_tupple.count("Georgantas"))

# numbers = (1, 2, 3, 4, 5, 1, 2, 1)
# largest = max(numbers)
# print("Largest number is:", largest)

# numbers = (1, 2, 3, 4, 5, 1, 2, 1)

# largest = numbers[4]

# for number in numbers:
#     if number > largest:
#         largest = number
# print("Largest number is:", largest)

# smallest = numbers[0]

# for number in numbers:
#     if number < smallest:
#         smallest = number
# print("Smallest number is:", smallest)

# number2 = (1, 2, 3, 4, 5, 1, 2, 1)

# # concatenate = number2 + numbers
# # print(concatenate)
# # print(sum(concatenate))

# my_list = list(number2)
# print(my_list)
# my_list.append(6)
# print(my_list)
# my_tupple = tuple(my_list)
# print(my_tupple)

# my_fruits = ('apple', 'banana', 'cherry')
# if 'banana' in my_fruits:
#     print("Yes, 'banana' is in the fruits tuple")   
    
# numbers = (1, 2, 3, 4, 5, 1, 2, 1)
# # even_sum = 0


# # for number in numbers:
# #     if number % 2 == 0:
# #         even_sum +=number
# #         print(even_sum)

# odd_sum = 0      
# for number in numbers:
#     if number %2 != 0:
#         odd_sum +=number
# print(odd_sum)      

# my_tupple = ("George", "Theodore", "Georgantas")

# reversed = reversed(my_tupple)
# print(tuple(reversed))

# reversed = my_tupple[::-1]
# print(reversed)


# my_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ("Friday morning", "Friday afternoon"))
# print(my_days[5][1])
# my_list = list(my_days)
# print(my_list)
# my_list.insert(6,("Saturday","Saturday afternoon"))
# print(my_list)
# my_tupple = tuple(my_list)


# my_names = ("Alice", "Bob", "Charlie", "Diana", "Ethan")
# for name in my_names:
#     if name.startswith("D"):
#         print(name)

# my_names = ("Alice", "Bob", "Aaron", "Diana", "Ethan")

# starting_with_a = [name for name in my_names if name.startswith("A")]

# print(len(starting_with_a))

 
my_numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# # my_numbers_ascending = sorted(my_numbers)
# # print(my_numbers_ascending)

# my_numbers_descending = sorted(my_numbers, reverse=True)
# print(my_numbers_descending)


# students_subject_scores = [
#     ("Alice", "Math", 88),
#     ("Bob", "Science", 76),
#     ("Charlie", "English", 92),
#     ("Diana", "Math", 85),
#     ("Ethan", "Science", 67),
#     ("Fiona", "English", 90),
#     ("George", "Math", 73),
#     ("Hannah", "Science", 95),
#     ("Ian", "English", 81),
#     ("Jenna", "Math", 78)
# ]

# for student in students_subject_scores:
#     name, subject, score = student
#     if score >= 80:
#         print(f"This student, {name}, reached the score of {score} in {subject.title()}")

# tuple_1 = (1, 2, 3)
# tuple_2 = ("a", "b", "c")

# # tuple_1, tuple_2 = tuple_2, tuple_1

# # print("tuple 1:", tuple_1)
# # print("tuple 2:", tuple_2)
 
# #  --or

# temp = tuple_1
# tuple_1 = tuple_2
# tuple_2 = temp
# print("tuple 1:", tuple_1)
# print("tuple 2:", tuple_2)



# import math

# point1 = (2, 3)
# point2 = (5, 7)

# distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
# print("Distance between points:", distance)


names = ("Alice", "Bob", "Charlie", "Diana", "Ethan", "Alice", "Bob")

unique_names = set(names)
print(unique_names)