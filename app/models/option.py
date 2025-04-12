from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Boolean, String, DateTime, Integer, ForeignKey

from datetime import datetime, date, timezone
from typing import List

from app.database import Base

from app.models.question import Question  # type: ignore
from app.models.submission import Submission  # type: ignore

class Option(Base):
    __tablename__ = "options"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    title: Mapped[str] = mapped_column(String(100))
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    question = relationship("Question", back_populates="option_ids")
    submissions: Mapped[List["Submission"]] = relationship(back_populates="option")