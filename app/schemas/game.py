from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class GameRequest(BaseModel):
    owner_id: int
    title: str
    description: str
    topic_id: int
    score: int


class GameResponse(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    topic_id: int
    score: int
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    class Config:
        from_attributes = True


class GameQuestionRequest(BaseModel):
    game_id: int
    question_id: int
    


class GameQuestionResponse(BaseModel):
    id: int
    game_id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True