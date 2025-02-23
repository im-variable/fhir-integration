import pytest
from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app

client = TestClient(app)  # Initialize the TestClient with the app

# Test case to check authentication response
def test_authentication():
    response = client.get("/auth/token")
    
    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Check the structure of the response
    data = response.json()
    assert "data" in data
    assert data["data"]["token_type"] == "Bearer"

# # Test case for invalid authentication
# def test_invalid_authentication():
#     response = client.get("/auth/token")
    
#     # Check if the response status code is 400 (Bad Request)
#     assert response.status_code == 400
    
#     # Check if the correct error message is returned
#     data = response.json()
#     assert "detail" in data
#     assert data["detail"] == "Invalid credentials"
