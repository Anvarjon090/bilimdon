from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime, Integer, ForeignKey

from datetime import datetime, date, timezone
from typing import List

from app.database import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))
    score: Mapped[int] = mapped_column(Integer, default=0)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="owned_games")
    questions: Mapped[List["GameQuestion"]] = relationship(back_populates="game")
    topic: Mapped["Topic"] = relationship("Topic", back_populates="games")
    participations: Mapped[List["Participation"]] = relationship(back_populates="game")