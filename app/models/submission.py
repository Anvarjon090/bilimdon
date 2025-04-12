from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Boolean, DateTime, Integer, ForeignKey

from datetime import datetime, timezone

from app.database import Base
from app.models.question import Question  # type: ignore
from app.models.option import Option  # type: ignore
from app.models.user import User  # type: ignore



class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
    option_id: Mapped[int] = mapped_column(Integer, ForeignKey("options.id"))
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    owner = relationship("User", back_populates="submissions")
    question = relationship("Question", back_populates="submissions")
    option = relationship("Option", back_populates="submissions")