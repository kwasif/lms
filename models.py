from book import Book
from user import User
from check import Check


class Models:
    # Default constructor to initialize library records for books, users and log
    def __init__(self):
        self.books = []
        self.users = []
        self.log = []

    # Model method to add new book
    def model_add_book(self, title, author, isbn):
        # Checking validity of ISBN number, it must be a 13 digit number
        if not Book.is_valid_isbn(isbn):
            print("Invalid ISBN. ISBN should be 13 digits long")
        else:
            book_new = Book(title, author, isbn)
            book_new.add_book(self)

    # Display list of books
    def model_list_books(self):
        Book.list_books(self)

    # Model method to add new user to library
    def model_add_user(self, new_name, new_user_id):
        # validate if user id is digit and greater than 0

        if new_user_id.isdigit():
            new_user_id = int(new_user_id)
            if new_user_id > 0:
                new_user = User(new_name, new_user_id)
                new_user.add_user(self)
            else:
                print("Entered non zero User ID")
        else:
            print("Entered User ID is not an integer")

    #method for checkout
    def model_book_checkout(self, user_id, isbn):
        if not Book.is_valid_isbn(isbn):
            print("Invalid ISBN. ISBN should be 13 digits long")
        else:
            if user_id.isdigit():
                # Check if user id is registered and book (isbn) is available before issuing book
                search_isbn = Book.search_book(self.books, isbn)
                search_user = User.search_user(self.users, None, int(user_id))
                if len(search_user) != 0:
                    if len(search_isbn) != 0:
                        Check.check_out(self, search_user[0], search_isbn[0])
                    else:
                        print(f"ISBN :: {isbn} does not exist in library system")
                else:
                    print(f"User ID :: {user_id} is not registered in library system")

    #method for checkout
    def model_book_checkin(self, user_id, isbn):
        if not Book.is_valid_isbn(isbn):
            print("Invalid ISBN. ISBN should be 13 digits long")
        else:
            if user_id.isdigit():
                # Check if user id is registered and book (isbn) is available before taking the book
                search_isbn = Book.search_book(self.books, isbn)
                search_user = User.search_user(self.users, None, int(user_id))
                if len(search_user) != 0:
                    if len(search_isbn) != 0:
                        Check.check_in(self, search_user[0], search_isbn[0])
                    else:
                        print(f"ISBN :: {isbn} does not exist in library system")
                else:
                    print(f"User ID :: {user_id} is not registered in library system")

    # Track book availability
    def model_book_availability(self, isbn):
        Book.track_availability(self, isbn)

    # Method to save updated records of users, books and session logs before exiting
    # User and Book data stored in data.json
    # Session log stored in log_timestamp.txt
    def model_data_log(self, new_storage):
        if not self.log:
            # No logs or data to be written
            print("Exiting.")
        else:
            # Write updated data to a json file
            new_storage.save_data(self)
            # Write session logs to a file
            new_storage.write_session_log(self)
            print("Exiting.")
