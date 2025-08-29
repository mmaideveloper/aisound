from services.logger_service import get_logger, log_function

@log_function
def detect_insect(image):
    # Dummy logic — replace with actual model inference
    # e.g., model.predict(image)
    return {
        "type": "bee",  # or "wasp", "hornet", etc.
        "confidence": 0.95
    }
