class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self, message="Hello World!"):
        print(message)

    def introduce(self):
        print(f"I'm {self.name}.")
        print(f"My age is {self.age}.")
        
class Student(Person):
    def __init__(self, name, age,
            	year_level, course):
        super().__init__(name, age)
        self.year_level = year_level
        self.course = course

    def state_course(self):
        print(f"I'm taking up {self.course}")

    def state_school(self, school):
        print(f"I'm studying in {school}")

student_1 = Student("Abrianne", 20, 2, "BSIT")
student_1.introduce()
student_1.state_course()
student_1.state_school("PUP-T")