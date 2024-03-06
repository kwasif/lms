from datetime import datetime


class Book:
    # Constructor for Book class
    def __init__(self, title=None, author=None, isbn=None):
        self.title = title  # Book title
        self.author = author  # Author name
        self.isbn = isbn  # Unique 13 digit number to identify any book stored as string to avoid removal of 0s
        self.is_available = 1  # by default true while inserting new book entry
        self.borrowed_by = 0 # User ID of issued person, default value 0
        # Date of checkout and due date can bed added as a part of
        #self.checkout_date
        #self.due_date


    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}"

    @staticmethod
    def list_books(library):
        for book in library.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, availability: {bool(book['is_available'])}")

    # Search book based on username or userid
    @staticmethod
    def search_book(book_list, query):
        matching_books = []
        query_lower = query.lower()
        for count, book in enumerate(book_list):
            if query_lower in book["title"].lower() or query_lower in book["author"].lower() or query_lower == book["isbn"]:
                matching_books.append({"index": count, "book": book})
        return matching_books

    # Adds book to the library
    def add_book(self, library):
        # ISBN must be unique for every book, check if this ISBN is already used
        search_result = Book.search(library.books, self.isbn)
        if len(search_result) != 0:
            print(f"FAILED to add book, ISBN: {self.isbn} already exists in library")
        else:
            library.books.append(self.__dict__)
            timestamp = datetime.now()
            library.log.append(f"{timestamp}:: ADDED new BOOK titled {self.title} by {self.author} to the library")
            print("New Book added")

    # Updating book attributes, allowed changing availability status and borrower id only
    @staticmethod
    def update_book(library, record_index, user_id, is_available):
        library.books[record_index]['is_available'] = is_available
        library.books[record_index]['borrowed_by'] = user_id
        timestamp = datetime.now()
        library.log.append(f"{timestamp}:: UPDATED BOOK Status titled {library.books[record_index]['title']} by {library.books[record_index]['author']} with ISBN {library.books[record_index]['isbn']} and availability {bool(is_available)}")

    # Delete book based on isbn
    def delete_book(self, library):
        for book in library.books:
            if book["isbn"] == self.isbn:
                timestamp = datetime.now()
                library.log.append(
                    f"{timestamp}:: DELETED BOOK titled {book['title']} by {book['author']} with ISBN {book['isbn']}")

                library.books.remove(book)
                print("Book deleted")
                return True
        print("Book not found")
        return False

    #Availability status of a book
    @staticmethod
    def track_availability(library, isbn):
        search_isbn = Book.search(library.books, isbn)
        if len(search_isbn) != 0:
            print(f"Availability status of book with isbn:: {isbn} is {bool(search_isbn[0]['book']['is_available'])}")
        else:
            print(f"Book with isbn:: {isbn} does not exist in library ")

    # Method to check if isbn number is 13 digit
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) == 13:
            return True
        else:
            return False

