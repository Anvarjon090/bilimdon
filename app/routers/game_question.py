from fastapi import APIRouter, HTTPException
from app.database import *
from app.schemas.game import GameQuestionResponse, GameQuestionRequest
from app.models import GameQuestion
from app.deppendencies import *
from typing import List


router = APIRouter(tags=["GameQuestion"])


@router.get('/game_question', response_model=List[GameQuestionResponse])
async def get_all(
    db: db_dep, 
):
    game_questions = db.query(GameQuestion).all()
    return game_questions

@router.get('/game_question/{id}', response_model=GameQuestionResponse)
async def get_game_question(
    db: db_dep, 
    id: int
):
    game_question = db.query(GameQuestion).filter(GameQuestion.id == id).first()
    if not game_question:
        raise HTTPException(status_code=404, detail="GameQuestion not found")
    return game_question

@router.post('/game_question', response_model=GameQuestionResponse)
async def create_game_question(
    db: db_dep, 
    game_question: GameQuestionRequest
):
    new_game_question = GameQuestion(**game_question.model_dump())
    db.add(new_game_question)
    db.commit()
    db.refresh(new_game_question)

    return new_game_question


@router.put('/game_question/{id}', response_model=GameQuestionResponse)
async def update_game_question(
    db: db_dep, 
    id: int, 
    game_question: GameQuestionRequest
):
    
    existing_game_question = db.query(GameQuestion).filter(GameQuestion.id == id).first()

    if not existing_game_question:
        raise HTTPException(status_code=404, detail="GameQuestion not found")

    existing_game_question.title = game_question.title
    existing_game_question.description = game_question.description
    existing_game_question.start_time = game_question.start_time
    existing_game_question.end_time = game_question.end_time

    db.commit()


@router.delete('/game_question/{id}')
async def delete_game_question(
    db: db_dep, 
    id: int
):
    game_question = db.query(GameQuestion).filter(GameQuestion.id == id).first()
    if not game_question:
        raise HTTPException(status_code=404, detail="GameQuestion not found")
    db.delete(game_question)
    db.commit()

    return {"message": f"GameQuestion with id {id} deleted successfully"}