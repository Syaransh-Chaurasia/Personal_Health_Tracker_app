from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import user, symptom, medication, vitals
from backend.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://reliable-cheesecake-01ebcf.netlify.app",  # Your frontend URL
        "http://localhost:3000",  # Optional: for local testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(user.router)
app.include_router(symptom.router)
app.include_router(medication.router)
app.include_router(vitals.router)
