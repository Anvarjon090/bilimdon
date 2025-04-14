from pydantic import BaseModel
from datetime import datetime


class QuestionRequest(BaseModel):
    owner_id: int
    title: str
    description:str
    topic_id:int
   


class QuestionResponse(BaseModel):
    id: int
    owner_id: int
    topic_id: int
    title: str
    description: str

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
   