from fastapi import FastAPI, Request, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("aisourd-webapi")
logger.info("Web api App started successfully")

app = FastAPI()

API_KEY = "12345"  # Replace with your actual key

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    return await call_next(request)

def verify_api_key_depends(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/", 
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
        "version": "1.0.0", 
        "description": "Welcome to the AISound API"
    }

@app.get("/image", dependencies=[Depends(verify_api_key_depends)])
def secure_endpoint():
    logger.info("secure endpoint accessed")
    return {"data": "Sensitive info"}



