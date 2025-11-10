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

    def get_borrowed_books(self):
        return self._borrowed_books
