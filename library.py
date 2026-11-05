# library.py
# A simple command-line library tracker.
books = {} # title -> {"author": str, "available": bool}
def find_book_title(title):
    for book_title in books:
        if book_title.lower() == title.lower():
            return book_title
    return None

def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add Book")
    print("2. List all Books")
    print("3. Borrow Book")
    print("4. Return Book")
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

    if find_book_title(title) is not None:
        print(f'"{title}" is already in the library.')
        return

    books[title] = {
        "author": author,
        "available": True
    }

    print(f'Added "{title}".')

def borrow_book():
    title = input("Title: ").strip()
    book_title = find_book_title(title)

    if book_title is None:
        print(f'No book titled "{title}".')
        return

    if not books[book_title]["available"]:
        print(f'"{book_title}" is already borrowed.')
        return

    books[book_title]["available"] = False
    print(f'You borrowed "{book_title}".')

def return_book():
    title = input("Title: ").strip()
    book_title = find_book_title(title)

    if book_title is None:
        print(f'No book titled "{title}".')
        return

    if books[book_title]["available"]:
        print(f'"{book_title}" is not borrowed.')
        return

    books[book_title]["available"] = True
    print(f'You returned "{book_title}".')

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
        elif choice=="3":
            borrow_book()
        elif choice=="4":
            return_book()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()