import pytest
from sqlalchemy import create_engine
from app.auth.oauth2 import create_access_token
from app.auth import schemas as auth_schemas
from app.jobs.schemas import JobCreate
from app.jobs import models as job_models
from app.users import models as user_models
from app.users import schemas as user_schemas
from app.main import app
from app.config import settings
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.database.database import Base, get_db
from tests import testdata

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.TEST_DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# DATABASE / SESSION

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

# TEST USER / RECRUITER    

@pytest.fixture
def test_user(client):
    """Take a client fixture, create a user in a test DB, return the created user object"""
    user_data = {
        "email": settings.TEST_USERNAME,
        "password": settings.TEST_PASSWORD
    }
    
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_recruiter(client):
    """Take a client fixture, create a recruiter in a test DB, return the created recruiter object"""
    recruiter_data = {
        "email": settings.TEST_USERNAME,
        "password": settings.TEST_PASSWORD
    }
    
    res = client.post("/recruiters/", json=recruiter_data)
    
    assert res.status_code == 201
    
    new_recruiter = res.json()
    new_recruiter['password'] = recruiter_data['password']
    return new_recruiter

# TOKENS

@pytest.fixture
def user_token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def recruiter_token(test_recruiter):
    return create_access_token({"user_id": test_recruiter['id']})


# AUTHORIZED USERS

@pytest.fixture
def authorized_recruiter(client, recruiter_token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {recruiter_token}"
    }
    
    return client


@pytest.fixture
def authorized_user(client, user_token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {user_token}"
    }
    
    return client

# JOBS

@pytest.fixture
def test_jobs(authorized_recruiter, session):
    
    def create_jobs_model(job):
        job['poster_id'] = 1
        return job_models.Job(**job)
    
    job_map = map(create_jobs_model, testdata.jobs_data)
    jobs = list(job_map)
    
    session.add_all(jobs)
    session.commit()
    
    jobs = session.query(job_models.Job).all()
    return jobs

# CV    

@pytest.fixture
def test_cv(client, test_user):
    cv_data = {
        "user_id": test_user['id'],
        "name": "Test CV"
    }
    
    res = client.post("/users/cv/", json=cv_data)
    new_cv = user_schemas.CV(**res.json())
    
    return new_cv

# COVERLETTER

@pytest.fixture
def test_cover_letter(client, test_user):
    coverletter_data = {
        "user_id": test_user['id'],
        "name": "Test Cover Letter"
    }
    
    res = client.post("/users/coverletter/", json=coverletter_data)
    new_coverletter = user_schemas.CoverLetter(**res.json())
    
    return new_coverletter