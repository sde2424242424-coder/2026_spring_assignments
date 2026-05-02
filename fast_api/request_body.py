from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/items/with-tax/")
async def create_item_with_tax(item: Item):
    item_dict = item.model_dump()

    if item.tax is not None:
        item_dict["price_with_tax"] = item.price + item.tax

    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        **item.model_dump()
    }

@app.put("/items/{item_id}/full")
async def update_item_full(
    item_id: int,
    item: Item,
    q: str | None = None
):
    result = {
        "item_id": item_id,
        **item.model_dump()
    }

    if q:
        result["q"] = q

    return result