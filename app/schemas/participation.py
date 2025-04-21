from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ParticipationRequest(BaseModel):
    user_id: int
    
    gained_score: int


   
class ParticipationResponse(BaseModel):
    id: int
    user_id: int
    game_id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    gained_score: int
    registered_at: datetime

    class Config:
        from_attributes = True
