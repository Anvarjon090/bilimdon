from fastapi import Depends, Request, HTTPException
from jose import jwt

from typing import Annotated
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.utils import *



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]





def get_current_user(
    request: Request,
    db: db_dep
):
    auth_header = request.headers.get("Authorization")
    is_bearer = auth_header.startswith("Bearer ") if auth_header else False
    token = auth_header.split(" ")[1] if auth_header else ""

    if not auth_header or not is_bearer:
        raise HTTPException(
            status_code=401,
            detail="You are not authenticated."
        )

    try:
        decoded_jwt = jwt.decode(
            token,
            SECRET_KEY,
            ALGORITHM
        )
        print(decoded_jwt)
        email = decoded_jwt.get("email")
        password = decoded_jwt.get("password")

        db_user = db.query(User).filter(User.email == email).first()

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        ) from e

    return db_user
