from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Tab(models.Base)
    __tablename__ = "tabs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    content = Column(Text) # Serialized tab format
