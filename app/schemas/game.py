from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class GameRequest(BaseModel):
    owner_id: int
    title: str
    description: str
    topic_id: int
    score: int


class GameRequest(BaseModel):
    owner_id: int
    title: str
    description: str
    topic_id: int
    score: int
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    class Config:
        from_attributes = True