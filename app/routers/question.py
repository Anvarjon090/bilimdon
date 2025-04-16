from fastapi import APIRouter, HTTPException, Response

from app.database  import * 
from app.schemas.question import QuestionResponse, QuestionRequest
from app.models import Question 
from app.models import Topic 
from datetime import datetime
from app.dependencies import *
from typing import List
from app.dependencies import db_dep




router = APIRouter(tags=["Question"])

 
@router.post('/question', response_model=QuestionResponse)
async def create_question(
    db: db_dep,  # type: ignore
    question: QuestionRequest
):
    
    topic = db.query(Topic).filter(Topic.id == question.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")


    new_question = Question(
        owner_id=question.owner_id,
        title=question.title,
        description=question.description,
        topic_id=question.topic_id,
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return new_question

@router.get('/question', response_model=List[QuestionResponse])
async def get_all(
    db: db_dep,  # type: ignore
):
    question = db.query(Question).all()

    return question




@router.put('/question/{id}', response_model=QuestionResponse)
async def update_question(
    db: db_dep,  # type: ignore
    id: int, 
    question: QuestionRequest
):
    
    existing_question = db.query(Question).filter(Question.id == id).first()

 
    if not existing_question:
        raise HTTPException(status_code=404, detail="Question not found")

  
    existing_question.owner_id = question.owner_id
    existing_question.title = question.title
    existing_question.description = question.description
    existing_question.topic_id = question.topic_id

  
    db.commit()
    db.refresh(existing_question)

    return existing_question








@router.delete('/question/{id}')
async def delete_question(
    db: db_dep, 
    id: int
   ):

    option_id = db.query(Question).filter(Question.id == id).first()
    if not option_id:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(option_id)
    db.commit()
  

    return {"message":f"Question with id {id} deleted successfully"}