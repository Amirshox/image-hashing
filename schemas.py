from pydantic import BaseModel


class ImageHashRequest(BaseModel):
    path: str = "media/image.jpg"


class ImageHashResponse(BaseModel):
    hash: str
