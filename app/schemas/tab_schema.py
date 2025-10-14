from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class TabBase(BaseModel):
    public_id: str
    filename: Optional[str] = None
    instrument: Optional[str] = None
    tuning: Optional[str] = None
    artist: Optional[str] = None
    title: Optional[str] = None
    genre: Optional[str] = None

class TabCreate(TabBase):
    pass

class TabRead(TabBase):
    id: UUID
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TabUpdate(BaseModel):
    filename: Optional[str] = None
    instrument: Optional[str] = None
    tuning: Optional[str] = None
    artist: Optional[str] = None
    title: Optional[str] = None
    genre: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)