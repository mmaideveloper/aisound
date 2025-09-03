from services.logger_service import get_logger, log_function

@log_function
def build_response(success, insect_type=None, details=None, error=None):
    if not success:
        return {
            "success": False,
            "error": error,
            "type_of_insects": insect_type or [],
            "details": details or []
        }
    return {
        "success": True,
        "error": "",
        "type_of_insects": insect_type or [],
        "details": details or []
    }
