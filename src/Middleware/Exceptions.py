from fastapi import Request

from fastapi.responses import JSONResponse

async def exceptions_handler(request: Request, exc):
    return JSONResponse(
        content={
            "Internal Server Error": f"{exc}"
        }
    )
