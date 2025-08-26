from fastapi import FastAPI
import logging
import sys
import os
from dotenv import load_dotenv
from pathlib import Path

from core.root_endpoint import router as root_router
from core.image_processing_endpoint import router as image_router

# Get the parent directory of the current file
env_path = Path(__file__).resolve().parent.parent / ".env"

# Load the .env file from that path
load_dotenv(dotenv_path=env_path)
 
API_VERSION = os.getenv("VERSION", "0.1.0")


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("aisound-webapi")
logger.info(f"Web api App started successfully:{API_VERSION}")

app = FastAPI(title="AISound API", version=API_VERSION)

app.include_router(root_router)
app.include_router(image_router)




