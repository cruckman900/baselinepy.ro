from sqlmodel import create_engine, SQLModel
from app.config import settings

engine = create_engine(settings.DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)