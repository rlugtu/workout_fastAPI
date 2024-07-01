
from typing_extensions import Optional, TypedDict


class CreateLiftExercise(TypedDict):
    name: str
    description: str
    userId: Optional[str]
