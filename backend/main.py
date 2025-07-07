from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import medication, symptom, vitals, user  # ✅ Make sure this is imported
from backend.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Health Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later replace with your Netlify domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(medication.router)
app.include_router(symptom.router)
app.include_router(vitals.router)
app.include_router(user.router)  # ✅ This was missing

@app.get("/")
def home():
    return {"message": "API is running"}
