from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database import engine
from app.models.tab_model import Tab

from sqlalchemy.orm import Session
from app.schemas.tab_schema import TabCreate, TabRead, TabUpdate
from app.services.tab_service import create_tab, get_or_404, update_tab, delete_tab
from uuid import UUID
from app.database import get_db

router = APIRouter()

class TabUpload(BaseModel):
    title: str
    artist: str
    genre: str
    tab: str

@router.get("/health/db")
def check_db():
    try:
        with Session(engine) as session:
            session.exec("SELECT 1")
        return {"status": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@router.post("/tabs", response_model=TabRead, tags=["Tabs"])
def create_tab_route(tab: TabCreate, db: Session = Depends(get_db)):
    return create_tab(db, tab)

@router.get("/{tab_id}", response_model=TabRead, tags=["Tabs"])
def read(tab_id: UUID, db: Session = Depends(get_db)):
    tab = get_or_404(db, tab_id)
    if not tab:
        raise HTTPException(status_code=404, detail="Tab not found")
    return tab

@router.patch("/{tab_id}", response_model=TabRead, tags=["Tabs"])
def update(tab_id: UUID, tab: TabUpdate, db: Session = Depends(get_db)):
    return update_tab(db, tab_id, tab)

@router.delete("/{tab_id}", tags=["Tabs"])
def delete(tab_id: UUID, db: Session = Depends(get_db)):
    delete_tab(db, tab_id)
    return {"detail": "Tab deleted"}

__all__ = ["router"]