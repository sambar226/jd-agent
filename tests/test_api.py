from fastapi.testclient import TestClient
from main import app

# TestClient allows us to simulate HTTP requests without starting a real server
client = TestClient(app)

def test_health_check():
    """Verify the API is up and running."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "JD Prep Agent"}

def test_jd_length_validation():
    """Verify that Pydantic blocks job descriptions that are too short."""
    payload = {"job_description": "We need a Python developer."} # Only 27 characters
    response = client.post("/api/v1/analyse", json=payload)
    
    # We expect a 422 Unprocessable Entity because our Pydantic min_length is 50
    assert response.status_code == 422
