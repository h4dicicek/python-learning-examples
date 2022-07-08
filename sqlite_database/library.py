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
            print("There are no books yet.")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3])
                print(book)
    
    def queryBookWithName(self,name):
        query = "SELECT * FROM books where name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if (len(books) == 0):
            return "There are no books with this name."
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            return book

    def addBook(self,book):
        query = "INSERT INTO books VALUES(?,?,?,?)"
        self.cursor.execute(query,(book.name,book.author,book.publisher,book.type))
        self.conn.commit()
    
    def deleteBook(self,name):
        query = "DELETE FROM books where name = ?"
        self.cursor.execute(query,(name,))
        self.conn.commit()