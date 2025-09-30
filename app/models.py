from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Tab(Base):
    __tablename__ = "tabs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    content = Column(Text)  # This will store your tab file format
