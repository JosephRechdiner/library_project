import json
from core.user import User
from core.book import Book
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
        b.is_available = book["is_available"]
        result.append(b)

    return result


def convert_users_to_python(users_list):
    result = []
    for user in users_list:
        u = User(user["Name"])
        u.set_borrowed_books(user["Borrowed_books"])
        u.set_user_id(user["Id"])
        result.append(u)

    return result

