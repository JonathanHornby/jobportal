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
    DATABASE_USERNAME: str = os.environ.get('DATABASE_USERNAME')
    
    DATABASE_PASSWORD: str = os.environ.get('DATABASE_PASSWORD')
    
    DATABASE_HOSTNAME: str = os.environ.get('DATABASE_HOSTNAME')
    
    DATABASE_PORT: str = os.environ.get('DATABASE_PORT')
    
    DATABASE_NAME: str = os.environ.get('DATABASE_NAME')

settings = Settings()