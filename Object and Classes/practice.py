"""class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
user_1 = User(1, "John")
user_2 = User(2, "Jane")

print(f"{user_1.name} - {user_1.id}")
print(f"{user_2.name} - {user_2.id}")"""

"""class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)"""

"""try:
    x = 10 / 0
    print("No errors happened!")
except Exception as e:
    print(e)"""
    
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 / num2
    
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is {result}.")
finally:
    print("Thank you for using the program.")


