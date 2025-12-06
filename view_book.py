library = []
def view_books():
    if len(library) == 0:
        print("No books in library.")
        return

    print("\n--- ALL BOOKS ---")
    for i, book in enumerate(library, start=1):
        status = "Available" if book["is_available"] else "Not Available"
        print(f"{i}. Title: {book['title']} | Author: {book['author']} | {status}")
