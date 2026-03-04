# Handle exceptions 

# try:
#    print(x)
# except:
#    print("this is exception")    

# try:
#   print("Hello")
# except:
#   print("wrong")
# finally:
#   print("the 'try except' is finished")

# x= -1
# if x<0 :
#     raise Exception("Sorry no numbers belowe zero")

# x= "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# def divide_numbers(a, b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Error: you tried to divide by zero!")
#         result = None
#     except TypeError:
#         print("Error: Both inputs must be numbers")
#         result = None
#     else:
#         print("Division successfull")
#     finally:
#         print("Execution complete")

#     return result

# print(divide_numbers(10,2))
# print(divide_numbers(5,0))
# print(divide_numbers(8,"a"))                    

# try:
#     a = float(input("give me a number for a"))
#     b = float(input("give me a number for b"))
#     result = a/b
# except ValueError:
#     print("both inputs should be numbers")
#     result = None
# except ZeroDivisionError:
#     print("you cannot divide by zero")
#     result = None
# else:
#     print("division successfull", result)      
# finally:
#     print("execution complete") 

     
import builtins
print(dir(builtins))     