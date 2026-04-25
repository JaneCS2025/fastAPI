#status codes
#100 - 199 are for "Information"
#200 - 299 are for "Successful" responses
#300 - 399 are for "Redirection"
#400 - 499 are for "Client error" responses
#an example is 404, for a "Not Found" response
#500 - 599 are for server errors

from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

#or do in this way:
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}