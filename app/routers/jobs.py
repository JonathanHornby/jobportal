from ..jobs import models, schemas
from ..auth import oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from ..auth.oauth2 import get_current_recruiter, get_current_user


router = APIRouter(
    prefix="/jobs",
    tags = ['Jobs']
)


@router.get("/", response_model=List[schemas.JobBasic])
def get_jobs(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    results = db.query(models.Job).limit(10).all()

    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No jobs found")
    return results


@router.get("/{id}", response_model=schemas.JobDetail)
def get_job(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id: {id} does not exist")
    return job


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.JobDetail)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db),
            recruiter_id: int = Depends(get_current_recruiter)):

    new_job = models.Job(
        poster_id = recruiter_id, **job.dict())
    
    if not new_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not all details provided")

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@router.post("/apply", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateJobApplication)
def apply_job(job_application: schemas.CreateJobApplication, db: Session = Depends(get_db),
              userid: int = Depends(get_current_user)):

    new_application = models.JobApplication(**job_application.dict())
    
    if not new_application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not all details provided")
    
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    
    return new_application


@router.post("/save", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateSavedJob)
def save_job(save_job: schemas.CreateSavedJob, db: Session = Depends(get_db),
              userid: int = Depends(get_current_user)):

    new_saved_job = models.SavedJob(user_id = userid, **save_job.dict())
    
    if not new_saved_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Error saving job")
    
    db.add(new_saved_job)
    db.commit()
    db.refresh(new_saved_job)
    
    return new_saved_job