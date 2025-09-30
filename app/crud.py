from app import models, database
from app.schemas import TabCreate

def create_tab(tab: TabCreate):
    db = database.SessionLocal()
    db_tab = models.Tab(**tab.dict())
    db.add(db_tab)
    db.commit()
    db.refresh(db_tab)
    return db_tab
