from typing_extensions import TypedDict


class CreateLiftExerciseActivity(TypedDict):
    sets: int
    reps: int
    weight: int
    notes: str
    liftExerciseId: str
    workoutId: str

class PutLiftExerciseActivity(TypedDict, total=False):
    sets: int
    reps: int
    weight: int
    notes: str
