# Global list
library = []

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Add book feature not implemented yet.")
        elif choice == '2':
            print("View books feature not implemented yet.")
        elif choice == '3':
            print("Search feature not implemented yet.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
