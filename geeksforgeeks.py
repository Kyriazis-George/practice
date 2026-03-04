# def checkOddEven():
#     number = int(input("give me a number"))
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# result = checkOddEven()
# print(result)



# def checkOddEven(x):
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(checkOddEven(6))

      
# class Solution:
#       def checkStatus(self, a, b, flag):
#             if flag == False and((a>=0 and b<0) or(a<0 and b>=0)):
#                    return True
#             if flag == True and(a<0 and b<0):
#                   return False
#             else:
#                   return False
# sol = Solution()
# print(sol.checkStatus(4,5,False))   
# print(sol.checkStatus(4,6,True))

# def friends_in_trouble(j_angry, s_angry):
#     return j_angry == s_angry

# while True:
#     j = input("Is John angry? (true/false): ").strip().lower()
#     s = input("Is Smith angry? (true/false): ").strip().lower()

#     if j == "true":
#         j_angry = True
#     elif j == "false":
#         j_angry = False
#     else:
#         print("invalid input for John")
#         continue

#     if s == "true":
#         s_angry = True
#     elif s == "false":
#         s_angry = False
#     else:
#         print("invalid input for Smith")
#         continue       
    
#     if friends_in_trouble(j_angry, s_angry):
#         print("you are in trouble")
#     else:
#         print("you are safe")     


             
