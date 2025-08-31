#Load image, runs modes, merge results
# webapi/services/image_processor.py

import os
from models.insects_model import detect_insect
from models.bee_model import analyze_bee
from services.response_builder_service import build_response
from PIL import Image
from services.logger_service import get_logger, log_function

@log_function
def save_image(image_path: str, metadata: dict) -> dict:
    # Placeholder for image processing logic
    # In a real implementation, this function would load the image,
    # apply various processing modes, and return the results.
    return {
        "status": "processed",
        "image_path": image_path,
        "metadata": metadata,
        "results": {
            "mode1": "result1",
            "mode2": "result2"
        }
    }

@log_function
async def process_image(image_path):
  
    try:
        image = Image.open(image_path).convert("RGB")

        insect_result = detect_insect(image)
        if insect_result["type"] != "bee":
            return build_response(success=True, insect_type=insect_result["type"], details=[])

        bee_details = analyze_bee(image)
        return build_response(success=True, insect_type="bee", details=bee_details)

    except Exception as e:
        return build_response(success=False, error=str(e))


