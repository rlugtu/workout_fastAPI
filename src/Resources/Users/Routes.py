from fastapi import Depends
from fastapi.routing import APIRouter
from prisma.models import User
from Config.ResponseHandler import APIResponse, ResponseModel
from Resources.Users.Service import create_user
from Middleware import auth_user

router = APIRouter(prefix="/users")

@router.post("/", response_model=ResponseModel[User])
async def create(user_id: str = Depends(auth_user)):
    response = await create_user(user_id)

    return APIResponse(response)
