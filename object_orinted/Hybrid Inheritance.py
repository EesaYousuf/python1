# Base class
class Person:
    def info(self):
        print("Person: General info")
# First level derived class
class Father(Person):
    def father_info(self):
        print("Father: Engineer")        
# Second level derived class
class Mother(Person):
    def mother_info(self):
        print("Mother: Doctor")
