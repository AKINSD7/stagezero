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

@app.get("/api/info", response_model=dict)
def get_info():
    return {
        "email": "ibrahimakinyemi@gmail.com",
        "timestamp": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/yourusername/project-repo"
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
