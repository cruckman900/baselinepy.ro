from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from uuid import uuid4

class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    body = Column(Text, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    track_id = Column(UUID(as_uuid=True), ForeignKey("tracks.id"))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    author = relationship("User")
    track = relationship("Track")
