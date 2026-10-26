import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base import Base


class ApplicationUser(Base):
    __tablename__ = "application_users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(20), index=True)
