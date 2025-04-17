from typing import Union
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from piccolo_admin.endpoints import create_admin
from app.tables import Book  
from app import settings


from app.routers.authr import router as auth_router
from app.routers.topic import router as topic_router
from app.routers.question import router as question_router

from app.routers.options import router as option_router
from app.routers.game import router as game_router
from app.routers.game_question import router as game_question_router
from app.routers.submission import router as submission_router
from app.routers.participation import router as participation_router
from app.routers.huma import router as huma_router
from db.connect_to_db import connect_to_db


#admin
app = FastAPI(title=settings.PROJECT_NAME)



app.include_router(auth_router)
app.include_router(topic_router)
app.include_router(question_router)
# Middleware for logging request and response
app.include_router(option_router)
app.include_router(game_router)
app.include_router(game_question_router)
app.include_router(submission_router)
app.include_router(participation_router)
app.include_router(huma_router)

#admin 
app.mount(settings.ADMIN_URL, create_admin([Book]))
