from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {"item_id": item_id}

    if q:
        item["q"] = q

    if not short:
        item["description"] = "This is an amazing item"

    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {
        "item_id": item_id,
        "owner_id": user_id
    }

    if q:
        item["q"] = q

    if not short:
        item["description"] = "Detailed description"

    return item

@app.get("/required/{item_id}")
async def read_required(item_id: str, needy: str):
    return {
        "item_id": item_id,
        "needy": needy
    }

@app.get("/mixed/{item_id}")
async def read_mixed(
    item_id: str,
    needy: str,
    skip: int = 0,
    limit: int | None = None
):
    return {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }