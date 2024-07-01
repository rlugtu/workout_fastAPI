from typing_extensions import List, Optional
from fastapi.exceptions import HTTPException
from prisma.models import LiftExercise
from Resources.Exercises.LiftExercise.Dtos import CreateLiftExercise
from Config.Prisma_Connection import prisma_connection as prisma

async def get_all_lift_exercises(user_id: str) -> List[LiftExercise]:
    try:
        return await prisma.liftexercise.find_many()
    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })

async def get_single_lift_exercises(lift_id: str, user_id: str) -> LiftExercise:
    try:
        return await prisma.liftexercise.find_first_or_raise(
            where={
                "id": lift_id,

            }
        )

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def create_lift_exercise(exercise: CreateLiftExercise, user_id: Optional[str]) -> LiftExercise:
    try:
        return await prisma.liftexercise.create(
            data={
                **exercise,
                "userId": user_id
            }
        )

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


#ADMIN
async def delete_lift_exercise(lift_id: str):
    try:
        return await prisma.liftexercise.delete(
            where={
                "id": lift_id
            }
        )

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })
