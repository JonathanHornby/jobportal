from ctypes import util
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..auth import schemas as auth_schemas, oauth2
from ..database import database
from ..recruiters import models as recruiter_models, schemas as recruiter_schemas
from ..seekers import models as seeker_models, schemas as seeker_schemas

router = APIRouter(
    prefix="/auth",
    tags=['Authentication'])

@router.post('/login_seeker', response_model=auth_schemas.Token)
def login_seeker(seeker_credentials: OAuth2PasswordRequestForm = Depends()):
    print("Auth")

@router.post('/login_recruiter', response_model=auth_schemas.Token)
def login_recruiter():
    print("Auth")

