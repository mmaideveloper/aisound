from fastapi import FastAPI, Request, HTTPException, Depends, Header
from fastapi.responses import JSONResponse

app = FastAPI()

API_KEY = "12345"  # Replace with your actual key

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    return await call_next(request)

def verify_api_key_depends(x_api_key: str = Header(...)):
    if x_api_key != "your-secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/")
def  public_root():
    return {
        "version": "1.0.0", 
        "description": "Welcome to the AISound API"
    }

@app.get("/image", dependencies=[Depends(verify_api_key_depends)])
def secure_endpoint():
    return {"data": "Sensitive info"}



