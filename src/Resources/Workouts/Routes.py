from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from prisma.models import Workout
from Resources.Workouts.Dtos import CreateWorkout
from Resources.Workouts.Service import get_all_workouts, create_workout, get_workout
from Middleware import auth_user
from Config.ResponseHandler import APIResponse, ResponseModel

router = APIRouter(prefix="/workouts")

@router.get("/", response_model=ResponseModel[List[Workout]])
async def get_all(program_id: str, user_id: str = Depends(auth_user)):
    response = await get_all_workouts(program_id, user_id)
    return APIResponse(response)

@router.get("/{workout_id}", response_model=ResponseModel[Workout])
async def get_one(workout_id: str, user_id: str = Depends(auth_user)):
    response = await get_workout(workout_id, user_id)
    return APIResponse(response)

@router.post("/", response_model=ResponseModel[Workout])
async def create(workout: CreateWorkout, program_id: str, user_id: str = Depends(auth_user)):
    response = await create_workout(workout, program_id, user_id)
    return APIResponse(response)
