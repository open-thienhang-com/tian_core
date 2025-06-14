from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class DataResponse(GenericModel, Generic[T]):
    message: str = Field(..., example="Success")
    data: Optional[T] = None

class PaginationMeta(BaseModel):
    total: int = Field(..., example=100)
    limit: int = Field(..., example=10)
    offset: int = Field(..., example=0)

class PaginatedResponse(GenericModel, Generic[T]):
    message: str = Field(..., example="List fetched successfully")
    data: List[T]
    meta: PaginationMeta

class ErrorResponse(GenericModel, Generic[T]):
    data: Optional[Union[T, List[T]]] = Field(
        default=None,
        description="Single item or list of results"
    )
    message: str = Field(..., description="Response message", example="Request failed")
    error: str = Field(..., description="Error message", example="Request failed")

# Success response model
class SuccessResponse(GenericModel, Generic[T]):
    data: Optional[Union[T, List[T]]] = Field(
        default=None,
        description="Single item or list of results"
    )
    message: str = Field(..., description="Success message")
    total: int = Field(..., example=1, description="Number of items")

DEFAULT_RESPONSES = {
    200: {
        "model": {},
        "description": "Request completed successfully.",
    },
    201: {"description": "Resource created successfully."},
    202: {"description": "Request accepted and is being processed."},
    204: {"description": "No content to return."},
    400: {
        "model": ErrorResponse,
        "description": "Bad request. The input data is invalid or malformed.",
    },
    500: {
        "model": ErrorResponse,
        "description": "error get meta data - id not found",
    },
    401: {
        "model": ErrorResponse,
        "description": "Unauthorized. Valid authentication is required."
    },
    403: {
        "model": ErrorResponse,
        "description": "Forbidden. You don't have permission to access this resource."
    },
    404: {
        "model": ErrorResponse,
        "description": "Not found. The requested resource does not exist."
    },
    409: {"description": "Conflict. Resource already exists or state conflict."},
    422: {"description": "Unprocessable Entity. Input failed validation checks."},
    502: {"description": "Bad gateway. Upstream service sent an invalid response."},
    503: {"description": "Service unavailable. The server is overloaded or down."},
    504: {"description": "Gateway timeout. Upstream service took too long to respond."},
}


def get_default_responses(success_model=None):
    responses = DEFAULT_RESPONSES.copy()
    if success_model:
        responses[200] = {
            "model": success_model,
            "description": "Request completed successfully.",
        }
    return responses