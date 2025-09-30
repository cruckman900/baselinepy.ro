from fastapi import FastAPI
from app import models, database, crud
from app.schemas import TabCreate

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "Welcome to fanTABulous!"}

@app.post("/tabs/")
def create_tab(tab: TabCreate):
    tab_id = crud.create_tab(tab)  # Assume this returns the new tab's ID
    return {
        "message": "Tab saved. The riff lives on 🎸",
        "id": tab_id
    }

@app.get("/health")
def heath_check():
    return {"status": "fanTABulous is alive and riffing 🤘"}