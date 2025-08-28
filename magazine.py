from .item import Item

class Magazine(Item):
    def __init__(self, title: str, pages: int, issue_number: int):
        super().__init__(title, pages)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine: {self.title} (Issue {self.issue_number}, {self.pages} pages)")
