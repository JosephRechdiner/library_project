class Book:
    ISBN_counter = "1000"

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.ISBN = Book.ISBN_counter
        self.is_available = True

        Book.ISBN_counter = str(int(Book.ISBN_counter) + 1)

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.ISBN} | {self.checking_available()}"

    def get_isbn(self):
        print("getting  isbn")
        return self.ISBN
    
    def checking_available(self):
        if self.is_available:
            return f"Available"
        return f"Not Available"
    
    def get_book_json_look(self):
        return {"Title": self.title, "Author": self.author, "ISBN": self.ISBN, "is_available": self.checking_available()}
    
