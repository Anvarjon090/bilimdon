from tokenize import Special
from pydantic import BaseModel, EmailStr
from sqlalchemy import Boolean, Integer, Table
from piccolo.columns import Varchar


class AuthRegistration(BaseModel):
    last_name: str
    frist_name: str
    birthdate: int
    email: EmailStr
    password: str
    is_staff: bool
    is_superuser:bool
class AuthRegistrationResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_staff: bool
    is_superuser: bool

class AuthLogin(BaseModel):
    email: str
    password: str





