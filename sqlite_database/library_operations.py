from dbm.ndbm import library
from library import *

print(
    """
____________________________
Operations:

Press 1 for get all books.

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
        books = library.getBooks()

        if len(books) == 0:
            print("There are no books yet.")

        else:
            for i in books:
                books = Book(i[0], i[1], i[2], i[3])
                print(books)

    elif operation == "2":
        name = input("Which book do you want to query?: ")
        book = library.getBookByName(name)
        if len(book) == 0:
            print("There are no books with this name.")

        elif len(book) == 1:
            for i in book:
                book = Book(i[0], i[1], i[2], i[3])
                print(book)

        else:
            print("Please press number 3.")

    elif operation == "3":
        name = input("Which book do you want to query?: ")
        books = library.getBooks(name)
        if len(books) > 1:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3])
                print(book)

        else:
            print("Please press number 2.")

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
