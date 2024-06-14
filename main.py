import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from PIL import Image

from imagehash import phash

from schemas import ImageHashRequest, ImageHashResponse

load_dotenv()

MEDIA_PATH = os.environ.get("MEDIA_PATH", "media")

app = FastAPI(
    title="Image Hashing API",
    description="API to compute the hash of an image",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image/hash", response_model=ImageHashResponse)
async def image_hash(
        request_data: ImageHashRequest
):
    try:
        full_path = os.path.join(MEDIA_PATH, request_data.path)
        image = Image.open(full_path)
        hash_val = str(phash(image, hash_size=16))
        return {"hash": hash_val}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
