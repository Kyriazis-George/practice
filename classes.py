# # # class Dog:

# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age

# # #     def sit(self):
# # #         print(f"{self.name} is sitting.")

# # #     def roll_over(self):
# # #         print(f"{self.name} rolled over!")



# # # my_dog = Dog('Willie', 6)
# # # your_dog = Dog('Lucy', 3)


# # # print(f"my dog's name is {my_dog.name}.")
# # # print(f"my dogs age is {my_dog.age}")
# # # my_dog.sit()

# # # print(f"my dog's name is {your_dog.name}.")
# # # print(f"my dogs age is {your_dog.age}")
# # # your_dog.roll_over()

# # # class Restaurant:

# # #     def __init__(self, name, cuisine_type):
# # #         self.name = name
# # #         self.cuisine_type = cuisine_type 

# # #     def open(self):
# # #         print(f"the {self.name}, is now open")

# # #     def closed(self):
# # #         print(f"the {self.name} restaurant is closed")    

# # #     def describe(self):
# # #         print(f"I like this restaurant {self.name} because of the {self.cuisine_type}")

# # # first_restaurant = Restaurant("Xanthipi","Traditional")
# # # other_restaurant = Restaurant("Tre Marie","Italian")

# # # print(f"I like the restaurant {first_restaurant.name}")
# # # first_restaurant.closed()
# # # first_restaurant.describe()

# # # print(f"I like the restaurant {other_restaurant.cuisine_type}")
# # # other_restaurant.open()
# # # other_restaurant.describe()

# # class user :
    
# #     def __init__(self, first_name, second_name):
# #         self.first_name = first_name
# #         self.second_name = second_name

# #     def describe(self):
# #         print(f"the first name is {self.first_name} and the second name is {self.second_name}")

# # first_person = user("George","kyriazis")
# # second_person = user("Zoi","Antonopoula")

# # print(f"I know this guy {first_person.first_name}")
# # first_person.describe()

# # print(f"I know this lady {second_person.first_name}, is {second_person.second_name}'s, wife")
# # second_person.describe()

# # # class Car:
# # #     def __init__(self, make, model, year):
# # #         self.make = make
# # #         self.model = model
# # #         self.year = year
# # #         self.odometer_reading = 23  # default starting value
       
# # #     def get_descriptive_name(self):
# # #         long_name = f"{self.year} {self.make} {self.model}"
# # #         return long_name.title()

# # #     def read_odometer(self):
# # #         print(f"This car has {self.odometer_reading} miles on it.")

# # #     def update_odometer(self, mileage):
# # #         if mileage >= self.odometer_reading:
# # #             self.odometer_reading = mileage
# # #         else:
# # #             print("You can't roll back an odometer!")

# # #     def increment_odometer(self, miles):
# # #         if miles >= 0:
# # #             self.odometer_reading += miles
# # #         else:
# # #             print("You can't roll back an odometer!")


# # # # ✅ Using the class
# # # my_used_car = Car('audi', 'a4', 2019)
# # # print(my_used_car.get_descriptive_name())

# # # my_used_car.update_odometer(23_500)   # set mileage properly
# # # my_used_car.read_odometer()           # check mileage

# # # my_used_car.increment_odometer(100)   # add miles
# # # # my_used_car.read_odometer()


        
# class Restaurant:

#     def __init__(self, name, cuisine_type,):
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
      

# first_restaurant = Restaurant("Xanthipi","Traditional")
# other_restaurant = Restaurant("Tre Marie","Italian")


# print(f"I like the restaurant {first_restaurant.name}")
# first_restaurant.closed()
# first_restaurant.describe()
# first_restaurant.set_number_served(25)


# print(f"I like the restaurant {other_restaurant.cuisine_type}")
# other_restaurant.open()
# other_restaurant.describe()
# other_restaurant.increment_number_served(40)

# # class User:
    
# #     def __init__(self, first_name, second_name):
# #         self.first_name = first_name
# #         self.second_name = second_name
# #         self.login_attempts = 0  # initialize login attempts

# #     def describe(self):
# #         print(f"The first name is {self.first_name} and the second name is {self.second_name}")

# #     def set_login_attempts(self, attempt):
# #         self.login_attempts = attempt
# #         print(f"There are {self.login_attempts} login attempts")

# #     def increment_login_attempts(self, amount=1):
# #         self.login_attempts += amount    
# #         print(f"There are {self.login_attempts} attempts")

# #     def reset_login_attempts(self):
# #         self.login_attempts = 0
# #         print("Login attempts have been reset")

# #     def greet_user(self):
# #         print(f"hi {self.second_name}, welcome back")




# # # Create users
# # first_person = User("George", "Kyriazis")
# # second_person = User("Zoi", "Antonopoula")
# # third_person = User("Anastasia", "Georganta")
# # fourth_person = User("Mike", "Labrakis")

# # print(f"I know this guy {first_person.first_name}")
# # first_person.describe()

# # print(f"I know this lady {second_person.first_name}, she is {second_person.second_name}'s wife")
# # second_person.describe()

# # # print("\n -- Testing login attempts ---")
# # # first_person.increment_login_attempts()   # +1
# # # first_person.increment_login_attempts(2) # +2
# # # first_person.set_login_attempts(10)      # set to 10
# # # first_person.reset_login_attempts()  

# # print(f"hi {first_person.first_name} {first_person.second_name}, welcome back")
# # third_person.greet_user()

# # group = (first_person, second_person, third_person, fourth_person)
# # for person in group:
# #     print(f"Hi {person.first_name}, how are you?")

# # for person in group:
# #     person.greet_user()

# # class Admin(User):
# #     def __init__(self,
        

# Smartphone Simulator 

class Phone:
    def __init__ (self, brand, model, battery, storage, apps_installed = None) :
        self.brand = brand
        self.model = model
        self.battery = battery
        self.storage = storage
        self.apps_installed = apps_installed if apps_installed else[]
        self.use_hours = 5
        self.battery_level = 10
        self.storage = 100
        
    
    def description(self):
         get_full_description = f"{self.brand} {self.model} {self.battery} {self.storage} {self.apps_installed} "
         return get_full_description.title()

    def install_app(self, app_name):
        self.app_name = app_name
        print(f"I have another app, {self.app_name}")

    def use_phone(self):
        
        print(f"this phone can stay open after {self.use_hours} hours of use")

    def update_use(self, hours):
        self.use_hours += hours
        print(f"use update {self.use_hours}")

    def charge_phone(self,level):
        self.battery_level += level
        print(f"my phone's current battery level is {self.battery_level}")
         

    def charge_range(self):
        if self.battery_level <= 40:
            range = 5
        elif self.battery_level >= 40:
            range = 10

        print(f"this phone can work about {range} hours on a full charge")        
    
class Battery(Phone):
    def __init__(self, brand, model, battery, storage, apps_installed = None):
        super().__init__(brand, model, battery, storage, apps_installed)
        self.capacity = battery
        self.charge_level = 70
        self.battery_level = battery
        
      

    def drain(self, amount):
        if amount < 0:
            print("Drain amount must be positive")
            return
        self.battery_level -= amount   
        if self.battery_level < 0:
            self.battery_level = 0

        print(f"Battery drained by {amount}%, current level {self.battery_level}%")    
        return self.battery_level
    

    def recharge(self, amount):
        if amount <= 0:
            print("recharge amount shold be positive" )
            return
        self.battery_level +=amount
        if self.battery_level > 100:
           self.battery_level = 100

        print(f"battery charged by {amount}%, current level {self.battery_level}%")
        return self.battery_level    
        
    def upgrate_battery(self,extra_capacity):
        if extra_capacity <= 0:
            print("capacity amount should be positive")
            return
        self.battery_level += extra_capacity
        print(f"capacity upgrated by {extra_capacity}% New capacity is {self.capacity}%")

        self.battery_level -= extra_capacity
        print(f"capacity fully charged to {self.battery_level}% after upgrate")

    def level_warning(self):
        self.battery_level = 85
        if self.battery_level <= 20:
            print (f"Your battery level is {self.battery_level} %, you need to find a charger")

        elif self.battery_level <= 40:
            print (f"you battery level is {self.battery_level}% you are ok for now")

        elif self.battery_level <=70:
            print(f"you battery level is{self.battery_level}% you have enough battery for the whole day")
        
        elif self.battery_level <=90:
            print(f"you battery level is {self.battery_level}% you are almost full charched")

        else:
            print(f"you are fully charched")            



    def get_battery_range(self):
        if self.battery_level <= 40:
            range = 6 
        elif self.battery_level <= 65:
            range = 10     

        elif self.battery_level <= 85:
            range = 14    
        
        else:
            range = 24

        print(f"this phone can stay open for {range} in this battery level")    


    def update_storage(self, extra_storage):
        if self.storage <= 0:
            print("any value should be positive")

            self.old_storage = self.storage
            self.new_storage = extra_storage
            return
        self.old_storage +=extra_storage
        print(f"your storage is {extra_storage}, so your full storage is {self.old_storage}")

        self.old_storage -=extra_storage
        print(f"your storage is {extra_storage}, so your full storage is {self.old_storage}")
           









my_phone = Phone("huawei","p20","100","100mb","Uber Taxi")
print(my_phone.description())
print(f"my phone is made by {my_phone.brand}, and is has {my_phone.apps_installed} app ")

my_phone.install_app("instagram")
my_phone.use_phone()
my_phone.use_hours = 10
my_phone.battery_level = 0
my_phone.charge_phone(10)
my_other_phone = Phone("Plus1","Elite","85","256","DropBox")
print(my_other_phone.description())
my_other_phone.update_use(10)
my_other_phone.use_phone()
my_Battery = Battery(brand = "Huawei",model = "P20",battery = 100, storage = "128GB")
my_Battery.drain(30)
my_Battery.drain(50)
my_Battery.recharge(30)
my_Battery.upgrate_battery(50)
my_Battery.level_warning()
my_Battery.get_battery_range()
my_Battery.update_storage(20)

