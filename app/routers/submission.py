from fastapi import APIRouter, HTTPException
from app.database import *
from app.schemas.submission import SubmissionResponse, SubmissionRequest
from app.models import Submission
from app.deppendencies import *
from typing import List
from sqlalchemy.orm import Session



router = APIRouter(tags=["Submission"])


@router.get('/submission', response_model=List[SubmissionResponse])
async def get_all(
    db: db_dep
):
    query = db.query(Submission)

    submissions = query.all()

    return submissions


@router.post('/submission', response_model=SubmissionResponse)
async def create_submission(
    db: db_dep,
    submission: SubmissionRequest
):
    new_submission = Submission(**submission.model_dump())
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission


@router.put('/submission/{id}', response_model=SubmissionResponse)
async def update_submission(
    db: db_dep,
    id: int,
    submission: SubmissionRequest
):
    existing_submission = db.query(Submission).filter(Submission.id == id).first()

    if not existing_submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    existing_submission.game_id = submission.game_id
    existing_submission.question_id = submission.question_id
    existing_submission.user_id = submission.user_id
    existing_submission.answer = submission.answer

    db.commit()
    db.refresh(existing_submission)

    return existing_submission



@router.delete('/submission/{id}')
async def delete_submission(
    db: db_dep,
    id: int
):
    submission = db.query(Submission).filter(Submission.id == id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    db.delete(submission)
    db.commit()

    return {"message": f"Submission with id {id} deleted successfully"}