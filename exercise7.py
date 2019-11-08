# EXERCISE 7

# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

import datetime 

class Cars:

    def __init__(self, yearmade, make, model):
        self.yearmade = yearmade
        self.make = make
        self.model = model


    def age(self):
        today = datetime.date.today()
        age = today.year - self.yearmade.year

        if today < datetime.date(today.year, self.yearmade.month, self.yearmade.day):
            age -= 1

        return age

vehicle = Cars(
    datetime.date(2014, 3, 31),
    "Toyota",
    "Vios"
)

print(vehicle.make)
print(vehicle.model)
print(vehicle.age())