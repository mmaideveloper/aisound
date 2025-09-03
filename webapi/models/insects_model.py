from services.logger_service import get_logger, log_function
import requests
from services.environment_service import get_env

logger = get_logger("insect-detection")

API_KEY = get_env("API_KEY_ROBOTFLOW", "")

MODEL_ENDPOINT = "https://detect.roboflow.com/insect_detect_classification/1"

@log_function
#issue with EfficientNetB0 model 
def detect_insect(image_path):

    insete_type = "unknown",
    confidence = 0.0

    #open image and send to roboflow model
    with open(image_path, "rb") as image_file:
        response = requests.post(
            MODEL_ENDPOINT,
            files={"file": image_file},
            params={ 
                "api_key": API_KEY, 
                "confidence": 20,
                "overlap":0.5
                }
        )

    if response.status_code == 200:
        result = response.json()
        if "predictions" in result and len(result["predictions"]) > 0:
            top_prediction = max(result["predictions"], key=lambda x: x["confidence"])
            insect_type = top_prediction["class"]
            confidence = top_prediction["confidence"]
            logger.info(f"Insect detected: {insect_type} with confidence {confidence}")
        else:
            logger.info("No insect detected in the image.")
    else:
        logger.error(f"Error in API request: {response.status_code} - {response.text}")

    return {
        "type":  "bee" if "bee" in insect_type.lower() else insect_type,
        "type_model": insect_type,
        "confidence": confidence,
        "success": response.status_code == 200
    }
