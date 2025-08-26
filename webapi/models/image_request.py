


from pydantic import BaseModel
from datetime import datetime

class ImageMetadata(BaseModel):
    time: datetime
    temperature: float
    location: str
    weight: float
    id: str
