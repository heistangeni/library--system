import unittest
from src.book import Book
from src.magazine import Magazine
from src.shelf import Shelf
from src.library import Library

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test Library")
        self.shelf = Shelf(1)
        self.book = Book("Python 101", 250, "John Doe")
        self.magazine = Magazine("AI Weekly", 40, 5)
        self.shelf.add_item(self.book)
        self.shelf.add_item(self.magazine)
        self.library.add_shelf(self.shelf)

    def test_count_items(self):
        self.assertEqual(self.library.count_items(), 2)

    def test_search_item(self):
        found = self.shelf.search_item("Python 101")
        self.assertIsInstance(found, Book)

if __name__ == "__main__":
    unittest.main()
