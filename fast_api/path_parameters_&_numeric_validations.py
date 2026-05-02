from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    result = {"item_id": item_id}

    if q:
        result["q"] = q

    return result

@app.get("/items/min/{item_id}")
async def read_min_item(
    item_id: Annotated[int, Path(ge=1, title="ID must be >= 1")],
    q: str
):
    return {"item_id": item_id, "q": q}

@app.get("/items/range/{item_id}")
async def read_range_item(
    item_id: Annotated[int, Path(gt=0, le=1000)],
    q: str
):
    return {"item_id": item_id, "q": q}

@app.get("/items/size/{item_id}")
async def read_size_item(
    *,
    item_id: Annotated[int, Path(ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)]
):
    result = {"item_id": item_id, "q": q}

    if size:
        result["size"] = size

    return result