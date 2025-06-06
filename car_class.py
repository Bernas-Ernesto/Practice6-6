# Task: Create a class `Car` with attributes make, model, and year.
# Add a method to display car details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year

    def display_info(self):
        print(f"{self.make}, {self.model}, {self.year}")

# Create a car object with user input and call the display_info() method
make = input("Enter a Brand: ")
model = input("Enter a Model: ")
year = input("Year Released: ")
my_car = Car(make, model, year)
my_car.display_info()

