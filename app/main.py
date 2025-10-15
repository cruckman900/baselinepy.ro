from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import cloudinary, user, tab
from app.routes.tab import router as tab_router
import os
from dotenv import load_dotenv
from app.startup import init_db

load_dotenv()
app = FastAPI()
app.include_router(tab.router)

init_db()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cloudinary.router)
app.include_router(user.router)
app.include_router(tab_router)
