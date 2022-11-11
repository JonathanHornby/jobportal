from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app import utils
from app.database.database import get_db
from ..users import schemas, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags = ['Users']
)


@router.get("/", response_model=List[schemas.UserBase])
def get_users(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    users = db.query(models.User).limit(limit).all()
    
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No users found")
    return users


@router.get("/{id}", response_model=schemas.UserDetail)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No users found")
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreated)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password    
    
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/cv/", status_code=status.HTTP_201_CREATED, response_model=schemas.CV)
def create_CV(cv: schemas.CVCreate, db: Session = Depends(get_db)):
    
    new_cv = models.Cv(**cv.dict())
    
    db.add(new_cv)
    db.commit()
    db.refresh(new_cv)
    
    return new_cv
    
    
@router.post("/coverletter/", status_code=status.HTTP_201_CREATED, response_model=schemas.CoverLetter)
def create_coverletter(coverletter: schemas.CreateCoverLetter, db: Session = Depends(get_db)):
    
    new_coverletter = models.CoverLetter(**coverletter.dict())
    
    db.add(new_coverletter)
    db.commit()
    db.refresh(new_coverletter)
    
    return new_coverletter