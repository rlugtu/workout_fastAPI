from fastapi.exceptions import HTTPException
from prisma.models import User
from Config.Prisma_Connection import prisma_connection as prisma

async def create_user(user_id: str) -> User:
    try:
        return await prisma.user.create(
            data={
                "id": user_id
            },
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail={
            "error": f"{e}"
        })
