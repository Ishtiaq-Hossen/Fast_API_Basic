from app.models.item import Item

class ItemService:
    @staticmethod
    def list_items():
        return Item.all()

    @staticmethod
    def create_item(data: dict):
        return Item.add(data)

    @staticmethod
    def get_item(item_id: int):
        return Item.get(item_id)

    @staticmethod
    def delete_item(item_id: int):
        return Item.delete(item_id)
