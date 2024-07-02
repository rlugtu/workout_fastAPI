

from typing_extensions import List
from fastapi import Depends
from fastapi.routing import APIRouter
from prisma.models import LiftActivity

from Config.ResponseHandler import APIResponse, ResponseModel
from Middleware.Auth import auth_user
from Resources.Exercises.LiftActivities.Dtos import CreateLiftExerciseActivity
from Resources.Exercises.LiftActivities.Service import create_lift_exercise_activity, get_lift_activities_by_workout, get_single_lift_activities_by_workout


router = APIRouter(prefix="/liftActivities")

@router.get("/", response_model=ResponseModel[List[LiftActivity]])
async def get_all(workout_id: str, user_id: str = Depends(auth_user)):
    response = await get_lift_activities_by_workout(workout_id, user_id)
    return APIResponse(response)


@router.get("/{lift_exercise_activity_id}", response_model=ResponseModel[LiftActivity])
async def get_one(lift_exercise_activity_id: str, workout_id: str, user_id: str = Depends(auth_user)):
    response = await get_single_lift_activities_by_workout(lift_exercise_activity_id, workout_id, user_id)
    return APIResponse(response)


@router.post("/", response_model=ResponseModel[LiftActivity])
async def create(liftActivity: CreateLiftExerciseActivity, user_id: str = Depends(auth_user)):
    response = await create_lift_exercise_activity(liftActivity, user_id)
    return APIResponse(response)
