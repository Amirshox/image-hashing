from pydantic import BaseModel


class ImageHashRequest(BaseModel):
    path: str = "media/image.jpg"


class ImageHashUrlRequest(BaseModel):
    url: str = "https://example.com/image.jpg"


class ImageHashResponse(BaseModel):
    hash: str
