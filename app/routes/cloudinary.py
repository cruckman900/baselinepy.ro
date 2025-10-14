from app.services.cloudinary_service import upload_tab_stream
from fastapi import APIRouter, UploadFile, HTTPException
from app.services.cloudinary_service import get_cloudinary_url
from io import BytesIO
from cloudinary.exceptions import BadRequest

# from app.utils.parser import detect_instrument, extract_tuning  # Assuming you’ve modularized these

from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

ALLOWED_MIME_TYPES = {
    "text/plain",
    "application/pdf",
    "text/markdown"
}

@router.get("/download/{public_id}")
def download_tab(public_id: str):
    url = get_cloudinary_url(public_id)
    if not url:
        raise HTTPException(status_code=404, detail="Tab not found on Cloudinary")
    return {"cloudinary_url": url}

from fastapi import File

@router.post("/upload-file")
async def upload_tab_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    file_stream = BytesIO(await file.read())
    if file_stream.getbuffer().nbytes == 0:
        raise HTTPException(status_code=400, detail="Empty file")
    try:
        url = upload_tab_stream(file_stream, file.filename)
    except BadRequest as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"cloudinary_url": url, "public_id": file.filename}
