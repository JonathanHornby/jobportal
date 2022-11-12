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
    
    
# TEST UPDATE AND DELETE JOBS

def test_update_job():
    pass


def test_delete_job():
    pass    

    
# TEST APPLY FOR JOB

def test_apply_job(authorized_user, test_user, test_jobs, test_cv, test_cover_letter):
    
    application_data = testdata.job_application
    application_data['user_id'] = test_user['id']
    res = authorized_user.post("/jobs/apply", json=application_data)

    new_application = job_schemas.CreateJobApplication(**res.json())
    
    assert res.status_code == 201
    assert new_application.job_id == testdata.job_application['job_id']


# # TEST SAVE JOB

# def test_save_job():
#     pass