from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from uuid import uuid4

class FileAsset(Base):
    __tablename__ = "file_assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    filename = Column(String, nullable=False)
    type = Column(String)
    url = Column(String)
    track_id = Column(UUID(as_uuid=True), ForeignKey("tracks.id"))
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
