# lms
LIBRARY MANAGEMENT SYSTEM

This is a command-line interface (CLI) implementation of a Library Management System (LMS).
The system allows users to perform various operations (register, check-in, check-out) related to managing books (add, delete, update, list, search)
and users(add, delete,update, list, search) within a library.


Current Features
1) Add Book : Adding new book to the library by providing author, title and ISBN
2) List of Books : Display list of books in the library
3) Add User : Addition of new user to the library by providing username and user ID
4) Checkout Book : Enables the user to check out a book. User needs to provide user id and ISBN of the book
5) Checkin Book : Enables the user to return a book. User needs to provide user id and ISBN of the book
6) Track Book Availability : Checks the availability status of the book based on ISBN provided
7) Exit : Terminates the application and exits the LMS. Updates the data records for users, books and saves session logs

Assumptions 
The following assumptions were made while developing the application 
1) Every user has unique User ID, only username can be updated
2) Every book has unique 13 digit ISBN number, only book availability status, borrower information updated
3) User, Book data is stored in data.json format and is updated after evry session
4) Session logs are maintained for every session along with timestamp information for each operation.

Usage
Run main.py script, The main menu will display selective options for the user
Follow the instructions and provide relevant information for each operation
Terminate the application using Exit option to ensure updated data, session logs are saved accordingly.

Note
Limited features as stated have been released. More functionalities to be released soon. 
Kindly report any bugs or issues pertaining to the application. 
