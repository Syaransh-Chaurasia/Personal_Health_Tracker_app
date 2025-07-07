from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routers import medication, symptom, vitals, user

app = FastAPI(title="Personal Health Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(medication.router)
app.include_router(symptom.router)
app.include_router(vitals.router)
app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Personal Health Tracker API"}
