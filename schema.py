from pydantic import BaseModel

class SuccessResponse(BaseModel):
    data: dict

class ErrorResponse(BaseModel):
    detail: str

