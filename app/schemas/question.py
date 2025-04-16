from pydantic import BaseModel

from datetime import datetime


class QuestionResponse(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str | None = None
    topic_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "owner_id": 1,
                "title": "Question 1",
                "description": "Question 1 description",
                "topic_id": 1,
                "created_at": "2021-01-01T00:00:00",
                "updated_at": "2021-01-01T00:00:00"
            }
        }
    }


class QuestionRequest(BaseModel):
    title: str
    description: str | None = None
    topic_id: int


class QuestionUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    topic_id: int | None = None