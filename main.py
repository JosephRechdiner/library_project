from core.book import Book
from core.user import User
from core.library import Library

def main():
    library = Library()
    choice = None
    while choice != "7":
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return book\n7. Save & Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            username = input("Enter username: ")
            user = User(username)
            library.add_user(user)

        elif choice == "3":
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            library.borrow_book(user_id, book_isbn)

        elif choice == "4":
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            library.return_book()

        
        
        elif choice == "7":
            # save data and exit
            break
        else:
            print("Invalid choice, try again.")