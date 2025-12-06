# library.py - Final after merging features

library = []

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    book = {
        "title": title,
        "author": author,
        "is_available": True
    }

    library.append(book)
    print("Book added successfully.")

def view_books():
    if not library:
        print("No books in library.")
        return

    print("\n--- ALL BOOKS ---")
    for i, book in enumerate(library, start=1):
        status = "Available" if book.get("is_available", True) else "Not Available"
        print(f"{i}. Title: {book['title']} | Author: {book['author']} | {status}")

def search_book():
    query = input("Enter keyword to search: ").strip().lower()
    if not query:
        print("Empty query.")
        return

    found = False
    for i, book in enumerate(library, start=1):
        if query in book["title"].lower():
            found = True
            status = "Available" if book.get("is_available", True) else "Not Available"
            print(f"{i}. Title: {book['title']} | Author: {book['author']} | {status}")

    if not found:
        print("No matching books found.")

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
