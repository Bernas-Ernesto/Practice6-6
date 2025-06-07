#Class: BSIT
#Attributes: name, section
#Methods: user input

class BSIT():
    def __init__(self, name = "", student_ID = "", year = "", 
                 section = ""):
        self.name = name 
        self.student_ID = student_ID 
        self.year = year 
        self.section = section 

class Students(): 
    def __init__(self):
        self.list_student = []
    
    def add_student_function(self):
        self.name = input("\nEnter name: ")
        self.student_ID = input("Enter Student ID: ")
        self.year = input("Enter Year Level: ")
        self.section = input("Enter Section: ")
        add_students = BSIT(self.name, self.student_ID, 
                                 self.year, self.section)
        self.list_student.append(add_students)
    
    def show_student_function(self):
        print("\nBSIT STUDENTS")
        for self in self.list_student:
            print(f"Name: {self.name}")
            print(f"Student ID: {self.student_ID}")
            print(f"BSIT {self.year} - {self.section}")

show_BSIT = Students()

no_of_students = int(input("\nEnter number of students: "))
for i in range(no_of_students):
    show_BSIT.add_student_function() 
    
show_BSIT.show_student_function()
        
    
        
        
        