class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = Book(title, author)
        self.books.append(new_book)

    def show_books(self):
        if not self.books:
            print("No Books available in the library.")
        else: 
            print("Books available in the library: ")
            for book in self.books:
                print(f"{book.title} by {book.author}")
                
library = Library()

for i in range(3):
    library.add_book()
    
library.show_books()



