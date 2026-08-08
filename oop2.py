from datetime import datetime


# -------------------------
# Base Class
# -------------------------
class Person:
    total_people = 0

    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
        Person.total_people += 1

    def display(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")


# -------------------------
# Member Class
# -------------------------
class Member(Person):

    MAX_BOOKS = 3

    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = []

    def borrow_book(self, book):

        if len(self.borrowed_books) >= Member.MAX_BOOKS:
            print(f"{self.name} already borrowed maximum books.")
            return

        if not book.available:
            print(f"{book.title} is unavailable.")
            return

        self.borrowed_books.append(book)
        book.borrow()

        print(f"{self.name} borrowed {book.title}")

    def return_book(self, book):

        if book not in self.borrowed_books:
            print("Book not borrowed.")
            return

        self.borrowed_books.remove(book)
        book.return_book()

        print(f"{self.name} returned {book.title}")

    def display(self):
        super().display()

        print("Borrowed Books:")

        if not self.borrowed_books:
            print("None")

        for book in self.borrowed_books:
            print(book.title)


# -------------------------
# Librarian
# -------------------------
class Librarian(Person):

    def display(self):
        print(f"Librarian: {self.name}")


# -------------------------
# Book
# -------------------------
class Book:

    total_books = 0

    def __init__(self, book_id, title, author):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

        Book.total_books += 1

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def display(self):

        print("-" * 30)

        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", "Available" if self.available else "Borrowed")

    @classmethod
    def total(cls):
        print("Total Books:", cls.total_books)

    @staticmethod
    def validate_title(title):
        return len(title.strip()) > 0


# -------------------------
# Library
# -------------------------
class Library:

    def __init__(self):

        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def search_by_title(self, keyword):

        result = []

        for book in self.books:
            if keyword.lower() in book.title.lower():
                result.append(book)

        return result

    def available_books(self):

        return [book for book in self.books if book.available]

    def borrowed_books(self):

        return [book for book in self.books if not book.available]

    def display_books(self):

        print("\nAll Books")

        for book in self.books:
            book.display()


# -------------------------
# Transaction
# -------------------------
class Transaction:

    history = []

    @classmethod
    def log(cls, member, book, action):

        cls.history.append(
            {
                "member": member.name,
                "book": book.title,
                "action": action,
                "time": datetime.now()
            }
        )

    @classmethod
    def show_history(cls):

        print("\nTransaction History\n")

        for item in cls.history:

            print(
                item["time"],
                item["member"],
                item["action"],
                item["book"]
            )


# -------------------------
# Demo
# -------------------------

library = Library()

book1 = Book(1, "Python Basics", "John")
book2 = Book(2, "Data Structures", "Alice")
book3 = Book(3, "Machine Learning", "Bob")
book4 = Book(4, "Artificial Intelligence", "Tom")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

member1 = Member(101, "Nimal")
member2 = Member(102, "Kamal")

library.register_member(member1)
library.register_member(member2)

member1.borrow_book(book1)
Transaction.log(member1, book1, "Borrowed")

member1.borrow_book(book2)
Transaction.log(member1, book2, "Borrowed")

member2.borrow_book(book3)
Transaction.log(member2, book3, "Borrowed")

member1.return_book(book1)
Transaction.log(member1, book1, "Returned")

library.display_books()

Transaction.show_history()

Book.total()

print("\nAvailable Books")

for book in library.available_books():
    print(book.title)