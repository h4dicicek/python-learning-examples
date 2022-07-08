import sqlite3
import time

class Book():
    def __init__(self,name,author,publisher,type):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type

    def __str__(self):
        return "Name: {}\nAuthor: {}\nPublisher: {}\nType: {}\n".format(self.name,self.author,self.publisher,self.type)

class Library():
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
        if (len(books) == 0):
            return "There are no books yet."
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                return book