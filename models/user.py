import sqlite3


class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        findUser = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(findUser, (username,))
        userRow = result.fetchone()
        if userRow:
            # passes them as positional arguments
            user = cls(*userRow)
        else:
            user = None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        findUser = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(findUser, (_id,))
        userRow = result.fetchone()
        if userRow:
            # passes them as positional arguments
            user = cls(*userRow)
        else:
            user = None

        connection.close()

        return user
