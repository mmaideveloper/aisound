#Load image, runs modes, merge results
# webapi/services/image_processor.py

import os
from models.insects_model import detect_insect
from models.bee_model import analyze_bee
from services.response_builder_service import build_response
from PIL import Image
from services.logger_service import get_logger, log_function

logger = get_logger("image-processor")

@log_function
async def process_image(image_path):
  
    try:
        
        insect_result = detect_insect(image_path)
        if insect_result["type"] != "bee":
            return build_response(success=True, insect_type=insect_result["type"], details=[])

        bee_details = analyze_bee(image_path)
        
        return build_response(success=True, insect_type="bee", details=bee_details)

    except Exception as e:
        return build_response(success=False, error=str(e))


