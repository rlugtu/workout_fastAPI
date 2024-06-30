import datetime
from typing import Optional
from typing_extensions import TypedDict

class CreateWorkout(TypedDict):
    name: str
    description: str
    endDate: Optional[datetime.datetime]

class PutProgram(TypedDict, total=False):
    name: str
    description: str
    endDate: Optional[datetime.datetime]
