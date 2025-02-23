# Epic FHIR Integration with FastAPI

This guide provides instructions on setting up and running a FastAPI application that integrates with Epic FHIR.

## Prerequisites

Ensure you have the following installed:
- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- Pytest (for testing)

You can install the necessary dependencies using:
```sh
pip install fastapi uvicorn requests pytest
```

## Running the FastAPI Application

To start the FastAPI server, run:
```sh
uvicorn main:app --reload --port 7000
```

This will start the server on port `7000`. You can access the API documentation at:
- Swagger UI: [http://127.0.0.1:7000/docs](http://127.0.0.1:7000/docs)
- Redoc: [http://127.0.0.1:7000/redoc](http://127.0.0.1:7000/redoc)

## API Endpoints

Your FastAPI application should include endpoints to interact with Epic FHIR. Example endpoints might include:

- `GET /patient/raw/{patient_mrn_no}` - Retrieve patient raw information from patient resource
- `GET /patient/{patient_mrn_no}` - Retrieve patient details in a customized format

Ensure that your application correctly handles OAuth2 authentication with Epic's FHIR API.

## Running Tests

You can run tests using pytest:
```sh
pytest tests/
```

Ensure you have test cases defined in the `tests/` directory.
