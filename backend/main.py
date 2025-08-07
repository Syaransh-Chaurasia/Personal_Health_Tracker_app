from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import user
from backend.database import Base, engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create all tables based on Base metadata (if not exists)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Allowed origins for CORS (adjust as needed)
origins = [
    "http://localhost:3000",
    "https://reliable-cheesecake-01ebcf.netlify.app"
]

# Add CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Frontend URLs allowed to access the API
    allow_credentials=True,         # Allow cookies, authorization headers
    allow_methods=["*"],            # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # Allow all headers
)

# Include your user router
app.include_router(user.router)
