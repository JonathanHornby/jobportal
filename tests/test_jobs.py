from app.jobs import schemas as job_schemas


def test_post_job_recruiter_valid_token(authorized_recruiter, client):
    job_data = {
        "title": "First test job",
        "industry": "Test ",
        "category": "Test ",
        "summary": "Test ",
        "salary_min": 10000,
        "salary_max": 50000,
        "product_type": 1,
        "valid_duration": 30,
        "company": "Test Company",
        "country": "Australia",
        "state": "QLD",
        "city": "Brisbane",
        "employment_type": "Test ",
        "remote_status": "Test ",
        "salary_currency": "$",
        "content": "Test ",
        "contact_name": "Test name",
        "contact_number": "0491020584",
        "perk_car": True,
        "perk_visa": False,
        "perk_relocation": False,
        "perk_days_week": 5,
        "perk_phone": False,
        "perk_laptop": False,
        "perk_bonus": False
    }
    res = client.post("/jobs/", json=job_data)
    new_job = job_schemas.JobDetail(**res.json())
    
    assert new_job.title == "First test job"
    assert new_job.id == 1
    assert res.status_code == 201
    
def test_post_job_recruiter_invalid_token():
    pass
    
def test_post_job_user_valid_token():
    pass
    
def test_post_job_user_invalid_token():
    pass
    
    