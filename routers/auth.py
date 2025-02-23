from fastapi import APIRouter, HTTPException
from starlette import status
from utilities.epic_fhir_config import get_auth2_response
from schema import SuccessResponse, ErrorResponse

router = APIRouter()

@router.get("/token", 
            response_model=SuccessResponse, 
            responses={404: {"model": ErrorResponse}},
            summary="Authenticate using OAuth2",
            description="This endpoint allows us to authenticate using OAuth2.0 and obtain an access token. If an error occurs, it returns a 404 error with an appropriate message."
            )
async def authenticate_auth2():
    """
    Authenticate using OAuth2.

    This endpoint retrieves the authentication token using OAuth2. 
    If successful, it returns the token in the response. If an error occurs, 
    it raises a 404 error indicating either a missing access token or a generic issue.
    
    Responses:
      - 200: Returns the access token in a SuccessResponse model.
      - 404: Returns an ErrorResponse model with an appropriate error message when an issue occurs.
    """
    try:
        # Call the async function to get the auth2 response
        res = get_auth2_response()
    except KeyError as e:
        if str(e) == "'access_token'":
            raise HTTPException(status_code=404, detail="EPIC Server Error")
        raise HTTPException(status_code=404, detail="Something went wrong")
    
    return SuccessResponse(data=res, status=status.HTTP_200_OK)
