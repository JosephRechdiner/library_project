# from core.book import Book
# from core.user import User
# from core.library import Library
# from data.python_convert import import_jason_data, convert_users_to_python, convert_books_to_python

# def main():
#     library = Library()
#     choice = None
#     while choice != "7":
#         print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return book\5List available book\n7. Save & Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             title = input("Enter book title: ")
#             author = input("Enter book author: ")
#             book = Book(title, author)
#             library.add_book(book)

#         elif choice == "2":
#             username = input("Enter username: ")
#             user = User(username)
#             library.add_user(user)
#         elif choice == "2":
#             username = input("Enter username: ")
#             user = User(username)
#             library.add_user(user)

#         elif choice == "3":
#             user_id = input("Enter user id: ")
#             book_isbn = input("Enter book isbn: ")
#             library.borrow_book(user_id, book_isbn)
#         elif choice == "3":
#             user_id = input("Enter user id: ")
#             book_isbn = input("Enter book isbn: ")
#             library.borrow_book(user_id, book_isbn)

#         elif choice == "4":
#             user_id = input("Enter user id: ")
#             book_isbn = input("Enter book isbn: ")
#             library.return_book(user_id, book_isbn)

#         elif choice == "5":
#             library.list_available_books()

        
#         elif choice == "7":
#             # save data and exit
#             break
#         else:
#             print("Invalid choice, try again.")

# from data.json_convert import *
# from data.python_convert import *
# from core.book import *
# from core.user import *
# from core.library import *


# if __name__ == "__main__":

#     l = Library()
#     books, users = import_jason_data()
#     books = convert_books_to_python(books)
#     users = convert_users_to_python(users)
#     l._users = users
#     l._books = books
#     l.list_available_books()
#     convert_borrowed_books(users, l)

    
#     print(11111111111111)
#     for book in l._books:
#         print(book)
#     l.list_available_books()
    
    # l = Library()
    # b1 = Book("hello", "yosi")
    # b2 = Book("bye", "israel")
    # b3 = Book("yooo", "chaim")
    # u1 = User("noam")
    # u2 = User("nir")
    # l.add_book(b1)
    # l.add_book(b2)
    # l.add_book(b3)
    # l.add_user(u1)
    # l.add_user(u2)
    # l.borrow_book(u1.get_user_id(), b1.get_isbn())


    # convert_to_json(l)

    

from data.json_convert import *
from data.python_convert import *
from core.book import *
from core.user import *
from core.library import *
def main():
    library = Library()
    library_data = import_jason_data()
    library._books = convert_books_to_python(library_data[0])
    library._users = convert_users_to_python(library_data[1])
    convert_borrowed_books(library)

    choice = None
    while choice != "7":
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return book\n5. List available book\n6. Search book\n7. Save & Exit")
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
            if user_id.isdigit():
                user_id = int(user_id)
            book_isbn = input("Enter book isbn: ")
            library.borrow_book(user_id, book_isbn)
            print(library._users[0]._borrowed_books)

        elif choice == "4":
            user_id = int(input("Enter user id: "))
            book_isbn = input("Enter book isbn: ")
            library.return_book(user_id, book_isbn)

        elif choice == "5":
            library.list_available_books()
        
        elif choice == "6":
            title = input("Enter book's title: ")
            library.search_book(title)

        elif choice == "7":
            convert_to_json(library)
            break

        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
