from fastapi.exceptions import HTTPException
from Config.Prisma_Connection import prisma_connection as prisma
from Resources.Exercises.LiftActivities.Dtos import CreateLiftExerciseActivity

async def get_lift_activities_by_workout(workout_id: str, user_id: str):
    try:
        return await prisma.liftactivity.find_many(
            where={
                "workout": {
                    "is": {
                        "id": workout_id,
                        "program": {
                            "is": {
                                "userId": user_id
                            }

                        }
                    }
                }
            },
            include={
                "liftExercise": True
            }
        )

    except Exception as e:
            raise HTTPException(status_code=404, detail={
                "error": f"{e}"
            })


async def get_single_lift_activities_by_workout(lift_activity_id: str,workout_id: str, user_id: str):
    try:
        return await prisma.liftactivity.find_first_or_raise(
            where={
                "id": lift_activity_id,
                "workout": {
                    "is": {
                        "id": workout_id,
                        "program": {
                            "is": {
                                "userId": user_id
                            }

                        }
                    }
                }
            },
            include={
                "liftExercise": True
            }
        )

    except Exception as e:
            raise HTTPException(status_code=404, detail={
                "error": f"{e}"
            })


async def create_lift_exercise_activity(activity: CreateLiftExerciseActivity, user_id: str):
    try:
        await prisma.workout.find_first_or_raise(
            where={
                "id": activity["workoutId"],
                "program": {
                    "is": {
                        "userId": user_id
                    }
                }
            },
        )

        return await prisma.liftactivity.create(
            data={
                **activity
            }
        )

    except Exception as e:
            raise HTTPException(status_code=422, detail={
                "error": f"{e}"
            })
