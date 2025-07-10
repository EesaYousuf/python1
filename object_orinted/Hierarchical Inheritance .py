# Base class
class Parent:
    def home(self):
        print("Parent: Owns a house.")
# First derived class
class Son(Parent):
    def bike(self):
        print("Son: Owns a bike.")
# Second derived class
class Daughter(Parent):
    def car(self):
        print("Daughter: Owns a car.")
