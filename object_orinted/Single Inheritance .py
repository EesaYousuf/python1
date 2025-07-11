# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
      # Create objects
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

dog = Dog("Buddy")
dog.speak()     # Output: Buddy barks.  