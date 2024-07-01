from typing import List
from fastapi.exceptions import HTTPException
from prisma.models import Program

from Config.Prisma_Connection import prisma_connection as prisma
from .Dtos import CreateProgram, PutProgram

async def get_all_programs(user_id: str) -> List[Program]:
    try:
        programs = await prisma.program.find_many(
            where={
                "userId": user_id
            }
        )

        return programs
    except Exception as e:
        raise HTTPException(status_code=404, detail={
            "error": f"{e}"
        })


async def get_program(program_id: str, include_workouts: bool, user_id:str) -> Program:
    try:
        return await prisma.program.find_unique(
            where={
                "id": program_id,
                "userId": user_id
            },
            include={
                "workouts": include_workouts
            }
        )

    except Exception as e:
        raise HTTPException(status_code=404, detail={
            "error": f"{e}"
        })


async def create_program(program: CreateProgram, user_id: str) -> Program:
    print(program, user_id)
    try:
        return await prisma.program.create(
            data={
                **program,
                "userId": user_id
            }
        )

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def update_program(program_id: str, program: PutProgram, user_id: str) -> Program:
    try:
        return await prisma.program.update(
            where={
                "id": program_id
            },
            data=program
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def delete_program(program_id: str, user_id: str) -> Program:
    try:
        return await prisma.program.delete(
            where={
                "id": program_id,
                "userId": user_id,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })
