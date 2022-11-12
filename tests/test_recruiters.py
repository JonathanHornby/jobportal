from app.config import settings
from app.recruiters import schemas as recruiter_schemas
from app import utils


def test_create_recruiter(client):
    recruiter_data = {
        "email": settings.TEST_USERNAME,
        "password": settings.TEST_PASSWORD
    }
    
    res = client.post("/recruiters/", json=recruiter_data)
    new_recruiter = recruiter_schemas.RecruiterCreate(**res.json())
    
    assert res.status_code == 201
    assert new_recruiter.email == recruiter_data['email']
    assert utils.verify_password(recruiter_data['password'], new_recruiter.password)


def test_get_recruiter(test_recruiter, client):
    res = client.get("/recruiters/1")

    assert res.json()['email'] == test_recruiter['email']
    assert res.status_code == 200
    
    
def test_get_recruiters(test_recruiter, client):
    res = client.get("/recruiters/")

    assert res.json()[0]['email'] == test_recruiter['email']
    assert res.status_code == 200


def test_update_recruiter():
    pass


def test_delete_recruiter():
    pass

    
def test_deactivate_recruiter():
    pass


def test_reactivate_recruiter():
    pass