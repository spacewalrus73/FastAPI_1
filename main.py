from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DATABASE DROPPED")
    await create_tables()
    print("DATABASE READY")
    yield
    print("APP OFF")


app = FastAPI(lifespan=lifespan)
app.include_router(router)
