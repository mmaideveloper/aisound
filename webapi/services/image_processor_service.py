#Load image, runs modes, merge results
# webapi/services/image_processor.py

import os
from models.insects_model import detect_insect
from models.bee_model import analyze_bee
from services.response_builder_service import build_response
from PIL import Image
from services.logger_service import get_logger, log_function
import traceback

logger = get_logger("image-processor")

@log_function
async def process_image(image_path):
  
    response : any = None
    insect_result : any = None
    bee_details : any = None
    try:
        
        insect_result = detect_insect(image_path)
        if insect_result["type"] != "bee":
            return  build_response(success=True, insect_type=insect_result, details=[])

        bee_details = analyze_bee(image_path)
        
        return build_response(success=True, insect_type=insect_result, details=bee_details)

    except Exception as e:
        full_trace = traceback.format_exc()
        return build_response(success=False, insect_type=insect_result, details=bee_details, error=str(e) + " " + full_trace)


