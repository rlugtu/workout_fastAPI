from typing import List
from fastapi import APIRouter, Depends
from prisma.models import Program
from Middleware import auth_user
from Config.ResponseHandler import APIResponse, ResponseModel
from .Dtos import CreateProgram, PutProgram
from .Service import get_all_programs, get_program, create_program, delete_program, update_program

router = APIRouter(prefix="/programs")

@router.get("/", response_model=ResponseModel[List[Program]])
async def get_all(user_id: str = Depends(auth_user)):
    response = await get_all_programs(user_id)
    return APIResponse(response)

@router.get("/{program_id}", response_model=ResponseModel[Program])
async def get_one(program_id: str, include_workouts: bool = False, user_id: str = Depends(auth_user)):
    response = await get_program(program_id, include_workouts, user_id)
    return APIResponse(response)

@router.post("/", response_model=ResponseModel[Program])
async def create(program: CreateProgram, user_id: str = Depends(auth_user)):
    response = await create_program(program, user_id)
    return APIResponse(response)

@router.put("/{program_id}", response_model=ResponseModel[Program])
async def update(program_id: str, program: PutProgram, user_id: str = Depends(auth_user)):
    response = await update_program(program_id, program, user_id)
    return APIResponse(response)


@router.delete("/{program_id}", response_model=ResponseModel[Program])
async def delete(program_id: str, user_id: str = Depends(auth_user)):
    response = await delete_program(program_id, user_id)
    return APIResponse(response)
