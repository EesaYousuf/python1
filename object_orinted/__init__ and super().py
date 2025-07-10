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

