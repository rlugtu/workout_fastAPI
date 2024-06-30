from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from prisma.models import Workout
from Resources.Workouts.Dtos import CreateWorkout, PutWorkout
from Resources.Workouts.Service import delete_workout, get_all_workouts, create_workout, get_workout, update_workout
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


@router.put("/{workout_id}", response_model=ResponseModel[Workout])
async def update(workout_id: str, updatedWorkout: PutWorkout, user_id: str = Depends(auth_user)):
    response = await update_workout(workout_id, updatedWorkout, user_id)

    return APIResponse(response)


@router.delete("/{workout_id}", response_model=ResponseModel[Workout])
async def delete(workout_id: str, user_id: str = Depends(auth_user)):
    response = await delete_workout(workout_id, user_id)

    return APIResponse(response)
