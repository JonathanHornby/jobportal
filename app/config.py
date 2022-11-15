from typing import List
import os
from pydantic import BaseSettings

class Settings(BaseSettings):

    # CORS
    CORS_ORIGINS: List[str] = ["*"]

    CORS_ALLOW_CREDENTIALS: bool = True

    CORS_ALLOW_METHODS: List[str] = ["*"]

    CORS_ALLOW_HEADERS: List[str] = ["*"]


    # DATABASE
    DATABASE_USERNAME: str #= os.environ.get('DATABASE_USERNAME')
    
    DATABASE_PASSWORD: str #= os.environ.get('DATABASE_PASSWORD')
    
    DATABASE_HOSTNAME: str #= os.environ.get('DATABASE_HOSTNAME')
    
    DATABASE_PORT: str #= os.environ.get('DATABASE_PORT')
    
    DATABASE_NAME: str #= os.environ.get('DATABASE_NAME')
    
    TEST_DATABASE_NAME: str = "jobsportal_test"


    # OAUTH
    SECRET_KEY: str #= os.environ.get('SECRET_KEY')
    
    ALGORITHM: str #= os.environ.get('ALGORITHM')
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int #= os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')
    
    # TEST
            
    TEST_USERNAME = "hello124@gmail.com"
    
    TEST_PASSWORD = "password123"

settings = Settings()