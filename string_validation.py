from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, 
        Query(
            title="Query String", 
            description="Qeury String for the items to search in the database that have a good match",
            min_length=3,
            alias="item-query",
            deprecated=True,
            include_in_schema=False,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results