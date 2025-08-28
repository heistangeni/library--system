from abc import ABC

class Item(ABC):
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    
    def display_info(self):
        return "Item info:{self.title}, {self.pages}'
