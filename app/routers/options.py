from fastapi import APIRouter, HTTPException, Response

from app.database  import * 
from app.schemas.model_schema import OptionResponse  , OptionRequest
from app.models import Option, Question

from app.deppendencies import *
from typing import List


router = APIRouter(tags=["Option"])


@router.post('/option', response_model=OptionResponse)
async def create_option(
    db: db_dep, 
    option: OptionRequest
):

    question = db.query(Question).filter(Question.id == option.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    new_option = Option(**option.dict())
    db.add(new_option)
    db.commit()
    db.refresh(new_option)

    return new_option



@router.get('/option', response_model=List[OptionResponse])
async def get_all(
    db: db_dep, 
):
    question = db.query(Option).all()

    return question



@router.put('/option/{id}', response_model=OptionResponse)
async def update_option(
    db: db_dep, 
    id: int, 
    option: OptionRequest
):
  
    existing_option = db.query(Option).filter(Option.id == id).first()

    if not existing_option:
        raise HTTPException(status_code=404, detail="Option not found")

  
    existing_option.title = option.title
    existing_option.is_correct = option.is_correct
    existing_option.question_id = option.question_id

   
    db.commit()
    db.refresh(existing_option)

    return existing_option




@router.delete('/option/{id}')
async def delete_option(
    db: db_dep, 
    id: int
   ):

    option_id = db.query(Option).filter(Option.id == id).first()
    if not option_id:
        raise HTTPException(status_code=404, detail="Option not found")
    db.delete(option_id)
    db.commit()
  

    return {"message":f"Option with id {id} deleted successfully"}