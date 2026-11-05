# library.py
# A simple command-line library tracker.
books = {} # title -> {"author": str, "available": bool}
def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add Book")
    print("2. List all Books")
    print("0. Exit")
    
def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
        print(f"{title} by {details['author']} - {status}")

def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    if title in books:
        print(f'"{title}" is already in the library.')
        return

    books[title] = {
        "author": author,
        "available": True
    }

    print(f'Added "{title}".')
def return_book():
    title = input("Title: ").strip()

    if title not in books:
        print(f'No book titled "{title}".')
        return

    if books[title]["available"]:
        print(f'"{title}" is not borrowed.')
        return

    books[title]["available"] = True
    print(f'You returned "{title}".')

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_book()
        elif choice=="2":
            list_books()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()