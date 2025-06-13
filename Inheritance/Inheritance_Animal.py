class Animal:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

class Dog(Animal):
    def __init__(self, name, breed, is_trained):
        super().__init__(name, breed)
        self.is_trained = is_trained 
    
    def display_info(self):
        super().display_info()
        print(f"Trained: {'YES' if self.is_trained else 'NO'}")
    
class Cat(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color 
    
    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")
        
def main():
    animal_list = [
        Dog("Kiyoshi", "Pomeranian", True),
        Cat("Raya", "Ragdoll", "Gray")
    ]
    for animal in animal_list: 
        animal.display_info()
        
main()
    