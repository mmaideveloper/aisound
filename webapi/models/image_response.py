
from pydantic import BaseModel

class ImageProcessingResponse(BaseModel):
    status: str
    filename: str
    stored_as: str
    metadata: dict
