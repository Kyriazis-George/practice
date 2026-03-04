# class Car:
#     def __init__(self, make, model, year, ):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # default starting value
       
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("You can't roll back an odometer!")

# class Battery:

#     def _init_ (self, battery_size = 40):
#         self.battery_size = battery_size         

#     def describe_battery(self):
#         print(f"this car has {self.battery_size} -kwh battery")


# class ElectricCar(Car):

#     def __init__(self, make, model, year, battery_size= 40):
#         super().__init__(make, model, year)
#         self.battery = Battery(battery_size)


#     def describe_battery(self):
#         self.battery.describe_battery()

#     def vehicle_description(self):
#         return f"{self.year} {self.make} {self.model} with {self.battery_size} - kwh"

#     def fill_gas_tank(self):
#         print(f"this car has no gas tank, but only a buttery with size {self.battery_size} kwh")

   
    

# my_used_car = Car('audi', 'a4', 2019)
# print(my_used_car.get_descriptive_name())

# new_description = ElectricCar(2023, "audi", "new", "80" )
# print(new_description.vehicle_description())

# my_used_car.update_odometer(23_500)   # set mileage properly
# my_used_car.read_odometer()           # check mileage

# my_used_car.increment_odometer(100)   # add miles
# my_used_car.read_odometer()           

# my_leaf = ElectricCar("Nissan", "leaf", "2024")
# print(f"{my_leaf.get_descriptive_name()}")

# my_leaf.describe_battery()

# my_leaf.fill_gas_tank()

# my_leaf.battery.describe_battery()



class Car:

    def __init__(self,make,model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it ")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles             

class Battery:

    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    

    def describe_battery(self):
        print(f"This car a {self.battery_size}-kwh battery")


    def get_range(self):
        if self.battery_size == 40:
            car_range = 150
        elif self.battery_size == 65:
            car_range = 225

        print(f"This car can go about {car_range} miles on a full charge")

   
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

        


my_leaf = ElectricCar('nissan','leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.get_range()
my_leaf.battery.describe_battery()




my_used_car = Car("Subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())

my_new_car = Car('Audi','a4', 2024)
print(my_new_car.get_descriptive_name())            

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()     

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("\nUpgrading the battery...")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()


