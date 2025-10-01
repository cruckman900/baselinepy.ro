import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from io import BytesIO

# from dotenv import load_dotenv
# load_dotenv(dotenv_path=".env")

import os
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def get_cloudinary_url(public_id: str) -> str | None:
    try:
        result = cloudinary.api.resource(public_id, resource_type="raw")
        return result.get("secure_url")
    except cloudinary.exceptions.Error as e:
        print(f"Cloudinary lookup failed for '{public_id}':", e)
        return None

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
