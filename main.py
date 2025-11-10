from core.book import Book
from core.user import User
from core.library import Library

def main():
    library = Library()
    choice = None
    while choice != "7":
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return book\5List available book\n7. Save & Exit")
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
            library.return_book(user_id, book_isbn)

        elif choice == "5":


        
        
        elif choice == "7":
            # save data and exit
            break
        else:
            print("Invalid choice, try again.")

from data.json_convert import *
from core.book import *
from core.user import *
from core.library import *

if __name__ == "__main__":
    l = Library()
    b1 = Book("hello", "yosi")
    b2 = Book("bye", "israel")
    b3 = Book("yooo", "chaim")
    u1 = User("noam")
    u2 = User("nir")
    l.add_book(b1)
    l.add_book(b2)
    l.add_book(b3)
    l.add_user(u1)
    l.add_user(u2)
    #l.borrow_book(u1.get_user_id(), b1.get_isbn())

    convert_to_json(l)