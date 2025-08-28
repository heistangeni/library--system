from .item import Item

class Book(Item):
    def __init__(self, title: str, pages: int, author: str):
        super().__init__(title, pages)
        self.author = author

    def display_info(self):
        print(f"Book: {self.title} by {self.author} ({self.pages} pages)")

    def get_author(self):
        return self.author
