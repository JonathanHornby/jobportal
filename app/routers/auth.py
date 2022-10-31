from ctypes import util
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..auth import schemas as auth_schemas, oauth2
from ..database import database
from ..recruiters import models as recruiter_models, schemas as recruiter_schemas
from ..users import models as user_models, schemas as user_schemas
from .. import utils

router = APIRouter(
    prefix="/auth",
    tags=['Authentication'])


@router.post('/login_user', response_model=auth_schemas.Token)
def login_user(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    user = db.query(user_models.User).filter(user_models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login_recruiter', response_model=auth_schemas.Token)
def login_recruiter(recruiter_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    recruiter = db.query(recruiter_models.Recruiter).filter(recruiter_models.Recruiter.email == recruiter_credentials.username).first()

    if not recruiter:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    if not utils.verify_password(recruiter_credentials.password, recruiter.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    access_token = oauth2.create_access_token(data={"recruiter_id": recruiter.id})

    return {"access_token": access_token, "token_type": "bearer"}
