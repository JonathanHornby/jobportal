from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.database import get_db
from ..users import schemas, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags = ['Users']
)


@router.get("/", response_model=List[schemas.UserBase])
def get_users(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    jobs = db.query(models.User).limit(limit).all()
    
    if not jobs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No users found")
    return jobs