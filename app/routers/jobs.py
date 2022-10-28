from ..jobs import models, schemas
from .. import oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional

router = APIRouter(
    prefix="/jobs",
    tags = ['Jobs']
)

@router.get("/", response_model=List[schemas.JobOut])
async def get_jobs():
    pass