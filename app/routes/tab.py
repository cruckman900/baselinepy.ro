from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from pydantic import BaseModel
from app.db import engine
from models import Tab
from app.utils.tab_parser import detect_instrument, extract_tuning, extract_metadata
from app.routes.cloudinary import download_tab

router = APIRouter()

class TabUpload(BaseModel):
    title: str
    artist: str
    genre: str
    tab: str

@router.get("/health/db")
def check_db():
    try:
        with Session(engine) as session:
            session.exec("SELECT 1")
        return {"status": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@router.get("/metadata/{public_id}")
async def get_tab_metadata(public_id: str):
    try:
        tab_text = download_tab(public_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Tab not found")

    return {
        "instrument": detect_instrument(tab_text),
        "tuning": extract_tuning(tab_text),
        "metadata": extract_metadata(tab_text)
    }

@router.post("/tabs")
def create_tab(tab: Tab):
    with Session(engine) as session:
        session.add(tab)
        session.commit()
        session.refresh(tab)
        return tab

@router.post("/upload")
async def upload_tab(data: TabUpload):
    print("Received tab:", data)
    return {"message", "Tab uploaded successfully"}