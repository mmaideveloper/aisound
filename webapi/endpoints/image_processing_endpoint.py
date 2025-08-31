# app/api/image_processing.py

import os
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from modules.image_request import ImageMetadata
from modules.image_response import ImageProcessingResponse
from services.image_processor_service import process_image
from services.logger_service import get_logger
from services.image_save_service import save_image_and_metadata
router = APIRouter()

logger = get_logger("aisound-image-processing")

@router.post("/images/processing", 
             summary="Analyze and process an uploaded image for model trainging.",
    description="Return recognition per current model and store image for future training.",
             tags=["Image"])
async def process_image_recognition(
    image: UploadFile = File(...),
    metadata: ImageMetadata = Depends()
):
     # Save image to temp folder
    image_response = await save_image_and_metadata(image, metadata)

    logger.debug(f"Image saved to {image_response.image_path}")

    # load image and perform processing (stubbed)
    result =  await process_image(image_response.image_path)

    logger.debug(f"Processing result: {result}")

    image_response.response = {
            "type_of_insects": result.get("type_of_insects") or "unknown",
            "details": result.get("details", []) or "no details available"
        } if result.get("success") else {"error": result.get("error")}
    image_response.status = "processed" if result.get("success") else "error"

    return image_response

@router.post("/images/get", 
             summary="Get a list of upload images",
    description="List of uploaded images and their processing status.",
    tags=["Image"])
async def images_get_list():
    # Stubbed: Return a list of processed images
    images = [
        {"id": "1", "filename": "image1.jpg", "status": "processed"},
        {"id": "2", "filename": "image2.jpg", "status": "pending"},
    ]
    return {"status": "success", "images": images}

@router.post("/images/get", 
             summary="Delete image folder if should not be used for training",
    description="Delete image by ID.",
             tags=["Image"])
async def image_delete(image_id: str):
    # Stubbed: Delete image by ID
    logger.debug(f"Deleting image with ID: {image_id}")
    return {"status": "success", "message": f"Image {image_id} deleted."}