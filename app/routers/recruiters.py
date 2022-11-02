from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.database import get_db
from ..recruiters import schemas, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/recruiters",
    tags = ['Recruiters']
)


@router.get("/", response_model=List[schemas.RecruiterBase])
def get_recruiters(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    recruiters = db.query(models.Recruiter).limit(limit).all()
    
    if not recruiters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No recruiters found")
    return recruiters


@router.get("/{id}", response_model=schemas.RecruiterDetail)
def get_recruiter(id: int, db: Session = Depends(get_db)):
    recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == id).first()
    
    if not recruiter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No recruiters found")
    return recruiter


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RecruiterCreate)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(get_db)):
    
    new_recruiter = models.Recruiter(**recruiter.dict())

    db.add(new_recruiter)
    db.commit()
    db.refresh(new_recruiter)

    return new_recruiter