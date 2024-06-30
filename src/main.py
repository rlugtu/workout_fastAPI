from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Config import prisma_connection
from prisma import Prisma

from Middleware.Exceptions import exceptions_handler
from Resources.Programs import router as programs_router
from Resources.Workouts import router as workouts_router

app = FastAPI()
prisma = Prisma()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, exceptions_handler)

app.include_router(programs_router)
app.include_router(workouts_router)

@app.on_event("startup")
async def startup():
    await prisma_connection.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma_connection.disconnect()
