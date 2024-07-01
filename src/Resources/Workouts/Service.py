from typing_extensions import List
from fastapi.exceptions import HTTPException
from prisma.models import Workout
from Config.Prisma_Connection import prisma_connection as prisma
from Resources.Workouts.Dtos import CreateWorkout, PutWorkout

async def get_all_workouts(program_id: str, user_id: str) -> List[Workout]:
    try:
        print(program_id, user_id)
        program = await prisma.program.find_first_or_raise(
            where={
                "id": program_id,
                "userId": user_id
            },
            include={
                "workouts": True
            }
        )

        return program.workouts or []

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def get_workout(workout_id: str, user_id: str) -> Workout:
    try:
        workout = await prisma.workout.find_first_or_raise(
            where={
                "id": workout_id,
            },
            include={
                "program": True
            }
        )
        # print(workout.program is not None, workout.program.userId)
        if workout.program is not None and workout.program.userId !=  user_id:
            raise HTTPException(status_code=403, detail={
                "error": "Not authorized to access this resource"
            })
        workout.program = None

        return workout

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def create_workout(workout: CreateWorkout, program_id: str, user_id: str) -> Workout:
    try:
        program = await prisma.program.find_first(
            where={
                "id": program_id,
                "userId": user_id
            }
        )

        if program is None:
            raise HTTPException(status_code=403, detail={
                "error": "Not authorized to access this resource"
            })

        return await prisma.workout.create(
            data={
                **workout,
                "programId": program_id
            }
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def update_workout(workout_id: str, updatedWorkout: PutWorkout, user_id:str) -> Workout:
    try:
        workout = await prisma.workout.find_first_or_raise(
            where={
                "id": workout_id,
            },
            include={
                "program": True
            }
        )

        if workout.program and workout.program.userId != user_id:
            raise HTTPException(status_code=403, detail={
                "error": "Not authorized to access this resource"
            })

        response = await prisma.workout.update(
            where={
                "id": workout.id
            },
            data={
                **updatedWorkout
            }
        )

        if response is None:
            raise HTTPException(status_code=422, detail={
                "error": "Error updating workout"
            })

        return response

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })


async def delete_workout(workout_id: str, user_id: str) -> Workout:
    try:
        workout = await prisma.workout.find_first_or_raise(
            where={
                "id": workout_id,
            },
            include={
                "program": True
            }
        )

        if workout.program is not None and workout.program.userId !=  user_id:
            raise HTTPException(status_code=403, detail={
                "error": "Not authorized to access this resource"
            })
        workout.program = None

        response = await prisma.workout.delete(
            where={
                "id": workout.id
            }
        )

        if response is None:
            raise HTTPException(status_code=422, detail={
                "error": "Error deleting workout"
            })

        return response

    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })
