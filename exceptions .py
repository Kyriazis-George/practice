# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# print("Give me to numbers and I'll divide them")
# print("enter 'q' to quit")

# while True:
#     first_number = input("\nFirst number :")
#     if first_number == 'q':
#         break
#     second_number = input("second number:")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number)/ int(second_number)
#     except ZeroDivisionError:    
#         print("you can't divide by 0!")
#     else:
#         print(answer)   

# from pathlib import Path

# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print (f"sorry ,{path} does not exists")    

# f = open("George.txt")
# print(f.readline())
# f.close()

# with open("George.txt")as f:
#     for x in f:
#         print(x*2)

# # f = open("mylife.txt","x")
# with open("mylife.txt", "a") as f:
#     f.write("there is a small content in this file")
# with open("mylife.txt") as f:
#     print(f.read())


# with open("George.txt",encoding="utf-8") as f:
#     contents = f.read()

# from pathlib import Path
# path = Path("numbers.txt")
# contents = path.read_text()
# contents = contents.rstrip()
# print(contents)

# contents = path.read_text().rstrip()

# from pathlib import Path
# path = Path("numbers.txt")
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

from pathlib import Path

path = Path('numbers.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))