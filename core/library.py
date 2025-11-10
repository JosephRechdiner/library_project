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

    def borrow_book(self, user_id, book_isbn):
        user = None
        for c_user in self._users:
            if c_user.get_user_id() == user_id:
                user = c_user
                break

        if not user:
            return "user not exist"

        for book in self._books:
            book.get_isbn() == book_isbn
            break

