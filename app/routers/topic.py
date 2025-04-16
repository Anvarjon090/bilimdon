from typing import List
from fastapi import APIRouter, HTTPException

from app.database  import * 
from app.schemas.topic import TopicResponse , TopicRequest
from app.models import Topic

from app.dependencies import *


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

    existing_topic = db.query(Topic).filter(Topic.name == topic.name).first()
    if existing_topic:
        raise HTTPException(
            status_code=400,
            detail=f"Topic with name '{topic.name}' already exists."
        )


    new_topic = Topic(**topic.model_dump())
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