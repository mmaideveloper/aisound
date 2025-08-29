from fastapi import FastAPI, Request, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from core.root_endpoint import router as root_router
import os
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("APIKEY","")  # Replace with your actual key

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    return await call_next(request)


def verify_api_key_depends(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
