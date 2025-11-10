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
    l.borrow_book(u1.get_user_id(), b1.get_isbn())

    convert_to_json(l)


   

