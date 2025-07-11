 Base class
class Grandfather:
    def house(self):
        print("Grandfather: Owns a big house.")
   # Derived class from Grandfather
class Father(Grandfather):
    def car(self):
        print("Father: Owns a car.")
 # Derived class from Father
class Son(Father):
    def laptop(self):
        print("Son: Owns a laptop.")
 # Creating object of Son class
s = Son()

# Accessing all inherited methods
s.house()   # Grandfather's method
s.car()     # Father's method
s.laptop()  # Son's method       
       
     
