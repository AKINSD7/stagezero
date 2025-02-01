from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (adjust as needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/info", response_model=dict)  # Ensure JSON response
def get_info():
    return {
        "email": "ibrahimakinyemi@gmail.com",
        "timestamp": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/yourusername/project-repo"
    }