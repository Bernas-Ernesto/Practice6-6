class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 
        
    def show(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Year Released: {self.year}")

# Create 2 book objects and show details
book = Book("Harry Potter", "J.K Rowling", 2000)
book.show()



