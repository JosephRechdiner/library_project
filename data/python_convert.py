import json
from core.user import User
from core.book import Book
from core.library import Library
PATH = "json_data.json"
def import_jason_data():
    with open(PATH, 'r') as f:
        data = json.load(f)
    books_list = data["Books"]
    users_list = data["Users"]
    return (books_list, users_list)

def convert_books_to_python(books_list):
    result = []
    for book in books_list:
        b = Book(book["Title"], book["Author"])
        b.ISBN = book["ISBN"]
        b.is_available = True #if book["Available"] == "Available" else False
        result.append(b)

    return result

def convert_borrowed_books(library):
    users = library._users
    for user in users:
        user_bb = user._borrowed_books
        user._borrowed_books = []
        for book in user_bb:
            library.borrow_book(user._id, book["ISBN"])
        



def convert_users_to_python(users_list):
    result = []
    for user in users_list:
        u = User(user["Name"])
        u._id = user["Id"]
        u._borrowed_books = user["Borrowed_books"]
        #convert_borrowed_books(u._id, user["Borrowed_books"], library)
        result.append(u)
    User.id_counter = u._id + 1
    return result

