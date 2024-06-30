from typing_extensions import Generic, TypeVar
from pydantic import BaseModel
from typing import Optional

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    data: Optional[T]


def APIResponse(data: T = None) -> ResponseModel[T]:
    return ResponseModel(data=data)
