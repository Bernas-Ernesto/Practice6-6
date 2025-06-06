#class named PUP Student
#attributes name, number, section, course
#methods user input, name, number, section, course, print summary 
class PUPStudent:
    def __init__(self, name = "", number = 0, section = " ", 
                 year = 0, course = ""):
        self.name = name 
        self.number = number 
        self.section = section 
        self.course = course 
        self.year = year

    def student_name(self):
        self.name = input("Name: ")
        
    def student_number(self):
        self.number = input("Student Number: ")

    def student_section(self):
        self.section = input("Enter Section: ")

    def student_year(self):
        self.year = input("Year: ")
        
    def student_course(self):
        self.course = input("Course: ")
        
    def summary(self):
        print("PUP STUDENT")
        print(f"Student Name: {self.name}")
        print(f"Student Number: {self.number}")
        print(f"Student Section: {self.section}")
        print(f"Student Year: {self.year}")
        print(f"Student Course: {self.course}")

pup_student_list = PUPStudent()
pup_student_list.student_name()
pup_student_list.student_number()
pup_student_list.student_course()
pup_student_list.student_section()
pup_student_list.student_year()

pup_student_list.summary()
    
    

