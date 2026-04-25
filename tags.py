from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

## Create different tags
@app.post("/items/", tags=["items"])
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]

##Second way - tags with enum
# class Tags(Enum):
#     items = "items"
#     users = "users"


# @app.get("/items/", tags=[Tags.items])
# async def get_items():
#     return ["Portal gun", "Plumbus"]


# @app.get("/users/", tags=[Tags.users])
# async def read_users():
#     return ["Rick", "Morty"]