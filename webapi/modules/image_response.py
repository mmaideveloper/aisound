from datetime import datetime
from typing import Optional
from pydantic import BaseModel,Field

class ImageProcessingResponse(BaseModel):
    id: str
    time: datetime = Field(defautl_factory = datetime.utcnow())
    location: Optional[str] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    light: Optional[float] = None
    filename:str
    image_path:str
    status: str
    metadata: dict
    response: dict
