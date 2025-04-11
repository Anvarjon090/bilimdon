from typing import Union
import time
from datetime import datetime

from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

# from app.routers.authr import router as auth_router


router = APIRouter()

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

# app.include_router(auth_router)   