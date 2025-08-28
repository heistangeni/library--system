from typing import List
from .item import Item

class Shelf:
    def __init__(self, shelf_id: int):
        self.shelf_id = shelf_id
        self.items: List[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def search_item(self, title: str):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None
