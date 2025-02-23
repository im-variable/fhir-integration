import pytest
from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app

client = TestClient(app)  # Initialize the TestClient with the app

# Test case to check if patient data is fetched correctly
def test_patient_from_mrn():
    mrn = 202667  # The default value for MRN
    response = client.get(f"/patient/{mrn}")
    
    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Check the structure of the response
    data = response.json()
    assert "data" in data
    assert data["data"]["mrn_no"] == mrn

# Test case for an invalid MRN
def test_invalid_patient_mrn():
    mrn = 999999  # Invalid MRN
    response = client.get(f"/patient/{mrn}")
    
    # Check if the response status code is 404
    assert response.status_code == 404
    
    # Check if the correct error message is returned
    data = response.json()
    assert "detail" in data
    assert data["detail"] == f"No Patient Found with MRN {mrn}"

# Test case for `/raw/{mrn}`
def test_raw_patient_from_mrn():
    mrn = 202667  # Default MRN
    response = client.get(f"/patient/raw/{mrn}")
    
    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Check the structure of the response
    data = response.json()
    assert "data" in data
    assert data["data"]["total"] > 0

# Test case for invalid `/raw/{mrn}`
def test_invalid_raw_patient_mrn():
    mrn = 999999  # Invalid MRN
    response = client.get(f"/patient/raw/{mrn}")
    
    # Check if the response status code is 404
    assert response.status_code == 200
    
    # Check if the correct error message is returned
    data = response.json()
    assert "data" in data
    assert data["data"]["total"] == 0
