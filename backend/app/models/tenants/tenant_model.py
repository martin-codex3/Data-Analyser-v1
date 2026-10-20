import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(
        primary_key=True, default_factory=lambda: uuid.uuid4()
    )
    first_name: Mapped[str] = mapped_column(String(40), nullable=False)
    last_name: Mapped[str] = mapped_column(String(40), nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(String(50))
    nationality: Mapped[str] = mapped_column(nullable=False, index=True)
    email: Mapped[str] = mapped_column(nullable=False, index=True, unique=True)
    business_type: Mapped[str] = mapped_column(String(100))
    profile_image: Mapped[str | None] = mapped_column(String(50))
