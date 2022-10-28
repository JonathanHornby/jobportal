from ..jobs import models, schemas
from ..auth import oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional

router = APIRouter(
    prefix="/jobs",
    tags = ['Jobs']
)

# TODO: set limit by settings
#  change search to a search object
@router.get("/", response_model=List[schemas.JobBase])
def get_jobs(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    results = db.query(models.Job).limit(10).all()

    return results

@router.get("/{id}", response_model=schemas.JobDetail)
def get_job(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id: {id} does not exist")
    return job

# TODO: get recruiter_id from oauth
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.JobCreate)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db),
            recruiter_id: int = 1):
    new_job = models.Job(
        recruiter_id = 1, **job.dict())

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
