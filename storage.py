from book import Book
from user import User
import json
from datetime import datetime


class Storage:
    def __init__(self, data_filename):
        self.data_filename = data_filename
        timestamp = datetime.now()
        log_file_str = "log_" + timestamp.strftime("%Y%m%d-%H%M%S") + ".txt"
        self.session_log_filename = log_file_str

    @staticmethod
    def serialize_data(library):
        users_data = []
        books_data = []
        for user in library.users:
            # Convert each user object to a dictionary
            users_data.append(user)
        for book in library.books:
            books_data.append(book)
        data = {"users": library.users, "books": library.books}
        return data

    def load_data(self, library):
        try:
            with open(self.data_filename, "r") as f:
                data = json.load(f)
                library.books = data["books"]
                library.users = data["users"]
        except FileNotFoundError:
            print("Data file with user and book information not found!")


    def save_data(self, library):
        #data = {"books": [book.__dict__ for book in library.books], "users": [user.__dict__ for user in library.users]}
        #data = {"books": [book.__dict__ for book in library.books], "users": [user.__dict__ for user in library.users]}
        #user_json = json.dumps(library.users)
        with open(self.data_filename, "w") as json_file:
            json.dump(self.serialize_data(library), json_file, indent=4)

    def write_session_log(self, library):
        with open(self.session_log_filename, 'w') as text_file:
            for log in library.log:
                text_file.write(log + "\n")

