from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import database
from app.routes import core, cloudinary, tab
from app.db import init_db
from app.database import Base
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(tab.router)

init_db()

Base.metadata.create_all(bind=database.engine)

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(core.router)
app.include_router(cloudinary.router)
app.include_router(tab.router)