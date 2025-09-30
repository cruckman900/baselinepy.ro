from pydantic import BaseModel

class TabCreate(BaseModel):
    title: str
    artist: str
    content: str
