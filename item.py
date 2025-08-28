from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    @abstractmethod
    def display_info(self):
        """Polymorphic method to display item details"""
        pass
