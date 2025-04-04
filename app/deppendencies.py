from typing import Annotated
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base  
from fastapi import Depends

Base = declarative_base()  

def get_db():
    db = SessionLocal()  # type: ignore
    try:
        yield db
    finally:
        db.close()


db_dep = Annotated[Session, Depends(get_db)]