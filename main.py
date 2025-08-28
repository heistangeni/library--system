from .library import Library
from .shelf import Shelf
from .book import Book
from .magazine import Magazine

def main():
    library = Library("Scholar Library")
    shelf1 = Shelf(1)

    book1 = Book("Design Patterns", 395, "GoF")
    mag1 = Magazine("Science Today", 50, 12)

    shelf1.add_item(book1)
    shelf1.add_item(mag1)
    library.add_shelf(shelf1)

    # Polymorphism
    print("\n Displaying Items")
    for item in shelf1.items:
        item.display_info()

    # Type checking
    print("\nSearch Example")
    found = shelf1.search_item("Design Patterns")
    if isinstance(found, Book):
        print(f"Found book! Author: {found.get_author()}")

    # Counting algorithm
    print("\nCounting Items")
    print(f"Total items in library: {library.count_items()}")

if __name__ == "__main__":
    main()
