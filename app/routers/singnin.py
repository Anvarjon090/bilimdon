from typing import Annotated

import jwt
from sqlalchemy import select
from fastapi import APIRouter, status as http_status, HTTPException, Request, Depends
from sqlalchemy.orm import Session

from app.schema.login import SingupSchema
from dependencies import get_db
from schemas.login import LoginSchema
from schemas.users import UserSchema
from models import User


router = APIRouter(
    prefix="/authentication", 
    tags=["Authentication"],
)

@router.post(
        "/signup",
    name = "Signup" Endpoint,
)

def signup(
    singup_daeta: SingupSchema,
    db_session: Annotated[Session, Depends(get_db)],
):

    data = singup_daeta.model_dump()
    data['hashes_password'] = hashed_password

    data.pop("password")

    try:
        entry = User(**data)
        db_session.add(entry)
        db_session.commit()
    except Exception as e:
        raise e
    
    data.pop("hashes_password")
    access_tokin = jwt.encode(data, "secret", algorithm="HS256")

    return {"detal": data, "token": access_tokin}   

@router.post(
    path="/signin",
    response_model=""
)
def signin(
    login_payload: LoginSchema,
    db_session: Annotated[Session, Depends(get_db)],
):
    username = login_payload.username
    # password = login_payload.password
    
    user_stmt = select(User).where(User.username == username)
    # user = db_session.execute(user_stmt).scalar_one_or_none()
    user_query = db_session.execute(user_stmt).first()


    if user_query is None:
        return HTTPException(status_code=404, detail="User not found")
    
    user = user_query[0]

    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # "birthdate": user.birthdate
    }
    
    user_data = UserSchema.model_validate(user_dict)

    user_data_payload = user_data.model_dump()
    
    access_token = jwt.encode(user_data_payload, "secret", algorithm="HS256")
    
    return {"jwt": access_token}
