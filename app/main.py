from fastapi import FastAPI
from .routers import jobs, auth, users, recruiters
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from .recruiters import models
from .jobs import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

app.include_router(jobs.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(recruiters.router)