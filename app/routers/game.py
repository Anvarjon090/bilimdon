from fastapi import APIRouter, HTTPException, Response

from app.database  import *
from app.schemas.game import GameResponse, GameRequest
from app.models import Game
from app.deppendencies import db_dep
from typing import List
from datetime import datetime
from app.models import User


router = APIRouter(tags=["Game"])


@router.get('/game', response_model=List[GameResponse])
async def get_all(
    db: db_dep, 
):
    game = db.query(Game).all()

    return game


from datetime import datetime

@router.post('/game', response_model=GameResponse)      
async def create_game(
    db: db_dep, 
    game: GameRequest
):
    new_game = Game(
        **game.model_dump(),
        start_time=datetime.now(), 
        end_time=datetime.now()    
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game

@router.put('/game/{id}', response_model=GameResponse)
async def update_game(
    db: db_dep, 
    id: int, 
    game: GameRequest
):
    
    existing_game = db.query(Game).filter(Game.id == id).first()

    if not existing_game:
        raise HTTPException(status_code=404, detail="Game not found")

    existing_game.title = game.title
    existing_game.description = game.description
    existing_game.start_time = game.start_time
    existing_game.end_time = game.end_time

    db.commit()
    db.refresh(existing_game)

    return existing_game

@router.delete('/game/{id}')
async def delete_game(
    db: db_dep, 
    id: int
):
    game_id = db.query(Game).filter(Game.id == id).first()
    if not game_id:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game_id)
    db.commit()

    return {"message":f"Game with id {id} deleted successfully"}