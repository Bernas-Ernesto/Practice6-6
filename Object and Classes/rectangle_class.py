class Rectangle:
    def __init__(self, length, width):
        pass
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)
print(rectangle.area())