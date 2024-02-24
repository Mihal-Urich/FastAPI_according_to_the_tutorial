from fastapi import FastAPI
from data_base import create_tables, dalete_tables
from contextlib import asynccontextmanager
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await dalete_tables()
    print("Base clean")
    await create_tables()
    print("Base already")
    yield
    print("Base Off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

