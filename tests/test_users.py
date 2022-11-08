from app.config import settings
from app.users import schemas as user_schemas
from app import utils


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
    
    
def test_delete_user():
    pass


def test_deactivate_user():
    pass


def test_reactivate_user():
    pass