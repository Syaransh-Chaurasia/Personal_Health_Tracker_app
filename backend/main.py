from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import medication, symptom, vitals

app = FastAPI(title="Personal Health Tracker")

# Allow frontend calls (CORS configuration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your Netlify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(medication.router)
app.include_router(symptom.router)
app.include_router(vitals.router)

@app.get("/")
def home():
    return {"message": "API is running"}
