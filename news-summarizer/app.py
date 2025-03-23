from fastapi import FastAPI
from api import router  # Import the router from api.py

app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "News Summarization & TTS API is running!"}
