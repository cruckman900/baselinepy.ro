import cloudinary
import cloudinary.uploader
import os
from io import BytesIO

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def upload_tab_stream(file_stream: BytesIO, filename: str) -> str:
    result = cloudinary.uploader.upload(
        file_stream,
        resource_type="raw",  # Use "raw" for non-image files like .txt, .md, etc.
        public_id=filename,
        use_filename=True,
        unique_filename=False,
        overwrite=True
    )
    return result["secure_url"]
