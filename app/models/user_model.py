from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from datetime import datetime, timezone
from uuid import uuid4

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
