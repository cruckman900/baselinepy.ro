from fastapi import FastAPI
from app import models, database, crud
from app.schemas import TabCreate

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

@app.post("tabs")
def create_tab(tab: TabCreate):
    return crud.create_tab(tab)
