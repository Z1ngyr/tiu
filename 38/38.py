import re
import sys


class Book:
    def __init__(self, isbn, name, author, pub_year):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.pub_year = pub_year

    def __str__(self):
        return f"{self.isbn} - {self.name} - {self.author} - {self.pub_year}"


class LibraryCatalog:
    list_books = []

    def addBook(self, isbn, name, author, pub_year):
        self.list_books.append(Book(isbn, name, author, pub_year))
        return str(self.list_books[len(self.list_books) - 1])

    def listBooks(self):
        return self.list_books

    def removeBooks(self, isbn):
        for i in range(len(self.list_books)):
            if self.list_books[i].isbn == isbn:
                temp = self.list_books[i]
                self.list_books.pop(i)
                return str(temp)
        return None

    def searchBooks(self, name):
        for i in range(len(self.list_books)):
            if name.lower() in self.list_books[i].name.lower():
                return str(self.list_books[i])

    def getCount(self):
        return len(self.list_books)


catalog_books = LibraryCatalog()


def validation_isbn(number):
    pattern = '^\d+(-\d+)+$'
    return True if re.fullmatch(pattern, str(number)) is not None else False


def validation_name(text):
    pattern = '[\s0-9a-zA-Zа-яА-Я.-]+'

    return True if re.fullmatch(pattern, text) is not None else False


def execute(line):
    if 'ADD' in line:
        line = line[:-1].replace(': ', ', ')
        data = line.split(', ')

    else:
        data = line.split()

    if len(data) == 1:
        if data[0] == 'COUNT':
            print(catalog_books.getCount())
        elif data[0] == 'LIST':
            for book in catalog_books.listBooks():
                print(book)
    elif len(data) == 2:
        if data[0] == 'SEARCH:':
            print(catalog_books.searchBooks(data[1]))
        elif data[0] == 'REMOVE:':
            print(catalog_books.removeBooks(data[1]))
    elif len(data) == 5:
        if data[0] == 'ADD':
            if validation_isbn(data[1]) and validation_name(data[2]) and validation_name(data[3]):
                print(catalog_books.addBook(data[1], data[2], data[3], data[4]))
            else:
                print(None)


for line in sys.stdin:
    execute(line)
