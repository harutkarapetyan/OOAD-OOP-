class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"    
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    
    def table_books(self):
        if len(self.books) == 0:
            print("The library is empty")
        else:
            for book in self.books:
                print(book)
                
    def by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
ob1 = Book("Girq1", "Hexinak1")
ob2 = Book("Girq2","Hexinak2")        
                        
lib = Library()

lib.add_book(ob1)
lib.add_book(ob2)
lib.table_books()                                    
        