import json
from core.book import *

PATH = "json_data.json"

def convert_to_json(library):
    data = {}
    data["Books"] = convert_books_to_json(library._books)
    data["Users"] = convert_users_to_json(library._users)

    with open(PATH, "w") as file:
        json.dump(data, file, indent=3) 

def convert_books_to_json(books):
    result = []
    for book in books:
        result.append(book.get_book_json_look())
    return result

def convert_users_to_json(users):
    result = []
    for user in users:
        result.append(user.get_user_json_look())
    return result
      
        
# def load_from_json(path):
#     with open(path, "r") as file:
#         data = json.load(file)
#     return data



