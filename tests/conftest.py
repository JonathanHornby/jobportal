import pytest
from sqlalchemy import create_engine
from app.auth.oauth2 import create_access_token
from app.auth import schemas as auth_schemas
from app.main import app
from app.config import settings
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.database.database import Base, get_db

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.TEST_DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


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
    

@pytest.fixture
def test_user(client):
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
    recruiter_data = {
        "email": settings.TEST_USERNAME,
        "password": settings.TEST_PASSWORD
    }
    
    res = client.post("/recruiters/", json=recruiter_data)
    
    assert res.status_code == 201
    
    new_recruiter = res.json()
    new_recruiter['password'] = recruiter_data['password']
    return new_recruiter


@pytest.fixture
def user_token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def recruiter_token(test_recruiter):
    return create_access_token({"user_id": test_recruiter['id']})


@pytest.fixture
def authorized_user():
    pass


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
