# Create a simple Library Management System using Object-Oriented Programming (OOP) in Python.

# Requirements:
# 1. Create a Book class with the following attributes:
#    - Book ID
#    - Book Name
#    - Author
#    - Availability Status
# 2. Create a Library class that manages multiple book objects using a list.
# 3. Implement the following methods:
#    - add_book(): Add a new book to the library.
#    - display_books(): Display all available books.
#    - search_book(): Search for a book using its ID.
#    - borrow_book(): Change the book status to borrowed.
#    - return_book(): Change the book status to available.
# 4. Create a menu-driven program that allows users to perform these operations.


class Book:
    def __init__(self, bookID, bookName, author, availabilityStatus):
        self.bookID = bookID
        self.bookName = bookName
        self.author = author
        self.availabilityStatus = availabilityStatus


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            if book.availabilityStatus == 1:
                print(book.bookID, book.bookName, book.author, book.availabilityStatus)


def addBooks():
    id = len(lib.books) + 1
    bookName = input("Enter the book name\n")
    authorName = input("Enter Author name\n")
    status = int(
        input("Enter Availability Status in number 1 for true and 0 for false \n")
    )
    book = Book(id, bookName, authorName, status)
    lib.add_book(book)


def SearchBooks():
    if len(lib.books) == 0:
        print("There is currently no book")
    else:
        searchID = int(input("Enter the Book ID which you want to see \n"))
        found = 0
        for each_book in lib.books:
            if each_book.bookID == searchID:
                print(
                    each_book.bookID,
                    each_book.bookName,
                    each_book.author,
                    type(each_book.availabilityStatus),
                )
                found = 1
                break
        if not found:
            print("No Book Found for the requested ID")


def borrow_book():
    if len(lib.books) == 0:
        print("There is currently no book")
    else:
        choice = int(input("Enter the Book which you want to boorw \n"))
        for item in lib.books:
            if choice == item.bookID:
                if item.availabilityStatus == 1:
                    print("The book is Available. You can take it")
                    item.availabilityStatus = 0
                else:
                    print("Book Not Found")


def return_book():
    if len(lib.books) == 0:
        print("There is currently no book")
    else:
        choice = int(input("Enter a book id which you want to return \n"))
        for item in lib.books:
            if choice == item.bookID:
                if item.availabilityStatus == 0:
                    print("The book has been returned")
                    item.availabilityStatus = 1
                else:
                    print("The book is Already Available. Try Another Option")


print("Welcome to Library Management System")
lib = Library()

while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book ")
    print("4. Borrow Book ")
    print("5. Return Book ")
    print("6. Exit")
    choice = int(input("Select a Number which you want to perform \n"))

    if choice == 1:
        addBooks()
    elif choice == 2:
        if len(lib.books) == 0:
            print("There is currently no book")
        else:
            lib.display_books()
    elif choice == 3:
        SearchBooks()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    else:
        break
