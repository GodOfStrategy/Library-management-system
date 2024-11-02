#Day 10 Classes and objects
#Task 5
#code starts here:
class Library:
    def __init__(self):
        # Initialize the books attribute as an empty list
        self.books = []

    def add_book(self):
        # Ask the user to input the title of the book
        title = input("Enter the title of the book you want to add: ").strip()
        self.books.append(title)
        print(f"'{title}' has been added to the library.")

    def display_books(self):
        # Display all book titles in the library
        if self.books:
            print("Available books in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
        else:
            print("No books available in the library.")

# Create an object of the Library class
library = Library()

# Add books based on user input
while True:
    library.add_book()
    more_books = input("Would you like to add another book? (yes/no): ").strip().lower()
    if more_books != 'yes':
        break

# Display all books in the library
library.display_books()
