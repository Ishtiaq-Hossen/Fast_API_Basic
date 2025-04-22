from typing import List
from pydantic import BaseModel

class Item:
    _items: List[dict] = []

    @classmethod
    def all(cls):
        return cls._items

    @classmethod
    def add(cls, item: dict):
        cls._items.append(item)
        return item

    @classmethod
    def get(cls, item_id: int):
        return next((i for i in cls._items if i["id"] == item_id), None)

    @classmethod
    def delete(cls, item_id: int):
        item = cls.get(item_id)
        if item:
            cls._items.remove(item)
        return item
