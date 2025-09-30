from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMYY_DATABASE_URL = "sqlite:///./tabs.db"
engine = create_engine(SQLALCHEMYY_DATABASE_URL, connect_args={"check_same_thread": false})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
