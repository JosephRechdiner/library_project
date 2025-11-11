# from user import User
# from book import Book


class Library:

    def __init__(self):
        self._books = []
        self._users = []

    def add_book(self, book):
        self._books.append(book)

    def delete_book(self, book):
        if book in self._books:
            self._books.remove(book)
            return "book deleted"
        else:
            return "book not found"

    def add_user(self, user):
        self._users.append(user)

    def delete_user(self, user):
        if user in self._books:
            self._users.remove(user)
            return "user deleted"
        else:
            return "user not exist"

    def get_user_by_id(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                return user


    def get_book_by_isbn(self, book_isbn):
        for book in self._books:
            if book.get_isbn() == book_isbn:
                return book


    def borrow_book(self, user_id, book_isbn):
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_isbn(book_isbn)
        if user and book:
            if book.is_available:
                book.is_available = False
                user.get_borrowed_books().append(book)
                return True

        return False


    def return_book(self,user_id, book_isbn):
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_isbn(book_isbn)

        if user and book:
            user.get_borrowed_books().remove(book)
            book.is_available = True
            print("sucsses return")
        else:
            print("error")
        
    
    def list_available_books(self):
        available_books = []
        for book in self._books:
            if book.is_available:
                print(book)

        return available_books
    

    def search_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return "book not found"


            







