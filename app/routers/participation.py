from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.database import *
from app.schemas.participation import ParticipationResponse, ParticipationRequest
from app.models import Participation
from app.dependencies import *
from typing import List
from sqlalchemy.orm import Session



router = APIRouter(tags=["Participation"])


@router.get('/participation', response_model=List[ParticipationResponse])
async def get_all(
    db: db_dep,
    game_id: int = None,
    user_id: int = None,
):
    query = db.query(Participation)

    if game_id:
        query = query.filter(Participation.game_id == game_id)
    if user_id:
        query = query.filter(Participation.user_id == user_id)

    participations = query.all()

    return participations

@router.post("/participation", response_model=ParticipationResponse)
async def create_participation(
    participation: ParticipationRequest,
    db: Session = Depends(get_db)
):
    new_participation = Participation(
        user_id=participation.user_id,
        game_id=participation.game_id,
        gained_score=participation.gained_score,
        start_time=datetime.utc(), 
        end_time=datetime.utc(),
        registered_at=datetime.utc()
    )
    db.add(new_participation)
    db.commit()
    db.refresh(new_participation)
    return new_participation

@router.put('/participation/{id}', response_model=ParticipationResponse)
async def update_participation(
    db: db_dep,
    id: int,
    participation: ParticipationRequest
):
    existing_participation = db.query(Participation).filter(Participation.id == id).first()

    if not existing_participation:
        raise HTTPException(status_code=404, detail="Participation not found")

    existing_participation.game_id = participation.game_id
    existing_participation.user_id = participation.user_id
    existing_participation.status = participation.status

    db.commit()
    db.refresh(existing_participation)



@router.delete('/participation/{id}')
async def delete_participation(
    db: db_dep,
    id: int
):
    existing_participation = db.query(Participation).filter(Participation.id == id).first()

    if not existing_participation:
        raise HTTPException(status_code=404, detail="Participation not found")

    db.delete(existing_participation)
    db.commit()

    return {"message": f"Participation with id {id} deleted successfully"}