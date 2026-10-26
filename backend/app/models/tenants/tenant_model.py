import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.application_users.application_user import ApplicationUser
from app.models.tenant_users.tenant_user import tenant_users
from app.utils.base import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    business_name: Mapped[str] = mapped_column(String(255))
    business_type: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    nationality: Mapped[str] = mapped_column(index=True)
    users: Mapped[list["ApplicationUser"]] = relationship(
        secondary=tenant_users, back_populates="tenants", lazy="selectin"
    )
