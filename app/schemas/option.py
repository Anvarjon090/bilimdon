from pydantic import BaseModel, EmailStr
from datetime import datetime


class OptionRequest(BaseModel):
    question_id: int
    title: str
    is_correct:bool
   
   


class OptionResponse(BaseModel):
    id: int
    question_id: int
    title: str
    is_correct: bool
    created_at: datetime

    class Config:
        from_attributes = True