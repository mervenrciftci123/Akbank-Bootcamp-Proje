class Library:
    def __init__(self):
        self.books_file = "books.txt"
        self.books = self.read_books()

    def __del__(self):
        self.books_file.close()

    def read_books(self):
        try:
            with open(self.books_file, "a+") as file:
                lines = file.readlines()
                if lines:
                    return [line.strip().split(",") for line in lines]
                else:
                    return []
        except FileNotFoundError:
            open(self.books_file, "w").close()  # Create empty file if not found
            return []

    def list_books(self):
        for book in self.books:
            print(f"Title: {book[0]}, Author: {book[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = int(input("Enter release year: "))
        pages = int(input("Enter number of pages: "))
        book_info = f"{title},{author},{release_year},{pages}"
        with open(self.books_file, "a") as file:
            file.write(book_info + "\n")
        self.books.append(book_info.split(","))

    def remove_book(self):
        title = input("Enter title of book to remove: ")
        for i, book in enumerate(self.books):
            if book[0] == title:
                del self.books[i]
                break
        else:
            print("Book not found!")
        self.update_books_file()

    def update_books_file(self):
        with open(self.books_file, "w") as file:
            for book in self.books:
                file.write(",".join(book) + "\n")


def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()