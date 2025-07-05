from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import medication, symptom, vitals
from database import Base, engine

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

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Health Tracker API"}
