"""This is a FastApi application main module"""
from io import BytesIO

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
def remove_background(file: UploadFile):
    """removes background of an image"""
    content: bytes = file.file.read()
    img_no_bg: bytes = remove(content)
    return StreamingResponse(BytesIO(img_no_bg), media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
