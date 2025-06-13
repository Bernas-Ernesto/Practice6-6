#Class name = BFT
#Attributes = name, age, birthday, address, status
#Methods = user input, summary

class BFT:
    def __init__(self, name = "", age = 0, birthday = "", 
                 address = "", status = ""):
        self.name = name 
        self.age = age 
        self.birthday = birthday 
        self.address = address 
        self.status = status 
    
    def family_name(self):
        self.name = input("Enter Name: ")
    
    def family_age(self):
        self.age = input("Enter Age: ")

    def family_birthday(self):
        self.birthday = input("Enter birthday: ")
        
    def family_address(self):
        self.address = input("Enter address: ")
    
    def family_status(self):
        self.status = input("Enter status: ")
        
    def summary(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Birthday: {self.birthday}")
        print(f"Address: {self.address}")
        print(f"Status: {self.status}")
        
info = BFT()
info.family_name()
info.family_age()
info.family_birthday()
info.family_address()
info.family_status()

info.summary()