from pydantic import BaseModel
from datetime import datetime


class SubmissionRequest(BaseModel):
    user_id: int
    question_id: int
    option_id: int
    game_id: int  
    owner_id: int  
    is_correct: bool

class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    question_id: int
    option_id: int
    created_at: datetime
    is_correct: bool

    class Config:
        from_attributes = True