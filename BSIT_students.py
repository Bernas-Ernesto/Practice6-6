#Class: BSIT
#Attributes: name, section
#Methods: user input

class BSIT():
    def __init__(self, name, student_id, section, year):
        self.name = name 
        self.student_id = student_id
        self.section = section 
        self.year = year 
    
class Students():
    def __init__(self):
        self.list_students = []
    
    def add_students_function(self):
        self.name = input("\nEnter Name: ")
        self.student_id = input("Enter Student ID: ")
        self.year = input("Enter Year: ")
        self.section = input("Enter Section: ")
        add_student = BSIT(self.name, self.student_id, self.section, 
                           self.year)
        self.list_students.append(add_student)

    def show_students(self):
        print("\nBSIT STUDENTS")
        for self in self.list_students:
            print(f"\nName: {self.name}")
            print(f"Student ID: {self.student_id}")
            print(f"BSIT {self.year} - {self.section}")
    
show_BSIT = Students()

no_of_students = int(input("Enter number of students: "))
for i in range(no_of_students):
    show_BSIT.add_students_function()

show_BSIT.show_students()
        
    
        
        
        