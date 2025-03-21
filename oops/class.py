class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        return f"your car is {self.brand} model is {self.model}"
car1=car("fukk",2021)
print(car1.display())
print(car1.brand)
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
e1=employee('eesa',23)
e2=employee('sana',23)            
    