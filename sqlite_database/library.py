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

    def getBooks(self, name=None):
        if name is None:
            query = "SELECT * FROM books"
            self.cursor.execute(query)
            books = self.cursor.fetchall()
            return books
        else:
            query = "SELECT * FROM books where name = ?"
            self.cursor.execute(query, (name,))
            books = self.cursor.fetchall()
            return books

    def getBookByName(self, name):
        query = "SELECT * FROM books where name = ?"
        self.cursor.execute(query, (name,))
        book = self.cursor.fetchall()
        return book

    def addBook(self, book):
        query = "INSERT INTO books VALUES(?,?,?,?)"
        self.cursor.execute(query, (book.name, book.author, book.publisher, book.type))
        self.conn.commit()

    def deleteBook(self, name):
        query = "DELETE FROM books where name = ?"
        self.cursor.execute(query, (name,))
        self.conn.commit()
