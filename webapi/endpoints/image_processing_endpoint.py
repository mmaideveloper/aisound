# app/api/image_processing.py

import os
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from modules.image_request import ImageMetadata
from modules.image_response import ImageProcessingResponse
from services.image_processor_service import process_image
from services.logger_service import get_logger

router = APIRouter()

TEMP_DIR = "./temp"
os.makedirs(TEMP_DIR, exist_ok=True)

logger = get_logger("aisound-image-processing")

@router.post("/imageProcessing", tags=["Image"])
async def process_image_recognition(
    image: UploadFile = File(...),
    metadata: ImageMetadata = Depends()
):
    # Validate image type
    #if image.content_type != "image/jpeg" or image.content_type != "image/png":
    #    raise HTTPException(status_code=400, detail="Only JPEG/PNG images are allowed.")

    # Validate image size (max 1MB)
    contents = await image.read()

    logger.debug(f"Received image: {image.filename} with metadata: {metadata}")

    if len(contents) > 1_048_576:  # 1MB
        raise HTTPException(status_code=400, detail="Image size exceeds 1MB.")

    # Save image to temp folder
    image_path = os.path.join(TEMP_DIR, f"{metadata.id}.jpg")
    with open(image_path, "wb") as f:
        f.write(contents)

    logger.debug(f"Image saved to {image_path}")

    # load image and perform processing (stubbed)
    result =  await process_image(image_path)

    logger.debug(f"Processing result: {result}")

    return ImageProcessingResponse(
        status="success",
        filename=image.filename,
        stored_as=image_path,
        metadata=metadata.dict(),
        response = {
            "type_of_insects": result.get("type_of_insects") or "unknown",
            "details": result.get("details", []) or "no details available"
        } if result.get("success") else {"error": result.get("error")}
    )
