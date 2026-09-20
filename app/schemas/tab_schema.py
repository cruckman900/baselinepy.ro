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
    # Structured composition JSON (measures, instrument, tuning, tempo, etc.)
    # serialized as a string — the frontend owns the shape of this blob.
    content: Optional[str] = None
    # Plain string owner reference (see Tab.user_id) so "my tabs" listing
    # works today without a hard FK to a not-yet-real auth system.
    user_id: Optional[str] = None

class TabCreate(TabBase):
    pass

class TabRead(TabBase):
    id: UUID
    uploaded_at: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    archived: bool = False

    model_config = ConfigDict(from_attributes=True)

class TabUpdate(BaseModel):
    filename: Optional[str] = None
    instrument: Optional[str] = None
    tuning: Optional[str] = None
    artist: Optional[str] = None
    title: Optional[str] = None
    genre: Optional[str] = None
    content: Optional[str] = None
    user_id: Optional[str] = None
    archived: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)