# Task: Create a class `Car` with attributes make, model, and year.
# Add a method to display car details.

class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 
        
    def display_info(self):
        print(f"Brand: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year Released: {self.year}")

make = input("Enter brand: ")
model = input("Enter a model: ")
year = input("Year Released: ")
show_my_car = Car(make, model, year)

show_my_car.display_info()
# Create a car object with user input and call the display_info() method

