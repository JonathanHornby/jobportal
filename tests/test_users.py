from app.config import settings
from app.users import schemas as user_schemas
from app import utils

# TEST USERS

def test_create_user(client):
    user_data = {
        "email": settings.TEST_USERNAME,
        "password": settings.TEST_PASSWORD
    }
    
    res = client.post("/users/", json=user_data)
    new_user = user_schemas.UserCreate(**res.json())
    
    assert res.status_code == 201
    assert new_user.email == user_data['email']
    assert utils.verify_password(user_data['password'], new_user.password)

    
def test_get_users(test_user, client):
    res = client.get("/users/1")

    assert res.json()['email'] == test_user['email']
    assert res.status_code == 200
    
    
def test_get_user(test_user, client):
    res = client.get("/users/")

    assert res.json()[0]['email'] == test_user['email']
    assert res.status_code == 200
    
    
def test_update_user():
    pass    
    
    
def test_delete_user():
    pass


def test_deactivate_user():
    pass


def test_reactivate_user():
    pass

# TEST CV

def test_create_cv(test_user, client):
    cv_data = {
        "user_id": test_user['id'],
        "name": "Test CV"
    }
    
    res = client.post("/users/cv/", json=cv_data)
    new_cv = user_schemas.CV(**res.json())
    
    assert res.status_code == 201
    assert new_cv.name == "Test CV"

def test_delete_cv():
    pass


def test_update_cv():
    pass

# TEST COVER LETTER

def test_create_cover_letter(test_user, client):
    coverletter_data = {
        "user_id": test_user['id'],
        "name": "Test Cover Letter"
    }
    
    res = client.post("/users/coverletter/", json=coverletter_data)
    new_coverletter = user_schemas.CreateCoverLetter(**res.json())
    
    assert res.status_code == 201
    assert new_coverletter.name == "Test Cover Letter"


def test_delete_cover_letter():
    pass


# def test_update_cover_letter():
#     pass