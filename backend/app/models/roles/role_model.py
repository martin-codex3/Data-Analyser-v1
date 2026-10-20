from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(str(50), nullable=False)
    created_date: Mapped[datetime] = mapped_column(default_factory=lambda: datetime.now)
