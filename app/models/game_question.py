from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime, Integer, ForeignKey

from datetime import datetime, date, timezone
from typing import List

from app.database import Base

from app.models.question import Question  # type: ignore
from app.models.game import Game # type: ignore



class GameQuestion(Base):
    __tablename__ = "game_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))

    question: Mapped["Question"] = relationship(back_populates="games")
    game: Mapped["Game"] = relationship(back_populates="questions")