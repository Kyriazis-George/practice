# class Restaurant:

#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type 
#         self.number_served = 0

#     def open(self):
#         print(f"the {self.name}, is now open")

#     def closed(self):
#         print(f"the {self.name} restaurant is closed")    

#     def describe(self):
#         print(f"I like this restaurant {self.name} because of the {self.cuisine_type}")

#     def set_number_served(self, number):
#         self.number_served = number
#         print(f"{self.name} has now served {self.number_served} customers .")

#     def increment_number_served(self, number):
#         self.number_served += number
#         print(f"{self.name} has now served {self.number_served} customers")
      

# class IceCreamStand(Restaurant):

#     def __init__(self, name, cuisine_type, flavors = None):
#         super().__init__(name, cuisine_type)
#         if flavors is None:
#             flavors = ["chocolate","vanilla"]
#         self.flavors = flavors    
    
#     def show_flavor(self):
#         print("available flavors")
#         for flavor in self.flavors:
#             print(f", {flavor}")



# first_restaurant = Restaurant("Xanthipi","Traditional")
# other_restaurant = Restaurant("Tre Marie","Italian")

# desserts = IceCreamStand("Xanthipi","Traditional",["chocolate","vanilla","banana"])
# desserts.show_flavor()


# print(f"I like the restaurant {first_restaurant.name}")
# first_restaurant.closed()
# first_restaurant.describe()
# first_restaurant.set_number_served(25)


# print(f"I like the restaurant {other_restaurant.cuisine_type}")
# other_restaurant.open()
# other_restaurant.describe()
# other_restaurant.increment_number_served(40)


# 9 - 7 , 9 - 7

# class user :
    
#     def __init__(self, first_name, second_name):
#         self.first_name = first_name
#         self.second_name = second_name

#     def describe(self):
#         print(f"the first name is {self.first_name} and the second name is {self.second_name}")

   
# class Privilages:
#     def __init__(self, privilages = None):
#         if privilages is None:
#             privilages = ["can delete post", "can delete post", "can ban user"] 
#         self.privilages = privilages    

#     def show_privilages(self):
#         print("list the privilages")
#         for privilage in self.privilages:
#             print(f" admin {privilage}")

    
# class Admin(user):
#     def __init__(self, first_name, second_name, privilages = None):
#         super().__init__(first_name, second_name)
#         self.privilages = Privilages() 


# first_person = user("George","kyriazis")
# second_person = user("Zoi","Antonopoulou")

# print(f"I know this guy {first_person.first_name}")
# first_person.describe()

# print(f"I know this lady {second_person.first_name}, is {second_person.second_name}'s, wife")
# second_person.describe()

# administration = Admin("George", "Kyriazis", ["can delete post", "can delete post", "can ban user"])
# administration.privilages.show_privilages()


# 9 - 9 

