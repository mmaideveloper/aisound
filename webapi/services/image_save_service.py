
from http.client import HTTPException
import os
import uuid
from datetime import datetime

from services.environment_service import get_env
from modules.image_response import ImageProcessingResponse
from modules.image_request import ImageMetadata
from services.logger_service import get_logger

logger = get_logger("aisound-image-processing")
TEMP_DIR = get_env("IMAGE_FOLDER", "temp")

os.makedirs(TEMP_DIR, exist_ok=True)

#TODO: Add to azure storage and database

async def save_image_and_metadata(image:any, request:ImageMetadata)-> ImageProcessingResponse:
    # Generate GUID
    guid = str(uuid.uuid4())

    # Validate image type
    #if image.content_type != "image/jpeg" or image.content_type != "image/png":
    #    raise HTTPException(status_code=400, detail="Only JPEG/PNG images are allowed.")

    # Validate image size (max 1MB)
    contents = await image.read()

    logger.debug(f"Received image: {image.filename} with metadata: {request.dict()}")

    if len(contents) > 1_048_576:  # 1MB
        raise HTTPException(status_code=400, detail="Image size exceeds 1MB.")

    image_name = image.filename.rsplit(".", 1)[0]
    extension = image.filename.rsplit(".", 1)[-1].lower()

    if extension not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=400, detail="Only JPEG/PNG images are allowed.")
    
    # Create subfolder name
    folder_name = f"{image_name}_{guid}"
    folder_path = os.path.join(TEMP_DIR, folder_name)
    
    # Create image subfolder
    image_path = os.path.join(folder_path, f"image-{guid}.{extension}")
    os.makedirs(folder_path, exist_ok=True)
    
    # Save image
    with open(image_path, "wb") as f:
        f.write(contents)

    logger.debug(f"Image saved to {image_path}")

    # Prepare metadata
    metadata = ImageProcessingResponse (
        id = guid,
        location = request.location,
        temperature = request.temperature,
        time =  datetime.utcnow().isoformat(),
        filename =  image.filename,
        image_path =image_path,
        status = "saved",
        metadata = request.dict(),
        response = {}
    )

    metadataJson = metadata.model_dump_json()
    # Save metadata.json
    metadata_path = os.path.join(folder_path, "metadata.json")
    with open(metadata_path, "w") as f:
        f.write(metadataJson)
    return metadata
