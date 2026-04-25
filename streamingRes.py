import anyio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"
        await anyio.sleep(0)


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())


# class CustomORJSONResponse(Response):
#     media_type = "application/json"

#     def render(self, content: Any) -> bytes:
#         assert orjson is not None, "orjson must be installed"
#         return orjson.dumps(content, option=orjson.OPT_INDENT_2)


# @app.get("/", response_class=CustomORJSONResponse)
# async def main():
#     return {"message": "Hello World"}

@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
async def read_item(item_id: str, img: bool | None = None):
    if img:
        return FileResponse("image.png", media_type="image/png")
    else:
        return {"id": "foo", "value": "there goes my hero"}