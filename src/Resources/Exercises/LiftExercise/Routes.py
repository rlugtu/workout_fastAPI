from fastapi import Depends
from typing_extensions import List
from fastapi.routing import APIRouter
from prisma.models import LiftExercise

from Config.ResponseHandler import APIResponse, ResponseModel
from Middleware import auth_user
from Resources.Exercises.LiftExercise.Dtos import CreateLiftExercise
from Resources.Exercises.LiftExercise.Service import create_lift_exercise, delete_lift_exercise, get_all_lift_exercises, get_single_lift_exercises


router = APIRouter(prefix="/liftExercises")

@router.get("/", response_model=ResponseModel[List[LiftExercise]])
async def get_all(user_id: str = Depends(auth_user)):
    response = await get_all_lift_exercises(user_id)
    return APIResponse(response)

@router.get("/{lift_exercise_id}", response_model=ResponseModel[LiftExercise])
async def get_one(lift_exercise_id: str, user_id: str = Depends(auth_user)):
    response = await get_single_lift_exercises(lift_exercise_id, user_id)
    return APIResponse(response)

@router.post("/", response_model=ResponseModel[LiftExercise])
async def create(exercise: CreateLiftExercise, user_id: str = Depends(auth_user)):
    response = await create_lift_exercise(exercise, user_id)
    return APIResponse(response)


@router.delete("/", response_model=ResponseModel[LiftExercise])
async def delete(exercise_id: str, user_id: str = Depends(auth_user)):
    response = await delete_lift_exercise(exercise_id)
    return APIResponse(response)
