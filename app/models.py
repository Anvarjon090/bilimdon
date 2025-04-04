from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped ,reconstructor
from datetime import datetime, date, timezone
from sqlalchemy import Date



from app.database import Base



class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(String(32), unique=True)
    firist_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate: Mapped[str] = mapped_column(Date)
    joined_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_stasff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)