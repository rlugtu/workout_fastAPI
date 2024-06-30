from fastapi import  HTTPException
import os
from jose import jwt
from starlette.requests import Request

CLERK_PEM_PUBLIC_KEY = (os.getenv("NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY") or "").replace('\\n', '\n')

async def auth_user(
    request: Request,
):
    try:
        tokenAuth = request.headers.get('authorization')
        if tokenAuth:
            token = tokenAuth[7:]
            user = jwt.decode(token, CLERK_PEM_PUBLIC_KEY, algorithms='RS256')
            if 'sub' in user:
                return user['sub']

        if request._cookies and request._cookies['__session']:
            session_token = request._cookies['__session']

            user = jwt.decode(session_token, CLERK_PEM_PUBLIC_KEY, algorithms='RS256')
            if 'sub' in user:
                return user['sub']
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
