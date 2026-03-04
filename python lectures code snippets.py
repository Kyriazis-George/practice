# student = { "name":"George", "second name": "Kyriazis", "degree": "music"}
# student.update({"student ID": 453})
# # print(type(student))

# print(student.get("degree"))


# age = input("enter you age:")

# print(type(age))

# age_int = int(age)

# if age_int>= 18:
#     "the condition is executed if the condition is True"
#     print(age_int + 2)
#     print("Eligible")

# else:
#     "the condition is executed if the condition is False"
#     print("not eligible")  

# i = 0
# while 0 < 5:
#     print(i)
#     if i == 2:
#         print("breaking loop")
#         break
#     i = i + 1
# print("---")    



# for i in range(10):
#     if i in range(10):
#         if i == 5:
#             print("Breaking Loop")
#             break
#     print(i)

# for i in range(10):
#     if i == 4:
#         print(f"skipping {i}")
#         continue
#     print(i)


# age = int(input("please put your age:"))

# gender = input("enter your gender male or female:")
# if gender == 'male':
#     if age > 18:
#         print("Eligible")

#     else:
#         print("no eligible")    

# else:
#     print("not eligible")


# for i in range(5):
#     for i in range(2):
#         print("Ali")
#     print('Done')    

# for i in range(5):
#     for i in range(3):
#         print("George")
#     print("Done")  

# car = ["bmw", "mercedes", "lada"]
# for i in car:
#     print(i*2)


# age = int(input("enter your age"))
# gender = input("tell me you gender")

# if gender == "male" and age > 18:
#     print("Eligible")
# elif not gender == "male":
#     print(f"you are {gender}, not eligible, you are not male")    
# elif gender =="male" or age > 18:
#     print("partialy eligible")
# else:
#     print("not eligible")        


# def add(num1, num2):
#     result = num1 + num2
#     return result
# answer = add(1, 4)
# print(answer)

# def add(num1 = 5, num2=2):
#     result = num1 + num2
#     return result
# answer= add(1 , 4)
# print(answer)

# def my_func(first_name = "George" , last_name= "Kyriazis"):
#     print(first_name + last_name)

# my_func()
# # my_func(first_name="George", last_name="Kyriazis")
  
# def add(num1, num2):
#     result = num1 + num2
#     return result

# answer = add(1,4)
# print(answer)

# def add(num1 = 5, num2 = 2):
#     result = num1 + num2
#     return result

# answer = add(1, 4)
# print(answer)

# def my_name(name = "George", surname = "Kyriazis"):
#          for i in range(5):
#                   print(name + surname)

# my_name()  
# my_name(name= "Zoi")      

# def add(*nums):
#     result = 0
#     for i in nums:
#         result = result + i
#     print(result)
# add(3, 2, 6, 4, 1)   
# 
# def add(*nums):
#     result = 0
#     for number in nums:
#         result = result + number
#     print(result)
# add(1, 2 , 3, 4 )            

# def square(num):
#     print(num*num)
# square(3)    

# f = lambda num : num * num

# result = f(2)
# print(result)


# f = lambda num1, num2 : num1 + num2
# result = f(2,3)
# print(result)

# def add(num1, num2):
#     print(num1 + num2)
# add(1, 4)    

# from module import add

# add(2,6)

# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


#     def func(self):
#         return f'{self.brand} {self.model}'
    
# myclass = car("toyota", "corolla")

# print(myclass.brand)
# print(myclass.model)
# print(myclass.func())

# class car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

#     def func(self):
#         return f'{self.brand} {self.model}'


# class electric_car(car):
#     def __init__(self, brand, model, batterysize):
#         super().__init__(brand, model)
#         self.batterysize = batterysize

# my_e_class = electric_car("tesla","model s", "85kwh")
# print(my_e_class.brand)
# print(my_e_class.model)
# print(my_e_class.func())   


# first_car = car("subaru","impreza")
# print(first_car.brand)
# print(first_car.func())
        
# encapsulation 

# class car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def func(self):
#         return f'{self.__brand} {self.model}'

#     def get_brand(self):
#         return self.__brand

# class electric_car(car):

#     def __init__(self, brand, model, batterysize):
#         super().__init__(brand, model)
#         self.batterysize = batterysize 



# my_electric_car = electric_car("tesla","model s", "100kwh")
# print(my_electric_car.get_brand())
# print(my_electric_car.func())



# class car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def func(self):
#         return f'{self.__brand} {self.model}'

#     def get_brand(self):
#         return self.__brand
    
#     def fuel_type(self):
#         return "petrol or diesel"

# class electric_car(car):

#     def __init__(self, brand, model, batterysize):
#         super().__init__(brand, model)
#         self.batterysize = batterysize 

#     def fuel_type(self):
#         return "electric charge"


# my_class = car("toyota","corolla")
# print(my_class.fuel_type())

# my_e_class = electric_car("tesla","model s", "100kwh")
# print(my_e_class.fuel_type())     


# x = 4
# try :
#     x/0
# except ZeroDivisionError as e:
#     print(e)



# # try:
# #     x/2
# # except Exception as e:
# #     print(e)
# #     print("error")

# # finally:
# #     print("in finally block")        


# for i in range(10):
#     try:
#         print(i/1)
#     finally:
#         print( i)    

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

#   def info(self):
#     return f'{self.brand} {self.model}'


# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

#   def info(self):
#       return f'{self.brand} {self.model}'

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")


#   def info(self):
#       return f'{self.brand} {self.model}'  

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# for x in (car1, boat1):
#   print(x.move())

# vehicles = [car1, boat1, plane1]

# for vehicle in vehicles:
#          vehicle.move()  
#          print(vehicle.info())


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
      print("move!")    

class Car(Vehicle):
   pass

class Boat(Vehicle):
   def move(self):
      print("Sail")  

class Plane(Vehicle):
   def move(self):
      print("fly !")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")  


for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()