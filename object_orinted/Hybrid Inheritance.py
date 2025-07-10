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
# Hybrid: inherits from both Father and Mother
class Child(Father, Mother):
    def child_info(self):
        print("Child: Student")


Creating object and calling methods:
python
Copy
Edit
c = Child()

c.info()         # Inherited from Person
c.father_info()  # From Father
c.mother_info()  # From Mother
c.child_info()   # Own method