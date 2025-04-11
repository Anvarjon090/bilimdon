from typing import List
from fastapi import APIRouter, HTTPException, Response

from app.database  import * 
from app.schemas.model_schema import TopicRequest, TopicResponse
from app.models import Question , Topic

from app.deppendencies import *


router = APIRouter(tags=["Topic"])


@router.get('/topic', response_model=List[TopicResponse]) 
async def get_all(
    db: db_dep, 
):
    topic = db.query(Topic).all()

    return topic


@router.post('/topic', response_model=TopicResponse)
async def create_topic(
    db: db_dep, 
    topic: TopicRequest
   ):
    new_topic = Topic(**topic.dict())

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic




@router.delete('/topic/{id}')
async def delete_topic(
    db: db_dep, 
    id: int
   ):

    topic_id = db.query(Topic).filter(Topic.id == id).first()
    if not topic_id:
        raise HTTPException(status_code=404, detail="Topic not found")
    db.delete(topic_id)
    db.commit()
  

    return {"message":f"Topic with id {id} deleted successfully"}