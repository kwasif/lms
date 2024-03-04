# This is a deliberately poorly implemented main script for a Library Management System.

from book import Book
from models import Models
from storage import Storage


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
            return choice
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


def main():
    # Model object to initialize data records
    lms_model = Models()
    # Read and Load data
    new_storage = Storage("data.json")
    new_storage.load_data(lms_model)

    while True:
        choice = main_menu()
        # Add a new book
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            lms_model.model_add_book(title, author, isbn)

        # Display list of books in library
        elif choice == '2':
            print("List of books in library")
            lms_model.model_list_books()

        # Adding new user
        elif choice == '3':
            print("\nAdding a New User to library:")
            new_name = input("Enter user name: ")
            new_user_id = input("Enter user ID: ")
            lms_model.model_add_user(new_name, new_user_id)

        # Checkout book from the library
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            lms_model.model_book_checkout(user_id, isbn)

        # Checkin book to the library
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            lms_model.model_book_checkin(user_id, isbn)

        # Track book availability
        elif choice == '6':
            isbn = input("Enter ISBN: ")
            lms_model.model_book_availability(isbn)

        # Exiting the application
        elif choice == '7':
            print("Commencing exit process, Saving updated records and session logs")
            lms_model.model_data_log(new_storage)
            break
        else:
            print("Invalid choice, please try again. Enter valid integer between 1-7")


if __name__ == "__main__":
    main()
