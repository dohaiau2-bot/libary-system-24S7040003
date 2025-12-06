def view_books():
    if not library:
        print("No books in library.")
        return

    print("\n--- ALL BOOKS ---")
    for i, book in enumerate(library, start=1):
        status = "Available" if book.get("is_available", True) else "Not Available"
        print(f"{i}. Title: {book['title']} | Author: {book['author']} | {status}")
