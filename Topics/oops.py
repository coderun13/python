# To map with real world scenarios, we started using objects in code
# Procedural -> functional -> Oops
# Class -> object
# Class is the blueprint for creating objects.
# Constructor: All classes have a fucntion called _init_(), which is always executed when the object is being initiated. 
# Attributes: data or variables
# Default and parmeterized constructors
# Class attributes: same for all objects
# Instance attributes: different for every object
# object attri > class attri
# Methods: functions that belong to objects
# 
# #

class Car:
    brand = "mercedes" #class attribute
    def __init__(self, color, buyer):
        self.color = color
        self.buyer = buyer
        # print("adding new car details...")
    
    def welcome(self):
        print("Your choice is great", self.buyer)
    
    def choice(self):
        print("\nTime to see choice of", self.buyer)



Car1 = Car("red", "snehal")
print(Car1.color)
print(Car1.brand)
Car1.welcome()

Car2 = Car("blue", "aryan")
Car2.choice()
print(Car2.color)
print(Car2.brand)