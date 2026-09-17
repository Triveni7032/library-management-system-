from book import Book
from member import Member


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        try:
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            if title == "":
                raise ValueError("Book title cannot be empty.")

            if author == "":
                raise ValueError("Author name cannot be empty.")

            for book in self.books:
                if book.book_id == book_id:
                    raise ValueError("Book ID already exists.")

            new_book = Book(book_id, title, author)
            self.books.append(new_book)

            print("Book added successfully.")

        except ValueError as error:
            print("Error:", error)

    def view_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\n===== BOOKS =====")

        for book in self.books:
            book.display_book()

    def search_book(self):

        try:
            book_id = int(input("Enter book ID: "))

            for book in self.books:

                if book.book_id == book_id:
                    book.display_book()
                    return

            print("Book not found.")

        except ValueError:
            print("Please enter a valid book ID.")

    def add_member(self):

        try:
            member_id = int(input("Enter member ID: "))
            name = input("Enter member name: ")

            if name == "":
                raise ValueError("Member name cannot be empty.")

            for member in self.members:
                if member.member_id == member_id:
                    raise ValueError("Member ID already exists.")

            new_member = Member(member_id, name)
            self.members.append(new_member)

            print("Member added successfully.")

        except ValueError as error:
            print("Error:", error)

    def view_members(self):

        if not self.members:
            print("No members available.")
            return

        print("\n===== MEMBERS =====")

        for member in self.members:
            member.display_member()

    def issue_book(self):

        try:
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))

            selected_book = None
            selected_member = None

            for book in self.books:
                if book.book_id == book_id:
                    selected_book = book
                    break

            for member in self.members:
                if member.member_id == member_id:
                    selected_member = member
                    break

            if selected_book is None:
                raise ValueError("Book not found.")

            if selected_member is None:
                raise ValueError("Member not found.")

            if not selected_book.is_available:
                raise ValueError("Book is already issued.")

            selected_book.is_available = False

            print(
                f"'{selected_book.title}' issued to "
                f"{selected_member.name}."
            )

        except ValueError as error:
            print("Error:", error)

    def return_book(self):

        try:
            book_id = int(input("Enter book ID: "))

            for book in self.books:

                if book.book_id == book_id:

                    if book.is_available:
                        raise ValueError(
                            "This book is already available."
                        )

                    book.is_available = True

                    print("Book returned successfully.")
                    return

            print("Book not found.")

        except ValueError as error:
            print("Error:", error)