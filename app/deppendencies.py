from typing import Annotated
from sqlalchemy.orm import sessionmaker, Session, SessionLocal
from sqlalchemy.ext.declarative import declarative_base  
from fastapi import Depends
from app.database import SessionLocal

Base = declarative_base()  

def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()


db_dep = Annotated[Session, Depends(get_db)]