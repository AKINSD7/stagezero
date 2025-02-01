import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fetch environment variables
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")  # Use default if not set
DATABASE_URL = os.getenv("DATABASE_URL", "")

@app.get("/api/info")
def get_info():
    return {
        "email": "ibrahimakinyemi@gmail.com",
        "timestamp": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/yourusername/project-repo",
        "secret_key": SECRET_KEY  # For testing (remove in production)
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
