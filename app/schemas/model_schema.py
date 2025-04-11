from pydantic import BaseModel, EmailStr
from datetime import datetime

class QuestionRequest(BaseModel):
    owner_id: int
    title: str
    description:str
    topic_id:int
   


class QuestionResponse(BaseModel):
    id:int
    owner_id: int
    title: str
    description:str
    topic_id:int
    created_at:datetime
   




class TopicRequest(BaseModel):
    name:str



class OptionRequest(BaseModel):
    question_id: int
    title: str
    is_correct:bool
   
   


class OptionResponse(BaseModel):
    id:int
    question_id: int
    title: str
    is_correct:str
    created_at:datetime
  