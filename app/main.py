from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app import models, database, crud
from app.schemas import TabCreate

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

path_to_file = "tabs/example.ftab"
models.Base.metadata.create_all(bind=database.engine)
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
        allow_credentials=True,
        allow_origins = origins,
        allow_methods = ["*"],
        allow_headers = ["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to fanTABulous!"}

@app.get("/health")
def heath_check():
    return {"status": "fanTABulous is alive and riffing 🤘"}

@app.post("/tabs/")
def create_tab(tab: TabCreate):
    tab_id = crud.create_tab(tab)  # Assume this returns the new tab's ID
    return {
        "message": "Tab saved. The riff lives on 🎸",
        "id": tab_id
    }

@app.post("/upload/")
async def upload_tab(file: UploadFile = File(...)):
    # Validate file extension
    if not file.filename.endswith(".ftab"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Read contents
    contents = await file.read()
    if not contents.strip():
        raise HTTPException(status_code=400, detail="Empty file")

    # Save file
    os.makedirs("tabs", exist_ok=True)
    file_path = os.path.join("tabs", file.filename)
    with open(file_path, "wb") as f:
        f.write(contents)

    # Validate and parse .ftab content
    file.file.seek(0)
    return {"filename": file.filename, "size": len(contents)}

@app.get("/download/{tab_id}")
async def download_tab(tab_id: str):
    file_path = os.path.join("tabs", f"{tab_id}.ftab")
    # Serve .ftab file for download
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Tab file not found")

    return FileResponse(file_path, media_type="text/plain", filename=f"{tab_id}.ftab")
