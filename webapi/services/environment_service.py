# env_service.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env once when this module is imported
env_path = Path(__file__).resolve().parent.parent / ".env"

print(f"Loading environment variables from: {env_path}")

load_dotenv(dotenv_path=env_path)

def get_env(key: str, default: str = None) -> str:
    return os.getenv(key, default)
