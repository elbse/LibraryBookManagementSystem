class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.public_year = publication_year
        self.available = True   # book availability

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is not available right now.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.public_year}, Status: {status}")

    def is_available(self):
        return self.available


# ----------------------------
# Library System With Error Handling
# ----------------------------
print("=== Library Book Management System ===")

# Pre-added books
library = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

while True:
    print("\n1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter publication year: "))  # may cause ValueError

            library.append(Book(title, author, year))
            print(f"Book '{title}' added successfully!")

        except ValueError:
            print("Invalid year! Please enter a valid number.")

    elif choice == "2":
        if not library:
            print("No books available in the library.")
            continue

        print("\nAvailable books:")
        for i, book in enumerate(library):
            status = "Available" if book.available else "Not Available"
            print(f"{i+1}. {book.title} - {status}")

        try:
            num = int(input("Enter book number to borrow: ")) - 1
            library[num].borrow_book()

        except ValueError:
            print("Invalid input! Enter a number.")
        except IndexError:
            print("Book number does not exist.")

    elif choice == "3":
        if not library:
            print("No books in the library.")
            continue

        print("\nBooks:")
        for i, book in enumerate(library):
            print(f"{i+1}. {book.title}")

        try:
            num = int(input("Enter book number to return: ")) - 1
            library[num].return_book()

        except ValueError:
            print("Invalid input! Enter a number.")
        except IndexError:
            print("Book number does not exist.")

    elif choice == "4":
        if not library:
            print("No books to display.")
        else:
            print("\n--- Library Books ---")
            for book in library:
                book.display_info()

    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
