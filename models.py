from book import Book
from user import User
from check import Check
from storage import Storage

# The model class decides which options to be given to a user
# perform sanity checks on user data before processing operation


class Models:
    # Default constructor to initialize library records for books, users and log
    def __init__(self):
        self.books = []
        self.users = []
        self.log = []
        self.storage_obj = Storage("data.json")

    # Loading of json data and commence launch of application
    def start(self):
        self.storage_obj.load_data(self)
        if self.storage_obj.located_data_file == 1:
            self.process_choice()
        else:
            print("Kindly locate the 'data.json' file and place it in application folder")

    # Main menu displayed for user's choice
    @staticmethod
    def main_menu():
        print("\nWelcome to Library Management System")
        print("\nChoose appropriate option based on your usage")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Checkout Book")
        print("5. Checkin Book")
        print("6. Track Book availability")
        print("7. Exit")

        while True:
            try:
                choice = (input("Enter your choice (1-7): "))
                if 1 <= int(choice) <= 7:
                    return choice
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")

    # Function to process user given choice and take necessary actions
    def process_choice(self):

        while True:
            choice = self.main_menu()
            # Add a new book
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")

                self.lms_model_add_book(title, author, isbn)

            # Display list of books in library
            elif choice == '2':
                print("List of books in library")
                self.lms_model_list_books()

            # Adding new user
            elif choice == '3':
                print("\nAdding a New User to library:")
                new_name = input("Enter user name: ")
                new_user_id = input("Enter user ID: ")
                # Function call to add user
                self.lms_model_add_user(new_name, new_user_id)

            # Checkout book from the library
            elif choice == '4':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                #Initiate book checkout
                self.lms_model_book_checkout(user_id, isbn)

            # Checkin book to the library
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkin: ")
                #Initiate book checkin
                self.lms_model_book_checkin(user_id, isbn)

            # Track book availability
            elif choice == '6':
                isbn = input("Enter ISBN: ")
                self.lms_model_book_availability(isbn)

            # Exiting the application
            elif choice == '7':
                print("Commencing exit process, Saving updated records and session logs")
                self.lms_model_data_log(self.storage_obj)
                break
            else:
                print("Invalid choice, please try again. Enter valid integer between 1-7")

    # Model method to add new book
    def lms_model_add_book(self, title, author, isbn):
        # Checking validity of ISBN number, it must be a 13 digit number
        if not self.is_valid_isbn(isbn):
            print("Invalid ISBN. ISBN should be 13 digits long")
        else:
            book_new_obj = Book(title, author, isbn)
            book_new_obj.add_book(self)

    # Display list of books
    def lms_model_list_books(self):
        Book.list_books(self)

    # Model method to validate userid type and add new user to library
    def lms_model_add_user(self, new_name, new_user_id):
        # validate if user id is digit and greater than 0

        if new_user_id.isdigit():
            new_user_id = int(new_user_id)
            if new_user_id > 0:
                new_user_obj = User(new_name, new_user_id)
                new_user_obj.add_user(self)
            else:
                print("Entered non zero User ID")
        else:
            print("Entered User ID is not an integer")

    #method for checkout
    def lms_model_book_checkout(self, user_id, isbn):
        if not self.is_valid_isbn(isbn):
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
    def lms_model_book_checkin(self, user_id, isbn):
        if not self.is_valid_isbn(isbn):
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
    def lms_model_book_availability(self, isbn):
        Book.track_availability(self, isbn)

    # Method to save updated records of users, books and session logs before exiting
    # User and Book data stored in data.json
    # Session log stored in log_timestamp.txt
    def lms_model_data_log(self, new_storage):
        if not self.log:
            # No logs or data to be written
            print("Exiting.")
        else:
            # Write updated data to a json file
            new_storage.save_data(self)
            # Write session logs to a file
            new_storage.write_session_log(self)
            print("Exiting.")

    # Check validity of ISBN number
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) == 13:
            return True
        else:
            return False
