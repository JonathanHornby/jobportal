from fastapi import HTTPException, status
from app.auth import schemas as auth_schemas, oauth2
from app.config import settings
    
def test_login_user(test_user, client):
    
    login_data = {
        "username": "hello124@gmail.com",
        "password": "password123"
    }
    client.headers['content-type'] = "application/x-www-form-urlencoded"
    
    res = client.post("/auth/login_user", login_data)
    token = res.json()
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail=f'Could not validate credentials',
                                        headers={"WWW-Authenticate": "Bearer"})
    
    assert res.status_code == 200
    assert token['token_type'] == 'bearer'
    assert oauth2.verify_acccess_token(token['access_token'], credentials_exception)
       

def test_incorrect_username(test_user, client):
    
    login_data = {
        "username": "Wrongusername",
        "password": "password123"
    }
    client.headers['content-type'] = "application/x-www-form-urlencoded"
    
    res = client.post("/auth/login_user", login_data)
    token = res.json()
    
    assert res.status_code == 403


def test_incorrect_password(test_user, client):
    
    login_data = {
        "username": "hello124@gmail.com",
        "password": "Wrongpassword"
    }
    client.headers['content-type'] = "application/x-www-form-urlencoded"
    
    res = client.post("/auth/login_user", login_data)
    token = res.json()
    
    assert res.status_code == 403
