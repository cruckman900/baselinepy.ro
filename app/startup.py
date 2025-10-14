from app.database import Base, engine
from app.models import User, Project, Track, Tab, Comment, FileAsset # import all models to register them

def init_db():
    Base.metadata.create_all(bind=engine)