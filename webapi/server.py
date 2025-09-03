from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from pathlib import Path

from services.logger_service import get_logger
from endpoints.root_endpoint import router as root_router
from endpoints.image_processing_endpoint import router as image_router
from services.environment_service import get_env

API_VERSION = get_env("VERSION", "0.1.0")


logger = get_logger("aisound-webapi")
logger.info(f"Web api App started successfully:{API_VERSION}")

app = FastAPI(title="AISound API", version=API_VERSION)

app.include_router(root_router)
app.include_router(image_router)

@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong on our end. Please try again later.",
            "Developer": str(exc)
        }
    )




