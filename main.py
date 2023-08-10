"""This is a FastApi application main module"""
from io import BytesIO

import requests
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from rembg import remove  # type: ignore


def download_image(url: str):
    res = requests.get(url, stream=True)
    image = res.content
    return image


def create_app() -> FastAPI:
    """This is the app"""
    _app: FastAPI = FastAPI(title="learn")
    return _app


app: FastAPI = create_app()
templates = Jinja2Templates(directory="templates")


@app.post("/remove_background")
def remove_background(file: UploadFile = None, url: str | None = None):
    """removes background of an image"""
    if file:
        content: bytes = file.file.read()
    else:
        content = download_image(url)
    img_no_bg: bytes = remove(content)
    return StreamingResponse(BytesIO(img_no_bg), media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
