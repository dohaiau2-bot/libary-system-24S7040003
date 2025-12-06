library=[]
def search_book():
    query = input("Enter keyword to search: ").lower()

    found = False
    for book in library:
        if query in book["title"].lower():
            print(f"Found: {book['title']} - {book['author']}")
            found = True

    if not found:
        print("No matching books found.")
