from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

#The key factor is that a dependency should be a "callable".
#A "callable" in Python is anything that Python can "call" like a function.
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

## short cut writing:
#commons: Annotated[CommonQueryParams, Depends()]