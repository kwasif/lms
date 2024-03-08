from book import Book
from datetime import datetime


class Check:
    # Checking out a book
    @staticmethod
    def check_out(library, user, choosen_book):
        if choosen_book['book']['is_available']:
            choosen_book['book']['is_available'] = 0

            print(choosen_book['book']['borrowed_by'])
            choosen_book['book']['borrowed_by'] = user['users']['user_id']
            index = choosen_book['index']

            Book.update_book(library, index, user['users']['user_id'],0)
            #Check out status updated in library

            timestamp = datetime.now()
            library.log.append(f"{timestamp}:: CHECKED OUT book titled {choosen_book['book']['title']} by {user['users']['user_id']} from the library")
            print(f"{choosen_book['book']['title']} borrowed successfully by {user['users']['name']}")
        else:
            print(f"{choosen_book['book']['title']} is not available.")

    # Method for check in of book by registered user
    @staticmethod
    def check_in(library, user,  return_book):
        if return_book['book']['is_available'] == 0 and return_book['book']['borrowed_by'] == user['users']['user_id']:
            index = return_book['index']

            Book.update_book(library, index, 0, 1)
            # Checkin status updated in library

            timestamp = datetime.now()
            library.log.append(
                f"{timestamp}:: CHECKED IN book titled {return_book['book']['title']} by user-id {user['users']['user_id']} to the library")
            print(f"{return_book['book']['title']} returned successfully by {user['users']['name']}")
        else:
            print(f"{return_book['book']['title']} is already present in the library or was not taken by this user.")


    # Based on check-in date and due date late fee can be calculated for user id
    # def calc_late_fee( due_date, checkin_date)
