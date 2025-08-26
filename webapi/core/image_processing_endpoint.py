# app/api/image_processing.py

import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.image_request import ImageMetadata
from models.image_response import ImageProcessingResponse

router = APIRouter()

TEMP_DIR = "./temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@router.post("/imageProcessing", tags=["Image"])
async def process_image(
    image: UploadFile = File(...),
    metadata: ImageMetadata = Depends()
):
    # Validate image type
    #if image.content_type != "image/jpeg" or image.content_type != "image/png":
    #    raise HTTPException(status_code=400, detail="Only JPEG/PNG images are allowed.")

    # Validate image size (max 1MB)
    contents = await image.read()
    if len(contents) > 1_048_576:  # 1MB
        raise HTTPException(status_code=400, detail="Image size exceeds 1MB.")

    # Save image to temp folder
    image_path = os.path.join(TEMP_DIR, f"{metadata.id}.jpg")
    with open(image_path, "wb") as f:
        f.write(contents)

    return ImageProcessingResponse(
        status="success",
        filename=image.filename,
        stored_as=image_path,
        metadata=metadata.dict()
    )
