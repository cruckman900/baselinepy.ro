from fastapi import APIRouter

from app import crud
from app.schemas import TabCreate

router = APIRouter()

@router.post("/tabs/")
def create_tab(tab: TabCreate):
    tab_id = crud.create_tab(tab)  # Assume this returns the new tab's ID
    return {
        "message": "Tab saved. The riff lives on 🎸",
        "id": tab_id
    }

@router.get("/download/{tab_id}")
async def download_tab(tab_id: str):
    file_path = os.path.join("tabs", f"{tab_id}.ftab")
    # Serve .ftab file for download
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Tab file not found")

    return FileResponse(file_path, media_type="text/plain", filename=f"{tab_id}.ftab")
