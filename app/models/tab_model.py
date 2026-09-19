from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from uuid import uuid4

class Tab(Base):
    __tablename__ = "tabs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    public_id = Column(String, nullable=False)
    filename = Column(String)
    artist = Column(String)
    instrument = Column(String)
    tuning = Column(String)
    title = Column(String, nullable=False)
    content = Column(Text)  # This will store your tab file format
    # Plain string owner reference — not a strict ForeignKey yet since there's
    # no real auth/session system in place (login just returns a user_id).
    # Lets tabs be scoped to "my tabs" today without hard-coupling to a FK
    # that would break once real per-user auth replaces the current dev
    # bypass.
    user_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    genre = Column(String)
