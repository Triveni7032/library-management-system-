from library import Library


def show_menu():
    print("\n==============================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Exit")
    print("==============================")


def main():

    library = Library()

    while True:

        show_menu()

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue

        if choice == 1:
            library.add_book()

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            library.search_book()

        elif choice == 4:
            library.add_member()

        elif choice == 5:
            library.view_members()

        elif choice == 6:
            library.issue_book()

        elif choice == 7:
            library.return_book()

        elif choice == 8:
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()