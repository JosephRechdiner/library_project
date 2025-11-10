class User:
    id_counter = 100

    def __init__(self, name):
        self._name = name
        self._id = User.id_counter
        self.borrowed_books = []
        User.id_counter += 1

    def get_user_name(self):
        return self._name

    def get_user_id(self):
        return self._id


