from app.jobs import schemas as job_schemas
from . import testdata


# TEST POST JOBS

def test_post_job_recruiter_valid_token(authorized_recruiter):

    res = authorized_recruiter.post("/jobs/", json=testdata.job_data)
    new_job = job_schemas.JobDetail(**res.json())
    
    assert new_job.title == "First test job"
    assert new_job.id == 1
    assert res.status_code == 201
    
    
def test_post_job_recruiter_invalid_token(client):
    
    res = client.post("/jobs/", json=testdata.job_data)
    assert res.status_code == 401
    
    
def test_post_job_user_valid_token(authorized_user, client):
    
    res = client.post("/jobs/", json=testdata.job_data)
    assert res.status_code == 401
    
    
def test_post_job_user_invalid_token(client):
    
    res = client.post("/jobs/", json=testdata.job_data)
    assert res.status_code == 401
    
# TEST GET JOBS

def test_get_jobs(client, test_jobs):
    
    res = client.get("/jobs/")
    jobs = res.json()

    assert len(jobs) == 2
    assert res.status_code == 200
    
    
def test_get_job(client, test_jobs):
    
    res = client.get("/jobs/2")
    job = job_schemas.JobDetail(**res.json())
    
    assert job.id == 2
    assert job.title == "Second test job"
    assert res.status_code == 200
    
# TEST APPLY FOR JOB

def test_apply_job():
    pass


# TEST SAVE JOB

def test_save_job():
    pass