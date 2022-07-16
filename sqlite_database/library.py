from codecs import latin_1_encode
import sqlite3


class Book:
    def __init__(self, name, author, publisher, type):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type

    def __str__(self):
        return "Name: {}\nAuthor: {}\nPublisher: {}\nType: {}\n".format(
            self.name, self.author, self.publisher, self.type
        )


class Library:
    def __init__(self):
        self.create_connect()

    def create_connect(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS books(name TEXT,author TEXT,publisher TEXT,type TEXT)"
        self.cursor.execute(query)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()

    def showBooks(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There are no books yet.")

        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3])
                print(book)

    def getBookByName(self, name):
        query = "SELECT * FROM books where name = ?"
        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            return "There are no books with this name."

        elif len(books) == 1:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3])
                return book

        else:
            return "Please press number 3."

    def getBooksByName(self, name):
        query = "SELECT * FROM books where name = ?"
        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if len(books) > 1:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3])
                print(book)
        else:
            print("Please press number 2.")

    def addBook(self, book):
        query = "INSERT INTO books VALUES(?,?,?,?)"
        self.cursor.execute(query, (book.name, book.author, book.publisher, book.type))
        self.conn.commit()

    def deleteBook(self, name):
        query = "DELETE FROM books where name = ?"
        self.cursor.execute(query, (name,))
        self.conn.commit()
