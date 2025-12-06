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
