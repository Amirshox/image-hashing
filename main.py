import os
from io import BytesIO

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from PIL import Image

from imagehash import phash

from schemas import ImageHashRequest, ImageHashUrlRequest, ImageHashResponse

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


@app.post("/image/hash/url", response_model=ImageHashResponse)
async def image_hash_url(
        request_data: ImageHashUrlRequest
):
    try:
        response = requests.get(request_data.url)
        response.raise_for_status()  # Ensure the request was successful
        image = Image.open(BytesIO(response.content))
        hash_val = str(phash(image, hash_size=16))
        return {"hash": hash_val}
    except requests.RequestException as req_exc:
        raise HTTPException(status_code=400, detail=f"Error fetching image: {str(req_exc)}")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.middleware("http")
async def add_process_time_header(request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
