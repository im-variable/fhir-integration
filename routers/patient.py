from fastapi import APIRouter, HTTPException, Path
from starlette import status
from pydantic import BaseModel
from utilities.epic_fhir_endpoints import get_mrn_patient_detail, get_raw_mrn_patient_detail
from schema import SuccessResponse, ErrorResponse

router = APIRouter()

@router.get(
    "/raw/{mrn}",
    response_model=SuccessResponse,
    responses={404: {"model": ErrorResponse}},
    summary="Retrieve raw data for a patient by MRN",
    description="This endpoint retrieves raw data for a patient based on their MRN (Medical Record Number). "
                "It includes unprocessed, detailed patient records, which can be useful for analytics or further data processing.",
)
async def raw_patient_from_mrn(
    mrn: int = Path(
        title="MRN (Medical Record Number)",  # Title in the Swagger UI
        description="The MRN of the patient to retrieve raw data for.",  # Description in the Swagger UI
    )
):
    """
    Retrieve raw data for a patient by MRN.

    This endpoint allows you to retrieve raw patient data using their MRN.
    - If the MRN is not found, a 404 error is returned.
    - If there is an issue with the access token, a 404 error indicating 'EPIC Server Error' is returned.

    Responses:
      - 200: Returns raw data for the patient if successful.
      - 404: Returns an error message if the MRN is not found or if there is an EPIC Server error.
    """
    try:
        # Call the async function to get raw patient details
        res = await get_raw_mrn_patient_detail(mrn)
    except KeyError as e:
        if str(e) == "'access_token'":
            raise HTTPException(status_code=404, detail="EPIC Server Error")
        raise HTTPException(status_code=404, detail=f"No Patient Found with MRN {mrn}")
    
    return SuccessResponse(data=res, status=status.HTTP_200_OK)


@router.get(
    "/{mrn}",
    response_model=SuccessResponse,
    responses={404: {"model": ErrorResponse}},
    summary="Retrieve patient details by MRN",
    description="This endpoint retrieves detailed patient data based on their MRN (Medical Record Number). "
                "The response typically includes patient information in a customized format.",
)
async def patient_from_mrn(
    mrn: int = Path(
        title="MRN (Medical Record Number)",  # Title in the Swagger UI
        description="The MRN of the patient to retrieve patient data for.",  # Description in the Swagger UI
    )
):
    """
    Retrieve detailed patient data by MRN.

    This endpoint retrieves detailed patient data based on the MRN.
    - If the MRN is not found, a 404 error is returned.
    - If there is an issue with the access token, a 404 error indicating 'EPIC Server Error' is returned.

    Responses:
      - 200: Returns detailed patient data if successful.
      - 404: Returns an error message if the MRN is not found or if there is an EPIC Server error.
    """
    try:
        # Call the async function to get patient details
        res = await get_mrn_patient_detail(mrn)
    except KeyError as e:
        if str(e) == "'access_token'":
            raise HTTPException(status_code=404, detail="EPIC Server Error")
        raise HTTPException(status_code=404, detail=f"No Patient Found with MRN {mrn}")
    
    return SuccessResponse(data=res, status=status.HTTP_200_OK)
