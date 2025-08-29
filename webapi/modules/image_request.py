from pydantic import BaseModel
from datetime import datetime

class ImageMetadata(BaseModel):
    time: datetime = datetime.now()
    temperature: float
    location: str
    weight: float
    id: str
