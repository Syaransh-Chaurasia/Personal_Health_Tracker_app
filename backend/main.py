from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import user, symptom, medication, vitals
from backend.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://reliable-cheesecake-01ebcf.netlify.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/user")
app.include_router(symptom.router, prefix="/symptom")
app.include_router(medication.router, prefix="/medication")
app.include_router(vitals.router, prefix="/vitals")
