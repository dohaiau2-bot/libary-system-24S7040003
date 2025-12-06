library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    book = {
        "title": title,
        "author": author,
        "is_available": True
    }

    library.append(book)
    print("Book added successfully.\n")

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
            print("View books not implemented yet.")
        elif choice == '3':
            print("Search not implemented yet.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
