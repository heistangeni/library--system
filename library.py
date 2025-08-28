from typing import List
from .shelf import Shelf


class Library:
    def __init__(self, name: str):
        self.name = name
        self.shelves: List[Shelf] = []

    def add_shelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def count_items(self):
        return sum(len(shelf.items) for shelf in self.shelves)
