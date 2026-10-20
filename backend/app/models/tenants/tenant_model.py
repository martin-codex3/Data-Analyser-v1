import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role_model import Role


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
    roles: Mapped[list["Role"]] = relationship(back_populates="tenant")
