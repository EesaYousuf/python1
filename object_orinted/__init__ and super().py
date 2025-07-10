class Grandfather:
    def __init__(self):
        print("Grandfather's constructor called.")

    def house(self):
        print("Grandfather: Owns a big house.")
class Father(Grandfather):
    def __init__(self):
        super().__init__()  # Call Grandfather's constructor
        print("Father's constructor called.")

    def car(self):
        print("Father: Owns a car.")
class Son(Father):
    def __init__(self):
        super().__init__()  # Call Father's constructor
        print("Son's constructor called.")

    def laptop(self):
        print("Son: Owns a laptop.")
