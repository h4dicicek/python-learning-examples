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