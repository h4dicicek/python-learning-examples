from dbm.ndbm import library
from library import *
print("""
____________________________
Operations:

Press 1 for see books.

Press 2 for query books with name.

Press 3 for add book.

Press 4 for delete book.

Press q for quit.
""")

library = Library()

while True:
    operation = input("Please enter the operation: ")
    if (operation == "q"):
        print("See you soon!")
        break
    elif (operation == "1"):
        print(library.showBooks())
    elif (operation == "2"):
        name = input("Which book do you want to query?: ")
        time.sleep(0.5)
        print("Wait..")
        time.sleep(0.7)
        print(library.queryBookWithName(name))
    elif (operation == "3"):
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        type = input("Type: ")
        new_book = Book(name,author,publisher,type)
        print("Book is adding..")
        time.sleep(0.5)
        library.addBook(new_book)
        time.sleep(0.7)
        print("Operation Completed!")
    elif (operation == "4"):
        name = input("Which book do you want to delete?: ")
        print("Book is deleting.")
        time.sleep(0.5)
        print(library.deleteBook(name))
        time.sleep(0.7)
        print("Operation Completed!")
    else:
        print("Operation not found!")