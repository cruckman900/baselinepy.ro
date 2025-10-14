from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.tab_parser import detect_instrument, extract_tuning, extract_metadata
from app.routes.cloudinary import download_tab

router = APIRouter()

class TabUpload(BaseModel):
    title: str
    artist: str
    genre: str
    tab: str

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

@router.post("/upload-tab", tags=["Tabs"])
async def upload_tab_json(data: TabUpload):
    print("Received tab:", data)
    return {"message", "Tab uploaded successfully"}

