from fastapi import APIRouter, HTTPException
from app.schemas.item_schema import ItemSchema
from app.services.item_service import ItemService

router = APIRouter()

@router.get("/items", response_model=list[ItemSchema])
def get_items():
    return ItemService.list_items()

@router.post("/items", response_model=ItemSchema)
def create_item(item: ItemSchema):
    return ItemService.create_item(item.dict())

@router.get("/items/{item_id}", response_model=ItemSchema)
def get_item(item_id: int):
    item = ItemService.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/items/{item_id}", response_model=ItemSchema)
def delete_item(item_id: int):
    item = ItemService.delete_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
