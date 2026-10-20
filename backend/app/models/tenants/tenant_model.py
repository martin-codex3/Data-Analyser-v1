import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tenant_roles.tenant_roles import tenant_roles
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role_model import Role


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    first_name: Mapped[str] = mapped_column(
        String(40),
    )
    last_name: Mapped[str] = mapped_column(
        String(40),
    )
    phone_number: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column(String(50))
    nationality: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    business_type: Mapped[str] = mapped_column(String(100))
    profile_image: Mapped[str] = mapped_column(String(50), nullable=True)
    roles: Mapped[list["Role"]] = relationship(
        secondary=tenant_roles, back_populates="tenants"
    )
