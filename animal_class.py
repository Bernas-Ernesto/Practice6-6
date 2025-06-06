# Task: Create a base class `Animal` with a method `speak`.
# Create two derived classes `Dog` and `Cat` that override `speak`.

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()