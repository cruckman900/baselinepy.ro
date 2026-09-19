from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Tab
from app.schemas.tab_schema import TabCreate, TabUpdate
from uuid import UUID

def create_tab(db: Session, tab_data: TabCreate) -> Tab:
    tab = Tab(**tab_data.model_dump())
    db.add(tab)
    db.commit()
    db.refresh(tab)
    return tab

def get_or_404(db: Session, tab_id: UUID) -> Tab:
    tab = db.query(Tab).filter(Tab.id == tab_id).first() # type: ignore
    if not tab:
        raise HTTPException(status_code=404, detail="Tab not found")
    return tab

def list_tabs(db: Session, user_id: Optional[str] = None) -> List[Tab]:
    query = db.query(Tab)
    if user_id:
        query = query.filter(Tab.user_id == user_id) # type: ignore
    return query.order_by(Tab.updated_at.desc()).all()

def update_tab(db: Session, tab_id: UUID, tab_data: TabUpdate) -> Tab:
    tab = get_or_404(db, tab_id)
    for field, value in tab_data.model_dump(exclude_unset=True).items():
        setattr(tab, field, value)
    db.commit()
    db.refresh(tab)
    return tab

def delete_tab(db: Session, tab_id: UUID) -> None:
    tab = get_or_404(db, tab_id)
    db.delete(tab)
    db.commit()
