class User:
    id_counter = 100

    def __init__(self, name):
        self._name = name
        self._id = User.id_counter
        self._borrowed_books = []
        User.id_counter += 1

    def get_user_name(self):
        return self._name

    def get_user_id(self):
        return self._id
    
    def set_user_id(self, new_id):
        self._id = new_id

    def get_borrowed_books(self):
        return self._borrowed_books

    def get_user_json_look(self):
        return {"Name": self._name, "Id": self._id, "Borrowed_books": convert_books_to_json(self.get_borrowed_books())}
    
