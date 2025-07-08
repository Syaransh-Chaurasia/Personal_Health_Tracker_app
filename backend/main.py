from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routers import user, symptom, medication, vitals

# ✅ Automatically create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Health Tracker API",
    description="Track symptoms, medications, and vitals securely.",
    version="1.0"
)

# ✅ CORS setup for both production and local testing
origins = [
    "https://reliable-cheesecake-01ebcf.netlify.app",  # ✅ Live frontend
    "http://localhost:3000",  # ✅ Local frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include Routers
app.include_router(user.router)
app.include_router(symptom.router)
app.include_router(medication.router)
app.include_router(vitals.router)

# ✅ Root route for testing
@app.get("/")
def read_root():
    return {"message": "Personal Health Tracker API is running"}
