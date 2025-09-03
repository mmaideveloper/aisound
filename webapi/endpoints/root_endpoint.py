# Root endpoint for version identification
import logging
import sys
import os
from fastapi import APIRouter
from dotenv import load_dotenv
from services.environment_service import get_env


API_VERSION = get_env("VERSION", "unknown")

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("aisound-webapi")

router = APIRouter()

@router.get("/", 
    response_model="",
    summary="Get API version and description",
    description="Root version identification endpoint",
    tags=["unsecure"],
    responses={
        200: {
            "description": "Item successfully created",
            "version": "1.0.0"
            }
        }
)
def  public_root():
    logger.info("Root endpoint accessed")
    return {
        "version": f"{API_VERSION}", 
        "description": "Welcome to the AISound API"
    }

@router.get("/health", 
    summary="Helath check endpoint",
    description="Health check endpoint",
    tags=["unsecure"],
)
def  public_root_health():
    return "Healthy"

