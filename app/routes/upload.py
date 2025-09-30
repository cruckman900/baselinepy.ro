from fastapi import APIRouter, UploadFile, HTTPException
from io import BytesIO

from app.utils.tab_parser import detect_instrument , extract_tuning
from services.cloudinary_service import upload_tab_stream
# from app.utils.parser import detect_instrument, extract_tuning  # Assuming you’ve modularized these

router = APIRouter()

ALLOWED_MIME_TYPES = {
    "text/plain",
    "application/pdf",
    "text/markdown"
}

@router.post("/upload")
async def upload_tab(file: UploadFile):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {file.content_type}")

    contents = await file.read()
    file_stream = BytesIO(contents)

    # Extract metadata from tab text
    tab_text = contents.decode("utf-8", errors="ignore")
    instrument = detect_instrument(tab_text)
    tuning = extract_tuning(tab_text)

    # Upload to Cloudinary
    url = upload_tab_stream(file_stream, file.filename)

    return {
        "cloudinary_url": url,
        "filename": file.filename,
        "mime_type": file.content_type,
        "instrument": instrument,
        "tuning": tuning
    }
