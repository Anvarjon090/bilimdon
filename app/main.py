from typing import Union
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers.authr import router as auth_router
from app.routers.question import router as question_router
from app.routers.topic import router as topic_router
from app.routers.options import router as option_router

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(auth_router)
app.include_router(question_router)
app.include_router(topic_router)
app.include_router(option_router)