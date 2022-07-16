from dbm.ndbm import library
from library import *

print(
    """
____________________________
Operations:

Press 1 for see books.

Press 2 for get book by name.

Press 3 for get books by name which books are have same name.

Press 4 for add book.

Press 5 for delete book.

Press q for quit.
"""
)

library = Library()

while True:
    operation = input("Please enter the operation: ")

    if operation == "q":
        print("See you soon!")
        break

    elif operation == "1":
        library.showBooks()

    elif operation == "2":
        name = input("Which book do you want to query?: ")
        print(library.getBookByName(name))

    elif operation == "3":
        name = input("Which book do you want to query?: ")
        library.getBooksByName(name)

    elif operation == "4":
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        type = input("Type: ")
        new_book = Book(name, author, publisher, type)
        print("Book is adding..")
        library.addBook(new_book)
        print("Operation Completed!")

    elif operation == "5":
        name = input("Which book do you want to delete?: ")
        print("Book is deleting.")
        library.deleteBook(name)
        print("Operation Completed!")

    else:
        print("Operation not found!")
