from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str



class SingupSchema(BaseModel):
    firist_name: str
    last_name: str
    username: str
    email: str
    password: str
    birthdate: str