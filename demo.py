from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

# Assuming these are the async functions for fetching data
from .utilities.epic_fhir_endpoints import get_mrn_patient_detail, get_raw_mrn_patient_detail

app = FastAPI()

class PatientResponse(BaseModel):
    data: dict

class ErrorResponse(BaseModel):
    error: str

@app.get("/patient/{mrn}", response_model=PatientResponse, responses={404: {"model": ErrorResponse}})
async def patient_from_mrn(mrn: str):
    try:
        # Call the async function to get patient details
        res = await get_mrn_patient_detail(mrn)
    except KeyError as e:
        if str(e) == "'access_token'":
            raise HTTPException(status_code=404, detail="EPIC Server Error")
        raise HTTPException(status_code=404, detail=f"No Patient Found with MRN {mrn}")
    
    return PatientResponse(data=res)


@app.get("/raw-patient/{mrn}", response_model=PatientResponse, responses={404: {"model": ErrorResponse}})
async def raw_patient_from_mrn(mrn: str):
    try:
        # Call the async function to get raw patient details
        res = await get_raw_mrn_patient_detail(mrn)
    except KeyError as e:
        if str(e) == "'access_token'":
            raise HTTPException(status_code=404, detail="EPIC Server Error")
        raise HTTPException(status_code=404, detail=f"No Patient Found with MRN {mrn}")
    
    return PatientResponse(data=res)
