from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import user
from backend.database import Base, engine
from dotenv import load_dotenv

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://reliable-cheesecake-01ebcf.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
